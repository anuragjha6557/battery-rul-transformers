# Benchmark tables: abl_curve

- Protocol version: 1.1
- Git SHA: fa6ae83c62
- Seeds: 5  |  unit runs: 180
- Note: n = 4 cells per NASA/CALCE dataset, so the 95 % cluster-bootstrap CI is wide by construction. Toyota rows are over test cells (test1 / test2 separately) with a cell-level bootstrap CI and a Holm-adjusted Wilcoxon p vs the best baseline. All metrics are computed per cell from the logged predictions.

## Headline (kind = overall; RMSE in %SOH, RUL MAE in cycles)

### calce_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | itransformer | 1.966 [1.857, 2.076] |  |  | 4 | 5 | 52ab36d1 |
| loco | all | overall | rmse_h1 | lgbm | 1.968 [1.848, 2.088] |  |  | 4 | 5 | abe86ed7 |
| loco | all | overall | rmse_h10 | itransformer | 2.313 [2.225, 2.411] |  |  | 4 | 5 | 52ab36d1 |
| loco | all | overall | rmse_h10 | lgbm | 2.306 [2.228, 2.392] |  |  | 4 | 5 | abe86ed7 |
| loco | all | overall | rmse_h50 | itransformer | 3.080 [2.851, 3.309] |  |  | 4 | 5 | 52ab36d1 |
| loco | all | overall | rmse_h50 | lgbm | 2.859 [2.561, 3.250] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | overall | rmse_h1 | itransformer | 0.393 [0.199, 0.587] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | overall | rmse_h1 | lgbm | 0.359 [0.170, 0.547] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | overall | rmse_h10 | itransformer | 1.070 [0.721, 1.573] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | overall | rmse_h10 | lgbm | 0.960 [0.437, 1.659] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | overall | rmse_h50 | itransformer | 1.414 [0.948, 1.913] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | overall | rmse_h50 | lgbm | 1.568 [1.116, 2.052] |  |  | 4 | 5 | abe86ed7 |

### calce_soh

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse | itransformer | 1.252 [1.209, 1.294] |  |  | 4 | 5 | 76ee1042 |
| loco | all | overall | rmse | lgbm | 1.211 [1.126, 1.329] |  |  | 4 | 5 | f0a024d7 |
| loco | start_points | overall | rmse | itransformer | 0.215 [0.126, 0.304] |  |  | 4 | 5 | 76ee1042 |
| loco | start_points | overall | rmse | lgbm | 0.247 [0.165, 0.356] |  |  | 4 | 5 | f0a024d7 |

### nasa_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | itransformer | 0.913 [0.655, 1.170] |  | 1.217 | 4 | 5 | a6205340 |
| loco | all | overall | rmse_h1 | lgbm | 0.943 [0.709, 1.177] |  | 1.210 | 4 | 5 | 7fcf66d7 |
| loco | all | overall | rmse_h10 | itransformer | 1.743 [1.097, 2.390] |  | 2.594 | 4 | 5 | a6205340 |
| loco | all | overall | rmse_h10 | lgbm | 1.825 [1.341, 2.309] |  | 2.313 | 4 | 5 | 7fcf66d7 |
| loco | all | overall | rmse_h50 | itransformer | 5.411 [5.175, 5.648] |  | 5.247 | 4 | 5 | a6205340 |
| loco | all | overall | rmse_h50 | lgbm | 3.332 [2.614, 4.233] |  | 2.916 | 4 | 5 | 7fcf66d7 |
| loco | start_points | overall | rmse_h1 | itransformer | 1.822 [1.084, 2.560] |  | 2.582 | 4 | 5 | a6205340 |
| loco | start_points | overall | rmse_h1 | lgbm | 1.844 [1.189, 2.499] |  | 2.515 | 4 | 5 | 7fcf66d7 |
| loco | start_points | overall | rmse_h10 | itransformer | 1.901 [1.108, 3.001] |  | 3.613 | 4 | 5 | a6205340 |
| loco | start_points | overall | rmse_h10 | lgbm | 1.941 [1.117, 2.765] |  | 2.787 | 4 | 5 | 7fcf66d7 |
| loco | start_points | overall | rmse_h50 | itransformer | 5.791 [4.231, 7.460] |  | 3.540 | 4 | 5 | a6205340 |
| loco | start_points | overall | rmse_h50 | lgbm | 3.538 [2.671, 5.053] |  | 2.871 | 4 | 5 | 7fcf66d7 |

### nasa_soh

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse | itransformer | 0.749 [0.573, 0.925] |  | 0.959 | 4 | 5 | 82f13006 |
| loco | all | overall | rmse | lgbm | 0.926 [0.694, 1.157] |  | 1.180 | 4 | 5 | 94651b36 |
| loco | start_points | overall | rmse | itransformer | 0.291 [0.156, 0.459] |  | 0.308 | 4 | 5 | 82f13006 |
| loco | start_points | overall | rmse | lgbm | 0.472 [0.298, 0.738] |  | 0.324 | 4 | 5 | 94651b36 |

### toyota_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rmse_h1 | itransformer | 0.124 [0.073, 0.183] |  |  | 43 | 5 | 4e5853ab |
| test1 | all | overall | rmse_h1 | lgbm | 0.135 [0.081, 0.198] |  |  | 43 | 5 | 8cc031eb |
| test1 | all | overall | rmse_h10 | itransformer | 0.156 [0.105, 0.216] |  |  | 43 | 5 | 4e5853ab |
| test1 | all | overall | rmse_h10 | lgbm | 0.178 [0.122, 0.243] |  |  | 43 | 5 | 8cc031eb |
| test1 | all | overall | rmse_h50 | itransformer | 0.389 [0.303, 0.503] |  |  | 43 | 5 | 4e5853ab |
| test1 | all | overall | rmse_h50 | lgbm | 0.419 [0.318, 0.550] |  |  | 43 | 5 | 8cc031eb |
| test1 | start_points | overall | rmse_h1 | itransformer | 0.040 [0.026, 0.057] |  |  | 43 | 5 | 4e5853ab |
| test1 | start_points | overall | rmse_h1 | lgbm | 0.039 [0.026, 0.055] |  |  | 43 | 5 | 8cc031eb |
| test1 | start_points | overall | rmse_h10 | itransformer | 0.083 [0.049, 0.128] |  |  | 43 | 5 | 4e5853ab |
| test1 | start_points | overall | rmse_h10 | lgbm | 0.093 [0.058, 0.136] |  |  | 43 | 5 | 8cc031eb |
| test1 | start_points | overall | rmse_h50 | itransformer | 0.252 [0.151, 0.379] |  |  | 43 | 5 | 4e5853ab |
| test1 | start_points | overall | rmse_h50 | lgbm | 0.274 [0.169, 0.423] |  |  | 43 | 5 | 8cc031eb |
| test2 | all | overall | rmse_h1 | itransformer | 0.015 [0.013, 0.018] |  |  | 40 | 5 | 4e5853ab |
| test2 | all | overall | rmse_h1 | lgbm | 0.019 [0.017, 0.021] |  |  | 40 | 5 | 8cc031eb |
| test2 | all | overall | rmse_h10 | itransformer | 0.035 [0.032, 0.040] |  |  | 40 | 5 | 4e5853ab |
| test2 | all | overall | rmse_h10 | lgbm | 0.059 [0.054, 0.065] |  |  | 40 | 5 | 8cc031eb |
| test2 | all | overall | rmse_h50 | itransformer | 0.226 [0.196, 0.256] |  |  | 40 | 5 | 4e5853ab |
| test2 | all | overall | rmse_h50 | lgbm | 0.281 [0.257, 0.305] |  |  | 40 | 5 | 8cc031eb |
| test2 | start_points | overall | rmse_h1 | itransformer | 0.013 [0.007, 0.019] |  |  | 40 | 5 | 4e5853ab |
| test2 | start_points | overall | rmse_h1 | lgbm | 0.017 [0.011, 0.024] |  |  | 40 | 5 | 8cc031eb |
| test2 | start_points | overall | rmse_h10 | itransformer | 0.021 [0.016, 0.026] |  |  | 40 | 5 | 4e5853ab |
| test2 | start_points | overall | rmse_h10 | lgbm | 0.055 [0.049, 0.063] |  |  | 40 | 5 | 8cc031eb |
| test2 | start_points | overall | rmse_h50 | itransformer | 0.079 [0.067, 0.093] |  |  | 40 | 5 | 4e5853ab |
| test2 | start_points | overall | rmse_h50 | lgbm | 0.221 [0.201, 0.240] |  |  | 40 | 5 | 8cc031eb |

### toyota_soh

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rmse | itransformer | 0.111 [0.067, 0.163] |  |  | 43 | 5 | 2dc7d291 |
| test1 | all | overall | rmse | lgbm | 0.133 [0.079, 0.196] |  |  | 43 | 5 | 627b7c23 |
| test1 | start_points | overall | rmse | itransformer | 0.029 [0.021, 0.039] |  |  | 43 | 5 | 2dc7d291 |
| test1 | start_points | overall | rmse | lgbm | 0.031 [0.020, 0.047] |  |  | 43 | 5 | 627b7c23 |
| test2 | all | overall | rmse | itransformer | 0.025 [0.023, 0.027] |  |  | 40 | 5 | 2dc7d291 |
| test2 | all | overall | rmse | lgbm | 0.020 [0.018, 0.023] |  |  | 40 | 5 | 627b7c23 |
| test2 | start_points | overall | rmse | itransformer | 0.027 [0.024, 0.031] |  |  | 40 | 5 | 2dc7d291 |
| test2 | start_points | overall | rmse | lgbm | 0.019 [0.013, 0.025] |  |  | 40 | 5 | 627b7c23 |

## Mean rank (dataset x task x split x policy x headline metric)

| model | mean rank | conditions | missing |
|---|---|---|---|
| itransformer | 1.31 | 32 | 0 |
| lgbm | 1.69 | 32 | 0 |

## Full tables

<details><summary>calce_forecast (70 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | itransformer | 1.966 [1.857, 2.076] |  |  | 4 | 5 | 52ab36d1 |
| loco | all | overall | rmse_h1 | lgbm | 1.968 [1.848, 2.088] |  |  | 4 | 5 | abe86ed7 |
| loco | all | overall | rmse_h10 | itransformer | 2.313 [2.225, 2.411] |  |  | 4 | 5 | 52ab36d1 |
| loco | all | overall | rmse_h10 | lgbm | 2.306 [2.228, 2.392] |  |  | 4 | 5 | abe86ed7 |
| loco | all | overall | rmse_h100 | itransformer | 3.820 [3.342, 4.297] |  |  | 4 | 5 | 52ab36d1 |
| loco | all | overall | rmse_h100 | lgbm | 3.502 [3.048, 4.069] |  |  | 4 | 5 | abe86ed7 |
| loco | all | overall | rmse_h25 | itransformer | 2.707 [2.528, 2.886] |  |  | 4 | 5 | 52ab36d1 |
| loco | all | overall | rmse_h25 | lgbm | 2.631 [2.496, 2.849] |  |  | 4 | 5 | abe86ed7 |
| loco | all | overall | rmse_h50 | itransformer | 3.080 [2.851, 3.309] |  |  | 4 | 5 | 52ab36d1 |
| loco | all | overall | rmse_h50 | lgbm | 2.859 [2.561, 3.250] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | fixed:200 | rmse_h1 | itransformer | 0.307 [0.209, 0.405] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | fixed:200 | rmse_h1 | lgbm | 0.281 [0.217, 0.382] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | fixed:200 | rmse_h10 | itransformer | 1.144 [0.171, 2.865] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | fixed:200 | rmse_h10 | lgbm | 1.377 [0.379, 3.241] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | fixed:200 | rmse_h100 | itransformer | 0.626 [0.359, 0.892] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | fixed:200 | rmse_h100 | lgbm | 1.071 [0.448, 1.879] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | fixed:200 | rmse_h25 | itransformer | 1.330 [0.856, 1.804] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | fixed:200 | rmse_h25 | lgbm | 1.772 [1.310, 2.179] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | fixed:200 | rmse_h50 | itransformer | 0.951 [0.622, 1.280] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | fixed:200 | rmse_h50 | lgbm | 1.682 [0.873, 2.437] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | fixed:400 | rmse_h1 | itransformer | 0.156 [0.058, 0.255] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | fixed:400 | rmse_h1 | lgbm | 0.090 [0.021, 0.181] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | fixed:400 | rmse_h10 | itransformer | 0.793 [0.514, 1.072] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | fixed:400 | rmse_h10 | lgbm | 0.665 [0.464, 0.867] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | fixed:400 | rmse_h100 | itransformer | 2.200 [0.715, 3.317] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | fixed:400 | rmse_h100 | lgbm | 2.689 [1.935, 4.014] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | fixed:400 | rmse_h25 | itransformer | 1.132 [0.654, 1.607] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | fixed:400 | rmse_h25 | lgbm | 0.964 [0.251, 1.884] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | fixed:400 | rmse_h50 | itransformer | 0.982 [0.381, 1.795] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | fixed:400 | rmse_h50 | lgbm | 0.899 [0.208, 1.723] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer | 0.401 [0.167, 0.848] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | frac:0.3 | rmse_h1 | lgbm | 0.363 [0.134, 0.771] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer | 0.736 [0.358, 0.971] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | frac:0.3 | rmse_h10 | lgbm | 0.690 [0.123, 1.258] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer | 1.260 [0.451, 2.172] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | frac:0.3 | rmse_h100 | lgbm | 2.115 [1.628, 2.603] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer | 0.557 [0.222, 1.003] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | frac:0.3 | rmse_h25 | lgbm | 0.689 [0.191, 1.252] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer | 1.953 [0.752, 3.564] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | frac:0.3 | rmse_h50 | lgbm | 2.252 [1.319, 3.839] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer | 0.478 [0.068, 0.984] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | frac:0.5 | rmse_h1 | lgbm | 0.450 [0.027, 0.918] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer | 0.976 [0.402, 1.412] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | frac:0.5 | rmse_h10 | lgbm | 0.627 [0.282, 1.053] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer | 1.033 [0.439, 1.930] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | frac:0.5 | rmse_h100 | lgbm | 1.216 [0.735, 1.696] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer | 0.988 [0.465, 1.398] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | frac:0.5 | rmse_h25 | lgbm | 0.754 [0.374, 1.135] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer | 0.633 [0.203, 1.233] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | frac:0.5 | rmse_h50 | lgbm | 0.498 [0.272, 0.724] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer | 0.141 [0.042, 0.240] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | frac:0.7 | rmse_h1 | lgbm | 0.129 [0.019, 0.250] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer | 0.554 [0.143, 1.249] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | frac:0.7 | rmse_h10 | lgbm | 0.355 [0.024, 1.005] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer | 2.209 [1.130, 3.287] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | frac:0.7 | rmse_h100 | lgbm | 2.038 [0.964, 3.112] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer | 0.944 [0.509, 1.378] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | frac:0.7 | rmse_h25 | lgbm | 0.742 [0.348, 1.111] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer | 1.224 [1.030, 1.467] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | frac:0.7 | rmse_h50 | lgbm | 0.968 [0.574, 1.399] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | overall | rmse_h1 | itransformer | 0.393 [0.199, 0.587] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | overall | rmse_h1 | lgbm | 0.359 [0.170, 0.547] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | overall | rmse_h10 | itransformer | 1.070 [0.721, 1.573] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | overall | rmse_h10 | lgbm | 0.960 [0.437, 1.659] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | overall | rmse_h100 | itransformer | 1.748 [0.957, 2.417] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | overall | rmse_h100 | lgbm | 2.022 [1.444, 2.609] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | overall | rmse_h25 | itransformer | 1.096 [0.821, 1.400] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | overall | rmse_h25 | lgbm | 1.136 [0.881, 1.539] |  |  | 4 | 5 | abe86ed7 |
| loco | start_points | overall | rmse_h50 | itransformer | 1.414 [0.948, 1.913] |  |  | 4 | 5 | 52ab36d1 |
| loco | start_points | overall | rmse_h50 | lgbm | 1.568 [1.116, 2.052] |  |  | 4 | 5 | abe86ed7 |

</details>

<details><summary>calce_soh (14 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse | itransformer | 1.252 [1.209, 1.294] |  |  | 4 | 5 | 76ee1042 |
| loco | all | overall | rmse | lgbm | 1.211 [1.126, 1.329] |  |  | 4 | 5 | f0a024d7 |
| loco | start_points | fixed:200 | rmse | itransformer | 0.282 [0.145, 0.439] |  |  | 4 | 5 | 76ee1042 |
| loco | start_points | fixed:200 | rmse | lgbm | 0.299 [0.055, 0.590] |  |  | 4 | 5 | f0a024d7 |
| loco | start_points | fixed:400 | rmse | itransformer | 0.100 [0.042, 0.185] |  |  | 4 | 5 | 76ee1042 |
| loco | start_points | fixed:400 | rmse | lgbm | 0.116 [0.051, 0.197] |  |  | 4 | 5 | f0a024d7 |
| loco | start_points | frac:0.3 | rmse | itransformer | 0.199 [0.050, 0.470] |  |  | 4 | 5 | 76ee1042 |
| loco | start_points | frac:0.3 | rmse | lgbm | 0.340 [0.255, 0.433] |  |  | 4 | 5 | f0a024d7 |
| loco | start_points | frac:0.5 | rmse | itransformer | 0.154 [0.023, 0.303] |  |  | 4 | 5 | 76ee1042 |
| loco | start_points | frac:0.5 | rmse | lgbm | 0.111 [0.050, 0.158] |  |  | 4 | 5 | f0a024d7 |
| loco | start_points | frac:0.7 | rmse | itransformer | 0.061 [0.021, 0.106] |  |  | 4 | 5 | 76ee1042 |
| loco | start_points | frac:0.7 | rmse | lgbm | 0.109 [0.040, 0.180] |  |  | 4 | 5 | f0a024d7 |
| loco | start_points | overall | rmse | itransformer | 0.215 [0.126, 0.304] |  |  | 4 | 5 | 76ee1042 |
| loco | start_points | overall | rmse | lgbm | 0.247 [0.165, 0.356] |  |  | 4 | 5 | f0a024d7 |

</details>

<details><summary>nasa_forecast (70 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | itransformer | 0.913 [0.655, 1.170] |  | 1.217 | 4 | 5 | a6205340 |
| loco | all | overall | rmse_h1 | lgbm | 0.943 [0.709, 1.177] |  | 1.210 | 4 | 5 | 7fcf66d7 |
| loco | all | overall | rmse_h10 | itransformer | 1.743 [1.097, 2.390] |  | 2.594 | 4 | 5 | a6205340 |
| loco | all | overall | rmse_h10 | lgbm | 1.825 [1.341, 2.309] |  | 2.313 | 4 | 5 | 7fcf66d7 |
| loco | all | overall | rmse_h100 | itransformer | 14.210 [13.105, 15.710] |  | 12.937 | 4 | 5 | a6205340 |
| loco | all | overall | rmse_h100 | lgbm | 3.853 [2.239, 5.466] |  | 2.321 | 4 | 5 | 7fcf66d7 |
| loco | all | overall | rmse_h25 | itransformer | 2.621 [2.000, 3.271] |  | 3.695 | 4 | 5 | a6205340 |
| loco | all | overall | rmse_h25 | lgbm | 2.746 [2.103, 3.389] |  | 3.310 | 4 | 5 | 7fcf66d7 |
| loco | all | overall | rmse_h50 | itransformer | 5.411 [5.175, 5.648] |  | 5.247 | 4 | 5 | a6205340 |
| loco | all | overall | rmse_h50 | lgbm | 3.332 [2.614, 4.233] |  | 2.916 | 4 | 5 | 7fcf66d7 |
| loco | start_points | fixed:30 | rmse_h1 | itransformer | 2.221 [0.832, 3.452] |  | 0.178 | 4 | 5 | a6205340 |
| loco | start_points | fixed:30 | rmse_h1 | lgbm | 2.291 [0.840, 3.413] |  | 0.128 | 4 | 5 | 7fcf66d7 |
| loco | start_points | fixed:30 | rmse_h10 | itransformer | 1.118 [0.369, 2.170] |  | 2.765 | 4 | 5 | a6205340 |
| loco | start_points | fixed:30 | rmse_h10 | lgbm | 1.168 [0.210, 2.127] |  | 1.796 | 4 | 5 | 7fcf66d7 |
| loco | start_points | fixed:30 | rmse_h100 | itransformer | 13.207 [7.537, 17.838] |  | 4.648 | 4 | 5 | a6205340 |
| loco | start_points | fixed:30 | rmse_h100 | lgbm | 3.866 [2.474, 5.334] |  | 2.501 | 4 | 5 | 7fcf66d7 |
| loco | start_points | fixed:30 | rmse_h25 | itransformer | 2.024 [1.244, 2.804] |  | 2.842 | 4 | 5 | a6205340 |
| loco | start_points | fixed:30 | rmse_h25 | lgbm | 1.985 [0.686, 3.285] |  | 2.705 | 4 | 5 | 7fcf66d7 |
| loco | start_points | fixed:30 | rmse_h50 | itransformer | 6.989 [4.192, 9.488] |  | 2.457 | 4 | 5 | a6205340 |
| loco | start_points | fixed:30 | rmse_h50 | lgbm | 2.999 [0.911, 5.793] |  | 2.721 | 4 | 5 | 7fcf66d7 |
| loco | start_points | fixed:50 | rmse_h1 | itransformer | 0.478 [0.100, 0.855] |  | 1.100 | 4 | 5 | a6205340 |
| loco | start_points | fixed:50 | rmse_h1 | lgbm | 0.548 [0.088, 1.008] |  | 0.917 | 4 | 5 | 7fcf66d7 |
| loco | start_points | fixed:50 | rmse_h10 | itransformer | 1.021 [0.534, 1.408] |  | 0.322 | 4 | 5 | a6205340 |
| loco | start_points | fixed:50 | rmse_h10 | lgbm | 1.959 [0.678, 3.890] |  | 0.452 | 4 | 5 | 7fcf66d7 |
| loco | start_points | fixed:50 | rmse_h100 | itransformer | 11.843 [8.457, 15.897] |  |  | 3 | 5 | 0ea87117 |
| loco | start_points | fixed:50 | rmse_h100 | lgbm | 4.598 [3.617, 5.921] |  |  | 3 | 5 | 732ad356 |
| loco | start_points | fixed:50 | rmse_h25 | itransformer | 3.217 [2.252, 4.099] |  | 1.893 | 4 | 5 | a6205340 |
| loco | start_points | fixed:50 | rmse_h25 | lgbm | 4.430 [2.501, 7.126] |  | 2.170 | 4 | 5 | 7fcf66d7 |
| loco | start_points | fixed:50 | rmse_h50 | itransformer | 5.383 [2.950, 7.684] |  | 5.321 | 4 | 5 | a6205340 |
| loco | start_points | fixed:50 | rmse_h50 | lgbm | 4.028 [2.177, 5.449] |  | 4.623 | 4 | 5 | 7fcf66d7 |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer | 0.189 [0.083, 0.346] |  | 0.092 | 4 | 5 | a6205340 |
| loco | start_points | frac:0.3 | rmse_h1 | lgbm | 0.203 [0.139, 0.264] |  | 0.113 | 4 | 5 | 7fcf66d7 |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer | 1.626 [0.580, 2.797] |  | 0.343 | 4 | 5 | a6205340 |
| loco | start_points | frac:0.3 | rmse_h10 | lgbm | 1.165 [0.609, 1.647] |  | 0.385 | 4 | 5 | 7fcf66d7 |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer | 13.313 [7.497, 19.347] |  | 5.201 | 4 | 5 | a6205340 |
| loco | start_points | frac:0.3 | rmse_h100 | lgbm | 4.647 [4.161, 5.150] |  | 3.943 | 4 | 5 | 7fcf66d7 |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer | 3.575 [2.313, 4.902] |  | 5.405 | 4 | 5 | a6205340 |
| loco | start_points | frac:0.3 | rmse_h25 | lgbm | 2.154 [0.664, 4.500] |  | 5.645 | 4 | 5 | 7fcf66d7 |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer | 6.811 [3.584, 10.037] |  | 2.368 | 4 | 5 | a6205340 |
| loco | start_points | frac:0.3 | rmse_h50 | lgbm | 2.653 [1.086, 4.220] |  | 0.771 | 4 | 5 | 7fcf66d7 |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer | 2.085 [0.270, 3.900] |  | 3.852 | 4 | 5 | a6205340 |
| loco | start_points | frac:0.5 | rmse_h1 | lgbm | 2.027 [0.264, 3.790] |  | 3.784 | 4 | 5 | 7fcf66d7 |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer | 2.386 [0.394, 5.768] |  | 7.556 | 4 | 5 | a6205340 |
| loco | start_points | frac:0.5 | rmse_h10 | lgbm | 2.449 [0.800, 4.619] |  | 5.740 | 4 | 5 | 7fcf66d7 |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer | 10.487 [4.995, 13.963] |  |  | 3 | 5 | 0ea87117 |
| loco | start_points | frac:0.5 | rmse_h100 | lgbm | 4.872 [2.122, 6.279] |  |  | 3 | 5 | 732ad356 |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer | 2.087 [0.591, 3.583] |  | 4.196 | 4 | 5 | a6205340 |
| loco | start_points | frac:0.5 | rmse_h25 | lgbm | 2.341 [0.795, 3.520] |  | 2.935 | 4 | 5 | 7fcf66d7 |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer | 4.242 [1.694, 6.790] |  | 2.362 | 4 | 5 | a6205340 |
| loco | start_points | frac:0.5 | rmse_h50 | lgbm | 3.405 [1.123, 6.018] |  | 0.368 | 4 | 5 | 7fcf66d7 |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer | 1.305 [0.202, 3.186] |  | 4.151 | 4 | 5 | a6205340 |
| loco | start_points | frac:0.7 | rmse_h1 | lgbm | 1.322 [0.189, 3.106] |  | 4.055 | 4 | 5 | 7fcf66d7 |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer | 0.831 [0.455, 1.272] |  | 0.318 | 4 | 5 | a6205340 |
| loco | start_points | frac:0.7 | rmse_h10 | lgbm | 1.036 [0.584, 1.487] |  | 1.519 | 4 | 5 | 7fcf66d7 |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer | 12.150 |  |  | 1 | 5 | 14527e19 |
| loco | start_points | frac:0.7 | rmse_h100 | lgbm | 3.904 |  |  | 1 | 5 | 3f3504f5 |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer | 2.578 [1.085, 4.654] |  | 1.869 | 4 | 5 | a6205340 |
| loco | start_points | frac:0.7 | rmse_h25 | lgbm | 3.131 [1.585, 4.742] |  | 3.726 | 4 | 5 | 7fcf66d7 |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer | 2.670 [1.626, 3.681] |  | 4.036 | 4 | 5 | a6205340 |
| loco | start_points | frac:0.7 | rmse_h50 | lgbm | 2.859 [1.875, 3.843] |  | 3.422 | 4 | 5 | 7fcf66d7 |
| loco | start_points | overall | rmse_h1 | itransformer | 1.822 [1.084, 2.560] |  | 2.582 | 4 | 5 | a6205340 |
| loco | start_points | overall | rmse_h1 | lgbm | 1.844 [1.189, 2.499] |  | 2.515 | 4 | 5 | 7fcf66d7 |
| loco | start_points | overall | rmse_h10 | itransformer | 1.901 [1.108, 3.001] |  | 3.613 | 4 | 5 | a6205340 |
| loco | start_points | overall | rmse_h10 | lgbm | 1.941 [1.117, 2.765] |  | 2.787 | 4 | 5 | 7fcf66d7 |
| loco | start_points | overall | rmse_h100 | itransformer | 11.761 [6.812, 16.447] |  | 4.932 | 4 | 5 | a6205340 |
| loco | start_points | overall | rmse_h100 | lgbm | 4.291 [3.296, 5.286] |  | 3.302 | 4 | 5 | 7fcf66d7 |
| loco | start_points | overall | rmse_h25 | itransformer | 3.070 [2.764, 3.402] |  | 3.539 | 4 | 5 | a6205340 |
| loco | start_points | overall | rmse_h25 | lgbm | 3.200 [1.959, 4.513] |  | 3.644 | 4 | 5 | 7fcf66d7 |
| loco | start_points | overall | rmse_h50 | itransformer | 5.791 [4.231, 7.460] |  | 3.540 | 4 | 5 | a6205340 |
| loco | start_points | overall | rmse_h50 | lgbm | 3.538 [2.671, 5.053] |  | 2.871 | 4 | 5 | 7fcf66d7 |

</details>

<details><summary>nasa_soh (14 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse | itransformer | 0.749 [0.573, 0.925] |  | 0.959 | 4 | 5 | 82f13006 |
| loco | all | overall | rmse | lgbm | 0.926 [0.694, 1.157] |  | 1.180 | 4 | 5 | 94651b36 |
| loco | start_points | fixed:30 | rmse | itransformer | 0.192 [0.068, 0.428] |  | 0.085 | 4 | 5 | 82f13006 |
| loco | start_points | fixed:30 | rmse | lgbm | 0.335 [0.147, 0.559] |  | 0.084 | 4 | 5 | 94651b36 |
| loco | start_points | fixed:50 | rmse | itransformer | 0.168 [0.093, 0.281] |  | 0.341 | 4 | 5 | 82f13006 |
| loco | start_points | fixed:50 | rmse | lgbm | 0.678 [0.394, 1.137] |  | 0.540 | 4 | 5 | 94651b36 |
| loco | start_points | frac:0.3 | rmse | itransformer | 0.264 [0.221, 0.297] |  | 0.292 | 4 | 5 | 82f13006 |
| loco | start_points | frac:0.3 | rmse | lgbm | 0.418 [0.229, 0.621] |  | 0.472 | 4 | 5 | 94651b36 |
| loco | start_points | frac:0.5 | rmse | itransformer | 0.231 [0.068, 0.447] |  | 0.150 | 4 | 5 | 82f13006 |
| loco | start_points | frac:0.5 | rmse | lgbm | 0.242 [0.055, 0.519] |  | 0.007 | 4 | 5 | 94651b36 |
| loco | start_points | frac:0.7 | rmse | itransformer | 0.399 [0.143, 0.698] |  | 0.445 | 4 | 5 | 82f13006 |
| loco | start_points | frac:0.7 | rmse | lgbm | 0.376 [0.085, 0.784] |  | 0.051 | 4 | 5 | 94651b36 |
| loco | start_points | overall | rmse | itransformer | 0.291 [0.156, 0.459] |  | 0.308 | 4 | 5 | 82f13006 |
| loco | start_points | overall | rmse | lgbm | 0.472 [0.298, 0.738] |  | 0.324 | 4 | 5 | 94651b36 |

</details>

<details><summary>toyota_forecast (120 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rmse_h1 | itransformer | 0.124 [0.073, 0.183] |  |  | 43 | 5 | 4e5853ab |
| test1 | all | overall | rmse_h1 | lgbm | 0.135 [0.081, 0.198] |  |  | 43 | 5 | 8cc031eb |
| test1 | all | overall | rmse_h10 | itransformer | 0.156 [0.105, 0.216] |  |  | 43 | 5 | 4e5853ab |
| test1 | all | overall | rmse_h10 | lgbm | 0.178 [0.122, 0.243] |  |  | 43 | 5 | 8cc031eb |
| test1 | all | overall | rmse_h100 | itransformer | 0.892 [0.688, 1.182] |  |  | 43 | 5 | 4e5853ab |
| test1 | all | overall | rmse_h100 | lgbm | 0.880 [0.663, 1.215] |  |  | 43 | 5 | 8cc031eb |
| test1 | all | overall | rmse_h200 | itransformer | 2.389 [2.007, 2.780] |  |  | 42 | 5 | 4e5853ab |
| test1 | all | overall | rmse_h200 | lgbm | 1.699 [1.458, 1.958] |  |  | 42 | 5 | 8cc031eb |
| test1 | all | overall | rmse_h50 | itransformer | 0.389 [0.303, 0.503] |  |  | 43 | 5 | 4e5853ab |
| test1 | all | overall | rmse_h50 | lgbm | 0.419 [0.318, 0.550] |  |  | 43 | 5 | 8cc031eb |
| test1 | start_points | fixed:100 | rmse_h1 | itransformer | 0.010 [0.006, 0.014] |  |  | 43 | 5 | 4e5853ab |
| test1 | start_points | fixed:100 | rmse_h1 | lgbm | 0.009 [0.006, 0.013] |  |  | 43 | 5 | 8cc031eb |
| test1 | start_points | fixed:100 | rmse_h10 | itransformer | 0.020 [0.012, 0.033] |  |  | 43 | 5 | 4e5853ab |
| test1 | start_points | fixed:100 | rmse_h10 | lgbm | 0.025 [0.012, 0.043] |  |  | 43 | 5 | 8cc031eb |
| test1 | start_points | fixed:100 | rmse_h100 | itransformer | 0.125 [0.094, 0.161] |  |  | 42 | 5 | 4e5853ab |
| test1 | start_points | fixed:100 | rmse_h100 | lgbm | 0.138 [0.104, 0.176] |  |  | 42 | 5 | 8cc031eb |
| test1 | start_points | fixed:100 | rmse_h200 | itransformer | 0.483 [0.362, 0.625] |  |  | 42 | 5 | 4e5853ab |
| test1 | start_points | fixed:100 | rmse_h200 | lgbm | 0.508 [0.331, 0.739] |  |  | 42 | 5 | 8cc031eb |
| test1 | start_points | fixed:100 | rmse_h50 | itransformer | 0.091 [0.035, 0.192] |  |  | 43 | 5 | 4e5853ab |
| test1 | start_points | fixed:100 | rmse_h50 | lgbm | 0.134 [0.045, 0.290] |  |  | 43 | 5 | 8cc031eb |
| test1 | start_points | frac:0.3 | rmse_h1 | itransformer | 0.015 [0.010, 0.022] |  |  | 43 | 5 | 4e5853ab |
| test1 | start_points | frac:0.3 | rmse_h1 | lgbm | 0.016 [0.010, 0.025] |  |  | 43 | 5 | 8cc031eb |
| test1 | start_points | frac:0.3 | rmse_h10 | itransformer | 0.048 [0.025, 0.077] |  |  | 43 | 5 | 4e5853ab |
| test1 | start_points | frac:0.3 | rmse_h10 | lgbm | 0.057 [0.032, 0.088] |  |  | 43 | 5 | 8cc031eb |
| test1 | start_points | frac:0.3 | rmse_h100 | itransformer | 0.275 [0.176, 0.413] |  |  | 43 | 5 | 4e5853ab |
| test1 | start_points | frac:0.3 | rmse_h100 | lgbm | 0.363 [0.133, 0.748] |  |  | 43 | 5 | 8cc031eb |
| test1 | start_points | frac:0.3 | rmse_h200 | itransformer | 0.806 [0.575, 1.079] |  |  | 42 | 5 | 4e5853ab |
| test1 | start_points | frac:0.3 | rmse_h200 | lgbm | 0.644 [0.389, 0.956] |  |  | 42 | 5 | 8cc031eb |
| test1 | start_points | frac:0.3 | rmse_h50 | itransformer | 0.084 [0.058, 0.117] |  |  | 43 | 5 | 4e5853ab |
| test1 | start_points | frac:0.3 | rmse_h50 | lgbm | 0.127 [0.051, 0.256] |  |  | 43 | 5 | 8cc031eb |
| test1 | start_points | frac:0.5 | rmse_h1 | itransformer | 0.037 [0.021, 0.056] |  |  | 43 | 5 | 4e5853ab |
| test1 | start_points | frac:0.5 | rmse_h1 | lgbm | 0.028 [0.016, 0.046] |  |  | 43 | 5 | 8cc031eb |
| test1 | start_points | frac:0.5 | rmse_h10 | itransformer | 0.063 [0.044, 0.085] |  |  | 43 | 5 | 4e5853ab |
| test1 | start_points | frac:0.5 | rmse_h10 | lgbm | 0.076 [0.049, 0.113] |  |  | 43 | 5 | 8cc031eb |
| test1 | start_points | frac:0.5 | rmse_h100 | itransformer | 0.643 [0.364, 1.023] |  |  | 42 | 5 | 4e5853ab |
| test1 | start_points | frac:0.5 | rmse_h100 | lgbm | 0.535 [0.338, 0.762] |  |  | 42 | 5 | 8cc031eb |
| test1 | start_points | frac:0.5 | rmse_h200 | itransformer | 2.615 [1.706, 3.821] |  |  | 41 | 5 | 4e5853ab |
| test1 | start_points | frac:0.5 | rmse_h200 | lgbm | 1.255 [0.931, 1.607] |  |  | 41 | 5 | 8cc031eb |
| test1 | start_points | frac:0.5 | rmse_h50 | itransformer | 0.229 [0.134, 0.346] |  |  | 43 | 5 | 4e5853ab |
| test1 | start_points | frac:0.5 | rmse_h50 | lgbm | 0.274 [0.174, 0.393] |  |  | 43 | 5 | 8cc031eb |
| test1 | start_points | frac:0.7 | rmse_h1 | itransformer | 0.051 [0.028, 0.082] |  |  | 43 | 5 | 4e5853ab |
| test1 | start_points | frac:0.7 | rmse_h1 | lgbm | 0.053 [0.029, 0.084] |  |  | 43 | 5 | 8cc031eb |
| test1 | start_points | frac:0.7 | rmse_h10 | itransformer | 0.102 [0.040, 0.191] |  |  | 43 | 5 | 4e5853ab |
| test1 | start_points | frac:0.7 | rmse_h10 | lgbm | 0.104 [0.045, 0.188] |  |  | 43 | 5 | 8cc031eb |
| test1 | start_points | frac:0.7 | rmse_h100 | itransformer | 0.864 [0.528, 1.330] |  |  | 42 | 5 | 4e5853ab |
| test1 | start_points | frac:0.7 | rmse_h100 | lgbm | 0.820 [0.595, 1.081] |  |  | 42 | 5 | 8cc031eb |
| test1 | start_points | frac:0.7 | rmse_h200 | itransformer | 1.225 [0.679, 1.845] |  |  | 17 | 5 | 4e5853ab |
| test1 | start_points | frac:0.7 | rmse_h200 | lgbm | 1.564 [1.051, 2.135] |  |  | 17 | 5 | 8cc031eb |
| test1 | start_points | frac:0.7 | rmse_h50 | itransformer | 0.335 [0.182, 0.552] |  |  | 43 | 5 | 4e5853ab |
| test1 | start_points | frac:0.7 | rmse_h50 | lgbm | 0.326 [0.186, 0.523] |  |  | 43 | 5 | 8cc031eb |
| test1 | start_points | overall | rmse_h1 | itransformer | 0.040 [0.026, 0.057] |  |  | 43 | 5 | 4e5853ab |
| test1 | start_points | overall | rmse_h1 | lgbm | 0.039 [0.026, 0.055] |  |  | 43 | 5 | 8cc031eb |
| test1 | start_points | overall | rmse_h10 | itransformer | 0.083 [0.049, 0.128] |  |  | 43 | 5 | 4e5853ab |
| test1 | start_points | overall | rmse_h10 | lgbm | 0.093 [0.058, 0.136] |  |  | 43 | 5 | 8cc031eb |
| test1 | start_points | overall | rmse_h100 | itransformer | 0.713 [0.484, 0.987] |  |  | 43 | 5 | 4e5853ab |
| test1 | start_points | overall | rmse_h100 | lgbm | 0.765 [0.504, 1.153] |  |  | 43 | 5 | 8cc031eb |
| test1 | start_points | overall | rmse_h200 | itransformer | 1.756 [1.294, 2.351] |  |  | 42 | 5 | 4e5853ab |
| test1 | start_points | overall | rmse_h200 | lgbm | 1.070 [0.817, 1.355] |  |  | 42 | 5 | 8cc031eb |
| test1 | start_points | overall | rmse_h50 | itransformer | 0.252 [0.151, 0.379] |  |  | 43 | 5 | 4e5853ab |
| test1 | start_points | overall | rmse_h50 | lgbm | 0.274 [0.169, 0.423] |  |  | 43 | 5 | 8cc031eb |
| test2 | all | overall | rmse_h1 | itransformer | 0.015 [0.013, 0.018] |  |  | 40 | 5 | 4e5853ab |
| test2 | all | overall | rmse_h1 | lgbm | 0.019 [0.017, 0.021] |  |  | 40 | 5 | 8cc031eb |
| test2 | all | overall | rmse_h10 | itransformer | 0.035 [0.032, 0.040] |  |  | 40 | 5 | 4e5853ab |
| test2 | all | overall | rmse_h10 | lgbm | 0.059 [0.054, 0.065] |  |  | 40 | 5 | 8cc031eb |
| test2 | all | overall | rmse_h100 | itransformer | 0.580 [0.518, 0.644] |  |  | 40 | 5 | 4e5853ab |
| test2 | all | overall | rmse_h100 | lgbm | 0.684 [0.630, 0.743] |  |  | 40 | 5 | 8cc031eb |
| test2 | all | overall | rmse_h200 | itransformer | 1.293 [1.151, 1.454] |  |  | 40 | 5 | 4e5853ab |
| test2 | all | overall | rmse_h200 | lgbm | 1.816 [1.691, 1.950] |  |  | 40 | 5 | 8cc031eb |
| test2 | all | overall | rmse_h50 | itransformer | 0.226 [0.196, 0.256] |  |  | 40 | 5 | 4e5853ab |
| test2 | all | overall | rmse_h50 | lgbm | 0.281 [0.257, 0.305] |  |  | 40 | 5 | 8cc031eb |
| test2 | start_points | fixed:100 | rmse_h1 | itransformer | 0.008 [0.004, 0.015] |  |  | 40 | 5 | 4e5853ab |
| test2 | start_points | fixed:100 | rmse_h1 | lgbm | 0.011 [0.005, 0.018] |  |  | 40 | 5 | 8cc031eb |
| test2 | start_points | fixed:100 | rmse_h10 | itransformer | 0.018 [0.010, 0.028] |  |  | 40 | 5 | 4e5853ab |
| test2 | start_points | fixed:100 | rmse_h10 | lgbm | 0.047 [0.039, 0.058] |  |  | 40 | 5 | 8cc031eb |
| test2 | start_points | fixed:100 | rmse_h100 | itransformer | 0.098 [0.073, 0.128] |  |  | 40 | 5 | 4e5853ab |
| test2 | start_points | fixed:100 | rmse_h100 | lgbm | 0.554 [0.529, 0.578] |  |  | 40 | 5 | 8cc031eb |
| test2 | start_points | fixed:100 | rmse_h200 | itransformer | 0.354 [0.235, 0.509] |  |  | 40 | 5 | 4e5853ab |
| test2 | start_points | fixed:100 | rmse_h200 | lgbm | 1.462 [1.407, 1.521] |  |  | 40 | 5 | 8cc031eb |
| test2 | start_points | fixed:100 | rmse_h50 | itransformer | 0.054 [0.043, 0.067] |  |  | 40 | 5 | 4e5853ab |
| test2 | start_points | fixed:100 | rmse_h50 | lgbm | 0.207 [0.191, 0.222] |  |  | 40 | 5 | 8cc031eb |
| test2 | start_points | frac:0.3 | rmse_h1 | itransformer | 0.014 [0.006, 0.025] |  |  | 40 | 5 | 4e5853ab |
| test2 | start_points | frac:0.3 | rmse_h1 | lgbm | 0.019 [0.010, 0.029] |  |  | 40 | 5 | 8cc031eb |
| test2 | start_points | frac:0.3 | rmse_h10 | itransformer | 0.016 [0.010, 0.023] |  |  | 40 | 5 | 4e5853ab |
| test2 | start_points | frac:0.3 | rmse_h10 | lgbm | 0.049 [0.040, 0.060] |  |  | 40 | 5 | 8cc031eb |
| test2 | start_points | frac:0.3 | rmse_h100 | itransformer | 0.186 [0.109, 0.282] |  |  | 40 | 5 | 4e5853ab |
| test2 | start_points | frac:0.3 | rmse_h100 | lgbm | 0.588 [0.536, 0.647] |  |  | 40 | 5 | 8cc031eb |
| test2 | start_points | frac:0.3 | rmse_h200 | itransformer | 0.699 [0.380, 1.089] |  |  | 40 | 5 | 4e5853ab |
| test2 | start_points | frac:0.3 | rmse_h200 | lgbm | 1.634 [1.466, 1.826] |  |  | 40 | 5 | 8cc031eb |
| test2 | start_points | frac:0.3 | rmse_h50 | itransformer | 0.067 [0.042, 0.097] |  |  | 40 | 5 | 4e5853ab |
| test2 | start_points | frac:0.3 | rmse_h50 | lgbm | 0.214 [0.192, 0.237] |  |  | 40 | 5 | 8cc031eb |
| test2 | start_points | frac:0.5 | rmse_h1 | itransformer | 0.008 [0.005, 0.013] |  |  | 40 | 5 | 4e5853ab |
| test2 | start_points | frac:0.5 | rmse_h1 | lgbm | 0.011 [0.007, 0.018] |  |  | 40 | 5 | 8cc031eb |
| test2 | start_points | frac:0.5 | rmse_h10 | itransformer | 0.018 [0.013, 0.025] |  |  | 40 | 5 | 4e5853ab |
| test2 | start_points | frac:0.5 | rmse_h10 | lgbm | 0.060 [0.049, 0.070] |  |  | 40 | 5 | 8cc031eb |
| test2 | start_points | frac:0.5 | rmse_h100 | itransformer | 0.190 [0.141, 0.244] |  |  | 40 | 5 | 4e5853ab |
| test2 | start_points | frac:0.5 | rmse_h100 | lgbm | 0.575 [0.495, 0.656] |  |  | 40 | 5 | 8cc031eb |
| test2 | start_points | frac:0.5 | rmse_h200 | itransformer | 0.798 [0.584, 1.041] |  |  | 40 | 5 | 4e5853ab |
| test2 | start_points | frac:0.5 | rmse_h200 | lgbm | 1.977 [1.737, 2.217] |  |  | 40 | 5 | 8cc031eb |
| test2 | start_points | frac:0.5 | rmse_h50 | itransformer | 0.064 [0.051, 0.080] |  |  | 40 | 5 | 4e5853ab |
| test2 | start_points | frac:0.5 | rmse_h50 | lgbm | 0.229 [0.197, 0.263] |  |  | 40 | 5 | 8cc031eb |
| test2 | start_points | frac:0.7 | rmse_h1 | itransformer | 0.007 [0.004, 0.014] |  |  | 40 | 5 | 4e5853ab |
| test2 | start_points | frac:0.7 | rmse_h1 | lgbm | 0.010 [0.006, 0.017] |  |  | 40 | 5 | 8cc031eb |
| test2 | start_points | frac:0.7 | rmse_h10 | itransformer | 0.014 [0.011, 0.017] |  |  | 40 | 5 | 4e5853ab |
| test2 | start_points | frac:0.7 | rmse_h10 | lgbm | 0.046 [0.036, 0.055] |  |  | 40 | 5 | 8cc031eb |
| test2 | start_points | frac:0.7 | rmse_h100 | itransformer | 0.302 [0.241, 0.370] |  |  | 40 | 5 | 4e5853ab |
| test2 | start_points | frac:0.7 | rmse_h100 | lgbm | 0.580 [0.473, 0.707] |  |  | 40 | 5 | 8cc031eb |
| test2 | start_points | frac:0.7 | rmse_h200 | itransformer | 1.366 [1.001, 1.835] |  |  | 38 | 5 | 4e5853ab |
| test2 | start_points | frac:0.7 | rmse_h200 | lgbm | 1.262 [1.024, 1.512] |  |  | 38 | 5 | 8cc031eb |
| test2 | start_points | frac:0.7 | rmse_h50 | itransformer | 0.074 [0.059, 0.090] |  |  | 40 | 5 | 4e5853ab |
| test2 | start_points | frac:0.7 | rmse_h50 | lgbm | 0.203 [0.172, 0.234] |  |  | 40 | 5 | 8cc031eb |
| test2 | start_points | overall | rmse_h1 | itransformer | 0.013 [0.007, 0.019] |  |  | 40 | 5 | 4e5853ab |
| test2 | start_points | overall | rmse_h1 | lgbm | 0.017 [0.011, 0.024] |  |  | 40 | 5 | 8cc031eb |
| test2 | start_points | overall | rmse_h10 | itransformer | 0.021 [0.016, 0.026] |  |  | 40 | 5 | 4e5853ab |
| test2 | start_points | overall | rmse_h10 | lgbm | 0.055 [0.049, 0.063] |  |  | 40 | 5 | 8cc031eb |
| test2 | start_points | overall | rmse_h100 | itransformer | 0.247 [0.203, 0.297] |  |  | 40 | 5 | 4e5853ab |
| test2 | start_points | overall | rmse_h100 | lgbm | 0.598 [0.544, 0.660] |  |  | 40 | 5 | 8cc031eb |
| test2 | start_points | overall | rmse_h200 | itransformer | 1.103 [0.875, 1.367] |  |  | 40 | 5 | 4e5853ab |
| test2 | start_points | overall | rmse_h200 | lgbm | 1.672 [1.540, 1.814] |  |  | 40 | 5 | 8cc031eb |
| test2 | start_points | overall | rmse_h50 | itransformer | 0.079 [0.067, 0.093] |  |  | 40 | 5 | 4e5853ab |
| test2 | start_points | overall | rmse_h50 | lgbm | 0.221 [0.201, 0.240] |  |  | 40 | 5 | 8cc031eb |

</details>

<details><summary>toyota_soh (24 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rmse | itransformer | 0.111 [0.067, 0.163] |  |  | 43 | 5 | 2dc7d291 |
| test1 | all | overall | rmse | lgbm | 0.133 [0.079, 0.196] |  |  | 43 | 5 | 627b7c23 |
| test1 | start_points | fixed:100 | rmse | itransformer | 0.009 [0.006, 0.014] |  |  | 43 | 5 | 2dc7d291 |
| test1 | start_points | fixed:100 | rmse | lgbm | 0.014 [0.008, 0.020] |  |  | 43 | 5 | 627b7c23 |
| test1 | start_points | frac:0.3 | rmse | itransformer | 0.017 [0.008, 0.030] |  |  | 43 | 5 | 2dc7d291 |
| test1 | start_points | frac:0.3 | rmse | lgbm | 0.029 [0.011, 0.057] |  |  | 43 | 5 | 627b7c23 |
| test1 | start_points | frac:0.5 | rmse | itransformer | 0.030 [0.017, 0.047] |  |  | 43 | 5 | 2dc7d291 |
| test1 | start_points | frac:0.5 | rmse | lgbm | 0.023 [0.013, 0.037] |  |  | 43 | 5 | 627b7c23 |
| test1 | start_points | frac:0.7 | rmse | itransformer | 0.030 [0.022, 0.038] |  |  | 43 | 5 | 2dc7d291 |
| test1 | start_points | frac:0.7 | rmse | lgbm | 0.029 [0.020, 0.039] |  |  | 43 | 5 | 627b7c23 |
| test1 | start_points | overall | rmse | itransformer | 0.029 [0.021, 0.039] |  |  | 43 | 5 | 2dc7d291 |
| test1 | start_points | overall | rmse | lgbm | 0.031 [0.020, 0.047] |  |  | 43 | 5 | 627b7c23 |
| test2 | all | overall | rmse | itransformer | 0.025 [0.023, 0.027] |  |  | 40 | 5 | 2dc7d291 |
| test2 | all | overall | rmse | lgbm | 0.020 [0.018, 0.023] |  |  | 40 | 5 | 627b7c23 |
| test2 | start_points | fixed:100 | rmse | itransformer | 0.025 [0.020, 0.032] |  |  | 40 | 5 | 2dc7d291 |
| test2 | start_points | fixed:100 | rmse | lgbm | 0.011 [0.005, 0.020] |  |  | 40 | 5 | 627b7c23 |
| test2 | start_points | frac:0.3 | rmse | itransformer | 0.027 [0.023, 0.031] |  |  | 40 | 5 | 2dc7d291 |
| test2 | start_points | frac:0.3 | rmse | lgbm | 0.011 [0.006, 0.018] |  |  | 40 | 5 | 627b7c23 |
| test2 | start_points | frac:0.5 | rmse | itransformer | 0.027 [0.024, 0.032] |  |  | 40 | 5 | 2dc7d291 |
| test2 | start_points | frac:0.5 | rmse | lgbm | 0.019 [0.011, 0.029] |  |  | 40 | 5 | 627b7c23 |
| test2 | start_points | frac:0.7 | rmse | itransformer | 0.021 [0.018, 0.025] |  |  | 40 | 5 | 2dc7d291 |
| test2 | start_points | frac:0.7 | rmse | lgbm | 0.014 [0.009, 0.020] |  |  | 40 | 5 | 627b7c23 |
| test2 | start_points | overall | rmse | itransformer | 0.027 [0.024, 0.031] |  |  | 40 | 5 | 2dc7d291 |
| test2 | start_points | overall | rmse | lgbm | 0.019 [0.013, 0.025] |  |  | 40 | 5 | 627b7c23 |

</details>
