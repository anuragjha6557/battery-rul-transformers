// More results: SOH/RUL dot plots, RUL scatter, calibration, interval width, ablation forest, direct vs recursive, transfer.
import { plot, layout, styleAxes, modelColor, isHighlighted, LABEL, series, ink, muted, fmt } from "./viz.mjs";

const lab = (m) => LABEL[m] || m;
// Resolve any CSS colour (hex or rgb) to rgba with the given alpha.
const rgba = (c, a) => {
  c = c.trim();
  if (c.startsWith("#")) {
    let h = c.slice(1);
    if (h.length === 3) h = [...h].map((x) => x + x).join("");
    const n = parseInt(h.slice(0, 6), 16);
    return `rgba(${(n >> 16) & 255},${(n >> 8) & 255},${n & 255},${a})`;
  }
  const m = c.match(/[\d.]+/g);
  return `rgba(${m[0]},${m[1]},${m[2]},${a})`;
};
const row = (n, gap) => {
  // x-domains for a 1 x n subplot row
  const w = (1 - gap * (n - 1)) / n;
  return Array.from({ length: n }, (_, i) => [i * (w + gap), i * (w + gap) + w]);
};
const title = (text, x, y = 1.0) => ({
  text: `<b>${text}</b>`, x, y, xref: "paper", yref: "paper", xanchor: "center", yanchor: "bottom",
  showarrow: false, font: { size: 12, color: ink() },
});
const axName = (i) => (i === 0 ? "" : String(i + 1));
const sym = (id) => "x" + axName(id); // x, x2, ...
const yat = (id) => "y" + axName(id);
const q = (arr, p) => {
  const s = [...arr].sort((a, b) => a - b);
  const i = (s.length - 1) * p;
  const lo = Math.floor(i);
  return s[lo] + (s[Math.min(lo + 1, s.length - 1)] - s[lo]) * (i - lo);
};
// Legend-only trace (no data) so a key can describe a marker style.
const key = (name, marker, extra = {}) => ({
  type: "scatter", mode: "markers", x: [null], y: [null], name, showlegend: true, hoverinfo: "skip",
  marker: { size: 9, ...marker }, ...extra,
});

// ---------- 1, 2: dot plots with CIs ----------
function dots(id, d, order, xTitle, unit, { cap = false, localKey = false } = {}) {
  plot(id, () => {
    const n = d.length;
    const doms = row(n, 0.035);
    const traces = [];
    const lay = layout({
      margin: { l: 10, r: 8, t: 34, b: 96 }, annotations: [],
      legend: { orientation: "h", y: -0.2, font: { size: 11 } },
    });
    const seen = new Set();
    let anyClipped = false;
    d.forEach((p, i) => {
      const hiMax = Math.max(...p.rows.filter((r) => !r.local).map((r) => r.hi));
      const lim = cap ? hiMax * 1.12 : hiMax * 1.05;
      const names = order.filter((m) => p.rows.some((r) => r.model === m));
      for (const r of p.rows) {
        const col = r.local ? muted() : modelColor(r.model);
        const off = r.mean > lim;
        anyClipped ||= off;
        const x = off ? lim * 0.95 : r.mean;
        const hi = Math.min(r.hi, lim);
        const show = !seen.has(r.model) && (isHighlighted(r.model) || false);
        if (show) seen.add(r.model);
        traces.push({
          type: "scatter", mode: "markers", x: [x], y: [lab(r.model)], name: lab(r.model), legendgroup: r.model,
          showlegend: show, xaxis: sym(i), yaxis: yat(i),
          marker: { color: col, size: 9, symbol: off ? "triangle-right" : r.local ? "diamond" : "circle", line: { width: 0 } },
          error_x: off ? { visible: false } : { type: "data", symmetric: false, array: [Math.max(hi - x, 0)], arrayminus: [Math.max(x - r.lo, 0)], thickness: 1.5, width: 3, color: col },
          hovertemplate: `<b>${lab(r.model)}</b>${r.local ? " (curve-fit baseline)" : ""}<br>${p.label}<br>${xTitle} ${fmt(r.mean, 2)} ${unit} [${fmt(r.lo, 2)}, ${fmt(r.hi, 2)}]${off ? "<br>off scale: drawn at the axis edge" : ""}<extra></extra>`,
        });
      }
      lay["xaxis" + axName(i)] = {
        domain: doms[i], anchor: yat(i), range: [0, lim], nticks: 3, tickfont: { size: 10 },
        title: { text: `${xTitle} (${unit})`, font: { size: 10 } }, zeroline: false,
      };
      lay["yaxis" + axName(i)] = {
        anchor: sym(i), type: "category", categoryorder: "array", categoryarray: names.map(lab), autorange: "reversed",
        tickfont: { size: 10 }, dtick: 1, showticklabels: i === 0, ...(i === 0 ? {} : { matches: "y" }),
      };
      lay.annotations.push(title(p.label, (doms[i][0] + doms[i][1]) / 2));
    });
    // legend keys: highlighted models are real traces; add grey "other" keys
    traces.push(key("Other models", { color: modelColor("gru") }));
    if (localKey) traces.push(key("Curve-fit baselines", { color: muted(), symbol: "diamond" }));
    if (anyClipped) traces.push(key("Off scale (at edge; value in hover)", { color: muted(), symbol: "triangle-right" }));
    styleAxes(lay);
    lay.margin.l = 118;
    return { traces, layout: lay };
  });
}

// ---------- 3: predicted vs true RUL ----------
function scatter(d) {
  plot("res-rul-scatter", () => {
    const splits = [["test1", "Toyota test 1"], ["test2", "Toyota test 2"]];
    const doms = row(2, 0.08);
    const traces = [];
    const lay = layout({ margin: { l: 64, r: 16, t: 34, b: 90 }, annotations: [], legend: { orientation: "h", y: -0.22, font: { size: 11 } } });
    const models = ["itransformer", "lgbm", "itransformer_sc"];
    const all = splits.flatMap(([s]) => models.flatMap((m) => d.scatter[s][m].flatMap((r) => [r.true, r.pred])));
    const top = Math.ceil((Math.max(...all) * 1.04) / 100) * 100;
    splits.forEach(([s, label], i) => {
      traces.push({
        type: "scatter", mode: "lines", x: [0, top], y: [0, top], name: "Perfect prediction (y = x)", legendgroup: "diag",
        showlegend: i === 0, xaxis: sym(i), yaxis: yat(i), line: { color: muted(), width: 2 }, hoverinfo: "skip",
      });
      for (const f of [0.8, 1.2])
        traces.push({
          type: "scatter", mode: "lines", x: [0, top], y: [0, top * f], name: "±20 %", legendgroup: "cone",
          showlegend: i === 0 && f === 0.8, xaxis: sym(i), yaxis: yat(i), line: { color: muted(), width: 2, dash: "dot" }, hoverinfo: "skip",
        });
      for (const m of models) {
        const pts = d.scatter[s][m];
        traces.push({
          type: "scatter", mode: "markers", name: lab(m), legendgroup: m, showlegend: i === 0, xaxis: sym(i), yaxis: yat(i),
          x: pts.map((r) => r.true), y: pts.map((r) => r.pred),
          marker: { color: rgba(modelColor(m), 0.8), size: 9, line: { color: modelColor(m), width: 1 } },
          customdata: pts.map((r) => [r.cell, ((r.pred - r.true) / r.true) * 100]),
          hovertemplate: `<b>${lab(m)}</b> · ${label}<br>cell %{customdata[0]}<br>true RUL %{x:.0f} cycles<br>predicted %{y:.0f} cycles<br>error %{customdata[1]:+.0f} %<extra></extra>`,
        });
      }
      lay["xaxis" + axName(i)] = { domain: doms[i], anchor: yat(i), range: [0, top], title: { text: "True RUL (cycles)" } };
      lay["yaxis" + axName(i)] = { anchor: sym(i), range: [0, top], title: i === 0 ? { text: "Predicted RUL (cycles)" } : undefined, ...(i ? { matches: "y" } : {}) };
      lay.annotations.push(title(label, (doms[i][0] + doms[i][1]) / 2));
    });
    styleAxes(lay);
    return { traces, layout: lay };
  });
}

// ---------- 4: calibration (raw -> CQR) ----------
function calib(d) {
  plot("res-calib", () => {
    const n = d.calib.length;
    const doms = row(n, 0.03);
    const traces = [];
    const lay = layout({ margin: { l: 120, r: 12, t: 34, b: 100 }, annotations: [], shapes: [], legend: { orientation: "h", y: -0.2, font: { size: 11 } } });
    const models = d.calib[0].rows.map((r) => r.model);
    const lo = Math.min(...d.calib.flatMap((p) => p.rows.map((r) => Math.min(r.raw_picp, r.cal_picp))));
    const xmin = Math.max(0, Math.floor((lo - 0.02) * 20) / 20);
    d.calib.forEach((p, i) => {
      for (const r of p.rows) {
        const c = modelColor(r.model);
        traces.push({
          type: "scatter", mode: "lines+markers", name: lab(r.model), legendgroup: r.model, showlegend: i === 0,
          x: [r.raw_picp, r.cal_picp], y: [lab(r.model), lab(r.model)], xaxis: sym(i), yaxis: yat(i),
          line: { color: c, width: 1.5 },
          marker: { color: c, size: 10, symbol: ["circle-open", "circle"], line: { color: c, width: 2 } },
          customdata: [["raw", r.raw_mpiw], ["calibrated", r.cal_mpiw]],
          hovertemplate: `<b>${lab(r.model)}</b> · ${p.label}<br>%{customdata[0]} coverage (PICP) %{x:.3f}<br>interval width %{customdata[1]:.2f} %SOH<extra></extra>`,
        });
      }
      const xa = sym(i);
      lay.shapes.push(
        { type: "rect", xref: xa, yref: yat(i) + " domain", x0: 0.85, x1: 0.95, y0: 0, y1: 1, fillcolor: rgba(muted(), 0.14), line: { width: 0 }, layer: "below" },
        { type: "line", xref: xa, yref: yat(i) + " domain", x0: 0.9, x1: 0.9, y0: 0, y1: 1, line: { color: muted(), width: 1.5, dash: "dash" }, layer: "below" },
      );
      lay["xaxis" + axName(i)] = { domain: doms[i], anchor: yat(i), range: [xmin, 1.02], tickformat: ".1f", nticks: 4, tickfont: { size: 10 }, title: { text: "Coverage (PICP)", font: { size: 10 } } };
      lay["yaxis" + axName(i)] = {
        anchor: xa, type: "category", categoryorder: "array", categoryarray: models.map(lab), autorange: "reversed",
        tickfont: { size: 11 }, showticklabels: i === 0, ...(i ? { matches: "y" } : {}),
      };
      lay.annotations.push(title(p.label, (doms[i][0] + doms[i][1]) / 2));
    });
    traces.push(
      key("Raw quantiles (hollow)", { color: muted(), symbol: "circle-open", line: { color: muted(), width: 2 } }),
      key("After calibration (filled)", { color: muted() }),
      { type: "scatter", mode: "lines", x: [null], y: [null], name: "Target 90 % (band 85–95 %)", line: { color: muted(), width: 1.5, dash: "dash" }, hoverinfo: "skip" },
    );
    styleAxes(lay);
    return { traces, layout: lay };
  });
}

// ---------- 5: interval width raw vs calibrated ----------
function width(d) {
  plot("res-width", () => {
    const traces = [];
    const labels = d.calib.map((p) => p.label);
    for (const m of d.width_models) {
      const vals = (k) => d.calib.map((p) => (p.rows.find((r) => r.model === m) || {})[k]);
      const c = modelColor(m);
      const mk = (k, raw) => ({
        type: "bar", name: lab(m), legendgroup: m, showlegend: !raw, offsetgroup: m + (raw ? "-raw" : "-cal"),
        x: labels, y: vals(k),
        marker: raw ? { color: rgba(c, 0.12), line: { color: c, width: 1.5 }, pattern: { shape: "/", fgcolor: c, size: 6, solidity: 0.35 } } : { color: c },
        hovertemplate: `<b>${lab(m)}</b> (${raw ? "raw" : "calibrated"})<br>%{x}<br>mean interval width %{y:.2f} %SOH<extra></extra>`,
      });
      traces.push(mk("raw_mpiw", true), mk("cal_mpiw", false));
    }
    traces.push(
      key("Hatched = raw quantiles", { color: rgba(muted(), 0.15), symbol: "square", line: { color: muted(), width: 1.5 } }),
      key("Solid = after calibration", { color: muted(), symbol: "square" }),
    );
    const lay = layout({
      barmode: "group", bargap: 0.18, bargroupgap: 0.04, margin: { l: 56, r: 12, t: 12, b: 90 },
      yaxis: { title: { text: "Mean 90 % interval width (%SOH)" }, rangemode: "tozero" },
      legend: { orientation: "h", y: -0.18, font: { size: 11 } },
    });
    return { traces, layout: lay };
  });
}

// ---------- 6: ablation forest ----------
function ablation(d) {
  plot("res-ablation", () => {
    const panels = ["CALCE", "NASA", "Toyota test 1", "Toyota test 2"];
    const n = panels.length;
    const doms = row(n, 0.025);
    const rows = d.ablation;
    const labels = rows.map((r) => r.label);
    const traces = [];
    const green = series(6), red = series(8), grey = muted();
    const verdicts = [
      ["better", "Better (CI below 0)", green, "circle"],
      ["worse", "Worse (CI above 0)", red, "square"],
      ["inconclusive", "Inconclusive (CI spans 0)", grey, "diamond"],
    ];
    const lay = layout({
      margin: { l: 300, r: 12, t: 34, b: 90 }, annotations: [], shapes: [],
      legend: { orientation: "h", y: -0.12, font: { size: 11 } },
    });
    const groupEdges = [4.5, 8.5];
    panels.forEach((label, i) => {
      const pts = rows.map((r, j) => [r.cells[i], j, r]).filter(([c]) => c);
      const maxes = pts.map(([c]) => Math.max(Math.abs(c.lo), Math.abs(c.hi)));
      const cap = q(maxes, 0.75) * 2;
      const lim = Math.min(Math.max(...maxes), cap) * 1.12;
      for (const [v, vname, col, symbol] of verdicts) {
        const sel = pts.filter(([c]) => (c.hi < 0 ? "better" : c.lo > 0 ? "worse" : "inconclusive") === v);
        if (!sel.length) continue;
        const clipX = (x) => Math.max(-lim, Math.min(lim, x));
        const xs = sel.map(([c]) => (Math.abs(c.delta) > lim ? Math.sign(c.delta) * lim * 0.95 : c.delta));
        traces.push({
          type: "scatter", mode: "markers", name: vname, legendgroup: v, showlegend: false, xaxis: sym(i), yaxis: yat(i),
          x: xs, y: sel.map(([, , r]) => r.label),
          marker: { color: col, size: 10, symbol: sel.map(([c]) => (Math.abs(c.delta) > lim ? (c.delta > 0 ? "triangle-right" : "triangle-left") : symbol)), line: { width: 0 } },
          error_x: {
            type: "data", symmetric: false, thickness: 1.5, width: 3, color: col,
            array: sel.map(([c], k) => Math.max(clipX(c.hi) - xs[k], 0)),
            arrayminus: sel.map(([c], k) => Math.max(xs[k] - clipX(c.lo), 0)),
          },
          customdata: sel.map(([c, , r]) => [r.candidate, r.reference, c.cand, c.ref, c.delta, c.lo, c.hi, c.k, vname]),
          hovertemplate: `<b>%{y}</b> · ${label}<br>candidate: %{customdata[0]}<br>reference: %{customdata[1]}<br>means: %{customdata[2]:.3f} vs %{customdata[3]:.3f} %SOH<br>Δ = %{customdata[4]:+.3f} %SOH [%{customdata[5]:+.3f}, %{customdata[6]:+.3f}]<br>cells better: %{customdata[7]}<br>%{customdata[8]}<extra></extra>`,
        });
      }
      lay["xaxis" + axName(i)] = {
        domain: doms[i], anchor: yat(i), range: [-lim, lim], nticks: 5, tickfont: { size: 10 }, zeroline: false,
        title: { text: "Δ RMSE (%SOH), negative = better", font: { size: 10 } },
      };
      lay["yaxis" + axName(i)] = {
        anchor: sym(i), type: "category", categoryorder: "array", categoryarray: labels, autorange: "reversed",
        tickfont: { size: 11 }, showticklabels: i === 0, ...(i ? { matches: "y" } : {}),
      };
      lay.shapes.push({ type: "line", xref: sym(i), yref: yat(i) + " domain", x0: 0, x1: 0, y0: 0, y1: 1, line: { color: ink(), width: 1.5 }, layer: "below" });
      for (const e of groupEdges)
        lay.shapes.push({ type: "line", xref: sym(i) + " domain", yref: yat(i), x0: 0, x1: 1, y0: e, y1: e, line: { color: rgba(muted(), 0.35), width: 1, dash: "dot" } });
      if (i >= 2) lay.annotations.push({ text: "no Toyota transfer rows", x: (doms[i][0] + doms[i][1]) / 2, y: 0.1, xref: "paper", yref: "paper", showarrow: false, font: { size: 10, color: muted() } });
      lay.annotations.push(title(label, (doms[i][0] + doms[i][1]) / 2));
    });
    // The "no Toyota transfer rows" note belongs to the transfer rows only: place it with the data instead.
    lay.annotations = lay.annotations.filter((a) => a.text !== "no Toyota transfer rows");
    for (const [v, vname, col, symbol] of verdicts)
      traces.push({ type: "scatter", mode: "markers", x: [null], y: [null], name: vname, legendgroup: v, showlegend: true, hoverinfo: "skip", marker: { color: col, size: 10, symbol } });
    styleAxes(lay);
    return { traces, layout: lay };
  });
}

// ---------- 7: direct vs recursive ----------
const decades = (p) => {
  const v = p.direct.concat(p.recursive).map((r) => r.mean);
  const lo = Math.min(...v) * 0.85, hi = Math.max(...v) * 1.15;
  const out = [];
  for (let e = Math.floor(Math.log10(lo)) - 1; e <= Math.ceil(Math.log10(hi)); e++)
    for (const m of [1, 2, 5]) if (m * 10 ** e >= lo && m * 10 ** e <= hi) out.push(m * 10 ** e);
  return out;
};
function recursive(d) {
  plot("res-recursive", () => {
    const traces = [];
    const lay = layout({ margin: { l: 48, r: 10, t: 22, b: 84 }, annotations: [], legend: { orientation: "h", y: -0.2, font: { size: 11 } } });
    const dom = [[0, 0.46], [0.54, 1]];
    const rowsY = [[0.64, 1], [0, 0.34]];
    d.recursive.forEach((p, i) => {
      const xd = dom[i % 2], yd = rowsY[Math.floor(i / 2)];
      const hs = [...new Set(p.direct.concat(p.recursive).map((r) => r.h))].sort((a, b) => a - b);
      for (const [k, name, col] of [["direct", "Direct heads", series(1)], ["recursive", "Recursive rollout", series(2)]])
        traces.push({
          type: "scatter", mode: "lines+markers", name, legendgroup: k, showlegend: i === 0, xaxis: sym(i), yaxis: yat(i),
          x: p[k].map((r) => r.h), y: p[k].map((r) => r.mean),
          line: { color: col, width: 2 }, marker: { color: col, size: 8 },
          customdata: p[k].map((r) => [r.lo, r.hi]),
          hovertemplate: `<b>${name}</b> · ${p.label}<br>horizon %{x} cycles<br>RMSE %{y:.2f} %SOH [%{customdata[0]:.2f}, %{customdata[1]:.2f}]<extra></extra>`,
        });
      lay["xaxis" + axName(i)] = { domain: xd, anchor: yat(i), type: "log", tickvals: hs, ticktext: hs.map(String), tickfont: { size: 10 }, title: i >= 2 ? { text: "Horizon (cycles)", font: { size: 10 } } : undefined };
      lay["yaxis" + axName(i)] = { domain: yd, anchor: sym(i), type: "log", tickvals: decades(p), tickformat: "~g", tickfont: { size: 10 }, title: i % 2 === 0 ? { text: "RMSE (%SOH)", font: { size: 10 } } : undefined };
      lay.annotations.push(title(p.label, (xd[0] + xd[1]) / 2, yd[1]));
    });
    styleAxes(lay);
    return { traces, layout: lay };
  });
}

// ---------- 8: transfer ----------
function transfer(d) {
  plot("res-transfer", () => {
    const traces = [];
    const lay = layout({
      barmode: "group", bargap: 0.25, margin: { l: 48, r: 10, t: 34, b: 84 }, annotations: [],
      legend: { orientation: "h", y: -0.2, font: { size: 11 } },
    });
    const short = { scratch: "Scratch", zero_shot: "Zero-<br>shot", ft_head: "Head-only<br>FT", ft_full: "Full<br>FT", few_shot: "Few-<br>shot" };
    const dom = [[0, 0.62], [0.72, 1]];
    [["forecast", "h = 50 forecast RMSE (%SOH)", "RMSE", "%SOH"], ["rul", "RUL MAE (cycles)", "RUL MAE", "cycles"]].forEach(([k, ytitle, metric, unit], i) => {
      [["NASA", series(1)], ["CALCE", series(2)]].forEach(([ds, col]) => {
        const rows = d.transfer[k][ds];
        traces.push({
          type: "bar", name: ds, legendgroup: ds, showlegend: i === 0, xaxis: sym(i), yaxis: yat(i),
          x: rows.map((r) => short[r.arm]), y: rows.map((r) => r.mean), marker: { color: col },
          error_y: { type: "data", symmetric: false, array: rows.map((r) => r.hi - r.mean), arrayminus: rows.map((r) => r.mean - r.lo), thickness: 1.5, width: 3, color: ink() },
          customdata: rows.map((r) => [r.label, r.lo, r.hi]),
          hovertemplate: `<b>${ds}</b> · %{customdata[0]}<br>${metric} %{y:.2f} ${unit} [%{customdata[1]:.2f}, %{customdata[2]:.2f}]<extra></extra>`,
        });
      });
      lay["xaxis" + axName(i)] = { domain: dom[i], anchor: yat(i), tickfont: { size: 10 } };
      lay["yaxis" + axName(i)] = { anchor: sym(i), title: { text: ytitle, font: { size: 10 } }, rangemode: "tozero", tickfont: { size: 10 } };
      lay.annotations.push(title(k === "forecast" ? "Forecast (h = 50)" : "RUL", (dom[i][0] + dom[i][1]) / 2));
    });
    styleAxes(lay);
    return { traces, layout: lay };
  });
}

export function render(d) {
  const guard = (name, fn) => {
    try {
      fn();
    } catch (e) {
      console.error("results_more", name, e);
    }
  };
  guard("soh", () => dots("res-soh", d.soh, d.order, "RMSE", "%SOH"));
  guard("rul", () => dots("res-rul", d.rul, d.order_rul, "MAE", "cycles", { cap: true, localKey: true }));
  guard("scatter", () => scatter(d));
  guard("calib", () => calib(d));
  guard("width", () => width(d));
  guard("ablation", () => ablation(d));
  guard("recursive", () => recursive(d));
  guard("transfer", () => transfer(d));
}
