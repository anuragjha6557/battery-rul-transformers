# Benchmark tables: smoke

- Protocol version: 1.1
- Git SHA: b10bf00929
- Seeds: 1  |  unit runs: 18
- Note: n = 4 cells per NASA/CALCE dataset, so the 95 % cluster-bootstrap CI is wide by construction. Toyota rows are over test cells (test1 / test2 separately) with a cell-level bootstrap CI and a Holm-adjusted Wilcoxon p vs the best baseline. All metrics are computed per cell from the logged predictions.

## Headline (kind = overall; RMSE in %SOH, RUL MAE in cycles)

### calce_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | last_slope | 2.686 [2.506, 2.869] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | all | overall | rmse_h1 | persistence | 2.606 [2.429, 2.783] |  |  | 4 | 1 | c77e8f0d |
| loco | all | overall | rmse_h10 | last_slope | 4.266 [4.097, 4.435] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | all | overall | rmse_h10 | persistence | 3.071 [3.003, 3.139] |  |  | 4 | 1 | c77e8f0d |
| loco | all | overall | rmse_h50 | last_slope | 13.491 [12.984, 13.882] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | all | overall | rmse_h50 | persistence | 6.278 [5.955, 6.519] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | overall | rmse_h1 | last_slope | 0.455 [0.240, 0.669] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | overall | rmse_h1 | persistence | 0.397 [0.177, 0.617] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | overall | rmse_h10 | last_slope | 2.474 [2.053, 3.110] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | overall | rmse_h10 | persistence | 1.332 [1.082, 1.703] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | overall | rmse_h50 | last_slope | 7.343 [6.361, 8.324] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | overall | rmse_h50 | persistence | 1.506 [1.020, 1.989] |  |  | 4 | 1 | c77e8f0d |

### nasa_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | last_slope | 0.992 [0.715, 1.269] | 0/4 cells, 0/4 cell-seeds (vs persistence) | 1.301 | 4 | 1 | ade93415 |
| loco | all | overall | rmse_h1 | persistence | 0.955 [0.697, 1.213] |  | 1.245 | 4 | 1 | 1c7e63ef |
| loco | all | overall | rmse_h10 | last_slope | 2.986 [2.037, 3.934] | 2/4 cells, 2/4 cell-seeds (vs persistence) | 3.895 | 4 | 1 | ade93415 |
| loco | all | overall | rmse_h10 | persistence | 2.737 [2.186, 3.288] |  | 3.153 | 4 | 1 | 1c7e63ef |
| loco | all | overall | rmse_h50 | last_slope | 12.164 [8.884, 15.444] | 2/4 cells, 2/4 cell-seeds (vs persistence) | 14.476 | 4 | 1 | ade93415 |
| loco | all | overall | rmse_h50 | persistence | 11.211 [9.697, 12.759] |  | 11.258 | 4 | 1 | 1c7e63ef |
| loco | start_points | overall | rmse_h1 | last_slope | 1.909 [1.139, 2.679] | 0/4 cells, 0/4 cell-seeds (vs persistence) | 2.642 | 4 | 1 | ade93415 |
| loco | start_points | overall | rmse_h1 | persistence | 1.654 [1.057, 2.251] |  | 2.261 | 4 | 1 | 1c7e63ef |
| loco | start_points | overall | rmse_h10 | last_slope | 3.935 [2.490, 5.381] | 2/4 cells, 2/4 cell-seeds (vs persistence) | 5.540 | 4 | 1 | ade93415 |
| loco | start_points | overall | rmse_h10 | persistence | 3.348 [2.574, 4.229] |  | 3.206 | 4 | 1 | 1c7e63ef |
| loco | start_points | overall | rmse_h50 | last_slope | 14.573 [9.092, 19.775] | 2/4 cells, 2/4 cell-seeds (vs persistence) | 21.338 | 4 | 1 | ade93415 |
| loco | start_points | overall | rmse_h50 | persistence | 13.452 [11.482, 15.613] |  | 12.879 | 4 | 1 | 1c7e63ef |

### toyota_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rmse_h1 | last_slope | 0.137 [0.081, 0.203] |  |  | 43 | 1 | 77403933 |
| test1 | all | overall | rmse_h1 | persistence | 0.158 [0.106, 0.219] | p=4.16e-06 (vs last_slope) |  | 43 | 1 | 85a8557f |
| test1 | all | overall | rmse_h10 | last_slope | 0.265 [0.184, 0.359] |  |  | 43 | 1 | 77403933 |
| test1 | all | overall | rmse_h10 | persistence | 0.600 [0.526, 0.679] | p=5.6e-09 (vs last_slope) |  | 43 | 1 | 85a8557f |
| test1 | all | overall | rmse_h50 | last_slope | 1.202 [0.954, 1.480] |  |  | 43 | 1 | 77403933 |
| test1 | all | overall | rmse_h50 | persistence | 2.502 [2.179, 2.849] | p=2.87e-08 (vs last_slope) |  | 43 | 1 | 85a8557f |
| test1 | start_points | overall | rmse_h1 | last_slope | 0.052 [0.033, 0.074] | p=0.0854 (vs persistence) |  | 43 | 1 | 77403933 |
| test1 | start_points | overall | rmse_h1 | persistence | 0.045 [0.032, 0.061] |  |  | 43 | 1 | 85a8557f |
| test1 | start_points | overall | rmse_h10 | last_slope | 0.239 [0.099, 0.422] | p=0.00277 (vs persistence) |  | 43 | 1 | 77403933 |
| test1 | start_points | overall | rmse_h10 | persistence | 0.234 [0.180, 0.307] |  |  | 43 | 1 | 85a8557f |
| test1 | start_points | overall | rmse_h50 | last_slope | 1.101 [0.460, 1.991] |  |  | 43 | 1 | 77403933 |
| test1 | start_points | overall | rmse_h50 | persistence | 1.197 [0.940, 1.577] | p=0.000391 (vs last_slope) |  | 43 | 1 | 85a8557f |
| test2 | all | overall | rmse_h1 | last_slope | 0.016 [0.014, 0.019] |  |  | 40 | 1 | 77403933 |
| test2 | all | overall | rmse_h1 | persistence | 0.036 [0.034, 0.038] | p=1.82e-12 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | all | overall | rmse_h10 | last_slope | 0.057 [0.051, 0.063] |  |  | 40 | 1 | 77403933 |
| test2 | all | overall | rmse_h10 | persistence | 0.303 [0.281, 0.324] | p=1.82e-12 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | all | overall | rmse_h50 | last_slope | 0.397 [0.360, 0.434] |  |  | 40 | 1 | 77403933 |
| test2 | all | overall | rmse_h50 | persistence | 1.354 [1.265, 1.437] | p=1.82e-12 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | start_points | overall | rmse_h1 | last_slope | 0.014 [0.008, 0.022] |  |  | 40 | 1 | 77403933 |
| test2 | start_points | overall | rmse_h1 | persistence | 0.018 [0.012, 0.025] | p=4.15e-06 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | start_points | overall | rmse_h10 | last_slope | 0.032 [0.025, 0.040] |  |  | 40 | 1 | 77403933 |
| test2 | start_points | overall | rmse_h10 | persistence | 0.090 [0.078, 0.105] | p=2e-10 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | start_points | overall | rmse_h50 | last_slope | 0.133 [0.113, 0.154] |  |  | 40 | 1 | 77403933 |
| test2 | start_points | overall | rmse_h50 | persistence | 0.472 [0.408, 0.547] | p=9.09e-12 (vs last_slope) |  | 40 | 1 | 85a8557f |

## Mean rank (dataset x task x split x policy x headline metric)

| model | mean rank | conditions | missing |
|---|---|---|---|
| persistence | 1.42 | 24 | 0 |
| last_slope | 1.58 | 24 | 0 |

## Full tables

<details><summary>calce_forecast (70 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | last_slope | 2.686 [2.506, 2.869] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | all | overall | rmse_h1 | persistence | 2.606 [2.429, 2.783] |  |  | 4 | 1 | c77e8f0d |
| loco | all | overall | rmse_h10 | last_slope | 4.266 [4.097, 4.435] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | all | overall | rmse_h10 | persistence | 3.071 [3.003, 3.139] |  |  | 4 | 1 | c77e8f0d |
| loco | all | overall | rmse_h100 | last_slope | 25.209 [24.266, 26.151] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | all | overall | rmse_h100 | persistence | 10.293 [9.591, 10.966] |  |  | 4 | 1 | c77e8f0d |
| loco | all | overall | rmse_h25 | last_slope | 7.632 [7.376, 7.792] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | all | overall | rmse_h25 | persistence | 4.180 [4.046, 4.314] |  |  | 4 | 1 | c77e8f0d |
| loco | all | overall | rmse_h50 | last_slope | 13.491 [12.984, 13.882] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | all | overall | rmse_h50 | persistence | 6.278 [5.955, 6.519] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:200 | rmse_h1 | last_slope | 0.422 [0.201, 0.609] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:200 | rmse_h1 | persistence | 0.347 [0.209, 0.485] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:200 | rmse_h10 | last_slope | 2.318 [0.806, 4.329] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:200 | rmse_h10 | persistence | 1.344 [0.340, 2.774] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:200 | rmse_h100 | last_slope | 10.695 [6.175, 15.216] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:200 | rmse_h100 | persistence | 1.897 [1.120, 2.489] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:200 | rmse_h25 | last_slope | 2.579 [0.690, 4.821] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:200 | rmse_h25 | persistence | 0.840 [0.239, 1.441] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:200 | rmse_h50 | last_slope | 4.995 [1.687, 8.303] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:200 | rmse_h50 | persistence | 0.844 [0.319, 1.572] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:400 | rmse_h1 | last_slope | 0.081 [0.034, 0.158] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:400 | rmse_h1 | persistence | 0.080 [0.019, 0.194] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:400 | rmse_h10 | last_slope | 1.629 [1.035, 2.223] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:400 | rmse_h10 | persistence | 1.009 [0.324, 1.694] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:400 | rmse_h100 | last_slope | 6.898 [1.827, 11.957] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:400 | rmse_h100 | persistence | 3.346 [1.619, 5.072] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:400 | rmse_h25 | last_slope | 2.439 [1.474, 3.403] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:400 | rmse_h25 | persistence | 1.333 [0.586, 2.081] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:400 | rmse_h50 | last_slope | 3.432 [1.337, 4.769] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:400 | rmse_h50 | persistence | 1.656 [0.742, 2.680] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.3 | rmse_h1 | last_slope | 0.474 [0.215, 0.961] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.3 | rmse_h1 | persistence | 0.373 [0.089, 0.866] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.3 | rmse_h10 | last_slope | 3.126 [1.808, 4.454] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.3 | rmse_h10 | persistence | 0.952 [0.590, 1.315] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.3 | rmse_h100 | last_slope | 22.123 [7.983, 36.262] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.3 | rmse_h100 | persistence | 0.918 [0.565, 1.150] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.3 | rmse_h25 | last_slope | 5.620 [1.950, 9.290] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.3 | rmse_h25 | persistence | 0.865 [0.571, 1.180] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.3 | rmse_h50 | last_slope | 10.522 [4.959, 16.085] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.3 | rmse_h50 | persistence | 1.300 [0.353, 2.350] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.5 | rmse_h1 | last_slope | 0.642 [0.198, 1.085] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.5 | rmse_h1 | persistence | 0.524 [0.047, 1.016] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.5 | rmse_h10 | last_slope | 2.527 [1.938, 3.130] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.5 | rmse_h10 | persistence | 1.354 [0.510, 1.928] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.5 | rmse_h100 | last_slope | 14.573 [5.467, 22.398] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.5 | rmse_h100 | persistence | 2.842 [2.048, 3.830] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.5 | rmse_h25 | last_slope | 4.282 [2.681, 6.100] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.5 | rmse_h25 | persistence | 1.599 [0.788, 2.409] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.5 | rmse_h50 | last_slope | 7.386 [2.980, 11.306] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.5 | rmse_h50 | persistence | 1.521 [0.930, 2.368] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.7 | rmse_h1 | last_slope | 0.112 [0.044, 0.200] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.7 | rmse_h1 | persistence | 0.092 [0.023, 0.162] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.7 | rmse_h10 | last_slope | 0.861 [0.120, 1.788] | 2/4 cells, 2/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.7 | rmse_h10 | persistence | 0.717 [0.237, 1.507] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.7 | rmse_h100 | last_slope | 2.351 [0.391, 5.280] |  |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.7 | rmse_h100 | persistence | 3.080 [1.373, 4.710] | 2/4 cells, 2/4 cell-seeds (vs last_slope) |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.7 | rmse_h25 | last_slope | 1.577 [0.923, 2.657] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.7 | rmse_h25 | persistence | 0.714 [0.117, 1.649] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.7 | rmse_h50 | last_slope | 1.873 [1.076, 3.358] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.7 | rmse_h50 | persistence | 1.046 [0.194, 1.898] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | overall | rmse_h1 | last_slope | 0.455 [0.240, 0.669] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | overall | rmse_h1 | persistence | 0.397 [0.177, 0.617] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | overall | rmse_h10 | last_slope | 2.474 [2.053, 3.110] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | overall | rmse_h10 | persistence | 1.332 [1.082, 1.703] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | overall | rmse_h100 | last_slope | 15.247 [12.166, 18.329] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | overall | rmse_h100 | persistence | 2.680 [1.781, 3.658] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | overall | rmse_h25 | last_slope | 4.141 [3.336, 4.947] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | overall | rmse_h25 | persistence | 1.317 [1.143, 1.422] |  |  | 4 | 1 | c77e8f0d |
| loco | start_points | overall | rmse_h50 | last_slope | 7.343 [6.361, 8.324] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 2751ee9f |
| loco | start_points | overall | rmse_h50 | persistence | 1.506 [1.020, 1.989] |  |  | 4 | 1 | c77e8f0d |

</details>

<details><summary>nasa_forecast (70 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | last_slope | 0.992 [0.715, 1.269] | 0/4 cells, 0/4 cell-seeds (vs persistence) | 1.301 | 4 | 1 | ade93415 |
| loco | all | overall | rmse_h1 | persistence | 0.955 [0.697, 1.213] |  | 1.245 | 4 | 1 | 1c7e63ef |
| loco | all | overall | rmse_h10 | last_slope | 2.986 [2.037, 3.934] | 2/4 cells, 2/4 cell-seeds (vs persistence) | 3.895 | 4 | 1 | ade93415 |
| loco | all | overall | rmse_h10 | persistence | 2.737 [2.186, 3.288] |  | 3.153 | 4 | 1 | 1c7e63ef |
| loco | all | overall | rmse_h100 | last_slope | 20.888 [14.826, 29.272] |  | 14.274 | 4 | 1 | ade93415 |
| loco | all | overall | rmse_h100 | persistence | 21.343 [19.065, 23.828] | 1/4 cells, 1/4 cell-seeds (vs last_slope) | 20.144 | 4 | 1 | 1c7e63ef |
| loco | all | overall | rmse_h25 | last_slope | 5.958 [4.205, 7.710] | 2/4 cells, 2/4 cell-seeds (vs persistence) | 7.523 | 4 | 1 | ade93415 |
| loco | all | overall | rmse_h25 | persistence | 5.731 [4.913, 6.569] |  | 6.007 | 4 | 1 | 1c7e63ef |
| loco | all | overall | rmse_h50 | last_slope | 12.164 [8.884, 15.444] | 2/4 cells, 2/4 cell-seeds (vs persistence) | 14.476 | 4 | 1 | ade93415 |
| loco | all | overall | rmse_h50 | persistence | 11.211 [9.697, 12.759] |  | 11.258 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:30 | rmse_h1 | last_slope | 2.349 [1.110, 3.513] | 1/4 cells, 1/4 cell-seeds (vs persistence) | 0.537 | 4 | 1 | ade93415 |
| loco | start_points | fixed:30 | rmse_h1 | persistence | 2.105 [1.142, 2.970] |  | 0.659 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:30 | rmse_h10 | last_slope | 0.696 [0.129, 1.432] |  | 0.251 | 4 | 1 | ade93415 |
| loco | start_points | fixed:30 | rmse_h10 | persistence | 2.367 [1.235, 4.018] | 0/4 cells, 0/4 cell-seeds (vs last_slope) | 0.977 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:30 | rmse_h100 | last_slope | 11.712 [0.440, 29.881] |  | 6.309 | 4 | 1 | ade93415 |
| loco | start_points | fixed:30 | rmse_h100 | persistence | 22.041 [19.036, 25.046] | 1/4 cells, 1/4 cell-seeds (vs last_slope) | 18.594 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:30 | rmse_h25 | last_slope | 2.904 [0.640, 6.334] |  | 1.727 | 4 | 1 | ade93415 |
| loco | start_points | fixed:30 | rmse_h25 | persistence | 5.609 [4.366, 7.695] | 0/4 cells, 0/4 cell-seeds (vs last_slope) | 4.798 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:30 | rmse_h50 | last_slope | 6.306 [1.574, 11.656] |  | 7.235 | 4 | 1 | ade93415 |
| loco | start_points | fixed:30 | rmse_h50 | persistence | 14.185 [12.427, 16.944] | 0/4 cells, 0/4 cell-seeds (vs last_slope) | 13.377 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:50 | rmse_h1 | last_slope | 0.750 [0.234, 1.464] | 2/4 cells, 2/4 cell-seeds (vs persistence) | 0.104 | 4 | 1 | ade93415 |
| loco | start_points | fixed:50 | rmse_h1 | persistence | 0.733 [0.375, 1.283] |  | 0.313 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:50 | rmse_h10 | last_slope | 6.496 [3.997, 8.995] | 1/4 cells, 1/4 cell-seeds (vs persistence) | 8.191 | 4 | 1 | ade93415 |
| loco | start_points | fixed:50 | rmse_h10 | persistence | 4.762 [3.862, 6.436] |  | 4.024 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:50 | rmse_h100 | last_slope | 32.235 [15.395, 51.238] | 1/3 cells, 1/3 cell-seeds (vs persistence) |  | 3 | 1 | aa576a67 |
| loco | start_points | fixed:50 | rmse_h100 | persistence | 23.003 [19.038, 25.889] |  |  | 3 | 1 | 6583fd6a |
| loco | start_points | fixed:50 | rmse_h25 | last_slope | 14.547 [9.163, 19.931] | 1/4 cells, 1/4 cell-seeds (vs persistence) | 20.054 | 4 | 1 | ade93415 |
| loco | start_points | fixed:50 | rmse_h25 | persistence | 10.212 [8.506, 12.505] |  | 9.637 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:50 | rmse_h50 | last_slope | 23.648 [14.338, 32.958] | 1/4 cells, 1/4 cell-seeds (vs persistence) | 36.164 | 4 | 1 | ade93415 |
| loco | start_points | fixed:50 | rmse_h50 | persistence | 14.977 [12.995, 16.630] |  | 15.329 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.3 | rmse_h1 | last_slope | 0.366 [0.145, 0.587] | 1/4 cells, 1/4 cell-seeds (vs persistence) | 0.263 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.3 | rmse_h1 | persistence | 0.262 [0.062, 0.494] |  | 0.216 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.3 | rmse_h10 | last_slope | 3.289 [2.078, 4.500] | 1/4 cells, 1/4 cell-seeds (vs persistence) | 2.289 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.3 | rmse_h10 | persistence | 1.776 [0.447, 3.105] |  | 2.497 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.3 | rmse_h100 | last_slope | 23.144 [10.125, 30.488] | 1/4 cells, 1/4 cell-seeds (vs persistence) | 30.580 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.3 | rmse_h100 | persistence | 21.592 [17.906, 25.277] |  | 17.279 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.3 | rmse_h25 | last_slope | 6.727 [2.243, 10.150] | 1/4 cells, 1/4 cell-seeds (vs persistence) | 11.114 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.3 | rmse_h25 | persistence | 4.666 [2.061, 6.293] |  | 0.850 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.3 | rmse_h50 | last_slope | 10.464 [3.890, 15.179] |  | 12.503 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.3 | rmse_h50 | persistence | 13.452 [11.698, 15.205] | 2/4 cells, 2/4 cell-seeds (vs last_slope) | 11.427 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.5 | rmse_h1 | last_slope | 2.119 [0.305, 3.934] | 1/4 cells, 1/4 cell-seeds (vs persistence) | 3.857 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.5 | rmse_h1 | persistence | 1.752 [0.144, 3.360] |  | 3.372 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.5 | rmse_h10 | last_slope | 3.570 [1.260, 6.697] |  | 8.321 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.5 | rmse_h10 | persistence | 3.664 [2.972, 4.463] | 1/4 cells, 1/4 cell-seeds (vs last_slope) | 3.465 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.5 | rmse_h100 | last_slope | 26.098 [18.310, 39.660] | 1/3 cells, 1/3 cell-seeds (vs persistence) |  | 3 | 1 | aa576a67 |
| loco | start_points | frac:0.5 | rmse_h100 | persistence | 21.687 [16.103, 26.550] |  |  | 3 | 1 | 6583fd6a |
| loco | start_points | frac:0.5 | rmse_h25 | last_slope | 6.441 [3.728, 8.000] |  | 8.129 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.5 | rmse_h25 | persistence | 6.722 [4.992, 8.310] | 1/4 cells, 1/4 cell-seeds (vs last_slope) | 4.010 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.5 | rmse_h50 | last_slope | 12.312 [9.073, 14.516] |  | 14.191 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.5 | rmse_h50 | persistence | 13.020 [9.963, 16.219] | 1/4 cells, 1/4 cell-seeds (vs last_slope) | 10.087 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.7 | rmse_h1 | last_slope | 1.460 [0.161, 3.389] | 2/4 cells, 2/4 cell-seeds (vs persistence) | 4.434 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.7 | rmse_h1 | persistence | 1.282 [0.357, 2.907] |  | 3.690 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.7 | rmse_h10 | last_slope | 2.002 [0.811, 3.192] |  | 3.435 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.7 | rmse_h10 | persistence | 2.565 [1.535, 3.576] | 1/4 cells, 1/4 cell-seeds (vs last_slope) | 3.998 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.7 | rmse_h100 | last_slope | 28.756 | 0/1 cells, 0/1 cell-seeds (vs persistence) |  | 1 | 1 | 3bdc1438 |
| loco | start_points | frac:0.7 | rmse_h100 | persistence | 23.823 |  |  | 1 | 1 | 6252a211 |
| loco | start_points | frac:0.7 | rmse_h25 | last_slope | 4.359 [2.028, 8.175] |  | 10.004 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.7 | rmse_h25 | persistence | 7.057 [4.781, 9.333] | 1/4 cells, 1/4 cell-seeds (vs last_slope) | 8.579 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.7 | rmse_h50 | last_slope | 11.921 [5.216, 19.355] | 2/4 cells, 2/4 cell-seeds (vs persistence) | 23.634 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.7 | rmse_h50 | persistence | 10.912 [8.091, 13.103] |  | 13.532 | 4 | 1 | 1c7e63ef |
| loco | start_points | overall | rmse_h1 | last_slope | 1.909 [1.139, 2.679] | 0/4 cells, 0/4 cell-seeds (vs persistence) | 2.642 | 4 | 1 | ade93415 |
| loco | start_points | overall | rmse_h1 | persistence | 1.654 [1.057, 2.251] |  | 2.261 | 4 | 1 | 1c7e63ef |
| loco | start_points | overall | rmse_h10 | last_slope | 3.935 [2.490, 5.381] | 2/4 cells, 2/4 cell-seeds (vs persistence) | 5.540 | 4 | 1 | ade93415 |
| loco | start_points | overall | rmse_h10 | persistence | 3.348 [2.574, 4.229] |  | 3.206 | 4 | 1 | 1c7e63ef |
| loco | start_points | overall | rmse_h100 | last_slope | 23.985 [14.809, 34.609] | 2/4 cells, 2/4 cell-seeds (vs persistence) | 22.079 | 4 | 1 | ade93415 |
| loco | start_points | overall | rmse_h100 | persistence | 21.443 [18.142, 24.745] |  | 17.949 | 4 | 1 | 1c7e63ef |
| loco | start_points | overall | rmse_h25 | last_slope | 8.281 [5.214, 11.347] | 2/4 cells, 2/4 cell-seeds (vs persistence) | 11.788 | 4 | 1 | ade93415 |
| loco | start_points | overall | rmse_h25 | persistence | 7.261 [6.150, 8.841] |  | 6.423 | 4 | 1 | 1c7e63ef |
| loco | start_points | overall | rmse_h50 | last_slope | 14.573 [9.092, 19.775] | 2/4 cells, 2/4 cell-seeds (vs persistence) | 21.338 | 4 | 1 | ade93415 |
| loco | start_points | overall | rmse_h50 | persistence | 13.452 [11.482, 15.613] |  | 12.879 | 4 | 1 | 1c7e63ef |

</details>

<details><summary>toyota_forecast (120 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rmse_h1 | last_slope | 0.137 [0.081, 0.203] |  |  | 43 | 1 | 77403933 |
| test1 | all | overall | rmse_h1 | persistence | 0.158 [0.106, 0.219] | p=4.16e-06 (vs last_slope) |  | 43 | 1 | 85a8557f |
| test1 | all | overall | rmse_h10 | last_slope | 0.265 [0.184, 0.359] |  |  | 43 | 1 | 77403933 |
| test1 | all | overall | rmse_h10 | persistence | 0.600 [0.526, 0.679] | p=5.6e-09 (vs last_slope) |  | 43 | 1 | 85a8557f |
| test1 | all | overall | rmse_h100 | last_slope | 2.913 [2.388, 3.474] |  |  | 43 | 1 | 77403933 |
| test1 | all | overall | rmse_h100 | persistence | 4.332 [3.771, 4.975] | p=3.31e-06 (vs last_slope) |  | 43 | 1 | 85a8557f |
| test1 | all | overall | rmse_h200 | last_slope | 6.232 [5.167, 7.395] |  |  | 42 | 1 | 77403933 |
| test1 | all | overall | rmse_h200 | persistence | 6.443 [5.818, 7.082] | p=0.0225 (vs last_slope) |  | 42 | 1 | 85a8557f |
| test1 | all | overall | rmse_h50 | last_slope | 1.202 [0.954, 1.480] |  |  | 43 | 1 | 77403933 |
| test1 | all | overall | rmse_h50 | persistence | 2.502 [2.179, 2.849] | p=2.87e-08 (vs last_slope) |  | 43 | 1 | 85a8557f |
| test1 | start_points | fixed:100 | rmse_h1 | last_slope | 0.010 [0.006, 0.015] |  |  | 43 | 1 | 77403933 |
| test1 | start_points | fixed:100 | rmse_h1 | persistence | 0.012 [0.008, 0.017] | p=0.227 (vs last_slope) |  | 43 | 1 | 85a8557f |
| test1 | start_points | fixed:100 | rmse_h10 | last_slope | 0.024 [0.015, 0.035] |  |  | 43 | 1 | 77403933 |
| test1 | start_points | fixed:100 | rmse_h10 | persistence | 0.103 [0.054, 0.182] | p=7.17e-09 (vs last_slope) |  | 43 | 1 | 85a8557f |
| test1 | start_points | fixed:100 | rmse_h100 | last_slope | 0.250 [0.172, 0.347] |  |  | 42 | 1 | 77403933 |
| test1 | start_points | fixed:100 | rmse_h100 | persistence | 0.867 [0.644, 1.149] | p=9.41e-11 (vs last_slope) |  | 42 | 1 | 85a8557f |
| test1 | start_points | fixed:100 | rmse_h200 | last_slope | 0.913 [0.687, 1.195] |  |  | 42 | 1 | 77403933 |
| test1 | start_points | fixed:100 | rmse_h200 | persistence | 2.152 [1.644, 2.794] | p=7.69e-11 (vs last_slope) |  | 42 | 1 | 85a8557f |
| test1 | start_points | fixed:100 | rmse_h50 | last_slope | 0.135 [0.065, 0.248] |  |  | 43 | 1 | 77403933 |
| test1 | start_points | fixed:100 | rmse_h50 | persistence | 0.576 [0.302, 1.024] | p=5.75e-11 (vs last_slope) |  | 43 | 1 | 85a8557f |
| test1 | start_points | frac:0.3 | rmse_h1 | last_slope | 0.023 [0.014, 0.036] | p=0.305 (vs persistence) |  | 43 | 1 | 77403933 |
| test1 | start_points | frac:0.3 | rmse_h1 | persistence | 0.021 [0.014, 0.031] |  |  | 43 | 1 | 85a8557f |
| test1 | start_points | frac:0.3 | rmse_h10 | last_slope | 0.126 [0.044, 0.263] |  |  | 43 | 1 | 77403933 |
| test1 | start_points | frac:0.3 | rmse_h10 | persistence | 0.139 [0.092, 0.204] | p=0.00266 (vs last_slope) |  | 43 | 1 | 85a8557f |
| test1 | start_points | frac:0.3 | rmse_h100 | last_slope | 1.226 [0.486, 2.447] |  |  | 43 | 1 | 77403933 |
| test1 | start_points | frac:0.3 | rmse_h100 | persistence | 1.432 [0.942, 2.189] | p=5.61e-05 (vs last_slope) |  | 43 | 1 | 85a8557f |
| test1 | start_points | frac:0.3 | rmse_h200 | last_slope | 2.764 [1.374, 5.062] |  |  | 42 | 1 | 77403933 |
| test1 | start_points | frac:0.3 | rmse_h200 | persistence | 2.821 [2.267, 3.472] | p=2.56e-05 (vs last_slope) |  | 42 | 1 | 85a8557f |
| test1 | start_points | frac:0.3 | rmse_h50 | last_slope | 0.518 [0.188, 1.077] |  |  | 43 | 1 | 77403933 |
| test1 | start_points | frac:0.3 | rmse_h50 | persistence | 0.614 [0.405, 0.926] | p=8.1e-05 (vs last_slope) |  | 43 | 1 | 85a8557f |
| test1 | start_points | frac:0.5 | rmse_h1 | last_slope | 0.053 [0.024, 0.091] | p=0.689 (vs persistence) |  | 43 | 1 | 77403933 |
| test1 | start_points | frac:0.5 | rmse_h1 | persistence | 0.033 [0.021, 0.051] |  |  | 43 | 1 | 85a8557f |
| test1 | start_points | frac:0.5 | rmse_h10 | last_slope | 0.312 [0.081, 0.659] | p=0.0947 (vs persistence) |  | 43 | 1 | 77403933 |
| test1 | start_points | frac:0.5 | rmse_h10 | persistence | 0.160 [0.111, 0.230] |  |  | 43 | 1 | 85a8557f |
| test1 | start_points | frac:0.5 | rmse_h100 | last_slope | 2.997 [0.668, 6.602] | p=0.00076 (vs persistence) |  | 42 | 1 | 77403933 |
| test1 | start_points | frac:0.5 | rmse_h100 | persistence | 1.779 [1.495, 2.097] |  |  | 42 | 1 | 85a8557f |
| test1 | start_points | frac:0.5 | rmse_h200 | last_slope | 8.282 [3.534, 15.660] | p=0.000168 (vs persistence) |  | 41 | 1 | 77403933 |
| test1 | start_points | frac:0.5 | rmse_h200 | persistence | 6.269 [5.184, 7.368] |  |  | 41 | 1 | 85a8557f |
| test1 | start_points | frac:0.5 | rmse_h50 | last_slope | 1.439 [0.291, 3.185] | p=0.00141 (vs persistence) |  | 43 | 1 | 77403933 |
| test1 | start_points | frac:0.5 | rmse_h50 | persistence | 0.851 [0.603, 1.223] |  |  | 43 | 1 | 85a8557f |
| test1 | start_points | frac:0.7 | rmse_h1 | last_slope | 0.056 [0.032, 0.088] |  |  | 43 | 1 | 77403933 |
| test1 | start_points | frac:0.7 | rmse_h1 | persistence | 0.062 [0.039, 0.092] | p=0.081 (vs last_slope) |  | 43 | 1 | 85a8557f |
| test1 | start_points | frac:0.7 | rmse_h10 | last_slope | 0.120 [0.048, 0.236] |  |  | 43 | 1 | 77403933 |
| test1 | start_points | frac:0.7 | rmse_h10 | persistence | 0.366 [0.291, 0.461] | p=5.45e-08 (vs last_slope) |  | 43 | 1 | 85a8557f |
| test1 | start_points | frac:0.7 | rmse_h100 | last_slope | 2.597 [2.022, 3.244] |  |  | 42 | 1 | 77403933 |
| test1 | start_points | frac:0.7 | rmse_h100 | persistence | 5.192 [4.513, 5.866] | p=3.95e-09 (vs last_slope) |  | 42 | 1 | 85a8557f |
| test1 | start_points | frac:0.7 | rmse_h200 | last_slope | 4.960 [3.958, 5.901] |  |  | 17 | 1 | 77403933 |
| test1 | start_points | frac:0.7 | rmse_h200 | persistence | 8.965 [7.231, 10.660] | p=1.53e-05 (vs last_slope) |  | 17 | 1 | 85a8557f |
| test1 | start_points | frac:0.7 | rmse_h50 | last_slope | 0.580 [0.410, 0.828] |  |  | 43 | 1 | 77403933 |
| test1 | start_points | frac:0.7 | rmse_h50 | persistence | 1.975 [1.653, 2.398] | p=1.98e-09 (vs last_slope) |  | 43 | 1 | 85a8557f |
| test1 | start_points | overall | rmse_h1 | last_slope | 0.052 [0.033, 0.074] | p=0.0854 (vs persistence) |  | 43 | 1 | 77403933 |
| test1 | start_points | overall | rmse_h1 | persistence | 0.045 [0.032, 0.061] |  |  | 43 | 1 | 85a8557f |
| test1 | start_points | overall | rmse_h10 | last_slope | 0.239 [0.099, 0.422] | p=0.00277 (vs persistence) |  | 43 | 1 | 77403933 |
| test1 | start_points | overall | rmse_h10 | persistence | 0.234 [0.180, 0.307] |  |  | 43 | 1 | 85a8557f |
| test1 | start_points | overall | rmse_h100 | last_slope | 2.867 [1.586, 4.633] |  |  | 43 | 1 | 77403933 |
| test1 | start_points | overall | rmse_h100 | persistence | 3.154 [2.605, 3.867] | p=9.13e-05 (vs last_slope) |  | 43 | 1 | 85a8557f |
| test1 | start_points | overall | rmse_h200 | last_slope | 6.252 [3.418, 10.551] | p=0.000342 (vs persistence) |  | 42 | 1 | 77403933 |
| test1 | start_points | overall | rmse_h200 | persistence | 5.459 [4.855, 6.081] |  |  | 42 | 1 | 85a8557f |
| test1 | start_points | overall | rmse_h50 | last_slope | 1.101 [0.460, 1.991] |  |  | 43 | 1 | 77403933 |
| test1 | start_points | overall | rmse_h50 | persistence | 1.197 [0.940, 1.577] | p=0.000391 (vs last_slope) |  | 43 | 1 | 85a8557f |
| test2 | all | overall | rmse_h1 | last_slope | 0.016 [0.014, 0.019] |  |  | 40 | 1 | 77403933 |
| test2 | all | overall | rmse_h1 | persistence | 0.036 [0.034, 0.038] | p=1.82e-12 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | all | overall | rmse_h10 | last_slope | 0.057 [0.051, 0.063] |  |  | 40 | 1 | 77403933 |
| test2 | all | overall | rmse_h10 | persistence | 0.303 [0.281, 0.324] | p=1.82e-12 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | all | overall | rmse_h100 | last_slope | 1.032 [0.933, 1.129] |  |  | 40 | 1 | 77403933 |
| test2 | all | overall | rmse_h100 | persistence | 2.349 [2.216, 2.473] | p=1.82e-12 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | all | overall | rmse_h200 | last_slope | 2.322 [2.142, 2.486] |  |  | 40 | 1 | 77403933 |
| test2 | all | overall | rmse_h200 | persistence | 3.713 [3.519, 3.907] | p=1.82e-12 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | all | overall | rmse_h50 | last_slope | 0.397 [0.360, 0.434] |  |  | 40 | 1 | 77403933 |
| test2 | all | overall | rmse_h50 | persistence | 1.354 [1.265, 1.437] | p=1.82e-12 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | start_points | fixed:100 | rmse_h1 | last_slope | 0.010 [0.004, 0.018] |  |  | 40 | 1 | 77403933 |
| test2 | start_points | fixed:100 | rmse_h1 | persistence | 0.011 [0.005, 0.018] | p=0.765 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | start_points | fixed:100 | rmse_h10 | last_slope | 0.034 [0.023, 0.049] |  |  | 40 | 1 | 77403933 |
| test2 | start_points | fixed:100 | rmse_h10 | persistence | 0.045 [0.030, 0.063] | p=0.563 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | start_points | fixed:100 | rmse_h100 | last_slope | 0.204 [0.152, 0.263] |  |  | 40 | 1 | 77403933 |
| test2 | start_points | fixed:100 | rmse_h100 | persistence | 0.440 [0.325, 0.591] | p=4.4e-05 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | start_points | fixed:100 | rmse_h200 | last_slope | 0.386 [0.289, 0.493] |  |  | 40 | 1 | 77403933 |
| test2 | start_points | fixed:100 | rmse_h200 | persistence | 0.961 [0.738, 1.252] | p=2.67e-06 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | start_points | fixed:100 | rmse_h50 | last_slope | 0.121 [0.090, 0.156] |  |  | 40 | 1 | 77403933 |
| test2 | start_points | fixed:100 | rmse_h50 | persistence | 0.194 [0.134, 0.273] | p=0.0208 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | start_points | frac:0.3 | rmse_h1 | last_slope | 0.015 [0.007, 0.026] |  |  | 40 | 1 | 77403933 |
| test2 | start_points | frac:0.3 | rmse_h1 | persistence | 0.017 [0.008, 0.028] | p=0.0422 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | start_points | frac:0.3 | rmse_h10 | last_slope | 0.018 [0.013, 0.025] |  |  | 40 | 1 | 77403933 |
| test2 | start_points | frac:0.3 | rmse_h10 | persistence | 0.060 [0.048, 0.076] | p=1.04e-08 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | start_points | frac:0.3 | rmse_h100 | last_slope | 0.131 [0.099, 0.168] |  |  | 40 | 1 | 77403933 |
| test2 | start_points | frac:0.3 | rmse_h100 | persistence | 0.577 [0.477, 0.707] | p=4.55e-11 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | start_points | frac:0.3 | rmse_h200 | last_slope | 0.317 [0.240, 0.404] |  |  | 40 | 1 | 77403933 |
| test2 | start_points | frac:0.3 | rmse_h200 | persistence | 1.260 [1.051, 1.532] | p=3.46e-11 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | start_points | frac:0.3 | rmse_h50 | last_slope | 0.074 [0.053, 0.101] |  |  | 40 | 1 | 77403933 |
| test2 | start_points | frac:0.3 | rmse_h50 | persistence | 0.295 [0.240, 0.364] | p=6e-11 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | start_points | frac:0.5 | rmse_h1 | last_slope | 0.010 [0.005, 0.017] |  |  | 40 | 1 | 77403933 |
| test2 | start_points | frac:0.5 | rmse_h1 | persistence | 0.013 [0.009, 0.020] | p=0.00336 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | start_points | frac:0.5 | rmse_h10 | last_slope | 0.029 [0.020, 0.041] |  |  | 40 | 1 | 77403933 |
| test2 | start_points | frac:0.5 | rmse_h10 | persistence | 0.075 [0.063, 0.088] | p=1.06e-06 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | start_points | frac:0.5 | rmse_h100 | last_slope | 0.241 [0.176, 0.313] |  |  | 40 | 1 | 77403933 |
| test2 | start_points | frac:0.5 | rmse_h100 | persistence | 0.823 [0.706, 0.967] | p=6.75e-10 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | start_points | frac:0.5 | rmse_h200 | last_slope | 0.734 [0.559, 0.923] |  |  | 40 | 1 | 77403933 |
| test2 | start_points | frac:0.5 | rmse_h200 | persistence | 2.027 [1.721, 2.393] | p=2.49e-10 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | start_points | frac:0.5 | rmse_h50 | last_slope | 0.105 [0.072, 0.145] |  |  | 40 | 1 | 77403933 |
| test2 | start_points | frac:0.5 | rmse_h50 | persistence | 0.377 [0.325, 0.443] | p=7.84e-09 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | start_points | frac:0.7 | rmse_h1 | last_slope | 0.008 [0.004, 0.014] |  |  | 40 | 1 | 77403933 |
| test2 | start_points | frac:0.7 | rmse_h1 | persistence | 0.017 [0.013, 0.024] | p=7.84e-09 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | start_points | frac:0.7 | rmse_h10 | last_slope | 0.016 [0.012, 0.021] |  |  | 40 | 1 | 77403933 |
| test2 | start_points | frac:0.7 | rmse_h10 | persistence | 0.137 [0.120, 0.157] | p=1.82e-12 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | start_points | frac:0.7 | rmse_h100 | last_slope | 0.552 [0.465, 0.645] |  |  | 40 | 1 | 77403933 |
| test2 | start_points | frac:0.7 | rmse_h100 | persistence | 1.851 [1.624, 2.088] | p=1.82e-12 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | start_points | frac:0.7 | rmse_h200 | last_slope | 3.641 [3.098, 4.238] |  |  | 38 | 1 | 77403933 |
| test2 | start_points | frac:0.7 | rmse_h200 | persistence | 6.059 [5.290, 6.846] | p=7.28e-12 (vs last_slope) |  | 38 | 1 | 85a8557f |
| test2 | start_points | frac:0.7 | rmse_h50 | last_slope | 0.125 [0.099, 0.155] |  |  | 40 | 1 | 77403933 |
| test2 | start_points | frac:0.7 | rmse_h50 | persistence | 0.771 [0.675, 0.874] | p=1.82e-12 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | start_points | overall | rmse_h1 | last_slope | 0.014 [0.008, 0.022] |  |  | 40 | 1 | 77403933 |
| test2 | start_points | overall | rmse_h1 | persistence | 0.018 [0.012, 0.025] | p=4.15e-06 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | start_points | overall | rmse_h10 | last_slope | 0.032 [0.025, 0.040] |  |  | 40 | 1 | 77403933 |
| test2 | start_points | overall | rmse_h10 | persistence | 0.090 [0.078, 0.105] | p=2e-10 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | start_points | overall | rmse_h100 | last_slope | 0.364 [0.324, 0.407] |  |  | 40 | 1 | 77403933 |
| test2 | start_points | overall | rmse_h100 | persistence | 1.088 [0.945, 1.248] | p=3.64e-12 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | start_points | overall | rmse_h200 | last_slope | 1.874 [1.616, 2.152] |  |  | 40 | 1 | 77403933 |
| test2 | start_points | overall | rmse_h200 | persistence | 3.330 [2.943, 3.720] | p=1.82e-12 (vs last_slope) |  | 40 | 1 | 85a8557f |
| test2 | start_points | overall | rmse_h50 | last_slope | 0.133 [0.113, 0.154] |  |  | 40 | 1 | 77403933 |
| test2 | start_points | overall | rmse_h50 | persistence | 0.472 [0.408, 0.547] | p=9.09e-12 (vs last_slope) |  | 40 | 1 | 85a8557f |

</details>
