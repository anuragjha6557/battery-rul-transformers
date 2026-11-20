# Benchmark tables: field_probe

- Protocol version: 1.1
- Git SHA: b7c03e9756
- Seeds: 1  |  unit runs: 27
- Note: n = 4 cells per NASA/CALCE dataset, so the 95 % cluster-bootstrap CI is wide by construction. Toyota rows are over test cells (test1 / test2 separately) with a cell-level bootstrap CI and a Holm-adjusted Wilcoxon p vs the best baseline. All metrics are computed per cell from the logged predictions.

## Headline (kind = overall; RMSE in %SOH, RUL MAE in cycles)

### calce_soh

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse | age_only | 6.887 [4.966, 8.809] |  |  | 4 | 1 | 725b8fcf |
| loco | all | overall | rmse | elasticnet | 4.700 [2.023, 9.188] |  |  | 4 | 1 | 1c5c4d61 |
| loco | all | overall | rmse | lgbm | 4.581 [2.465, 6.295] |  |  | 4 | 1 | 0a4fb8a0 |
| loco | start_points | overall | rmse | age_only | 1.172 [0.494, 1.884] |  |  | 4 | 1 | 725b8fcf |
| loco | start_points | overall | rmse | elasticnet | 2.302 [1.551, 3.201] |  |  | 4 | 1 | 1c5c4d61 |
| loco | start_points | overall | rmse | lgbm | 0.708 [0.638, 0.777] |  |  | 4 | 1 | 0a4fb8a0 |

### nasa_soh

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse | age_only | 5.846 [3.492, 8.201] |  | 2.929 | 4 | 1 | 67382b1a |
| loco | all | overall | rmse | elasticnet | 2.270 [1.601, 2.939] |  | 1.321 | 4 | 1 | 5a0bdeda |
| loco | all | overall | rmse | lgbm | 4.003 [2.183, 7.178] |  | 2.207 | 4 | 1 | fb5850b9 |
| loco | start_points | overall | rmse | age_only | 5.033 [4.479, 5.367] |  | 4.212 | 4 | 1 | 67382b1a |
| loco | start_points | overall | rmse | elasticnet | 2.685 [1.821, 3.628] |  | 2.041 | 4 | 1 | 5a0bdeda |
| loco | start_points | overall | rmse | lgbm | 2.886 [1.708, 4.065] |  | 1.243 | 4 | 1 | fb5850b9 |

### toyota_soh

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rmse | age_only | 4.008 [3.665, 4.471] |  |  | 43 | 1 | c1cb4cc4 |
| test1 | all | overall | rmse | elasticnet | 1.137 [0.940, 1.373] |  |  | 43 | 1 | dcd326fc |
| test1 | all | overall | rmse | lgbm | 0.723 [0.566, 0.924] |  |  | 43 | 1 | ebace092 |
| test1 | start_points | overall | rmse | age_only | 2.168 [1.705, 2.664] |  |  | 43 | 1 | c1cb4cc4 |
| test1 | start_points | overall | rmse | elasticnet | 0.938 [0.731, 1.192] |  |  | 43 | 1 | dcd326fc |
| test1 | start_points | overall | rmse | lgbm | 0.434 [0.328, 0.573] |  |  | 43 | 1 | ebace092 |
| test2 | all | overall | rmse | age_only | 3.673 [3.520, 3.821] |  |  | 40 | 1 | c1cb4cc4 |
| test2 | all | overall | rmse | elasticnet | 16.539 [15.492, 17.709] |  |  | 40 | 1 | dcd326fc |
| test2 | all | overall | rmse | lgbm | 4.113 [3.965, 4.251] |  |  | 40 | 1 | ebace092 |
| test2 | start_points | overall | rmse | age_only | 3.509 [3.286, 3.718] |  |  | 40 | 1 | c1cb4cc4 |
| test2 | start_points | overall | rmse | elasticnet | 5.704 [5.455, 5.960] |  |  | 40 | 1 | dcd326fc |
| test2 | start_points | overall | rmse | lgbm | 4.269 [4.042, 4.491] |  |  | 40 | 1 | ebace092 |

## Mean rank (dataset x task x split x policy x headline metric)

| model | mean rank | conditions | missing |
|---|---|---|---|
| lgbm | 1.50 | 8 | 0 |
| elasticnet | 2.12 | 8 | 0 |
| age_only | 2.38 | 8 | 0 |

## Full tables

<details><summary>calce_soh (21 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse | age_only | 6.887 [4.966, 8.809] |  |  | 4 | 1 | 725b8fcf |
| loco | all | overall | rmse | elasticnet | 4.700 [2.023, 9.188] |  |  | 4 | 1 | 1c5c4d61 |
| loco | all | overall | rmse | lgbm | 4.581 [2.465, 6.295] |  |  | 4 | 1 | 0a4fb8a0 |
| loco | start_points | fixed:200 | rmse | age_only | 1.381 [0.763, 1.760] |  |  | 4 | 1 | 725b8fcf |
| loco | start_points | fixed:200 | rmse | elasticnet | 2.578 [1.530, 3.626] |  |  | 4 | 1 | 1c5c4d61 |
| loco | start_points | fixed:200 | rmse | lgbm | 0.627 [0.250, 1.005] |  |  | 4 | 1 | 0a4fb8a0 |
| loco | start_points | fixed:400 | rmse | age_only | 0.390 [0.127, 0.727] |  |  | 4 | 1 | 725b8fcf |
| loco | start_points | fixed:400 | rmse | elasticnet | 2.102 [1.272, 3.355] |  |  | 4 | 1 | 1c5c4d61 |
| loco | start_points | fixed:400 | rmse | lgbm | 0.613 [0.420, 0.826] |  |  | 4 | 1 | 0a4fb8a0 |
| loco | start_points | frac:0.3 | rmse | age_only | 1.300 [0.351, 2.471] |  |  | 4 | 1 | 725b8fcf |
| loco | start_points | frac:0.3 | rmse | elasticnet | 2.294 [1.103, 3.556] |  |  | 4 | 1 | 1c5c4d61 |
| loco | start_points | frac:0.3 | rmse | lgbm | 0.754 [0.620, 0.912] |  |  | 4 | 1 | 0a4fb8a0 |
| loco | start_points | frac:0.5 | rmse | age_only | 1.037 [0.242, 2.422] |  |  | 4 | 1 | 725b8fcf |
| loco | start_points | frac:0.5 | rmse | elasticnet | 1.771 [0.723, 2.714] |  |  | 4 | 1 | 1c5c4d61 |
| loco | start_points | frac:0.5 | rmse | lgbm | 0.595 [0.234, 1.032] |  |  | 4 | 1 | 0a4fb8a0 |
| loco | start_points | frac:0.7 | rmse | age_only | 0.832 [0.212, 1.534] |  |  | 4 | 1 | 725b8fcf |
| loco | start_points | frac:0.7 | rmse | elasticnet | 2.137 [1.231, 3.312] |  |  | 4 | 1 | 1c5c4d61 |
| loco | start_points | frac:0.7 | rmse | lgbm | 0.651 [0.539, 0.827] |  |  | 4 | 1 | 0a4fb8a0 |
| loco | start_points | overall | rmse | age_only | 1.172 [0.494, 1.884] |  |  | 4 | 1 | 725b8fcf |
| loco | start_points | overall | rmse | elasticnet | 2.302 [1.551, 3.201] |  |  | 4 | 1 | 1c5c4d61 |
| loco | start_points | overall | rmse | lgbm | 0.708 [0.638, 0.777] |  |  | 4 | 1 | 0a4fb8a0 |

</details>

<details><summary>nasa_soh (21 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse | age_only | 5.846 [3.492, 8.201] |  | 2.929 | 4 | 1 | 67382b1a |
| loco | all | overall | rmse | elasticnet | 2.270 [1.601, 2.939] |  | 1.321 | 4 | 1 | 5a0bdeda |
| loco | all | overall | rmse | lgbm | 4.003 [2.183, 7.178] |  | 2.207 | 4 | 1 | fb5850b9 |
| loco | start_points | fixed:30 | rmse | age_only | 4.134 [3.969, 4.299] |  | 4.327 | 4 | 1 | 67382b1a |
| loco | start_points | fixed:30 | rmse | elasticnet | 2.633 [0.942, 4.323] |  | 3.955 | 4 | 1 | 5a0bdeda |
| loco | start_points | fixed:30 | rmse | lgbm | 2.903 [1.512, 3.968] |  | 0.930 | 4 | 1 | fb5850b9 |
| loco | start_points | fixed:50 | rmse | age_only | 4.566 [3.204, 5.580] |  | 2.579 | 4 | 1 | 67382b1a |
| loco | start_points | fixed:50 | rmse | elasticnet | 2.485 [0.906, 4.064] |  | 0.721 | 4 | 1 | 5a0bdeda |
| loco | start_points | fixed:50 | rmse | lgbm | 3.135 [1.432, 4.865] |  | 0.910 | 4 | 1 | fb5850b9 |
| loco | start_points | frac:0.3 | rmse | age_only | 5.236 [4.785, 5.687] |  | 4.570 | 4 | 1 | 67382b1a |
| loco | start_points | frac:0.3 | rmse | elasticnet | 2.607 [1.490, 3.992] |  | 1.476 | 4 | 1 | 5a0bdeda |
| loco | start_points | frac:0.3 | rmse | lgbm | 3.311 [2.411, 4.765] |  | 2.259 | 4 | 1 | fb5850b9 |
| loco | start_points | frac:0.5 | rmse | age_only | 5.305 [4.473, 5.862] |  | 5.811 | 4 | 1 | 67382b1a |
| loco | start_points | frac:0.5 | rmse | elasticnet | 2.772 [1.259, 4.285] |  | 1.019 | 4 | 1 | 5a0bdeda |
| loco | start_points | frac:0.5 | rmse | lgbm | 1.994 [0.422, 3.567] |  | 0.083 | 4 | 1 | fb5850b9 |
| loco | start_points | frac:0.7 | rmse | age_only | 5.452 [3.767, 6.609] |  | 2.946 | 4 | 1 | 67382b1a |
| loco | start_points | frac:0.7 | rmse | elasticnet | 1.642 [0.850, 2.434] |  | 1.201 | 4 | 1 | 5a0bdeda |
| loco | start_points | frac:0.7 | rmse | lgbm | 2.041 [1.035, 3.894] |  | 0.964 | 4 | 1 | fb5850b9 |
| loco | start_points | overall | rmse | age_only | 5.033 [4.479, 5.367] |  | 4.212 | 4 | 1 | 67382b1a |
| loco | start_points | overall | rmse | elasticnet | 2.685 [1.821, 3.628] |  | 2.041 | 4 | 1 | 5a0bdeda |
| loco | start_points | overall | rmse | lgbm | 2.886 [1.708, 4.065] |  | 1.243 | 4 | 1 | fb5850b9 |

</details>

<details><summary>toyota_soh (36 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rmse | age_only | 4.008 [3.665, 4.471] |  |  | 43 | 1 | c1cb4cc4 |
| test1 | all | overall | rmse | elasticnet | 1.137 [0.940, 1.373] |  |  | 43 | 1 | dcd326fc |
| test1 | all | overall | rmse | lgbm | 0.723 [0.566, 0.924] |  |  | 43 | 1 | ebace092 |
| test1 | start_points | fixed:100 | rmse | age_only | 0.567 [0.284, 1.052] |  |  | 43 | 1 | c1cb4cc4 |
| test1 | start_points | fixed:100 | rmse | elasticnet | 0.731 [0.528, 1.025] |  |  | 43 | 1 | dcd326fc |
| test1 | start_points | fixed:100 | rmse | lgbm | 0.276 [0.145, 0.462] |  |  | 43 | 1 | ebace092 |
| test1 | start_points | frac:0.3 | rmse | age_only | 1.299 [0.894, 1.783] |  |  | 43 | 1 | c1cb4cc4 |
| test1 | start_points | frac:0.3 | rmse | elasticnet | 0.847 [0.627, 1.113] |  |  | 43 | 1 | dcd326fc |
| test1 | start_points | frac:0.3 | rmse | lgbm | 0.193 [0.137, 0.257] |  |  | 43 | 1 | ebace092 |
| test1 | start_points | frac:0.5 | rmse | age_only | 2.498 [1.876, 3.154] |  |  | 43 | 1 | c1cb4cc4 |
| test1 | start_points | frac:0.5 | rmse | elasticnet | 0.887 [0.657, 1.144] |  |  | 43 | 1 | dcd326fc |
| test1 | start_points | frac:0.5 | rmse | lgbm | 0.369 [0.273, 0.476] |  |  | 43 | 1 | ebace092 |
| test1 | start_points | frac:0.7 | rmse | age_only | 2.778 [2.187, 3.412] |  |  | 43 | 1 | c1cb4cc4 |
| test1 | start_points | frac:0.7 | rmse | elasticnet | 0.864 [0.586, 1.216] |  |  | 43 | 1 | dcd326fc |
| test1 | start_points | frac:0.7 | rmse | lgbm | 0.568 [0.397, 0.780] |  |  | 43 | 1 | ebace092 |
| test1 | start_points | overall | rmse | age_only | 2.168 [1.705, 2.664] |  |  | 43 | 1 | c1cb4cc4 |
| test1 | start_points | overall | rmse | elasticnet | 0.938 [0.731, 1.192] |  |  | 43 | 1 | dcd326fc |
| test1 | start_points | overall | rmse | lgbm | 0.434 [0.328, 0.573] |  |  | 43 | 1 | ebace092 |
| test2 | all | overall | rmse | age_only | 3.673 [3.520, 3.821] |  |  | 40 | 1 | c1cb4cc4 |
| test2 | all | overall | rmse | elasticnet | 16.539 [15.492, 17.709] |  |  | 40 | 1 | dcd326fc |
| test2 | all | overall | rmse | lgbm | 4.113 [3.965, 4.251] |  |  | 40 | 1 | ebace092 |
| test2 | start_points | fixed:100 | rmse | age_only | 0.252 [0.146, 0.387] |  |  | 40 | 1 | c1cb4cc4 |
| test2 | start_points | fixed:100 | rmse | elasticnet | 4.773 [4.546, 5.008] |  |  | 40 | 1 | dcd326fc |
| test2 | start_points | fixed:100 | rmse | lgbm | 4.155 [3.932, 4.393] |  |  | 40 | 1 | ebace092 |
| test2 | start_points | frac:0.3 | rmse | age_only | 2.216 [1.814, 2.689] |  |  | 40 | 1 | c1cb4cc4 |
| test2 | start_points | frac:0.3 | rmse | elasticnet | 5.420 [5.214, 5.633] |  |  | 40 | 1 | dcd326fc |
| test2 | start_points | frac:0.3 | rmse | lgbm | 4.409 [4.096, 4.739] |  |  | 40 | 1 | ebace092 |
| test2 | start_points | frac:0.5 | rmse | age_only | 4.875 [4.499, 5.210] |  |  | 40 | 1 | c1cb4cc4 |
| test2 | start_points | frac:0.5 | rmse | elasticnet | 6.195 [5.844, 6.547] |  |  | 40 | 1 | dcd326fc |
| test2 | start_points | frac:0.5 | rmse | lgbm | 4.388 [3.931, 4.817] |  |  | 40 | 1 | ebace092 |
| test2 | start_points | frac:0.7 | rmse | age_only | 4.258 [3.958, 4.524] |  |  | 40 | 1 | c1cb4cc4 |
| test2 | start_points | frac:0.7 | rmse | elasticnet | 6.181 [5.744, 6.574] |  |  | 40 | 1 | dcd326fc |
| test2 | start_points | frac:0.7 | rmse | lgbm | 3.615 [3.158, 4.074] |  |  | 40 | 1 | ebace092 |
| test2 | start_points | overall | rmse | age_only | 3.509 [3.286, 3.718] |  |  | 40 | 1 | c1cb4cc4 |
| test2 | start_points | overall | rmse | elasticnet | 5.704 [5.455, 5.960] |  |  | 40 | 1 | dcd326fc |
| test2 | start_points | overall | rmse | lgbm | 4.269 [4.042, 4.491] |  |  | 40 | 1 | ebace092 |

</details>
