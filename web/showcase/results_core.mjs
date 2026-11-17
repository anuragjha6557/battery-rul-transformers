// Core results: mean rank, RMSE vs horizon, forecast fans, history-length effect, per-cell scatter.
import { plot, layout, styleAxes, modelColor, modelDash, isHighlighted, LABEL, ink, muted, fmt } from "./viz.mjs";

const lab = (m) => LABEL[m] || m;
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
const grid = (rows, cols, gapX = 0.09, gapY = 0.16) => {
  // domains for a rows x cols subplot grid, indexed row-major (top row first)
  const out = [];
  const w = (1 - gapX * (cols - 1)) / cols;
  const h = (1 - gapY * (rows - 1)) / rows;
  for (let r = 0; r < rows; r++)
    for (let c = 0; c < cols; c++)
      out.push({ x: [c * (w + gapX), c * (w + gapX) + w], y: [1 - r * (h + gapY) - h, 1 - r * (h + gapY)] });
  return out;
};
const subTitle = (text, dom) => ({
  text, x: dom.x[0], y: dom.y[1] + 0.005, xref: "paper", yref: "paper", xanchor: "left", yanchor: "bottom",
  showarrow: false, font: { size: 12, color: ink() },
});

// ---------- rank ----------
function rank(d) {
  plot("res-rank", () => {
    const rows = [...d.rank].sort((a, b) => b.rank - a.rank); // plotly draws first row at the bottom
    const traces = [{
      type: "bar", orientation: "h", x: rows.map((r) => r.rank), y: rows.map((r) => lab(r.model)),
      marker: { color: rows.map((r) => modelColor(r.model)) }, showlegend: false,
      customdata: rows.map((r) => [r.n, r.missing]),
      text: rows.map((r) => fmt(r.rank, 2)), textposition: "outside", cliponaxis: false,
      hovertemplate: "<b>%{y}</b><br>mean rank %{x:.2f}<br>%{customdata[0]} conditions (%{customdata[1]} missing)<extra></extra>",
    }];
    const lay = layout({
      margin: { l: 150, r: 40, t: 12, b: 44 }, showlegend: false,
      xaxis: { title: { text: "Mean rank over conditions (lower is better)" }, rangemode: "tozero" },
      yaxis: { automargin: true },
    });
    return { traces, layout: lay };
  });
}

// ---------- RMSE vs horizon ----------
function horizon(d) {
  plot("res-horizon", () => {
    const doms = grid(2, 2, 0.1, 0.2);
    const traces = [];
    const lay = layout({ margin: { l: 56, r: 16, t: 28, b: 90 }, legend: { orientation: "h", y: -0.16, font: { size: 11 } }, annotations: [] });
    const order = (ms) => [...ms.filter((m) => !isHighlighted(m)), ...ms.filter(isHighlighted)];
    d.horizon.forEach((p, i) => {
      const ax = i === 0 ? "" : String(i + 1);
      for (const m of order(Object.keys(p.models))) {
        const v = p.models[m];
        const hi = isHighlighted(m);
        traces.push({
          type: "scatter", mode: hi ? "lines+markers" : "lines", name: lab(m), legendgroup: m, showlegend: i === 0,
          x: p.horizons, y: v.mean, xaxis: "x" + ax, yaxis: "y" + ax, connectgaps: false,
          line: { color: modelColor(m), width: hi ? 2 : 1, dash: modelDash(m) },
          marker: { color: modelColor(m), size: 8 }, opacity: hi ? 1 : 0.75,
          customdata: p.horizons.map((h, j) => [h, v.lo[j], v.hi[j]]),
          hovertemplate: `<b>${lab(m)}</b><br>${p.title}<br>horizon %{customdata[0]:d} cycles<br>RMSE %{y:.2f} % SOH [%{customdata[1]:.2f}, %{customdata[2]:.2f}]<extra></extra>`,
        });
      }
      lay["xaxis" + ax] = { domain: doms[i].x, anchor: "y" + ax, type: "log", tickvals: p.horizons, ticktext: p.horizons.map(String), title: { text: "Forecast horizon (cycles)", font: { size: 11 } } };
      lay["yaxis" + ax] = { domain: doms[i].y, anchor: "x" + ax, title: { text: "RMSE (% SOH)", font: { size: 11 } }, rangemode: "tozero" };
      lay.annotations.push(subTitle(`<b>${p.title}</b>`, doms[i]));
    });
    styleAxes(lay);
    return { traces, layout: lay };
  });
}

// ---------- forecast fans ----------
const FAN_MODELS = ["itransformer", "lgbm", "itransformer_sc", "persistence"];
function fan(d) {
  plot("res-fan", () => {
    const doms = grid(2, 2, 0.08, 0.2);
    const traces = [];
    const lay = layout({ margin: { l: 56, r: 16, t: 28, b: 90 }, legend: { orientation: "h", y: -0.1, font: { size: 11 } }, annotations: [] });
    d.fan.forEach((p, i) => {
      const ax = i === 0 ? "" : String(i + 1);
      const xa = "x" + ax, ya = "y" + ax;
      const x0 = p.origin - 1.5 * p.max_h, x1 = p.origin + p.max_h + 10;
      traces.push({
        type: "scatter", mode: "lines", name: "Measured SOH", legendgroup: "measured", showlegend: i === 0,
        x: p.traj_x, y: p.traj_y, xaxis: xa, yaxis: ya, line: { color: ink(), width: 1.5 },
        hovertemplate: `<b>Measured</b><br>cycle %{x:d}<br>SOH %{y:.2f} %<extra></extra>`,
      });
      let ys = [];
      p.traj_x.forEach((x, j) => { if (x >= x0 && x <= x1) ys.push(p.traj_y[j]); });
      // origin marker: dotted vertical line
      traces.push({
        type: "scatter", mode: "lines", name: "Forecast origin", legendgroup: "origin", showlegend: i === 0,
        x: [p.origin, p.origin], y: [0, 1], yaxis: ya, xaxis: xa, hoverinfo: "skip",
        line: { color: muted(), width: 1, dash: "dot" },
      });
      const originTrace = traces[traces.length - 1];
      for (const m of FAN_MODELS) {
        const pts = p.models[m];
        const col = modelColor(m);
        const xs = [p.origin, ...pts.map((q) => q.x)];
        const ysf = [p.origin_soh, ...pts.map((q) => q.point)];
        if (m !== "lgbm" && m !== "persistence" || m === "lgbm") ysf.forEach((v) => ys.push(v));
        const hasBand = pts[0].lo != null;
        if (hasBand) {
          const vis = m === "itransformer" ? true : "legendonly";
          const bx = [p.origin, ...pts.map((q) => q.x)];
          const lo = [p.origin_soh, ...pts.map((q) => q.lo)];
          const hi = [p.origin_soh, ...pts.map((q) => q.hi)];
          traces.push({
            type: "scatter", mode: "lines", name: `${lab(m)} 90 % band`, legendgroup: m + "-band", showlegend: i === 0,
            x: [...bx, ...bx.slice().reverse()], y: [...hi, ...lo.slice().reverse()], xaxis: xa, yaxis: ya,
            fill: "toself", fillcolor: rgba(col, 0.18), line: { width: 0, color: col }, hoverinfo: "skip", visible: vis,
          });
          if (vis === true) { hi.forEach((v) => ys.push(v)); lo.forEach((v) => ys.push(v)); }
        }
        traces.push({
          type: "scatter", mode: "lines+markers", name: lab(m), legendgroup: m, showlegend: i === 0,
          x: xs, y: ysf, xaxis: xa, yaxis: ya,
          line: { color: col, width: 2, dash: modelDash(m) }, marker: { color: col, size: 8 },
          customdata: [[0, null, null, p.origin_soh], ...pts.map((q) => [q.h, q.lo ?? null, q.hi ?? null, q.meas])],
          hovertemplate:
            `<b>${lab(m)}</b><br>horizon %{customdata[0]:d} cycles (cycle %{x:d})<br>forecast %{y:.2f} % SOH` +
            (hasBand ? `<br>90 % interval [%{customdata[1]:.2f}, %{customdata[2]:.2f}] % SOH` : "") +
            `<br>measured %{customdata[3]:.2f} % SOH<extra></extra>`,
        });
      }
      const lo = Math.min(...ys), hi = Math.max(...ys), pad = (hi - lo) * 0.06 || 0.5;
      originTrace.y = [lo - pad, hi + pad];
      lay["xaxis" + ax] = { domain: doms[i].x, anchor: ya, range: [Math.max(0, x0), x1], title: { text: "Cycle", font: { size: 11 } } };
      lay["yaxis" + ax] = { domain: doms[i].y, anchor: xa, range: [lo - pad, hi + pad], title: { text: "SOH (%)", font: { size: 11 } } };
      lay.annotations.push(subTitle(`<b>${p.name} ${p.cell}</b> · ${p.note} · h50 err ${fmt(p.itr_h50_err, 2)} %`, doms[i]));
    });
    styleAxes(lay);
    return { traces, layout: lay };
  });
}

// ---------- history length ----------
function history(d) {
  plot("res-history", () => {
    const h = d.history;
    const traces = Object.keys(h.models).map((m) => ({
      type: "bar", name: lab(m), x: h.bins.map((b, i) => `${b} (n=${h.n_per_bin[i]})`), y: h.models[m],
      marker: { color: modelColor(m), pattern: m === "persistence" ? { shape: "/", fgcolor: modelColor(m), bgcolor: "rgba(0,0,0,0)" } : undefined },
      opacity: isHighlighted(m) ? 1 : 0.8,
      hovertemplate: `<b>${lab(m)}</b><br>origin cycles ${"%{x}"}<br>RMSE %{y:.2f} % SOH<extra></extra>`,
    }));
    const lay = layout({
      barmode: "group", margin: { l: 56, r: 16, t: 12, b: 100 }, legend: { orientation: "h", y: -0.28, font: { size: 11 } },
      xaxis: { title: { text: "Forecast origin cycle (n = origins per seed), NASA, h = 50" } },
      yaxis: { title: { text: "RMSE (% SOH)" }, rangemode: "tozero" },
    });
    return { traces, layout: lay };
  });
}

// ---------- per-cell ----------
function cells(d) {
  plot("res-cells", () => {
    const doms = grid(1, 2, 0.08, 0);
    const traces = [];
    const lay = layout({ margin: { l: 56, r: 16, t: 28, b: 90 }, legend: { orientation: "h", y: -0.2, font: { size: 11 } }, annotations: [] });
    ["nasa", "calce"].forEach((ds, i) => {
      const c = d.cells[ds];
      const ax = i === 0 ? "" : "2";
      const ms = Object.keys(c.models);
      const step = 0.17;
      ms.forEach((m, j) => {
        const off = (j - (ms.length - 1) / 2) * step;
        const dx = [], dy = [], dtxt = [], mx = [], my = [];
        c.cells.forEach((cell, k) => {
          c.models[m].seeds[k].forEach((v, s) => {
            dx.push(k + off + (s - 2) * 0.018); dy.push(v); dtxt.push([cell, s]);
          });
          mx.push(k + off); my.push(c.models[m].mean[k]);
        });
        traces.push({
          type: "scatter", mode: "markers", name: lab(m), legendgroup: m, showlegend: i === 0,
          visible: m === "persistence" ? "legendonly" : true,
          x: dx, y: dy, customdata: dtxt, xaxis: "x" + ax, yaxis: "y" + ax, opacity: 0.7,
          marker: { color: modelColor(m), size: 8 },
          hovertemplate: `<b>${lab(m)}</b><br>cell %{customdata[0]}, seed %{customdata[1]}<br>RMSE %{y:.2f} % SOH<extra></extra>`,
        });
        traces.push({
          type: "scatter", mode: "markers", name: `${lab(m)} mean`, legendgroup: m, showlegend: false,
          visible: m === "persistence" ? "legendonly" : true,
          x: mx, y: my, customdata: c.cells, xaxis: "x" + ax, yaxis: "y" + ax,
          marker: { symbol: "line-ew", size: 22, color: modelColor(m), line: { color: modelColor(m), width: 2.5 } },
          hovertemplate: `<b>${lab(m)}</b><br>cell %{customdata}<br>mean over 5 seeds %{y:.2f} % SOH<extra></extra>`,
        });
      });
      lay["xaxis" + ax] = { domain: doms[i].x, anchor: "y" + ax, tickvals: c.cells.map((_, k) => k), ticktext: c.cells, range: [-0.6, c.cells.length - 0.4], title: { text: "Held-out cell", font: { size: 11 } } };
      lay["yaxis" + ax] = { domain: doms[i].y, anchor: "x" + ax, title: { text: "h = 50 RMSE (% SOH)", font: { size: 11 } }, rangemode: "tozero" };
      lay.annotations.push(subTitle(`<b>${ds === "nasa" ? "NASA" : "CALCE"}</b> · dots = seeds, ticks = mean`, doms[i]));
    });
    styleAxes(lay);
    return { traces, layout: lay };
  });
}

export function render(d) {
  for (const f of [rank, horizon, fan, history, cells]) {
    try { f(d); } catch (e) { console.error("results_core", f.name, e); }
  }
}
