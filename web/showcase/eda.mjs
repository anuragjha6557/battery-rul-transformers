// EDA section: dataset table + exploratory charts. Colours come only from viz.mjs helpers.
import { plot, layout, styleAxes, series, ink, muted, DATASET_LABEL } from "./viz.mjs";

const LO = [205, 226, 251]; // sequential single-hue (blue) ramp, light -> dark
const HI = [16, 66, 129];
const ramp = (t) => `rgb(${LO.map((l, i) => Math.round(l + (HI[i] - l) * t)).join(",")})`;
const rampScale = [[0, ramp(0)], [1, ramp(1)]];
const SPLIT_SLOT = { train: 1, test1: 2, test2: 3 };
const f0 = (v) => Math.round(v).toLocaleString("en-US");

function table(d) {
  const nm = { nasa: "NASA", calce: "CALCE", toyota: "Toyota/MIT" };
  const body = d.table
    .map((r) => {
      const life = `${f0(r.life_min)} – ${f0(r.life_median)} – ${f0(r.life_max)}` +
        (r.dataset === "toyota" ? " (provider label)" : "") +
        (r.censored ? ` <i>(${r.censored} censored)</i>` : "");
      return `<tr><td><b>${nm[r.dataset]}</b></td><td>${r.chemistry}</td><td>${r.nominal_ah}</td><td>${r.cells}</td>` +
        `<td>${f0(r.cycles)}</td><td>${life}</td><td>${r.protocol}</td><td>${r.split}</td></tr>`;
    })
    .join("");
  document.getElementById("eda-table").innerHTML =
    `<table><thead><tr><th>Dataset</th><th>Chemistry</th><th>Nominal (Ah)</th><th>Cells</th><th>Cycles</th>` +
    `<th>Cycle life to 80 % (min – median – max)</th><th>Test protocol</th><th>Evaluation split</th></tr></thead><tbody>${body}</tbody></table>`;
}

function sohPanel(d) {
  plot("eda-soh", () => {
    const traces = [];
    const dom = [[0, 0.3], [0.35, 0.65], [0.7, 0.93]];
    const panels = ["nasa", "calce", "toyota"];
    panels.forEach((ds, p) => {
      const ax = p + 1 === 1 ? "" : String(p + 1);
      const cells = d.soh[ds];
      cells.forEach((c, i) => {
        const common = { x: c.cycle, y: c.soh, xaxis: `x${ax}`, yaxis: `y${ax}`, type: "scatter", mode: "lines" };
        if (ds === "toyota") {
          const lo = 148, hi = 2237;
          traces.push({
            ...common, showlegend: false, opacity: 0.6,
            line: { width: 1, color: ramp((c.life - lo) / (hi - lo)) },
            hovertemplate: `${c.cell}<br>cycle %{x}<br>SOH %{y:.1f} %<br>life ${f0(c.life)} cycles<extra></extra>`,
          });
        } else {
          traces.push({
            ...common, name: c.cell, legendgroup: ds, line: { width: 2, color: series(i + 1) },
            hovertemplate: `${c.cell}<br>cycle %{x}<br>SOH %{y:.1f} %<extra></extra>`,
          });
        }
      });
      const xs = ds === "toyota" ? [0, 2300] : ds === "nasa" ? [0, 170] : [0, 1000];
      traces.push({
        x: xs, y: [80, 80], xaxis: `x${ax}`, yaxis: `y${ax}`, mode: "lines", hoverinfo: "skip",
        line: { width: 1, dash: "dash", color: muted() }, showlegend: p === 0, name: "80 % (end of life)", legendgroup: "ref",
      });
    });
    traces.push({
      x: [null], y: [null], xaxis: "x3", yaxis: "y3", type: "scatter", mode: "markers", showlegend: false, hoverinfo: "skip",
      marker: { color: [148, 2237], cmin: 148, cmax: 2237, colorscale: rampScale, size: 0.1, showscale: true,
        colorbar: { title: { text: "cycle life", font: { color: ink() } }, thickness: 10, len: 0.8, x: 1.0, tickfont: { color: ink() } } },
    });
    const lay = layout({ margin: { l: 48, r: 70, t: 36, b: 90 }, height: undefined });
    ["xaxis", "yaxis"].forEach((k) => delete lay[k]);
    panels.forEach((ds, p) => {
      const ax = p === 0 ? "" : String(p + 1);
      lay[`xaxis${ax}`] = { domain: dom[p], title: { text: "cycle" }, anchor: `y${ax}` };
      lay[`yaxis${ax}`] = { anchor: `x${ax}`, range: [10, 108], title: p === 0 ? { text: "SOH (%)" } : undefined };
    });
    lay.annotations = panels.map((ds, p) => ({
      text: `<b>${DATASET_LABEL[ds === "toyota" ? "toyota" : ds]}</b>`, x: (dom[p][0] + dom[p][1]) / 2, y: 1.04, xref: "paper", yref: "paper",
      showarrow: false, font: { color: ink(), size: 13 },
    }));
    lay.legend = { orientation: "h", y: -0.22, font: { size: 11 } };
    return { traces, layout: styleAxes(lay) };
  });
}

function life(d) {
  plot("eda-life", () => {
    const traces = ["train", "test1", "test2"].map((s) => {
      const r = d.life.filter((x) => x.split === s);
      return {
        type: "box", name: s, y: r.map((x) => x.life), text: r.map((x) => x.cell), boxpoints: "all", jitter: 0.6, pointpos: 0,
        marker: { color: series(1), size: 7, opacity: 0.6 }, line: { color: series(1), width: 2 }, fillcolor: "rgba(0,0,0,0)",
        hovertemplate: "%{text}<br>life %{y:,.0f} cycles<extra></extra>", showlegend: false,
      };
    });
    return { traces, layout: styleAxes(layout({ margin: { l: 56, r: 16, t: 16, b: 48 }, xaxis: { title: { text: "official split" } }, yaxis: { title: { text: "cycle life (cycles)" } } })) };
  });
}

function early(d) {
  const e = d.early;
  plot("eda-early", () => {
    const traces = ["train", "test1", "test2"].map((s) => {
      const r = e.points.filter((x) => x.split === s);
      return {
        type: "scatter", mode: "markers", name: s, x: r.map((p) => p.x), y: r.map((p) => p.y), text: r.map((p) => p.cell),
        customdata: r.map((p) => p.life), marker: { color: series(SPLIT_SLOT[s]), size: 8, opacity: 0.85 },
        hovertemplate: `%{text} (${s})<br>log10 var ΔQ: %{x:.2f}<br>cycle life: %{customdata:,.0f} cycles<extra></extra>`,
      };
    });
    const xs = e.points.map((p) => p.x);
    const x0 = Math.min(...xs), x1 = Math.max(...xs);
    traces.push({
      type: "scatter", mode: "lines", name: "least-squares fit (train)", x: [x0, x1], y: [x0, x1].map((x) => e.intercept + e.slope * x),
      line: { width: 2, color: ink() }, hoverinfo: "skip",
    });
    const lay = layout({
      title: { text: `Pearson r = ${e.pearson_train.toFixed(2)} (train, n = ${e.n_train})`, font: { size: 13, color: ink() } },
      margin: { l: 56, r: 16, t: 40, b: 80 }, legend: { orientation: "h", y: -0.32, font: { size: 11 } },
      xaxis: { title: { text: "log10 Var[ΔQ100−10(V)]" } }, yaxis: { title: { text: "log10 cycle life" } },
    });
    return { traces, layout: styleAxes(lay) };
  });
}

function nasaRegen(d) {
  plot("eda-nasa-regen", () => {
    const traces = [];
    d.nasa_regen.forEach((c, i) => {
      traces.push({ type: "scatter", mode: "lines", name: c.cell, x: c.cycle, y: c.soh, line: { width: 2, color: series(i + 1) },
        hovertemplate: `${c.cell}<br>cycle %{x}<br>SOH %{y:.1f} %<extra></extra>` });
    });
    d.nasa_regen.forEach((c, i) => {
      traces.push({ type: "scatter", mode: "markers", name: "after long rest", legendgroup: "rest", showlegend: i === 0,
        x: c.rest_cycle, y: c.rest_soh, customdata: c.rest_s.map((s) => s / 3600),
        marker: { symbol: "triangle-up", size: 11, color: series(i + 1), line: { width: 1.5, color: ink() } },
        hovertemplate: `${c.cell}<br>cycle %{x}<br>SOH %{y:.1f} %<br>rest before: %{customdata:.0f} h<extra></extra>` });
    });
    return { traces, layout: styleAxes(layout({ xaxis: { title: { text: "cycle" } }, yaxis: { title: { text: "SOH (%)" } }, margin: { l: 56, r: 16, t: 16, b: 48 } })) };
  });
}

function calceDips(d) {
  const c = d.calce_dips;
  plot("eda-calce-dips", () => {
    const traces = [
      { type: "scatter", mode: "lines", name: c.cell, x: c.cycle, y: c.soh, line: { width: 2, color: series(1) },
        hovertemplate: `${c.cell}<br>cycle %{x}<br>SOH %{y:.1f} %<extra></extra>` },
      { type: "scatter", mode: "markers", name: "CV step skipped (artifact)", x: c.art_cycle, y: c.art_soh, customdata: c.art_cv_s,
        marker: { symbol: "x", size: 9, color: series(2), line: { width: 2, color: series(2) } },
        hovertemplate: `${c.cell}<br>cycle %{x}<br>SOH %{y:.1f} %<br>CV time %{customdata:.0f} s<extra></extra>` },
    ];
    return { traces, layout: styleAxes(layout({ xaxis: { title: { text: "cycle" } }, yaxis: { title: { text: "SOH (%)" } }, margin: { l: 56, r: 16, t: 16, b: 48 } })) };
  });
}

function eol(d) {
  const e = d.eol;
  plot("eda-eol", () => {
    const traces = [
      { type: "scatter", mode: "lines", name: "raw SOH", x: e.cycle, y: e.soh, line: { width: 1, color: muted() }, opacity: 0.7,
        hovertemplate: `${e.cell}<br>cycle %{x}<br>SOH %{y:.1f} %<extra></extra>` },
      { type: "scatter", mode: "lines", name: "11-cycle rolling median", x: e.cycle, y: e.roll, line: { width: 2, color: series(1) },
        hovertemplate: `${e.cell}<br>cycle %{x}<br>median SOH %{y:.1f} %<extra></extra>` },
    ];
    const vline = (x, label, ay) => ({ x, xref: "x", y: 1, yref: "paper", text: label, showarrow: false, xanchor: "left", yanchor: "top", xshift: 4, yshift: ay, font: { color: ink(), size: 11 } });
    const lay = layout({
      title: { text: `${e.cell}: the two EOL rules differ by ${Math.round(e.gap)} cycles`, font: { size: 13, color: ink() } },
      margin: { l: 56, r: 16, t: 40, b: 60 }, xaxis: { title: { text: "cycle" } }, yaxis: { title: { text: "SOH (%)" } },
      shapes: [
        { type: "line", xref: "x", yref: "paper", x0: e.raw_cross, x1: e.raw_cross, y0: 0, y1: 1, line: { width: 1.5, dash: "dash", color: ink() } },
        { type: "line", xref: "x", yref: "paper", x0: e.eol, x1: e.eol, y0: 0, y1: 1, line: { width: 1.5, dash: "dash", color: ink() } },
        { type: "line", xref: "paper", yref: "y", x0: 0, x1: 1, y0: 80, y1: 80, line: { width: 1, dash: "dot", color: muted() } },
      ],
      annotations: [vline(e.raw_cross, `raw first crossing (cycle ${e.raw_cross})`, -4), vline(e.eol, `EOL label, sustained rule (cycle ${e.eol})`, -4)],
    });
    return { traces, layout: styleAxes(lay) };
  });
}

function corr(d) {
  plot("eda-corr", () => {
    const feats = [...new Set(d.corr.map((r) => r.feature))];
    const slot = { nasa: 1, calce: 2, toyota: 3 };
    const traces = ["nasa", "calce", "toyota"].map((ds) => {
      const m = Object.fromEntries(d.corr.filter((r) => r.dataset === ds).map((r) => [r.feature, r]));
      return {
        type: "bar", orientation: "h", name: DATASET_LABEL[ds], y: feats, x: feats.map((f) => m[f]?.rho ?? null),
        customdata: feats.map((f) => m[f]?.n ?? null), marker: { color: series(slot[ds]) },
        hovertemplate: `${DATASET_LABEL[ds]}<br>%{y}<br>Spearman ρ = %{x:.2f}<br>n = %{customdata:,} cycles<extra></extra>`,
      };
    });
    const lay = layout({ barmode: "group", margin: { l: 130, r: 16, t: 16, b: 60 }, xaxis: { title: { text: "Spearman ρ with SOH" }, range: [-1, 1] }, yaxis: { autorange: "reversed" }, legend: { orientation: "h", y: -0.25 } });
    return { traces, layout: styleAxes(lay) };
  });
}

export function render(d) {
  table(d);
  sohPanel(d);
  life(d);
  early(d);
  nasaRegen(d);
  calceDips(d);
  eol(d);
  corr(d);
}
