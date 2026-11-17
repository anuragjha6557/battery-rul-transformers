# Benchmark tables: abl_recursive

- Protocol version: 1.1
- Git SHA: 1fba81a99d
- Seeds: 5  |  unit runs: 45
- Note: n = 4 cells per NASA/CALCE dataset, so the 95 % cluster-bootstrap CI is wide by construction. Toyota rows are over test cells (test1 / test2 separately) with a cell-level bootstrap CI and a Holm-adjusted Wilcoxon p vs the best baseline. All metrics are computed per cell from the logged predictions.

## Headline (kind = overall; RMSE in %SOH, RUL MAE in cycles)

### calce_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | recursive | 1.944 [1.842, 2.045] |  |  | 4 | 5 | fdbbd898 |
| loco | all | overall | rmse_h10 | recursive | 2.404 [2.338, 2.493] |  |  | 4 | 5 | fdbbd898 |
| loco | all | overall | rmse_h50 | recursive | 6.921 [5.971, 7.872] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | overall | rmse_h1 | recursive | 0.367 [0.160, 0.574] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | overall | rmse_h10 | recursive | 1.141 [0.872, 1.477] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | overall | rmse_h50 | recursive | 1.320 [0.987, 1.653] |  |  | 4 | 5 | fdbbd898 |

### nasa_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | recursive | 0.925 [0.649, 1.200] |  | 1.288 | 4 | 5 | 82f9d05a |
| loco | all | overall | rmse_h10 | recursive | 2.076 [1.471, 2.680] |  | 3.041 | 4 | 5 | 82f9d05a |
| loco | all | overall | rmse_h50 | recursive | 30.285 [25.102, 37.062] |  | 28.356 | 4 | 5 | 82f9d05a |
| loco | start_points | overall | rmse_h1 | recursive | 1.782 [1.045, 2.519] |  | 2.643 | 4 | 5 | 82f9d05a |
| loco | start_points | overall | rmse_h10 | recursive | 2.147 [1.068, 3.570] |  | 4.222 | 4 | 5 | 82f9d05a |
| loco | start_points | overall | rmse_h50 | recursive | 39.624 [37.183, 42.396] |  | 38.537 | 4 | 5 | 82f9d05a |

### toyota_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rmse_h1 | recursive | 0.118 [0.070, 0.174] |  |  | 43 | 5 | e5d6a401 |
| test1 | all | overall | rmse_h10 | recursive | 0.147 [0.102, 0.200] |  |  | 43 | 5 | e5d6a401 |
| test1 | all | overall | rmse_h50 | recursive | 0.616 [0.516, 0.733] |  |  | 43 | 5 | e5d6a401 |
| test1 | start_points | overall | rmse_h1 | recursive | 0.037 [0.022, 0.056] |  |  | 43 | 5 | e5d6a401 |
| test1 | start_points | overall | rmse_h10 | recursive | 0.105 [0.060, 0.160] |  |  | 43 | 5 | e5d6a401 |
| test1 | start_points | overall | rmse_h50 | recursive | 0.399 [0.263, 0.564] |  |  | 43 | 5 | e5d6a401 |
| test2 | all | overall | rmse_h1 | recursive | 0.015 [0.012, 0.017] |  |  | 40 | 5 | e5d6a401 |
| test2 | all | overall | rmse_h10 | recursive | 0.036 [0.032, 0.040] |  |  | 40 | 5 | e5d6a401 |
| test2 | all | overall | rmse_h50 | recursive | 0.229 [0.208, 0.251] |  |  | 40 | 5 | e5d6a401 |
| test2 | start_points | overall | rmse_h1 | recursive | 0.011 [0.007, 0.016] |  |  | 40 | 5 | e5d6a401 |
| test2 | start_points | overall | rmse_h10 | recursive | 0.024 [0.021, 0.027] |  |  | 40 | 5 | e5d6a401 |
| test2 | start_points | overall | rmse_h50 | recursive | 0.123 [0.109, 0.140] |  |  | 40 | 5 | e5d6a401 |

## Mean rank (dataset x task x split x policy x headline metric)

| model | mean rank | conditions | missing |
|---|---|---|---|
| recursive | 1.00 | 24 | 0 |

## Full tables

<details><summary>calce_forecast (35 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | recursive | 1.944 [1.842, 2.045] |  |  | 4 | 5 | fdbbd898 |
| loco | all | overall | rmse_h10 | recursive | 2.404 [2.338, 2.493] |  |  | 4 | 5 | fdbbd898 |
| loco | all | overall | rmse_h100 | recursive | 26.175 [17.513, 34.838] |  |  | 4 | 5 | fdbbd898 |
| loco | all | overall | rmse_h25 | recursive | 3.311 [3.153, 3.455] |  |  | 4 | 5 | fdbbd898 |
| loco | all | overall | rmse_h50 | recursive | 6.921 [5.971, 7.872] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | fixed:200 | rmse_h1 | recursive | 0.265 [0.208, 0.306] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | fixed:200 | rmse_h10 | recursive | 1.041 [0.234, 2.295] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | fixed:200 | rmse_h100 | recursive | 1.849 [1.184, 2.387] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | fixed:200 | rmse_h25 | recursive | 0.901 [0.653, 1.265] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | fixed:200 | rmse_h50 | recursive | 0.817 [0.746, 0.940] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | fixed:400 | rmse_h1 | recursive | 0.100 [0.020, 0.184] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | fixed:400 | rmse_h10 | recursive | 0.761 [0.267, 1.260] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | fixed:400 | rmse_h100 | recursive | 2.991 [1.233, 4.748] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | fixed:400 | rmse_h25 | recursive | 1.069 [0.679, 1.550] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | fixed:400 | rmse_h50 | recursive | 1.252 [0.507, 2.232] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | frac:0.3 | rmse_h1 | recursive | 0.328 [0.036, 0.841] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | frac:0.3 | rmse_h10 | recursive | 0.962 [0.593, 1.332] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | frac:0.3 | rmse_h100 | recursive | 0.785 [0.585, 0.984] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | frac:0.3 | rmse_h25 | recursive | 0.683 [0.550, 0.869] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | frac:0.3 | rmse_h50 | recursive | 1.588 [0.927, 2.582] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | frac:0.5 | rmse_h1 | recursive | 0.443 [0.063, 1.000] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | frac:0.5 | rmse_h10 | recursive | 1.138 [0.551, 1.711] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | frac:0.5 | rmse_h100 | recursive | 2.538 [1.735, 3.470] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | frac:0.5 | rmse_h25 | recursive | 1.369 [0.840, 1.954] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | frac:0.5 | rmse_h50 | recursive | 1.161 [0.735, 1.821] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | frac:0.7 | rmse_h1 | recursive | 0.149 [0.054, 0.239] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | frac:0.7 | rmse_h10 | recursive | 0.748 [0.262, 1.421] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | frac:0.7 | rmse_h100 | recursive | 2.582 [1.155, 3.872] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | frac:0.7 | rmse_h25 | recursive | 0.760 [0.364, 1.423] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | frac:0.7 | rmse_h50 | recursive | 0.701 [0.126, 1.277] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | overall | rmse_h1 | recursive | 0.367 [0.160, 0.574] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | overall | rmse_h10 | recursive | 1.141 [0.872, 1.477] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | overall | rmse_h100 | recursive | 2.428 [1.633, 3.223] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | overall | rmse_h25 | recursive | 1.104 [0.935, 1.272] |  |  | 4 | 5 | fdbbd898 |
| loco | start_points | overall | rmse_h50 | recursive | 1.320 [0.987, 1.653] |  |  | 4 | 5 | fdbbd898 |

</details>

<details><summary>nasa_forecast (35 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | recursive | 0.925 [0.649, 1.200] |  | 1.288 | 4 | 5 | 82f9d05a |
| loco | all | overall | rmse_h10 | recursive | 2.076 [1.471, 2.680] |  | 3.041 | 4 | 5 | 82f9d05a |
| loco | all | overall | rmse_h100 | recursive | 837.296 [391.867, 1282.725] |  | 388.848 | 4 | 5 | 82f9d05a |
| loco | all | overall | rmse_h25 | recursive | 5.377 [4.496, 6.351] |  | 6.880 | 4 | 5 | 82f9d05a |
| loco | all | overall | rmse_h50 | recursive | 30.285 [25.102, 37.062] |  | 28.356 | 4 | 5 | 82f9d05a |
| loco | start_points | fixed:30 | rmse_h1 | recursive | 2.238 [1.158, 3.246] |  | 0.638 | 4 | 5 | 82f9d05a |
| loco | start_points | fixed:30 | rmse_h10 | recursive | 1.139 [0.352, 2.673] |  | 3.443 | 4 | 5 | 82f9d05a |
| loco | start_points | fixed:30 | rmse_h100 | recursive | 687.282 [398.770, 1025.381] |  | 608.311 | 4 | 5 | 82f9d05a |
| loco | start_points | fixed:30 | rmse_h25 | recursive | 5.275 [2.217, 8.334] |  | 8.881 | 4 | 5 | 82f9d05a |
| loco | start_points | fixed:30 | rmse_h50 | recursive | 28.810 [22.662, 34.958] |  | 31.212 | 4 | 5 | 82f9d05a |
| loco | start_points | fixed:50 | rmse_h1 | recursive | 0.530 [0.082, 1.178] |  | 1.539 | 4 | 5 | 82f9d05a |
| loco | start_points | fixed:50 | rmse_h10 | recursive | 1.259 [0.413, 2.663] |  | 3.406 | 4 | 5 | 82f9d05a |
| loco | start_points | fixed:50 | rmse_h100 | recursive | 1831.310 [548.286, 2805.749] |  |  | 3 | 5 | 15556ebb |
| loco | start_points | fixed:50 | rmse_h25 | recursive | 8.438 [5.505, 12.309] |  | 14.034 | 4 | 5 | 82f9d05a |
| loco | start_points | fixed:50 | rmse_h50 | recursive | 58.448 [49.325, 67.570] |  | 66.717 | 4 | 5 | 82f9d05a |
| loco | start_points | frac:0.3 | rmse_h1 | recursive | 0.136 [0.079, 0.220] |  | 0.078 | 4 | 5 | 82f9d05a |
| loco | start_points | frac:0.3 | rmse_h10 | recursive | 1.666 [0.704, 2.774] |  | 0.887 | 4 | 5 | 82f9d05a |
| loco | start_points | frac:0.3 | rmse_h100 | recursive | 804.087 [345.273, 1262.901] |  | 442.710 | 4 | 5 | 82f9d05a |
| loco | start_points | frac:0.3 | rmse_h25 | recursive | 5.719 [2.801, 8.637] |  | 9.940 | 4 | 5 | 82f9d05a |
| loco | start_points | frac:0.3 | rmse_h50 | recursive | 29.229 [26.378, 34.680] |  | 26.745 | 4 | 5 | 82f9d05a |
| loco | start_points | frac:0.5 | rmse_h1 | recursive | 1.981 [0.180, 3.782] |  | 3.870 | 4 | 5 | 82f9d05a |
| loco | start_points | frac:0.5 | rmse_h10 | recursive | 2.345 [0.349, 6.004] |  | 7.869 | 4 | 5 | 82f9d05a |
| loco | start_points | frac:0.5 | rmse_h100 | recursive | 1000.510 [309.333, 1763.515] |  |  | 3 | 5 | 15556ebb |
| loco | start_points | frac:0.5 | rmse_h25 | recursive | 5.951 [4.646, 7.256] |  | 6.724 | 4 | 5 | 82f9d05a |
| loco | start_points | frac:0.5 | rmse_h50 | recursive | 34.813 [23.078, 43.495] |  | 17.869 | 4 | 5 | 82f9d05a |
| loco | start_points | frac:0.7 | rmse_h1 | recursive | 1.374 [0.164, 3.150] |  | 4.131 | 4 | 5 | 82f9d05a |
| loco | start_points | frac:0.7 | rmse_h10 | recursive | 2.051 [1.371, 2.732] |  | 1.305 | 4 | 5 | 82f9d05a |
| loco | start_points | frac:0.7 | rmse_h100 | recursive | 92.049 |  |  | 1 | 5 | 780b8171 |
| loco | start_points | frac:0.7 | rmse_h25 | recursive | 5.495 [3.483, 7.224] |  | 5.099 | 4 | 5 | 82f9d05a |
| loco | start_points | frac:0.7 | rmse_h50 | recursive | 28.560 [19.731, 38.206] |  | 25.829 | 4 | 5 | 82f9d05a |
| loco | start_points | overall | rmse_h1 | recursive | 1.782 [1.045, 2.519] |  | 2.643 | 4 | 5 | 82f9d05a |
| loco | start_points | overall | rmse_h10 | recursive | 2.147 [1.068, 3.570] |  | 4.222 | 4 | 5 | 82f9d05a |
| loco | start_points | overall | rmse_h100 | recursive | 1051.253 [446.024, 1656.482] |  | 533.962 | 4 | 5 | 82f9d05a |
| loco | start_points | overall | rmse_h25 | recursive | 6.749 [5.114, 8.582] |  | 9.605 | 4 | 5 | 82f9d05a |
| loco | start_points | overall | rmse_h50 | recursive | 39.624 [37.183, 42.396] |  | 38.537 | 4 | 5 | 82f9d05a |

</details>

<details><summary>toyota_forecast (60 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rmse_h1 | recursive | 0.118 [0.070, 0.174] |  |  | 43 | 5 | e5d6a401 |
| test1 | all | overall | rmse_h10 | recursive | 0.147 [0.102, 0.200] |  |  | 43 | 5 | e5d6a401 |
| test1 | all | overall | rmse_h100 | recursive | 1.747 [1.487, 2.100] |  |  | 43 | 5 | e5d6a401 |
| test1 | all | overall | rmse_h200 | recursive | 4.860 [4.346, 5.375] |  |  | 42 | 5 | e5d6a401 |
| test1 | all | overall | rmse_h50 | recursive | 0.616 [0.516, 0.733] |  |  | 43 | 5 | e5d6a401 |
| test1 | start_points | fixed:100 | rmse_h1 | recursive | 0.010 [0.007, 0.014] |  |  | 43 | 5 | e5d6a401 |
| test1 | start_points | fixed:100 | rmse_h10 | recursive | 0.022 [0.013, 0.034] |  |  | 43 | 5 | e5d6a401 |
| test1 | start_points | fixed:100 | rmse_h100 | recursive | 0.407 [0.354, 0.462] |  |  | 42 | 5 | e5d6a401 |
| test1 | start_points | fixed:100 | rmse_h200 | recursive | 1.518 [1.289, 1.786] |  |  | 42 | 5 | e5d6a401 |
| test1 | start_points | fixed:100 | rmse_h50 | recursive | 0.125 [0.087, 0.184] |  |  | 43 | 5 | e5d6a401 |
| test1 | start_points | frac:0.3 | rmse_h1 | recursive | 0.013 [0.008, 0.021] |  |  | 43 | 5 | e5d6a401 |
| test1 | start_points | frac:0.3 | rmse_h10 | recursive | 0.049 [0.022, 0.084] |  |  | 43 | 5 | e5d6a401 |
| test1 | start_points | frac:0.3 | rmse_h100 | recursive | 0.553 [0.400, 0.756] |  |  | 43 | 5 | e5d6a401 |
| test1 | start_points | frac:0.3 | rmse_h200 | recursive | 1.892 [1.571, 2.217] |  |  | 42 | 5 | e5d6a401 |
| test1 | start_points | frac:0.3 | rmse_h50 | recursive | 0.147 [0.098, 0.223] |  |  | 43 | 5 | e5d6a401 |
| test1 | start_points | frac:0.5 | rmse_h1 | recursive | 0.033 [0.017, 0.055] |  |  | 43 | 5 | e5d6a401 |
| test1 | start_points | frac:0.5 | rmse_h10 | recursive | 0.102 [0.047, 0.176] |  |  | 43 | 5 | e5d6a401 |
| test1 | start_points | frac:0.5 | rmse_h100 | recursive | 1.146 [0.764, 1.606] |  |  | 42 | 5 | e5d6a401 |
| test1 | start_points | frac:0.5 | rmse_h200 | recursive | 5.050 [3.997, 6.150] |  |  | 41 | 5 | e5d6a401 |
| test1 | start_points | frac:0.5 | rmse_h50 | recursive | 0.396 [0.199, 0.648] |  |  | 43 | 5 | e5d6a401 |
| test1 | start_points | frac:0.7 | rmse_h1 | recursive | 0.048 [0.023, 0.081] |  |  | 43 | 5 | e5d6a401 |
| test1 | start_points | frac:0.7 | rmse_h10 | recursive | 0.110 [0.047, 0.200] |  |  | 43 | 5 | e5d6a401 |
| test1 | start_points | frac:0.7 | rmse_h100 | recursive | 1.888 [1.379, 2.586] |  |  | 42 | 5 | e5d6a401 |
| test1 | start_points | frac:0.7 | rmse_h200 | recursive | 4.820 [3.685, 6.295] |  |  | 17 | 5 | e5d6a401 |
| test1 | start_points | frac:0.7 | rmse_h50 | recursive | 0.488 [0.322, 0.736] |  |  | 43 | 5 | e5d6a401 |
| test1 | start_points | overall | rmse_h1 | recursive | 0.037 [0.022, 0.056] |  |  | 43 | 5 | e5d6a401 |
| test1 | start_points | overall | rmse_h10 | recursive | 0.105 [0.060, 0.160] |  |  | 43 | 5 | e5d6a401 |
| test1 | start_points | overall | rmse_h100 | recursive | 1.341 [1.014, 1.739] |  |  | 43 | 5 | e5d6a401 |
| test1 | start_points | overall | rmse_h200 | recursive | 3.937 [3.402, 4.500] |  |  | 42 | 5 | e5d6a401 |
| test1 | start_points | overall | rmse_h50 | recursive | 0.399 [0.263, 0.564] |  |  | 43 | 5 | e5d6a401 |
| test2 | all | overall | rmse_h1 | recursive | 0.015 [0.012, 0.017] |  |  | 40 | 5 | e5d6a401 |
| test2 | all | overall | rmse_h10 | recursive | 0.036 [0.032, 0.040] |  |  | 40 | 5 | e5d6a401 |
| test2 | all | overall | rmse_h100 | recursive | 0.816 [0.728, 0.913] |  |  | 40 | 5 | e5d6a401 |
| test2 | all | overall | rmse_h200 | recursive | 2.585 [2.260, 2.967] |  |  | 40 | 5 | e5d6a401 |
| test2 | all | overall | rmse_h50 | recursive | 0.229 [0.208, 0.251] |  |  | 40 | 5 | e5d6a401 |
| test2 | start_points | fixed:100 | rmse_h1 | recursive | 0.006 [0.004, 0.008] |  |  | 40 | 5 | e5d6a401 |
| test2 | start_points | fixed:100 | rmse_h10 | recursive | 0.015 [0.012, 0.021] |  |  | 40 | 5 | e5d6a401 |
| test2 | start_points | fixed:100 | rmse_h100 | recursive | 0.247 [0.226, 0.269] |  |  | 40 | 5 | e5d6a401 |
| test2 | start_points | fixed:100 | rmse_h200 | recursive | 0.829 [0.776, 0.883] |  |  | 40 | 5 | e5d6a401 |
| test2 | start_points | fixed:100 | rmse_h50 | recursive | 0.051 [0.043, 0.060] |  |  | 40 | 5 | e5d6a401 |
| test2 | start_points | frac:0.3 | rmse_h1 | recursive | 0.012 [0.005, 0.021] |  |  | 40 | 5 | e5d6a401 |
| test2 | start_points | frac:0.3 | rmse_h10 | recursive | 0.013 [0.010, 0.017] |  |  | 40 | 5 | e5d6a401 |
| test2 | start_points | frac:0.3 | rmse_h100 | recursive | 0.335 [0.284, 0.397] |  |  | 40 | 5 | e5d6a401 |
| test2 | start_points | frac:0.3 | rmse_h200 | recursive | 1.190 [0.945, 1.522] |  |  | 40 | 5 | e5d6a401 |
| test2 | start_points | frac:0.3 | rmse_h50 | recursive | 0.102 [0.082, 0.129] |  |  | 40 | 5 | e5d6a401 |
| test2 | start_points | frac:0.5 | rmse_h1 | recursive | 0.007 [0.006, 0.008] |  |  | 40 | 5 | e5d6a401 |
| test2 | start_points | frac:0.5 | rmse_h10 | recursive | 0.025 [0.019, 0.032] |  |  | 40 | 5 | e5d6a401 |
| test2 | start_points | frac:0.5 | rmse_h100 | recursive | 0.431 [0.333, 0.550] |  |  | 40 | 5 | e5d6a401 |
| test2 | start_points | frac:0.5 | rmse_h200 | recursive | 1.816 [1.309, 2.462] |  |  | 40 | 5 | e5d6a401 |
| test2 | start_points | frac:0.5 | rmse_h50 | recursive | 0.115 [0.093, 0.141] |  |  | 40 | 5 | e5d6a401 |
| test2 | start_points | frac:0.7 | rmse_h1 | recursive | 0.010 [0.006, 0.017] |  |  | 40 | 5 | e5d6a401 |
| test2 | start_points | frac:0.7 | rmse_h10 | recursive | 0.023 [0.020, 0.027] |  |  | 40 | 5 | e5d6a401 |
| test2 | start_points | frac:0.7 | rmse_h100 | recursive | 0.604 [0.519, 0.711] |  |  | 40 | 5 | e5d6a401 |
| test2 | start_points | frac:0.7 | rmse_h200 | recursive | 3.086 [2.691, 3.535] |  |  | 38 | 5 | e5d6a401 |
| test2 | start_points | frac:0.7 | rmse_h50 | recursive | 0.151 [0.134, 0.169] |  |  | 40 | 5 | e5d6a401 |
| test2 | start_points | overall | rmse_h1 | recursive | 0.011 [0.007, 0.016] |  |  | 40 | 5 | e5d6a401 |
| test2 | start_points | overall | rmse_h10 | recursive | 0.024 [0.021, 0.027] |  |  | 40 | 5 | e5d6a401 |
| test2 | start_points | overall | rmse_h100 | recursive | 0.458 [0.393, 0.540] |  |  | 40 | 5 | e5d6a401 |
| test2 | start_points | overall | rmse_h200 | recursive | 2.144 [1.812, 2.538] |  |  | 40 | 5 | e5d6a401 |
| test2 | start_points | overall | rmse_h50 | recursive | 0.123 [0.109, 0.140] |  |  | 40 | 5 | e5d6a401 |

</details>
