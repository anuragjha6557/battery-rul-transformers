// Parity test: web/field.mjs vs the Python FieldPredictor (vectors from scripts/export_onnx_field.py).
// hist/tab are rebuilt from the CSV text and must match the Python tensors; the final result is
// computed from the stored ONNX outputs (no ONNX in node) and must match FieldPredictor.predict.
// Run: node tests/web/test_field.mjs
import { readFileSync } from "node:fs";
import assert from "node:assert/strict";
import {
  InputError, cleanInputs, parseCSV, pastExpandingMedian, pastRollingMedian, postprocess, prepare, validateField,
} from "../../web/field.mjs";

const here = new URL(".", import.meta.url).pathname;
const vectors = JSON.parse(readFileSync(`${here}field_vectors.json`, "utf8"));
const metas = Object.fromEntries(
  ["nasa", "calce", "toyota"].map((p) => [p, JSON.parse(readFileSync(`${here}field_serve_meta_${p}.json`, "utf8"))]),
);

const close = (a, b, tol, what) => {
  assert.equal(a.length, b.length, `${what}: length`);
  for (let i = 0; i < a.length; i++) assert.ok(Math.abs(a[i] - b[i]) <= tol, `${what}[${i}]: ${a[i]} vs ${b[i]}`);
};
const rel = (a, b, tol, what) => assert.ok(Math.abs(a - b) <= tol * Math.max(1, Math.abs(b)), `${what}: ${a} vs ${b}`);

let n = 0, nCounts = 0;
for (const v of vectors) {
  const meta = metas[v.protocol];
  const frame = validateField(parseCSV(v.csv), meta);
  const prep = prepare(meta, frame);
  close(prep.scaledLast, v.scaled_last, 1e-6, `${v.name} scaled last row`);
  const q = {};
  for (const t of Object.keys(meta.tasks)) {
    close(Array.from(prep.hist[t]), v.hist[t].flat(), 1e-5, `${v.name} ${t} hist`);
    close(Array.from(prep.tab), v.tab[t], 1e-5, `${v.name} ${t} tab`);
    q[t] = Float32Array.from(v.q[t].flat());
  }
  const res = postprocess(meta, frame, prep, q), py = v.predict;
  assert.deepEqual(res.cleaning, py.cleaning, `${v.name} cleaning counts`);
  nCounts += Object.keys(py.cleaning).length;
  assert.equal(res.n_cycles, py.n_cycles);
  assert.equal(res.last_cycle, py.last_cycle);
  const keys = ["soh", "lo", "hi"];
  for (const k of keys) close([res.soh_now[k]], [py.soh_now[k]], 1e-6, `${v.name} soh_now.${k}`);
  assert.equal(res.soh_now.useful, py.soh_now.useful, `${v.name} soh_now.useful`);
  assert.equal(res.forecast.length, py.forecast.length);
  res.forecast.forEach((f, i) => {
    assert.equal(f.horizon, py.forecast[i].horizon);
    assert.equal(f.cycle, py.forecast[i].cycle);
    assert.equal(f.useful, py.forecast[i].useful, `${v.name} forecast[${i}].useful`);
    for (const k of keys) close([f[k]], [py.forecast[i][k]], 1e-6, `${v.name} forecast[${i}].${k}`);
  });
  for (const k of ["cycles", "lo", "hi", "eol_cycle"]) rel(res.rul[k], py.rul[k], 1e-4, `${v.name} rul.${k}`);
  assert.equal(res.rul.already_below_threshold, py.rul.already_below_threshold);
  assert.equal(res.coverage, py.coverage);
  assert.equal(res.ood.is_ood, py.ood.is_ood, `${v.name} ood flag`);
  close([res.ood.distance], [py.ood.distance], 1e-6, `${v.name} ood distance`);
  assert.deepEqual(res.ood.flags, py.ood.flags, `${v.name} ood flags`);
  n++;
}
assert.ok(nCounts > 0, "vectors must exercise the cleaning rules");

// rolling-median semantics: NaN rows occupy window slots but do not count as observations
const nan = Number.NaN;
const show = (a) => Array.from(a).map((x) => (Number.isNaN(x) ? "nan" : x));
assert.deepEqual(show(pastRollingMedian(Float64Array.of(1, 2, nan, 4, 5, 6), 3, 2)), ["nan", "nan", 1.5, 1.5, 3, 4.5]);
assert.deepEqual(show(pastExpandingMedian(Float64Array.of(5, 1, nan, 3, 9), 3)), ["nan", "nan", "nan", "nan", 3]);

// a paused charge masks its duration-derived columns; NaN never trips a rule
{
  const N = 12, meta = metas.toyota;
  const cols = new Map([
    ["charge_time_s", new Float64Array(N).fill(1000)],
    ["cv_time_s", new Float64Array(N).fill(600)],
    ["ir_ohm", new Float64Array(N).fill(0.016)],
    ["rest_before_s", new Float64Array(N).fill(nan)],
  ]);
  cols.get("charge_time_s")[8] = 4000;
  cols.get("ir_ohm")[5] = nan;
  const { cols: out, counts } = cleanInputs({ n: N, cols }, meta.cleaning);
  assert.equal(counts.charge_pause, 1);
  assert.ok(Number.isNaN(out.get("cv_time_s")[8]) && Number.isNaN(out.get("charge_time_s")[8]));
  assert.equal(out.get("cv_time_s")[7], 600);
  assert.equal(counts.ir_ohm, 0);
}

// input validation mirrors the InputError cases
const toy = metas.toyota;
const hdr = "cycle_idx,cv_time_s\n";
const rows = (k, f = (i) => i) => Array.from({ length: k }, (_, i) => `${f(i)},600`).join("\n");
const bad = [
  "foo,bar\n1,2",
  hdr + rows(4),
  hdr + rows(8, (i) => i % 4),
  "cycle_idx,cv_time_s\n1,600\n2,600\nx,600\n4,600\n5,600\n6,600",
];
for (const text of bad) assert.throws(() => validateField(parseCSV(text), toy), InputError);
assert.throws(() => parseCSV("cycle_idx\n"), InputError);
// case-insensitive headers; blank / non-numeric -> NaN; unknown columns ignored; absent columns all NaN
const body = Array.from({ length: 6 }, (_, i) => `${6 - i},${i % 2 ? "" : "oops"},0.9`).join("\n");
const ok = validateField(parseCSV(`CYCLE_IDX,Cv_Time_S,soh_measured\n${body}`), toy);
assert.deepEqual(ok.cycle_idx, [1, 2, 3, 4, 5, 6]);
assert.ok(ok.cols.get("cv_time_s").every(Number.isNaN) && ok.cols.get("ir_ohm").every(Number.isNaN));
console.log(`ok: ${n} uploads match the Python FieldPredictor (${nCounts} cleaning counts checked); ${bad.length + 1} input errors raised`);
