// Three-tasks schematic (task A nowcast, B direct multi-horizon forecast, C RUL) on a real cell.
import { ink, layout, muted, plot, series } from "./viz.mjs";

const rgba = (c, a) => {
  const m = c.match(/^#([0-9a-f]{6})$/i);
  if (!m) return c;
  const n = parseInt(m[1], 16);
  return `rgba(${(n >> 16) & 255},${(n >> 8) & 255},${n & 255},${a})`;
};

export function render(d) {
  plot("method-tasks", () => {
    const at = (c) => d.soh[d.cycle.indexOf(c)] ?? d.soh[d.soh.length - 1];
    const o = d.origin, s0 = at(o);
    const past = d.cycle.map((c, i) => [c, d.soh[i]]).filter(([c]) => c <= o);
    const fut = d.cycle.map((c, i) => [c, d.soh[i]]).filter(([c]) => c >= o);
    const hx = d.horizons.map((h) => o + h);
    const traces = [
      { x: past.map((p) => p[0]), y: past.map((p) => p[1]), mode: "lines", name: "observed SOH (cycles ≤ Tₚ)",
        line: { color: ink(), width: 2 }, hovertemplate: "cycle %{x}<br>SOH %{y:.1f}%<extra></extra>" },
      { x: fut.map((p) => p[0]), y: fut.map((p) => p[1]), mode: "lines", name: "future (hidden from the model)",
        line: { color: muted(), width: 1.5, dash: "dot" }, hovertemplate: "cycle %{x}<br>SOH %{y:.1f}%<extra></extra>" },
      { x: [o], y: [s0], mode: "markers", name: "A · SOH estimate at Tₚ",
        marker: { color: series(3), size: 11, symbol: "diamond" }, hovertemplate: "task A: SOH at cycle %{x}<extra></extra>" },
      { x: hx, y: hx.map(at), mode: "markers", name: "B · direct forecasts at h = 1…100",
        marker: { color: series(1), size: 9 }, customdata: d.horizons,
        hovertemplate: "task B: h = %{customdata}<br>cycle %{x}<extra></extra>" },
    ];
    const lay = layout({
      xaxis: { title: { text: "cycle" }, range: [o - 3.2 * d.lookback, d.eol + 60] },
      yaxis: { title: { text: "state of health (%)" } },
      title: { text: d.cell, font: { size: 12 }, x: 0.01 },
      shapes: [
        { type: "rect", xref: "x", yref: "paper", x0: o - d.lookback, x1: o, y0: 0, y1: 1, fillcolor: rgba(series(1), 0.1), line: { width: 0 } },
        { type: "line", xref: "x", yref: "paper", x0: o, x1: o, y0: 0, y1: 1, line: { color: ink(), width: 1, dash: "dash" } },
        { type: "line", xref: "paper", yref: "y", x0: 0, x1: 1, y0: d.theta, y1: d.theta, line: { color: muted(), width: 1 } },
      ],
      annotations: [
        { x: o - d.lookback / 2, y: 1.0, yref: "paper", text: `look-back window (${d.lookback} cycles)`, showarrow: false, yanchor: "bottom", font: { size: 11, color: muted() } },
        { x: o, y: 0.02, yref: "paper", text: "origin Tₚ", showarrow: false, xanchor: "left", yanchor: "bottom", font: { size: 11, color: ink() } },
        { x: d.eol, y: d.theta, ax: o, ay: d.theta, xref: "x", yref: "y", axref: "x", ayref: "y", showarrow: true, arrowhead: 2, arrowside: "end+start",
          arrowcolor: series(2), arrowwidth: 2, text: "" },
        { x: (o + d.eol) / 2, y: d.theta, yshift: -12, text: `C · RUL = ${Math.round(d.eol - o)} cycles to 80 % SOH`, showarrow: false, font: { size: 11, color: ink() } },
      ],
    });
    return { traces, layout: lay };
  });
}
