// UI for the static Space: loads the ONNX graphs, runs them with onnxruntime-web, draws results.
import { InputError, parseCSV, postprocess, prepare, validate } from "./core.mjs";

const DEMOS = [
  ["nasa_B0018", "NASA B0018 (LiCoO₂-type 18650)"],
  ["calce_CS2_38", "CALCE CS2_38 (LiCoO₂ prismatic)"],
  ["toyota_b1c1", "Toyota/MIT b1c1 (LFP, fast-charge)"],
];
const $ = (id) => document.getElementById(id);
let meta, sessF, sessR;

// ---------- tabs ----------
for (const b of document.querySelectorAll("nav button")) {
  b.addEventListener("click", () => {
    for (const o of document.querySelectorAll("nav button")) o.setAttribute("aria-selected", String(o === b));
    for (const t of ["predict", "format", "about"]) $(`tab-${t}`).classList.toggle("hidden", t !== b.dataset.tab);
    if (b.dataset.tab === "predict" && !$("result").classList.contains("hidden")) Plotly.Plots.resize("plot");
  });
}
const tmpl = "cycle_idx,capacity_ah\n" + Array.from({ length: 12 }, (_, i) => `${i + 1},${(2 - 0.004 * i).toFixed(4)}`).join("\n");
$("template").href = "data:text/csv;charset=utf-8," + encodeURIComponent(tmpl + "\n");

for (const [v, label] of DEMOS) $("demo").add(new Option(label, v));
$("demo").addEventListener("change", () => $("upload-wrap").classList.toggle("hidden", $("demo").value !== ""));

function show(kind, html) {
  $("msg").innerHTML = html ? `<div class="banner ${kind}">${html}</div>` : "";
}

// ---------- model ----------
async function load() {
  try {
    ort.env.wasm.numThreads = 1;
    meta = await (await fetch("serve_meta.json")).json();
    [sessF, sessR] = await Promise.all([
      ort.InferenceSession.create("forecast.onnx"),
      ort.InferenceSession.create("rul.onnx"),
    ]);
    $("run").disabled = false;
    $("run").textContent = "Predict";
    const demo = new URLSearchParams(location.search).get("demo");  // shareable ?demo=<cell>
    if (demo && DEMOS.some(([v]) => v === demo)) {
      $("demo").value = demo;
      $("demo").dispatchEvent(new Event("change"));
      $("run").click();
    }
  } catch (e) {
    show("err", `Could not load the model (${e.message}). Reload the page to retry.`);
  }
}

async function infer(sess, hist, L, tab) {
  const out = await sess.run({
    hist: new ort.Tensor("float32", hist, [1, L, 2]),
    tab: new ort.Tensor("float32", tab, [1, 5]),
  });
  return out.q.data;
}

async function readInput() {
  const demo = $("demo").value;
  if (demo) {
    const [inp, full, eol] = await Promise.all([
      fetch(`examples/${demo}.csv`).then((r) => r.text()),
      fetch(`examples/${demo}_full.csv`).then((r) => (r.ok ? r.text() : null)),
      fetch(`examples/${demo}_eol.json`).then((r) => (r.ok ? r.json() : null)),
    ]);
    return { data: parseCSV(inp), truth: full ? parseCSV(full) : null, eol };
  }
  const f = $("file").files[0];
  if (!f) throw new InputError("upload a CSV file or pick a demo cell");
  return { data: parseCSV(await f.text()), truth: null, eol: null };
}

// ---------- run ----------
$("run").addEventListener("click", async () => {
  $("run").disabled = true;
  try {
    const { data, truth, eol } = await readInput();
    const rows = validate(data, meta.min_cycles);
    const p = prepare(meta, rows);
    const qf = await infer(sessF, p.histF, meta.tasks.forecast.lookback, p.tab);
    const qr = await infer(sessR, p.histR, meta.tasks.rul.lookback, p.tab);
    const res = postprocess(meta, rows.cycle_idx, p.soh, p.tab, qf, qr);
    render(res, truth, eol);
  } catch (e) {
    $("result").classList.add("hidden");
    show("err", e instanceof InputError ? `Input problem: ${escape(e.message)}` : `Unexpected error: ${escape(e.message)}`);
  } finally {
    $("run").disabled = false;
  }
});

const escape = (s) => String(s).replace(/[&<>]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" })[c]);
const pct = (v) => `${(v * 100).toFixed(1)}%`;

function css(name) {
  return getComputedStyle(document.documentElement).getPropertyValue(name).trim();
}

function render(res, truth, eol) {
  const o = res.ood;
  show(
    o.is_ood ? "warn" : "ok",
    o.is_ood
      ? `<b>Outside the training distribution: treat intervals and RUL as unreliable.</b><ul>${o.flags.map((f) => `<li>${escape(f)}</li>`).join("")}</ul>`
      : `Inputs resemble the training cells (distance ${o.distance.toFixed(1)} vs threshold ${o.threshold.toFixed(1)}), so the calibrated intervals are expected to hold.`,
  );
  $("result").classList.remove("hidden");

  const last = res.last_cycle, r = res.rul;
  const truthEol = eol && Number.isFinite(eol.eol_cycle) ? eol.eol_cycle : null;
  $("kpis").innerHTML = [
    ["Current SOH", pct(res.history.soh.at(-1)), `cycle ${last}`],
    ["Remaining useful life", `${Math.round(r.cycles)} cycles`, `90% interval ${Math.round(r.lo)}–${Math.round(r.hi)}`],
    ["Predicted end of life", `cycle ${Math.round(r.eol_cycle)}`, `80% SOH threshold`],
    ...(truthEol !== null
      ? [["Actual end of life (hidden)", `cycle ${Math.round(truthEol)}`, `true RUL ${Math.round(truthEol - last)} cycles`]]
      : []),
  ].map(([k, v, s]) => `<div class="kpi"><div class="k">${k}</div><div class="v">${v}</div><div class="k">${s}</div></div>`).join("");
  if (r.already_below_threshold) {
    $("kpis").insertAdjacentHTML("beforeend", `<div class="kpi"><div class="k">Note</div><div>Already below 80% SOH: past end of life by the usual definition.</div></div>`);
  }

  $("ftable").innerHTML =
    "<tr><th>Horizon</th><th>Cycle</th><th>SOH forecast</th><th>90% interval</th></tr>" +
    res.forecast.map((f) => `<tr><td>+${f.horizon}</td><td>${f.cycle}</td><td>${pct(f.soh)}</td><td>${pct(f.lo)} – ${pct(f.hi)}</td></tr>`).join("");

  const ink = css("--ink"), muted = css("--muted"), line = css("--line");
  const fc = [last, ...res.forecast.map((f) => f.cycle)];
  const s0 = res.history.soh.at(-1);
  const traces = [
    { x: fc, y: [s0, ...res.forecast.map((f) => f.hi)].map((v) => v * 100), mode: "lines", line: { width: 0 }, hoverinfo: "skip", showlegend: false },
    { x: fc, y: [s0, ...res.forecast.map((f) => f.lo)].map((v) => v * 100), mode: "lines", line: { width: 0 }, fill: "tonexty", fillcolor: "rgba(214,96,0,0.22)", name: "90% interval" },
    { x: res.history.cycle, y: res.history.soh.map((v) => v * 100), mode: "lines", name: "measured SOH", line: { color: "#1f5f99", width: 2 } },
  ];
  if (truth) {
    const tr = validate(truth, 1);
    const ref = tr.capacity_ah.slice(0, 5).reduce((a, b) => a + b, 0) / Math.min(5, tr.capacity_ah.length);
    const idx = tr.cycle_idx.map((c, i) => [c, i]).filter(([c]) => c > last);
    traces.push({ x: idx.map(([c]) => c), y: idx.map(([, i]) => (tr.capacity_ah[i] / ref) * 100), mode: "lines", name: "measured later (hidden)", line: { color: muted, dash: "dot", width: 1.5 } });
  }
  traces.push({ x: fc, y: [s0, ...res.forecast.map((f) => f.soh)].map((v) => v * 100), mode: "lines+markers", name: "forecast (median)", line: { color: "#d66000", width: 2.5 }, marker: { size: 6 } });
  const xmax = Math.max(last + r.hi, truthEol ?? 0, fc.at(-1)) * 1.04;
  // y-range from what is visible (hidden-truth points beyond xmax would squash the plot)
  const vis = traces.flatMap((t) => t.y.filter((_, i) => t.x[i] <= xmax));
  const ylo = Math.min(...vis, 80), yhi = Math.max(...vis);
  const pad = Math.max(1, (yhi - ylo) * 0.06);
  const shapes = [
    { type: "rect", xref: "x", yref: "paper", x0: last + r.lo, x1: last + r.hi, y0: 0, y1: 1, fillcolor: "rgba(214,160,0,0.15)", line: { width: 0 } },
    { type: "line", xref: "x", yref: "paper", x0: r.eol_cycle, x1: r.eol_cycle, y0: 0, y1: 1, line: { color: "#b8860b", dash: "dash", width: 2 } },
    { type: "line", xref: "paper", yref: "y", x0: 0, x1: 1, y0: 80, y1: 80, line: { color: "#b22222", width: 1.5 } },
  ];
  if (truthEol !== null) shapes.push({ type: "line", xref: "x", yref: "paper", x0: truthEol, x1: truthEol, y0: 0, y1: 1, line: { color: ink, dash: "dot", width: 1.5 } });
  const annotations = [
    { x: r.eol_cycle, y: 1, yref: "paper", text: "predicted EOL", showarrow: false, yanchor: "bottom", font: { color: "#b8860b", size: 11 } },
    { x: 0, xref: "paper", y: 80, text: "80% threshold", showarrow: false, xanchor: "left", yanchor: "bottom", font: { color: "#b22222", size: 11 } },
  ];
  if (truthEol !== null) annotations.push({ x: truthEol, y: 0.93, yref: "paper", text: "actual EOL ", showarrow: false, xanchor: "right", font: { color: ink, size: 11 } });
  Plotly.newPlot("plot", traces, {
    margin: { l: 56, r: 16, t: 28, b: 48 },
    paper_bgcolor: "rgba(0,0,0,0)", plot_bgcolor: "rgba(0,0,0,0)",
    font: { color: ink, family: "system-ui, sans-serif" },
    xaxis: { title: "cycle", gridcolor: line, range: [res.history.cycle[0], xmax] },
    yaxis: { title: "state of health (%)", gridcolor: line, range: [ylo - pad, yhi + pad] },
    legend: { orientation: "h", y: -0.2 },
    shapes, annotations,
  }, { responsive: true, displaylogo: false });
}

load();
