// Shared chart style for the showcase (dataviz reference palette; fixed entity colours).
// Every chart module imports from here so models keep the same colour on every chart.

/** Fixed model -> slot mapping (colour follows the entity, never its rank). */
export const MODEL_SLOT = {
  itransformer: 1, // blue
  lgbm: 2, // orange
  itransformer_sc: 3, // aqua
  patchtst: 7, // violet
  lstm: 5, // magenta
};
export const LABEL = {
  itransformer: "iTransformer (MC)",
  itransformer_sc: "iTransformer (SC)",
  lgbm: "LightGBM",
  elasticnet: "ElasticNet",
  patchtst: "PatchTST",
  nlinear: "NLinear",
  dlinear: "DLinear",
  rlinear: "RLinear",
  lstm: "LSTM",
  gru: "GRU",
  transformer: "Transformer",
  persistence: "Persistence (SOH stays the same)",
  last_slope: "Last slope",
  prev_soh: "Previous SOH",
  param_linear: "Linear fit",
  param_exp2: "Double-exponential fit",
  param_power: "Power-law fit",
  gpr: "Gaussian process",
};
export const DATASET_LABEL = {
  nasa: "NASA",
  calce: "CALCE",
  toyota: "Toyota/MIT",
  "toyota-test1": "Toyota test 1",
  "toyota-test2": "Toyota test 2",
  "nasa-loco": "NASA",
  "calce-loco": "CALCE",
};

const css = (n) => getComputedStyle(document.documentElement).getPropertyValue(n).trim();

/** Colour for a model: its fixed slot, persistence = muted ink (dashed), others = grey. */
export function modelColor(model) {
  const slot = MODEL_SLOT[model];
  if (slot) return css(`--series-${slot}`);
  if (model === "persistence" || model === "last_slope") return css("--text-secondary");
  return css("--other");
}
export function modelDash(model) {
  return model === "persistence" || model === "last_slope" ? "dash" : "solid";
}
export const isHighlighted = (m) => m in MODEL_SLOT || m === "persistence";
export const series = (i) => css(`--series-${i}`);
export const ink = () => css("--text-primary");
export const muted = () => css("--text-secondary");

/** Base Plotly layout: recessive grid, no chart junk, legend on top. */
export function layout(extra = {}) {
  const grid = css("--grid");
  const ax = { gridcolor: grid, zerolinecolor: grid, linecolor: grid, tickcolor: grid, automargin: true };
  return {
    paper_bgcolor: "rgba(0,0,0,0)",
    plot_bgcolor: "rgba(0,0,0,0)",
    font: { family: "system-ui, -apple-system, Segoe UI, sans-serif", size: 12, color: css("--text-primary") },
    margin: { l: 56, r: 16, t: 36, b: 48 },
    hoverlabel: { bgcolor: css("--surface-2"), bordercolor: grid, font: { color: css("--text-primary") } },
    legend: { orientation: "h", y: -0.18, font: { size: 11 } },
    xaxis: { ...ax, ...(extra.xaxis || {}) },
    yaxis: { ...ax, ...(extra.yaxis || {}) },
    ...Object.fromEntries(Object.entries(extra).filter(([k]) => k !== "xaxis" && k !== "yaxis")),
  };
}
/** Apply the base axis style to extra axes (xaxis2, yaxis3, ...) of a subplot layout. */
export function styleAxes(lay) {
  const grid = css("--grid");
  for (const k of Object.keys(lay)) {
    if (/^[xy]axis\d*$/.test(k)) Object.assign(lay[k], { gridcolor: grid, zerolinecolor: grid, linecolor: grid, automargin: true, ...lay[k] });
  }
  return lay;
}
export const CONFIG = { responsive: true, displaylogo: false, modeBarButtonsToRemove: ["lasso2d", "select2d"] };

/** Render into #id; charts redraw on theme change via window event 'themechange'. */
export function plot(id, buildFn) {
  const draw = () => {
    const { traces, layout: lay } = buildFn();
    Plotly.react(id, traces, lay, CONFIG);
  };
  draw();
  window.addEventListener("themechange", draw);
}

export const fmt = (v, d = 2) => (v == null || Number.isNaN(v) ? "–" : Number(v).toFixed(d));
