// Showcase part `field`: the field setting (no SOH/capacity history), ADR-0018..0022.
import { LABEL, fmt, layout, muted, plot, series, styleAxes } from "./viz.mjs";

const css = (n) => getComputedStyle(document.documentElement).getPropertyValue(n).trim();
const $ = (id) => document.getElementById(id);
const lab = (m) => (m === "age_only" ? "Age only" : (LABEL[m] ?? m).replace(" (MC)", ""));
// Fixed entity colours; transformer has no slot in viz.mjs (it shares slot 3 with iTransformer SC, absent here).
const SLOT = { itransformer: 1, lgbm: 2, transformer: 4, lstm: 5, patchtst: 7 };
const color = (m) => (SLOT[m] ? series(SLOT[m]) : css("--text-secondary"));
const esc = (s) => String(s ?? "").replace(/&/g, "&amp;").replace(/</g, "&lt;");
const sign = (v, d = 2) => (v >= 0 ? "+" : "−") + Math.abs(v).toFixed(d);
const TASK_NAME = { soh: "F-A SOH estimation", forecast: "F-B forecast (h = 50)", rul: "F-C RUL" };

function table(el, head, rows, cls = "") {
  $(el).innerHTML = `<table class="${cls}"><thead><tr>${head.map((h) => `<th>${h}</th>`).join("")}</tr></thead><tbody>${rows
    .map((r) => `<tr>${r.map((c) => `<td>${c}</td>`).join("")}</tr>`)
    .join("")}</tbody></table>`;
}

/** Dot + CI plot, one panel per `panels` entry; rows = categories. Filled = CI excludes 0, hollow = inconclusive. */
function dotPanels(id, panels, { height, left = 120, xTitle } = {}) {
  plot(id, () => {
    const traces = [], lay = { grid: { rows: 1, columns: panels.length, pattern: "independent" }, annotations: [], shapes: [] };
    panels.forEach((p, i) => {
      const ax = i ? String(i + 1) : "";
      for (const r of p.rows) {
        const sig = r.hi < 0 || r.lo > 0;
        traces.push({
          x: [r.delta], y: [r.y], xaxis: `x${ax}`, yaxis: `y${ax}`, mode: "markers", showlegend: false,
          error_x: { type: "data", symmetric: false, array: [r.hi - r.delta], arrayminus: [r.delta - r.lo], color: r.color, thickness: 1.5 },
          marker: { size: 10, color: sig ? r.color : "rgba(0,0,0,0)", line: { color: r.color, width: 2 }, symbol: "circle" },
          hovertemplate: `${esc(r.y)}: ${sign(r.delta, 3)} [${r.lo.toFixed(3)}, ${r.hi.toFixed(3)}]${r.k ? `, ${r.k} cells better` : ""}<extra>${esc(p.title)}</extra>`,
        });
      }
      lay[`xaxis${ax}`] = { zeroline: false, title: i === 0 && xTitle ? { text: xTitle } : undefined };
      lay[`yaxis${ax}`] = { showticklabels: i === 0, automargin: true, autorange: "reversed" };
      lay.shapes.push({ type: "line", xref: `x${ax}`, yref: `y${ax} domain`, x0: 0, x1: 0, y0: 0, y1: 1, line: { color: muted(), width: 1 } });
      lay.annotations.push({ text: p.title, xref: `x${ax} domain`, yref: `y${ax} domain`, x: 0, y: 1.1, showarrow: false, xanchor: "left", font: { size: 12 } });
    });
    return { traces, layout: styleAxes(layout({ ...lay, margin: { l: left, r: 16, t: 40, b: 44 }, height })) };
  });
}

export function render(d) {
  const conds = d.conds;

  // 1 · signal availability + Spearman
  table("field-signals", ["Signal", "NASA", "CALCE", "Toyota", "Notes"], d.signals.map((r) => r.map(esc)), "left");
  table(
    "field-rho",
    ["Spearman ρ with SOH (per-cell median)", "NASA", "CALCE", "Toyota"],
    d.spearman.map((r) => [esc(r.feature), ...["nasa", "calce", "toyota"].map((k) => (r[k] == null ? "–" : sign(r[k], 2)))]),
  );

  // 2 · lab vs field gap (log x, one panel per task)
  plot("field-gap", () => {
    const traces = [], lay = { grid: { rows: 1, columns: 3, pattern: "independent" }, annotations: [] };
    d.tasks.forEach((t, i) => {
      const ax = i ? String(i + 1) : "", rows = d.gap.filter((g) => g.task === t.id);
      const common = { xaxis: `x${ax}`, yaxis: `y${ax}`, y: rows.map((r) => r.cond) };
      traces.push({ ...common, x: rows.map((r) => Math.max(r.lab, 1e-3)), mode: "markers", name: "with SOH history (lab, best model)", legendgroup: "lab", showlegend: i === 0,
        marker: { size: 11, color: series(1), symbol: "circle" }, customdata: rows.map((r) => lab(r.lab_model)),
        hovertemplate: "%{y}: %{x:.3g} (%{customdata})<extra>lab</extra>" });
      traces.push({ ...common, x: rows.map((r) => r.field), mode: "markers", name: "field, best model", legendgroup: "field", showlegend: i === 0,
        marker: { size: 11, color: series(2), symbol: "diamond" }, customdata: rows.map((r) => lab(r.field_model)),
        hovertemplate: "%{y}: %{x:.3g} (%{customdata})<extra>field</extra>" });
      traces.push({ ...common, x: rows.map((r) => r.age_only), mode: "markers", name: "age only (field)", legendgroup: "age", showlegend: i === 0,
        marker: { size: 9, color: muted(), symbol: "x" }, hovertemplate: "%{y}: %{x:.3g}<extra>age only</extra>" });
      lay[`xaxis${ax}`] = { type: "log", title: { text: t.label.split(" (")[0] + (t.id === "rul" ? " (cycles)" : " (% SOH)") } };
      lay[`yaxis${ax}`] = { showticklabels: i === 0, autorange: "reversed", automargin: true };
      lay.annotations.push({ text: t.label, xref: `x${ax} domain`, yref: `y${ax} domain`, x: 0, y: 1.1, showarrow: false, xanchor: "left", font: { size: 12 } });
    });
    return { traces, layout: styleAxes(layout({ ...lay, margin: { l: 110, r: 16, t: 40, b: 90 }, legend: { orientation: "h", y: -0.28, font: { size: 11 } } })) };
  });

  // 3 · headline table: model x condition, tint = ratio to the best model of that cell (log, clipped)
  const models = ["age_only", "itransformer", "transformer", "lstm", "lgbm", "elasticnet", "patchtst"];
  const DIV = 1000; // anything above this (ElasticNet RUL on NASA/CALCE) is shown as "diverged"
  let h = `<table class="heat"><thead><tr><th rowspan="2">Model</th>`;
  for (const t of d.tasks) h += `<th colspan="${conds.length}" class="grp">${esc(t.label)}</th>`;
  h += "</tr><tr>" + d.tasks.map(() => conds.map((c) => `<th class="sub">${esc(c)}</th>`).join("")).join("") + "</tr></thead><tbody>";
  const best = {};
  for (const r of d.heat) if (r.model !== "age_only") best[`${r.task}|${r.cond}`] = Math.min(best[`${r.task}|${r.cond}`] ?? Infinity, r.mean);
  for (const m of models) {
    h += `<tr><td>${esc(lab(m))}</td>`;
    for (const t of d.tasks) {
      for (const c of conds) {
        const r = d.heat.find((x) => x.model === m && x.task === t.id && x.cond === c);
        if (!r) { h += "<td>–</td>"; continue; }
        const b = best[`${t.id}|${c}`], ratio = r.mean / b, isBest = m !== "age_only" && r.mean === b;
        const pct = Math.round(Math.min(Math.log2(Math.max(ratio, 1)) / Math.log2(8), 1) * 70);
        const txt = r.mean > DIV ? "diverged" : fmt(r.mean, t.id === "rul" ? 1 : 2);
        const tip = `${lab(m)}, ${c}: ${fmt(r.mean, 3)} [${fmt(r.lo, 3)}, ${fmt(r.hi, 3)}]${r.lookback ? `, lookback ${r.lookback}` : ""}${r.mean > DIV ? " (training diverged; excluded from the colour scale)" : ""}`;
        h += `<td class="${isBest ? "best" : ""}" title="${esc(tip)}" style="background:color-mix(in srgb, var(--series-2) ${r.mean > DIV ? 0 : pct}%, transparent)">${txt}${r.mean > DIV ? " ⚠" : ""}</td>`;
      }
    }
    h += "</tr>";
  }
  $("field-heat").innerHTML = h + "</tbody></table>";

  // 4 · iTransformer claims
  // 4a variates: field_curve - field
  const vm = ["itransformer", "patchtst", "transformer", "lstm", "lgbm", "elasticnet"];
  dotPanels("field-variates", conds.map((c) => ({ title: c, rows: vm.map((m) => d.variates.find((v) => v.model === m && v.cond === c)).filter(Boolean).map((v) => ({ ...v, y: lab(v.model), color: color(v.model) })) })),
    { xTitle: "Δ SOH RMSE, field_curve − field (% SOH; left = curve helps)" });
  // 4b lookback: L128 - L32
  const lbm = ["itransformer", "transformer", "lstm"];
  dotPanels("field-lookback-soh", conds.slice(1).map((c) => ({ title: `${c}: SOH estimation`, rows: lbm.map((m) => d.lookback.find((v) => v.task === "soh" && v.model === m && v.cond === c)).filter(Boolean).map((v) => ({ ...v, y: lab(v.model), color: color(v.model) })) })),
    { xTitle: "Δ RMSE, L = 128 − L = 32 (% SOH; left = longer is better)" });
  dotPanels("field-lookback-fc", conds.slice(1).map((c) => ({ title: `${c}: forecast h = 50`, rows: lbm.map((m) => d.lookback.find((v) => v.task === "forecast" && v.model === m && v.cond === c)).filter(Boolean).map((v) => ({ ...v, y: lab(v.model), color: color(v.model) })) })),
    { xTitle: "Δ RMSE h = 50, L = 128 − L = 32 (% SOH)" });
  // 4c regeneration token: error reduction at regeneration targets, h = 1
  plot("field-regen", () => {
    const traces = [], lay = { grid: { rows: 1, columns: 2, pattern: "independent" }, annotations: [], shapes: [] };
    ["NASA", "CALCE"].forEach((ds, i) => {
      const ax = i ? "2" : "", rows = d.regen.filter((r) => r.dataset === ds);
      const ymap = rows.map((r) => `${lab(r.model)} ${r.kind === "token" ? "(rest as a variate token)" : "(rest as tabular input)"}`);
      traces.push({ type: "bar", orientation: "h", xaxis: `x${ax}`, yaxis: `y${ax}`, y: ymap, x: rows.map((r) => r.reduction * 100), showlegend: false,
        marker: { color: rows.map((r) => color(r.model)), pattern: { shape: rows.map((r) => (r.kind === "token" ? "/" : "")), bgcolor: "rgba(0,0,0,0)", fgcolor: css("--bg") } },
        customdata: rows.map((r) => [r.k, r.n, r.rmse_base, r.rmse_cand]),
        hovertemplate: "%{y}: %{x:+.1f} % error change (RMSE %{customdata[2]:.2f} → %{customdata[3]:.2f}), %{customdata[0]} cells better, n = %{customdata[1]}<extra></extra>" });
      lay[`xaxis${ax}`] = { zeroline: true, title: i === 0 ? { text: "error reduction at regeneration targets, h = 1 (%; right = better)" } : undefined };
      lay[`yaxis${ax}`] = { showticklabels: i === 0, autorange: "reversed", automargin: true };
      lay.annotations.push({ text: ds, xref: `x${ax} domain`, yref: `y${ax} domain`, x: 0, y: 1.1, showarrow: false, xanchor: "left", font: { size: 12 } });
    });
    return { traces, layout: styleAxes(layout({ ...lay, margin: { l: 230, r: 16, t: 40, b: 50 } })) };
  });
  // 4d channel mixing: iTransformer − PatchTST
  const tasksOrder = ["soh", "forecast", "rul"];
  dotPanels("field-mixing", tasksOrder.map((t) => ({ title: TASK_NAME[t], rows: d.mixing.filter((r) => r.task === t).map((r) => ({ ...r, y: r.cond, color: color("itransformer") })) })),
    { xTitle: "Δ error, iTransformer − PatchTST (left = iTransformer better)", left: 110 });

  // verdict ranks
  $("field-ranks").innerHTML = d.ranks.map((r) => `${esc(lab(r.model))} ${r.rank.toFixed(2)}`).join(" · ");

  // 5 · intervals
  const IM = ["itransformer", "transformer", "lstm", "lgbm", "patchtst"];
  const ivRows = (task) => d.intervals[task];
  const panelChart = (id, task, key, xTitle, xr, shapes) =>
    plot(id, () => {
      const traces = [], lay = { grid: { rows: 1, columns: conds.length, pattern: "independent" }, annotations: [], shapes: [] };
      conds.forEach((c, i) => {
        const ax = i ? String(i + 1) : "", rows = IM.map((m) => ivRows(task).find((r) => r.cond === c && r.model === m)).filter(Boolean);
        traces.push({ type: "bar", orientation: "h", xaxis: `x${ax}`, yaxis: `y${ax}`, y: rows.map((r) => lab(r.model)), x: rows.map((r) => r[key]), showlegend: false,
          marker: { color: rows.map((r) => color(r.model)) },
          hovertemplate: `%{y}: ${key === "picp" ? "coverage %{x:.2f}" : "%{x:.1%} of origins useful"}<extra>${esc(c)}</extra>` });
        lay[`xaxis${ax}`] = { range: xr, tickformat: key === "picp" ? ".2f" : ".0%", title: i === 0 ? { text: xTitle } : undefined };
        lay[`yaxis${ax}`] = { showticklabels: i === 0, autorange: "reversed", automargin: true };
        lay.annotations.push({ text: c, xref: `x${ax} domain`, yref: `y${ax} domain`, x: 0, y: 1.1, showarrow: false, xanchor: "left", font: { size: 12 } });
        if (shapes) lay.shapes.push(...shapes(ax));
      });
      return { traces, layout: styleAxes(layout({ ...lay, margin: { l: 110, r: 16, t: 40, b: 50 } })) };
    });
  panelChart("field-cov", "forecast", "picp", "90 % interval coverage, h = 50 (target 0.90)", [0.4, 1], (ax) => [
    { type: "rect", xref: `x${ax}`, yref: `y${ax} domain`, x0: 0.85, x1: 0.95, y0: 0, y1: 1, fillcolor: css("--series-3"), opacity: 0.18, line: { width: 0 }, layer: "below" },
  ]);
  panelChart("field-useful", "forecast", "useful", "useful share of origins, h = 50", [0, 1]);
  table(
    "field-rul-iv",
    ["RUL, CQR 90 % interval", ...conds.flatMap((c) => [`${esc(c)} coverage`, "width (cycles)"])],
    IM.map((m) => [esc(lab(m)), ...conds.flatMap((c) => { const r = ivRows("rul").find((x) => x.cond === c && x.model === m); return r ? [r.picp.toFixed(2), Math.round(r.width)] : ["–", "–"]; })]),
  );
}
