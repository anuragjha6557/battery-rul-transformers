// Browser port of the field-mode serving path (ADR-0022), pure functions, no DOM:
//   src/battery_rul/serve/field.py        (validate_field, latest_sample, useful, predict, ood)
//   src/battery_rul/data/cleaning.py      (clean_inputs: physical ranges, charge pause, robust z)
//   src/battery_rul/tasks/samples.py      (_derive, apply_prepared, _scaled, _windows)
// The ONNX graphs (scripts/export_onnx_field.py) take hist (1, L, C+1) and tab (1, 1) and return
// the member-mean quantiles q (1, H, Q). Parity with Python is tested by tests/web/test_field.mjs
// against vectors written by the export script. Pandas semantics are mirrored deliberately:
// comparisons with NaN are false; rolling windows count rows (NaN rows occupy a slot) but need
// `min_periods` non-NaN observations; rolling medians are over the non-NaN values of the window.

export class InputError extends Error {}

const NaNv = Number.NaN;
const NUM = /^[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?$/;
const pyList = (a) => `[${a.map((s) => `'${s}'`).join(", ")}]`;

/** CSV text -> {names, cols: Map(lowercase name -> Float64Array)}; blank / non-numeric -> NaN. */
export function parseCSV(text) {
  const lines = text.replace(/\r/g, "").split("\n").filter((l) => l.trim() !== "");
  if (lines.length < 2) throw new InputError("the file has no data rows");
  const names = lines[0].split(",").map((h) => h.trim().replace(/^"|"$/g, "").trim().toLowerCase());
  const n = lines.length - 1;
  const cols = new Map();
  for (const h of names) if (!cols.has(h)) cols.set(h, new Float64Array(n).fill(NaNv));
  for (let i = 0; i < n; i++) {
    const f = lines[i + 1].split(",");
    for (let j = 0; j < names.length && j < f.length; j++) {
      const s = f[j].trim().replace(/^"|"$/g, "").trim();
      // a duplicated header keeps its first column (pandas renames later ones)
      if (NUM.test(s) && names.indexOf(names[j]) === j) cols.get(names[j])[i] = Number(s);
    }
  }
  return { names, cols, n };
}

/** numpy round (half to even), as `ci.round().astype(int)`. */
function roundHalfEven(x) {
  const r = Math.round(x);
  return Math.abs(x % 1) === 0.5 && r % 2 !== 0 ? r - 1 : r;
}

/**
 * validate_field: returns a canonical frame {n, cycle_idx, cols: Map, order} sorted by cycle.
 * `order[i]` is the index in the uploaded file of sorted row i (to look up extra columns).
 */
export function validateField(table, meta) {
  const ci = table.cols.get("cycle_idx");
  if (!ci) throw new InputError(`missing column 'cycle_idx' (got ${pyList(table.names)})`);
  const n = table.n;
  let bad = 0;
  for (const v of ci) if (Number.isNaN(v)) bad++;
  if (bad) throw new InputError(`${bad} row(s) have a non-numeric cycle_idx`);
  if (new Set(ci).size !== n) throw new InputError("cycle_idx has duplicates; give one row per cycle");
  if (n < meta.min_cycles) throw new InputError(`need at least ${meta.min_cycles} cycles, got ${n}`);
  if (n > meta.max_cycles) throw new InputError(`at most ${meta.max_cycles} cycles are supported, got ${n}`);
  const order = [...Array(n).keys()].sort((a, b) => roundHalfEven(ci[a]) - roundHalfEven(ci[b]));
  const derive = Object.values(meta.derived_from).filter((r) => r !== "cycle_idx");
  const wanted = [...new Set([...meta.inputs.slice(1), ...meta.optional_inputs, ...derive])];
  const cols = new Map();
  for (const c of wanted) {
    const src = table.cols.get(c.toLowerCase());
    cols.set(c, src ? Float64Array.from(order, (i) => src[i]) : new Float64Array(n).fill(NaNv));
  }
  return { n, cycle_idx: order.map((i) => roundHalfEven(ci[i])), cols, order };
}

// ---------------------------------------------------------------- pandas-style rolling helpers
function median(sorted) {
  const m = sorted.length;
  return m % 2 ? sorted[(m - 1) / 2] : (sorted[m / 2 - 1] + sorted[m / 2]) / 2;
}

/** x.shift(1).rolling(window, min_periods).median(): window = the `window` rows before t. */
export function pastRollingMedian(x, window, minPeriods) {
  const out = new Float64Array(x.length).fill(NaNv);
  for (let t = 0; t < x.length; t++) {
    const v = [];
    for (let j = Math.max(0, t - window); j < t; j++) if (!Number.isNaN(x[j])) v.push(x[j]);
    if (v.length >= minPeriods) out[t] = median(v.sort((a, b) => a - b));
  }
  return out;
}

/** x.shift(1).expanding(min_periods).median(), incremental sorted insert. */
export function pastExpandingMedian(x, minPeriods) {
  const out = new Float64Array(x.length).fill(NaNv);
  const s = [];
  for (let t = 0; t < x.length; t++) {
    if (s.length >= minPeriods) out[t] = median(s);
    const v = x[t];
    if (!Number.isNaN(v)) {
      let lo = 0, hi = s.length;
      while (lo < hi) { const mid = (lo + hi) >> 1; if (s[mid] < v) lo = mid + 1; else hi = mid; }
      s.splice(lo, 0, v);
    }
  }
  return out;
}

/** clean_inputs (ADR-0018 causal rules). Returns {cols: Map (copies), counts: {name: n}}. */
export function cleanInputs(frame, cfg) {
  const cols = new Map([...frame.cols].map(([k, v]) => [k, Float64Array.from(v)]));
  const n = frame.n;
  const counts = {};
  for (const [c, [lo, hi]] of Object.entries(cfg.physical_ranges)) {
    const x = cols.get(c);
    if (!x) continue;
    let k = 0;
    for (let i = 0; i < n; i++) if (x[i] < lo || x[i] > hi) { x[i] = NaNv; k++; } // NaN compares false
    counts[`range:${c}`] = k;
  }
  // masks use the range-cleaned values, before any pause masking (input_outliers)
  const pause = new Array(n).fill(false);
  const ct = cols.get("charge_time_s");
  if (ct) {
    const med = pastExpandingMedian(ct, cfg.pause_min_history);
    for (let i = 0; i < n; i++) pause[i] = ct[i] > cfg.pause_factor * med[i];
  }
  const rest = cols.get("rest_before_s");
  const afterRest = Array.from({ length: n }, (_, i) => (rest ? rest[i] > cfg.long_rest_s : false));
  const robust = [];
  for (const c of cfg.robust_cols) {
    const x = cols.get(c);
    if (!x) continue;
    const med = pastRollingMedian(x, cfg.robust_window, cfg.robust_min_history);
    const dev = Float64Array.from(x, (v, i) => Math.abs(v - med[i]));
    const madRaw = pastRollingMedian(dev, cfg.robust_window, cfg.robust_min_history);
    const bad = new Array(n).fill(false);
    for (let i = 0; i < n; i++) {
      const floor = cfg.robust_rel_floor * Math.abs(med[i]);
      const mad = (madRaw[i] > floor ? madRaw[i] : floor) + 1e-12; // NaN > floor is false
      bad[i] = dev[i] > cfg.robust_k * mad && !afterRest[i];
    }
    robust.push([c, bad]);
  }
  counts.charge_pause = pause.filter(Boolean).length;
  for (const [c, x] of cols) {
    const dur = cfg.charge_duration_cols.includes(c) || cfg.charge_duration_prefixes.some((p) => c.startsWith(p));
    if (!dur) continue;
    for (let i = 0; i < n; i++) if (pause[i]) x[i] = NaNv;
  }
  for (const [c, bad] of robust) {
    const x = cols.get(c);
    let k = 0;
    for (let i = 0; i < n; i++) if (bad[i] && !pause[i]) { x[i] = NaNv; k++; }
    counts[c] = k;
  }
  return { cols, counts };
}

const clipZ = (z, lim) => (Number.isNaN(z) ? 0 : Math.min(lim, Math.max(-lim, z)));

/** _derive + forward fill + standardise + clip + zero-fill (apply_prepared). Float64Array per channel. */
export function scaleChannels(meta, cleaned, cycleIdx) {
  const n = cycleIdx.length, cfg = meta.cleaning;
  const out = [];
  meta.channels.forEach((ch, k) => {
    let x;
    if (ch === "cycle_count") x = Float64Array.from(cycleIdx, (v) => Math.log1p(v));
    else if (ch === "log_rest_s") {
      const r = cleaned.get("rest_before_s");
      x = Float64Array.from({ length: n }, (_, i) => (r ? Math.log1p(Math.max(r[i], 0)) : NaNv));
      for (let i = 0; i < n; i++) if (r && Number.isNaN(r[i])) x[i] = NaNv; // Math.max(NaN, 0) is NaN
    } else if (ch === "skipped_cv") {
      const cv = cleaned.get("cv_time_s");
      x = Float64Array.from({ length: n }, (_, i) => (!cv || Number.isNaN(cv[i]) ? NaNv : cv[i] < cfg.skipped_cv_s ? 1 : 0));
    } else x = cleaned.has(ch) ? Float64Array.from(cleaned.get(ch)) : new Float64Array(n).fill(NaNv);
    let last = NaNv;
    for (let i = 0; i < n; i++) {
      if (Number.isNaN(x[i])) x[i] = last; else last = x[i];
    }
    const mu = meta.scaler.mean[k], sc = meta.scaler.scale[k];
    for (let i = 0; i < n; i++) x[i] = clipZ((x[i] - mu) / sc, cfg.clip_z);
    out.push(x);
  });
  return out;
}

/** hist (L, C+1) row-major: last L rows left-padded with zeros, validity mask as the last channel. */
export function windowHist(scaled, L) {
  const C = scaled.length, n = scaled[0].length, W = C + 1;
  const out = new Float32Array(L * W);
  for (let j = 0; j < L; j++) {
    const i = n - L + j;
    if (i < 0) continue;
    for (let c = 0; c < C; c++) out[j * W + c] = scaled[c][i];
    out[j * W + C] = 1;
  }
  return out;
}

/** Everything the ONNX graphs need, plus the cleaning counts and the raw frame for the OOD check. */
export function prepare(meta, frame) {
  const { cols, counts } = cleanInputs(frame, meta.cleaning);
  const scaled = scaleChannels(meta, cols, frame.cycle_idx);
  const lastCycle = frame.cycle_idx[frame.n - 1];
  const hist = {};
  for (const t of Object.keys(meta.tasks)) hist[t] = windowHist(scaled, meta.tasks[t].lookback);
  return {
    hist,
    tab: Float32Array.of(Math.log1p(lastCycle)),
    scaledLast: scaled.map((x) => x[frame.n - 1]),
    counts,
    lastCycle,
  };
}

// ---------------------------------------------------------------- post-processing
const levelIndex = (levels, p) => {
  let best = 0;
  for (let i = 1; i < levels.length; i++) if (Math.abs(levels[i] - p) < Math.abs(levels[best] - p)) best = i;
  return best;
};
const close = (a, b) => Math.abs(a - b) <= 1e-8 + 1e-5 * Math.abs(b); // np.isclose

/** ADR-0019 informativeness of an SOH interval. */
export function useful(meta, lo, hi, point) {
  return hi - lo < meta.useful_frac * Math.max(point - meta.theta, 0.005);
}

function interval(t, q, Q, j, key) {
  const lo_i = levelIndex(t.quantiles, t.alpha / 2), hi_i = levelIndex(t.quantiles, 1 - t.alpha / 2);
  if (!close(t.quantiles[lo_i], t.alpha / 2) || !close(t.quantiles[hi_i], 1 - t.alpha / 2)) {
    throw new Error(`quantile levels ${t.quantiles} lack ${t.alpha / 2} / ${1 - t.alpha / 2}`);
  }
  const c = t.cqr_correction[key];
  let lo = q[j * Q + lo_i] - c, hi = q[j * Q + hi_i] + c;
  [lo, hi] = [Math.min(lo, hi), Math.max(lo, hi)];
  const med = t.quantiles.findIndex((v) => v === 0.5);
  return [q[j * Q + med], lo, hi];
}

/** Distance (stored precision; diagonal, Ledoit-Wolf or full per protocol) of the latest scaled channel vector + the same flags as FieldPredictor.ood. */
export function ood(meta, scaledLast, frame) {
  const o = meta.ood;
  const d = scaledLast.map((v, i) => v - o.mean[i]);
  let m2 = 0;
  for (let i = 0; i < d.length; i++) for (let j = 0; j < d.length; j++) m2 += d[i] * o.precision[i][j] * d[j];
  const dist = Math.sqrt(Math.max(m2, 0));
  const flags = [];
  if (dist > o.threshold) {
    flags.push(
      `latest cycle's signals are far from the training cycles (distance ${dist.toFixed(1)} > ${o.threshold.toFixed(1)}, ` +
        `the training 99th percentile); the intervals assume a cell like the ${meta.protocol} training cells`,
    );
  }
  const empty = meta.inputs.slice(1).filter((c) => !frame.cols.has(c) || frame.cols.get(c).every(Number.isNaN));
  if (empty.length) flags.push(`missing or empty signal column(s) ${pyList(empty)}; treated as unobserved`);
  const lb = Math.max(...Object.values(meta.tasks).map((t) => t.lookback));
  if (frame.n < lb) flags.push(`short history (${frame.n} cycles < lookback ${lb}); the window is padded`);
  return { is_ood: flags.length > 0, distance: dist, threshold: o.threshold, flags };
}

/** q: {soh, forecast, rul} Float32Array(H*Q) ONNX outputs. Same result dict as FieldPredictor.predict. */
export function postprocess(meta, frame, prep, q) {
  const T = meta.tasks, last = prep.lastCycle;
  const Qs = T.soh.quantiles.length;
  const [pt, lo, hi] = interval(T.soh, q.soh, Qs, 0, "0");
  const soh_now = { soh: pt, lo: Math.max(lo, 0), hi, useful: useful(meta, lo, hi, pt) };

  const Qf = T.forecast.quantiles.length;
  const forecast = T.forecast.horizons.map((h, j) => {
    const [p, l, u] = interval(T.forecast, q.forecast, Qf, j, String(h));
    return { horizon: h, cycle: last + h, soh: p, lo: Math.max(l, 0), hi: u, useful: useful(meta, l, u, p) };
  });

  const Qr = T.rul.quantiles.length;
  const [rp, rl0, rh0] = interval(T.rul, q.rul, Qr, 0, "0");
  const rl = Math.max(rl0, 0), rh = Math.max(rh0, rl);
  const rpt = Math.min(Math.max(rp, rl), rh);
  const rul = {
    cycles: rpt, lo: rl, hi: rh, eol_cycle: last + rpt, threshold_soh: meta.theta,
    already_below_threshold: soh_now.soh < meta.theta,
  };
  return {
    protocol: meta.protocol,
    n_cycles: frame.n,
    last_cycle: last,
    soh_now,
    forecast,
    rul,
    coverage: 1 - T.forecast.alpha,
    cleaning: Object.fromEntries(Object.entries(prep.counts).filter(([, v]) => v)),
    ood: ood(meta, prep.scaledLast, frame),
    heldout: meta.heldout ?? {},
    model: meta.model_version,
  };
}

/** Full pipeline from CSV text; `infer(task, hist, tab) -> Promise<Float32Array>` runs one ONNX graph. */
export async function predictField(meta, text, infer) {
  const table = parseCSV(text);
  const frame = validateField(table, meta);
  const prep = prepare(meta, frame);
  const q = {};
  for (const t of Object.keys(meta.tasks)) q[t] = await infer(t, prep.hist[t], prep.tab);
  return { table, frame, prep, result: postprocess(meta, frame, prep, q) };
}
