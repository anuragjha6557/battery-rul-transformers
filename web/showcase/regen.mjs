// Showcase part `regen`: capacity regeneration (ADR-0016) and CALCE artifact cycles (ADR-0017).
import { LABEL, ink, layout, modelColor, muted, plot, series, styleAxes } from "./viz.mjs";

const lab = (m) => LABEL[m] ?? m;
const rgba = (c, a) => {
  const m = c.match(/^#([0-9a-f]{6})$/i);
  if (!m) return c;
  const n = parseInt(m[1], 16);
  return `rgba(${(n >> 16) & 255},${(n >> 8) & 255},${n & 255},${a})`;
};

export function render(d) {
  // 1 · SOH estimation at regeneration cycles (the rest has already happened)
  plot("regen-taska", () => {
    const rows = [...d.task_a].sort((a, b) => b.rmse - a.rmse);
    const y = rows.map((r) => lab(r.model));
    return {
      traces: [
        { type: "bar", orientation: "h", y, x: rows.map((r) => r.rmse_other), name: "other cycles",
          marker: { color: rows.map((r) => rgba(modelColor(r.model), 0.35)) },
          hovertemplate: "%{y}: %{x:.2f} % SOH on ordinary cycles<extra></extra>" },
        { type: "bar", orientation: "h", y, x: rows.map((r) => r.rmse), name: "regeneration cycles (after a rest > 6 h)",
          marker: { color: rows.map((r) => modelColor(r.model)) }, customdata: rows.map((r) => [r.bias, r.n]),
          hovertemplate: "%{y}: RMSE %{x:.2f} % SOH, bias %{customdata[0]:+.2f} (n = %{customdata[1]})<extra>regeneration cycles</extra>" },
      ],
      layout: layout({ barmode: "group", xaxis: { title: { text: "SOH estimation RMSE (% SOH), NASA" } }, margin: { l: 150, r: 16, t: 16, b: 90 },
        legend: { orientation: "h", y: -0.32, font: { size: 11 } } }),
    };
  });

  // 2 · forecasts just before a long rest: LSTM with vs without the planned rest schedule
  plot("regen-fan", () => {
    const f = d.fans, P = f.panels;
    const traces = [], lay = { grid: { rows: 1, columns: P.length, pattern: "independent" }, annotations: [] };
    const sty = {
      lstm: { color: modelColor("lstm"), dash: "dot", symbol: "cross" },
      "lstm+rest": { color: modelColor("lstm"), dash: "dashdot", symbol: "star" },
      persistence: { color: muted(), dash: "dash", symbol: "x" },
    };
    P.forEach((p, i) => {
      const ax = i ? String(i + 1) : "", xa = `x${ax}`, ya = `y${ax}`;
      const lo = p.origin - 6, hi = p.origin + Math.max(...f.h) + 4;
      const idx = f.truth.cycle.map((c, j) => [c, j]).filter(([c]) => c >= lo && c <= hi);
      const s0 = f.truth.soh[f.truth.cycle.indexOf(p.origin)];
      traces.push({ x: idx.map(([c]) => c), y: idx.map(([, j]) => f.truth.soh[j]), xaxis: xa, yaxis: ya, mode: "lines",
        name: "measured SOH", legendgroup: "truth", showlegend: i === 0, line: { color: ink(), width: 1.5 },
        hovertemplate: "cycle %{x}: %{y:.1f} %<extra>measured</extra>" });
      const rests = f.rests.filter((c) => c > lo && c <= hi);
      traces.push({ x: rests, y: rests.map((c) => f.truth.soh[f.truth.cycle.indexOf(c)]), xaxis: xa, yaxis: ya, mode: "markers",
        name: "after a long rest", legendgroup: "rest", showlegend: i === 0,
        marker: { symbol: "triangle-up", size: 11, color: series(3) }, hovertemplate: "cycle %{x}: rest > 6 h before it<extra></extra>" });
      for (const [m, s] of Object.entries(p.series)) {
        const st = sty[m];
        traces.push({ x: [p.origin, ...f.h.map((h) => p.origin + h)], y: [s0, ...s.soh], xaxis: xa, yaxis: ya, mode: "lines+markers",
          name: s.label, legendgroup: m, showlegend: i === 0,
          line: { color: st.color, dash: st.dash, width: m === "lstm+rest" ? 2.5 : 1.5 }, marker: { symbol: st.symbol, size: m === "lstm+rest" ? 11 : 8, color: st.color },
          customdata: [0, ...f.h], hovertemplate: `+%{customdata} cycles: %{y:.1f} %<extra>${s.label}</extra>` });
      }
      lay[`xaxis${ax}`] = { title: { text: "cycle" }, range: [lo, hi] };
      lay[`yaxis${ax}`] = { title: i ? undefined : { text: "SOH (%)" } };
      lay.annotations.push({ text: `${f.cell}: forecast issued at cycle ${p.origin}`, xref: `${xa} domain`, yref: `${ya} domain`, x: 0, y: 1.08,
        showarrow: false, xanchor: "left", font: { size: 12 } });
      lay.shapes = [...(lay.shapes || []), { type: "line", xref: xa, yref: `${ya} domain`, x0: p.origin, x1: p.origin, y0: 0, y1: 1, line: { color: muted(), dash: "dot", width: 1 } }];
    });
    return { traces, layout: styleAxes(layout({ ...lay, margin: { l: 56, r: 16, t: 36, b: 60 } })) };
  });

  // 3 · error at regeneration targets: benchmark vs + planned rests (NASA), h = 1 and 10
  plot("regen-events", () => {
    const ev = d.events.filter((r) => r.ds === "nasa");
    const models = ["transformer", "lstm", "elasticnet", "lgbm", "itransformer", "itransformer_sc"];
    const traces = [];
    [1, 10].forEach((h, i) => {
      const ax = i ? "2" : "";
      for (const arm of ["benchmark", "rest-aware"]) {
        const rows = models.map((m) => ev.find((r) => r.model === m && r.h === h && r.arm === arm));
        traces.push({
          type: "bar", x: models.map(lab), y: rows.map((r) => r?.rmse), xaxis: `x${ax}`, yaxis: `y${ax}`,
          name: arm === "benchmark" ? "without the schedule" : "+ planned rests", legendgroup: arm, showlegend: i === 0,
          marker: {
            color: models.map((m) => (arm === "benchmark" ? rgba(modelColor(m), 0.3) : modelColor(m))),
            line: { color: models.map((m) => modelColor(m)), width: 1.5 },
          },
          customdata: rows.map((r) => [r?.bias, r?.n]),
          hovertemplate: `h = ${h}: RMSE %{y:.2f} % SOH, bias %{customdata[0]:+.2f} (n = %{customdata[1]})<extra>${arm}</extra>`,
        });
      }
    });
    const lay = layout({
      barmode: "group", grid: { rows: 1, columns: 2, pattern: "independent" },
      yaxis: { title: { text: "RMSE at regeneration cycles (% SOH)" } }, yaxis2: {}, xaxis: { tickangle: -25 }, xaxis2: { tickangle: -25 },
      annotations: [
        { text: "1 cycle ahead", xref: "x domain", yref: "y domain", x: 0, y: 1.1, showarrow: false, xanchor: "left" },
        { text: "10 cycles ahead", xref: "x2 domain", yref: "y2 domain", x: 0, y: 1.1, showarrow: false, xanchor: "left" },
      ],
      margin: { l: 56, r: 16, t: 36, b: 120 },
      legend: { orientation: "h", y: -0.5, font: { size: 11 } },
    });
    return { traces, layout: styleAxes(lay) };
  });

  // 4 · CALCE: dropping charger-glitch cycles (paired deltas, artifact-free targets)
  plot("regen-clean", () => {
    const c = d.clean_paired.filter((r) => r.model !== "persistence");
    const metrics = ["rmse_h10 (artifact-free targets)", "rmse_h50 (artifact-free targets)", "rul_mae start points (cycles)"];
    const titles = ["Forecast, 10 cycles ahead (Δ % SOH)", "Forecast, 50 cycles ahead (Δ % SOH)", "RUL at start points (Δ cycles)"];
    const traces = [], lay = { grid: { rows: 1, columns: 3, pattern: "independent" }, annotations: [], shapes: [] };
    metrics.forEach((mt, i) => {
      const ax = i ? String(i + 1) : "";
      const rows = c.filter((r) => r.metric === mt);
      for (const r of rows) {
        const better = r.hi < 0, worse = r.lo > 0;
        traces.push({
          x: [r.delta], y: [lab(r.model)], xaxis: `x${ax}`, yaxis: `y${ax}`, mode: "markers", showlegend: false,
          error_x: { type: "data", symmetric: false, array: [r.hi - r.delta], arrayminus: [r.delta - r.lo], color: modelColor(r.model), thickness: 1.5 },
          marker: { size: 10, color: modelColor(r.model), symbol: better ? "circle" : worse ? "square" : "diamond-open" },
          hovertemplate: `${lab(r.model)}: %{x:+.3f} [${r.lo.toFixed(3)}, ${r.hi.toFixed(3)}], ${r.k_cells} cells better<br>${r.bench.toFixed(2)} → ${r.clean.toFixed(2)}<extra></extra>`,
        });
      }
      lay[`xaxis${ax}`] = { zeroline: false };
      lay[`yaxis${ax}`] = { showticklabels: i === 0, automargin: true };
      lay.shapes.push({ type: "line", xref: `x${ax}`, yref: `y${ax} domain`, x0: 0, x1: 0, y0: 0, y1: 1, line: { color: muted(), width: 1 } });
      lay.annotations.push({ text: titles[i], xref: `x${ax} domain`, yref: `y${ax} domain`, x: 0, y: 1.08, showarrow: false, xanchor: "left", font: { size: 12 } });
    });
    return { traces, layout: styleAxes(layout({ ...lay, margin: { l: 130, r: 16, t: 36, b: 40 } })) };
  });
}
