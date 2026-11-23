# Benchmark tables: field_regen

- Protocol version: 1.1
- Git SHA: eecc261b52
- Seeds: 5  |  unit runs: 200
- Note: n = 4 cells per NASA/CALCE dataset, so the 95 % cluster-bootstrap CI is wide by construction. Toyota rows are over test cells (test1 / test2 separately) with a cell-level bootstrap CI and a Holm-adjusted Wilcoxon p vs the best baseline. All metrics are computed per cell from the logged predictions.

## Headline (kind = overall; RMSE in %SOH, RUL MAE in cycles)

### calce_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | itransformer[lookback=32,rest_token=True] | 3.786 [2.705, 4.872] |  |  | 4 | 5 | 87c0ee93 |
| loco | all | overall | rmse_h1 | itransformer[lookback=32] | 4.235 [3.658, 5.187] |  |  | 4 | 5 | 0bd789f1 |
| loco | all | overall | rmse_h1 | lgbm | 4.245 [2.537, 5.515] |  |  | 4 | 5 | eb92ee9b |
| loco | all | overall | rmse_h1 | lstm[lookback=128] | 1.614 [1.362, 1.876] |  |  | 4 | 5 | f24ee787 |
| loco | all | overall | rmse_h1 | transformer[lookback=32] | 2.653 [1.827, 3.698] |  |  | 4 | 5 | bb15ad85 |
| loco | all | overall | rmse_h10 | itransformer[lookback=32,rest_token=True] | 3.966 [2.881, 5.092] |  |  | 4 | 5 | 87c0ee93 |
| loco | all | overall | rmse_h10 | itransformer[lookback=32] | 4.337 [3.770, 5.312] |  |  | 4 | 5 | 0bd789f1 |
| loco | all | overall | rmse_h10 | lgbm | 4.197 [2.577, 5.399] |  |  | 4 | 5 | eb92ee9b |
| loco | all | overall | rmse_h10 | lstm[lookback=128] | 1.874 [1.669, 2.153] |  |  | 4 | 5 | f24ee787 |
| loco | all | overall | rmse_h10 | transformer[lookback=32] | 2.552 [1.941, 3.317] |  |  | 4 | 5 | bb15ad85 |
| loco | all | overall | rmse_h50 | itransformer[lookback=32,rest_token=True] | 3.995 [2.869, 5.120] |  |  | 4 | 5 | 87c0ee93 |
| loco | all | overall | rmse_h50 | itransformer[lookback=32] | 4.628 [4.216, 5.286] |  |  | 4 | 5 | 0bd789f1 |
| loco | all | overall | rmse_h50 | lgbm | 4.720 [3.252, 5.800] |  |  | 4 | 5 | eb92ee9b |
| loco | all | overall | rmse_h50 | lstm[lookback=128] | 2.352 [1.950, 2.755] |  |  | 4 | 5 | f24ee787 |
| loco | all | overall | rmse_h50 | transformer[lookback=32] | 3.132 [2.423, 4.029] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | overall | rmse_h1 | itransformer[lookback=32,rest_token=True] | 1.801 [1.171, 2.431] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | overall | rmse_h1 | itransformer[lookback=32] | 2.439 [1.592, 3.228] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | overall | rmse_h1 | lgbm | 1.751 [0.570, 3.664] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | overall | rmse_h1 | lstm[lookback=128] | 0.833 [0.623, 1.106] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | overall | rmse_h1 | transformer[lookback=32] | 1.218 [1.131, 1.317] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | overall | rmse_h10 | itransformer[lookback=32,rest_token=True] | 1.976 [1.353, 2.600] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | overall | rmse_h10 | itransformer[lookback=32] | 2.299 [1.432, 2.824] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | overall | rmse_h10 | lgbm | 1.999 [0.810, 3.451] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | overall | rmse_h10 | lstm[lookback=128] | 1.190 [0.720, 1.660] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | overall | rmse_h10 | transformer[lookback=32] | 1.138 [0.618, 1.658] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | overall | rmse_h50 | itransformer[lookback=32,rest_token=True] | 2.048 [1.800, 2.326] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | overall | rmse_h50 | itransformer[lookback=32] | 2.293 [2.149, 2.448] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | overall | rmse_h50 | lgbm | 2.439 [1.127, 4.288] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | overall | rmse_h50 | lstm[lookback=128] | 1.829 [0.834, 2.714] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | overall | rmse_h50 | transformer[lookback=32] | 2.014 [1.178, 2.710] |  |  | 4 | 5 | bb15ad85 |

### nasa_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | itransformer[lookback=64,rest_token=True] | 6.496 [4.981, 7.935] |  | 6.790 | 4 | 5 | 84b978b3 |
| loco | all | overall | rmse_h1 | itransformer[lookback=64] | 6.524 [5.034, 7.899] |  | 6.505 | 4 | 5 | 53eea59e |
| loco | all | overall | rmse_h1 | lgbm | 3.549 [1.667, 6.452] |  | 2.368 | 4 | 5 | 1287a5eb |
| loco | all | overall | rmse_h1 | lstm[lookback=64] | 4.174 [2.586, 5.762] |  | 6.541 | 4 | 5 | c585c752 |
| loco | all | overall | rmse_h1 | transformer[lookback=64] | 7.857 [4.997, 11.456] |  | 7.955 | 4 | 5 | c4909d46 |
| loco | all | overall | rmse_h10 | itransformer[lookback=64,rest_token=True] | 6.124 [4.777, 7.669] |  | 6.331 | 4 | 5 | 84b978b3 |
| loco | all | overall | rmse_h10 | itransformer[lookback=64] | 6.273 [4.840, 7.791] |  | 5.909 | 4 | 5 | 53eea59e |
| loco | all | overall | rmse_h10 | lgbm | 4.259 [2.557, 6.930] |  | 2.599 | 4 | 5 | 1287a5eb |
| loco | all | overall | rmse_h10 | lstm[lookback=64] | 4.123 [2.840, 5.406] |  | 5.257 | 4 | 5 | c585c752 |
| loco | all | overall | rmse_h10 | transformer[lookback=64] | 7.755 [5.062, 10.721] |  | 8.396 | 4 | 5 | c4909d46 |
| loco | all | overall | rmse_h50 | itransformer[lookback=64,rest_token=True] | 6.314 [4.670, 8.164] |  | 5.116 | 4 | 5 | 84b978b3 |
| loco | all | overall | rmse_h50 | itransformer[lookback=64] | 6.353 [4.596, 8.122] |  | 4.942 | 4 | 5 | 53eea59e |
| loco | all | overall | rmse_h50 | lgbm | 6.380 [3.555, 9.770] |  | 2.668 | 4 | 5 | 1287a5eb |
| loco | all | overall | rmse_h50 | lstm[lookback=64] | 6.593 [4.240, 9.933] |  | 5.689 | 4 | 5 | c585c752 |
| loco | all | overall | rmse_h50 | transformer[lookback=64] | 6.856 [4.440, 10.937] |  | 5.256 | 4 | 5 | c4909d46 |
| loco | start_points | overall | rmse_h1 | itransformer[lookback=64,rest_token=True] | 5.510 [4.175, 6.844] |  | 6.797 | 4 | 5 | 84b978b3 |
| loco | start_points | overall | rmse_h1 | itransformer[lookback=64] | 5.504 [4.692, 6.315] |  | 6.379 | 4 | 5 | 53eea59e |
| loco | start_points | overall | rmse_h1 | lgbm | 2.273 [1.052, 3.391] |  | 2.606 | 4 | 5 | 1287a5eb |
| loco | start_points | overall | rmse_h1 | lstm[lookback=64] | 3.359 [2.303, 4.366] |  | 4.593 | 4 | 5 | c585c752 |
| loco | start_points | overall | rmse_h1 | transformer[lookback=64] | 4.834 [3.688, 6.518] |  | 4.237 | 4 | 5 | c4909d46 |
| loco | start_points | overall | rmse_h10 | itransformer[lookback=64,rest_token=True] | 5.010 [4.355, 5.540] |  | 5.710 | 4 | 5 | 84b978b3 |
| loco | start_points | overall | rmse_h10 | itransformer[lookback=64] | 5.619 [5.242, 5.995] |  | 5.995 | 4 | 5 | 53eea59e |
| loco | start_points | overall | rmse_h10 | lgbm | 3.925 [2.496, 5.354] |  | 2.802 | 4 | 5 | 1287a5eb |
| loco | start_points | overall | rmse_h10 | lstm[lookback=64] | 4.512 [3.370, 6.268] |  | 3.862 | 4 | 5 | c585c752 |
| loco | start_points | overall | rmse_h10 | transformer[lookback=64] | 6.106 [5.322, 7.389] |  | 5.562 | 4 | 5 | c4909d46 |
| loco | start_points | overall | rmse_h50 | itransformer[lookback=64,rest_token=True] | 5.568 [4.457, 6.682] |  | 5.681 | 4 | 5 | 84b978b3 |
| loco | start_points | overall | rmse_h50 | itransformer[lookback=64] | 5.521 [4.348, 7.015] |  | 5.021 | 4 | 5 | 53eea59e |
| loco | start_points | overall | rmse_h50 | lgbm | 5.545 [3.575, 7.807] |  | 2.763 | 4 | 5 | 1287a5eb |
| loco | start_points | overall | rmse_h50 | lstm[lookback=64] | 6.204 [3.287, 9.689] |  | 6.684 | 4 | 5 | c585c752 |
| loco | start_points | overall | rmse_h50 | transformer[lookback=64] | 5.776 [3.659, 9.558] |  | 3.561 | 4 | 5 | c4909d46 |

## Mean rank (dataset x task x split x policy x headline metric)

| model | mean rank | conditions | missing |
|---|---|---|---|
| lstm[lookback=128] | 1.17 | 6 | 6 |
| transformer[lookback=32] | 1.83 | 6 | 6 |
| lstm[lookback=64] | 2.67 | 6 | 6 |
| itransformer[lookback=64,rest_token=True] | 3.00 | 6 | 6 |
| lgbm | 3.00 | 12 | 0 |
| itransformer[lookback=32,rest_token=True] | 3.17 | 6 | 6 |
| itransformer[lookback=64] | 3.17 | 6 | 6 |
| itransformer[lookback=32] | 4.50 | 6 | 6 |
| transformer[lookback=64] | 4.50 | 6 | 6 |

## Full tables

<details><summary>calce_forecast (175 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | itransformer[lookback=32,rest_token=True] | 3.786 [2.705, 4.872] |  |  | 4 | 5 | 87c0ee93 |
| loco | all | overall | rmse_h1 | itransformer[lookback=32] | 4.235 [3.658, 5.187] |  |  | 4 | 5 | 0bd789f1 |
| loco | all | overall | rmse_h1 | lgbm | 4.245 [2.537, 5.515] |  |  | 4 | 5 | eb92ee9b |
| loco | all | overall | rmse_h1 | lstm[lookback=128] | 1.614 [1.362, 1.876] |  |  | 4 | 5 | f24ee787 |
| loco | all | overall | rmse_h1 | transformer[lookback=32] | 2.653 [1.827, 3.698] |  |  | 4 | 5 | bb15ad85 |
| loco | all | overall | rmse_h10 | itransformer[lookback=32,rest_token=True] | 3.966 [2.881, 5.092] |  |  | 4 | 5 | 87c0ee93 |
| loco | all | overall | rmse_h10 | itransformer[lookback=32] | 4.337 [3.770, 5.312] |  |  | 4 | 5 | 0bd789f1 |
| loco | all | overall | rmse_h10 | lgbm | 4.197 [2.577, 5.399] |  |  | 4 | 5 | eb92ee9b |
| loco | all | overall | rmse_h10 | lstm[lookback=128] | 1.874 [1.669, 2.153] |  |  | 4 | 5 | f24ee787 |
| loco | all | overall | rmse_h10 | transformer[lookback=32] | 2.552 [1.941, 3.317] |  |  | 4 | 5 | bb15ad85 |
| loco | all | overall | rmse_h100 | itransformer[lookback=32,rest_token=True] | 4.491 [3.595, 5.388] |  |  | 4 | 5 | 87c0ee93 |
| loco | all | overall | rmse_h100 | itransformer[lookback=32] | 5.343 [4.960, 5.661] |  |  | 4 | 5 | 0bd789f1 |
| loco | all | overall | rmse_h100 | lgbm | 5.073 [4.119, 6.086] |  |  | 4 | 5 | eb92ee9b |
| loco | all | overall | rmse_h100 | lstm[lookback=128] | 2.718 [2.102, 3.317] |  |  | 4 | 5 | f24ee787 |
| loco | all | overall | rmse_h100 | transformer[lookback=32] | 3.189 [2.897, 3.418] |  |  | 4 | 5 | bb15ad85 |
| loco | all | overall | rmse_h25 | itransformer[lookback=32,rest_token=True] | 3.942 [2.852, 5.032] |  |  | 4 | 5 | 87c0ee93 |
| loco | all | overall | rmse_h25 | itransformer[lookback=32] | 4.459 [3.831, 5.361] |  |  | 4 | 5 | 0bd789f1 |
| loco | all | overall | rmse_h25 | lgbm | 4.637 [3.008, 5.977] |  |  | 4 | 5 | eb92ee9b |
| loco | all | overall | rmse_h25 | lstm[lookback=128] | 2.133 [1.845, 2.410] |  |  | 4 | 5 | f24ee787 |
| loco | all | overall | rmse_h25 | transformer[lookback=32] | 2.416 [2.129, 2.695] |  |  | 4 | 5 | bb15ad85 |
| loco | all | overall | rmse_h50 | itransformer[lookback=32,rest_token=True] | 3.995 [2.869, 5.120] |  |  | 4 | 5 | 87c0ee93 |
| loco | all | overall | rmse_h50 | itransformer[lookback=32] | 4.628 [4.216, 5.286] |  |  | 4 | 5 | 0bd789f1 |
| loco | all | overall | rmse_h50 | lgbm | 4.720 [3.252, 5.800] |  |  | 4 | 5 | eb92ee9b |
| loco | all | overall | rmse_h50 | lstm[lookback=128] | 2.352 [1.950, 2.755] |  |  | 4 | 5 | f24ee787 |
| loco | all | overall | rmse_h50 | transformer[lookback=32] | 3.132 [2.423, 4.029] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | fixed:200 | rmse_h1 | itransformer[lookback=32,rest_token=True] | 1.543 [0.716, 2.371] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | fixed:200 | rmse_h1 | itransformer[lookback=32] | 2.460 [1.123, 3.797] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | fixed:200 | rmse_h1 | lgbm | 0.315 [0.087, 0.614] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | fixed:200 | rmse_h1 | lstm[lookback=128] | 0.580 [0.183, 1.342] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | fixed:200 | rmse_h1 | transformer[lookback=32] | 0.939 [0.476, 1.670] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | fixed:200 | rmse_h10 | itransformer[lookback=32,rest_token=True] | 1.586 [1.101, 2.226] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | fixed:200 | rmse_h10 | itransformer[lookback=32] | 1.672 [1.086, 2.648] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | fixed:200 | rmse_h10 | lgbm | 1.183 [0.287, 2.376] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | fixed:200 | rmse_h10 | lstm[lookback=128] | 1.226 [0.467, 1.985] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | fixed:200 | rmse_h10 | transformer[lookback=32] | 1.067 [0.269, 1.865] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | fixed:200 | rmse_h100 | itransformer[lookback=32,rest_token=True] | 1.854 [1.033, 3.162] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | fixed:200 | rmse_h100 | itransformer[lookback=32] | 2.711 [2.015, 3.527] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | fixed:200 | rmse_h100 | lgbm | 1.762 [0.511, 3.372] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | fixed:200 | rmse_h100 | lstm[lookback=128] | 1.065 [0.447, 1.943] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | fixed:200 | rmse_h100 | transformer[lookback=32] | 1.016 [0.669, 1.263] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | fixed:200 | rmse_h25 | itransformer[lookback=32,rest_token=True] | 1.367 [0.865, 1.671] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | fixed:200 | rmse_h25 | itransformer[lookback=32] | 1.486 [0.973, 1.973] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | fixed:200 | rmse_h25 | lgbm | 2.481 [1.609, 3.969] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | fixed:200 | rmse_h25 | lstm[lookback=128] | 1.693 [0.883, 2.394] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | fixed:200 | rmse_h25 | transformer[lookback=32] | 1.403 [0.937, 1.795] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | fixed:200 | rmse_h50 | itransformer[lookback=32,rest_token=True] | 1.612 [0.941, 2.395] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | fixed:200 | rmse_h50 | itransformer[lookback=32] | 1.978 [1.262, 2.539] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | fixed:200 | rmse_h50 | lgbm | 2.399 [0.711, 4.723] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | fixed:200 | rmse_h50 | lstm[lookback=128] | 1.409 [0.619, 2.200] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | fixed:200 | rmse_h50 | transformer[lookback=32] | 1.294 [0.618, 1.927] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | fixed:400 | rmse_h1 | itransformer[lookback=32,rest_token=True] | 0.942 [0.623, 1.292] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | fixed:400 | rmse_h1 | itransformer[lookback=32] | 1.664 [0.849, 2.768] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | fixed:400 | rmse_h1 | lgbm | 0.832 [0.519, 1.237] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | fixed:400 | rmse_h1 | lstm[lookback=128] | 0.862 [0.743, 0.998] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | fixed:400 | rmse_h1 | transformer[lookback=32] | 1.330 [0.514, 2.244] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | fixed:400 | rmse_h10 | itransformer[lookback=32,rest_token=True] | 1.157 [0.789, 1.549] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | fixed:400 | rmse_h10 | itransformer[lookback=32] | 1.520 [0.726, 2.479] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | fixed:400 | rmse_h10 | lgbm | 1.220 [0.526, 1.914] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | fixed:400 | rmse_h10 | lstm[lookback=128] | 0.961 [0.392, 1.529] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | fixed:400 | rmse_h10 | transformer[lookback=32] | 1.034 [0.499, 1.703] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | fixed:400 | rmse_h100 | itransformer[lookback=32,rest_token=True] | 2.286 [1.301, 3.381] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | fixed:400 | rmse_h100 | itransformer[lookback=32] | 2.242 [1.243, 3.683] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | fixed:400 | rmse_h100 | lgbm | 2.183 [1.052, 3.630] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | fixed:400 | rmse_h100 | lstm[lookback=128] | 3.184 [1.973, 4.693] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | fixed:400 | rmse_h100 | transformer[lookback=32] | 2.643 [0.634, 5.248] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | fixed:400 | rmse_h25 | itransformer[lookback=32,rest_token=True] | 1.544 [1.250, 1.858] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | fixed:400 | rmse_h25 | itransformer[lookback=32] | 2.502 [1.791, 3.212] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | fixed:400 | rmse_h25 | lgbm | 1.245 [0.252, 2.553] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | fixed:400 | rmse_h25 | lstm[lookback=128] | 1.649 [0.665, 2.675] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | fixed:400 | rmse_h25 | transformer[lookback=32] | 1.592 [0.799, 2.182] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | fixed:400 | rmse_h50 | itransformer[lookback=32,rest_token=True] | 2.101 [1.478, 3.123] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | fixed:400 | rmse_h50 | itransformer[lookback=32] | 2.694 [1.891, 3.589] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | fixed:400 | rmse_h50 | lgbm | 1.402 [0.329, 2.475] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | fixed:400 | rmse_h50 | lstm[lookback=128] | 2.352 [0.709, 3.996] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | fixed:400 | rmse_h50 | transformer[lookback=32] | 2.590 [1.122, 4.057] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer[lookback=32,rest_token=True] | 1.913 [0.825, 3.002] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer[lookback=32] | 2.611 [1.126, 4.202] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | frac:0.3 | rmse_h1 | lgbm | 2.952 [0.275, 7.922] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | frac:0.3 | rmse_h1 | lstm[lookback=128] | 0.853 [0.444, 1.205] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | frac:0.3 | rmse_h1 | transformer[lookback=32] | 1.010 [0.648, 1.468] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer[lookback=32,rest_token=True] | 2.129 [0.876, 3.383] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer[lookback=32] | 2.615 [1.101, 4.003] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | frac:0.3 | rmse_h10 | lgbm | 3.493 [1.159, 7.309] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | frac:0.3 | rmse_h10 | lstm[lookback=128] | 1.402 [0.874, 1.905] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | frac:0.3 | rmse_h10 | transformer[lookback=32] | 1.073 [0.464, 1.830] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer[lookback=32,rest_token=True] | 1.640 [0.655, 3.213] |  |  | 3 | 5 | 3be7b2c7 |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer[lookback=32] | 1.733 [1.000, 2.148] |  |  | 3 | 5 | 686f7a88 |
| loco | start_points | frac:0.3 | rmse_h100 | lgbm | 2.923 [0.574, 5.567] |  |  | 3 | 5 | 54caa0f1 |
| loco | start_points | frac:0.3 | rmse_h100 | lstm[lookback=128] | 1.833 [0.372, 2.800] |  |  | 3 | 5 | 8830006c |
| loco | start_points | frac:0.3 | rmse_h100 | transformer[lookback=32] | 1.851 [1.023, 2.676] |  |  | 3 | 5 | 89a5616f |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer[lookback=32,rest_token=True] | 1.927 [0.931, 3.564] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer[lookback=32] | 2.409 [1.437, 3.380] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | frac:0.3 | rmse_h25 | lgbm | 2.788 [0.243, 6.608] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | frac:0.3 | rmse_h25 | lstm[lookback=128] | 1.263 [0.732, 1.794] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | frac:0.3 | rmse_h25 | transformer[lookback=32] | 1.300 [0.812, 1.838] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer[lookback=32,rest_token=True] | 1.756 [0.734, 2.980] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer[lookback=32] | 1.517 [0.950, 2.310] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | frac:0.3 | rmse_h50 | lgbm | 4.051 [1.715, 7.730] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | frac:0.3 | rmse_h50 | lstm[lookback=128] | 2.342 [0.959, 3.725] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | frac:0.3 | rmse_h50 | transformer[lookback=32] | 2.338 [0.794, 3.883] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer[lookback=32,rest_token=True] | 2.156 [1.246, 3.065] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer[lookback=32] | 2.372 [1.502, 3.242] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | frac:0.5 | rmse_h1 | lgbm | 0.573 [0.194, 0.953] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | frac:0.5 | rmse_h1 | lstm[lookback=128] | 0.650 [0.346, 0.967] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | frac:0.5 | rmse_h1 | transformer[lookback=32] | 0.433 [0.315, 0.551] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer[lookback=32,rest_token=True] | 2.226 [1.145, 3.307] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer[lookback=32] | 2.490 [1.536, 3.326] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | frac:0.5 | rmse_h10 | lgbm | 0.795 [0.460, 1.118] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | frac:0.5 | rmse_h10 | lstm[lookback=128] | 0.996 [0.318, 1.673] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | frac:0.5 | rmse_h10 | transformer[lookback=32] | 0.997 [0.411, 1.582] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer[lookback=32,rest_token=True] | 2.454 [1.935, 2.898] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer[lookback=32] | 3.256 [2.809, 3.998] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | frac:0.5 | rmse_h100 | lgbm | 0.563 [0.160, 1.047] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | frac:0.5 | rmse_h100 | lstm[lookback=128] | 0.648 [0.169, 1.233] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | frac:0.5 | rmse_h100 | transformer[lookback=32] | 0.751 [0.327, 1.176] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer[lookback=32,rest_token=True] | 1.907 [1.316, 2.635] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer[lookback=32] | 2.444 [1.592, 3.190] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | frac:0.5 | rmse_h25 | lgbm | 1.016 [0.455, 1.391] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | frac:0.5 | rmse_h25 | lstm[lookback=128] | 1.045 [0.559, 1.531] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | frac:0.5 | rmse_h25 | transformer[lookback=32] | 1.145 [0.700, 1.557] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer[lookback=32,rest_token=True] | 1.856 [1.522, 2.181] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer[lookback=32] | 2.448 [2.119, 2.777] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | frac:0.5 | rmse_h50 | lgbm | 0.501 [0.289, 0.778] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | frac:0.5 | rmse_h50 | lstm[lookback=128] | 0.334 [0.274, 0.397] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | frac:0.5 | rmse_h50 | transformer[lookback=32] | 0.529 [0.383, 0.675] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer[lookback=32,rest_token=True] | 1.233 [0.659, 1.897] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer[lookback=32] | 1.572 [0.929, 2.215] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | frac:0.7 | rmse_h1 | lgbm | 0.964 [0.444, 1.565] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | frac:0.7 | rmse_h1 | lstm[lookback=128] | 0.711 [0.337, 1.134] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | frac:0.7 | rmse_h1 | transformer[lookback=32] | 1.213 [0.933, 1.492] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer[lookback=32,rest_token=True] | 1.329 [0.825, 1.833] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer[lookback=32] | 1.609 [0.836, 2.618] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | frac:0.7 | rmse_h10 | lgbm | 0.936 [0.705, 1.181] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | frac:0.7 | rmse_h10 | lstm[lookback=128] | 0.623 [0.251, 1.220] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | frac:0.7 | rmse_h10 | transformer[lookback=32] | 0.910 [0.367, 1.634] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer[lookback=32,rest_token=True] | 2.305 [1.882, 2.733] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer[lookback=32] | 2.181 [1.365, 3.325] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | frac:0.7 | rmse_h100 | lgbm | 1.612 [0.700, 2.455] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | frac:0.7 | rmse_h100 | lstm[lookback=128] | 2.379 [1.092, 4.100] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | frac:0.7 | rmse_h100 | transformer[lookback=32] | 2.180 [0.787, 4.178] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer[lookback=32,rest_token=True] | 1.093 [0.659, 1.563] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer[lookback=32] | 1.600 [0.911, 2.618] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | frac:0.7 | rmse_h25 | lgbm | 0.850 [0.154, 1.547] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | frac:0.7 | rmse_h25 | lstm[lookback=128] | 0.517 [0.284, 0.811] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | frac:0.7 | rmse_h25 | transformer[lookback=32] | 0.898 [0.524, 1.433] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer[lookback=32,rest_token=True] | 1.423 [1.129, 1.838] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer[lookback=32] | 1.350 [0.854, 1.811] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | frac:0.7 | rmse_h50 | lgbm | 0.666 [0.108, 1.546] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | frac:0.7 | rmse_h50 | lstm[lookback=128] | 1.254 [0.534, 1.975] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | frac:0.7 | rmse_h50 | transformer[lookback=32] | 1.672 [0.909, 2.434] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | overall | rmse_h1 | itransformer[lookback=32,rest_token=True] | 1.801 [1.171, 2.431] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | overall | rmse_h1 | itransformer[lookback=32] | 2.439 [1.592, 3.228] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | overall | rmse_h1 | lgbm | 1.751 [0.570, 3.664] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | overall | rmse_h1 | lstm[lookback=128] | 0.833 [0.623, 1.106] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | overall | rmse_h1 | transformer[lookback=32] | 1.218 [1.131, 1.317] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | overall | rmse_h10 | itransformer[lookback=32,rest_token=True] | 1.976 [1.353, 2.600] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | overall | rmse_h10 | itransformer[lookback=32] | 2.299 [1.432, 2.824] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | overall | rmse_h10 | lgbm | 1.999 [0.810, 3.451] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | overall | rmse_h10 | lstm[lookback=128] | 1.190 [0.720, 1.660] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | overall | rmse_h10 | transformer[lookback=32] | 1.138 [0.618, 1.658] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | overall | rmse_h100 | itransformer[lookback=32,rest_token=True] | 2.480 [2.043, 2.924] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | overall | rmse_h100 | itransformer[lookback=32] | 2.776 [2.434, 3.119] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | overall | rmse_h100 | lgbm | 2.090 [1.230, 2.949] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | overall | rmse_h100 | lstm[lookback=128] | 2.170 [1.235, 3.164] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | overall | rmse_h100 | transformer[lookback=32] | 1.986 [1.034, 3.373] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | overall | rmse_h25 | itransformer[lookback=32,rest_token=True] | 1.880 [1.483, 2.276] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | overall | rmse_h25 | itransformer[lookback=32] | 2.423 [1.665, 2.874] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | overall | rmse_h25 | lgbm | 2.197 [1.162, 3.707] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | overall | rmse_h25 | lstm[lookback=128] | 1.434 [1.108, 1.851] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | overall | rmse_h25 | transformer[lookback=32] | 1.452 [1.311, 1.626] |  |  | 4 | 5 | bb15ad85 |
| loco | start_points | overall | rmse_h50 | itransformer[lookback=32,rest_token=True] | 2.048 [1.800, 2.326] |  |  | 4 | 5 | 87c0ee93 |
| loco | start_points | overall | rmse_h50 | itransformer[lookback=32] | 2.293 [2.149, 2.448] |  |  | 4 | 5 | 0bd789f1 |
| loco | start_points | overall | rmse_h50 | lgbm | 2.439 [1.127, 4.288] |  |  | 4 | 5 | eb92ee9b |
| loco | start_points | overall | rmse_h50 | lstm[lookback=128] | 1.829 [0.834, 2.714] |  |  | 4 | 5 | f24ee787 |
| loco | start_points | overall | rmse_h50 | transformer[lookback=32] | 2.014 [1.178, 2.710] |  |  | 4 | 5 | bb15ad85 |

</details>

<details><summary>nasa_forecast (175 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | itransformer[lookback=64,rest_token=True] | 6.496 [4.981, 7.935] |  | 6.790 | 4 | 5 | 84b978b3 |
| loco | all | overall | rmse_h1 | itransformer[lookback=64] | 6.524 [5.034, 7.899] |  | 6.505 | 4 | 5 | 53eea59e |
| loco | all | overall | rmse_h1 | lgbm | 3.549 [1.667, 6.452] |  | 2.368 | 4 | 5 | 1287a5eb |
| loco | all | overall | rmse_h1 | lstm[lookback=64] | 4.174 [2.586, 5.762] |  | 6.541 | 4 | 5 | c585c752 |
| loco | all | overall | rmse_h1 | transformer[lookback=64] | 7.857 [4.997, 11.456] |  | 7.955 | 4 | 5 | c4909d46 |
| loco | all | overall | rmse_h10 | itransformer[lookback=64,rest_token=True] | 6.124 [4.777, 7.669] |  | 6.331 | 4 | 5 | 84b978b3 |
| loco | all | overall | rmse_h10 | itransformer[lookback=64] | 6.273 [4.840, 7.791] |  | 5.909 | 4 | 5 | 53eea59e |
| loco | all | overall | rmse_h10 | lgbm | 4.259 [2.557, 6.930] |  | 2.599 | 4 | 5 | 1287a5eb |
| loco | all | overall | rmse_h10 | lstm[lookback=64] | 4.123 [2.840, 5.406] |  | 5.257 | 4 | 5 | c585c752 |
| loco | all | overall | rmse_h10 | transformer[lookback=64] | 7.755 [5.062, 10.721] |  | 8.396 | 4 | 5 | c4909d46 |
| loco | all | overall | rmse_h100 | itransformer[lookback=64,rest_token=True] | 7.215 [4.580, 10.148] |  | 4.048 | 4 | 5 | 84b978b3 |
| loco | all | overall | rmse_h100 | itransformer[lookback=64] | 7.177 [4.484, 10.383] |  | 3.583 | 4 | 5 | 53eea59e |
| loco | all | overall | rmse_h100 | lgbm | 6.286 [2.518, 10.054] |  | 2.479 | 4 | 5 | 1287a5eb |
| loco | all | overall | rmse_h100 | lstm[lookback=64] | 7.341 [3.940, 11.102] |  | 4.806 | 4 | 5 | c585c752 |
| loco | all | overall | rmse_h100 | transformer[lookback=64] | 7.254 [4.747, 10.493] |  | 4.035 | 4 | 5 | c4909d46 |
| loco | all | overall | rmse_h25 | itransformer[lookback=64,rest_token=True] | 6.016 [4.588, 7.588] |  | 4.934 | 4 | 5 | 84b978b3 |
| loco | all | overall | rmse_h25 | itransformer[lookback=64] | 6.075 [4.264, 7.885] |  | 4.411 | 4 | 5 | 53eea59e |
| loco | all | overall | rmse_h25 | lgbm | 5.240 [3.269, 8.315] |  | 2.873 | 4 | 5 | 1287a5eb |
| loco | all | overall | rmse_h25 | lstm[lookback=64] | 5.229 [3.612, 7.202] |  | 5.417 | 4 | 5 | c585c752 |
| loco | all | overall | rmse_h25 | transformer[lookback=64] | 8.931 [6.535, 12.172] |  | 8.674 | 4 | 5 | c4909d46 |
| loco | all | overall | rmse_h50 | itransformer[lookback=64,rest_token=True] | 6.314 [4.670, 8.164] |  | 5.116 | 4 | 5 | 84b978b3 |
| loco | all | overall | rmse_h50 | itransformer[lookback=64] | 6.353 [4.596, 8.122] |  | 4.942 | 4 | 5 | 53eea59e |
| loco | all | overall | rmse_h50 | lgbm | 6.380 [3.555, 9.770] |  | 2.668 | 4 | 5 | 1287a5eb |
| loco | all | overall | rmse_h50 | lstm[lookback=64] | 6.593 [4.240, 9.933] |  | 5.689 | 4 | 5 | c585c752 |
| loco | all | overall | rmse_h50 | transformer[lookback=64] | 6.856 [4.440, 10.937] |  | 5.256 | 4 | 5 | c4909d46 |
| loco | start_points | fixed:30 | rmse_h1 | itransformer[lookback=64,rest_token=True] | 2.224 |  | 2.224 | 1 | 5 | c9d8bc54 |
| loco | start_points | fixed:30 | rmse_h1 | itransformer[lookback=64] | 1.853 |  | 1.853 | 1 | 5 | fb0c18b5 |
| loco | start_points | fixed:30 | rmse_h1 | lgbm | 1.570 |  | 1.570 | 1 | 5 | 5ab88038 |
| loco | start_points | fixed:30 | rmse_h1 | lstm[lookback=64] | 3.165 |  | 3.165 | 1 | 5 | fdb0ef80 |
| loco | start_points | fixed:30 | rmse_h1 | transformer[lookback=64] | 3.765 |  | 3.765 | 1 | 5 | 218e6c56 |
| loco | start_points | fixed:30 | rmse_h10 | itransformer[lookback=64,rest_token=True] | 3.278 [2.660, 3.896] |  | 3.751 | 4 | 5 | 84b978b3 |
| loco | start_points | fixed:30 | rmse_h10 | itransformer[lookback=64] | 4.438 [2.894, 6.000] |  | 2.458 | 4 | 5 | 53eea59e |
| loco | start_points | fixed:30 | rmse_h10 | lgbm | 4.218 [2.461, 5.974] |  | 1.725 | 4 | 5 | 1287a5eb |
| loco | start_points | fixed:30 | rmse_h10 | lstm[lookback=64] | 5.607 [4.380, 6.708] |  | 3.800 | 4 | 5 | c585c752 |
| loco | start_points | fixed:30 | rmse_h10 | transformer[lookback=64] | 6.789 [4.528, 8.790] |  | 3.330 | 4 | 5 | c4909d46 |
| loco | start_points | fixed:30 | rmse_h100 | itransformer[lookback=64,rest_token=True] | 5.975 [4.217, 8.210] |  | 4.237 | 4 | 5 | 84b978b3 |
| loco | start_points | fixed:30 | rmse_h100 | itransformer[lookback=64] | 5.856 [3.515, 8.453] |  | 3.988 | 4 | 5 | 53eea59e |
| loco | start_points | fixed:30 | rmse_h100 | lgbm | 4.951 [0.494, 9.408] |  | 0.257 | 4 | 5 | 1287a5eb |
| loco | start_points | fixed:30 | rmse_h100 | lstm[lookback=64] | 6.636 [4.947, 9.964] |  | 4.942 | 4 | 5 | c585c752 |
| loco | start_points | fixed:30 | rmse_h100 | transformer[lookback=64] | 6.782 [4.800, 9.251] |  | 4.153 | 4 | 5 | c4909d46 |
| loco | start_points | fixed:30 | rmse_h25 | itransformer[lookback=64,rest_token=True] | 6.544 [4.771, 8.317] |  | 4.715 | 4 | 5 | 84b978b3 |
| loco | start_points | fixed:30 | rmse_h25 | itransformer[lookback=64] | 5.780 [3.834, 7.759] |  | 3.138 | 4 | 5 | 53eea59e |
| loco | start_points | fixed:30 | rmse_h25 | lgbm | 4.870 [2.283, 7.457] |  | 1.547 | 4 | 5 | 1287a5eb |
| loco | start_points | fixed:30 | rmse_h25 | lstm[lookback=64] | 5.207 [2.996, 7.598] |  | 2.453 | 4 | 5 | c585c752 |
| loco | start_points | fixed:30 | rmse_h25 | transformer[lookback=64] | 7.291 [4.396, 10.187] |  | 2.839 | 4 | 5 | c4909d46 |
| loco | start_points | fixed:30 | rmse_h50 | itransformer[lookback=64,rest_token=True] | 4.010 [1.745, 7.003] |  | 1.226 | 4 | 5 | 84b978b3 |
| loco | start_points | fixed:30 | rmse_h50 | itransformer[lookback=64] | 3.885 [2.069, 6.735] |  | 2.031 | 4 | 5 | 53eea59e |
| loco | start_points | fixed:30 | rmse_h50 | lgbm | 6.090 [2.481, 8.977] |  | 0.917 | 4 | 5 | 1287a5eb |
| loco | start_points | fixed:30 | rmse_h50 | lstm[lookback=64] | 6.461 [3.581, 10.435] |  | 4.988 | 4 | 5 | c585c752 |
| loco | start_points | fixed:30 | rmse_h50 | transformer[lookback=64] | 5.592 [3.439, 9.341] |  | 3.167 | 4 | 5 | c4909d46 |
| loco | start_points | fixed:50 | rmse_h1 | itransformer[lookback=64,rest_token=True] | 6.327 [2.955, 10.178] |  | 12.416 | 4 | 5 | 84b978b3 |
| loco | start_points | fixed:50 | rmse_h1 | itransformer[lookback=64] | 7.073 [4.095, 10.148] |  | 12.107 | 4 | 5 | 53eea59e |
| loco | start_points | fixed:50 | rmse_h1 | lgbm | 2.099 [1.030, 3.006] |  | 1.963 | 4 | 5 | 1287a5eb |
| loco | start_points | fixed:50 | rmse_h1 | lstm[lookback=64] | 3.488 [2.261, 4.632] |  | 5.162 | 4 | 5 | c585c752 |
| loco | start_points | fixed:50 | rmse_h1 | transformer[lookback=64] | 5.128 [3.479, 7.035] |  | 3.043 | 4 | 5 | c4909d46 |
| loco | start_points | fixed:50 | rmse_h10 | itransformer[lookback=64,rest_token=True] | 5.979 [4.592, 7.951] |  | 8.989 | 4 | 5 | 84b978b3 |
| loco | start_points | fixed:50 | rmse_h10 | itransformer[lookback=64] | 6.226 [4.517, 7.884] |  | 8.422 | 4 | 5 | 53eea59e |
| loco | start_points | fixed:50 | rmse_h10 | lgbm | 3.564 [0.708, 6.420] |  | 0.036 | 4 | 5 | 1287a5eb |
| loco | start_points | fixed:50 | rmse_h10 | lstm[lookback=64] | 4.025 [2.371, 6.715] |  | 2.528 | 4 | 5 | c585c752 |
| loco | start_points | fixed:50 | rmse_h10 | transformer[lookback=64] | 6.161 [4.205, 8.732] |  | 6.119 | 4 | 5 | c4909d46 |
| loco | start_points | fixed:50 | rmse_h100 | itransformer[lookback=64,rest_token=True] | 7.882 [4.159, 12.345] |  |  | 3 | 5 | ca6dbfcd |
| loco | start_points | fixed:50 | rmse_h100 | itransformer[lookback=64] | 7.679 [5.080, 11.059] |  |  | 3 | 5 | c4611d38 |
| loco | start_points | fixed:50 | rmse_h100 | lgbm | 6.896 [1.085, 13.206] |  |  | 3 | 5 | 805e65a4 |
| loco | start_points | fixed:50 | rmse_h100 | lstm[lookback=64] | 7.933 [2.466, 13.687] |  |  | 3 | 5 | e69d4f5b |
| loco | start_points | fixed:50 | rmse_h100 | transformer[lookback=64] | 7.339 [4.204, 11.624] |  |  | 3 | 5 | 65ccf181 |
| loco | start_points | fixed:50 | rmse_h25 | itransformer[lookback=64,rest_token=True] | 6.023 [3.722, 9.120] |  | 10.819 | 4 | 5 | 84b978b3 |
| loco | start_points | fixed:50 | rmse_h25 | itransformer[lookback=64] | 5.622 [4.484, 6.601] |  | 6.934 | 4 | 5 | 53eea59e |
| loco | start_points | fixed:50 | rmse_h25 | lgbm | 4.311 [1.837, 7.909] |  | 2.054 | 4 | 5 | 1287a5eb |
| loco | start_points | fixed:50 | rmse_h25 | lstm[lookback=64] | 5.713 [2.744, 9.055] |  | 6.303 | 4 | 5 | c585c752 |
| loco | start_points | fixed:50 | rmse_h25 | transformer[lookback=64] | 7.571 [4.428, 11.904] |  | 6.850 | 4 | 5 | c4909d46 |
| loco | start_points | fixed:50 | rmse_h50 | itransformer[lookback=64,rest_token=True] | 6.523 [5.223, 8.155] |  | 9.024 | 4 | 5 | 84b978b3 |
| loco | start_points | fixed:50 | rmse_h50 | itransformer[lookback=64] | 5.192 [4.440, 6.104] |  | 4.674 | 4 | 5 | 53eea59e |
| loco | start_points | fixed:50 | rmse_h50 | lgbm | 5.616 [3.627, 8.086] |  | 4.327 | 4 | 5 | 1287a5eb |
| loco | start_points | fixed:50 | rmse_h50 | lstm[lookback=64] | 5.876 [2.274, 9.478] |  | 8.776 | 4 | 5 | c585c752 |
| loco | start_points | fixed:50 | rmse_h50 | transformer[lookback=64] | 5.655 [3.085, 9.599] |  | 3.604 | 4 | 5 | c4909d46 |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer[lookback=64,rest_token=True] | 4.678 [3.554, 6.385] |  | 3.290 | 4 | 5 | 84b978b3 |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer[lookback=64] | 4.026 [2.800, 5.250] |  | 2.009 | 4 | 5 | 53eea59e |
| loco | start_points | frac:0.3 | rmse_h1 | lgbm | 2.336 [0.959, 4.158] |  | 2.331 | 4 | 5 | 1287a5eb |
| loco | start_points | frac:0.3 | rmse_h1 | lstm[lookback=64] | 3.661 [2.563, 4.661] |  | 4.558 | 4 | 5 | c585c752 |
| loco | start_points | frac:0.3 | rmse_h1 | transformer[lookback=64] | 4.343 [3.810, 4.803] |  | 4.965 | 4 | 5 | c4909d46 |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer[lookback=64,rest_token=True] | 4.248 [2.554, 5.943] |  | 1.747 | 4 | 5 | 84b978b3 |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer[lookback=64] | 4.498 [2.824, 6.279] |  | 2.255 | 4 | 5 | 53eea59e |
| loco | start_points | frac:0.3 | rmse_h10 | lgbm | 3.158 [1.758, 4.687] |  | 1.194 | 4 | 5 | 1287a5eb |
| loco | start_points | frac:0.3 | rmse_h10 | lstm[lookback=64] | 4.065 [2.876, 5.707] |  | 3.943 | 4 | 5 | c585c752 |
| loco | start_points | frac:0.3 | rmse_h10 | transformer[lookback=64] | 4.494 [3.723, 5.506] |  | 3.478 | 4 | 5 | c4909d46 |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer[lookback=64,rest_token=True] | 6.518 [4.861, 8.036] |  | 3.863 | 4 | 5 | 84b978b3 |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer[lookback=64] | 6.018 [4.007, 8.029] |  | 3.145 | 4 | 5 | 53eea59e |
| loco | start_points | frac:0.3 | rmse_h100 | lgbm | 5.580 [2.159, 9.002] |  | 3.913 | 4 | 5 | 1287a5eb |
| loco | start_points | frac:0.3 | rmse_h100 | lstm[lookback=64] | 7.132 [3.357, 10.906] |  | 5.512 | 4 | 5 | c585c752 |
| loco | start_points | frac:0.3 | rmse_h100 | transformer[lookback=64] | 6.657 [4.368, 9.786] |  | 3.650 | 4 | 5 | c4909d46 |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer[lookback=64,rest_token=True] | 4.018 [3.120, 5.458] |  | 6.142 | 4 | 5 | 84b978b3 |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer[lookback=64] | 3.721 [3.163, 4.375] |  | 3.493 | 4 | 5 | 53eea59e |
| loco | start_points | frac:0.3 | rmse_h25 | lgbm | 5.378 [3.181, 6.792] |  | 6.550 | 4 | 5 | 1287a5eb |
| loco | start_points | frac:0.3 | rmse_h25 | lstm[lookback=64] | 6.486 [4.281, 8.690] |  | 8.471 | 4 | 5 | c585c752 |
| loco | start_points | frac:0.3 | rmse_h25 | transformer[lookback=64] | 7.435 [4.855, 10.016] |  | 4.852 | 4 | 5 | c4909d46 |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer[lookback=64,rest_token=True] | 4.373 [3.290, 6.324] |  | 3.282 | 4 | 5 | 84b978b3 |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer[lookback=64] | 5.246 [3.902, 7.017] |  | 5.147 | 4 | 5 | 53eea59e |
| loco | start_points | frac:0.3 | rmse_h50 | lgbm | 5.763 [2.725, 8.142] |  | 1.464 | 4 | 5 | 1287a5eb |
| loco | start_points | frac:0.3 | rmse_h50 | lstm[lookback=64] | 5.908 [2.771, 10.528] |  | 5.206 | 4 | 5 | c585c752 |
| loco | start_points | frac:0.3 | rmse_h50 | transformer[lookback=64] | 5.990 [3.254, 10.659] |  | 2.892 | 4 | 5 | c4909d46 |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer[lookback=64,rest_token=True] | 4.436 [2.359, 5.549] |  | 2.359 | 3 | 5 | 0568f3b7 |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer[lookback=64] | 4.072 [1.981, 5.250] |  | 1.981 | 3 | 5 | f2886535 |
| loco | start_points | frac:0.5 | rmse_h1 | lgbm | 2.757 [0.379, 3.967] |  | 3.926 | 3 | 5 | 3ce47d7e |
| loco | start_points | frac:0.5 | rmse_h1 | lstm[lookback=64] | 2.340 [1.462, 2.822] |  | 2.822 | 3 | 5 | 95fd6c84 |
| loco | start_points | frac:0.5 | rmse_h1 | transformer[lookback=64] | 3.131 [2.470, 3.931] |  | 2.993 | 3 | 5 | a525d7fe |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer[lookback=64,rest_token=True] | 3.811 [2.618, 5.185] |  | 2.420 | 4 | 5 | 84b978b3 |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer[lookback=64] | 3.186 [1.787, 4.631] |  | 1.272 | 4 | 5 | 53eea59e |
| loco | start_points | frac:0.5 | rmse_h10 | lgbm | 4.354 [1.799, 5.934] |  | 5.840 | 4 | 5 | 1287a5eb |
| loco | start_points | frac:0.5 | rmse_h10 | lstm[lookback=64] | 3.515 [1.448, 6.002] |  | 3.664 | 4 | 5 | c585c752 |
| loco | start_points | frac:0.5 | rmse_h10 | transformer[lookback=64] | 4.190 [2.711, 5.627] |  | 4.690 | 4 | 5 | c4909d46 |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer[lookback=64,rest_token=True] | 7.373 [3.094, 9.534] |  |  | 3 | 5 | ca6dbfcd |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer[lookback=64] | 7.866 [3.359, 10.298] |  |  | 3 | 5 | c4611d38 |
| loco | start_points | frac:0.5 | rmse_h100 | lgbm | 5.442 [0.465, 10.783] |  |  | 3 | 5 | 805e65a4 |
| loco | start_points | frac:0.5 | rmse_h100 | lstm[lookback=64] | 6.617 [1.797, 11.635] |  |  | 3 | 5 | e69d4f5b |
| loco | start_points | frac:0.5 | rmse_h100 | transformer[lookback=64] | 6.682 [3.884, 10.385] |  |  | 3 | 5 | 65ccf181 |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer[lookback=64,rest_token=True] | 4.104 [2.219, 5.288] |  | 1.350 | 4 | 5 | 84b978b3 |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer[lookback=64] | 4.568 [3.064, 5.501] |  | 2.275 | 4 | 5 | 53eea59e |
| loco | start_points | frac:0.5 | rmse_h25 | lgbm | 3.811 [1.650, 6.110] |  | 1.796 | 4 | 5 | 1287a5eb |
| loco | start_points | frac:0.5 | rmse_h25 | lstm[lookback=64] | 4.393 [2.056, 7.250] |  | 4.508 | 4 | 5 | c585c752 |
| loco | start_points | frac:0.5 | rmse_h25 | transformer[lookback=64] | 5.924 [3.101, 9.207] |  | 5.286 | 4 | 5 | c4909d46 |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer[lookback=64,rest_token=True] | 4.881 [2.590, 7.173] |  | 2.549 | 4 | 5 | 84b978b3 |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer[lookback=64] | 5.939 [3.829, 8.004] |  | 5.219 | 4 | 5 | 53eea59e |
| loco | start_points | frac:0.5 | rmse_h50 | lgbm | 4.652 [1.424, 8.163] |  | 0.051 | 4 | 5 | 1287a5eb |
| loco | start_points | frac:0.5 | rmse_h50 | lstm[lookback=64] | 5.769 [2.369, 10.005] |  | 6.086 | 4 | 5 | c585c752 |
| loco | start_points | frac:0.5 | rmse_h50 | transformer[lookback=64] | 5.141 [2.949, 9.145] |  | 2.945 | 4 | 5 | c4909d46 |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer[lookback=64,rest_token=True] | 4.204 [2.333, 6.770] |  |  | 3 | 5 | ca6dbfcd |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer[lookback=64] | 4.335 [3.027, 5.466] |  |  | 3 | 5 | c4611d38 |
| loco | start_points | frac:0.7 | rmse_h1 | lgbm | 1.739 [0.756, 2.580] |  |  | 3 | 5 | 805e65a4 |
| loco | start_points | frac:0.7 | rmse_h1 | lstm[lookback=64] | 1.999 [1.139, 3.161] |  |  | 3 | 5 | e69d4f5b |
| loco | start_points | frac:0.7 | rmse_h1 | transformer[lookback=64] | 4.376 [2.006, 8.580] |  |  | 3 | 5 | 65ccf181 |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer[lookback=64,rest_token=True] | 4.245 [3.094, 5.952] |  | 6.811 | 4 | 5 | 84b978b3 |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer[lookback=64] | 5.385 [3.399, 7.580] |  | 8.771 | 4 | 5 | 53eea59e |
| loco | start_points | frac:0.7 | rmse_h10 | lgbm | 2.407 [1.170, 4.182] |  | 0.871 | 4 | 5 | 1287a5eb |
| loco | start_points | frac:0.7 | rmse_h10 | lstm[lookback=64] | 3.069 [1.582, 4.855] |  | 3.191 | 4 | 5 | c585c752 |
| loco | start_points | frac:0.7 | rmse_h10 | transformer[lookback=64] | 5.312 [2.470, 8.153] |  | 7.003 | 4 | 5 | c4909d46 |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer[lookback=64,rest_token=True] | 9.979 |  |  | 1 | 5 | 022270ca |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer[lookback=64] | 11.010 |  |  | 1 | 5 | d17f341d |
| loco | start_points | frac:0.7 | rmse_h100 | lgbm | 12.446 |  |  | 1 | 5 | 9cb4b137 |
| loco | start_points | frac:0.7 | rmse_h100 | lstm[lookback=64] | 12.802 |  |  | 1 | 5 | 110cad56 |
| loco | start_points | frac:0.7 | rmse_h100 | transformer[lookback=64] | 11.384 |  |  | 1 | 5 | 86348f7b |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer[lookback=64,rest_token=True] | 5.358 [3.651, 6.610] |  | 5.620 | 4 | 5 | 84b978b3 |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer[lookback=64] | 5.861 [3.899, 7.971] |  | 5.035 | 4 | 5 | 53eea59e |
| loco | start_points | frac:0.7 | rmse_h25 | lgbm | 3.801 [1.284, 7.530] |  | 2.022 | 4 | 5 | 1287a5eb |
| loco | start_points | frac:0.7 | rmse_h25 | lstm[lookback=64] | 4.922 [1.957, 8.893] |  | 4.875 | 4 | 5 | c585c752 |
| loco | start_points | frac:0.7 | rmse_h25 | transformer[lookback=64] | 8.122 [4.330, 12.025] |  | 9.661 | 4 | 5 | c4909d46 |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer[lookback=64,rest_token=True] | 5.029 [3.612, 6.418] |  | 6.903 | 4 | 5 | 84b978b3 |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer[lookback=64] | 4.791 [3.871, 5.698] |  | 4.479 | 4 | 5 | 53eea59e |
| loco | start_points | frac:0.7 | rmse_h50 | lgbm | 3.922 [1.612, 5.794] |  | 4.058 | 4 | 5 | 1287a5eb |
| loco | start_points | frac:0.7 | rmse_h50 | lstm[lookback=64] | 5.112 [2.360, 7.669] |  | 5.422 | 4 | 5 | c585c752 |
| loco | start_points | frac:0.7 | rmse_h50 | transformer[lookback=64] | 5.021 [3.001, 8.367] |  | 3.386 | 4 | 5 | c4909d46 |
| loco | start_points | overall | rmse_h1 | itransformer[lookback=64,rest_token=True] | 5.510 [4.175, 6.844] |  | 6.797 | 4 | 5 | 84b978b3 |
| loco | start_points | overall | rmse_h1 | itransformer[lookback=64] | 5.504 [4.692, 6.315] |  | 6.379 | 4 | 5 | 53eea59e |
| loco | start_points | overall | rmse_h1 | lgbm | 2.273 [1.052, 3.391] |  | 2.606 | 4 | 5 | 1287a5eb |
| loco | start_points | overall | rmse_h1 | lstm[lookback=64] | 3.359 [2.303, 4.366] |  | 4.593 | 4 | 5 | c585c752 |
| loco | start_points | overall | rmse_h1 | transformer[lookback=64] | 4.834 [3.688, 6.518] |  | 4.237 | 4 | 5 | c4909d46 |
| loco | start_points | overall | rmse_h10 | itransformer[lookback=64,rest_token=True] | 5.010 [4.355, 5.540] |  | 5.710 | 4 | 5 | 84b978b3 |
| loco | start_points | overall | rmse_h10 | itransformer[lookback=64] | 5.619 [5.242, 5.995] |  | 5.995 | 4 | 5 | 53eea59e |
| loco | start_points | overall | rmse_h10 | lgbm | 3.925 [2.496, 5.354] |  | 2.802 | 4 | 5 | 1287a5eb |
| loco | start_points | overall | rmse_h10 | lstm[lookback=64] | 4.512 [3.370, 6.268] |  | 3.862 | 4 | 5 | c585c752 |
| loco | start_points | overall | rmse_h10 | transformer[lookback=64] | 6.106 [5.322, 7.389] |  | 5.562 | 4 | 5 | c4909d46 |
| loco | start_points | overall | rmse_h100 | itransformer[lookback=64,rest_token=True] | 7.098 [5.083, 9.113] |  | 4.598 | 4 | 5 | 84b978b3 |
| loco | start_points | overall | rmse_h100 | itransformer[lookback=64] | 6.888 [4.548, 9.228] |  | 3.658 | 4 | 5 | 53eea59e |
| loco | start_points | overall | rmse_h100 | lgbm | 5.492 [1.748, 9.350] |  | 2.773 | 4 | 5 | 1287a5eb |
| loco | start_points | overall | rmse_h100 | lstm[lookback=64] | 7.217 [4.396, 10.645] |  | 5.539 | 4 | 5 | c585c752 |
| loco | start_points | overall | rmse_h100 | transformer[lookback=64] | 6.649 [4.500, 9.565] |  | 3.983 | 4 | 5 | c4909d46 |
| loco | start_points | overall | rmse_h25 | itransformer[lookback=64,rest_token=True] | 6.067 [5.471, 6.663] |  | 6.938 | 4 | 5 | 84b978b3 |
| loco | start_points | overall | rmse_h25 | itransformer[lookback=64] | 5.754 [5.255, 6.158] |  | 5.020 | 4 | 5 | 53eea59e |
| loco | start_points | overall | rmse_h25 | lgbm | 4.788 [2.873, 6.967] |  | 3.371 | 4 | 5 | 1287a5eb |
| loco | start_points | overall | rmse_h25 | lstm[lookback=64] | 5.923 [3.793, 8.364] |  | 6.240 | 4 | 5 | c585c752 |
| loco | start_points | overall | rmse_h25 | transformer[lookback=64] | 7.808 [5.552, 10.785] |  | 6.688 | 4 | 5 | c4909d46 |
| loco | start_points | overall | rmse_h50 | itransformer[lookback=64,rest_token=True] | 5.568 [4.457, 6.682] |  | 5.681 | 4 | 5 | 84b978b3 |
| loco | start_points | overall | rmse_h50 | itransformer[lookback=64] | 5.521 [4.348, 7.015] |  | 5.021 | 4 | 5 | 53eea59e |
| loco | start_points | overall | rmse_h50 | lgbm | 5.545 [3.575, 7.807] |  | 2.763 | 4 | 5 | 1287a5eb |
| loco | start_points | overall | rmse_h50 | lstm[lookback=64] | 6.204 [3.287, 9.689] |  | 6.684 | 4 | 5 | c585c752 |
| loco | start_points | overall | rmse_h50 | transformer[lookback=64] | 5.776 [3.659, 9.558] |  | 3.561 | 4 | 5 | c4909d46 |

</details>
