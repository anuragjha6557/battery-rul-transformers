// Field mode of the static demo (ADR-0022): SOH estimate, forecast and RUL from BMS signals only,
// no capacity log. Processing lives in field.mjs (parity-tested against the Python FieldPredictor);
// this file is DOM + chart only. Everything runs in the browser; uploaded data is never sent anywhere.
// The mode switch stays hidden unless field/<protocol>/field_serve_meta.json exists (Space without
// field artifacts => lab-only page).
import { InputError, predictField } from "./field.mjs";

const $ = (id) => document.getElementById(id);
const PROTOCOLS = [["nasa", "NASA (18650 cells)"], ["calce", "CALCE (CS2 prismatic)"], ["toyota", "Toyota/MIT (LFP fast charge)"]];
const metas = {}, sessions = {};
let DEMOS = [];
let busy = false, ran = false;

const escape = (s) => String(s).replace(/[&<>]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" })[c]);
const pct = (v, d = 1) => `${(v * 100).toFixed(d)}%`;
const css = (n) => getComputedStyle(document.documentElement).getPropertyValue(n).trim();
const rgba = (hex, a) => {
  const m = /^#?([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})$/i.exec(hex);
  return m ? `rgba(${parseInt(m[1], 16)},${parseInt(m[2], 16)},${parseInt(m[3], 16)},${a})` : hex;
};
const show = (kind, html) => { $("f-msg").innerHTML = html ? `<div class="banner ${kind}">${html}</div>` : ""; };

// ---------------------------------------------------------------- mode switch
function setMode(field) {
  $("lab").classList.toggle("hidden", field);
  $("field").classList.toggle("hidden", !field);
  $("mode-lab").setAttribute("aria-pressed", String(!field));
  $("mode-field").setAttribute("aria-pressed", String(field));
  const url = new URL(location.href);
  if (field) url.searchParams.set("mode", "field"); else url.searchParams.delete("mode");
  history.replaceState(null, "", url);
  if (field && $("plot-field").data) Plotly.Plots.resize("plot-field");
  else if (field && !ran) run();
}
$("mode-lab").addEventListener("click", () => setMode(false));
$("mode-field").addEventListener("click", () => setMode(true));

// ---------------------------------------------------------------- protocol / cell pickers
const meta = () => metas[$("f-proto").value];

function fillProtocol() {
  const m = meta();
  const need = m.inputs.map((c) => `<code>${escape(c)}</code>`).join(" ");
  $("f-cols").innerHTML =
    `<b>${escape(m.protocol)} input contract.</b> One row per cycle. Required: <code>cycle_idx</code>. Signals (blank allowed; a missing column is treated as unobserved and flagged): ${need.replace(/^<code>cycle_idx<\/code> /, "")}. ` +
    `Optional <code>charge_time_s</code> (only used to detect paused charges, never a model input). Other columns are ignored. Needs at least ${m.min_cycles} cycles; ${Math.max(...Object.values(m.tasks).map((t) => t.lookback))} or more fill the model's window.`;
  const demos = DEMOS.filter((d) => d.protocol === m.protocol);
  $("f-demo").innerHTML = "";
  for (const d of demos) $("f-demo").add(new Option(`${d.label} · ${d.n_cycles} cycles`, d.name));
  $("f-demo").add(new Option("Upload my own CSV", ""));
  $("f-demo").dispatchEvent(new Event("change"));
}
$("f-proto").addEventListener("change", fillProtocol);
$("f-demo").addEventListener("change", () => {
  $("f-upload-wrap").classList.toggle("hidden", $("f-demo").value !== "");
  if ($("f-demo").value && !$("field").classList.contains("hidden")) run(); // no model download in lab mode
});
$("f-run").addEventListener("click", run);
$("f-file").addEventListener("change", run);

// ---------------------------------------------------------------- inference
async function session(proto, task) {
  const key = `${proto}/${task}`;
  sessions[key] ??= ort.InferenceSession.create(`field/${proto}/${task}.onnx`);
  return sessions[key];
}

async function run() {
  if (busy) return;
  busy = true;
  ran = true;
  $("f-run").disabled = true;
  try {
    const m = meta(), demo = $("f-demo").value;
    let text;
    if (demo) {
      const r = await fetch(`examples/field/${demo}.csv`);
      if (!r.ok) throw new Error(`demo file ${demo}.csv not found`);
      text = await r.text();
    } else {
      const f = $("f-file").files[0];
      if (!f) throw new InputError("choose a CSV file (see the required columns above)");
      text = await f.text();
    }
    const infer = async (task, hist, tab) => {
      const L = m.tasks[task].lookback, W = m.channels.length + 1;
      const out = await (await session(m.protocol, task)).run({
        hist: new ort.Tensor("float32", hist, [1, L, W]),
        tab: new ort.Tensor("float32", tab, [1, 1]),
      });
      return out.q.data;
    };
    const { table, frame, result } = await predictField(m, text, infer);
    const meas = table.cols.get("soh_measured");
    const measured = meas ? { cycle: frame.cycle_idx, soh: Array.from(frame.order, (i) => meas[i]) } : null;
    $("f-result").classList.remove("hidden");
    $("f-result").querySelectorAll(".panel,.kpis").forEach((el) => el.classList.remove("hidden"));
    render(m, result, measured);
  } catch (e) {
    $("f-result").classList.remove("hidden");
    $("f-result").querySelectorAll(".panel,.kpis").forEach((el) => el.classList.add("hidden"));
    show("err", e instanceof InputError ? `Input problem: ${escape(e.message)}` : `Unexpected error: ${escape(e.message)}`);
  } finally {
    busy = false;
    $("f-run").disabled = false;
  }
}

// ---------------------------------------------------------------- rendering
const tag = (useful) => (useful ? '<span class="tag ok">informative</span>' : '<span class="tag">uninformative</span>');

function render(m, r, measured) {
  const s = r.soh_now, u = r.rul;
  const cleanTxt = Object.entries(r.cleaning).map(([k, v]) => `${escape(k)} ${v}`).join(", ");
  $("f-kpis").innerHTML = [
    ["SOH estimate now (cycle " + r.last_cycle + ")", `${pct(s.soh)}${tag(s.useful)}`, `90% interval ${pct(s.lo)} – ${pct(s.hi)}`],
    u.already_below_threshold
      ? ["Remaining useful life", "already below 80% SOH", "RUL is only trained for cells above the threshold"]
      : ["Remaining useful life", u.cycles < 1 ? "< 1 cycle" : `${Math.round(u.cycles)} cycles`, `90% interval ${Math.round(u.lo)} – ${Math.round(u.hi)} · end of life near cycle ${Math.round(u.eol_cycle)}`],
    ["Uploaded", `${r.n_cycles} cycles`, `input cleaning: ${cleanTxt || "nothing masked"}`],
  ].map(([k, v, sub]) => `<div class="kpi"><div class="k">${k}</div><div class="v">${v}</div><div class="k">${sub}</div></div>`).join("");

  const o = r.ood;
  show(o.is_ood ? "warn" : "ok", o.is_ood
    ? `<b>Outside the training distribution: treat intervals and RUL as unreliable.</b><ul>${o.flags.map((f) => `<li>${escape(f)}</li>`).join("")}</ul>`
    : `The latest cycle's signals resemble the ${escape(m.protocol)} training cycles (distance ${o.distance.toFixed(1)} vs threshold ${o.threshold.toFixed(1)}). This guard is weak under batch shift (see the warning above), so it does not certify the intervals.`);

  drawChart(m, r, measured);

  $("f-table").innerHTML =
    "<tr><th>Horizon</th><th>Cycle</th><th>SOH forecast</th><th>90% interval</th><th>Interval</th><th>Measured (not used)</th></tr>" +
    [{ horizon: 0, cycle: r.last_cycle, ...s }, ...r.forecast].map((f) => {
      const i = measured ? measured.cycle.indexOf(f.cycle) : -1;
      const v = i >= 0 ? measured.soh[i] : NaN;
      return `<tr><td>${f.horizon ? "+" + f.horizon : "now"}</td><td>${f.cycle}</td><td>${pct(f.soh)}</td><td>${pct(f.lo)} – ${pct(f.hi)}</td><td>${f.useful ? "informative" : "uninformative"}</td><td>${Number.isFinite(v) ? pct(v) : "–"}</td></tr>`;
    }).join("");

  const h = Object.entries(r.heldout ?? {}).map(([split, t]) => {
    const a = t.soh?.["overall/rmse"], c = t.soh?.picp_h0, rc = t.rul?.picp_h0;
    return a == null ? "" : `${escape(split)}: SOH RMSE ${a.toFixed(2)} % SOH, 90% interval coverage ${c?.toFixed(2)} (SOH), ${rc?.toFixed(2)} (RUL)`;
  }).filter(Boolean);
  $("f-heldout").textContent = h.length ? `Held-out cells of this protocol (benchmark, seed 0), all origins: ${h.join(" · ")}.` : "";
}

function drawChart(m, r, measured) {
  const ink = css("--ink"), muted = css("--muted"), line = css("--line"), accent = css("--accent");
  const pts = [{ cycle: r.last_cycle, soh: r.soh_now.soh, lo: r.soh_now.lo, hi: r.soh_now.hi, useful: r.soh_now.useful, horizon: 0 }, ...r.forecast];
  // a band segment between two points is "informative" when the interval at its far end is
  const seg = (i) => pts[i + 1].useful;
  const polys = [];
  let shownA = false, shownB = false;
  for (let i = 0; i < pts.length - 1; i++) {
    const a = pts[i], b = pts[i + 1], good = seg(i);
    const first = good ? !shownA : !shownB;
    if (good) shownA = true; else shownB = true;
    polys.push({
      x: [a.cycle, b.cycle, b.cycle, a.cycle], y: [a.hi, b.hi, b.lo, a.lo].map((v) => v * 100), type: "scatter", mode: "lines",
      fill: "toself", line: { width: 0 }, hoverinfo: "skip", showlegend: first,
      name: good ? "90% interval (informative)" : "90% interval, uninformative (hatched)",
      legendgroup: good ? "good" : "bad",
      fillcolor: good ? rgba(ink, 0.16) : "rgba(0,0,0,0)",
      ...(good ? {} : { fillpattern: { shape: "/", size: 6, solidity: 0.25, fgcolor: muted, bgcolor: "rgba(0,0,0,0)", fgopacity: 0.6 } }),
    });
  }
  const traces = [...polys];
  if (measured) {
    traces.push({ x: measured.cycle, y: measured.soh.map((v) => v * 100), mode: "lines", name: "measured (not used by the model)",
      line: { color: muted, dash: "dot", width: 1.5 }, hovertemplate: "measured %{y:.1f}%<extra></extra>" });
  }
  traces.push({
    x: pts.map((p) => p.cycle), y: pts.map((p) => p.soh * 100), mode: "lines+markers", name: "model estimate / forecast",
    line: { color: ink, width: 3 }, marker: { size: 8, color: ink, line: { width: 1.5, color: css("--panel") } },
    customdata: pts.map((p) => [p.horizon, p.lo * 100, p.hi * 100, p.useful ? "informative" : "uninformative"]),
    hovertemplate: "%{customdata[0]:+d} cycles: %{y:.1f}% (90%: %{customdata[1]:.1f}–%{customdata[2]:.1f}%, %{customdata[3]})<extra></extra>",
  });
  const lastX = r.last_cycle, maxH = Math.max(...m.tasks.forecast.horizons);
  const x0 = measured ? measured.cycle[0] : lastX - maxH, x1 = lastX + maxH * 1.08;
  const vis = [...pts.flatMap((p) => [p.lo, p.hi]), 0.8, ...(measured ? measured.soh.filter((_, i) => measured.cycle[i] <= x1) : [])].filter(Number.isFinite);
  const y0 = Math.min(...vis) * 100, y1 = Math.max(...vis) * 100, pad = Math.max(1, (y1 - y0) * 0.06);
  const bad = pts.slice(1).find((p) => !p.useful);
  const ann = [
    { x: 0, xref: "paper", y: 80, text: "80% threshold", showarrow: false, xanchor: "left", yanchor: "bottom", font: { color: "#b22222", size: 11 } },
    { x: lastX, y: 1, yref: "paper", text: "last uploaded cycle", showarrow: false, xanchor: "right", yanchor: "bottom", font: { color: ink, size: 11 } },
  ];
  if (bad) ann.push({ x: bad.cycle, y: bad.hi * 100, text: "uninformative", showarrow: true, arrowhead: 0, ax: 0, ay: -26, font: { color: muted, size: 11 } });
  const layout = {
    margin: { l: 56, r: 16, t: 24, b: 70 }, paper_bgcolor: "rgba(0,0,0,0)", plot_bgcolor: "rgba(0,0,0,0)",
    font: { color: ink, family: "system-ui, sans-serif", size: 12 }, dragmode: false, hovermode: "closest",
    hoverlabel: { bgcolor: css("--panel"), bordercolor: line, font: { color: ink } },
    legend: { orientation: "h", y: -0.2 },
    xaxis: { title: "cycle", gridcolor: line, range: [x0, x1], fixedrange: true },
    yaxis: { title: "state of health (%)", gridcolor: line, range: [y0 - pad, y1 + pad], fixedrange: true },
    shapes: [
      { type: "line", xref: "x", yref: "paper", x0: lastX, x1: lastX, y0: 0, y1: 1, line: { color: ink, width: 2 } },
      { type: "line", xref: "paper", yref: "y", x0: 0, x1: 1, y0: 80, y1: 80, line: { color: "#b22222", width: 1.5 } },
      ...(r.rul.already_below_threshold ? [] : [{ type: "line", xref: "x", yref: "paper", x0: r.rul.eol_cycle, x1: r.rul.eol_cycle, y0: 0, y1: 1, line: { color: accent, dash: "dash", width: 1.5 } }]),
    ],
    annotations: ann,
  };
  Plotly.react("plot-field", traces, layout, { responsive: true, displayModeBar: false });
  const nBad = pts.slice(1).filter((p) => !p.useful).length;
  $("f-plotnote").textContent =
    `Hatched band: the 90% interval is wider than half the distance from the forecast to 80% SOH (ADR-0019), so it carries little information.` +
    (nBad ? ` ${nBad} of ${pts.length - 1} forecast horizons are uninformative here.` : "") +
    (measured ? " The dotted line is the measured SOH from the file's soh_measured column, shown for comparison only." : "") +
    (r.rul.already_below_threshold ? "" : " The dashed vertical line is the predicted end of life (80% SOH).");
}

// ---------------------------------------------------------------- startup
async function init() {
  const avail = [];
  await Promise.all(PROTOCOLS.map(async ([p]) => {
    try {
      const r = await fetch(`field/${p}/field_serve_meta.json`);
      if (r.ok) { metas[p] = await r.json(); avail.push(p); }
    } catch { /* no field artifacts for this protocol */ }
  }));
  if (!avail.length) return; // lab-only page: the mode switch stays hidden
  try {
    const r = await fetch("examples/field/demos.json");
    if (r.ok) DEMOS = await r.json();
  } catch { /* uploads still work */ }
  for (const [p, label] of PROTOCOLS) if (metas[p]) $("f-proto").add(new Option(label, p));
  $("modes").classList.remove("hidden");
  if (typeof ort !== "undefined") ort.env.wasm.numThreads = 1;
  $("f-run").disabled = false;
  $("f-run").textContent = "Run";
  const q = new URLSearchParams(location.search);
  const demo = DEMOS.find((d) => d.name === q.get("demo"));
  if (demo && metas[demo.protocol]) $("f-proto").value = demo.protocol;
  fillProtocol();
  if (demo && metas[demo.protocol]) { $("f-demo").value = demo.name; $("f-demo").dispatchEvent(new Event("change")); }
  if (q.get("mode") === "field") setMode(true);
}
init();
