// Whole-life trajectories: every method's h-step-ahead held-out forecasts over a cell's life.
// Benchmark predictions: app/examples/traj/<cell>_compare.json (scripts/make_demo_compare.py).
// Live deployed model: computed in the browser (core.mjs, parity-tested) on cells it never saw.
import { parseCSV, postprocess, prepare, validate } from "./core.mjs";

const $ = (id) => document.getElementById(id);
const css = (n) => getComputedStyle(document.documentElement).getPropertyValue(n).trim();
const LIVE = "live";
const ORDER = ["live", "itransformer", "lgbm", "itransformer_sc", "patchtst", "lstm", "persistence", "last_slope", "elasticnet",
  "nlinear", "dlinear", "rlinear", "gru", "transformer",
  "lstm+rest", "transformer+rest", "lgbm+rest", "itransformer+rest", "itransformer_sc+rest", "elasticnet+rest"];
const SLOT = { itransformer: 1, lgbm: 2, itransformer_sc: 3, patchtst: 7, lstm: 5, gru: 4, transformer: 8, elasticnet: 6 };
const DASH = { persistence: "dash", last_slope: "dash" };
let CELLS = [], meta = null, sessF = null, sessR = null;
let D = null; // loaded cell
let H = 50, SEL = ["live", "itransformer", "lgbm", "persistence"], BAND = "";

function color(m) {
  if (m === LIVE) return css("--text-primary");
  const b = m.replace("+rest", "");
  if (SLOT[b]) return css(`--series-${SLOT[b]}`);
  if (b === "persistence" || b === "last_slope") return css("--text-secondary");
  return css("--other");
}
const dash = (m) => (m.endsWith("+rest") ? "dashdot" : DASH[m] ?? "solid");
const rgba = (c, a) => {
  const m = c.match(/^#([0-9a-f]{6})$/i);
  if (!m) return c;
  const n = parseInt(m[1], 16);
  return `rgba(${(n >> 16) & 255},${(n >> 8) & 255},${n & 255},${a})`;
};
const label = (m) => (m === LIVE ? "iTransformer-v2 (live, deployed)" : D?.cmp.models[m]?.label ?? m);

$("theme").addEventListener("click", () => {
  const dark = matchMedia("(prefers-color-scheme: dark)").matches;
  const cur = document.documentElement.dataset.theme || (dark ? "dark" : "light");
  document.documentElement.dataset.theme = cur === "dark" ? "light" : "dark";
  draw();
});

// ------------------------------------------------------------------ loading
async function init() {
  CELLS = await (await fetch("examples/traj/cells.json")).json();
  for (const c of CELLS) $("cell").add(new Option(c.label, c.name));
  const q = new URLSearchParams(location.search);
  if (q.get("cell") && CELLS.some((c) => c.name === q.get("cell"))) $("cell").value = q.get("cell");
  if (q.get("h")) H = Number(q.get("h"));
  $("cell").addEventListener("change", loadCell);
  $("band").addEventListener("change", () => { BAND = $("band").value; draw(); });
  try {
    ort.env.wasm.numThreads = 1;
    meta = await (await fetch("serve_meta.json")).json();
    [sessF, sessR] = await Promise.all([ort.InferenceSession.create("forecast.onnx"), ort.InferenceSession.create("rul.onnx")]);
  } catch (e) {
    console.error("live model unavailable", e);
  }
  await loadCell();
}

async function loadCell() {
  const name = $("cell").value, info = CELLS.find((c) => c.name === name);
  $("status").textContent = "loading…";
  const [cmp, full, eol] = await Promise.all([
    fetch(`examples/traj/${name}_compare.json`).then((r) => r.json()),
    fetch(`examples/traj/${name}_full.csv`).then((r) => r.text()),
    fetch(`examples/traj/${name}_eol.json`).then((r) => r.json()),
  ]);
  const rows = validate(parseCSV(full), 2);
  const ref = rows.capacity_ah.slice(0, 5).reduce((a, b) => a + b, 0) / Math.min(5, rows.capacity_ah.length);
  const soh = rows.capacity_ah.map((c) => c / ref);
  const sohAt = new Map(rows.cycle_idx.map((c, i) => [c, soh[i]]));
  D = { name, info, cmp, rows, soh, sohAt, eol: eol.eol_cycle, live: null };
  const models = ORDER.filter((m) => (m === LIVE ? info.live && sessF : m in cmp.models));
  SEL = SEL.filter((m) => models.includes(m));
  if (!SEL.length) SEL = models.slice(0, 3);
  D.models = models;
  buildHorizons();
  buildChips();
  buildBand();
  $("note").textContent = info.live
    ? "This cell was never used to train any method, including the live model (it is one of its calibration cells)."
    : "The live model is hidden here because this cell was part of its training data; every benchmark method shown is held out (leave-one-cell-out / official test split).";
  draw();
  if (info.live && sessF) computeLive(D);
  else $("status").textContent = "";
}

/** Live model predictions at every origin (in the browser, chunked). */
async function computeLive(d) {
  const n = d.rows.cycle_idx.length, k0 = meta.min_cycles - 1;
  const hz = meta.tasks.forecast.horizons;
  const out = { origin: [], point: [], lo: [], hi: [], rul: [], rlo: [], rhi: [] };
  for (let k = k0; k < n && d === D; k++) {
    const rows = { cycle_idx: d.rows.cycle_idx.slice(0, k + 1), capacity_ah: d.rows.capacity_ah.slice(0, k + 1) };
    const p = prepare(meta, rows);
    const run = async (s, h, L) => (await s.run({ hist: new ort.Tensor("float32", h, [1, L, 2]), tab: new ort.Tensor("float32", p.tab, [1, 5]) })).q.data;
    const qf = await run(sessF, p.histF, meta.tasks.forecast.lookback);
    const qr = await run(sessR, p.histR, meta.tasks.rul.lookback);
    const res = postprocess(meta, rows.cycle_idx, p.soh, p.tab, qf, qr);
    out.origin.push(rows.cycle_idx[k]);
    out.point.push(res.forecast.map((f) => f.soh));
    out.lo.push(res.forecast.map((f) => f.lo));
    out.hi.push(res.forecast.map((f) => f.hi));
    out.rul.push(res.rul.cycles); out.rlo.push(res.rul.lo); out.rhi.push(res.rul.hi);
    if (k % 40 === 0) {
      $("status").textContent = `live model: ${Math.round(((k - k0) / (n - k0)) * 100)}%`;
      await new Promise((r) => setTimeout(r, 0));
    }
  }
  if (d !== D) return;
  d.live = { h: hz, ...out };
  $("status").textContent = "";
  buildHorizons();
  draw();
}

// ------------------------------------------------------------------ controls
function horizonsOf(m) {
  if (m === LIVE) return D.live?.h ?? meta?.tasks.forecast.horizons ?? [];
  return D.cmp.models[m]?.forecast ? D.cmp.h : [];
}
function buildHorizons() {
  const all = [...new Set([...D.cmp.h, ...(D.info.live ? meta?.tasks.forecast.horizons ?? [] : [])])].sort((a, b) => a - b);
  if (!all.includes(H)) H = all.includes(50) ? 50 : all[0];
  $("hz").innerHTML = all.map((h) => `<button aria-pressed="${h === H}" data-h="${h}">h = ${h}</button>`).join("");
  for (const b of $("hz").querySelectorAll("button")) {
    b.addEventListener("click", () => { H = Number(b.dataset.h); buildHorizons(); buildChips(); draw(); });
  }
}
function buildChips() {
  $("chips").innerHTML = D.models.map((m) => {
    const has = horizonsOf(m).includes(H) || (m === LIVE && !D.live);
    return `<label class="chip${has ? "" : " off"}" title="${has ? "" : `no forecast at h = ${H}`}"><input type="checkbox" data-m="${m}" ${SEL.includes(m) ? "checked" : ""} ${has ? "" : "disabled"}>` +
      `<span class="sw" style="background:${color(m)}"></span>${label(m)}</label>`;
  }).join("");
  for (const i of $("chips").querySelectorAll("input")) {
    i.addEventListener("change", () => {
      SEL = i.checked ? [...SEL, i.dataset.m] : SEL.filter((x) => x !== i.dataset.m);
      buildBand(); draw();
    });
  }
}
function buildBand() {
  const opts = SEL.filter((m) => (m === LIVE ? true : D.cmp.models[m]?.forecast?.lo));
  if (BAND && !opts.includes(BAND)) BAND = "";
  if (!BAND && opts.length) BAND = opts[0];
  $("band").innerHTML = `<option value="">none</option>` + opts.map((m) => `<option value="${m}" ${m === BAND ? "selected" : ""}>${label(m)}</option>`).join("");
}

// ------------------------------------------------------------------ series
/** {x: target cycles, y: forecast SOH, lo, hi} at horizon H for model m, or null. */
function track(m) {
  if (m === LIVE) {
    const L = D.live;
    if (!L) return null;
    const j = L.h.indexOf(H);
    if (j < 0) return null;
    return { x: L.origin.map((o) => o + H), y: L.point.map((p) => p[j]), lo: L.lo.map((p) => p[j]), hi: L.hi.map((p) => p[j]) };
  }
  const e = D.cmp.models[m]?.forecast, j = D.cmp.h.indexOf(H);
  if (!e || j < 0) return null;
  const s = D.cmp.scale, o = D.cmp.origin.forecast;
  const pick = (a) => a?.map((r) => (r[j] == null ? null : r[j] / s));
  return { x: o.map((c) => c + H), y: pick(e.point), lo: pick(e.lo), hi: pick(e.hi) };
}
function rulTrack(m) {
  if (m === LIVE) return D.live ? { x: D.live.origin, y: D.live.rul } : null;
  const e = D.cmp.models[m]?.rul;
  return e ? { x: D.cmp.origin.rul, y: e.point } : null;
}
function metrics(m) {
  const t = track(m);
  let n = 0, se = 0, bias = 0, cov = 0, ncov = 0;
  if (t) {
    t.x.forEach((c, i) => {
      const y = D.sohAt.get(c), p = t.y[i];
      if (y == null || p == null) return;
      const e = (p - y) * 100; n++; se += e * e; bias += e;
      if (t.lo && t.lo[i] != null) { ncov++; if (y >= t.lo[i] && y <= t.hi[i]) cov++; }
    });
  }
  let rn = 0, ra = 0;
  const r = rulTrack(m);
  if (r && Number.isFinite(D.eol)) {
    r.x.forEach((c, i) => { if (c <= D.eol && r.y[i] != null) { rn++; ra += Math.abs(r.y[i] - (D.eol - c)); } });
  }
  return { rmse: n ? Math.sqrt(se / n) : null, bias: n ? bias / n : null, cov: ncov ? cov / ncov : null, rul: rn ? ra / rn : null, n };
}
function rolling(x, y, w = 11) {
  const out = [];
  for (let i = 0; i < y.length; i++) {
    let s = 0, c = 0;
    for (let j = Math.max(0, i - (w >> 1)); j <= Math.min(y.length - 1, i + (w >> 1)); j++) if (y[j] != null) { s += y[j]; c++; }
    out.push(c ? s / c : null);
  }
  return out;
}

// ------------------------------------------------------------------ drawing
function baseLayout(extra) {
  const g = css("--grid"), ink = css("--text-primary");
  return {
    paper_bgcolor: "rgba(0,0,0,0)", plot_bgcolor: "rgba(0,0,0,0)",
    font: { color: ink, family: "system-ui, sans-serif", size: 12 },
    margin: { l: 58, r: 16, t: 10, b: 46 }, hovermode: "x unified",
    hoverlabel: { bgcolor: css("--surface-2"), bordercolor: g, font: { color: ink } },
    legend: { orientation: "h", y: -0.2, font: { size: 11 } },
    ...extra,
    xaxis: { gridcolor: g, zerolinecolor: g, ...(extra.xaxis || {}) },
    yaxis: { gridcolor: g, zerolinecolor: g, ...(extra.yaxis || {}) },
  };
}
const CFG = { responsive: true, displaylogo: false, modeBarButtonsToRemove: ["lasso2d", "select2d"] };

function draw() {
  if (!D) return;
  const ink = css("--text-primary"), muted = css("--text-secondary");
  const c = D.rows.cycle_idx, last = c.at(-1);
  const xEnd = Number.isFinite(D.eol) ? Math.min(last, D.eol + Math.max(30, 0.2 * D.eol)) : last;
  const xr = [c[0], xEnd];
  $("t-soh").textContent = `Predicted vs measured SOH, forecasts made ${H} cycles ahead`;
  $("t-tab").textContent = `Ranking at h = ${H} cycles`;
  const cyc = D.cmp.events ?? { long_rest: [], cv_skip: [] };

  // SOH chart
  const tr = [];
  if (BAND && SEL.includes(BAND)) {
    const t = track(BAND);
    if (t && t.lo) {
      const col = color(BAND);
      tr.push({ x: t.x, y: t.hi.map((v) => (v == null ? null : v * 100)), mode: "lines", line: { width: 0 }, hoverinfo: "skip", showlegend: false });
      tr.push({ x: t.x, y: t.lo.map((v) => (v == null ? null : v * 100)), mode: "lines", line: { width: 0 }, fill: "tonexty",
        fillcolor: rgba(col.startsWith("#") ? col : "#888888", 0.18), name: `90% interval: ${label(BAND)}`, hoverinfo: "skip" });
    }
  }
  tr.push({ x: c, y: D.soh.map((v) => v * 100), mode: "lines", name: "measured SOH", line: { color: rgba(css("--series-4").startsWith("#") ? css("--series-4") : "#eda100", 0.9), width: 4 }, opacity: 0.55,
    hovertemplate: "%{y:.1f}%<extra>measured</extra>" });
  for (const m of SEL) {
    const t = track(m);
    if (!t) continue;
    tr.push({ x: t.x, y: t.y.map((v) => (v == null ? null : v * 100)), mode: "lines", name: label(m),
      line: { color: color(m), width: m === LIVE ? 2.6 : 1.8, dash: dash(m) }, hovertemplate: "%{y:.1f}%<extra>" + label(m) + "</extra>" });
  }
  const mk = (cs, sym, col, name) => {
    const ii = cs.map((x) => c.indexOf(x)).filter((i) => i >= 0);
    if (ii.length) tr.push({ x: ii.map((i) => c[i]), y: ii.map((i) => D.soh[i] * 100), mode: "markers", name,
      marker: { symbol: sym, size: 8, color: col }, hoverinfo: "skip" });
  };
  mk(cyc.long_rest, "triangle-up", css("--series-3"), "after a long rest");
  mk(cyc.cv_skip, "x-thin-open", css("--series-8"), "charger glitch (artifact)");
  const vis = D.soh.filter((_, i) => c[i] <= xEnd).map((v) => v * 100);
  const ylo = Math.min(...vis, 80), yhi = Math.max(...vis);
  const shapes = [{ type: "line", xref: "paper", yref: "y", x0: 0, x1: 1, y0: 80, y1: 80, line: { color: css("--series-8"), width: 1, dash: "dot" } }];
  if (Number.isFinite(D.eol)) shapes.push({ type: "line", xref: "x", yref: "paper", x0: D.eol, x1: D.eol, y0: 0, y1: 1, line: { color: muted, dash: "dot", width: 1 } });
  Plotly.react("c-soh", tr, baseLayout({ xaxis: { title: { text: "cycle (the cycle being predicted)" }, range: xr },
    yaxis: { title: { text: "state of health (%)" }, range: [ylo - 2, yhi + 1.5] }, shapes,
    annotations: Number.isFinite(D.eol) ? [{ x: D.eol, y: 0.99, yref: "paper", text: " end of life", showarrow: false, xanchor: "left", yanchor: "top", font: { size: 11, color: muted } }] : [] }), CFG);

  // error chart
  const er = [];
  for (const m of SEL) {
    const t = track(m);
    if (!t) continue;
    const e = t.x.map((x, i) => { const y = D.sohAt.get(x); return y == null || t.y[i] == null ? null : Math.abs(t.y[i] - y) * 100; });
    er.push({ x: t.x, y: rolling(t.x, e), mode: "lines", name: label(m), line: { color: color(m), width: m === LIVE ? 2.4 : 1.6, dash: dash(m) },
      hovertemplate: "%{y:.2f} pp<extra>" + label(m) + "</extra>" });
  }
  Plotly.react("c-err", er, baseLayout({ margin: { l: 58, r: 16, t: 10, b: 80 }, legend: { orientation: "h", y: -0.38, font: { size: 11 } }, xaxis: { title: { text: "cycle being predicted" }, range: xr },
    yaxis: { title: { text: `|error| at h = ${H} (pp SOH)` }, rangemode: "tozero" } }), CFG);

  // table
  const rows = SEL.map((m) => ({ m, ...metrics(m) })).filter((r) => r.n || r.rul != null).sort((a, b) => (a.rmse ?? 1e9) - (b.rmse ?? 1e9));
  const f = (v, d, suf = "") => (v == null ? "–" : `${v.toFixed(d)}${suf}`);
  $("tab").innerHTML = "<tr><th>Method</th><th>RMSE (% SOH)</th><th>Bias</th><th>90% coverage</th><th>RUL MAE (cycles)</th><th>Targets</th></tr>" +
    rows.map((r) => `<tr><td><span class="sw2" style="background:${color(r.m)}"></span>${label(r.m)}</td><td>${f(r.rmse, 2)}</td><td>${r.bias == null ? "–" : (r.bias >= 0 ? "+" : "") + r.bias.toFixed(2)}</td>` +
      `<td>${r.cov == null ? "–" : Math.round(r.cov * 100) + "%"}</td><td>${f(r.rul, 0)}</td><td>${r.n}</td></tr>`).join("");

  // RUL chart
  const rr = [];
  if (Number.isFinite(D.eol)) {
    const tx = c.filter((x) => x <= D.eol);
    rr.push({ x: tx, y: tx.map((x) => (D.eol - x) * 1.2), mode: "lines", line: { color: muted, dash: "dot", width: 1 }, name: "±20% of truth", hoverinfo: "skip" });
    rr.push({ x: tx, y: tx.map((x) => (D.eol - x) * 0.8), mode: "lines", line: { color: muted, dash: "dot", width: 1 }, showlegend: false, hoverinfo: "skip" });
    rr.push({ x: tx, y: tx.map((x) => D.eol - x), mode: "lines", name: "true RUL", line: { color: css("--series-8"), width: 2, dash: "dash" }, hovertemplate: "%{y:.0f}<extra>true RUL</extra>" });
  }
  for (const m of SEL) {
    const t = rulTrack(m);
    if (!t) continue;
    rr.push({ x: t.x, y: t.y, mode: "lines", name: label(m), line: { color: color(m), width: m === LIVE ? 2.4 : 1.5, dash: dash(m) },
      hovertemplate: "%{y:.0f} cycles<extra>" + label(m) + "</extra>" });
  }
  Plotly.react("c-rul", rr, baseLayout({ xaxis: { title: { text: "prediction point (cycle)" }, range: [c[0], Number.isFinite(D.eol) ? D.eol + 10 : last] },
    yaxis: { title: { text: "remaining useful life (cycles)" }, rangemode: "tozero" } }), CFG);
}

init();
