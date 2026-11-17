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
    if (demo) {
      const [cut, full, eol] = await Promise.all([
        fetch(`examples/${demo}.csv`).then((r) => r.text()),
        fetch(`examples/${demo}_full.csv`).then((r) => r.text()),
        fetch(`examples/${demo}_eol.json`).then((r) => (r.ok ? r.json() : null)),
      ]);
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
    drawStatic();
    await setOrigin(k0, true);
    computeTrack(); // background
  } catch (e) {
    S = null;
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
  const traces = [
    { x: fc, y: [s0, ...res.forecast.map((f) => f.hi)].map((v) => v * 100), mode: "lines", line: { width: 0 }, hoverinfo: "skip", showlegend: false },
    { x: fc, y: [s0, ...res.forecast.map((f) => f.lo)].map((v) => v * 100), mode: "lines", line: { width: 0 }, fill: "tonexty",
      fillcolor: "rgba(214,96,0,0.22)", name: "90% interval", hoverinfo: "skip" },
    { x: c.slice(0, k + 1), y: S.soh.slice(0, k + 1).map((v) => v * 100), mode: "lines", name: "seen by the model",
      line: { color: "#1f5f99", width: 2 }, hovertemplate: "SOH %{y:.1f}%<extra>measured</extra>" },
    { x: c.slice(k), y: S.soh.slice(k).map((v) => v * 100), mode: "lines", name: "measured later (hidden from the model)",
      line: { color: muted, dash: "dot", width: 1.5 }, hovertemplate: "SOH %{y:.1f}%<extra>measured later</extra>" },
    { x: fc, y: [s0, ...res.forecast.map((f) => f.soh)].map((v) => v * 100), mode: "lines+markers", name: "forecast (median)",
      line: { color: "#d66000", width: 2.5 }, marker: { size: 7 },
      customdata: [[0, s0 * 100, s0 * 100], ...res.forecast.map((f) => [f.horizon, f.lo * 100, f.hi * 100])],
      hovertemplate: "+%{customdata[0]} cycles: %{y:.1f}% (90%: %{customdata[1]:.1f}–%{customdata[2]:.1f}%)<extra>forecast</extra>" },
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

  $("ftable").innerHTML =
    "<tr><th>Horizon</th><th>Cycle</th><th>SOH forecast</th><th>90% interval</th><th>Measured</th></tr>" +
    res.forecast.map((f) => {
      const i = c.indexOf(f.cycle);
      return `<tr><td>+${f.horizon}</td><td>${f.cycle}</td><td>${pct(f.soh)}</td><td>${pct(f.lo)} – ${pct(f.hi)}</td><td>${i >= 0 ? pct(S.soh[i]) : "–"}</td></tr>`;
    }).join("");
}

function drawTrack() {
  if (!S) return;
  const ink = css("--ink"), muted = css("--muted"), line = css("--line");
  const t = S.track, x = t.map((p) => p.cycle);
  const traces = [
    { x, y: t.map((p) => p.hi), mode: "lines", line: { width: 0 }, hoverinfo: "skip", showlegend: false },
    { x, y: t.map((p) => p.lo), mode: "lines", line: { width: 0 }, fill: "tonexty", fillcolor: "rgba(31,95,153,0.18)", name: "90% interval", hoverinfo: "skip" },
    { x, y: t.map((p) => p.rul), mode: "lines", name: "predicted RUL", line: { color: "#1f5f99", width: 2 },
      customdata: t.map((p) => [p.lo, p.hi]), hovertemplate: "predicted %{y:.0f} (90%: %{customdata[0]:.0f}–%{customdata[1]:.0f}) cycles<extra></extra>" },
  ];
  if (S.truthEol !== null) {
    const tx = S.rows.cycle_idx.filter((cc) => cc <= S.truthEol);
    traces.push(
      { x: tx, y: tx.map((cc) => (S.truthEol - cc) * 1.2), mode: "lines", line: { color: muted, dash: "dot", width: 1 }, name: "±20% of truth", hoverinfo: "skip" },
      { x: tx, y: tx.map((cc) => (S.truthEol - cc) * 0.8), mode: "lines", line: { color: muted, dash: "dot", width: 1 }, showlegend: false, hoverinfo: "skip" },
      { x: tx, y: tx.map((cc) => S.truthEol - cc), mode: "lines", name: "true RUL", line: { color: ink, width: 1.5 },
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
