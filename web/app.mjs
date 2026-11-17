// Interactive dashboard for the static Space. The user moves the prediction point (drag on the
// chart, slider or play); the ONNX models re-predict in the browser from the cycles up to that
// point only. Prediction logic lives in core.mjs (parity-tested against the Python predictor).
import { InputError, parseCSV, postprocess, prepare, validate } from "./core.mjs";

const $ = (id) => document.getElementById(id);
let meta, sessF, sessR;
let DEMOS = []; // [name, label] from examples/demos.json (scripts/make_examples.py)

// state of the loaded cell
let S = null; // {rows, soh, truthEol, eolLabel, k, cache: Map, track, demo}
let busy = false, pending = null, playing = false;

// ---------------------------------------------------------------- benchmark comparison
// Precomputed held-out predictions of the benchmarked models (scripts/make_demo_compare.py), demo cells only.
const MAX_SEL = 5;
const CMP_STYLE = { // fixed colours, labels from web/showcase/viz.mjs
  itransformer: { color: "#2a78d6", symbol: "circle" },
  lgbm: { color: "#eb6834", symbol: "diamond" },
  itransformer_sc: { color: "#1baf7a", symbol: "square" },
  patchtst: { color: "#6250d6", symbol: "triangle-up" },
  lstm: { color: "#e87ba4", symbol: "cross" },
  persistence: { color: "#7d8088", symbol: "x", dash: "dash" },
};
const OTHER_SYMBOLS = ["star", "hexagram", "triangle-down", "pentagon", "bowtie", "hourglass", "circle-open", "diamond-open"];
const CMP_ORDER = ["itransformer", "lgbm", "itransformer_sc", "patchtst", "lstm", "persistence", "last_slope", "elasticnet",
  "nlinear", "dlinear", "rlinear", "gru", "transformer"];
const CMP_LABEL = { // shown when no compare file is loaded
  itransformer: "iTransformer (MC)", lgbm: "LightGBM", itransformer_sc: "iTransformer (SC)", patchtst: "PatchTST", lstm: "LSTM",
  persistence: "Persistence (SOH stays the same)", last_slope: "Last slope", elasticnet: "ElasticNet", nlinear: "NLinear",
  dlinear: "DLinear", rlinear: "RLinear", gru: "GRU", transformer: "Transformer",
};
const LIVE_LABEL = "iTransformer-v2 (live, deployed)";
const NOTE_NA = "benchmark comparisons are available for the demo cells only (they are the models' real held-out predictions)";
const cmpStyle = (m) => CMP_STYLE[m] ?? { color: "#9b9a94", symbol: OTHER_SYMBOLS[Math.max(0, CMP_ORDER.indexOf(m)) % OTHER_SYMBOLS.length] };
let CMP = null; // {h, scale, fi: Map origin->row, ri: Map, models, rulCache}
let SEL = ["lgbm", "itransformer", "persistence"]; // selection order = drawing order; the first one with an interval gets the band
let lastRes = null;
const rgba = (hex, a) => {
  const m = /^#?([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})$/i.exec(hex);
  return m ? `rgba(${parseInt(m[1], 16)},${parseInt(m[2], 16)},${parseInt(m[3], 16)},${a})` : hex;
};

function buildCmp(j) {
  const idx = (o) => new Map(o.map((c, i) => [c, i]));
  return { h: j.h, scale: j.scale, models: j.models, fi: idx(j.origin.forecast ?? []), ri: idx(j.origin.rul ?? []),
    rulOrigin: j.origin.rul ?? [], rulCache: new Map() };
}
/** Is a precomputed forecast available at the current prediction point? */
const cmpAvail = (last) => !!CMP && CMP.fi.has(last);

function buildChips() {
  const keys = CMP ? CMP_ORDER.filter((m) => m in CMP.models).concat(Object.keys(CMP.models).filter((m) => !CMP_ORDER.includes(m))) : CMP_ORDER;
  if (CMP) SEL = SEL.filter((m) => m in CMP.models);
  $("cmp-chips").innerHTML = keys.map((m) => {
    const st = cmpStyle(m), label = CMP?.models[m]?.label ?? CMP_LABEL[m] ?? m;
    return `<label class="chip"><input type="checkbox" data-m="${m}"${SEL.includes(m) ? " checked" : ""}>` +
      `<span class="sw" style="background:${st.color}"></span>${escape(label)}</label>`;
  }).join("");
  for (const inp of $("cmp-chips").querySelectorAll("input")) {
    inp.addEventListener("change", () => {
      const m = inp.dataset.m;
      SEL = inp.checked ? [...SEL.filter((x) => x !== m), m] : SEL.filter((x) => x !== m);
      if (lastRes) render(lastRes); else updateChips(false);
    });
  }
  updateChips(false);
}
function updateChips(avail) {
  for (const inp of $("cmp-chips").querySelectorAll("input")) {
    const full = !SEL.includes(inp.dataset.m) && SEL.length >= MAX_SEL;
    inp.disabled = !avail || full;
    inp.parentElement.classList.toggle("off", inp.disabled);
    inp.parentElement.title = !avail ? NOTE_NA : full ? `At most ${MAX_SEL} methods at once: untick one first` : "";
  }
  $("cmp-na").classList.toggle("hidden", avail);
  $("cmp-na").textContent = NOTE_NA;
}

// ---------------------------------------------------------------- page chrome
for (const b of document.querySelectorAll("nav button")) {
  b.addEventListener("click", () => {
    for (const o of document.querySelectorAll("nav button")) o.setAttribute("aria-selected", String(o === b));
    for (const t of ["predict", "format", "about"]) $(`tab-${t}`).classList.toggle("hidden", t !== b.dataset.tab);
    if (b.dataset.tab === "predict" && S) { Plotly.Plots.resize("plot"); Plotly.Plots.resize("plot-rul"); }
  });
}
const tmpl = "cycle_idx,capacity_ah\n" + Array.from({ length: 12 }, (_, i) => `${i + 1},${(2 - 0.004 * i).toFixed(4)}`).join("\n");
$("template").href = "data:text/csv;charset=utf-8," + encodeURIComponent(tmpl + "\n");
$("demo").addEventListener("change", () => {
  $("upload-wrap").classList.toggle("hidden", $("demo").value !== "");
  if ($("demo").value) loadCell();
});
$("run").addEventListener("click", () => loadCell());
$("file").addEventListener("change", () => loadCell());

const escape = (s) => String(s).replace(/[&<>]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" })[c]);
const pct = (v) => `${(v * 100).toFixed(1)}%`;
const css = (n) => getComputedStyle(document.documentElement).getPropertyValue(n).trim();
function show(kind, html) {
  $("msg").innerHTML = html ? `<div class="banner ${kind}">${html}</div>` : "";
}

function renderAccuracy(acc) {
  const t = acc.datasets.toyota;
  if (!t) return;
  $("accuracy").innerHTML =
    `<b>How accurate is it?</b> On ${t.n_cells} held-out Toyota cells (never trained on), predicting from half-way through life, ` +
    `the median remaining-life error is <b>${Math.round(t.median_abs_err)} cycles (${Math.round(t.median_rel_err * 100)}%)</b> and ` +
    `<b>${Math.round(t.coverage * 100)}%</b> of the 90% intervals contain the true value. ` +
    `Full benchmark: <a href="showcase.html">project showcase</a>.`;
}

// ---------------------------------------------------------------- model
async function load() {
  try {
    ort.env.wasm.numThreads = 1;
    meta = await (await fetch("serve_meta.json")).json();
    DEMOS = (await (await fetch("examples/demos.json")).json()).map((d) => [d.name, d.label]);
    for (const [v, label] of DEMOS) $("demo").add(new Option(`${label} · held out from training`, v));
    renderAccuracy(await (await fetch("examples/accuracy.json")).json());
    [sessF, sessR] = await Promise.all([
      ort.InferenceSession.create("forecast.onnx"),
      ort.InferenceSession.create("rul.onnx"),
    ]);
    $("run").disabled = false;
    $("run").textContent = "Load";
    const q = new URLSearchParams(location.search).get("demo"); // shareable ?demo=<cell>
    $("demo").value = q && DEMOS.some(([v]) => v === q) ? q : DEMOS.at(-1)[0];
    $("demo").dispatchEvent(new Event("change"));
  } catch (e) {
    show("err", `Could not load the model (${escape(e.message)}). Reload the page to retry.`);
  }
}

async function infer(sess, hist, L, tab) {
  const out = await sess.run({
    hist: new ort.Tensor("float32", hist, [1, L, 2]),
    tab: new ort.Tensor("float32", tab, [1, 5]),
  });
  return out.q.data;
}

/** Full prediction using only rows[0..k]. Cached per origin index. */
async function predictAt(k) {
  if (S.cache.has(k)) return S.cache.get(k);
  const rows = { cycle_idx: S.rows.cycle_idx.slice(0, k + 1), capacity_ah: S.rows.capacity_ah.slice(0, k + 1) };
  const p = prepare(meta, rows);
  const qf = await infer(sessF, p.histF, meta.tasks.forecast.lookback, p.tab);
  const qr = await infer(sessR, p.histR, meta.tasks.rul.lookback, p.tab);
  const res = postprocess(meta, rows.cycle_idx, p.soh, p.tab, qf, qr);
  S.cache.set(k, res);
  return res;
}

/** First cycle where SOH stays below the threshold for 5 cycles (the NASA/CALCE label rule). */
function sustainedEol(cycles, soh, theta, run = 5) {
  for (let i = 0; i + run <= soh.length; i++) {
    if (soh.slice(i, i + run).every((v) => v < theta)) return cycles[i];
  }
  return null;
}

// ---------------------------------------------------------------- loading a cell
function showPanels(on) {
  $("result").classList.remove("hidden");
  $("result").querySelectorAll(".panel,.kpis").forEach((el) => el.classList.toggle("hidden", !on));
}

async function loadCell() {
  stopPlay();
  try {
    const demo = $("demo").value;
    let rows, k0, truthEol = null, eolLabel = "";
    CMP = null; lastRes = null;
    if (demo) {
      const [cut, full, eol, cmp] = await Promise.all([
        fetch(`examples/${demo}.csv`).then((r) => r.text()),
        fetch(`examples/${demo}_full.csv`).then((r) => r.text()),
        fetch(`examples/${demo}_eol.json`).then((r) => (r.ok ? r.json() : null)),
        fetch(`examples/${demo}_compare.json`).then((r) => (r.ok ? r.json() : null)).catch(() => null),
      ]);
      if (cmp) CMP = buildCmp(cmp);
      rows = validate(parseCSV(full), meta.min_cycles);
      const lastCut = validate(parseCSV(cut), meta.min_cycles).cycle_idx.at(-1);
      k0 = Math.max(0, rows.cycle_idx.indexOf(lastCut));
      if (eol && Number.isFinite(eol.eol_cycle)) { truthEol = eol.eol_cycle; eolLabel = eol.label; }
    } else {
      const f = $("file").files[0];
      if (!f) throw new InputError("choose a CSV file (columns cycle_idx, capacity_ah)");
      rows = validate(parseCSV(await f.text()), meta.min_cycles);
      k0 = rows.cycle_idx.length - 1;
    }
    const ref = rows.capacity_ah.slice(0, 5).reduce((a, b) => a + b, 0) / Math.min(5, rows.capacity_ah.length);
    const soh = rows.capacity_ah.map((c) => c / ref);
    if (truthEol === null) {
      const e = sustainedEol(rows.cycle_idx, soh, meta.theta);
      if (e !== null) { truthEol = e; eolLabel = "first sustained drop below 80% in the data"; }
    }
    const at = Number(new URLSearchParams(location.search).get("at")); // shareable ?at=<cycle>
    if (at && demo) {
      const i = rows.cycle_idx.findLastIndex((cc) => cc <= at);
      if (i >= meta.min_cycles - 1) k0 = i;
    }
    S = { rows, soh, truthEol, eolLabel, k: k0, cache: new Map(), track: [], demo };
    // Predicting long after end of life is meaningless (CALCE cells were cycled to ~20% SOH):
    // stop the slider and the view 15% past the actual EOL when it is known.
    let kMax = rows.cycle_idx.length - 1;
    if (truthEol !== null) {
      const stop = truthEol + Math.max(20, 0.15 * truthEol);
      kMax = Math.max(meta.min_cycles - 1, rows.cycle_idx.findLastIndex((cc) => cc <= stop));
    }
    S.kMax = kMax;
    S.k = k0 = Math.min(k0, kMax);
    Object.assign($("origin"), { min: meta.min_cycles - 1, max: kMax, value: k0 });
    show("", "");
    showPanels(true);
    buildChips();
    drawStatic();
    await setOrigin(k0, true);
    computeTrack(); // background
  } catch (e) {
    S = null; CMP = null; lastRes = null;
    showPanels(false);
    show("err", e instanceof InputError ? `Input problem: ${escape(e.message)}` : `Unexpected error: ${escape(e.message)}`);
  }
}

// ---------------------------------------------------------------- origin control
async function setOrigin(k, force = false) {
  if (!S) return;
  k = Math.max(+$("origin").min, Math.min(+$("origin").max, Math.round(k)));
  if (!force && k === S.k && S.cache.has(k)) return;
  S.k = k;
  $("origin").value = k;
  if (busy) { pending = k; return; }
  busy = true;
  try {
    const res = await predictAt(k);
    if (S && S.k === k) render(res);
  } finally {
    busy = false;
    if (pending !== null) { const p = pending; pending = null; setOrigin(p, true); }
  }
}
$("origin").addEventListener("input", (e) => { stopPlay(); setOrigin(+e.target.value); });

/** Map a pointer position on a Plotly chart to the last cycle index at or before it. */
function pointerToK(div, ev) {
  const fl = div._fullLayout;
  if (!fl || !S) return null;
  const rect = div.getBoundingClientRect();
  const x = fl.xaxis.p2l(ev.clientX - rect.left - fl._size.l);
  const c = S.rows.cycle_idx;
  if (x <= c[0]) return 0;
  let lo = 0, hi = c.length - 1;
  while (lo < hi) { const mid = (lo + hi + 1) >> 1; if (c[mid] <= x) lo = mid; else hi = mid - 1; }
  return lo;
}
for (const id of ["plot", "plot-rul"]) {
  const div = $(id);
  let drag = false;
  const move = (ev) => { const k = pointerToK(div, ev); if (k !== null) setOrigin(k); };
  div.addEventListener("pointerdown", (ev) => { drag = true; stopPlay(); div.setPointerCapture(ev.pointerId); move(ev); });
  div.addEventListener("pointermove", (ev) => { if (drag) move(ev); });
  div.addEventListener("pointerup", () => { drag = false; });
  div.addEventListener("pointercancel", () => { drag = false; });
}

function stopPlay() { playing = false; $("play").textContent = "▶ Play"; }
$("play").addEventListener("click", async () => {
  if (playing) return stopPlay();
  if (!S) return;
  playing = true;
  $("play").textContent = "❚❚ Pause";
  const max = +$("origin").max;
  let k = S.k >= max ? +$("origin").min : S.k;
  const step = Math.max(1, Math.round(S.rows.cycle_idx.length / 150));
  while (playing && S && k <= max) {
    await setOrigin(k, true);
    await new Promise((r) => setTimeout(r, 40));
    k += step;
  }
  stopPlay();
});

// ---------------------------------------------------------------- RUL track (all origins)
async function computeTrack() {
  const s = S, n = s.rows.cycle_idx.length, kMin = meta.min_cycles - 1;
  const kEnd = s.kMax + 1;
  const stride = Math.max(1, Math.ceil((kEnd - kMin) / 300));
  for (let k = kMin, i = 0; k < kEnd && s === S; k += stride, i++) {
    const r = (await predictAt(k)).rul;
    s.track.push({ cycle: s.rows.cycle_idx[k], rul: r.cycles, lo: r.lo, hi: r.hi });
    if (i % 25 === 0) { drawTrack(); await new Promise((r2) => setTimeout(r2, 0)); }
  }
  if (s === S) drawTrack();
}

// ---------------------------------------------------------------- drawing
let xRange, yRange;
function drawStatic() {
  const c = S.rows.cycle_idx, last = c[S.kMax];
  const xmax = Math.max(last + 100, S.truthEol ?? 0) + 0.04 * last;
  xRange = [c[0], xmax];
  const vis = S.soh.filter((_, i) => c[i] <= xmax);
  const lo = Math.min(...vis, meta.theta) * 100, hi = Math.max(...vis) * 100;
  const pad = Math.max(1, (hi - lo) * 0.06);
  yRange = [lo - pad, hi + pad];
}

function base(shapes = [], annotations = []) {
  const ink = css("--ink"), line = css("--line");
  return {
    margin: { l: 56, r: 16, t: 12, b: 44 },
    paper_bgcolor: "rgba(0,0,0,0)", plot_bgcolor: "rgba(0,0,0,0)",
    font: { color: ink, family: "system-ui, sans-serif", size: 12 },
    dragmode: false, hovermode: "x unified",
    hoverlabel: { bgcolor: css("--panel"), bordercolor: line, font: { color: ink } },
    legend: { orientation: "h", y: -0.18 },
    shapes, annotations,
  };
}

function render(res) {
  lastRes = res;
  const ink = css("--ink"), muted = css("--muted"), line = css("--line");
  const k = S.k, c = S.rows.cycle_idx, last = res.last_cycle, r = res.rul;
  $("origin-label").textContent = S.truthEol !== null
    ? `cycle ${last} (${Math.round((last / S.truthEol) * 100)}% of life)`
    : `cycle ${last} (${Math.round(((k + 1) / c.length) * 100)}% of record)`;

  // KPIs
  const trueRul = S.truthEol !== null ? S.truthEol - last : null;
  $("kpis").innerHTML = [
    ["SOH at this point", pct(res.history.soh.at(-1)), `cycle ${last}`],
    ["Predicted remaining life", r.cycles < 1 ? "< 1 cycle" : `${Math.round(r.cycles)} cycles`, `90% interval ${Math.round(r.lo)}–${Math.round(r.hi)}`],
    ["Predicted end of life", `cycle ${Math.round(r.eol_cycle)}`, "80% SOH threshold"],
    trueRul !== null
      ? ["Actual remaining life", trueRul > 0 ? `${Math.round(trueRul)} cycles` : "reached", `EOL cycle ${Math.round(S.truthEol)} · ${escape(S.eolLabel)}`]
      : ["Actual remaining life", "unknown", "the data never drops below 80%"],
  ].map(([kk, v, s]) => `<div class="kpi"><div class="k">${kk}</div><div class="v">${v}</div><div class="k">${s}</div></div>`).join("");

  const o = res.ood;
  show(o.is_ood ? "warn" : "ok", o.is_ood
    ? `<b>Outside the training distribution at this point: treat intervals and RUL as unreliable.</b><ul>${o.flags.map((f) => `<li>${escape(f)}</li>`).join("")}</ul>`
    : `Inputs at this point resemble the training cells (distance ${o.distance.toFixed(1)} vs threshold ${o.threshold.toFixed(1)}), so the calibrated intervals are expected to hold.`);

  // main chart
  const fc = [last, ...res.forecast.map((f) => f.cycle)], s0 = res.history.soh.at(-1);
  const avail = cmpAvail(last);
  updateChips(avail);
  const fi = avail ? CMP.fi.get(last) : -1, sc = avail ? 100 / CMP.scale : 0;
  const sel = avail ? SEL : [];
  const cmpTraces = [], band = [];
  const bandM = sel.find((m) => CMP.models[m].forecast?.lo);
  if (bandM) {
    const f = CMP.models[bandM].forecast, st = cmpStyle(bandM), xs = CMP.h.map((h) => last + h);
    band.push(
      { x: [last, ...xs], y: [s0 * 100, ...f.hi[fi].map((v) => (v === null ? null : v * sc))], mode: "lines", line: { width: 0 }, hoverinfo: "skip", showlegend: false },
      { x: [last, ...xs], y: [s0 * 100, ...f.lo[fi].map((v) => (v === null ? null : v * sc))], mode: "lines", line: { width: 0 }, fill: "tonexty",
        fillcolor: rgba(st.color, 0.18), name: `90% interval, ${CMP.models[bandM].label}`, hoverinfo: "skip" });
  }
  for (const m of sel) {
    const f = CMP.models[m].forecast;
    if (!f) continue;
    const st = cmpStyle(m), pt = f.point[fi];
    cmpTraces.push({
      x: [last, ...CMP.h.map((h) => last + h)], y: [s0 * 100, ...pt.map((v) => (v === null ? null : v * sc))],
      mode: "lines+markers", name: CMP.models[m].label,
      line: { color: st.color, width: 1.2, dash: st.dash ?? "dot" },
      marker: { size: [0, ...CMP.h.map(() => 8)], symbol: st.symbol, color: st.color, line: { width: 1, color: css("--panel") } },
      customdata: [[0, null, null], ...CMP.h.map((h, i) => [h, f.lo ? f.lo[fi][i] * sc : null, f.hi ? f.hi[fi][i] * sc : null])],
      hovertemplate: "+%{customdata[0]}: %{y:.1f}%" + (f.lo ? " (90%: %{customdata[1]:.1f}–%{customdata[2]:.1f}%)" : "") + `<extra>${escape(CMP.models[m].label)}</extra>`,
    });
  }
  const traces = [
    { x: fc, y: [s0, ...res.forecast.map((f) => f.hi)].map((v) => v * 100), mode: "lines", line: { width: 0 }, hoverinfo: "skip", showlegend: false },
    { x: fc, y: [s0, ...res.forecast.map((f) => f.lo)].map((v) => v * 100), mode: "lines", line: { width: 0 }, fill: "tonexty",
      fillcolor: rgba(ink, 0.13), name: "90% interval, live", hoverinfo: "skip" },
    ...band,
    { x: c.slice(0, k + 1), y: S.soh.slice(0, k + 1).map((v) => v * 100), mode: "lines", name: "seen by the model",
      line: { color: "#1f5f99", width: 2 }, hovertemplate: "SOH %{y:.1f}%<extra>measured</extra>" },
    { x: c.slice(k), y: S.soh.slice(k).map((v) => v * 100), mode: "lines", name: "measured later (hidden from the model)",
      line: { color: muted, dash: "dot", width: 1.5 }, hovertemplate: "SOH %{y:.1f}%<extra>measured later</extra>" },
    ...cmpTraces,
    { x: fc, y: [s0, ...res.forecast.map((f) => f.soh)].map((v) => v * 100), mode: "lines+markers", name: LIVE_LABEL,
      line: { color: ink, width: 3.5 }, marker: { size: 9, color: ink, line: { width: 1.5, color: css("--panel") } },
      customdata: [[0, s0 * 100, s0 * 100], ...res.forecast.map((f) => [f.horizon, f.lo * 100, f.hi * 100])],
      hovertemplate: "+%{customdata[0]} cycles: %{y:.1f}% (90%: %{customdata[1]:.1f}–%{customdata[2]:.1f}%)<extra>live model</extra>" },
  ];
  const shapes = [
    { type: "rect", xref: "x", yref: "paper", x0: last + r.lo, x1: last + r.hi, y0: 0, y1: 1, fillcolor: "rgba(214,160,0,0.13)", line: { width: 0 }, layer: "below" },
    { type: "line", xref: "x", yref: "paper", x0: last, x1: last, y0: 0, y1: 1, line: { color: ink, width: 2 } },
    { type: "line", xref: "x", yref: "paper", x0: r.eol_cycle, x1: r.eol_cycle, y0: 0, y1: 1, line: { color: "#b8860b", dash: "dash", width: 2 } },
    { type: "line", xref: "paper", yref: "y", x0: 0, x1: 1, y0: 80, y1: 80, line: { color: "#b22222", width: 1.5 } },
  ];
  const ann = [
    { x: last, y: 1, yref: "paper", text: "◀ drag ▶", showarrow: false, yanchor: "bottom", font: { color: ink, size: 11 } },
    { x: r.eol_cycle, y: 0.02, yref: "paper", text: "predicted EOL", showarrow: false, xanchor: "left", yanchor: "bottom", font: { color: "#b8860b", size: 11 } },
    { x: 0, xref: "paper", y: 80, text: "80% threshold", showarrow: false, xanchor: "left", yanchor: "bottom", font: { color: "#b22222", size: 11 } },
  ];
  if (S.truthEol !== null) {
    shapes.push({ type: "line", xref: "x", yref: "paper", x0: S.truthEol, x1: S.truthEol, y0: 0, y1: 1, line: { color: muted, dash: "dot", width: 1.5 } });
    ann.push({ x: S.truthEol, y: 0.92, yref: "paper", text: "actual EOL ", showarrow: false, xanchor: "right", font: { color: muted, size: 11 } });
  }
  const lay = base(shapes, ann);
  lay.margin.t = 24;
  lay.xaxis = { title: "cycle", gridcolor: line, range: xRange, fixedrange: true };
  lay.yaxis = { title: "state of health (%)", gridcolor: line, range: yRange, fixedrange: true };
  Plotly.react("plot", traces, lay, { responsive: true, displayModeBar: false });
  drawTrack();
  renderCmpTable(res, sel, fi);

  $("ftable").innerHTML =
    "<tr><th>Horizon</th><th>Cycle</th><th>SOH forecast</th><th>90% interval</th><th>Measured</th></tr>" +
    res.forecast.map((f) => {
      const i = c.indexOf(f.cycle);
      return `<tr><td>+${f.horizon}</td><td>${f.cycle}</td><td>${pct(f.soh)}</td><td>${pct(f.lo)} – ${pct(f.hi)}</td><td>${i >= 0 ? pct(S.soh[i]) : "–"}</td></tr>`;
    }).join("");
}

function renderCmpTable(res, sel, fi) {
  const c = S.rows.cycle_idx, last = res.last_cycle, trueRul = S.truthEol !== null && S.truthEol - last > 0 ? S.truthEol - last : null;
  const H = 50, hv = res.forecast.find((f) => f.horizon === H);
  const iM = c.indexOf(last + H), meas = iM >= 0 ? S.soh[iM] : null;
  const rows = [{ name: LIVE_LABEL, color: css("--ink"), live: true, soh: hv?.soh, lo: hv?.lo, hi: hv?.hi,
    rul: res.rul.cycles, rlo: res.rul.lo, rhi: res.rul.hi }];
  if (fi >= 0) {
    const hi = CMP.h.indexOf(H), ri = CMP.ri.get(last);
    for (const m of sel) {
      const e = CMP.models[m], f = e.forecast, r = e.rul, v = (x) => (x == null ? null : x / CMP.scale);
      rows.push({ name: e.label, color: cmpStyle(m).color, soh: hi >= 0 && f ? v(f.point[fi][hi]) : null,
        lo: hi >= 0 && f?.lo ? v(f.lo[fi][hi]) : null, hi: hi >= 0 && f?.hi ? v(f.hi[fi][hi]) : null,
        rul: ri !== undefined && r ? r.point[ri] : null, rlo: ri !== undefined && r?.lo ? r.lo[ri] : null, rhi: ri !== undefined && r?.hi ? r.hi[ri] : null });
    }
  }
  for (const r of rows) r.err = trueRul !== null && r.rul != null ? r.rul - trueRul : null;
  if (trueRul !== null) rows.sort((a, b) => (a.err === null) - (b.err === null) || Math.abs(a.err ?? 0) - Math.abs(b.err ?? 0));
  const sgn = (v, u, d = 0) => `${v > 0 ? "+" : v < 0 ? "−" : ""}${Math.abs(v).toFixed(d)}${u}`;
  $("cmptable").innerHTML = `<tr><th>Method</th><th>SOH at +${H}</th><th>error vs measured</th><th>Predicted RUL (90%)</th><th>RUL error</th></tr>` +
    rows.map((r) => `<tr${r.live ? ' class="live"' : ""}><td><span class="sw" style="background:${r.color}"></span>${escape(r.name)}</td>` +
      `<td>${r.soh != null ? pct(r.soh) : "–"}${r.lo != null && r.hi != null ? ` <span class="muted">(${pct(r.lo)}–${pct(r.hi)})</span>` : ""}</td>` +
      `<td>${r.soh != null && meas !== null ? sgn((r.soh - meas) * 100, " pp", 1) : "–"}</td>` +
      `<td>${r.rul != null ? Math.round(r.rul) : "–"}${r.rlo != null && r.rhi != null ? ` <span class="muted">(${Math.round(r.rlo)}–${Math.round(r.rhi)})</span>` : ""}</td>` +
      `<td>${r.err !== null ? sgn(r.err, " cycles") : "–"}</td></tr>`).join("");
  $("cmpnote").textContent = [
    meas === null ? `Measured SOH at +${H} cycles is not known (past the end of the data).` : "",
    trueRul === null ? "Actual remaining life is unknown or already reached, so rows are not ranked." : "Sorted by absolute RUL error.",
    fi < 0 ? "Benchmarked methods are shown for the demo cells only." : "",
  ].filter(Boolean).join(" ");
}

function cmpRulTrace(m) {
  let t = CMP.rulCache.get(m);
  if (!t) {
    const r = CMP.models[m].rul;
    if (!r) return null;
    t = { x: CMP.rulOrigin, y: r.point.map((v) => v), lo: r.lo, hi: r.hi };
    CMP.rulCache.set(m, t);
  }
  return t;
}

function drawTrack() {
  if (!S) return;
  const ink = css("--ink"), muted = css("--muted"), line = css("--line");
  const t = S.track, x = t.map((p) => p.cycle);
  const cap = S.rows.cycle_idx[S.kMax];
  const cmpT = [];
  if (cmpAvail(S.rows.cycle_idx[S.k])) {
    for (const m of SEL) {
      const r = cmpRulTrace(m);
      if (!r) continue;
      const n = r.x.findIndex((o) => o > cap), e = n < 0 ? r.x.length : n, st = cmpStyle(m);
      cmpT.push({ x: r.x.slice(0, e), y: r.y.slice(0, e), mode: "lines", name: CMP.models[m].label,
        line: { color: st.color, width: 1.8, dash: st.dash ?? "solid" }, connectgaps: false,
        hovertemplate: `%{y:.0f} cycles<extra>${escape(CMP.models[m].label)}</extra>` });
    }
  }
  const traces = [
    { x, y: t.map((p) => p.hi), mode: "lines", line: { width: 0 }, hoverinfo: "skip", showlegend: false },
    { x, y: t.map((p) => p.lo), mode: "lines", line: { width: 0 }, fill: "tonexty", fillcolor: rgba(ink, 0.1), name: "90% interval, live", hoverinfo: "skip" },
    ...cmpT,
    { x, y: t.map((p) => p.rul), mode: "lines", name: LIVE_LABEL, line: { color: ink, width: 3.5 },
      customdata: t.map((p) => [p.lo, p.hi]), hovertemplate: "%{y:.0f} (90%: %{customdata[0]:.0f}–%{customdata[1]:.0f}) cycles<extra>live model</extra>" },
  ];
  if (S.truthEol !== null) {
    const tx = S.rows.cycle_idx.filter((cc) => cc <= S.truthEol);
    traces.push(
      { x: tx, y: tx.map((cc) => (S.truthEol - cc) * 1.2), mode: "lines", line: { color: muted, dash: "dot", width: 1 }, name: "±20% of truth", hoverinfo: "skip" },
      { x: tx, y: tx.map((cc) => (S.truthEol - cc) * 0.8), mode: "lines", line: { color: muted, dash: "dot", width: 1 }, showlegend: false, hoverinfo: "skip" },
      { x: tx, y: tx.map((cc) => S.truthEol - cc), mode: "lines", name: "true RUL", line: { color: "#b22222", width: 2, dash: "dash" },
        hovertemplate: "true %{y:.0f} cycles<extra></extra>" },
    );
  }
  const cur = S.rows.cycle_idx[S.k];
  const lay = base([{ type: "line", xref: "x", yref: "paper", x0: cur, x1: cur, y0: 0, y1: 1, line: { color: ink, width: 2 } }]);
  lay.margin.b = 70;
  lay.legend.y = -0.3;
  lay.xaxis = { title: "prediction point (cycle)", gridcolor: line, range: xRange, fixedrange: true };
  lay.yaxis = { title: "remaining useful life (cycles)", gridcolor: line, rangemode: "tozero", fixedrange: true };
  Plotly.react("plot-rul", traces, lay, { responsive: true, displayModeBar: false });
}

load();
