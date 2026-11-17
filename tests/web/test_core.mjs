// Parity test: web/core.mjs vs the Python predictor (vectors from scripts/export_onnx.py).
// Run: node tests/web/test_core.mjs [tests/web/test_vectors.json tests/web/serve_meta.json]
import { readFileSync } from "node:fs";
import assert from "node:assert/strict";
import { InputError, parseCSV, postprocess, prepare, validate } from "../../web/core.mjs";

const here = new URL(".", import.meta.url).pathname;
const vectors = JSON.parse(readFileSync(process.argv[2] ?? `${here}test_vectors.json`, "utf8"));
const meta = JSON.parse(readFileSync(process.argv[3] ?? `${here}serve_meta.json`, "utf8"));

const close = (a, b, tol, what) => {
  assert.equal(a.length, b.length, `${what}: length`);
  for (let i = 0; i < a.length; i++) {
    assert.ok(Math.abs(a[i] - b[i]) <= tol, `${what}[${i}]: ${a[i]} vs ${b[i]}`);
  }
};

let n = 0;
for (const v of vectors) {
  const rows = validate({ cycle_idx: v.cycle_idx, capacity_ah: v.capacity_ah }, meta.min_cycles);
  const p = prepare(meta, rows);
  close(Array.from(p.histF), v.forecast.hist.flat(), 1e-6, `${v.name} forecast window`);
  close(Array.from(p.histR), v.rul.hist.flat(), 1e-6, `${v.name} rul window`);
  // float32 summaries; curvature is ~1e-6 so compare relatively as well
  close(Array.from(p.tab), v.forecast.tab, 1e-6, `${v.name} summaries`);
  const res = postprocess(meta, rows.cycle_idx, p.soh, p.tab, Float32Array.from(v.forecast.q.flat()),
    Float32Array.from(v.rul.q.flat()));
  const py = v.predict;
  for (const k of ["soh", "lo", "hi"]) {
    close(res.forecast.map((f) => f[k]), py.forecast.map((f) => f[k]), 1e-6, `${v.name} forecast.${k}`);
  }
  for (const k of ["cycles", "lo", "hi", "eol_cycle"]) close([res.rul[k]], [py.rul[k]], 1e-3, `${v.name} rul.${k}`);
  assert.equal(res.ood.is_ood, py.ood.is_ood, `${v.name} ood flag`);
  close([res.ood.distance], [py.ood.distance], 1e-3, `${v.name} ood distance`);
  assert.deepEqual(res.ood.flags.length, py.ood.flags.length, `${v.name} ood flags`);
  n++;
}

// input validation mirrors InputError cases
const bad = [
  "foo,bar\n1,2",
  "cycle_idx,capacity_ah\n" + Array.from({ length: 5 }, (_, i) => `${i},1`).join("\n"),
  "cycle_idx,capacity_ah\n" + Array.from({ length: 12 }, (_, i) => `${i % 6},1`).join("\n"),
  "cycle_idx,capacity_ah\n" + Array.from({ length: 12 }, (_, i) => `${i},${i ? 1 : 0}`).join("\n"),
];
for (const text of bad) {
  assert.throws(() => validate(parseCSV(text), meta.min_cycles), InputError);
}
console.log(`ok: ${n} demo cells match the Python predictor; ${bad.length} input errors raised`);
