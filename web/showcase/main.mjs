// Showcase entry: theme toggle, hero tiles, pipeline diagram, then the EDA and results charts.

const $ = (id) => document.getElementById(id);

// ---------- theme toggle (charts redraw on 'themechange') ----------
$("theme").addEventListener("click", () => {
  const dark = matchMedia("(prefers-color-scheme: dark)").matches;
  const cur = document.documentElement.dataset.theme || (dark ? "dark" : "light");
  document.documentElement.dataset.theme = cur === "dark" ? "light" : "dark";
  window.dispatchEvent(new Event("themechange"));
});

// ---------- pipeline diagram ----------
function pipeline() {
  const steps = [
    ["Raw data", "NASA .mat · CALCE .xlsx · Toyota HDF5"],
    ["Canonical schema", "pandera-validated, checksummed"],
    ["Tasks & labels", "SOH · forecast · RUL; EOL rules"],
    ["Leakage-safe splits", "LOCO / official; train-only scaling"],
    ["18 models", "equal-budget Optuna, 5 seeds"],
    ["Evaluation", "CIs, Wilcoxon+Holm, mean rank"],
    ["CQR calibration", "90 % intervals"],
    ["Deployment", "ONNX in the browser"],
  ];
  const w = 122, gap = 15, y = 40, h = 70;
  let s = "";
  steps.forEach(([t, sub], i) => {
    const x = 4 + i * (w + gap);
    s += `<rect class="box" x="${x}" y="${y}" width="${w}" height="${h}" rx="8"/>`;
    s += `<text x="${x + w / 2}" y="${y + 28}" text-anchor="middle" font-weight="600">${t}</text>`;
    const words = sub.split(" ");
    const mid = Math.ceil(words.length / 2);
    [words.slice(0, mid).join(" "), words.slice(mid).join(" ")].forEach((line, j) => {
      s += `<text class="sub" x="${x + w / 2}" y="${y + 46 + j * 14}" text-anchor="middle">${line}</text>`;
    });
    if (i < steps.length - 1) {
      const ax = x + w + 2;
      s += `<path class="arrow" d="M${ax} ${y + h / 2} L${ax + gap - 4} ${y + h / 2} M${ax + gap - 9} ${y + h / 2 - 4} L${ax + gap - 4} ${y + h / 2} L${ax + gap - 9} ${y + h / 2 + 4}"/>`;
    }
  });
  $("pipeline").innerHTML = s;
}

function heroTiles(summary) {
  $("hero-tiles").innerHTML = summary
    .map((t) => `<div class="tile"><div class="k">${t.k}</div><div class="v">${t.v}</div><div class="k">${t.s}</div></div>`)
    .join("");
}

function guard(name, fn) {
  try {
    fn();
  } catch (e) {
    console.error(name, e);
  }
}

async function part(name) {
  // Each part = showcase/<name>.mjs (render) + showcase/data/<name>.json; parts load independently.
  try {
    const [mod, data] = await Promise.all([
      import(`./${name}.mjs`),
      fetch(`showcase/data/${name}.json`).then((r) => r.json()),
    ]);
    mod.render(data);
    return data;
  } catch (e) {
    console.error(`part ${name}`, e);
    return null;
  }
}

async function main() {
  pipeline();
  const [, core] = await Promise.all([part("eda"), part("results_core"), part("results_more"), part("method"), part("regen")]);
  if (core?.hero) heroTiles(core.hero);
  if (core?.horizon_note) $("res-horizon-note").innerHTML = core.horizon_note;
}
main();
