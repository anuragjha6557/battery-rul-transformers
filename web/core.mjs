// Browser port of src/battery_rul/serve/predictor.py (pre/post-processing around the ONNX graphs).
// Must stay numerically identical to Python: tests/web/test_core.mjs checks it against
// vectors produced by scripts/export_onnx.py from the Python predictor.

export class InputError extends Error {}

const MAX_CYCLES = 20000;

/** Parse CSV text into {cycle_idx: number[], capacity_ah: number[]} (header names case-insensitive). */
export function parseCSV(text) {
  const lines = text.replace(/\r/g, "").split("\n").filter((l) => l.trim() !== "");
  if (lines.length < 2) throw new InputError("the file has no data rows");
  const header = lines[0].split(",").map((h) => h.trim().replace(/^"|"$/g, "").toLowerCase());
  const ic = header.indexOf("cycle_idx");
  const iq = header.indexOf("capacity_ah");
  const missing = [["cycle_idx", ic], ["capacity_ah", iq]].filter(([, i]) => i < 0).map(([n]) => n);
  if (missing.length) {
    throw new InputError(
      `missing column(s) [${missing.join(", ")}]; expected 'cycle_idx' and 'capacity_ah' (got [${header.join(", ")}])`,
    );
  }
  const cycle_idx = [], capacity_ah = [];
  for (const line of lines.slice(1)) {
    const f = line.split(",");
    cycle_idx.push(Number(f[ic]));
    capacity_ah.push(Number(f[iq]));
  }
  return { cycle_idx, capacity_ah };
}

/** Same checks and cleaning as predictor.validate_cycles; returns rows sorted by cycle. */
export function validate(data, minCycles) {
  const n = data.cycle_idx.length;
  let bad = 0;
  for (let i = 0; i < n; i++) {
    if (!Number.isFinite(data.cycle_idx[i]) || !Number.isFinite(data.capacity_ah[i])) bad++;
  }
  if (bad) throw new InputError(`${bad} row(s) have non-numeric cycle_idx/capacity_ah`);
  if (data.capacity_ah.some((c) => c <= 0)) throw new InputError("capacity_ah must be positive");
  if (new Set(data.cycle_idx).size !== n) {
    throw new InputError("cycle_idx has duplicates; give one row per cycle");
  }
  const order = [...Array(n).keys()].sort((a, b) => data.cycle_idx[a] - data.cycle_idx[b]);
  if (n < minCycles) throw new InputError(`need at least ${minCycles} cycles, got ${n}`);
  if (n > MAX_CYCLES) throw new InputError(`at most ${MAX_CYCLES} cycles are supported, got ${n}`);
  return {
    cycle_idx: order.map((i) => Math.round(data.cycle_idx[i])),
    capacity_ah: order.map((i) => data.capacity_ah[i]),
  };
}

/** SOH = capacity / mean(first 5 cycles) (data/schema.add_soh). */
export function toSOH(capacity) {
  const k = Math.min(5, capacity.length);
  let ref = 0;
  for (let i = 0; i < k; i++) ref += capacity[i];
  ref /= k;
  return capacity.map((c) => c / ref);
}

/** Window ending at the last cycle, left-padded: Float32Array(L*2) of [soh or 0, mask] rows. */
export function window(soh, L) {
  const out = new Float32Array(L * 2);
  const n = soh.length;
  for (let j = 0; j < L; j++) {
    const i = n - L + j;
    if (i >= 0) {
      out[2 * j] = soh[i];
      out[2 * j + 1] = 1;
    }
  }
  return out;
}

function slope(y) {
  // np.polyfit(arange(n), y, 1)[0]
  const n = y.length;
  if (n < 2) return 0;
  const mx = (n - 1) / 2;
  let my = 0;
  for (const v of y) my += v;
  my /= n;
  let sxy = 0, sxx = 0;
  for (let i = 0; i < n; i++) {
    sxy += (i - mx) * (y[i] - my);
    sxx += (i - mx) * (i - mx);
  }
  return sxy / sxx;
}

function quadCoef(y) {
  // np.polyfit(arange(n), y, 2)[0]: least squares on centred x for stability.
  const n = y.length;
  const c = (n - 1) / 2;
  let s0 = n, s1 = 0, s2 = 0, s3 = 0, s4 = 0, t0 = 0, t1 = 0, t2 = 0;
  for (let i = 0; i < n; i++) {
    const x = i - c, x2 = x * x;
    s1 += x; s2 += x2; s3 += x2 * x; s4 += x2 * x2;
    t0 += y[i]; t1 += x * y[i]; t2 += x2 * y[i];
  }
  // Solve [[s4,s3,s2],[s3,s2,s1],[s2,s1,s0]] [a,b,c0] = [t2,t1,t0] by Cramer's rule; the x^2
  // coefficient is invariant to centring x.
  const det = (m) =>
    m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) -
    m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) +
    m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]);
  const A = [[s4, s3, s2], [s3, s2, s1], [s2, s1, s0]];
  const Aa = [[t2, s3, s2], [t1, s2, s1], [t0, s1, s0]];
  return det(Aa) / det(A);
}

/** Causal SOH summaries at the last cycle (tasks/samples._summary_features). */
export function summaries(soh) {
  const tail = (k) => soh.slice(Math.max(0, soh.length - k));
  const t5 = tail(5), t50 = tail(50);
  const mean5 = t5.reduce((a, b) => a + b, 0) / t5.length;
  const curv = t50.length >= 3 ? quadCoef(t50) : 0;
  return new Float32Array([soh[soh.length - 1], mean5, slope(tail(10)), slope(t50), curv]);
}

function levelIndex(levels, p) {
  let best = 0;
  for (let i = 1; i < levels.length; i++) {
    if (Math.abs(levels[i] - p) < Math.abs(levels[best] - p)) best = i;
  }
  return best;
}

/** Mahalanobis distance + range checks (predictor.Predictor.ood). */
export function ood(meta, soh, tab, nCycles) {
  const o = meta.ood;
  const d = Array.from(tab, (v, i) => v - o.mean[i]);
  let m2 = 0;
  for (let i = 0; i < d.length; i++) for (let j = 0; j < d.length; j++) m2 += d[i] * o.precision[i][j] * d[j];
  const dist = Math.sqrt(Math.max(m2, 0));
  const flags = [];
  if (dist > o.threshold) {
    flags.push(
      `SOH-trajectory summary is far from the training cells (Mahalanobis ${dist.toFixed(1)} > ${o.threshold.toFixed(1)}, the 99th percentile of training)`,
    );
  }
  const [lo, hi] = meta.soh_range;
  if (Math.min(...soh) < lo || Math.max(...soh) > hi) {
    flags.push(`SOH outside [${lo}, ${hi}] (check units or the first cycles)`);
  }
  if (soh.length >= 10) {
    const fade = -tab[3] * 100;
    const [flo, fhi] = o.fade_per_100_range;
    if (!(flo <= fade && fade <= fhi)) {
      const pct = (v) => `${(v * 100).toFixed(2)}%`;
      flags.push(
        `recent fade rate ${pct(fade)} SOH/100 cycles is outside the training range [${pct(flo)}, ${pct(fhi)}]`,
      );
    }
  }
  const L = meta.tasks.forecast.lookback;
  if (nCycles < L) flags.push(`short history (${nCycles} cycles < lookback ${L}); the model pads the window`);
  return { is_ood: flags.length > 0, distance: dist, threshold: o.threshold, flags };
}

/**
 * Turn ONNX outputs into the predictor's result dict.
 * qf: Float32Array(H*Q) forecast quantiles (sorted along Q); qr: Float32Array(Q) RUL quantiles.
 */
export function postprocess(meta, cycles, soh, tab, qf, qr) {
  const last = cycles[cycles.length - 1];
  const f = meta.tasks.forecast, r = meta.tasks.rul;
  const Q = f.quantiles.length;
  const lo_i = levelIndex(f.quantiles, f.alpha / 2), hi_i = levelIndex(f.quantiles, 1 - f.alpha / 2);
  const med = f.quantiles.indexOf(0.5);
  const forecast = f.horizons.map((h, j) => {
    const c = f.cqr_correction[String(h)];
    let lo = qf[j * Q + lo_i] - c, hi = qf[j * Q + hi_i] + c;
    [lo, hi] = [Math.min(lo, hi), Math.max(lo, hi)];
    return { horizon: h, cycle: last + h, soh: qf[j * Q + med], lo: Math.max(lo, 0), hi };
  });
  const rlo_i = levelIndex(r.quantiles, r.alpha / 2), rhi_i = levelIndex(r.quantiles, 1 - r.alpha / 2);
  const c = r.cqr_correction["0"];
  const r_lo = Math.max(qr[rlo_i] - c, 0);
  const r_hi = Math.max(qr[rhi_i] + c, r_lo);
  const r_pt = Math.min(Math.max(qr[r.quantiles.indexOf(0.5)], r_lo), r_hi);
  return {
    n_cycles: cycles.length,
    last_cycle: last,
    history: { cycle: cycles, soh },
    forecast,
    rul: {
      cycles: r_pt, lo: r_lo, hi: r_hi, eol_cycle: last + r_pt,
      threshold_soh: meta.theta, already_below_threshold: soh[soh.length - 1] < meta.theta,
    },
    coverage: 1 - f.alpha,
    ood: ood(meta, soh, tab, cycles.length),
    model: meta.model_version,
  };
}

/** Inputs for both graphs from validated rows. */
export function prepare(meta, rows) {
  const soh = toSOH(rows.capacity_ah);
  const tab = summaries(soh);
  return {
    soh,
    tab,
    histF: window(soh, meta.tasks.forecast.lookback),
    histR: window(soh, meta.tasks.rul.lookback),
  };
}
