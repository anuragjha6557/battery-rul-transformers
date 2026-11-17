# Benchmark tables: benchmark

- Protocol version: 1.1
- Git SHA: 7086afc90e
- Seeds: 5  |  unit runs: 1620
- Note: n = 4 cells per NASA/CALCE dataset, so the 95 % cluster-bootstrap CI is wide by construction. Toyota rows are over test cells (test1 / test2 separately) with a cell-level bootstrap CI and a Holm-adjusted Wilcoxon p vs the best baseline. All metrics are computed per cell from the logged predictions.

## Headline (kind = overall; RMSE in %SOH, RUL MAE in cycles)

### calce_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | dlinear | 2.938 [2.766, 3.110] | 0/4 cells, 8/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | all | overall | rmse_h1 | elasticnet | 1.912 [1.825, 1.999] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | all | overall | rmse_h1 | gru | 1.936 [1.838, 2.034] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | all | overall | rmse_h1 | itransformer | 1.966 [1.854, 2.083] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | all | overall | rmse_h1 | itransformer_sc | 2.087 [1.924, 2.263] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | all | overall | rmse_h1 | last_slope | 2.686 [2.506, 2.869] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | all | overall | rmse_h1 | lgbm | 1.960 [1.845, 2.075] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | all | overall | rmse_h1 | lstm | 1.936 [1.831, 2.041] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | all | overall | rmse_h1 | nlinear | 2.475 [2.284, 2.662] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | all | overall | rmse_h1 | patchtst | 1.981 [1.886, 2.081] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | all | overall | rmse_h1 | persistence | 2.606 [2.429, 2.783] |  |  | 4 | 5 | 5c5d170c |
| loco | all | overall | rmse_h1 | rlinear | 2.404 [2.230, 2.573] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | all | overall | rmse_h1 | transformer | 2.323 [2.141, 2.524] | 4/4 cells, 19/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | all | overall | rmse_h10 | dlinear | 3.643 [3.593, 3.693] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | all | overall | rmse_h10 | elasticnet | 2.333 [2.263, 2.411] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | all | overall | rmse_h10 | gru | 2.320 [2.210, 2.414] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | all | overall | rmse_h10 | itransformer | 2.306 [2.219, 2.401] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | all | overall | rmse_h10 | itransformer_sc | 2.334 [2.267, 2.426] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | all | overall | rmse_h10 | last_slope | 4.266 [4.097, 4.435] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | all | overall | rmse_h10 | lgbm | 2.303 [2.240, 2.382] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | all | overall | rmse_h10 | lstm | 2.323 [2.202, 2.444] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | all | overall | rmse_h10 | nlinear | 2.546 [2.485, 2.606] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | all | overall | rmse_h10 | patchtst | 2.367 [2.316, 2.438] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | all | overall | rmse_h10 | persistence | 3.071 [3.003, 3.139] |  |  | 4 | 5 | 5c5d170c |
| loco | all | overall | rmse_h10 | rlinear | 2.516 [2.456, 2.566] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | all | overall | rmse_h10 | transformer | 2.600 [2.429, 2.731] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | all | overall | rmse_h50 | dlinear | 5.791 [5.671, 5.937] | 4/4 cells, 16/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | all | overall | rmse_h50 | elasticnet | 3.926 [3.081, 5.023] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | all | overall | rmse_h50 | gru | 3.307 [2.631, 3.915] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | all | overall | rmse_h50 | itransformer | 3.133 [2.873, 3.393] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | all | overall | rmse_h50 | itransformer_sc | 3.090 [2.805, 3.480] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | all | overall | rmse_h50 | last_slope | 13.491 [12.984, 13.882] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | all | overall | rmse_h50 | lgbm | 2.840 [2.521, 3.243] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | all | overall | rmse_h50 | lstm | 3.119 [2.595, 3.528] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | all | overall | rmse_h50 | nlinear | 4.194 [3.942, 4.447] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | all | overall | rmse_h50 | patchtst | 3.796 [3.521, 4.071] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | all | overall | rmse_h50 | persistence | 6.278 [5.955, 6.519] |  |  | 4 | 5 | 5c5d170c |
| loco | all | overall | rmse_h50 | rlinear | 4.147 [3.886, 4.408] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | all | overall | rmse_h50 | transformer | 3.557 [2.796, 4.400] | 4/4 cells, 19/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | overall | rmse_h1 | dlinear | 1.782 [1.660, 1.940] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | overall | rmse_h1 | elasticnet | 0.443 [0.367, 0.593] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | overall | rmse_h1 | gru | 0.385 [0.232, 0.538] | 2/4 cells, 9/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | overall | rmse_h1 | itransformer | 0.394 [0.198, 0.589] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | overall | rmse_h1 | itransformer_sc | 0.388 [0.199, 0.577] | 3/4 cells, 14/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | overall | rmse_h1 | last_slope | 0.455 [0.240, 0.669] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | overall | rmse_h1 | lgbm | 0.355 [0.160, 0.550] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | overall | rmse_h1 | lstm | 0.411 [0.197, 0.625] | 1/4 cells, 8/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | overall | rmse_h1 | nlinear | 0.388 [0.179, 0.598] | 3/4 cells, 13/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | overall | rmse_h1 | patchtst | 0.422 [0.243, 0.602] | 2/4 cells, 9/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | overall | rmse_h1 | persistence | 0.397 [0.177, 0.617] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | overall | rmse_h1 | rlinear | 0.397 [0.187, 0.607] | 2/4 cells, 11/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | overall | rmse_h1 | transformer | 0.531 [0.370, 0.660] | 0/4 cells, 4/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | overall | rmse_h10 | dlinear | 2.329 [2.203, 2.516] | 0/4 cells, 4/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | overall | rmse_h10 | elasticnet | 1.152 [0.786, 1.794] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | overall | rmse_h10 | gru | 0.994 [0.540, 1.570] | 4/4 cells, 19/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | overall | rmse_h10 | itransformer | 1.049 [0.716, 1.546] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | overall | rmse_h10 | itransformer_sc | 1.046 [0.706, 1.558] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | overall | rmse_h10 | last_slope | 2.474 [2.053, 3.110] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | overall | rmse_h10 | lgbm | 0.991 [0.502, 1.671] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | overall | rmse_h10 | lstm | 1.061 [0.601, 1.694] | 3/4 cells, 16/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | overall | rmse_h10 | nlinear | 0.984 [0.573, 1.613] | 4/4 cells, 18/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | overall | rmse_h10 | patchtst | 1.010 [0.695, 1.582] | 4/4 cells, 19/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | overall | rmse_h10 | persistence | 1.332 [1.082, 1.703] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | overall | rmse_h10 | rlinear | 0.992 [0.625, 1.571] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | overall | rmse_h10 | transformer | 1.062 [0.753, 1.556] | 4/4 cells, 18/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | overall | rmse_h50 | dlinear | 2.621 [2.272, 2.890] | 0/4 cells, 7/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | overall | rmse_h50 | elasticnet | 2.314 [1.273, 3.356] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | overall | rmse_h50 | gru | 1.799 [1.111, 2.286] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | overall | rmse_h50 | itransformer | 1.492 [0.997, 2.046] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | overall | rmse_h50 | itransformer_sc | 1.489 [1.031, 2.007] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | overall | rmse_h50 | last_slope | 7.343 [6.361, 8.324] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | overall | rmse_h50 | lgbm | 1.496 [0.956, 2.036] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | overall | rmse_h50 | lstm | 1.668 [1.065, 2.137] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | overall | rmse_h50 | nlinear | 1.773 [1.163, 2.684] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | overall | rmse_h50 | patchtst | 1.638 [1.038, 2.538] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | overall | rmse_h50 | persistence | 1.506 [1.020, 1.989] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | overall | rmse_h50 | rlinear | 1.750 [1.240, 2.648] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | overall | rmse_h50 | transformer | 1.852 [1.266, 2.326] | 1/4 cells, 6/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |

### calce_rul

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rul_mae | dlinear | 129.127 [123.850, 134.697] |  |  | 4 | 5 | 2954d2ac |
| loco | all | overall | rul_mae | elasticnet | 155.562 [81.341, 232.171] |  |  | 4 | 5 | 96e56f24 |
| loco | all | overall | rul_mae | gru | 85.032 [62.752, 107.312] |  |  | 4 | 5 | 800a470b |
| loco | all | overall | rul_mae | itransformer | 68.193 [40.047, 100.169] |  |  | 4 | 5 | cad19238 |
| loco | all | overall | rul_mae | itransformer_sc | 67.558 [42.668, 102.179] |  |  | 4 | 5 | 8125fe8a |
| loco | all | overall | rul_mae | lgbm | 74.731 [53.242, 96.522] |  |  | 4 | 5 | c2305071 |
| loco | all | overall | rul_mae | lstm | 72.319 [50.230, 101.873] |  |  | 4 | 5 | 6c1ef016 |
| loco | all | overall | rul_mae | nlinear | 127.936 [124.783, 132.629] |  |  | 4 | 5 | 119d8ef1 |
| loco | all | overall | rul_mae | patchtst | 110.910 [97.504, 121.278] |  |  | 4 | 5 | 65d9f648 |
| loco | all | overall | rul_mae | rlinear | 179.443 [163.112, 198.825] |  |  | 4 | 5 | bdad0aa4 |
| loco | all | overall | rul_mae | transformer | 83.204 [52.577, 113.832] |  |  | 4 | 5 | b001f101 |
| loco | start_points | overall | rul_mae | dlinear | 98.738 [70.053, 122.669] |  |  | 4 | 5 | 2954d2ac |
| loco | start_points | overall | rul_mae | elasticnet | 136.150 [60.142, 235.394] |  |  | 4 | 5 | 96e56f24 |
| loco | start_points | overall | rul_mae | gru | 77.916 [57.871, 111.354] |  |  | 4 | 5 | 800a470b |
| loco | start_points | overall | rul_mae | itransformer | 76.607 [43.841, 116.139] |  |  | 4 | 5 | cad19238 |
| loco | start_points | overall | rul_mae | itransformer_sc | 72.985 [38.624, 111.943] |  |  | 4 | 5 | 8125fe8a |
| loco | start_points | overall | rul_mae | lgbm | 82.096 [61.527, 110.784] |  |  | 4 | 5 | c2305071 |
| loco | start_points | overall | rul_mae | lstm | 80.063 [50.396, 113.203] |  |  | 4 | 5 | 6c1ef016 |
| loco | start_points | overall | rul_mae | nlinear | 103.996 [70.666, 131.870] |  |  | 4 | 5 | 119d8ef1 |
| loco | start_points | overall | rul_mae | patchtst | 91.477 [76.484, 106.470] |  |  | 4 | 5 | 65d9f648 |
| loco | start_points | overall | rul_mae | rlinear | 178.077 [153.136, 203.017] |  |  | 4 | 5 | bdad0aa4 |
| loco | start_points | overall | rul_mae | transformer | 80.005 [49.439, 136.511] |  |  | 4 | 5 | b001f101 |

### calce_soh

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse | dlinear | 2.492 [2.307, 2.671] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 3160ba54 |
| loco | all | overall | rmse | elasticnet | 0.658 [0.575, 0.766] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 3ffdca0f |
| loco | all | overall | rmse | gru | 1.712 [1.536, 1.921] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 4604bc09 |
| loco | all | overall | rmse | itransformer | 1.256 [1.212, 1.304] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 0b237c08 |
| loco | all | overall | rmse | itransformer_sc | 1.269 [1.201, 1.338] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 2d772b8f |
| loco | all | overall | rmse | lgbm | 1.193 [1.104, 1.317] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 95b19ba2 |
| loco | all | overall | rmse | lstm | 1.622 [1.409, 1.835] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) |  | 4 | 5 | b7364c34 |
| loco | all | overall | rmse | nlinear | 2.431 [2.243, 2.600] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 65662866 |
| loco | all | overall | rmse | patchtst | 1.957 [1.879, 2.037] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 3bd1f9b9 |
| loco | all | overall | rmse | prev_soh | 2.606 [2.429, 2.783] |  |  | 4 | 5 | a4feb20f |
| loco | all | overall | rmse | rlinear | 2.512 [2.340, 2.690] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 69bff78f |
| loco | all | overall | rmse | transformer | 1.760 [1.637, 1.882] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) |  | 4 | 5 | cb5b78e5 |
| loco | start_points | overall | rmse | dlinear | 0.362 [0.243, 0.481] | 1/4 cells, 5/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 3160ba54 |
| loco | start_points | overall | rmse | elasticnet | 0.315 [0.219, 0.419] | 2/4 cells, 10/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 3ffdca0f |
| loco | start_points | overall | rmse | gru | 0.366 [0.231, 0.500] | 2/4 cells, 9/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 4604bc09 |
| loco | start_points | overall | rmse | itransformer | 0.192 [0.106, 0.279] | 4/4 cells, 18/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 0b237c08 |
| loco | start_points | overall | rmse | itransformer_sc | 0.235 [0.145, 0.324] | 3/4 cells, 18/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 2d772b8f |
| loco | start_points | overall | rmse | lgbm | 0.242 [0.124, 0.342] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 95b19ba2 |
| loco | start_points | overall | rmse | lstm | 0.407 [0.258, 0.516] | 2/4 cells, 7/20 cell-seeds (vs prev_soh) |  | 4 | 5 | b7364c34 |
| loco | start_points | overall | rmse | nlinear | 0.368 [0.263, 0.472] | 2/4 cells, 11/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 65662866 |
| loco | start_points | overall | rmse | patchtst | 0.310 [0.166, 0.438] | 3/4 cells, 17/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 3bd1f9b9 |
| loco | start_points | overall | rmse | prev_soh | 0.359 [0.261, 0.456] |  |  | 4 | 5 | a4feb20f |
| loco | start_points | overall | rmse | rlinear | 0.349 [0.239, 0.459] | 2/4 cells, 10/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 69bff78f |
| loco | start_points | overall | rmse | transformer | 0.391 [0.278, 0.487] | 0/4 cells, 6/20 cell-seeds (vs prev_soh) |  | 4 | 5 | cb5b78e5 |

### nasa_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | dlinear | 3.641 [3.606, 3.688] | 0/4 cells, 0/20 cell-seeds (vs persistence) | 3.627 | 4 | 5 | 3b67b415 |
| loco | all | overall | rmse_h1 | elasticnet | 0.945 [0.707, 1.183] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 1.228 | 4 | 5 | e1ff5d55 |
| loco | all | overall | rmse_h1 | gru | 2.279 [1.787, 2.772] | 0/4 cells, 0/20 cell-seeds (vs persistence) | 3.030 | 4 | 5 | 9731ae77 |
| loco | all | overall | rmse_h1 | itransformer | 0.915 [0.660, 1.171] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 1.217 | 4 | 5 | 9dedaedf |
| loco | all | overall | rmse_h1 | itransformer_sc | 0.929 [0.681, 1.176] | 4/4 cells, 17/20 cell-seeds (vs persistence) | 1.222 | 4 | 5 | e5cc9a22 |
| loco | all | overall | rmse_h1 | last_slope | 0.992 [0.715, 1.269] | 0/4 cells, 0/20 cell-seeds (vs persistence) | 1.301 | 4 | 5 | 7a0d4ec4 |
| loco | all | overall | rmse_h1 | lgbm | 0.938 [0.700, 1.177] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 1.211 | 4 | 5 | acedf5f4 |
| loco | all | overall | rmse_h1 | lstm | 1.919 [1.475, 2.363] | 0/4 cells, 0/20 cell-seeds (vs persistence) | 2.419 | 4 | 5 | 5494788a |
| loco | all | overall | rmse_h1 | nlinear | 0.948 [0.706, 1.191] | 3/4 cells, 12/20 cell-seeds (vs persistence) | 1.227 | 4 | 5 | b4ecdb12 |
| loco | all | overall | rmse_h1 | patchtst | 0.908 [0.651, 1.165] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 1.217 | 4 | 5 | d75a14c6 |
| loco | all | overall | rmse_h1 | persistence | 0.955 [0.697, 1.213] |  | 1.245 | 4 | 5 | a26a213d |
| loco | all | overall | rmse_h1 | rlinear | 0.959 [0.700, 1.217] | 0/4 cells, 8/20 cell-seeds (vs persistence) | 1.246 | 4 | 5 | 78bc3e35 |
| loco | all | overall | rmse_h1 | transformer | 2.761 [1.698, 4.062] | 0/4 cells, 0/20 cell-seeds (vs persistence) | 4.628 | 4 | 5 | 19b71fc1 |
| loco | all | overall | rmse_h10 | dlinear | 6.802 [6.386, 7.217] | 0/4 cells, 0/20 cell-seeds (vs persistence) | 7.046 | 4 | 5 | 3b67b415 |
| loco | all | overall | rmse_h10 | elasticnet | 2.821 [1.604, 4.037] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 3.630 | 4 | 5 | e1ff5d55 |
| loco | all | overall | rmse_h10 | gru | 2.921 [2.175, 4.002] | 2/4 cells, 8/20 cell-seeds (vs persistence) | 2.767 | 4 | 5 | 9731ae77 |
| loco | all | overall | rmse_h10 | itransformer | 1.732 [1.081, 2.384] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 2.600 | 4 | 5 | 9dedaedf |
| loco | all | overall | rmse_h10 | itransformer_sc | 1.801 [1.205, 2.397] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 2.563 | 4 | 5 | e5cc9a22 |
| loco | all | overall | rmse_h10 | last_slope | 2.986 [2.037, 3.934] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 3.895 | 4 | 5 | 7a0d4ec4 |
| loco | all | overall | rmse_h10 | lgbm | 1.805 [1.302, 2.309] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 2.347 | 4 | 5 | acedf5f4 |
| loco | all | overall | rmse_h10 | lstm | 2.703 [2.283, 3.394] | 2/4 cells, 13/20 cell-seeds (vs persistence) | 2.491 | 4 | 5 | 5494788a |
| loco | all | overall | rmse_h10 | nlinear | 1.921 [1.390, 2.451] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 2.576 | 4 | 5 | b4ecdb12 |
| loco | all | overall | rmse_h10 | patchtst | 1.726 [1.121, 2.332] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 2.515 | 4 | 5 | d75a14c6 |
| loco | all | overall | rmse_h10 | persistence | 2.737 [2.186, 3.288] |  | 3.153 | 4 | 5 | a26a213d |
| loco | all | overall | rmse_h10 | rlinear | 2.076 [1.425, 2.728] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 2.857 | 4 | 5 | 78bc3e35 |
| loco | all | overall | rmse_h10 | transformer | 4.143 [2.826, 6.087] | 0/4 cells, 6/20 cell-seeds (vs persistence) | 7.085 | 4 | 5 | 19b71fc1 |
| loco | all | overall | rmse_h50 | dlinear | 11.250 [10.299, 12.159] | 2/4 cells, 12/20 cell-seeds (vs persistence) | 11.168 | 4 | 5 | 3b67b415 |
| loco | all | overall | rmse_h50 | elasticnet | 5.321 [3.447, 7.988] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 4.946 | 4 | 5 | e1ff5d55 |
| loco | all | overall | rmse_h50 | gru | 4.409 [3.333, 5.745] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.657 | 4 | 5 | 9731ae77 |
| loco | all | overall | rmse_h50 | itransformer | 5.378 [5.169, 5.574] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 5.322 | 4 | 5 | 9dedaedf |
| loco | all | overall | rmse_h50 | itransformer_sc | 4.052 [3.721, 4.328] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.563 | 4 | 5 | e5cc9a22 |
| loco | all | overall | rmse_h50 | last_slope | 12.164 [8.884, 15.444] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 14.476 | 4 | 5 | 7a0d4ec4 |
| loco | all | overall | rmse_h50 | lgbm | 3.238 [2.423, 4.261] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.065 | 4 | 5 | acedf5f4 |
| loco | all | overall | rmse_h50 | lstm | 3.577 [3.104, 4.415] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.141 | 4 | 5 | 5494788a |
| loco | all | overall | rmse_h50 | nlinear | 3.461 [2.715, 4.395] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.087 | 4 | 5 | b4ecdb12 |
| loco | all | overall | rmse_h50 | patchtst | 4.020 [2.930, 5.537] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.560 | 4 | 5 | d75a14c6 |
| loco | all | overall | rmse_h50 | persistence | 11.211 [9.697, 12.759] |  | 11.258 | 4 | 5 | a26a213d |
| loco | all | overall | rmse_h50 | rlinear | 6.700 [6.010, 7.359] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 6.835 | 4 | 5 | 78bc3e35 |
| loco | all | overall | rmse_h50 | transformer | 5.448 [4.164, 6.496] | 4/4 cells, 19/20 cell-seeds (vs persistence) | 5.462 | 4 | 5 | 19b71fc1 |
| loco | start_points | overall | rmse_h1 | dlinear | 4.010 [3.844, 4.176] | 0/4 cells, 2/20 cell-seeds (vs persistence) | 4.110 | 4 | 5 | 3b67b415 |
| loco | start_points | overall | rmse_h1 | elasticnet | 1.664 [1.265, 2.040] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 1.966 | 4 | 5 | e1ff5d55 |
| loco | start_points | overall | rmse_h1 | gru | 2.323 [1.714, 2.949] | 0/4 cells, 2/20 cell-seeds (vs persistence) | 2.503 | 4 | 5 | 9731ae77 |
| loco | start_points | overall | rmse_h1 | itransformer | 1.820 [1.085, 2.555] | 0/4 cells, 2/20 cell-seeds (vs persistence) | 2.576 | 4 | 5 | 9dedaedf |
| loco | start_points | overall | rmse_h1 | itransformer_sc | 1.809 [1.109, 2.509] | 0/4 cells, 0/20 cell-seeds (vs persistence) | 2.492 | 4 | 5 | e5cc9a22 |
| loco | start_points | overall | rmse_h1 | last_slope | 1.909 [1.139, 2.679] | 0/4 cells, 0/20 cell-seeds (vs persistence) | 2.642 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | overall | rmse_h1 | lgbm | 1.843 [1.196, 2.491] | 0/4 cells, 0/20 cell-seeds (vs persistence) | 2.498 | 4 | 5 | acedf5f4 |
| loco | start_points | overall | rmse_h1 | lstm | 1.966 [1.856, 2.101] | 2/4 cells, 8/20 cell-seeds (vs persistence) | 1.960 | 4 | 5 | 5494788a |
| loco | start_points | overall | rmse_h1 | nlinear | 1.796 [1.165, 2.427] | 0/4 cells, 0/20 cell-seeds (vs persistence) | 2.379 | 4 | 5 | b4ecdb12 |
| loco | start_points | overall | rmse_h1 | patchtst | 1.838 [1.094, 2.583] | 0/4 cells, 1/20 cell-seeds (vs persistence) | 2.584 | 4 | 5 | d75a14c6 |
| loco | start_points | overall | rmse_h1 | persistence | 1.654 [1.057, 2.251] |  | 2.261 | 4 | 5 | a26a213d |
| loco | start_points | overall | rmse_h1 | rlinear | 1.728 [1.041, 2.414] | 1/4 cells, 8/20 cell-seeds (vs persistence) | 2.355 | 4 | 5 | 78bc3e35 |
| loco | start_points | overall | rmse_h1 | transformer | 2.865 [1.604, 4.208] | 0/4 cells, 0/20 cell-seeds (vs persistence) | 4.919 | 4 | 5 | 19b71fc1 |
| loco | start_points | overall | rmse_h10 | dlinear | 7.114 [6.460, 7.878] | 0/4 cells, 0/20 cell-seeds (vs persistence) | 7.220 | 4 | 5 | 3b67b415 |
| loco | start_points | overall | rmse_h10 | elasticnet | 2.633 [1.339, 3.926] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 4.343 | 4 | 5 | e1ff5d55 |
| loco | start_points | overall | rmse_h10 | gru | 2.628 [1.441, 3.814] | 4/4 cells, 15/20 cell-seeds (vs persistence) | 3.087 | 4 | 5 | 9731ae77 |
| loco | start_points | overall | rmse_h10 | itransformer | 1.882 [1.057, 2.953] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 3.579 | 4 | 5 | 9dedaedf |
| loco | start_points | overall | rmse_h10 | itransformer_sc | 2.044 [1.223, 2.975] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 3.554 | 4 | 5 | e5cc9a22 |
| loco | start_points | overall | rmse_h10 | last_slope | 3.935 [2.490, 5.381] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 5.540 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | overall | rmse_h10 | lgbm | 1.906 [1.063, 2.750] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 2.856 | 4 | 5 | acedf5f4 |
| loco | start_points | overall | rmse_h10 | lstm | 2.818 [1.900, 3.804] | 4/4 cells, 16/20 cell-seeds (vs persistence) | 3.083 | 4 | 5 | 5494788a |
| loco | start_points | overall | rmse_h10 | nlinear | 2.115 [1.174, 3.057] | 4/4 cells, 17/20 cell-seeds (vs persistence) | 3.203 | 4 | 5 | b4ecdb12 |
| loco | start_points | overall | rmse_h10 | patchtst | 1.699 [0.965, 2.810] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 3.388 | 4 | 5 | d75a14c6 |
| loco | start_points | overall | rmse_h10 | persistence | 3.348 [2.574, 4.229] |  | 3.206 | 4 | 5 | a26a213d |
| loco | start_points | overall | rmse_h10 | rlinear | 2.666 [2.035, 3.276] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 3.467 | 4 | 5 | 78bc3e35 |
| loco | start_points | overall | rmse_h10 | transformer | 3.573 [2.128, 5.537] | 2/4 cells, 12/20 cell-seeds (vs persistence) | 6.569 | 4 | 5 | 19b71fc1 |
| loco | start_points | overall | rmse_h50 | dlinear | 13.635 [11.939, 15.332] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 12.312 | 4 | 5 | 3b67b415 |
| loco | start_points | overall | rmse_h50 | elasticnet | 5.448 [2.837, 8.060] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 6.983 | 4 | 5 | e1ff5d55 |
| loco | start_points | overall | rmse_h50 | gru | 3.707 [2.278, 5.310] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 2.690 | 4 | 5 | 9731ae77 |
| loco | start_points | overall | rmse_h50 | itransformer | 5.715 [4.163, 7.364] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.530 | 4 | 5 | 9dedaedf |
| loco | start_points | overall | rmse_h50 | itransformer_sc | 5.012 [4.120, 6.229] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 4.768 | 4 | 5 | e5cc9a22 |
| loco | start_points | overall | rmse_h50 | last_slope | 14.573 [9.092, 19.775] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 21.338 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | overall | rmse_h50 | lgbm | 3.325 [2.292, 4.882] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.041 | 4 | 5 | acedf5f4 |
| loco | start_points | overall | rmse_h50 | lstm | 3.408 [2.160, 4.934] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.492 | 4 | 5 | 5494788a |
| loco | start_points | overall | rmse_h50 | nlinear | 3.876 [2.640, 5.600] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.605 | 4 | 5 | b4ecdb12 |
| loco | start_points | overall | rmse_h50 | patchtst | 3.600 [2.269, 4.931] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 4.691 | 4 | 5 | d75a14c6 |
| loco | start_points | overall | rmse_h50 | persistence | 13.452 [11.482, 15.613] |  | 12.879 | 4 | 5 | a26a213d |
| loco | start_points | overall | rmse_h50 | rlinear | 7.641 [6.502, 9.484] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 6.357 | 4 | 5 | 78bc3e35 |
| loco | start_points | overall | rmse_h50 | transformer | 5.091 [3.351, 6.748] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 4.923 | 4 | 5 | 19b71fc1 |

### nasa_rul

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rul_mae | dlinear | 15.590 [9.447, 22.489] |  | 7.338 | 4 | 5 | 66a55967 |
| loco | all | overall | rul_mae | elasticnet | 73.095 [33.713, 101.144] |  | 16.025 | 4 | 5 | 17c49e01 |
| loco | all | overall | rul_mae | gru | 25.570 [15.361, 36.340] |  | 15.115 | 4 | 5 | 4e5a6656 |
| loco | all | overall | rul_mae | itransformer | 16.708 [10.672, 22.745] |  | 12.726 | 4 | 5 | cf2844f4 |
| loco | all | overall | rul_mae | itransformer_sc | 17.612 [12.364, 22.860] |  | 12.174 | 4 | 5 | 99bba290 |
| loco | all | overall | rul_mae | lgbm | 19.833 [14.226, 25.439] |  | 12.709 | 4 | 5 | faab17c4 |
| loco | all | overall | rul_mae | lstm | 17.433 [11.508, 23.887] |  | 12.498 | 4 | 5 | 86645d26 |
| loco | all | overall | rul_mae | nlinear | 16.251 [10.278, 23.435] |  | 8.051 | 4 | 5 | 723c6ded |
| loco | all | overall | rul_mae | patchtst | 36.057 [22.341, 46.425] |  | 16.541 | 4 | 5 | 9aa4edae |
| loco | all | overall | rul_mae | rlinear | 35.155 [22.550, 47.760] |  | 27.107 | 4 | 5 | b18361de |
| loco | all | overall | rul_mae | transformer | 31.330 [21.904, 42.150] |  | 21.483 | 4 | 5 | a5a14771 |
| loco | start_points | overall | rul_mae | dlinear | 13.965 [7.618, 21.495] |  | 5.293 | 4 | 5 | 66a55967 |
| loco | start_points | overall | rul_mae | elasticnet | 93.558 [41.998, 137.829] |  | 13.298 | 4 | 5 | 17c49e01 |
| loco | start_points | overall | rul_mae | gru | 25.071 [12.047, 38.096] |  | 10.786 | 4 | 5 | 4e5a6656 |
| loco | start_points | overall | rul_mae | itransformer | 14.275 [7.625, 20.932] |  | 7.765 | 4 | 5 | cf2844f4 |
| loco | start_points | overall | rul_mae | itransformer_sc | 14.683 [9.289, 20.078] |  | 7.314 | 4 | 5 | 99bba290 |
| loco | start_points | overall | rul_mae | lgbm | 16.923 [8.253, 25.593] |  | 8.780 | 4 | 5 | faab17c4 |
| loco | start_points | overall | rul_mae | lstm | 18.124 [13.698, 23.461] |  | 12.906 | 4 | 5 | 86645d26 |
| loco | start_points | overall | rul_mae | nlinear | 14.659 [6.909, 23.565] |  | 3.866 | 4 | 5 | 723c6ded |
| loco | start_points | overall | rul_mae | patchtst | 35.141 [17.202, 50.136] |  | 8.836 | 4 | 5 | 9aa4edae |
| loco | start_points | overall | rul_mae | rlinear | 35.758 [14.707, 56.810] |  | 19.908 | 4 | 5 | b18361de |
| loco | start_points | overall | rul_mae | transformer | 32.755 [20.489, 45.022] |  | 19.476 | 4 | 5 | a5a14771 |

### nasa_soh

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse | dlinear | 0.940 [0.706, 1.174] | 3/4 cells, 13/20 cell-seeds (vs prev_soh) | 1.202 | 4 | 5 | 5ef63051 |
| loco | all | overall | rmse | elasticnet | 1.240 [0.701, 2.043] | 2/4 cells, 10/20 cell-seeds (vs prev_soh) | 2.473 | 4 | 5 | c3c0651b |
| loco | all | overall | rmse | gru | 2.673 [2.353, 3.075] | 0/4 cells, 0/20 cell-seeds (vs prev_soh) | 3.295 | 4 | 5 | dbed923e |
| loco | all | overall | rmse | itransformer | 0.703 [0.540, 0.866] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) | 0.936 | 4 | 5 | 48e8d64a |
| loco | all | overall | rmse | itransformer_sc | 0.699 [0.563, 0.835] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) | 0.820 | 4 | 5 | 197d4e36 |
| loco | all | overall | rmse | lgbm | 0.928 [0.694, 1.162] | 3/4 cells, 15/20 cell-seeds (vs prev_soh) | 1.184 | 4 | 5 | e72f6de0 |
| loco | all | overall | rmse | lstm | 1.187 [1.141, 1.240] | 1/4 cells, 12/20 cell-seeds (vs prev_soh) | 1.156 | 4 | 5 | 7e0af82e |
| loco | all | overall | rmse | nlinear | 0.933 [0.693, 1.173] | 3/4 cells, 14/20 cell-seeds (vs prev_soh) | 1.203 | 4 | 5 | 1d4b3de0 |
| loco | all | overall | rmse | patchtst | 0.928 [0.656, 1.201] | 3/4 cells, 15/20 cell-seeds (vs prev_soh) | 1.261 | 4 | 5 | ef980b9c |
| loco | all | overall | rmse | prev_soh | 0.955 [0.697, 1.213] |  | 1.245 | 4 | 5 | 0d396b2f |
| loco | all | overall | rmse | rlinear | 0.929 [0.669, 1.189] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) | 1.219 | 4 | 5 | bd5b08dc |
| loco | all | overall | rmse | transformer | 3.666 [2.774, 5.171] | 0/4 cells, 0/20 cell-seeds (vs prev_soh) | 5.909 | 4 | 5 | 078809a4 |
| loco | start_points | overall | rmse | dlinear | 0.379 [0.288, 0.536] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) | 0.323 | 4 | 5 | 5ef63051 |
| loco | start_points | overall | rmse | elasticnet | 0.621 [0.186, 1.254] | 3/4 cells, 15/20 cell-seeds (vs prev_soh) | 1.600 | 4 | 5 | c3c0651b |
| loco | start_points | overall | rmse | gru | 2.443 [2.083, 2.769] | 0/4 cells, 0/20 cell-seeds (vs prev_soh) | 2.363 | 4 | 5 | dbed923e |
| loco | start_points | overall | rmse | itransformer | 0.305 [0.142, 0.496] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) | 0.341 | 4 | 5 | 48e8d64a |
| loco | start_points | overall | rmse | itransformer_sc | 0.422 [0.191, 0.652] | 3/4 cells, 15/20 cell-seeds (vs prev_soh) | 0.602 | 4 | 5 | 197d4e36 |
| loco | start_points | overall | rmse | lgbm | 0.476 [0.304, 0.745] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) | 0.332 | 4 | 5 | e72f6de0 |
| loco | start_points | overall | rmse | lstm | 0.981 [0.831, 1.194] | 0/4 cells, 9/20 cell-seeds (vs prev_soh) | 0.817 | 4 | 5 | 7e0af82e |
| loco | start_points | overall | rmse | nlinear | 0.373 [0.281, 0.546] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) | 0.295 | 4 | 5 | 1d4b3de0 |
| loco | start_points | overall | rmse | patchtst | 0.399 [0.223, 0.651] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) | 0.356 | 4 | 5 | ef980b9c |
| loco | start_points | overall | rmse | prev_soh | 0.646 [0.506, 0.809] |  | 0.508 | 4 | 5 | 0d396b2f |
| loco | start_points | overall | rmse | rlinear | 0.406 [0.272, 0.647] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) | 0.274 | 4 | 5 | bd5b08dc |
| loco | start_points | overall | rmse | transformer | 3.126 [2.610, 4.037] | 0/4 cells, 0/20 cell-seeds (vs prev_soh) | 4.509 | 4 | 5 | 078809a4 |

### toyota_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rmse_h1 | dlinear | 0.136 [0.081, 0.200] | p=0.257 (vs last_slope) |  | 43 | 5 | 0b00c3d4 |
| test1 | all | overall | rmse_h1 | elasticnet | 0.134 [0.080, 0.197] | p=0.0143 (vs last_slope) |  | 43 | 5 | 4c070a82 |
| test1 | all | overall | rmse_h1 | gru | 0.176 [0.119, 0.242] | p=2.73e-12 (vs last_slope) |  | 43 | 5 | 74f02c88 |
| test1 | all | overall | rmse_h1 | itransformer | 0.124 [0.073, 0.183] | p=1.75e-11 (vs last_slope) |  | 43 | 5 | 0ce99716 |
| test1 | all | overall | rmse_h1 | itransformer_sc | 0.132 [0.078, 0.196] | p=5.84e-09 (vs last_slope) |  | 43 | 5 | aa089496 |
| test1 | all | overall | rmse_h1 | last_slope | 0.137 [0.081, 0.203] |  |  | 43 | 5 | c733fae1 |
| test1 | all | overall | rmse_h1 | lgbm | 0.133 [0.079, 0.197] | p=0.000139 (vs last_slope) |  | 43 | 5 | 7c413ce2 |
| test1 | all | overall | rmse_h1 | lstm | 0.140 [0.086, 0.203] | p=0.0571 (vs last_slope) |  | 43 | 5 | cc4f6edb |
| test1 | all | overall | rmse_h1 | nlinear | 0.134 [0.079, 0.198] | p=4.16e-09 (vs last_slope) |  | 43 | 5 | 60722fba |
| test1 | all | overall | rmse_h1 | patchtst | 0.130 [0.077, 0.193] | p=5.6e-05 (vs last_slope) |  | 43 | 5 | 73deb6e0 |
| test1 | all | overall | rmse_h1 | persistence | 0.158 [0.106, 0.219] | p=2.91e-05 (vs last_slope) |  | 43 | 5 | 84662b2e |
| test1 | all | overall | rmse_h1 | rlinear | 0.120 [0.074, 0.174] | p=0.0571 (vs last_slope) |  | 43 | 5 | ee0fc6f5 |
| test1 | all | overall | rmse_h1 | transformer | 0.186 [0.135, 0.246] | p=1.75e-11 (vs last_slope) |  | 43 | 5 | eb07a039 |
| test1 | all | overall | rmse_h10 | dlinear | 0.225 [0.164, 0.297] | p=0.000144 (vs last_slope) |  | 43 | 5 | 0b00c3d4 |
| test1 | all | overall | rmse_h10 | elasticnet | 0.197 [0.142, 0.261] | p=1.8e-10 (vs last_slope) |  | 43 | 5 | 4c070a82 |
| test1 | all | overall | rmse_h10 | gru | 0.177 [0.128, 0.233] | p=1.81e-07 (vs last_slope) |  | 43 | 5 | 74f02c88 |
| test1 | all | overall | rmse_h10 | itransformer | 0.157 [0.105, 0.216] | p=1.16e-09 (vs last_slope) |  | 43 | 5 | 0ce99716 |
| test1 | all | overall | rmse_h10 | itransformer_sc | 0.184 [0.129, 0.249] | p=4.38e-09 (vs last_slope) |  | 43 | 5 | aa089496 |
| test1 | all | overall | rmse_h10 | last_slope | 0.265 [0.184, 0.359] |  |  | 43 | 5 | c733fae1 |
| test1 | all | overall | rmse_h10 | lgbm | 0.175 [0.118, 0.242] | p=1.44e-09 (vs last_slope) |  | 43 | 5 | 7c413ce2 |
| test1 | all | overall | rmse_h10 | lstm | 0.177 [0.121, 0.243] | p=2.73e-12 (vs last_slope) |  | 43 | 5 | cc4f6edb |
| test1 | all | overall | rmse_h10 | nlinear | 0.212 [0.147, 0.289] | p=9.78e-11 (vs last_slope) |  | 43 | 5 | 60722fba |
| test1 | all | overall | rmse_h10 | patchtst | 0.173 [0.119, 0.236] | p=4.38e-09 (vs last_slope) |  | 43 | 5 | 73deb6e0 |
| test1 | all | overall | rmse_h10 | persistence | 0.600 [0.526, 0.679] | p=2.24e-08 (vs last_slope) |  | 43 | 5 | 84662b2e |
| test1 | all | overall | rmse_h10 | rlinear | 0.184 [0.132, 0.243] | p=6.25e-11 (vs last_slope) |  | 43 | 5 | ee0fc6f5 |
| test1 | all | overall | rmse_h10 | transformer | 0.212 [0.158, 0.276] | p=0.000879 (vs last_slope) |  | 43 | 5 | eb07a039 |
| test1 | all | overall | rmse_h50 | dlinear | 0.846 [0.721, 0.980] | p=2.6e-08 (vs last_slope) |  | 43 | 5 | 0b00c3d4 |
| test1 | all | overall | rmse_h50 | elasticnet | 0.655 [0.567, 0.746] | p=2.73e-12 (vs last_slope) |  | 43 | 5 | 4c070a82 |
| test1 | all | overall | rmse_h50 | gru | 0.475 [0.391, 0.569] | p=7.5e-11 (vs last_slope) |  | 43 | 5 | 74f02c88 |
| test1 | all | overall | rmse_h50 | itransformer | 0.402 [0.315, 0.514] | p=1.59e-11 (vs last_slope) |  | 43 | 5 | 0ce99716 |
| test1 | all | overall | rmse_h50 | itransformer_sc | 0.532 [0.434, 0.648] | p=1.92e-10 (vs last_slope) |  | 43 | 5 | aa089496 |
| test1 | all | overall | rmse_h50 | last_slope | 1.202 [0.954, 1.480] |  |  | 43 | 5 | c733fae1 |
| test1 | all | overall | rmse_h50 | lgbm | 0.451 [0.347, 0.586] | p=5.2e-10 (vs last_slope) |  | 43 | 5 | 7c413ce2 |
| test1 | all | overall | rmse_h50 | lstm | 0.501 [0.416, 0.591] | p=2.73e-12 (vs last_slope) |  | 43 | 5 | cc4f6edb |
| test1 | all | overall | rmse_h50 | nlinear | 0.766 [0.628, 0.912] | p=9.09e-12 (vs last_slope) |  | 43 | 5 | 60722fba |
| test1 | all | overall | rmse_h50 | patchtst | 0.537 [0.443, 0.649] | p=1.92e-10 (vs last_slope) |  | 43 | 5 | 73deb6e0 |
| test1 | all | overall | rmse_h50 | persistence | 2.502 [2.179, 2.849] | p=2.87e-08 (vs last_slope) |  | 43 | 5 | 84662b2e |
| test1 | all | overall | rmse_h50 | rlinear | 0.698 [0.574, 0.831] | p=2.73e-12 (vs last_slope) |  | 43 | 5 | ee0fc6f5 |
| test1 | all | overall | rmse_h50 | transformer | 0.513 [0.431, 0.599] | p=2.73e-12 (vs last_slope) |  | 43 | 5 | eb07a039 |
| test1 | start_points | overall | rmse_h1 | dlinear | 0.048 [0.032, 0.066] | p=0.641 (vs persistence) |  | 43 | 5 | 0b00c3d4 |
| test1 | start_points | overall | rmse_h1 | elasticnet | 0.040 [0.027, 0.056] | p=0.0465 (vs persistence) |  | 43 | 5 | 4c070a82 |
| test1 | start_points | overall | rmse_h1 | gru | 0.083 [0.058, 0.116] | p=1.64e-05 (vs persistence) |  | 43 | 5 | 74f02c88 |
| test1 | start_points | overall | rmse_h1 | itransformer | 0.040 [0.026, 0.058] | p=0.00938 (vs persistence) |  | 43 | 5 | 0ce99716 |
| test1 | start_points | overall | rmse_h1 | itransformer_sc | 0.040 [0.027, 0.057] | p=0.0109 (vs persistence) |  | 43 | 5 | aa089496 |
| test1 | start_points | overall | rmse_h1 | last_slope | 0.052 [0.033, 0.074] | p=0.341 (vs persistence) |  | 43 | 5 | c733fae1 |
| test1 | start_points | overall | rmse_h1 | lgbm | 0.039 [0.025, 0.055] | p=0.000317 (vs persistence) |  | 43 | 5 | 7c413ce2 |
| test1 | start_points | overall | rmse_h1 | lstm | 0.054 [0.037, 0.074] | p=0.641 (vs persistence) |  | 43 | 5 | cc4f6edb |
| test1 | start_points | overall | rmse_h1 | nlinear | 0.040 [0.027, 0.057] | p=0.0276 (vs persistence) |  | 43 | 5 | 60722fba |
| test1 | start_points | overall | rmse_h1 | patchtst | 0.039 [0.026, 0.055] | p=0.00147 (vs persistence) |  | 43 | 5 | 73deb6e0 |
| test1 | start_points | overall | rmse_h1 | persistence | 0.045 [0.032, 0.061] |  |  | 43 | 5 | 84662b2e |
| test1 | start_points | overall | rmse_h1 | rlinear | 0.067 [0.038, 0.103] | p=0.641 (vs persistence) |  | 43 | 5 | ee0fc6f5 |
| test1 | start_points | overall | rmse_h1 | transformer | 0.095 [0.079, 0.114] | p=1.8e-08 (vs persistence) |  | 43 | 5 | eb07a039 |
| test1 | start_points | overall | rmse_h10 | dlinear | 0.111 [0.077, 0.153] | p=5.71e-08 (vs persistence) |  | 43 | 5 | 0b00c3d4 |
| test1 | start_points | overall | rmse_h10 | elasticnet | 0.105 [0.070, 0.146] | p=2.78e-07 (vs persistence) |  | 43 | 5 | 4c070a82 |
| test1 | start_points | overall | rmse_h10 | gru | 0.112 [0.072, 0.162] | p=9.01e-07 (vs persistence) |  | 43 | 5 | 74f02c88 |
| test1 | start_points | overall | rmse_h10 | itransformer | 0.082 [0.048, 0.127] | p=2.49e-08 (vs persistence) |  | 43 | 5 | 0ce99716 |
| test1 | start_points | overall | rmse_h10 | itransformer_sc | 0.092 [0.058, 0.135] | p=7.31e-08 (vs persistence) |  | 43 | 5 | aa089496 |
| test1 | start_points | overall | rmse_h10 | last_slope | 0.239 [0.099, 0.422] | p=0.00277 (vs persistence) |  | 43 | 5 | c733fae1 |
| test1 | start_points | overall | rmse_h10 | lgbm | 0.096 [0.059, 0.140] | p=3.63e-07 (vs persistence) |  | 43 | 5 | 7c413ce2 |
| test1 | start_points | overall | rmse_h10 | lstm | 0.112 [0.068, 0.167] | p=9.57e-07 (vs persistence) |  | 43 | 5 | cc4f6edb |
| test1 | start_points | overall | rmse_h10 | nlinear | 0.090 [0.057, 0.134] | p=4.36e-08 (vs persistence) |  | 43 | 5 | 60722fba |
| test1 | start_points | overall | rmse_h10 | patchtst | 0.081 [0.050, 0.120] | p=2.37e-08 (vs persistence) |  | 43 | 5 | 73deb6e0 |
| test1 | start_points | overall | rmse_h10 | persistence | 0.234 [0.180, 0.307] |  |  | 43 | 5 | 84662b2e |
| test1 | start_points | overall | rmse_h10 | rlinear | 0.119 [0.068, 0.181] | p=1.4e-05 (vs persistence) |  | 43 | 5 | ee0fc6f5 |
| test1 | start_points | overall | rmse_h10 | transformer | 0.134 [0.102, 0.173] | p=4.49e-06 (vs persistence) |  | 43 | 5 | eb07a039 |
| test1 | start_points | overall | rmse_h50 | dlinear | 0.428 [0.390, 0.474] | p=0.247 (vs last_slope) |  | 43 | 5 | 0b00c3d4 |
| test1 | start_points | overall | rmse_h50 | elasticnet | 0.441 [0.336, 0.565] | p=0.0705 (vs last_slope) |  | 43 | 5 | 4c070a82 |
| test1 | start_points | overall | rmse_h50 | gru | 0.355 [0.242, 0.482] | p=0.0019 (vs last_slope) |  | 43 | 5 | 74f02c88 |
| test1 | start_points | overall | rmse_h50 | itransformer | 0.250 [0.154, 0.372] | p=7.46e-05 (vs last_slope) |  | 43 | 5 | 0ce99716 |
| test1 | start_points | overall | rmse_h50 | itransformer_sc | 0.286 [0.198, 0.393] | p=2.66e-05 (vs last_slope) |  | 43 | 5 | aa089496 |
| test1 | start_points | overall | rmse_h50 | last_slope | 1.101 [0.460, 1.991] |  |  | 43 | 5 | c733fae1 |
| test1 | start_points | overall | rmse_h50 | lgbm | 0.305 [0.187, 0.465] | p=3.74e-05 (vs last_slope) |  | 43 | 5 | 7c413ce2 |
| test1 | start_points | overall | rmse_h50 | lstm | 0.343 [0.243, 0.461] | p=0.00319 (vs last_slope) |  | 43 | 5 | cc4f6edb |
| test1 | start_points | overall | rmse_h50 | nlinear | 0.272 [0.225, 0.325] | p=3.06e-05 (vs last_slope) |  | 43 | 5 | 60722fba |
| test1 | start_points | overall | rmse_h50 | patchtst | 0.215 [0.165, 0.278] | p=1.09e-06 (vs last_slope) |  | 43 | 5 | 73deb6e0 |
| test1 | start_points | overall | rmse_h50 | persistence | 1.197 [0.940, 1.577] | p=0.00196 (vs last_slope) |  | 43 | 5 | 84662b2e |
| test1 | start_points | overall | rmse_h50 | rlinear | 0.378 [0.265, 0.518] | p=0.000222 (vs last_slope) |  | 43 | 5 | ee0fc6f5 |
| test1 | start_points | overall | rmse_h50 | transformer | 0.357 [0.263, 0.466] | p=0.00445 (vs last_slope) |  | 43 | 5 | eb07a039 |
| test2 | all | overall | rmse_h1 | dlinear | 0.019 [0.016, 0.021] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | all | overall | rmse_h1 | elasticnet | 0.019 [0.017, 0.022] | p=3.82e-11 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | all | overall | rmse_h1 | gru | 0.089 [0.076, 0.106] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | all | overall | rmse_h1 | itransformer | 0.015 [0.013, 0.018] | p=3.94e-06 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | all | overall | rmse_h1 | itransformer_sc | 0.016 [0.013, 0.019] | p=4.51e-05 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | all | overall | rmse_h1 | last_slope | 0.016 [0.014, 0.019] |  |  | 40 | 5 | c733fae1 |
| test2 | all | overall | rmse_h1 | lgbm | 0.020 [0.017, 0.022] | p=8.28e-08 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | all | overall | rmse_h1 | lstm | 0.025 [0.022, 0.027] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | all | overall | rmse_h1 | nlinear | 0.017 [0.014, 0.020] | p=0.0343 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | all | overall | rmse_h1 | patchtst | 0.017 [0.014, 0.019] | p=0.259 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | all | overall | rmse_h1 | persistence | 0.036 [0.034, 0.038] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | all | overall | rmse_h1 | rlinear | 0.018 [0.016, 0.020] | p=0.00432 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | all | overall | rmse_h1 | transformer | 0.113 [0.105, 0.122] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | all | overall | rmse_h10 | dlinear | 0.064 [0.060, 0.068] | p=0.000288 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | all | overall | rmse_h10 | elasticnet | 0.064 [0.058, 0.070] | p=0.014 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | all | overall | rmse_h10 | gru | 0.108 [0.089, 0.130] | p=3.02e-08 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | all | overall | rmse_h10 | itransformer | 0.032 [0.028, 0.037] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | all | overall | rmse_h10 | itransformer_sc | 0.037 [0.032, 0.042] | p=7.28e-11 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | all | overall | rmse_h10 | last_slope | 0.057 [0.051, 0.063] |  |  | 40 | 5 | c733fae1 |
| test2 | all | overall | rmse_h10 | lgbm | 0.061 [0.055, 0.066] | p=0.485 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | all | overall | rmse_h10 | lstm | 0.051 [0.045, 0.058] | p=0.0642 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | all | overall | rmse_h10 | nlinear | 0.046 [0.042, 0.051] | p=4.07e-08 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | all | overall | rmse_h10 | patchtst | 0.033 [0.029, 0.039] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | all | overall | rmse_h10 | persistence | 0.303 [0.281, 0.324] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | all | overall | rmse_h10 | rlinear | 0.045 [0.040, 0.050] | p=1.18e-07 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | all | overall | rmse_h10 | transformer | 0.107 [0.101, 0.113] | p=3.27e-11 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | all | overall | rmse_h50 | dlinear | 0.470 [0.448, 0.494] | p=0.000528 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | all | overall | rmse_h50 | elasticnet | 0.491 [0.450, 0.532] | p=9.66e-08 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | all | overall | rmse_h50 | gru | 0.467 [0.407, 0.528] | p=0.183 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | all | overall | rmse_h50 | itransformer | 0.200 [0.174, 0.226] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | all | overall | rmse_h50 | itransformer_sc | 0.180 [0.153, 0.210] | p=1.15e-10 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | all | overall | rmse_h50 | last_slope | 0.397 [0.360, 0.434] |  |  | 40 | 5 | c733fae1 |
| test2 | all | overall | rmse_h50 | lgbm | 0.302 [0.278, 0.327] | p=5.62e-06 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | all | overall | rmse_h50 | lstm | 0.282 [0.253, 0.312] | p=5.62e-06 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | all | overall | rmse_h50 | nlinear | 0.298 [0.270, 0.328] | p=7.83e-07 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | all | overall | rmse_h50 | patchtst | 0.185 [0.165, 0.207] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | all | overall | rmse_h50 | persistence | 1.354 [1.265, 1.437] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | all | overall | rmse_h50 | rlinear | 0.270 [0.239, 0.301] | p=7.83e-07 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | all | overall | rmse_h50 | transformer | 0.281 [0.252, 0.311] | p=7.8e-09 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | start_points | overall | rmse_h1 | dlinear | 0.016 [0.009, 0.023] | p=1.79e-05 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | start_points | overall | rmse_h1 | elasticnet | 0.018 [0.012, 0.025] | p=2.83e-06 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | start_points | overall | rmse_h1 | gru | 0.079 [0.064, 0.099] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | start_points | overall | rmse_h1 | itransformer | 0.013 [0.007, 0.019] | p=0.0601 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | start_points | overall | rmse_h1 | itransformer_sc | 0.014 [0.008, 0.021] | p=0.526 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | start_points | overall | rmse_h1 | last_slope | 0.014 [0.008, 0.022] |  |  | 40 | 5 | c733fae1 |
| test2 | start_points | overall | rmse_h1 | lgbm | 0.018 [0.012, 0.024] | p=0.00124 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | start_points | overall | rmse_h1 | lstm | 0.021 [0.015, 0.028] | p=6.75e-09 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | start_points | overall | rmse_h1 | nlinear | 0.014 [0.008, 0.022] | p=1 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | start_points | overall | rmse_h1 | patchtst | 0.013 [0.007, 0.019] | p=0.526 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | start_points | overall | rmse_h1 | persistence | 0.018 [0.012, 0.025] | p=2.91e-05 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | start_points | overall | rmse_h1 | rlinear | 0.012 [0.008, 0.018] | p=1 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | start_points | overall | rmse_h1 | transformer | 0.115 [0.106, 0.124] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | start_points | overall | rmse_h10 | dlinear | 0.041 [0.036, 0.048] | p=5.29e-05 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | start_points | overall | rmse_h10 | elasticnet | 0.029 [0.024, 0.035] | p=0.368 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | start_points | overall | rmse_h10 | gru | 0.095 [0.073, 0.121] | p=8.13e-09 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | start_points | overall | rmse_h10 | itransformer | 0.020 [0.016, 0.026] | p=2.71e-06 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | start_points | overall | rmse_h10 | itransformer_sc | 0.024 [0.018, 0.030] | p=5.2e-05 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | start_points | overall | rmse_h10 | last_slope | 0.032 [0.025, 0.040] |  |  | 40 | 5 | c733fae1 |
| test2 | start_points | overall | rmse_h10 | lgbm | 0.056 [0.048, 0.064] | p=3.88e-06 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | start_points | overall | rmse_h10 | lstm | 0.046 [0.040, 0.054] | p=0.000265 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | start_points | overall | rmse_h10 | nlinear | 0.026 [0.020, 0.035] | p=0.00221 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | start_points | overall | rmse_h10 | patchtst | 0.020 [0.015, 0.026] | p=1.31e-06 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | start_points | overall | rmse_h10 | persistence | 0.090 [0.078, 0.105] | p=2.2e-09 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | start_points | overall | rmse_h10 | rlinear | 0.020 [0.016, 0.025] | p=4.03e-07 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | start_points | overall | rmse_h10 | transformer | 0.096 [0.091, 0.102] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | start_points | overall | rmse_h50 | dlinear | 0.367 [0.354, 0.382] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | start_points | overall | rmse_h50 | elasticnet | 0.286 [0.256, 0.316] | p=3.89e-08 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | start_points | overall | rmse_h50 | gru | 0.444 [0.382, 0.508] | p=2e-09 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | start_points | overall | rmse_h50 | itransformer | 0.070 [0.059, 0.082] | p=4.05e-07 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | start_points | overall | rmse_h50 | itransformer_sc | 0.084 [0.062, 0.112] | p=0.000272 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | start_points | overall | rmse_h50 | last_slope | 0.133 [0.113, 0.154] |  |  | 40 | 5 | c733fae1 |
| test2 | start_points | overall | rmse_h50 | lgbm | 0.222 [0.202, 0.241] | p=2.33e-06 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | start_points | overall | rmse_h50 | lstm | 0.213 [0.183, 0.246] | p=0.000353 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | start_points | overall | rmse_h50 | nlinear | 0.120 [0.098, 0.145] | p=0.628 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | start_points | overall | rmse_h50 | patchtst | 0.077 [0.066, 0.089] | p=1.59e-06 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | start_points | overall | rmse_h50 | persistence | 0.472 [0.408, 0.547] | p=1e-10 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | start_points | overall | rmse_h50 | rlinear | 0.094 [0.073, 0.119] | p=0.00227 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | start_points | overall | rmse_h50 | transformer | 0.134 [0.115, 0.156] | p=0.952 (vs last_slope) |  | 40 | 5 | eb07a039 |

### toyota_rul

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rul_mae | dlinear | 134.275 [96.428, 182.072] |  |  | 43 | 5 | c066ff8c |
| test1 | all | overall | rul_mae | elasticnet | 110.004 [78.385, 150.217] |  |  | 43 | 5 | 6228f90c |
| test1 | all | overall | rul_mae | gru | 80.826 [57.844, 108.591] |  |  | 43 | 5 | 68c083f5 |
| test1 | all | overall | rul_mae | itransformer | 78.362 [54.298, 108.739] |  |  | 43 | 5 | 1f7dadba |
| test1 | all | overall | rul_mae | itransformer_sc | 76.097 [53.084, 105.406] |  |  | 43 | 5 | 4a0a69dd |
| test1 | all | overall | rul_mae | lgbm | 57.869 [39.443, 80.381] |  |  | 43 | 5 | b88b5644 |
| test1 | all | overall | rul_mae | lstm | 70.208 [51.137, 93.125] |  |  | 43 | 5 | 7a6e2343 |
| test1 | all | overall | rul_mae | nlinear | 134.312 [96.475, 182.102] |  |  | 43 | 5 | f6a02b2d |
| test1 | all | overall | rul_mae | patchtst | 250.500 [204.828, 304.197] |  |  | 43 | 5 | 5b64c567 |
| test1 | all | overall | rul_mae | rlinear | 339.280 [287.944, 399.732] |  |  | 43 | 5 | aa9b25f1 |
| test1 | all | overall | rul_mae | transformer | 88.107 [64.229, 115.516] |  |  | 43 | 5 | cd2ed4cc |
| test1 | start_points | overall | rul_mae | dlinear | 156.452 [108.107, 217.042] |  |  | 43 | 5 | c066ff8c |
| test1 | start_points | overall | rul_mae | elasticnet | 125.405 [85.423, 176.345] |  |  | 43 | 5 | 6228f90c |
| test1 | start_points | overall | rul_mae | gru | 92.286 [64.128, 127.250] |  |  | 43 | 5 | 68c083f5 |
| test1 | start_points | overall | rul_mae | itransformer | 94.330 [67.393, 128.161] |  |  | 43 | 5 | 1f7dadba |
| test1 | start_points | overall | rul_mae | itransformer_sc | 97.213 [68.566, 132.581] |  |  | 43 | 5 | 4a0a69dd |
| test1 | start_points | overall | rul_mae | lgbm | 67.601 [45.610, 94.968] |  |  | 43 | 5 | b88b5644 |
| test1 | start_points | overall | rul_mae | lstm | 76.267 [54.146, 104.259] |  |  | 43 | 5 | 7a6e2343 |
| test1 | start_points | overall | rul_mae | nlinear | 156.510 [108.240, 217.209] |  |  | 43 | 5 | f6a02b2d |
| test1 | start_points | overall | rul_mae | patchtst | 287.042 [234.037, 351.378] |  |  | 43 | 5 | 5b64c567 |
| test1 | start_points | overall | rul_mae | rlinear | 400.143 [333.537, 478.880] |  |  | 43 | 5 | aa9b25f1 |
| test1 | start_points | overall | rul_mae | transformer | 99.973 [71.229, 133.382] |  |  | 43 | 5 | cd2ed4cc |
| test2 | all | overall | rul_mae | dlinear | 228.638 [192.558, 270.241] |  |  | 40 | 5 | c066ff8c |
| test2 | all | overall | rul_mae | elasticnet | 144.845 [111.655, 181.870] |  |  | 40 | 5 | 6228f90c |
| test2 | all | overall | rul_mae | gru | 181.852 [144.439, 224.114] |  |  | 40 | 5 | 68c083f5 |
| test2 | all | overall | rul_mae | itransformer | 132.495 [114.716, 152.479] |  |  | 40 | 5 | 1f7dadba |
| test2 | all | overall | rul_mae | itransformer_sc | 119.174 [101.336, 138.518] |  |  | 40 | 5 | 4a0a69dd |
| test2 | all | overall | rul_mae | lgbm | 184.111 [146.696, 226.053] |  |  | 40 | 5 | b88b5644 |
| test2 | all | overall | rul_mae | lstm | 162.489 [126.112, 203.447] |  |  | 40 | 5 | 7a6e2343 |
| test2 | all | overall | rul_mae | nlinear | 228.602 [192.523, 270.195] |  |  | 40 | 5 | f6a02b2d |
| test2 | all | overall | rul_mae | patchtst | 439.806 [396.156, 488.354] |  |  | 40 | 5 | 5b64c567 |
| test2 | all | overall | rul_mae | rlinear | 500.895 [456.237, 550.052] |  |  | 40 | 5 | aa9b25f1 |
| test2 | all | overall | rul_mae | transformer | 197.530 [158.876, 241.623] |  |  | 40 | 5 | cd2ed4cc |
| test2 | start_points | overall | rul_mae | dlinear | 268.875 [221.856, 322.296] |  |  | 40 | 5 | c066ff8c |
| test2 | start_points | overall | rul_mae | elasticnet | 174.555 [132.039, 222.183] |  |  | 40 | 5 | 6228f90c |
| test2 | start_points | overall | rul_mae | gru | 222.226 [174.619, 275.988] |  |  | 40 | 5 | 68c083f5 |
| test2 | start_points | overall | rul_mae | itransformer | 148.814 [121.862, 178.203] |  |  | 40 | 5 | 1f7dadba |
| test2 | start_points | overall | rul_mae | itransformer_sc | 140.132 [113.587, 169.878] |  |  | 40 | 5 | 4a0a69dd |
| test2 | start_points | overall | rul_mae | lgbm | 225.294 [177.597, 278.713] |  |  | 40 | 5 | b88b5644 |
| test2 | start_points | overall | rul_mae | lstm | 198.626 [151.921, 251.321] |  |  | 40 | 5 | 7a6e2343 |
| test2 | start_points | overall | rul_mae | nlinear | 268.839 [221.819, 322.262] |  |  | 40 | 5 | f6a02b2d |
| test2 | start_points | overall | rul_mae | patchtst | 545.111 [491.458, 604.655] |  |  | 40 | 5 | 5b64c567 |
| test2 | start_points | overall | rul_mae | rlinear | 608.419 [551.652, 670.555] |  |  | 40 | 5 | aa9b25f1 |
| test2 | start_points | overall | rul_mae | transformer | 236.446 [186.416, 293.541] |  |  | 40 | 5 | cd2ed4cc |

### toyota_soh

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rmse | dlinear | 0.126 [0.075, 0.186] | p=2.5e-12 (vs prev_soh) |  | 43 | 5 | 3ac7bfd2 |
| test1 | all | overall | rmse | elasticnet | 0.129 [0.077, 0.189] | p=2.5e-12 (vs prev_soh) |  | 43 | 5 | 46575c2e |
| test1 | all | overall | rmse | gru | 0.136 [0.082, 0.199] | p=2.5e-12 (vs prev_soh) |  | 43 | 5 | 3ddf16a8 |
| test1 | all | overall | rmse | itransformer | 0.111 [0.067, 0.163] | p=2.5e-12 (vs prev_soh) |  | 43 | 5 | 86cda30d |
| test1 | all | overall | rmse | itransformer_sc | 0.111 [0.067, 0.163] | p=2.5e-12 (vs prev_soh) |  | 43 | 5 | 38d1aefd |
| test1 | all | overall | rmse | lgbm | 0.133 [0.079, 0.196] | p=2.5e-12 (vs prev_soh) |  | 43 | 5 | ac42ccf2 |
| test1 | all | overall | rmse | lstm | 0.135 [0.082, 0.199] | p=2.5e-12 (vs prev_soh) |  | 43 | 5 | cd05dc09 |
| test1 | all | overall | rmse | nlinear | 0.126 [0.075, 0.185] | p=2.5e-12 (vs prev_soh) |  | 43 | 5 | c114a71d |
| test1 | all | overall | rmse | patchtst | 0.109 [0.066, 0.159] | p=2.5e-12 (vs prev_soh) |  | 43 | 5 | 93bc379a |
| test1 | all | overall | rmse | prev_soh | 0.158 [0.106, 0.219] |  |  | 43 | 5 | 7e056afa |
| test1 | all | overall | rmse | rlinear | 0.124 [0.073, 0.182] | p=2.5e-12 (vs prev_soh) |  | 43 | 5 | e63748eb |
| test1 | all | overall | rmse | transformer | 0.139 [0.085, 0.202] | p=7.5e-12 (vs prev_soh) |  | 43 | 5 | 56c061b1 |
| test1 | start_points | overall | rmse | dlinear | 0.047 [0.025, 0.081] | p=0.00783 (vs prev_soh) |  | 43 | 5 | 3ac7bfd2 |
| test1 | start_points | overall | rmse | elasticnet | 0.040 [0.026, 0.058] | p=0.029 (vs prev_soh) |  | 43 | 5 | 46575c2e |
| test1 | start_points | overall | rmse | gru | 0.035 [0.023, 0.051] | p=0.00255 (vs prev_soh) |  | 43 | 5 | 3ddf16a8 |
| test1 | start_points | overall | rmse | itransformer | 0.028 [0.021, 0.037] | p=0.00427 (vs prev_soh) |  | 43 | 5 | 86cda30d |
| test1 | start_points | overall | rmse | itransformer_sc | 0.028 [0.020, 0.038] | p=0.00891 (vs prev_soh) |  | 43 | 5 | 38d1aefd |
| test1 | start_points | overall | rmse | lgbm | 0.031 [0.019, 0.047] | p=6.17e-05 (vs prev_soh) |  | 43 | 5 | ac42ccf2 |
| test1 | start_points | overall | rmse | lstm | 0.035 [0.023, 0.050] | p=0.00255 (vs prev_soh) |  | 43 | 5 | cd05dc09 |
| test1 | start_points | overall | rmse | nlinear | 0.054 [0.031, 0.083] | p=0.138 (vs prev_soh) |  | 43 | 5 | c114a71d |
| test1 | start_points | overall | rmse | patchtst | 0.028 [0.022, 0.037] | p=0.0081 (vs prev_soh) |  | 43 | 5 | 93bc379a |
| test1 | start_points | overall | rmse | prev_soh | 0.041 [0.030, 0.056] |  |  | 43 | 5 | 7e056afa |
| test1 | start_points | overall | rmse | rlinear | 0.057 [0.026, 0.109] | p=0.0085 (vs prev_soh) |  | 43 | 5 | e63748eb |
| test1 | start_points | overall | rmse | transformer | 0.038 [0.027, 0.054] | p=0.138 (vs prev_soh) |  | 43 | 5 | 56c061b1 |
| test2 | all | overall | rmse | dlinear | 0.016 [0.013, 0.018] | p=2e-11 (vs prev_soh) |  | 40 | 5 | 3ac7bfd2 |
| test2 | all | overall | rmse | elasticnet | 0.024 [0.022, 0.026] | p=2.42e-10 (vs prev_soh) |  | 40 | 5 | 46575c2e |
| test2 | all | overall | rmse | gru | 0.049 [0.045, 0.053] | p=3.12e-05 (vs prev_soh) |  | 40 | 5 | 3ddf16a8 |
| test2 | all | overall | rmse | itransformer | 0.023 [0.022, 0.025] | p=1e-09 (vs prev_soh) |  | 40 | 5 | 86cda30d |
| test2 | all | overall | rmse | itransformer_sc | 0.036 [0.033, 0.039] | p=0.9 (vs prev_soh) |  | 40 | 5 | 38d1aefd |
| test2 | all | overall | rmse | lgbm | 0.024 [0.021, 0.026] | p=6e-10 (vs prev_soh) |  | 40 | 5 | ac42ccf2 |
| test2 | all | overall | rmse | lstm | 0.024 [0.022, 0.026] | p=1e-09 (vs prev_soh) |  | 40 | 5 | cd05dc09 |
| test2 | all | overall | rmse | nlinear | 0.017 [0.015, 0.020] | p=2e-11 (vs prev_soh) |  | 40 | 5 | c114a71d |
| test2 | all | overall | rmse | patchtst | 0.014 [0.011, 0.016] | p=2e-11 (vs prev_soh) |  | 40 | 5 | 93bc379a |
| test2 | all | overall | rmse | prev_soh | 0.036 [0.034, 0.038] |  |  | 40 | 5 | 7e056afa |
| test2 | all | overall | rmse | rlinear | 0.015 [0.013, 0.018] | p=2e-11 (vs prev_soh) |  | 40 | 5 | e63748eb |
| test2 | all | overall | rmse | transformer | 0.038 [0.035, 0.040] | p=0.443 (vs prev_soh) |  | 40 | 5 | 56c061b1 |
| test2 | start_points | overall | rmse | dlinear | 0.015 [0.009, 0.021] | p=1.04e-06 (vs prev_soh) |  | 40 | 5 | 3ac7bfd2 |
| test2 | start_points | overall | rmse | elasticnet | 0.022 [0.016, 0.029] | p=0.00673 (vs prev_soh) |  | 40 | 5 | 46575c2e |
| test2 | start_points | overall | rmse | gru | 0.049 [0.045, 0.054] | p=1.1e-09 (vs prev_soh) |  | 40 | 5 | 3ddf16a8 |
| test2 | start_points | overall | rmse | itransformer | 0.025 [0.022, 0.029] | p=0.02 (vs prev_soh) |  | 40 | 5 | 86cda30d |
| test2 | start_points | overall | rmse | itransformer_sc | 0.040 [0.036, 0.044] | p=1.43e-06 (vs prev_soh) |  | 40 | 5 | 38d1aefd |
| test2 | start_points | overall | rmse | lgbm | 0.023 [0.018, 0.030] | p=0.00357 (vs prev_soh) |  | 40 | 5 | ac42ccf2 |
| test2 | start_points | overall | rmse | lstm | 0.022 [0.017, 0.029] | p=0.024 (vs prev_soh) |  | 40 | 5 | cd05dc09 |
| test2 | start_points | overall | rmse | nlinear | 0.016 [0.011, 0.023] | p=0.024 (vs prev_soh) |  | 40 | 5 | c114a71d |
| test2 | start_points | overall | rmse | patchtst | 0.012 [0.007, 0.018] | p=6.1e-08 (vs prev_soh) |  | 40 | 5 | 93bc379a |
| test2 | start_points | overall | rmse | prev_soh | 0.018 [0.013, 0.025] |  |  | 40 | 5 | 7e056afa |
| test2 | start_points | overall | rmse | rlinear | 0.014 [0.009, 0.021] | p=7.67e-06 (vs prev_soh) |  | 40 | 5 | e63748eb |
| test2 | start_points | overall | rmse | transformer | 0.037 [0.033, 0.042] | p=1.27e-09 (vs prev_soh) |  | 40 | 5 | 56c061b1 |

## Mean rank (dataset x task x split x policy x headline metric)

| model | mean rank | conditions | missing |
|---|---|---|---|
| itransformer | 3.08 | 40 | 0 |
| itransformer_sc | 3.95 | 40 | 0 |
| lgbm | 4.55 | 40 | 0 |
| patchtst | 4.65 | 40 | 0 |
| nlinear | 6.15 | 40 | 0 |
| lstm | 6.47 | 40 | 0 |
| rlinear | 7.17 | 40 | 0 |
| elasticnet | 7.35 | 40 | 0 |
| gru | 7.72 | 40 | 0 |
| prev_soh | 8.88 | 8 | 32 |
| dlinear | 9.03 | 40 | 0 |
| transformer | 9.28 | 40 | 0 |
| persistence | 10.12 | 24 | 16 |
| last_slope | 10.25 | 24 | 16 |

## Calibration (90 % intervals; PICP target 0.90 +/- 0.05; MPIW in %SOH or cycles)

Raw = stored (0.05, 0.95) quantiles; cal = CQR with pooled inner-val residuals (PROTOCOL §3/§5). Models without inner-val predictions (GPR) have raw only. mean [95% cluster-bootstrap CI over cells].

| dataset | task | policy | horizon | model | PICP raw | PICP cal | MPIW raw | MPIW cal | cells |
|---|---|---|---|---|---|---|---|---|---|
| calce | forecast | all | 1 | dlinear | 0.959 [0.954, 0.965] | 0.902 [0.897, 0.908] | 13.500 [13.368, 13.596] | 9.861 [9.728, 9.955] | 4 |
| calce | forecast | all | 1 | elasticnet | 0.000 [0.000, 0.000] | 0.905 [0.896, 0.914] | 0.000 [0.000, 0.000] | 2.274 [2.211, 2.336] | 4 |
| calce | forecast | all | 1 | gru | 0.946 [0.938, 0.952] | 0.935 [0.929, 0.942] | 4.613 [4.152, 5.165] | 4.393 [3.969, 4.875] | 4 |
| calce | forecast | all | 1 | itransformer | 0.900 [0.890, 0.909] | 0.907 [0.898, 0.916] | 2.697 [2.584, 2.810] | 2.777 [2.687, 2.882] | 4 |
| calce | forecast | all | 1 | itransformer_sc | 0.905 [0.898, 0.913] | 0.906 [0.902, 0.910] | 2.734 [2.666, 2.801] | 2.772 [2.729, 2.847] | 4 |
| calce | forecast | all | 1 | lgbm | 0.903 [0.897, 0.911] | 0.913 [0.903, 0.922] | 3.586 [3.403, 3.799] | 3.722 [3.553, 3.932] | 4 |
| calce | forecast | all | 1 | lstm | 0.924 [0.914, 0.931] | 0.923 [0.909, 0.935] | 3.267 [3.081, 3.570] | 3.280 [3.097, 3.581] | 4 |
| calce | forecast | all | 1 | nlinear | 0.897 [0.878, 0.915] | 0.902 [0.880, 0.921] | 3.169 [3.067, 3.244] | 3.242 [3.106, 3.332] | 4 |
| calce | forecast | all | 1 | patchtst | 0.938 [0.927, 0.945] | 0.921 [0.911, 0.931] | 3.930 [3.815, 4.068] | 3.687 [3.544, 3.830] | 4 |
| calce | forecast | all | 1 | rlinear | 0.900 [0.892, 0.909] | 0.916 [0.908, 0.924] | 3.905 [3.794, 4.003] | 4.048 [3.933, 4.127] | 4 |
| calce | forecast | all | 1 | transformer | 0.963 [0.958, 0.969] | 0.952 [0.944, 0.959] | 9.094 [8.227, 9.796] | 6.848 [6.305, 7.323] | 4 |
| calce | forecast | all | 10 | dlinear | 0.913 [0.908, 0.917] | 0.901 [0.895, 0.905] | 12.702 [12.543, 12.831] | 11.280 [11.089, 11.443] | 4 |
| calce | forecast | all | 10 | elasticnet | 0.000 [0.000, 0.000] | 0.897 [0.871, 0.919] | 0.000 [0.000, 0.000] | 5.332 [5.072, 5.503] | 4 |
| calce | forecast | all | 10 | gru | 0.902 [0.891, 0.921] | 0.913 [0.897, 0.929] | 5.958 [5.650, 6.266] | 6.134 [6.046, 6.233] | 4 |
| calce | forecast | all | 10 | itransformer | 0.860 [0.832, 0.888] | 0.904 [0.876, 0.933] | 4.884 [4.767, 5.000] | 5.511 [5.336, 5.655] | 4 |
| calce | forecast | all | 10 | itransformer_sc | 0.873 [0.840, 0.907] | 0.904 [0.877, 0.930] | 5.156 [4.949, 5.363] | 5.658 [5.448, 5.869] | 4 |
| calce | forecast | all | 10 | lgbm | 0.877 [0.859, 0.900] | 0.907 [0.889, 0.926] | 5.208 [4.940, 5.476] | 5.650 [5.399, 5.902] | 4 |
| calce | forecast | all | 10 | lstm | 0.882 [0.838, 0.916] | 0.904 [0.862, 0.935] | 5.350 [5.029, 5.777] | 5.757 [5.403, 6.148] | 4 |
| calce | forecast | all | 10 | nlinear | 0.899 [0.876, 0.922] | 0.903 [0.879, 0.925] | 5.848 [5.721, 5.976] | 5.933 [5.811, 6.075] | 4 |
| calce | forecast | all | 10 | patchtst | 0.895 [0.864, 0.920] | 0.906 [0.876, 0.932] | 6.167 [5.999, 6.308] | 6.352 [6.156, 6.486] | 4 |
| calce | forecast | all | 10 | rlinear | 0.870 [0.838, 0.902] | 0.906 [0.880, 0.931] | 6.553 [6.442, 6.664] | 7.106 [6.872, 7.358] | 4 |
| calce | forecast | all | 10 | transformer | 0.952 [0.945, 0.960] | 0.930 [0.919, 0.942] | 10.157 [9.636, 10.679] | 8.215 [7.823, 8.442] | 4 |
| calce | forecast | all | 25 | dlinear | 0.915 [0.899, 0.927] | 0.902 [0.883, 0.916] | 13.908 [13.742, 14.074] | 12.804 [12.641, 12.966] | 4 |
| calce | forecast | all | 25 | elasticnet | 0.000 [0.000, 0.000] | 0.904 [0.873, 0.927] | 0.000 [0.000, 0.000] | 8.968 [8.573, 9.333] | 4 |
| calce | forecast | all | 25 | gru | 0.883 [0.852, 0.914] | 0.912 [0.889, 0.937] | 7.417 [7.044, 7.790] | 8.094 [7.636, 8.499] | 4 |
| calce | forecast | all | 25 | itransformer | 0.828 [0.778, 0.876] | 0.895 [0.848, 0.942] | 5.942 [5.670, 6.169] | 7.214 [6.637, 7.593] | 4 |
| calce | forecast | all | 25 | itransformer_sc | 0.855 [0.801, 0.905] | 0.901 [0.858, 0.934] | 6.601 [6.102, 7.012] | 7.443 [6.922, 7.853] | 4 |
| calce | forecast | all | 25 | lgbm | 0.848 [0.803, 0.889] | 0.908 [0.850, 0.939] | 6.583 [6.197, 6.845] | 7.714 [7.028, 8.193] | 4 |
| calce | forecast | all | 25 | lstm | 0.868 [0.822, 0.907] | 0.907 [0.869, 0.942] | 6.875 [6.321, 7.428] | 7.815 [7.165, 8.336] | 4 |
| calce | forecast | all | 25 | nlinear | 0.892 [0.860, 0.913] | 0.901 [0.868, 0.923] | 9.571 [9.424, 9.740] | 9.802 [9.609, 9.945] | 4 |
| calce | forecast | all | 25 | patchtst | 0.881 [0.827, 0.915] | 0.898 [0.848, 0.932] | 8.640 [8.123, 9.024] | 8.965 [8.489, 9.285] | 4 |
| calce | forecast | all | 25 | rlinear | 0.869 [0.826, 0.905] | 0.903 [0.866, 0.930] | 9.204 [8.843, 9.695] | 9.774 [9.363, 10.251] | 4 |
| calce | forecast | all | 25 | transformer | 0.947 [0.930, 0.959] | 0.927 [0.895, 0.951] | 11.145 [10.112, 12.530] | 9.632 [8.472, 11.024] | 4 |
| calce | forecast | all | 50 | dlinear | 0.774 [0.753, 0.789] | 0.900 [0.888, 0.917] | 15.201 [15.107, 15.340] | 22.250 [21.890, 22.838] | 4 |
| calce | forecast | all | 50 | elasticnet | 0.000 [0.000, 0.000] | 0.900 [0.864, 0.949] | 0.000 [0.000, 0.000] | 12.151 [11.112, 13.294] | 4 |
| calce | forecast | all | 50 | gru | 0.871 [0.824, 0.917] | 0.912 [0.870, 0.954] | 8.980 [8.111, 9.954] | 10.360 [9.558, 11.538] | 4 |
| calce | forecast | all | 50 | itransformer | 0.799 [0.741, 0.832] | 0.896 [0.857, 0.935] | 6.720 [6.366, 7.075] | 8.968 [8.334, 9.378] | 4 |
| calce | forecast | all | 50 | itransformer_sc | 0.837 [0.752, 0.907] | 0.888 [0.812, 0.946] | 7.720 [6.929, 8.303] | 9.056 [8.134, 9.803] | 4 |
| calce | forecast | all | 50 | lgbm | 0.805 [0.719, 0.890] | 0.903 [0.826, 0.952] | 7.101 [6.246, 8.021] | 9.251 [7.884, 10.433] | 4 |
| calce | forecast | all | 50 | lstm | 0.852 [0.794, 0.915] | 0.899 [0.844, 0.951] | 7.828 [7.198, 8.405] | 9.398 [8.587, 10.152] | 4 |
| calce | forecast | all | 50 | nlinear | 0.888 [0.842, 0.915] | 0.903 [0.856, 0.929] | 12.547 [12.207, 12.928] | 12.958 [12.591, 13.325] | 4 |
| calce | forecast | all | 50 | patchtst | 0.867 [0.761, 0.923] | 0.893 [0.799, 0.948] | 11.137 [9.855, 11.896] | 11.697 [10.421, 12.568] | 4 |
| calce | forecast | all | 50 | rlinear | 0.864 [0.801, 0.917] | 0.894 [0.828, 0.940] | 11.966 [11.350, 12.588] | 12.803 [11.999, 13.559] | 4 |
| calce | forecast | all | 50 | transformer | 0.926 [0.902, 0.951] | 0.908 [0.870, 0.943] | 11.522 [10.590, 12.455] | 10.601 [9.574, 11.631] | 4 |
| calce | forecast | all | 100 | dlinear | 0.842 [0.825, 0.862] | 0.900 [0.884, 0.917] | 21.960 [21.765, 22.128] | 25.613 [25.265, 25.854] | 4 |
| calce | forecast | all | 100 | elasticnet | 0.000 [0.000, 0.000] | 0.899 [0.858, 0.940] | 0.000 [0.000, 0.000] | 14.474 [14.057, 15.169] | 4 |
| calce | forecast | all | 100 | gru | 0.813 [0.738, 0.889] | 0.902 [0.871, 0.950] | 9.941 [9.330, 10.747] | 12.262 [11.720, 13.116] | 4 |
| calce | forecast | all | 100 | itransformer | 0.734 [0.633, 0.794] | 0.887 [0.832, 0.931] | 8.698 [7.999, 9.310] | 12.775 [11.530, 13.795] | 4 |
| calce | forecast | all | 100 | itransformer_sc | 0.789 [0.704, 0.857] | 0.882 [0.813, 0.941] | 9.570 [8.699, 10.292] | 12.389 [11.535, 13.242] | 4 |
| calce | forecast | all | 100 | lgbm | 0.762 [0.676, 0.839] | 0.898 [0.807, 0.954] | 9.060 [7.635, 10.291] | 12.461 [10.399, 13.955] | 4 |
| calce | forecast | all | 100 | lstm | 0.801 [0.718, 0.884] | 0.891 [0.854, 0.943] | 8.929 [8.229, 9.477] | 11.478 [10.896, 11.982] | 4 |
| calce | forecast | all | 100 | nlinear | 0.890 [0.818, 0.927] | 0.903 [0.827, 0.949] | 18.888 [18.165, 19.610] | 19.443 [18.509, 20.220] | 4 |
| calce | forecast | all | 100 | patchtst | 0.844 [0.720, 0.929] | 0.896 [0.804, 0.965] | 15.946 [14.338, 17.102] | 17.596 [16.059, 18.907] | 4 |
| calce | forecast | all | 100 | rlinear | 0.850 [0.773, 0.911] | 0.889 [0.824, 0.941] | 17.149 [16.158, 18.090] | 19.135 [17.825, 20.308] | 4 |
| calce | forecast | all | 100 | transformer | 0.906 [0.861, 0.950] | 0.901 [0.850, 0.952] | 12.794 [12.136, 13.566] | 12.516 [11.422, 13.402] | 4 |
| calce | forecast | start_points | 1 | dlinear | 0.990 [0.970, 1.000] | 0.980 [0.960, 1.000] | 14.686 [14.472, 14.919] | 11.047 [10.811, 11.302] | 4 |
| calce | forecast | start_points | 1 | elasticnet | 0.000 [0.000, 0.000] | 1.000 [1.000, 1.000] | 0.000 [0.000, 0.000] | 2.274 [2.211, 2.336] | 4 |
| calce | forecast | start_points | 1 | gru | 0.990 [0.970, 1.000] | 0.990 [0.970, 1.000] | 3.291 [2.982, 3.723] | 3.070 [2.778, 3.433] | 4 |
| calce | forecast | start_points | 1 | itransformer | 0.900 [0.800, 1.000] | 0.900 [0.800, 1.000] | 1.649 [1.372, 1.926] | 1.729 [1.425, 2.034] | 4 |
| calce | forecast | start_points | 1 | itransformer_sc | 0.930 [0.790, 1.000] | 0.930 [0.790, 1.000] | 1.857 [1.669, 1.991] | 1.895 [1.716, 2.075] | 4 |
| calce | forecast | start_points | 1 | lgbm | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 3.193 [2.635, 3.752] | 3.330 [2.774, 3.885] | 4 |
| calce | forecast | start_points | 1 | lstm | 0.980 [0.940, 1.000] | 0.960 [0.880, 1.000] | 2.276 [2.025, 2.527] | 2.289 [2.040, 2.549] | 4 |
| calce | forecast | start_points | 1 | nlinear | 0.950 [0.850, 1.000] | 0.950 [0.850, 1.000] | 2.103 [1.957, 2.277] | 2.176 [2.029, 2.361] | 4 |
| calce | forecast | start_points | 1 | patchtst | 0.970 [0.910, 1.000] | 0.950 [0.850, 1.000] | 2.627 [2.322, 2.852] | 2.384 [2.126, 2.578] | 4 |
| calce | forecast | start_points | 1 | rlinear | 0.960 [0.880, 1.000] | 0.960 [0.880, 1.000] | 2.484 [2.174, 2.772] | 2.627 [2.309, 2.917] | 4 |
| calce | forecast | start_points | 1 | transformer | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 7.805 [6.847, 8.763] | 5.560 [4.900, 6.219] | 4 |
| calce | forecast | start_points | 10 | dlinear | 0.930 [0.920, 0.950] | 0.970 [0.940, 1.000] | 13.656 [13.249, 13.941] | 12.234 [11.801, 12.518] | 4 |
| calce | forecast | start_points | 10 | elasticnet | 0.000 [0.000, 0.000] | 0.950 [0.850, 1.000] | 0.000 [0.000, 0.000] | 5.332 [5.072, 5.503] | 4 |
| calce | forecast | start_points | 10 | gru | 0.930 [0.820, 1.000] | 0.940 [0.850, 1.000] | 4.117 [3.781, 4.618] | 4.293 [3.997, 4.687] | 4 |
| calce | forecast | start_points | 10 | itransformer | 0.710 [0.520, 0.900] | 0.880 [0.800, 0.960] | 2.850 [2.329, 3.372] | 3.478 [2.943, 4.012] | 4 |
| calce | forecast | start_points | 10 | itransformer_sc | 0.930 [0.820, 1.000] | 0.950 [0.850, 1.000] | 3.338 [2.865, 3.643] | 3.840 [3.336, 4.184] | 4 |
| calce | forecast | start_points | 10 | lgbm | 0.950 [0.850, 1.000] | 0.950 [0.850, 1.000] | 4.098 [3.852, 4.434] | 4.540 [4.329, 4.810] | 4 |
| calce | forecast | start_points | 10 | lstm | 0.930 [0.790, 1.000] | 0.950 [0.850, 1.000] | 3.615 [3.363, 3.920] | 4.023 [3.696, 4.354] | 4 |
| calce | forecast | start_points | 10 | nlinear | 0.950 [0.850, 1.000] | 0.950 [0.850, 1.000] | 3.999 [3.725, 4.225] | 4.084 [3.784, 4.277] | 4 |
| calce | forecast | start_points | 10 | patchtst | 0.940 [0.850, 1.000] | 0.940 [0.850, 1.000] | 4.091 [3.570, 4.565] | 4.277 [3.699, 4.734] | 4 |
| calce | forecast | start_points | 10 | rlinear | 0.940 [0.850, 1.000] | 0.950 [0.850, 1.000] | 4.565 [3.985, 5.119] | 5.118 [4.414, 5.759] | 4 |
| calce | forecast | start_points | 10 | transformer | 0.980 [0.940, 1.000] | 0.970 [0.910, 1.000] | 8.279 [7.735, 9.009] | 6.337 [5.782, 6.893] | 4 |
| calce | forecast | start_points | 25 | dlinear | 0.960 [0.910, 1.000] | 0.950 [0.880, 1.000] | 14.094 [13.791, 14.306] | 12.990 [12.682, 13.199] | 4 |
| calce | forecast | start_points | 25 | elasticnet | 0.000 [0.000, 0.000] | 1.000 [1.000, 1.000] | 0.000 [0.000, 0.000] | 8.968 [8.573, 9.333] | 4 |
| calce | forecast | start_points | 25 | gru | 0.890 [0.780, 1.000] | 0.940 [0.880, 1.000] | 5.611 [5.427, 5.914] | 6.287 [5.968, 6.690] | 4 |
| calce | forecast | start_points | 25 | itransformer | 0.720 [0.500, 0.940] | 0.900 [0.700, 1.000] | 3.267 [2.685, 3.848] | 4.539 [3.798, 5.165] | 4 |
| calce | forecast | start_points | 25 | itransformer_sc | 0.850 [0.700, 1.000] | 0.870 [0.740, 1.000] | 4.243 [3.704, 4.570] | 5.086 [4.532, 5.403] | 4 |
| calce | forecast | start_points | 25 | lgbm | 0.750 [0.500, 0.950] | 0.900 [0.800, 1.000] | 5.678 [5.294, 5.887] | 6.809 [6.409, 7.210] | 4 |
| calce | forecast | start_points | 25 | lstm | 0.880 [0.760, 1.000] | 0.970 [0.940, 1.000] | 5.052 [4.759, 5.344] | 5.992 [5.693, 6.253] | 4 |
| calce | forecast | start_points | 25 | nlinear | 0.810 [0.580, 1.000] | 0.850 [0.670, 1.000] | 7.887 [7.733, 8.027] | 8.118 [8.010, 8.200] | 4 |
| calce | forecast | start_points | 25 | patchtst | 0.800 [0.570, 0.980] | 0.810 [0.580, 1.000] | 6.407 [5.807, 7.007] | 6.732 [6.132, 7.332] | 4 |
| calce | forecast | start_points | 25 | rlinear | 0.790 [0.650, 0.940] | 0.800 [0.650, 0.950] | 6.766 [6.323, 7.168] | 7.336 [6.890, 7.797] | 4 |
| calce | forecast | start_points | 25 | transformer | 1.000 [1.000, 1.000] | 0.960 [0.920, 1.000] | 8.790 [8.187, 9.267] | 7.277 [7.116, 7.458] | 4 |
| calce | forecast | start_points | 50 | dlinear | 0.910 [0.890, 0.920] | 0.990 [0.970, 1.000] | 16.129 [15.630, 16.629] | 23.178 [22.422, 23.954] | 4 |
| calce | forecast | start_points | 50 | elasticnet | 0.000 [0.000, 0.000] | 0.950 [0.850, 1.000] | 0.000 [0.000, 0.000] | 12.151 [11.112, 13.294] | 4 |
| calce | forecast | start_points | 50 | gru | 0.840 [0.740, 0.940] | 0.940 [0.850, 1.000] | 6.448 [6.096, 6.779] | 7.828 [7.336, 8.321] | 4 |
| calce | forecast | start_points | 50 | itransformer | 0.820 [0.660, 0.960] | 0.950 [0.850, 1.000] | 3.794 [3.087, 4.500] | 6.041 [5.165, 6.730] | 4 |
| calce | forecast | start_points | 50 | itransformer_sc | 0.930 [0.850, 1.000] | 0.950 [0.850, 1.000] | 5.296 [4.688, 5.879] | 6.632 [5.893, 7.325] | 4 |
| calce | forecast | start_points | 50 | lgbm | 0.650 [0.500, 0.800] | 0.950 [0.850, 1.000] | 4.964 [4.493, 5.523] | 7.114 [6.400, 7.781] | 4 |
| calce | forecast | start_points | 50 | lstm | 0.870 [0.760, 0.980] | 0.950 [0.850, 1.000] | 5.369 [5.182, 5.612] | 6.939 [6.538, 7.339] | 4 |
| calce | forecast | start_points | 50 | nlinear | 0.900 [0.800, 1.000] | 0.930 [0.850, 1.000] | 10.644 [10.496, 10.822] | 11.055 [10.873, 11.202] | 4 |
| calce | forecast | start_points | 50 | patchtst | 0.920 [0.810, 0.990] | 0.950 [0.850, 1.000] | 9.323 [8.159, 10.144] | 9.883 [8.653, 10.910] | 4 |
| calce | forecast | start_points | 50 | rlinear | 0.930 [0.850, 1.000] | 0.950 [0.850, 1.000] | 9.568 [9.185, 10.228] | 10.406 [9.859, 11.035] | 4 |
| calce | forecast | start_points | 50 | transformer | 0.960 [0.880, 1.000] | 0.960 [0.880, 1.000] | 9.488 [8.987, 9.989] | 8.567 [8.373, 8.838] | 4 |
| calce | forecast | start_points | 100 | dlinear | 0.970 [0.960, 0.990] | 0.980 [0.960, 1.000] | 20.856 [20.483, 21.391] | 24.509 [24.094, 25.155] | 4 |
| calce | forecast | start_points | 100 | elasticnet | 0.000 [0.000, 0.000] | 1.000 [1.000, 1.000] | 0.000 [0.000, 0.000] | 14.474 [14.057, 15.169] | 4 |
| calce | forecast | start_points | 100 | gru | 0.880 [0.700, 1.000] | 0.980 [0.940, 1.000] | 8.388 [8.201, 8.575] | 10.709 [10.348, 11.039] | 4 |
| calce | forecast | start_points | 100 | itransformer | 0.800 [0.570, 0.960] | 0.990 [0.970, 1.000] | 6.009 [4.747, 7.272] | 10.086 [8.473, 11.338] | 4 |
| calce | forecast | start_points | 100 | itransformer_sc | 0.880 [0.700, 1.000] | 0.950 [0.850, 1.000] | 7.524 [6.666, 8.381] | 10.342 [9.352, 11.332] | 4 |
| calce | forecast | start_points | 100 | lgbm | 0.750 [0.650, 0.800] | 0.950 [0.850, 1.000] | 6.424 [5.634, 7.214] | 9.825 [8.346, 11.109] | 4 |
| calce | forecast | start_points | 100 | lstm | 0.890 [0.770, 0.980] | 1.000 [1.000, 1.000] | 7.300 [6.777, 7.670] | 9.849 [9.143, 10.556] | 4 |
| calce | forecast | start_points | 100 | nlinear | 0.950 [0.850, 1.000] | 0.950 [0.850, 1.000] | 15.506 [15.107, 15.801] | 16.061 [15.625, 16.649] | 4 |
| calce | forecast | start_points | 100 | patchtst | 0.920 [0.760, 1.000] | 0.950 [0.850, 1.000] | 13.325 [12.160, 14.485] | 14.975 [13.704, 16.374] | 4 |
| calce | forecast | start_points | 100 | rlinear | 0.900 [0.700, 1.000] | 0.900 [0.700, 1.000] | 12.489 [11.630, 13.537] | 14.475 [13.618, 15.533] | 4 |
| calce | forecast | start_points | 100 | transformer | 0.950 [0.880, 1.000] | 0.990 [0.970, 1.000] | 10.762 [10.119, 11.464] | 10.484 [9.596, 11.373] | 4 |
| calce | rul | all | 0 | dlinear | 0.848 [0.777, 0.919] | 0.903 [0.863, 0.945] | 439.820 [425.050, 455.100] | 465.706 [451.001, 480.028] | 4 |
| calce | rul | all | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.876 [0.744, 0.985] | 0.000 [0.000, 0.000] | 789.093 [614.008, 1014.653] | 4 |
| calce | rul | all | 0 | gru | 0.787 [0.685, 0.889] | 0.859 [0.758, 0.952] | 260.973 [216.102, 305.845] | 292.727 [228.843, 356.610] | 4 |
| calce | rul | all | 0 | itransformer | 0.698 [0.345, 0.954] | 0.738 [0.376, 0.990] | 215.929 [147.695, 272.048] | 248.862 [171.777, 318.804] | 4 |
| calce | rul | all | 0 | itransformer_sc | 0.740 [0.377, 0.955] | 0.775 [0.412, 0.982] | 222.627 [157.079, 277.014] | 260.823 [187.296, 313.853] | 4 |
| calce | rul | all | 0 | lgbm | 0.730 [0.617, 0.869] | 0.864 [0.728, 1.000] | 295.575 [260.474, 322.010] | 374.294 [328.028, 414.598] | 4 |
| calce | rul | all | 0 | lstm | 0.672 [0.337, 0.926] | 0.753 [0.400, 0.976] | 210.296 [153.502, 255.660] | 253.007 [192.395, 301.627] | 4 |
| calce | rul | all | 0 | nlinear | 0.827 [0.733, 0.921] | 0.897 [0.853, 0.945] | 435.756 [411.304, 460.207] | 466.155 [446.851, 483.012] | 4 |
| calce | rul | all | 0 | patchtst | 0.808 [0.784, 0.844] | 0.917 [0.895, 0.942] | 390.326 [365.094, 415.557] | 461.623 [433.453, 489.793] | 4 |
| calce | rul | all | 0 | rlinear | 0.786 [0.746, 0.830] | 0.893 [0.873, 0.912] | 885.422 [828.315, 932.388] | 1004.761 [952.506, 1057.016] | 4 |
| calce | rul | all | 0 | transformer | 0.849 [0.731, 0.952] | 0.874 [0.773, 0.976] | 352.197 [327.845, 381.137] | 373.113 [340.642, 417.210] | 4 |
| calce | rul | start_points | 0 | dlinear | 0.930 [0.860, 1.000] | 0.990 [0.970, 1.000] | 387.356 [371.795, 406.654] | 413.242 [400.193, 430.841] | 4 |
| calce | rul | start_points | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.850 [0.550, 1.000] | 0.000 [0.000, 0.000] | 789.093 [614.008, 1014.653] | 4 |
| calce | rul | start_points | 0 | gru | 0.820 [0.590, 0.970] | 0.900 [0.830, 0.970] | 269.101 [229.533, 308.668] | 300.854 [242.274, 359.434] | 4 |
| calce | rul | start_points | 0 | itransformer | 0.620 [0.240, 0.900] | 0.690 [0.280, 1.000] | 210.002 [146.915, 267.628] | 242.935 [170.997, 308.881] | 4 |
| calce | rul | start_points | 0 | itransformer_sc | 0.710 [0.280, 1.000] | 0.730 [0.280, 1.000] | 227.326 [162.545, 286.807] | 265.522 [195.263, 321.662] | 4 |
| calce | rul | start_points | 0 | lgbm | 0.800 [0.600, 1.000] | 0.900 [0.700, 1.000] | 269.271 [227.780, 300.825] | 347.990 [295.707, 392.956] | 4 |
| calce | rul | start_points | 0 | lstm | 0.570 [0.200, 0.940] | 0.690 [0.240, 0.980] | 198.083 [151.973, 243.098] | 240.794 [190.866, 289.066] | 4 |
| calce | rul | start_points | 0 | nlinear | 0.880 [0.760, 1.000] | 0.940 [0.880, 1.000] | 379.143 [361.440, 404.606] | 409.542 [393.100, 431.523] | 4 |
| calce | rul | start_points | 0 | patchtst | 0.900 [0.800, 1.000] | 0.960 [0.920, 1.000] | 358.729 [340.339, 375.510] | 430.026 [412.845, 442.795] | 4 |
| calce | rul | start_points | 0 | rlinear | 0.820 [0.740, 0.920] | 0.940 [0.850, 1.000] | 764.406 [596.614, 855.440] | 883.745 [701.491, 986.732] | 4 |
| calce | rul | start_points | 0 | transformer | 0.870 [0.610, 1.000] | 0.890 [0.670, 1.000] | 354.397 [329.567, 378.454] | 375.313 [344.970, 417.005] | 4 |
| calce | soh | all | 0 | dlinear | 0.904 [0.890, 0.924] | 0.903 [0.887, 0.925] | 3.273 [3.189, 3.369] | 3.268 [3.164, 3.374] | 4 |
| calce | soh | all | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.903 [0.874, 0.931] | 0.000 [0.000, 0.000] | 1.846 [1.756, 1.936] | 4 |
| calce | soh | all | 0 | gru | 0.900 [0.889, 0.910] | 0.904 [0.893, 0.916] | 3.140 [2.908, 3.431] | 3.176 [2.969, 3.442] | 4 |
| calce | soh | all | 0 | itransformer | 0.869 [0.855, 0.884] | 0.915 [0.905, 0.921] | 1.612 [1.490, 1.734] | 1.890 [1.798, 2.018] | 4 |
| calce | soh | all | 0 | itransformer_sc | 0.861 [0.852, 0.874] | 0.909 [0.903, 0.915] | 1.616 [1.514, 1.748] | 1.907 [1.806, 2.044] | 4 |
| calce | soh | all | 0 | lgbm | 0.827 [0.809, 0.846] | 0.910 [0.889, 0.931] | 2.272 [2.070, 2.434] | 2.729 [2.517, 2.885] | 4 |
| calce | soh | all | 0 | lstm | 0.898 [0.891, 0.911] | 0.900 [0.894, 0.909] | 2.328 [2.236, 2.424] | 2.347 [2.238, 2.455] | 4 |
| calce | soh | all | 0 | nlinear | 0.907 [0.892, 0.922] | 0.909 [0.893, 0.925] | 3.528 [3.365, 3.690] | 3.547 [3.403, 3.682] | 4 |
| calce | soh | all | 0 | patchtst | 0.870 [0.854, 0.883] | 0.907 [0.893, 0.915] | 2.206 [2.103, 2.326] | 2.529 [2.422, 2.637] | 4 |
| calce | soh | all | 0 | rlinear | 0.832 [0.825, 0.839] | 0.903 [0.899, 0.908] | 3.084 [2.979, 3.189] | 3.408 [3.306, 3.510] | 4 |
| calce | soh | all | 0 | transformer | 0.922 [0.914, 0.929] | 0.913 [0.899, 0.924] | 3.032 [2.883, 3.170] | 2.908 [2.739, 3.077] | 4 |
| calce | soh | start_points | 0 | dlinear | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 2.587 [2.399, 2.774] | 2.582 [2.386, 2.764] | 4 |
| calce | soh | start_points | 0 | elasticnet | 0.000 [0.000, 0.000] | 1.000 [1.000, 1.000] | 0.000 [0.000, 0.000] | 1.846 [1.756, 1.936] | 4 |
| calce | soh | start_points | 0 | gru | 0.960 [0.880, 1.000] | 0.960 [0.880, 1.000] | 1.946 [1.775, 2.074] | 1.982 [1.842, 2.082] | 4 |
| calce | soh | start_points | 0 | itransformer | 0.940 [0.850, 1.000] | 1.000 [1.000, 1.000] | 0.798 [0.687, 0.902] | 1.076 [0.953, 1.207] | 4 |
| calce | soh | start_points | 0 | itransformer_sc | 0.900 [0.830, 0.970] | 1.000 [1.000, 1.000] | 0.825 [0.717, 0.946] | 1.116 [1.009, 1.241] | 4 |
| calce | soh | start_points | 0 | lgbm | 0.850 [0.800, 0.950] | 0.950 [0.850, 1.000] | 0.800 [0.692, 0.907] | 1.257 [1.145, 1.373] | 4 |
| calce | soh | start_points | 0 | lstm | 0.950 [0.850, 1.000] | 0.950 [0.850, 1.000] | 1.793 [1.634, 1.919] | 1.812 [1.623, 1.999] | 4 |
| calce | soh | start_points | 0 | nlinear | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 2.582 [2.240, 2.838] | 2.601 [2.248, 2.889] | 4 |
| calce | soh | start_points | 0 | patchtst | 0.870 [0.740, 1.000] | 0.950 [0.850, 1.000] | 1.275 [0.982, 1.467] | 1.597 [1.313, 1.799] | 4 |
| calce | soh | start_points | 0 | rlinear | 0.850 [0.800, 0.950] | 1.000 [1.000, 1.000] | 1.880 [1.360, 2.319] | 2.204 [1.683, 2.635] | 4 |
| calce | soh | start_points | 0 | transformer | 0.980 [0.940, 1.000] | 0.990 [0.970, 1.000] | 2.504 [2.426, 2.583] | 2.380 [2.243, 2.516] | 4 |
| nasa | forecast | all | 1 | dlinear | 0.961 [0.914, 0.991] | 0.898 [0.801, 0.980] | 17.829 [17.005, 18.596] | 10.797 [9.642, 11.880] | 4 |
| nasa | forecast | all | 1 | elasticnet | 0.000 [0.000, 0.000] | 0.884 [0.790, 0.951] | 0.000 [0.000, 0.000] | 2.279 [1.952, 2.576] | 4 |
| nasa | forecast | all | 1 | gru | 0.978 [0.945, 0.995] | 0.944 [0.895, 0.993] | 14.146 [12.565, 15.782] | 12.413 [10.151, 14.675] | 4 |
| nasa | forecast | all | 1 | itransformer | 0.902 [0.876, 0.923] | 0.900 [0.871, 0.920] | 2.404 [2.048, 2.787] | 2.401 [2.049, 2.799] | 4 |
| nasa | forecast | all | 1 | itransformer_sc | 0.900 [0.869, 0.920] | 0.898 [0.857, 0.922] | 2.502 [2.160, 3.036] | 2.487 [2.135, 2.990] | 4 |
| nasa | forecast | all | 1 | lgbm | 0.895 [0.829, 0.960] | 0.909 [0.852, 0.966] | 2.355 [2.087, 2.670] | 2.488 [2.188, 2.855] | 4 |
| nasa | forecast | all | 1 | lstm | 0.945 [0.906, 0.978] | 0.942 [0.897, 0.979] | 9.983 [9.100, 10.867] | 9.544 [8.527, 10.562] | 4 |
| nasa | forecast | all | 1 | nlinear | 0.874 [0.794, 0.953] | 0.905 [0.849, 0.961] | 2.351 [2.150, 2.553] | 2.612 [2.393, 2.832] | 4 |
| nasa | forecast | all | 1 | patchtst | 0.953 [0.943, 0.961] | 0.918 [0.892, 0.943] | 3.867 [3.312, 4.656] | 3.405 [2.874, 4.156] | 4 |
| nasa | forecast | all | 1 | rlinear | 0.858 [0.792, 0.903] | 0.902 [0.854, 0.933] | 2.958 [2.573, 3.530] | 3.320 [2.950, 3.870] | 4 |
| nasa | forecast | all | 1 | transformer | 0.996 [0.994, 0.999] | 0.986 [0.978, 0.995] | 18.036 [15.730, 21.021] | 15.055 [12.276, 18.396] | 4 |
| nasa | forecast | all | 10 | dlinear | 0.906 [0.865, 0.947] | 0.895 [0.838, 0.953] | 20.056 [19.882, 20.292] | 14.669 [14.270, 14.910] | 4 |
| nasa | forecast | all | 10 | elasticnet | 0.000 [0.000, 0.000] | 0.807 [0.498, 1.000] | 0.000 [0.000, 0.000] | 10.381 [8.270, 12.146] | 4 |
| nasa | forecast | all | 10 | gru | 0.934 [0.836, 0.991] | 0.946 [0.872, 0.996] | 16.051 [14.448, 17.236] | 16.681 [14.680, 18.378] | 4 |
| nasa | forecast | all | 10 | itransformer | 0.730 [0.659, 0.801] | 0.899 [0.820, 0.971] | 4.425 [3.924, 4.925] | 6.474 [5.964, 6.883] | 4 |
| nasa | forecast | all | 10 | itransformer_sc | 0.773 [0.677, 0.869] | 0.878 [0.783, 0.966] | 5.166 [4.824, 5.709] | 6.415 [5.972, 7.112] | 4 |
| nasa | forecast | all | 10 | lgbm | 0.842 [0.710, 0.974] | 0.897 [0.803, 0.990] | 5.176 [4.556, 5.812] | 6.688 [6.149, 7.180] | 4 |
| nasa | forecast | all | 10 | lstm | 0.865 [0.756, 0.929] | 0.925 [0.866, 0.983] | 10.782 [9.974, 11.584] | 13.192 [12.131, 14.253] | 4 |
| nasa | forecast | all | 10 | nlinear | 0.827 [0.729, 0.925] | 0.902 [0.817, 0.988] | 5.781 [5.450, 6.112] | 7.443 [6.664, 8.223] | 4 |
| nasa | forecast | all | 10 | patchtst | 0.894 [0.822, 0.934] | 0.898 [0.809, 0.951] | 6.188 [5.379, 7.322] | 6.369 [5.693, 7.460] | 4 |
| nasa | forecast | all | 10 | rlinear | 0.782 [0.681, 0.854] | 0.887 [0.779, 0.956] | 6.854 [5.865, 8.121] | 8.717 [8.007, 9.863] | 4 |
| nasa | forecast | all | 10 | transformer | 0.988 [0.973, 0.996] | 0.933 [0.877, 0.989] | 21.019 [15.727, 30.051] | 18.103 [12.207, 27.795] | 4 |
| nasa | forecast | all | 25 | dlinear | 0.927 [0.867, 0.975] | 0.902 [0.810, 0.981] | 15.813 [15.129, 16.496] | 13.754 [12.400, 15.108] | 4 |
| nasa | forecast | all | 25 | elasticnet | 0.000 [0.000, 0.000] | 0.778 [0.342, 1.000] | 0.000 [0.000, 0.000] | 18.331 [12.841, 22.989] | 4 |
| nasa | forecast | all | 25 | gru | 0.899 [0.809, 0.958] | 0.941 [0.861, 0.994] | 16.238 [15.081, 17.177] | 20.053 [19.396, 20.673] | 4 |
| nasa | forecast | all | 25 | itransformer | 0.589 [0.482, 0.671] | 0.890 [0.774, 0.953] | 4.647 [4.213, 5.119] | 9.732 [9.089, 10.421] | 4 |
| nasa | forecast | all | 25 | itransformer_sc | 0.688 [0.528, 0.834] | 0.848 [0.658, 0.972] | 5.894 [5.571, 6.483] | 9.155 [7.927, 10.672] | 4 |
| nasa | forecast | all | 25 | lgbm | 0.838 [0.702, 0.975] | 0.939 [0.882, 0.996] | 7.579 [6.582, 8.575] | 10.024 [9.339, 10.708] | 4 |
| nasa | forecast | all | 25 | lstm | 0.748 [0.568, 0.856] | 0.896 [0.738, 0.992] | 13.098 [11.430, 14.765] | 18.716 [14.945, 22.487] | 4 |
| nasa | forecast | all | 25 | nlinear | 0.804 [0.680, 0.891] | 0.892 [0.782, 0.983] | 8.998 [8.567, 9.428] | 11.536 [10.795, 12.077] | 4 |
| nasa | forecast | all | 25 | patchtst | 0.829 [0.702, 0.920] | 0.876 [0.751, 0.960] | 7.880 [6.566, 9.771] | 8.922 [7.535, 10.846] | 4 |
| nasa | forecast | all | 25 | rlinear | 0.780 [0.678, 0.859] | 0.882 [0.796, 0.946] | 12.611 [10.409, 15.358] | 16.334 [13.964, 19.520] | 4 |
| nasa | forecast | all | 25 | transformer | 0.939 [0.883, 0.978] | 0.966 [0.938, 0.987] | 19.895 [14.128, 25.738] | 20.216 [17.101, 24.661] | 4 |
| nasa | forecast | all | 50 | dlinear | 0.558 [0.506, 0.605] | 0.894 [0.719, 0.990] | 19.789 [19.525, 20.054] | 30.666 [28.059, 32.337] | 4 |
| nasa | forecast | all | 50 | elasticnet | 0.000 [0.000, 0.000] | 0.761 [0.289, 1.000] | 0.000 [0.000, 0.000] | 19.175 [13.013, 26.450] | 4 |
| nasa | forecast | all | 50 | gru | 0.841 [0.741, 0.926] | 0.935 [0.864, 0.984] | 17.744 [16.273, 19.571] | 20.547 [18.865, 22.967] | 4 |
| nasa | forecast | all | 50 | itransformer | 0.459 [0.382, 0.536] | 0.902 [0.873, 0.932] | 5.156 [4.264, 6.361] | 21.219 [20.073, 22.540] | 4 |
| nasa | forecast | all | 50 | itransformer_sc | 0.567 [0.457, 0.680] | 0.892 [0.838, 0.943] | 7.658 [6.781, 8.933] | 15.924 [14.349, 17.521] | 4 |
| nasa | forecast | all | 50 | lgbm | 0.806 [0.669, 0.922] | 0.914 [0.750, 1.000] | 8.963 [7.246, 10.398] | 13.515 [11.054, 15.359] | 4 |
| nasa | forecast | all | 50 | lstm | 0.822 [0.747, 0.897] | 0.935 [0.887, 0.976] | 12.590 [11.730, 13.598] | 15.567 [14.622, 16.512] | 4 |
| nasa | forecast | all | 50 | nlinear | 0.819 [0.756, 0.870] | 0.916 [0.870, 0.955] | 15.235 [13.298, 17.251] | 16.924 [15.607, 18.415] | 4 |
| nasa | forecast | all | 50 | patchtst | 0.786 [0.765, 0.804] | 0.889 [0.820, 0.947] | 9.667 [8.139, 11.790] | 12.617 [11.749, 13.403] | 4 |
| nasa | forecast | all | 50 | rlinear | 0.726 [0.706, 0.746] | 0.913 [0.856, 0.970] | 24.055 [18.997, 30.789] | 34.192 [28.512, 40.386] | 4 |
| nasa | forecast | all | 50 | transformer | 0.881 [0.799, 0.962] | 0.892 [0.782, 0.972] | 19.552 [17.820, 21.364] | 20.221 [18.705, 21.953] | 4 |
| nasa | forecast | all | 100 | dlinear | 0.192 [0.056, 0.340] | 0.857 [0.596, 0.995] | 26.521 [26.047, 27.397] | 48.564 [46.378, 50.078] | 4 |
| nasa | forecast | all | 100 | elasticnet | 0.000 [0.000, 0.000] | 0.500 [0.000, 1.000] | 0.000 [0.000, 0.000] | 28.777 [10.762, 46.791] | 4 |
| nasa | forecast | all | 100 | gru | 0.920 [0.816, 0.992] | 0.959 [0.894, 0.998] | 20.405 [18.657, 22.552] | 23.813 [20.625, 27.407] | 4 |
| nasa | forecast | all | 100 | itransformer | 0.012 [0.000, 0.024] | 0.850 [0.651, 0.982] | 3.025 [1.989, 4.289] | 39.454 [37.176, 41.300] | 4 |
| nasa | forecast | all | 100 | itransformer_sc | 0.364 [0.188, 0.696] | 0.905 [0.847, 0.945] | 8.871 [5.633, 13.436] | 33.412 [31.010, 35.724] | 4 |
| nasa | forecast | all | 100 | lgbm | 0.578 [0.234, 0.921] | 0.871 [0.637, 1.000] | 7.744 [6.888, 8.600] | 15.648 [12.632, 18.835] | 4 |
| nasa | forecast | all | 100 | lstm | 0.680 [0.400, 0.961] | 0.851 [0.705, 0.997] | 14.328 [12.885, 16.589] | 21.099 [19.017, 23.316] | 4 |
| nasa | forecast | all | 100 | nlinear | 0.737 [0.575, 0.865] | 0.892 [0.845, 0.944] | 16.020 [11.200, 22.447] | 20.061 [14.727, 26.658] | 4 |
| nasa | forecast | all | 100 | patchtst | 0.618 [0.558, 0.700] | 0.863 [0.695, 0.967] | 20.966 [15.747, 29.603] | 32.560 [29.992, 35.702] | 4 |
| nasa | forecast | all | 100 | rlinear | 0.602 [0.525, 0.678] | 0.890 [0.837, 0.943] | 38.458 [21.130, 64.140] | 59.479 [43.812, 82.617] | 4 |
| nasa | forecast | all | 100 | transformer | 0.920 [0.795, 0.998] | 0.881 [0.699, 0.998] | 21.682 [19.035, 24.272] | 22.470 [18.522, 25.053] | 4 |
| nasa | forecast | start_points | 1 | dlinear | 0.940 [0.880, 1.000] | 0.830 [0.690, 0.960] | 17.651 [16.035, 19.268] | 10.620 [8.636, 12.603] | 4 |
| nasa | forecast | start_points | 1 | elasticnet | 0.000 [0.000, 0.000] | 0.700 [0.600, 0.800] | 0.000 [0.000, 0.000] | 2.279 [1.952, 2.576] | 4 |
| nasa | forecast | start_points | 1 | gru | 0.960 [0.910, 1.000] | 0.930 [0.820, 1.000] | 16.035 [13.580, 17.980] | 14.302 [11.705, 16.898] | 4 |
| nasa | forecast | start_points | 1 | itransformer | 0.700 [0.600, 0.800] | 0.700 [0.600, 0.800] | 2.646 [2.043, 3.248] | 2.642 [2.031, 3.253] | 4 |
| nasa | forecast | start_points | 1 | itransformer_sc | 0.680 [0.560, 0.800] | 0.680 [0.560, 0.800] | 2.414 [2.005, 2.912] | 2.399 [2.035, 2.888] | 4 |
| nasa | forecast | start_points | 1 | lgbm | 0.700 [0.500, 0.900] | 0.700 [0.500, 0.900] | 2.563 [2.131, 3.135] | 2.696 [2.251, 3.312] | 4 |
| nasa | forecast | start_points | 1 | lstm | 0.950 [0.880, 1.000] | 0.920 [0.860, 0.980] | 10.779 [9.826, 11.915] | 10.340 [9.252, 11.521] | 4 |
| nasa | forecast | start_points | 1 | nlinear | 0.640 [0.480, 0.800] | 0.650 [0.500, 0.800] | 2.247 [2.042, 2.451] | 2.508 [2.323, 2.700] | 4 |
| nasa | forecast | start_points | 1 | patchtst | 0.700 [0.600, 0.800] | 0.680 [0.560, 0.800] | 3.549 [2.629, 4.469] | 3.087 [2.261, 3.924] | 4 |
| nasa | forecast | start_points | 1 | rlinear | 0.640 [0.580, 0.720] | 0.690 [0.600, 0.780] | 2.662 [2.089, 3.285] | 3.024 [2.483, 3.636] | 4 |
| nasa | forecast | start_points | 1 | transformer | 0.990 [0.970, 1.000] | 0.960 [0.910, 1.000] | 17.527 [15.584, 19.526] | 14.546 [12.139, 16.953] | 4 |
| nasa | forecast | start_points | 10 | dlinear | 0.870 [0.820, 0.930] | 0.840 [0.740, 0.940] | 20.240 [20.000, 20.431] | 14.853 [14.392, 15.165] | 4 |
| nasa | forecast | start_points | 10 | elasticnet | 0.000 [0.000, 0.000] | 0.800 [0.550, 1.000] | 0.000 [0.000, 0.000] | 10.381 [8.270, 12.146] | 4 |
| nasa | forecast | start_points | 10 | gru | 0.920 [0.790, 1.000] | 0.920 [0.790, 1.000] | 17.047 [15.801, 17.841] | 17.676 [15.882, 18.721] | 4 |
| nasa | forecast | start_points | 10 | itransformer | 0.830 [0.740, 0.950] | 0.900 [0.800, 1.000] | 5.308 [3.974, 6.642] | 7.356 [6.251, 8.683] | 4 |
| nasa | forecast | start_points | 10 | itransformer_sc | 0.780 [0.590, 0.950] | 0.850 [0.740, 0.960] | 5.854 [4.951, 6.806] | 7.104 [6.277, 8.209] | 4 |
| nasa | forecast | start_points | 10 | lgbm | 0.750 [0.500, 1.000] | 0.800 [0.550, 1.000] | 5.425 [4.965, 5.871] | 6.937 [6.471, 7.328] | 4 |
| nasa | forecast | start_points | 10 | lstm | 0.870 [0.790, 0.940] | 0.920 [0.840, 1.000] | 12.310 [10.897, 14.124] | 14.720 [12.804, 16.635] | 4 |
| nasa | forecast | start_points | 10 | nlinear | 0.780 [0.560, 1.000] | 0.890 [0.780, 1.000] | 5.909 [5.698, 6.154] | 7.572 [7.080, 7.988] | 4 |
| nasa | forecast | start_points | 10 | patchtst | 0.940 [0.850, 1.000] | 0.930 [0.850, 1.000] | 6.502 [5.135, 8.327] | 6.683 [5.328, 8.617] | 4 |
| nasa | forecast | start_points | 10 | rlinear | 0.670 [0.500, 0.830] | 0.860 [0.720, 1.000] | 7.050 [5.123, 9.082] | 8.913 [7.227, 10.975] | 4 |
| nasa | forecast | start_points | 10 | transformer | 1.000 [1.000, 1.000] | 0.980 [0.940, 1.000] | 21.178 [15.913, 29.108] | 18.263 [12.277, 27.163] | 4 |
| nasa | forecast | start_points | 25 | dlinear | 0.810 [0.610, 0.940] | 0.760 [0.470, 0.960] | 15.861 [14.420, 17.303] | 13.803 [11.691, 15.915] | 4 |
| nasa | forecast | start_points | 25 | elasticnet | 0.000 [0.000, 0.000] | 0.750 [0.400, 1.000] | 0.000 [0.000, 0.000] | 18.331 [12.841, 22.989] | 4 |
| nasa | forecast | start_points | 25 | gru | 0.870 [0.770, 0.920] | 0.920 [0.810, 0.990] | 17.702 [16.624, 18.430] | 21.517 [20.955, 22.078] | 4 |
| nasa | forecast | start_points | 25 | itransformer | 0.430 [0.250, 0.640] | 0.830 [0.750, 0.920] | 5.481 [4.255, 7.082] | 10.566 [9.380, 12.579] | 4 |
| nasa | forecast | start_points | 25 | itransformer_sc | 0.550 [0.360, 0.690] | 0.760 [0.530, 0.960] | 6.561 [5.856, 7.460] | 9.822 [8.691, 11.624] | 4 |
| nasa | forecast | start_points | 25 | lgbm | 0.800 [0.600, 1.000] | 0.850 [0.700, 1.000] | 7.685 [6.774, 8.597] | 10.130 [9.531, 10.730] | 4 |
| nasa | forecast | start_points | 25 | lstm | 0.610 [0.260, 0.820] | 0.780 [0.460, 1.000] | 13.759 [11.473, 16.219] | 19.377 [14.988, 23.766] | 4 |
| nasa | forecast | start_points | 25 | nlinear | 0.740 [0.530, 0.930] | 0.890 [0.780, 0.980] | 8.466 [7.891, 9.156] | 11.004 [10.394, 11.614] | 4 |
| nasa | forecast | start_points | 25 | patchtst | 0.880 [0.760, 1.000] | 0.910 [0.820, 1.000] | 8.228 [6.280, 10.521] | 9.270 [7.484, 11.475] | 4 |
| nasa | forecast | start_points | 25 | rlinear | 0.620 [0.400, 0.850] | 0.890 [0.700, 1.000] | 11.534 [8.207, 15.006] | 15.258 [11.863, 19.169] | 4 |
| nasa | forecast | start_points | 25 | transformer | 0.930 [0.820, 1.000] | 0.970 [0.940, 1.000] | 20.559 [14.468, 26.650] | 20.880 [17.442, 25.242] | 4 |
| nasa | forecast | start_points | 50 | dlinear | 0.400 [0.270, 0.500] | 0.750 [0.370, 1.000] | 19.648 [18.981, 20.178] | 30.525 [27.462, 32.435] | 4 |
| nasa | forecast | start_points | 50 | elasticnet | 0.000 [0.000, 0.000] | 0.800 [0.400, 1.000] | 0.000 [0.000, 0.000] | 19.175 [13.013, 26.450] | 4 |
| nasa | forecast | start_points | 50 | gru | 0.880 [0.700, 1.000] | 0.920 [0.790, 1.000] | 18.951 [16.787, 21.115] | 21.753 [19.348, 24.158] | 4 |
| nasa | forecast | start_points | 50 | itransformer | 0.370 [0.250, 0.460] | 0.840 [0.680, 1.000] | 5.242 [4.007, 6.711] | 21.306 [19.816, 22.890] | 4 |
| nasa | forecast | start_points | 50 | itransformer_sc | 0.410 [0.250, 0.620] | 0.830 [0.680, 0.960] | 7.383 [6.108, 8.657] | 15.649 [14.636, 16.663] | 4 |
| nasa | forecast | start_points | 50 | lgbm | 0.750 [0.400, 1.000] | 0.800 [0.400, 1.000] | 8.853 [6.827, 10.339] | 13.406 [10.661, 15.482] | 4 |
| nasa | forecast | start_points | 50 | lstm | 0.760 [0.650, 0.870] | 0.920 [0.820, 1.000] | 12.658 [11.548, 14.227] | 15.635 [14.795, 16.292] | 4 |
| nasa | forecast | start_points | 50 | nlinear | 0.880 [0.820, 0.960] | 0.930 [0.860, 1.000] | 13.802 [11.126, 16.479] | 15.490 [13.468, 17.512] | 4 |
| nasa | forecast | start_points | 50 | patchtst | 0.790 [0.620, 0.950] | 0.890 [0.780, 1.000] | 10.154 [8.280, 12.027] | 13.104 [12.662, 13.667] | 4 |
| nasa | forecast | start_points | 50 | rlinear | 0.750 [0.520, 0.980] | 0.910 [0.820, 1.000] | 21.782 [15.279, 28.286] | 31.920 [24.733, 39.107] | 4 |
| nasa | forecast | start_points | 50 | transformer | 0.910 [0.830, 0.980] | 0.920 [0.820, 1.000] | 17.933 [16.153, 20.148] | 18.601 [16.138, 21.064] | 4 |
| nasa | forecast | start_points | 100 | dlinear | 0.250 [0.000, 0.500] | 0.835 [0.580, 1.000] | 26.535 [26.085, 27.051] | 48.578 [45.989, 50.113] | 4 |
| nasa | forecast | start_points | 100 | elasticnet | 0.000 [0.000, 0.000] | 0.500 [0.000, 1.000] | 0.000 [0.000, 0.000] | 28.777 [10.762, 46.791] | 4 |
| nasa | forecast | start_points | 100 | gru | 0.915 [0.775, 1.000] | 0.938 [0.812, 1.000] | 19.760 [17.906, 21.595] | 23.167 [20.041, 26.450] | 4 |
| nasa | forecast | start_points | 100 | itransformer | 0.000 [0.000, 0.000] | 0.875 [0.625, 1.000] | 3.538 [2.125, 4.950] | 39.967 [37.432, 41.667] | 4 |
| nasa | forecast | start_points | 100 | itransformer_sc | 0.315 [0.050, 0.745] | 0.925 [0.775, 1.000] | 9.884 [6.061, 13.708] | 34.425 [33.401, 35.701] | 4 |
| nasa | forecast | start_points | 100 | lgbm | 0.438 [0.125, 0.812] | 0.850 [0.550, 1.000] | 7.643 [6.719, 8.586] | 15.547 [12.464, 18.630] | 4 |
| nasa | forecast | start_points | 100 | lstm | 0.665 [0.350, 0.975] | 0.850 [0.700, 1.000] | 14.086 [12.799, 16.403] | 20.857 [18.932, 23.197] | 4 |
| nasa | forecast | start_points | 100 | nlinear | 0.775 [0.550, 1.000] | 0.925 [0.850, 1.000] | 17.537 [10.644, 24.429] | 21.578 [14.171, 28.984] | 4 |
| nasa | forecast | start_points | 100 | patchtst | 0.700 [0.525, 0.875] | 0.845 [0.625, 1.000] | 22.009 [17.692, 27.819] | 33.602 [31.445, 35.405] | 4 |
| nasa | forecast | start_points | 100 | rlinear | 0.750 [0.538, 0.938] | 0.938 [0.812, 1.000] | 42.517 [20.850, 64.184] | 63.538 [43.532, 83.544] | 4 |
| nasa | forecast | start_points | 100 | transformer | 0.927 [0.812, 1.000] | 0.902 [0.737, 1.000] | 22.731 [19.574, 25.427] | 23.519 [18.729, 26.813] | 4 |
| nasa | rul | all | 0 | dlinear | 0.602 [0.452, 0.752] | 0.921 [0.790, 1.000] | 80.440 [65.130, 95.749] | 119.668 [101.359, 133.376] | 4 |
| nasa | rul | all | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.863 [0.623, 0.996] | 0.000 [0.000, 0.000] | 440.880 [109.882, 771.878] | 4 |
| nasa | rul | all | 0 | gru | 0.563 [0.329, 0.793] | 0.637 [0.321, 0.888] | 60.138 [49.401, 70.875] | 69.706 [59.962, 79.450] | 4 |
| nasa | rul | all | 0 | itransformer | 0.826 [0.735, 0.917] | 0.868 [0.682, 0.979] | 68.196 [60.030, 75.513] | 85.962 [65.983, 102.566] | 4 |
| nasa | rul | all | 0 | itransformer_sc | 0.823 [0.761, 0.873] | 0.921 [0.866, 0.976] | 67.382 [58.994, 72.429] | 87.608 [82.148, 93.069] | 4 |
| nasa | rul | all | 0 | lgbm | 0.707 [0.490, 0.925] | 0.923 [0.769, 1.000] | 56.303 [48.233, 64.373] | 88.679 [70.277, 107.951] | 4 |
| nasa | rul | all | 0 | lstm | 0.850 [0.740, 0.957] | 0.883 [0.776, 0.969] | 67.852 [58.155, 79.673] | 71.661 [61.160, 85.841] | 4 |
| nasa | rul | all | 0 | nlinear | 0.588 [0.393, 0.770] | 0.923 [0.811, 1.000] | 88.061 [70.382, 105.740] | 132.315 [113.925, 146.376] | 4 |
| nasa | rul | all | 0 | patchtst | 0.466 [0.257, 0.706] | 0.929 [0.795, 1.000] | 52.313 [36.189, 68.438] | 197.743 [169.428, 214.346] | 4 |
| nasa | rul | all | 0 | rlinear | 0.165 [0.068, 0.261] | 0.920 [0.781, 1.000] | 12.032 [8.493, 15.570] | 187.340 [166.473, 199.291] | 4 |
| nasa | rul | all | 0 | transformer | 0.623 [0.303, 0.873] | 0.667 [0.351, 0.943] | 64.697 [60.051, 70.654] | 76.719 [66.602, 94.193] | 4 |
| nasa | rul | start_points | 0 | dlinear | 0.660 [0.380, 0.900] | 0.950 [0.850, 1.000] | 77.902 [55.296, 100.507] | 117.130 [96.871, 130.965] | 4 |
| nasa | rul | start_points | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.850 [0.550, 1.000] | 0.000 [0.000, 0.000] | 440.880 [109.882, 771.878] | 4 |
| nasa | rul | start_points | 0 | gru | 0.570 [0.200, 0.940] | 0.650 [0.300, 1.000] | 65.237 [57.084, 73.389] | 74.804 [66.176, 83.433] | 4 |
| nasa | rul | start_points | 0 | itransformer | 0.910 [0.820, 1.000] | 0.930 [0.790, 1.000] | 68.658 [59.770, 76.625] | 86.424 [65.516, 103.621] | 4 |
| nasa | rul | start_points | 0 | itransformer_sc | 0.910 [0.810, 0.980] | 0.980 [0.940, 1.000] | 68.356 [61.538, 73.096] | 88.582 [81.204, 95.961] | 4 |
| nasa | rul | start_points | 0 | lgbm | 0.600 [0.200, 1.000] | 0.900 [0.700, 1.000] | 52.544 [43.580, 61.601] | 84.920 [66.062, 106.935] | 4 |
| nasa | rul | start_points | 0 | lstm | 0.860 [0.710, 0.970] | 0.910 [0.780, 0.990] | 71.662 [62.865, 80.460] | 75.472 [67.454, 84.594] | 4 |
| nasa | rul | start_points | 0 | nlinear | 0.620 [0.320, 0.900] | 0.950 [0.850, 1.000] | 85.700 [58.208, 113.192] | 129.954 [109.122, 144.096] | 4 |
| nasa | rul | start_points | 0 | patchtst | 0.370 [0.140, 0.790] | 0.950 [0.850, 1.000] | 55.080 [34.002, 76.158] | 200.510 [171.279, 220.639] | 4 |
| nasa | rul | start_points | 0 | rlinear | 0.150 [0.000, 0.300] | 0.900 [0.700, 1.000] | 12.205 [7.744, 16.667] | 187.514 [166.981, 200.037] | 4 |
| nasa | rul | start_points | 0 | transformer | 0.580 [0.240, 0.900] | 0.640 [0.300, 0.980] | 66.510 [59.840, 73.902] | 78.533 [68.437, 97.657] | 4 |
| nasa | soh | all | 0 | dlinear | 0.884 [0.807, 0.961] | 0.899 [0.838, 0.960] | 3.046 [2.900, 3.194] | 3.056 [2.928, 3.172] | 4 |
| nasa | soh | all | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.893 [0.712, 0.989] | 0.000 [0.000, 0.000] | 4.941 [3.900, 5.981] | 4 |
| nasa | soh | all | 0 | gru | 0.984 [0.975, 0.993] | 0.962 [0.944, 0.979] | 15.944 [14.511, 18.551] | 14.511 [12.616, 17.288] | 4 |
| nasa | soh | all | 0 | itransformer | 0.827 [0.740, 0.902] | 0.884 [0.777, 0.949] | 1.265 [0.916, 1.637] | 1.441 [1.113, 1.795] | 4 |
| nasa | soh | all | 0 | itransformer_sc | 0.866 [0.829, 0.902] | 0.898 [0.857, 0.932] | 1.481 [1.023, 1.940] | 1.599 [1.166, 2.037] | 4 |
| nasa | soh | all | 0 | lgbm | 0.842 [0.733, 0.951] | 0.917 [0.850, 0.975] | 1.740 [1.421, 2.017] | 2.149 [1.887, 2.401] | 4 |
| nasa | soh | all | 0 | lstm | 0.916 [0.862, 0.970] | 0.934 [0.872, 0.986] | 5.824 [4.554, 7.231] | 6.023 [4.792, 7.442] | 4 |
| nasa | soh | all | 0 | nlinear | 0.873 [0.781, 0.965] | 0.876 [0.785, 0.966] | 2.432 [2.266, 2.599] | 2.478 [2.298, 2.658] | 4 |
| nasa | soh | all | 0 | patchtst | 0.913 [0.875, 0.942] | 0.902 [0.869, 0.933] | 2.436 [1.925, 3.080] | 2.318 [1.797, 2.936] | 4 |
| nasa | soh | all | 0 | rlinear | 0.855 [0.800, 0.902] | 0.901 [0.850, 0.936] | 2.129 [1.745, 2.514] | 2.354 [2.004, 2.712] | 4 |
| nasa | soh | all | 0 | transformer | 0.987 [0.970, 0.999] | 0.957 [0.907, 0.991] | 26.538 [23.033, 29.992] | 23.451 [19.748, 26.214] | 4 |
| nasa | soh | start_points | 0 | dlinear | 0.950 [0.920, 0.980] | 0.970 [0.940, 1.000] | 2.893 [2.663, 3.072] | 2.902 [2.652, 3.086] | 4 |
| nasa | soh | start_points | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.950 [0.850, 1.000] | 0.000 [0.000, 0.000] | 4.941 [3.900, 5.981] | 4 |
| nasa | soh | start_points | 0 | gru | 0.990 [0.970, 1.000] | 0.960 [0.930, 0.990] | 17.274 [15.693, 18.343] | 15.838 [13.871, 17.367] | 4 |
| nasa | soh | start_points | 0 | itransformer | 0.890 [0.800, 0.970] | 0.970 [0.940, 1.000] | 1.344 [0.881, 1.991] | 1.521 [1.079, 2.149] | 4 |
| nasa | soh | start_points | 0 | itransformer_sc | 0.890 [0.800, 0.980] | 0.920 [0.820, 1.000] | 1.487 [1.002, 2.147] | 1.604 [1.135, 2.277] | 4 |
| nasa | soh | start_points | 0 | lgbm | 0.850 [0.700, 1.000] | 0.950 [0.850, 1.000] | 1.629 [1.266, 1.892] | 2.039 [1.710, 2.286] | 4 |
| nasa | soh | start_points | 0 | lstm | 0.890 [0.730, 1.000] | 0.910 [0.730, 1.000] | 5.928 [4.140, 7.434] | 6.127 [4.377, 7.646] | 4 |
| nasa | soh | start_points | 0 | nlinear | 0.960 [0.920, 1.000] | 0.960 [0.920, 1.000] | 2.381 [2.182, 2.594] | 2.427 [2.209, 2.636] | 4 |
| nasa | soh | start_points | 0 | patchtst | 0.980 [0.940, 1.000] | 0.950 [0.850, 1.000] | 2.743 [2.036, 3.850] | 2.625 [1.907, 3.706] | 4 |
| nasa | soh | start_points | 0 | rlinear | 0.950 [0.880, 1.000] | 0.960 [0.910, 1.000] | 2.304 [1.731, 2.994] | 2.529 [2.002, 3.245] | 4 |
| nasa | soh | start_points | 0 | transformer | 1.000 [1.000, 1.000] | 0.990 [0.970, 1.000] | 23.984 [20.348, 27.298] | 20.898 [17.063, 23.918] | 4 |
| toyota | forecast | all | 1 | dlinear | 0.951 [0.934, 0.965] | 0.895 [0.876, 0.912] | 2.308 [2.201, 2.434] | 2.240 [2.133, 2.366] | 43 |
| toyota | forecast | all | 1 | elasticnet | 0.000 [0.000, 0.000] | 0.880 [0.840, 0.914] | 0.000 [0.000, 0.000] | 0.116 [0.116, 0.116] | 43 |
| toyota | forecast | all | 1 | gru | 0.990 [0.984, 0.996] | 0.976 [0.966, 0.986] | 0.707 [0.627, 0.802] | 0.598 [0.518, 0.693] | 43 |
| toyota | forecast | all | 1 | itransformer | 0.928 [0.902, 0.950] | 0.900 [0.870, 0.926] | 0.167 [0.150, 0.186] | 0.147 [0.130, 0.167] | 43 |
| toyota | forecast | all | 1 | itransformer_sc | 0.864 [0.824, 0.899] | 0.899 [0.862, 0.929] | 0.116 [0.106, 0.126] | 0.135 [0.126, 0.145] | 43 |
| toyota | forecast | all | 1 | lgbm | 0.880 [0.843, 0.913] | 0.901 [0.866, 0.931] | 0.118 [0.111, 0.125] | 0.131 [0.124, 0.138] | 43 |
| toyota | forecast | all | 1 | lstm | 0.978 [0.966, 0.989] | 0.971 [0.957, 0.983] | 0.375 [0.348, 0.408] | 0.335 [0.307, 0.368] | 43 |
| toyota | forecast | all | 1 | nlinear | 0.888 [0.851, 0.921] | 0.903 [0.868, 0.934] | 0.121 [0.118, 0.124] | 0.133 [0.130, 0.136] | 43 |
| toyota | forecast | all | 1 | patchtst | 0.917 [0.893, 0.938] | 0.923 [0.899, 0.943] | 0.237 [0.207, 0.271] | 0.240 [0.210, 0.274] | 43 |
| toyota | forecast | all | 1 | rlinear | 0.908 [0.888, 0.927] | 0.933 [0.914, 0.950] | 0.338 [0.291, 0.388] | 0.350 [0.303, 0.400] | 43 |
| toyota | forecast | all | 1 | transformer | 0.999 [0.997, 1.000] | 0.997 [0.995, 0.999] | 2.730 [2.671, 2.797] | 2.098 [2.039, 2.164] | 43 |
| toyota | forecast | all | 10 | dlinear | 0.937 [0.920, 0.951] | 0.910 [0.892, 0.925] | 1.724 [1.627, 1.839] | 1.666 [1.569, 1.781] | 43 |
| toyota | forecast | all | 10 | elasticnet | 0.000 [0.000, 0.000] | 0.882 [0.849, 0.909] | 0.000 [0.000, 0.000] | 0.316 [0.316, 0.316] | 43 |
| toyota | forecast | all | 10 | gru | 0.980 [0.971, 0.988] | 0.963 [0.951, 0.973] | 0.663 [0.595, 0.741] | 0.582 [0.514, 0.660] | 43 |
| toyota | forecast | all | 10 | itransformer | 0.920 [0.901, 0.937] | 0.909 [0.890, 0.927] | 0.265 [0.239, 0.295] | 0.254 [0.227, 0.283] | 43 |
| toyota | forecast | all | 10 | itransformer_sc | 0.853 [0.823, 0.879] | 0.905 [0.879, 0.927] | 0.281 [0.255, 0.308] | 0.331 [0.305, 0.359] | 43 |
| toyota | forecast | all | 10 | lgbm | 0.869 [0.841, 0.894] | 0.923 [0.898, 0.945] | 0.309 [0.262, 0.372] | 0.361 [0.314, 0.425] | 43 |
| toyota | forecast | all | 10 | lstm | 0.942 [0.925, 0.957] | 0.941 [0.924, 0.957] | 0.374 [0.344, 0.409] | 0.370 [0.340, 0.405] | 43 |
| toyota | forecast | all | 10 | nlinear | 0.896 [0.870, 0.919] | 0.890 [0.863, 0.913] | 0.339 [0.327, 0.354] | 0.330 [0.318, 0.345] | 43 |
| toyota | forecast | all | 10 | patchtst | 0.860 [0.842, 0.876] | 0.916 [0.899, 0.932] | 0.321 [0.281, 0.365] | 0.356 [0.316, 0.400] | 43 |
| toyota | forecast | all | 10 | rlinear | 0.855 [0.831, 0.879] | 0.923 [0.904, 0.940] | 0.443 [0.382, 0.508] | 0.490 [0.429, 0.556] | 43 |
| toyota | forecast | all | 10 | transformer | 0.998 [0.996, 1.000] | 0.997 [0.994, 0.999] | 3.441 [3.375, 3.518] | 2.615 [2.549, 2.692] | 43 |
| toyota | forecast | all | 50 | dlinear | 0.891 [0.875, 0.905] | 0.906 [0.887, 0.923] | 3.811 [3.525, 4.203] | 3.685 [3.399, 4.077] | 43 |
| toyota | forecast | all | 50 | elasticnet | 0.000 [0.000, 0.000] | 0.880 [0.844, 0.910] | 0.000 [0.000, 0.000] | 1.755 [1.755, 1.755] | 43 |
| toyota | forecast | all | 50 | gru | 0.909 [0.875, 0.937] | 0.901 [0.867, 0.930] | 1.305 [1.155, 1.483] | 1.280 [1.130, 1.458] | 43 |
| toyota | forecast | all | 50 | itransformer | 0.878 [0.842, 0.909] | 0.900 [0.865, 0.929] | 0.822 [0.731, 0.923] | 0.876 [0.786, 0.978] | 43 |
| toyota | forecast | all | 50 | itransformer_sc | 0.866 [0.837, 0.891] | 0.901 [0.874, 0.926] | 1.141 [1.012, 1.293] | 1.220 [1.090, 1.372] | 43 |
| toyota | forecast | all | 50 | lgbm | 0.836 [0.799, 0.871] | 0.919 [0.887, 0.945] | 1.363 [1.188, 1.573] | 1.533 [1.357, 1.743] | 43 |
| toyota | forecast | all | 50 | lstm | 0.894 [0.857, 0.924] | 0.899 [0.862, 0.929] | 1.180 [1.039, 1.357] | 1.193 [1.052, 1.370] | 43 |
| toyota | forecast | all | 50 | nlinear | 0.888 [0.864, 0.911] | 0.890 [0.865, 0.912] | 1.872 [1.793, 1.976] | 1.878 [1.799, 1.981] | 43 |
| toyota | forecast | all | 50 | patchtst | 0.860 [0.839, 0.880] | 0.905 [0.885, 0.923] | 1.229 [1.075, 1.408] | 1.311 [1.156, 1.489] | 43 |
| toyota | forecast | all | 50 | rlinear | 0.862 [0.835, 0.887] | 0.900 [0.875, 0.922] | 1.507 [1.312, 1.739] | 1.582 [1.387, 1.814] | 43 |
| toyota | forecast | all | 50 | transformer | 0.977 [0.957, 0.990] | 0.959 [0.935, 0.976] | 2.964 [2.863, 3.099] | 2.366 [2.266, 2.502] | 43 |
| toyota | forecast | all | 100 | dlinear | 0.812 [0.769, 0.844] | 0.871 [0.824, 0.906] | 6.208 [6.073, 6.397] | 6.724 [6.588, 6.912] | 43 |
| toyota | forecast | all | 100 | elasticnet | 0.000 [0.000, 0.000] | 0.889 [0.839, 0.928] | 0.000 [0.000, 0.000] | 4.751 [4.751, 4.751] | 43 |
| toyota | forecast | all | 100 | gru | 0.855 [0.804, 0.895] | 0.887 [0.836, 0.925] | 2.632 [2.258, 3.089] | 2.817 [2.443, 3.273] | 43 |
| toyota | forecast | all | 100 | itransformer | 0.850 [0.812, 0.886] | 0.897 [0.862, 0.928] | 2.028 [1.772, 2.328] | 2.245 [1.988, 2.544] | 43 |
| toyota | forecast | all | 100 | itransformer_sc | 0.868 [0.826, 0.904] | 0.892 [0.851, 0.927] | 2.667 [2.373, 3.007] | 2.774 [2.480, 3.114] | 43 |
| toyota | forecast | all | 100 | lgbm | 0.797 [0.742, 0.847] | 0.900 [0.848, 0.940] | 2.780 [2.442, 3.212] | 3.165 [2.828, 3.597] | 43 |
| toyota | forecast | all | 100 | lstm | 0.866 [0.824, 0.900] | 0.903 [0.863, 0.935] | 2.686 [2.285, 3.194] | 2.889 [2.489, 3.397] | 43 |
| toyota | forecast | all | 100 | nlinear | 0.884 [0.846, 0.915] | 0.891 [0.853, 0.922] | 4.772 [4.575, 5.019] | 4.821 [4.624, 5.068] | 43 |
| toyota | forecast | all | 100 | patchtst | 0.853 [0.816, 0.885] | 0.887 [0.852, 0.917] | 2.919 [2.569, 3.362] | 3.052 [2.702, 3.495] | 43 |
| toyota | forecast | all | 100 | rlinear | 0.871 [0.833, 0.905] | 0.883 [0.846, 0.916] | 3.641 [3.184, 4.160] | 3.694 [3.238, 4.213] | 43 |
| toyota | forecast | all | 100 | transformer | 0.939 [0.902, 0.965] | 0.928 [0.890, 0.956] | 3.741 [3.378, 4.235] | 3.563 [3.200, 4.057] | 43 |
| toyota | forecast | all | 200 | dlinear | 0.828 [0.803, 0.852] | 0.895 [0.873, 0.916] | 8.828 [8.784, 8.881] | 11.824 [11.779, 11.876] | 42 |
| toyota | forecast | all | 200 | elasticnet | 0.000 [0.000, 0.000] | 0.916 [0.884, 0.943] | 0.000 [0.000, 0.000] | 11.340 [11.340, 11.340] | 42 |
| toyota | forecast | all | 200 | gru | 0.795 [0.723, 0.855] | 0.900 [0.836, 0.949] | 5.931 [5.142, 6.906] | 7.720 [6.931, 8.696] | 42 |
| toyota | forecast | all | 200 | itransformer | 0.714 [0.662, 0.763] | 0.869 [0.839, 0.899] | 3.269 [2.916, 3.643] | 5.830 [5.477, 6.204] | 42 |
| toyota | forecast | all | 200 | itransformer_sc | 0.831 [0.784, 0.873] | 0.859 [0.816, 0.898] | 5.880 [5.120, 6.723] | 6.359 [5.599, 7.201] | 42 |
| toyota | forecast | all | 200 | lgbm | 0.842 [0.804, 0.878] | 0.923 [0.895, 0.948] | 6.248 [5.731, 6.826] | 7.181 [6.664, 7.759] | 42 |
| toyota | forecast | all | 200 | lstm | 0.824 [0.764, 0.878] | 0.909 [0.860, 0.947] | 6.181 [5.486, 7.013] | 7.671 [6.976, 8.503] | 42 |
| toyota | forecast | all | 200 | nlinear | 0.893 [0.871, 0.915] | 0.901 [0.880, 0.922] | 11.107 [11.019, 11.210] | 11.215 [11.128, 11.319] | 42 |
| toyota | forecast | all | 200 | patchtst | 0.837 [0.783, 0.886] | 0.862 [0.810, 0.908] | 6.895 [6.018, 7.879] | 7.217 [6.339, 8.200] | 42 |
| toyota | forecast | all | 200 | rlinear | 0.854 [0.802, 0.900] | 0.864 [0.813, 0.909] | 7.956 [6.812, 9.188] | 8.090 [6.946, 9.322] | 42 |
| toyota | forecast | all | 200 | transformer | 0.903 [0.861, 0.940] | 0.932 [0.900, 0.958] | 7.993 [7.349, 8.728] | 8.936 [8.292, 9.671] | 42 |
| toyota | forecast | start_points | 1 | dlinear | 0.963 [0.943, 0.980] | 0.931 [0.903, 0.956] | 1.896 [1.807, 2.026] | 1.828 [1.739, 1.958] | 43 |
| toyota | forecast | start_points | 1 | elasticnet | 0.000 [0.000, 0.000] | 0.895 [0.843, 0.942] | 0.000 [0.000, 0.000] | 0.116 [0.116, 0.116] | 43 |
| toyota | forecast | start_points | 1 | gru | 0.986 [0.967, 1.000] | 0.979 [0.960, 0.994] | 0.732 [0.528, 1.005] | 0.623 [0.419, 0.896] | 43 |
| toyota | forecast | start_points | 1 | itransformer | 0.927 [0.887, 0.960] | 0.877 [0.827, 0.922] | 0.150 [0.116, 0.190] | 0.131 [0.096, 0.171] | 43 |
| toyota | forecast | start_points | 1 | itransformer_sc | 0.855 [0.787, 0.913] | 0.884 [0.821, 0.934] | 0.098 [0.084, 0.114] | 0.117 [0.104, 0.133] | 43 |
| toyota | forecast | start_points | 1 | lgbm | 0.895 [0.849, 0.936] | 0.907 [0.860, 0.948] | 0.117 [0.106, 0.129] | 0.129 [0.119, 0.142] | 43 |
| toyota | forecast | start_points | 1 | lstm | 0.976 [0.951, 0.994] | 0.966 [0.941, 0.987] | 0.383 [0.297, 0.504] | 0.343 [0.257, 0.464] | 43 |
| toyota | forecast | start_points | 1 | nlinear | 0.877 [0.819, 0.927] | 0.886 [0.830, 0.935] | 0.111 [0.108, 0.114] | 0.123 [0.120, 0.126] | 43 |
| toyota | forecast | start_points | 1 | patchtst | 0.888 [0.835, 0.934] | 0.894 [0.843, 0.938] | 0.132 [0.102, 0.169] | 0.135 [0.105, 0.172] | 43 |
| toyota | forecast | start_points | 1 | rlinear | 0.849 [0.797, 0.895] | 0.890 [0.843, 0.931] | 0.183 [0.131, 0.245] | 0.195 [0.143, 0.257] | 43 |
| toyota | forecast | start_points | 1 | transformer | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 2.508 [2.437, 2.600] | 1.875 [1.805, 1.967] | 43 |
| toyota | forecast | start_points | 10 | dlinear | 0.953 [0.923, 0.980] | 0.936 [0.902, 0.966] | 1.432 [1.369, 1.536] | 1.374 [1.311, 1.478] | 43 |
| toyota | forecast | start_points | 10 | elasticnet | 0.000 [0.000, 0.000] | 0.913 [0.855, 0.959] | 0.000 [0.000, 0.000] | 0.316 [0.316, 0.316] | 43 |
| toyota | forecast | start_points | 10 | gru | 0.970 [0.943, 0.991] | 0.943 [0.912, 0.971] | 0.673 [0.493, 0.913] | 0.592 [0.412, 0.831] | 43 |
| toyota | forecast | start_points | 10 | itransformer | 0.895 [0.851, 0.935] | 0.883 [0.836, 0.926] | 0.231 [0.184, 0.286] | 0.219 [0.172, 0.275] | 43 |
| toyota | forecast | start_points | 10 | itransformer_sc | 0.836 [0.774, 0.893] | 0.898 [0.844, 0.945] | 0.217 [0.184, 0.256] | 0.267 [0.234, 0.306] | 43 |
| toyota | forecast | start_points | 10 | lgbm | 0.866 [0.814, 0.913] | 0.907 [0.855, 0.953] | 0.253 [0.199, 0.328] | 0.305 [0.252, 0.380] | 43 |
| toyota | forecast | start_points | 10 | lstm | 0.923 [0.883, 0.959] | 0.926 [0.887, 0.959] | 0.402 [0.283, 0.579] | 0.397 [0.279, 0.574] | 43 |
| toyota | forecast | start_points | 10 | nlinear | 0.927 [0.883, 0.964] | 0.920 [0.876, 0.958] | 0.297 [0.286, 0.313] | 0.288 [0.277, 0.304] | 43 |
| toyota | forecast | start_points | 10 | patchtst | 0.806 [0.753, 0.857] | 0.880 [0.834, 0.923] | 0.196 [0.150, 0.251] | 0.231 [0.185, 0.286] | 43 |
| toyota | forecast | start_points | 10 | rlinear | 0.779 [0.715, 0.838] | 0.890 [0.835, 0.938] | 0.248 [0.176, 0.333] | 0.295 [0.224, 0.380] | 43 |
| toyota | forecast | start_points | 10 | transformer | 0.998 [0.994, 1.000] | 0.992 [0.978, 1.000] | 3.241 [3.158, 3.348] | 2.415 [2.332, 2.522] | 43 |
| toyota | forecast | start_points | 50 | dlinear | 0.910 [0.887, 0.933] | 0.926 [0.898, 0.950] | 2.883 [2.557, 3.428] | 2.757 [2.431, 3.303] | 43 |
| toyota | forecast | start_points | 50 | elasticnet | 0.000 [0.000, 0.000] | 0.930 [0.878, 0.971] | 0.000 [0.000, 0.000] | 1.755 [1.755, 1.755] | 43 |
| toyota | forecast | start_points | 50 | gru | 0.907 [0.859, 0.948] | 0.894 [0.843, 0.938] | 1.172 [0.881, 1.543] | 1.147 [0.856, 1.518] | 43 |
| toyota | forecast | start_points | 50 | itransformer | 0.893 [0.849, 0.933] | 0.913 [0.871, 0.950] | 0.675 [0.547, 0.828] | 0.730 [0.602, 0.882] | 43 |
| toyota | forecast | start_points | 50 | itransformer_sc | 0.894 [0.847, 0.935] | 0.931 [0.888, 0.967] | 0.858 [0.691, 1.077] | 0.936 [0.770, 1.155] | 43 |
| toyota | forecast | start_points | 50 | lgbm | 0.855 [0.785, 0.919] | 0.930 [0.884, 0.971] | 0.931 [0.755, 1.157] | 1.100 [0.924, 1.327] | 43 |
| toyota | forecast | start_points | 50 | lstm | 0.906 [0.850, 0.952] | 0.915 [0.860, 0.960] | 0.969 [0.757, 1.224] | 0.982 [0.770, 1.237] | 43 |
| toyota | forecast | start_points | 50 | nlinear | 0.933 [0.895, 0.964] | 0.936 [0.899, 0.969] | 1.678 [1.577, 1.828] | 1.684 [1.583, 1.833] | 43 |
| toyota | forecast | start_points | 50 | patchtst | 0.838 [0.793, 0.881] | 0.898 [0.859, 0.934] | 0.821 [0.637, 1.062] | 0.902 [0.718, 1.144] | 43 |
| toyota | forecast | start_points | 50 | rlinear | 0.822 [0.769, 0.873] | 0.871 [0.822, 0.916] | 0.977 [0.733, 1.301] | 1.052 [0.808, 1.376] | 43 |
| toyota | forecast | start_points | 50 | transformer | 0.969 [0.938, 0.990] | 0.953 [0.919, 0.979] | 2.808 [2.652, 3.008] | 2.210 [2.055, 2.411] | 43 |
| toyota | forecast | start_points | 100 | dlinear | 0.865 [0.813, 0.903] | 0.898 [0.843, 0.938] | 5.860 [5.694, 6.109] | 6.375 [6.209, 6.624] | 43 |
| toyota | forecast | start_points | 100 | elasticnet | 0.000 [0.000, 0.000] | 0.907 [0.843, 0.959] | 0.000 [0.000, 0.000] | 4.751 [4.751, 4.751] | 43 |
| toyota | forecast | start_points | 100 | gru | 0.847 [0.781, 0.901] | 0.874 [0.809, 0.929] | 2.514 [1.998, 3.112] | 2.698 [2.182, 3.296] | 43 |
| toyota | forecast | start_points | 100 | itransformer | 0.870 [0.821, 0.915] | 0.909 [0.870, 0.945] | 1.890 [1.547, 2.310] | 2.107 [1.763, 2.526] | 43 |
| toyota | forecast | start_points | 100 | itransformer_sc | 0.866 [0.803, 0.919] | 0.894 [0.833, 0.944] | 2.365 [1.986, 2.805] | 2.472 [2.092, 2.911] | 43 |
| toyota | forecast | start_points | 100 | lgbm | 0.808 [0.733, 0.878] | 0.924 [0.866, 0.971] | 2.491 [2.070, 3.018] | 2.876 [2.456, 3.404] | 43 |
| toyota | forecast | start_points | 100 | lstm | 0.858 [0.803, 0.907] | 0.898 [0.847, 0.942] | 2.460 [1.979, 3.036] | 2.663 [2.182, 3.239] | 43 |
| toyota | forecast | start_points | 100 | nlinear | 0.899 [0.836, 0.950] | 0.912 [0.851, 0.958] | 4.587 [4.316, 4.933] | 4.636 [4.365, 4.982] | 43 |
| toyota | forecast | start_points | 100 | patchtst | 0.834 [0.774, 0.888] | 0.886 [0.835, 0.931] | 2.495 [2.025, 3.085] | 2.628 [2.158, 3.218] | 43 |
| toyota | forecast | start_points | 100 | rlinear | 0.849 [0.793, 0.901] | 0.859 [0.807, 0.909] | 3.021 [2.433, 3.704] | 3.074 [2.486, 3.758] | 43 |
| toyota | forecast | start_points | 100 | transformer | 0.938 [0.893, 0.973] | 0.927 [0.880, 0.964] | 3.563 [3.101, 4.139] | 3.385 [2.923, 3.961] | 43 |
| toyota | forecast | start_points | 200 | dlinear | 0.873 [0.847, 0.896] | 0.960 [0.936, 0.981] | 8.822 [8.764, 8.894] | 11.817 [11.759, 11.889] | 42 |
| toyota | forecast | start_points | 200 | elasticnet | 0.000 [0.000, 0.000] | 0.968 [0.929, 1.000] | 0.000 [0.000, 0.000] | 11.340 [11.340, 11.340] | 42 |
| toyota | forecast | start_points | 200 | gru | 0.833 [0.757, 0.898] | 0.937 [0.876, 0.982] | 5.973 [5.144, 6.951] | 7.762 [6.933, 8.741] | 42 |
| toyota | forecast | start_points | 200 | itransformer | 0.752 [0.682, 0.822] | 0.911 [0.869, 0.950] | 3.527 [2.901, 4.244] | 6.088 [5.462, 6.805] | 42 |
| toyota | forecast | start_points | 200 | itransformer_sc | 0.859 [0.782, 0.927] | 0.883 [0.817, 0.941] | 6.157 [5.077, 7.343] | 6.635 [5.555, 7.821] | 42 |
| toyota | forecast | start_points | 200 | lgbm | 0.919 [0.869, 0.962] | 0.978 [0.952, 1.000] | 6.096 [5.497, 6.762] | 7.029 [6.430, 7.695] | 42 |
| toyota | forecast | start_points | 200 | lstm | 0.873 [0.800, 0.936] | 0.940 [0.881, 0.984] | 6.236 [5.465, 7.128] | 7.726 [6.955, 8.618] | 42 |
| toyota | forecast | start_points | 200 | nlinear | 0.945 [0.907, 0.977] | 0.957 [0.926, 0.983] | 11.156 [11.039, 11.297] | 11.265 [11.148, 11.406] | 42 |
| toyota | forecast | start_points | 200 | patchtst | 0.858 [0.771, 0.931] | 0.881 [0.805, 0.944] | 7.156 [5.924, 8.543] | 7.477 [6.245, 8.865] | 42 |
| toyota | forecast | start_points | 200 | rlinear | 0.850 [0.765, 0.925] | 0.854 [0.772, 0.927] | 7.909 [6.419, 9.563] | 8.043 [6.552, 9.697] | 42 |
| toyota | forecast | start_points | 200 | transformer | 0.932 [0.881, 0.974] | 0.951 [0.913, 0.984] | 8.102 [7.406, 8.875] | 9.045 [8.349, 9.818] | 42 |
| toyota | forecast | all | 1 | dlinear | 0.991 [0.987, 0.994] | 0.973 [0.969, 0.977] | 1.923 [1.897, 1.949] | 1.855 [1.829, 1.881] | 40 |
| toyota | forecast | all | 1 | elasticnet | 0.000 [0.000, 0.000] | 0.984 [0.976, 0.990] | 0.000 [0.000, 0.000] | 0.116 [0.116, 0.116] | 40 |
| toyota | forecast | all | 1 | gru | 0.998 [0.997, 0.999] | 0.988 [0.986, 0.991] | 0.755 [0.692, 0.827] | 0.646 [0.583, 0.718] | 40 |
| toyota | forecast | all | 1 | itransformer | 0.986 [0.979, 0.992] | 0.982 [0.975, 0.988] | 0.104 [0.102, 0.107] | 0.085 [0.082, 0.087] | 40 |
| toyota | forecast | all | 1 | itransformer_sc | 0.976 [0.968, 0.983] | 0.982 [0.975, 0.988] | 0.078 [0.074, 0.083] | 0.097 [0.094, 0.102] | 40 |
| toyota | forecast | all | 1 | lgbm | 0.985 [0.978, 0.991] | 0.985 [0.978, 0.991] | 0.127 [0.124, 0.130] | 0.140 [0.137, 0.143] | 40 |
| toyota | forecast | all | 1 | lstm | 0.995 [0.993, 0.997] | 0.993 [0.989, 0.996] | 0.283 [0.276, 0.293] | 0.243 [0.236, 0.252] | 40 |
| toyota | forecast | all | 1 | nlinear | 0.984 [0.977, 0.990] | 0.985 [0.977, 0.990] | 0.110 [0.110, 0.111] | 0.123 [0.122, 0.123] | 40 |
| toyota | forecast | all | 1 | patchtst | 0.968 [0.960, 0.975] | 0.973 [0.966, 0.979] | 0.112 [0.105, 0.119] | 0.115 [0.108, 0.123] | 40 |
| toyota | forecast | all | 1 | rlinear | 0.957 [0.948, 0.965] | 0.979 [0.971, 0.985] | 0.152 [0.143, 0.162] | 0.164 [0.155, 0.174] | 40 |
| toyota | forecast | all | 1 | transformer | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 2.339 [2.313, 2.365] | 1.706 [1.680, 1.733] | 40 |
| toyota | forecast | all | 10 | dlinear | 0.988 [0.985, 0.992] | 0.980 [0.975, 0.984] | 1.446 [1.423, 1.465] | 1.388 [1.365, 1.407] | 40 |
| toyota | forecast | all | 10 | elasticnet | 0.000 [0.000, 0.000] | 0.961 [0.950, 0.971] | 0.000 [0.000, 0.000] | 0.316 [0.316, 0.316] | 40 |
| toyota | forecast | all | 10 | gru | 0.998 [0.997, 0.999] | 0.988 [0.980, 0.994] | 0.695 [0.633, 0.768] | 0.614 [0.552, 0.687] | 40 |
| toyota | forecast | all | 10 | itransformer | 0.980 [0.973, 0.986] | 0.976 [0.968, 0.983] | 0.164 [0.160, 0.167] | 0.152 [0.149, 0.156] | 40 |
| toyota | forecast | all | 10 | itransformer_sc | 0.967 [0.958, 0.974] | 0.977 [0.969, 0.984] | 0.179 [0.170, 0.190] | 0.230 [0.220, 0.241] | 40 |
| toyota | forecast | all | 10 | lgbm | 0.972 [0.963, 0.981] | 0.990 [0.986, 0.993] | 0.290 [0.279, 0.300] | 0.342 [0.332, 0.353] | 40 |
| toyota | forecast | all | 10 | lstm | 0.975 [0.967, 0.983] | 0.979 [0.972, 0.985] | 0.303 [0.293, 0.314] | 0.299 [0.289, 0.309] | 40 |
| toyota | forecast | all | 10 | nlinear | 0.987 [0.981, 0.991] | 0.986 [0.980, 0.991] | 0.298 [0.295, 0.301] | 0.289 [0.286, 0.292] | 40 |
| toyota | forecast | all | 10 | patchtst | 0.903 [0.896, 0.911] | 0.971 [0.965, 0.977] | 0.143 [0.135, 0.152] | 0.179 [0.170, 0.188] | 40 |
| toyota | forecast | all | 10 | rlinear | 0.891 [0.881, 0.902] | 0.974 [0.965, 0.981] | 0.202 [0.189, 0.215] | 0.249 [0.237, 0.262] | 40 |
| toyota | forecast | all | 10 | transformer | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 3.226 [3.206, 3.248] | 2.400 [2.380, 2.422] | 40 |
| toyota | forecast | all | 50 | dlinear | 0.875 [0.866, 0.885] | 0.961 [0.953, 0.968] | 2.852 [2.811, 2.890] | 2.726 [2.686, 2.765] | 40 |
| toyota | forecast | all | 50 | elasticnet | 0.000 [0.000, 0.000] | 0.931 [0.916, 0.947] | 0.000 [0.000, 0.000] | 1.755 [1.755, 1.755] | 40 |
| toyota | forecast | all | 50 | gru | 0.489 [0.393, 0.584] | 0.466 [0.374, 0.561] | 1.138 [1.046, 1.245] | 1.112 [1.021, 1.220] | 40 |
| toyota | forecast | all | 50 | itransformer | 0.930 [0.913, 0.945] | 0.948 [0.933, 0.961] | 0.456 [0.435, 0.478] | 0.511 [0.490, 0.533] | 40 |
| toyota | forecast | all | 50 | itransformer_sc | 0.967 [0.952, 0.979] | 0.980 [0.970, 0.988] | 0.660 [0.616, 0.708] | 0.738 [0.694, 0.787] | 40 |
| toyota | forecast | all | 50 | lgbm | 0.455 [0.399, 0.514] | 0.759 [0.683, 0.830] | 0.917 [0.886, 0.950] | 1.086 [1.056, 1.120] | 40 |
| toyota | forecast | all | 50 | lstm | 0.627 [0.563, 0.690] | 0.656 [0.593, 0.717] | 0.756 [0.715, 0.807] | 0.769 [0.728, 0.820] | 40 |
| toyota | forecast | all | 50 | nlinear | 0.983 [0.977, 0.988] | 0.984 [0.978, 0.989] | 1.613 [1.588, 1.642] | 1.618 [1.593, 1.648] | 40 |
| toyota | forecast | all | 50 | patchtst | 0.885 [0.875, 0.895] | 0.962 [0.955, 0.967] | 0.578 [0.543, 0.616] | 0.660 [0.624, 0.697] | 40 |
| toyota | forecast | all | 50 | rlinear | 0.906 [0.891, 0.921] | 0.972 [0.965, 0.979] | 0.767 [0.714, 0.828] | 0.842 [0.789, 0.903] | 40 |
| toyota | forecast | all | 50 | transformer | 0.994 [0.991, 0.997] | 0.975 [0.963, 0.985] | 2.536 [2.520, 2.551] | 1.939 [1.923, 1.954] | 40 |
| toyota | forecast | all | 100 | dlinear | 0.886 [0.877, 0.894] | 0.972 [0.963, 0.979] | 5.794 [5.769, 5.817] | 6.309 [6.284, 6.332] | 40 |
| toyota | forecast | all | 100 | elasticnet | 0.000 [0.000, 0.000] | 0.953 [0.941, 0.965] | 0.000 [0.000, 0.000] | 4.751 [4.751, 4.751] | 40 |
| toyota | forecast | all | 100 | gru | 0.268 [0.223, 0.319] | 0.329 [0.274, 0.388] | 2.110 [1.926, 2.338] | 2.295 [2.111, 2.522] | 40 |
| toyota | forecast | all | 100 | itransformer | 0.892 [0.867, 0.914] | 0.947 [0.929, 0.962] | 1.044 [0.961, 1.138] | 1.261 [1.178, 1.355] | 40 |
| toyota | forecast | all | 100 | itransformer_sc | 0.955 [0.928, 0.977] | 0.970 [0.947, 0.988] | 1.610 [1.482, 1.764] | 1.716 [1.589, 1.870] | 40 |
| toyota | forecast | all | 100 | lgbm | 0.387 [0.333, 0.446] | 0.790 [0.724, 0.851] | 1.986 [1.893, 2.104] | 2.371 [2.278, 2.489] | 40 |
| toyota | forecast | all | 100 | lstm | 0.409 [0.351, 0.468] | 0.575 [0.492, 0.657] | 1.568 [1.439, 1.727] | 1.771 [1.642, 1.930] | 40 |
| toyota | forecast | all | 100 | nlinear | 0.965 [0.954, 0.975] | 0.980 [0.972, 0.986] | 4.203 [4.110, 4.319] | 4.252 [4.159, 4.368] | 40 |
| toyota | forecast | all | 100 | patchtst | 0.899 [0.884, 0.913] | 0.960 [0.951, 0.969] | 1.557 [1.448, 1.685] | 1.690 [1.581, 1.818] | 40 |
| toyota | forecast | all | 100 | rlinear | 0.950 [0.936, 0.962] | 0.969 [0.960, 0.978] | 2.088 [1.907, 2.314] | 2.141 [1.960, 2.368] | 40 |
| toyota | forecast | all | 100 | transformer | 0.964 [0.931, 0.985] | 0.956 [0.916, 0.981] | 2.391 [2.303, 2.492] | 2.213 [2.125, 2.314] | 40 |
| toyota | forecast | all | 200 | dlinear | 0.935 [0.924, 0.945] | 0.984 [0.980, 0.987] | 8.739 [8.710, 8.776] | 11.734 [11.706, 11.772] | 40 |
| toyota | forecast | all | 200 | elasticnet | 0.000 [0.000, 0.000] | 0.977 [0.966, 0.986] | 0.000 [0.000, 0.000] | 11.340 [11.340, 11.340] | 40 |
| toyota | forecast | all | 200 | gru | 0.187 [0.142, 0.237] | 0.424 [0.333, 0.517] | 5.937 [5.473, 6.474] | 7.726 [7.262, 8.263] | 40 |
| toyota | forecast | all | 200 | itransformer | 0.818 [0.777, 0.856] | 0.964 [0.951, 0.976] | 2.198 [2.031, 2.408] | 4.759 [4.592, 4.969] | 40 |
| toyota | forecast | all | 200 | itransformer_sc | 0.947 [0.925, 0.967] | 0.980 [0.968, 0.989] | 4.138 [3.679, 4.728] | 4.616 [4.158, 5.207] | 40 |
| toyota | forecast | all | 200 | lgbm | 0.430 [0.369, 0.498] | 0.860 [0.801, 0.913] | 5.421 [5.081, 5.826] | 6.354 [6.014, 6.759] | 40 |
| toyota | forecast | all | 200 | lstm | 0.371 [0.314, 0.432] | 0.846 [0.796, 0.893] | 3.846 [3.537, 4.207] | 5.336 [5.027, 5.697] | 40 |
| toyota | forecast | all | 200 | nlinear | 0.944 [0.915, 0.969] | 0.965 [0.944, 0.984] | 10.965 [10.899, 11.050] | 11.074 [11.008, 11.159] | 40 |
| toyota | forecast | all | 200 | patchtst | 0.936 [0.911, 0.957] | 0.981 [0.965, 0.993] | 4.883 [4.336, 5.589] | 5.204 [4.657, 5.911] | 40 |
| toyota | forecast | all | 200 | rlinear | 0.956 [0.935, 0.973] | 0.973 [0.955, 0.986] | 5.301 [4.673, 6.111] | 5.434 [4.807, 6.245] | 40 |
| toyota | forecast | all | 200 | transformer | 0.931 [0.896, 0.959] | 0.951 [0.928, 0.970] | 4.770 [4.485, 5.137] | 5.713 [5.428, 6.080] | 40 |
| toyota | forecast | start_points | 1 | dlinear | 0.972 [0.945, 0.995] | 0.972 [0.945, 0.995] | 1.704 [1.679, 1.736] | 1.636 [1.611, 1.668] | 40 |
| toyota | forecast | start_points | 1 | elasticnet | 0.000 [0.000, 0.000] | 0.950 [0.900, 0.988] | 0.000 [0.000, 0.000] | 0.116 [0.116, 0.116] | 40 |
| toyota | forecast | start_points | 1 | gru | 0.995 [0.989, 1.000] | 0.982 [0.970, 0.993] | 0.686 [0.621, 0.761] | 0.577 [0.512, 0.652] | 40 |
| toyota | forecast | start_points | 1 | itransformer | 0.954 [0.904, 0.991] | 0.950 [0.900, 0.988] | 0.083 [0.080, 0.086] | 0.063 [0.061, 0.066] | 40 |
| toyota | forecast | start_points | 1 | itransformer_sc | 0.944 [0.894, 0.988] | 0.949 [0.899, 0.988] | 0.059 [0.054, 0.066] | 0.079 [0.074, 0.085] | 40 |
| toyota | forecast | start_points | 1 | lgbm | 0.956 [0.912, 0.988] | 0.956 [0.912, 0.988] | 0.120 [0.117, 0.123] | 0.133 [0.130, 0.136] | 40 |
| toyota | forecast | start_points | 1 | lstm | 0.979 [0.955, 0.996] | 0.970 [0.936, 0.994] | 0.250 [0.243, 0.259] | 0.210 [0.203, 0.219] | 40 |
| toyota | forecast | start_points | 1 | nlinear | 0.950 [0.900, 0.988] | 0.950 [0.900, 0.988] | 0.107 [0.106, 0.107] | 0.119 [0.119, 0.120] | 40 |
| toyota | forecast | start_points | 1 | patchtst | 0.953 [0.903, 0.990] | 0.953 [0.902, 0.990] | 0.053 [0.046, 0.062] | 0.056 [0.049, 0.065] | 40 |
| toyota | forecast | start_points | 1 | rlinear | 0.925 [0.871, 0.968] | 0.951 [0.903, 0.988] | 0.064 [0.055, 0.076] | 0.076 [0.067, 0.088] | 40 |
| toyota | forecast | start_points | 1 | transformer | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 2.249 [2.223, 2.274] | 1.616 [1.591, 1.642] | 40 |
| toyota | forecast | start_points | 10 | dlinear | 0.980 [0.955, 1.000] | 0.975 [0.945, 0.995] | 1.415 [1.400, 1.427] | 1.357 [1.342, 1.369] | 40 |
| toyota | forecast | start_points | 10 | elasticnet | 0.000 [0.000, 0.000] | 1.000 [1.000, 1.000] | 0.000 [0.000, 0.000] | 0.316 [0.316, 0.316] | 40 |
| toyota | forecast | start_points | 10 | gru | 0.996 [0.991, 1.000] | 0.980 [0.961, 0.995] | 0.592 [0.526, 0.668] | 0.510 [0.445, 0.587] | 40 |
| toyota | forecast | start_points | 10 | itransformer | 0.970 [0.938, 0.995] | 0.966 [0.934, 0.993] | 0.132 [0.128, 0.136] | 0.121 [0.117, 0.125] | 40 |
| toyota | forecast | start_points | 10 | itransformer_sc | 0.956 [0.919, 0.988] | 0.961 [0.925, 0.990] | 0.125 [0.113, 0.140] | 0.175 [0.163, 0.190] | 40 |
| toyota | forecast | start_points | 10 | lgbm | 0.956 [0.919, 0.988] | 0.975 [0.944, 1.000] | 0.261 [0.249, 0.272] | 0.313 [0.302, 0.325] | 40 |
| toyota | forecast | start_points | 10 | lstm | 0.960 [0.935, 0.980] | 0.969 [0.944, 0.988] | 0.265 [0.255, 0.277] | 0.261 [0.251, 0.273] | 40 |
| toyota | forecast | start_points | 10 | nlinear | 0.970 [0.936, 0.995] | 0.969 [0.931, 0.994] | 0.275 [0.272, 0.279] | 0.266 [0.263, 0.270] | 40 |
| toyota | forecast | start_points | 10 | patchtst | 0.884 [0.843, 0.924] | 0.961 [0.927, 0.989] | 0.070 [0.062, 0.080] | 0.106 [0.098, 0.115] | 40 |
| toyota | forecast | start_points | 10 | rlinear | 0.874 [0.830, 0.915] | 0.961 [0.926, 0.989] | 0.088 [0.075, 0.105] | 0.135 [0.123, 0.152] | 40 |
| toyota | forecast | start_points | 10 | transformer | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 3.130 [3.109, 3.153] | 2.304 [2.283, 2.327] | 40 |
| toyota | forecast | start_points | 50 | dlinear | 0.834 [0.814, 0.853] | 0.939 [0.914, 0.960] | 2.444 [2.425, 2.471] | 2.318 [2.299, 2.345] | 40 |
| toyota | forecast | start_points | 50 | elasticnet | 0.000 [0.000, 0.000] | 1.000 [1.000, 1.000] | 0.000 [0.000, 0.000] | 1.755 [1.755, 1.755] | 40 |
| toyota | forecast | start_points | 50 | gru | 0.389 [0.277, 0.502] | 0.367 [0.263, 0.476] | 0.944 [0.841, 1.067] | 0.919 [0.816, 1.042] | 40 |
| toyota | forecast | start_points | 50 | itransformer | 0.969 [0.943, 0.990] | 0.982 [0.963, 0.997] | 0.330 [0.309, 0.357] | 0.385 [0.364, 0.411] | 40 |
| toyota | forecast | start_points | 50 | itransformer_sc | 0.954 [0.911, 0.988] | 0.971 [0.938, 0.996] | 0.427 [0.373, 0.498] | 0.506 [0.451, 0.576] | 40 |
| toyota | forecast | start_points | 50 | lgbm | 0.356 [0.275, 0.438] | 0.681 [0.581, 0.781] | 0.681 [0.657, 0.710] | 0.850 [0.827, 0.880] | 40 |
| toyota | forecast | start_points | 50 | lstm | 0.537 [0.465, 0.609] | 0.566 [0.497, 0.634] | 0.568 [0.518, 0.630] | 0.581 [0.531, 0.643] | 40 |
| toyota | forecast | start_points | 50 | nlinear | 0.971 [0.938, 0.996] | 0.974 [0.941, 0.999] | 1.473 [1.442, 1.512] | 1.478 [1.448, 1.517] | 40 |
| toyota | forecast | start_points | 50 | patchtst | 0.863 [0.812, 0.910] | 0.969 [0.935, 0.993] | 0.299 [0.262, 0.346] | 0.381 [0.344, 0.427] | 40 |
| toyota | forecast | start_points | 50 | rlinear | 0.870 [0.819, 0.918] | 0.946 [0.899, 0.984] | 0.422 [0.358, 0.504] | 0.497 [0.433, 0.579] | 40 |
| toyota | forecast | start_points | 50 | transformer | 0.999 [0.996, 1.000] | 0.993 [0.980, 1.000] | 2.442 [2.429, 2.455] | 1.845 [1.832, 1.858] | 40 |
| toyota | forecast | start_points | 100 | dlinear | 0.894 [0.868, 0.919] | 0.974 [0.951, 0.993] | 5.646 [5.627, 5.663] | 6.161 [6.142, 6.179] | 40 |
| toyota | forecast | start_points | 100 | elasticnet | 0.000 [0.000, 0.000] | 1.000 [1.000, 1.000] | 0.000 [0.000, 0.000] | 4.751 [4.751, 4.751] | 40 |
| toyota | forecast | start_points | 100 | gru | 0.172 [0.123, 0.230] | 0.234 [0.175, 0.297] | 1.759 [1.551, 2.020] | 1.944 [1.735, 2.205] | 40 |
| toyota | forecast | start_points | 100 | itransformer | 0.941 [0.914, 0.966] | 0.982 [0.964, 0.996] | 0.766 [0.676, 0.873] | 0.982 [0.893, 1.089] | 40 |
| toyota | forecast | start_points | 100 | itransformer_sc | 0.935 [0.884, 0.978] | 0.950 [0.904, 0.988] | 1.192 [1.026, 1.404] | 1.298 [1.132, 1.510] | 40 |
| toyota | forecast | start_points | 100 | lgbm | 0.350 [0.281, 0.425] | 0.787 [0.706, 0.863] | 1.595 [1.492, 1.739] | 1.981 [1.877, 2.124] | 40 |
| toyota | forecast | start_points | 100 | lstm | 0.342 [0.276, 0.410] | 0.509 [0.419, 0.600] | 1.224 [1.070, 1.418] | 1.427 [1.273, 1.621] | 40 |
| toyota | forecast | start_points | 100 | nlinear | 0.936 [0.896, 0.971] | 0.965 [0.931, 0.991] | 3.929 [3.816, 4.074] | 3.978 [3.865, 4.123] | 40 |
| toyota | forecast | start_points | 100 | patchtst | 0.911 [0.868, 0.951] | 0.975 [0.954, 0.993] | 1.007 [0.871, 1.176] | 1.140 [1.004, 1.309] | 40 |
| toyota | forecast | start_points | 100 | rlinear | 0.910 [0.860, 0.954] | 0.940 [0.896, 0.976] | 1.464 [1.241, 1.752] | 1.518 [1.295, 1.805] | 40 |
| toyota | forecast | start_points | 100 | transformer | 0.981 [0.949, 0.999] | 0.975 [0.934, 0.997] | 2.125 [2.022, 2.251] | 1.947 [1.844, 2.073] | 40 |
| toyota | forecast | start_points | 200 | dlinear | 0.915 [0.887, 0.940] | 0.979 [0.959, 0.995] | 8.738 [8.704, 8.781] | 11.733 [11.700, 11.776] | 40 |
| toyota | forecast | start_points | 200 | elasticnet | 0.000 [0.000, 0.000] | 0.988 [0.969, 1.000] | 0.000 [0.000, 0.000] | 11.340 [11.340, 11.340] | 40 |
| toyota | forecast | start_points | 200 | gru | 0.182 [0.131, 0.236] | 0.403 [0.305, 0.501] | 5.915 [5.428, 6.489] | 7.704 [7.217, 8.278] | 40 |
| toyota | forecast | start_points | 200 | itransformer | 0.852 [0.806, 0.894] | 0.974 [0.949, 0.994] | 2.114 [1.925, 2.344] | 4.675 [4.486, 4.905] | 40 |
| toyota | forecast | start_points | 200 | itransformer_sc | 0.926 [0.880, 0.966] | 0.978 [0.956, 0.996] | 4.086 [3.522, 4.803] | 4.564 [4.000, 5.282] | 40 |
| toyota | forecast | start_points | 200 | lgbm | 0.444 [0.375, 0.519] | 0.819 [0.744, 0.894] | 5.321 [4.921, 5.783] | 6.253 [5.854, 6.715] | 40 |
| toyota | forecast | start_points | 200 | lstm | 0.356 [0.296, 0.419] | 0.846 [0.793, 0.896] | 3.864 [3.518, 4.262] | 5.354 [5.008, 5.752] | 40 |
| toyota | forecast | start_points | 200 | nlinear | 0.912 [0.871, 0.950] | 0.941 [0.904, 0.975] | 10.978 [10.902, 11.075] | 11.087 [11.010, 11.184] | 40 |
| toyota | forecast | start_points | 200 | patchtst | 0.934 [0.894, 0.969] | 0.985 [0.957, 1.000] | 4.686 [4.046, 5.498] | 5.008 [4.368, 5.819] | 40 |
| toyota | forecast | start_points | 200 | rlinear | 0.960 [0.918, 0.993] | 0.965 [0.925, 0.997] | 5.150 [4.413, 6.090] | 5.284 [4.547, 6.223] | 40 |
| toyota | forecast | start_points | 200 | transformer | 0.943 [0.898, 0.978] | 0.957 [0.924, 0.984] | 4.812 [4.494, 5.210] | 5.755 [5.437, 6.153] | 40 |
| toyota | rul | all | 0 | dlinear | 0.868 [0.814, 0.913] | 0.942 [0.891, 0.982] | 574.277 [569.922, 579.318] | 687.014 [682.659, 692.055] | 43 |
| toyota | rul | all | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.938 [0.882, 0.982] | 0.000 [0.000, 0.000] | 577.202 [577.202, 577.202] | 43 |
| toyota | rul | all | 0 | gru | 0.829 [0.751, 0.898] | 0.928 [0.879, 0.970] | 246.839 [214.953, 281.777] | 376.962 [345.075, 411.900] | 43 |
| toyota | rul | all | 0 | itransformer | 0.934 [0.892, 0.968] | 0.957 [0.920, 0.985] | 306.480 [285.249, 329.937] | 364.703 [343.472, 388.159] | 43 |
| toyota | rul | all | 0 | itransformer_sc | 0.904 [0.859, 0.942] | 0.964 [0.934, 0.988] | 336.116 [309.143, 363.898] | 455.524 [428.551, 483.306] | 43 |
| toyota | rul | all | 0 | lgbm | 0.816 [0.750, 0.875] | 0.969 [0.933, 0.998] | 251.450 [222.426, 286.302] | 523.018 [493.995, 557.871] | 43 |
| toyota | rul | all | 0 | lstm | 0.861 [0.805, 0.911] | 0.960 [0.922, 0.989] | 212.138 [192.364, 234.024] | 388.277 [368.503, 410.163] | 43 |
| toyota | rul | all | 0 | nlinear | 0.863 [0.809, 0.909] | 0.941 [0.891, 0.982] | 539.815 [535.240, 544.250] | 650.555 [645.980, 654.990] | 43 |
| toyota | rul | all | 0 | patchtst | 0.716 [0.672, 0.759] | 0.940 [0.903, 0.968] | 684.233 [578.877, 811.245] | 1449.191 [1343.835, 1576.203] | 43 |
| toyota | rul | all | 0 | rlinear | 0.758 [0.709, 0.806] | 0.934 [0.894, 0.967] | 2282.916 [1987.885, 2630.286] | 3111.627 [2816.596, 3458.997] | 43 |
| toyota | rul | all | 0 | transformer | 0.909 [0.858, 0.952] | 0.945 [0.908, 0.976] | 422.110 [391.986, 454.887] | 499.318 [469.194, 532.096] | 43 |
| toyota | rul | start_points | 0 | dlinear | 0.877 [0.812, 0.935] | 0.930 [0.866, 0.983] | 561.922 [555.747, 569.244] | 674.659 [668.484, 681.981] | 43 |
| toyota | rul | start_points | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.930 [0.860, 0.988] | 0.000 [0.000, 0.000] | 577.202 [577.202, 577.202] | 43 |
| toyota | rul | start_points | 0 | gru | 0.807 [0.707, 0.897] | 0.920 [0.858, 0.971] | 273.553 [233.187, 317.638] | 403.675 [363.309, 447.760] | 43 |
| toyota | rul | start_points | 0 | itransformer | 0.921 [0.867, 0.965] | 0.952 [0.906, 0.988] | 330.240 [299.195, 363.524] | 388.463 [357.418, 421.747] | 43 |
| toyota | rul | start_points | 0 | itransformer_sc | 0.880 [0.822, 0.933] | 0.958 [0.924, 0.987] | 371.062 [324.244, 418.359] | 490.470 [443.652, 537.767] | 43 |
| toyota | rul | start_points | 0 | lgbm | 0.802 [0.709, 0.884] | 0.971 [0.936, 1.000] | 261.568 [223.270, 306.731] | 533.137 [494.839, 578.300] | 43 |
| toyota | rul | start_points | 0 | lstm | 0.836 [0.758, 0.905] | 0.962 [0.909, 0.999] | 246.739 [213.385, 285.398] | 422.878 [389.524, 461.537] | 43 |
| toyota | rul | start_points | 0 | nlinear | 0.860 [0.792, 0.920] | 0.931 [0.870, 0.983] | 540.937 [536.571, 545.847] | 651.677 [647.311, 656.587] | 43 |
| toyota | rul | start_points | 0 | patchtst | 0.609 [0.534, 0.683] | 0.921 [0.873, 0.959] | 617.806 [500.599, 751.812] | 1382.764 [1265.556, 1516.770] | 43 |
| toyota | rul | start_points | 0 | rlinear | 0.734 [0.657, 0.808] | 0.906 [0.849, 0.953] | 1772.785 [1140.160, 2526.069] | 2601.496 [1968.870, 3354.779] | 43 |
| toyota | rul | start_points | 0 | transformer | 0.900 [0.844, 0.948] | 0.943 [0.902, 0.978] | 455.240 [418.292, 496.263] | 532.448 [495.501, 573.471] | 43 |
| toyota | rul | all | 0 | dlinear | 0.764 [0.708, 0.815] | 0.846 [0.792, 0.896] | 563.389 [560.526, 566.749] | 676.126 [673.263, 679.486] | 40 |
| toyota | rul | all | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.863 [0.794, 0.925] | 0.000 [0.000, 0.000] | 577.202 [577.202, 577.202] | 40 |
| toyota | rul | all | 0 | gru | 0.512 [0.439, 0.585] | 0.693 [0.612, 0.771] | 255.305 [230.974, 280.263] | 385.427 [361.097, 410.386] | 40 |
| toyota | rul | all | 0 | itransformer | 0.819 [0.782, 0.855] | 0.901 [0.866, 0.932] | 404.084 [377.699, 430.521] | 462.307 [435.921, 488.744] | 40 |
| toyota | rul | all | 0 | itransformer_sc | 0.866 [0.824, 0.905] | 0.952 [0.924, 0.974] | 435.072 [401.674, 468.029] | 554.480 [521.082, 587.437] | 40 |
| toyota | rul | all | 0 | lgbm | 0.504 [0.454, 0.555] | 0.739 [0.673, 0.804] | 247.230 [236.492, 258.480] | 518.799 [508.061, 530.048] | 40 |
| toyota | rul | all | 0 | lstm | 0.574 [0.505, 0.644] | 0.765 [0.690, 0.839] | 216.591 [206.676, 226.487] | 392.730 [382.815, 402.626] | 40 |
| toyota | rul | all | 0 | nlinear | 0.766 [0.710, 0.818] | 0.845 [0.792, 0.895] | 540.601 [538.291, 543.394] | 651.341 [649.032, 654.134] | 40 |
| toyota | rul | all | 0 | patchtst | 0.186 [0.156, 0.218] | 0.654 [0.595, 0.712] | 222.290 [202.986, 243.399] | 987.248 [967.944, 1008.357] | 40 |
| toyota | rul | all | 0 | rlinear | 0.501 [0.455, 0.555] | 0.757 [0.710, 0.802] | 1156.541 [1083.039, 1231.632] | 1985.252 [1911.750, 2060.343] | 40 |
| toyota | rul | all | 0 | transformer | 0.703 [0.638, 0.767] | 0.786 [0.719, 0.850] | 392.654 [378.458, 406.663] | 469.863 [455.666, 483.872] | 40 |
| toyota | rul | start_points | 0 | dlinear | 0.762 [0.688, 0.838] | 0.819 [0.750, 0.887] | 545.024 [541.846, 549.119] | 657.761 [654.583, 661.856] | 40 |
| toyota | rul | start_points | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.812 [0.725, 0.894] | 0.000 [0.000, 0.000] | 577.202 [577.202, 577.202] | 40 |
| toyota | rul | start_points | 0 | gru | 0.426 [0.326, 0.526] | 0.610 [0.509, 0.708] | 284.356 [257.330, 312.429] | 414.479 [387.452, 442.551] | 40 |
| toyota | rul | start_points | 0 | itransformer | 0.830 [0.774, 0.885] | 0.877 [0.821, 0.930] | 463.565 [427.408, 499.046] | 521.788 [485.630, 557.269] | 40 |
| toyota | rul | start_points | 0 | itransformer_sc | 0.853 [0.794, 0.905] | 0.931 [0.886, 0.970] | 519.214 [465.843, 571.317] | 638.622 [585.251, 690.725] | 40 |
| toyota | rul | start_points | 0 | lgbm | 0.388 [0.319, 0.456] | 0.675 [0.600, 0.750] | 248.111 [235.048, 261.651] | 519.680 [506.617, 533.220] | 40 |
| toyota | rul | start_points | 0 | lstm | 0.509 [0.421, 0.596] | 0.701 [0.608, 0.792] | 242.950 [230.620, 254.866] | 419.089 [406.759, 431.005] | 40 |
| toyota | rul | start_points | 0 | nlinear | 0.762 [0.686, 0.835] | 0.819 [0.750, 0.887] | 531.122 [528.821, 534.085] | 641.862 [639.561, 644.825] | 40 |
| toyota | rul | start_points | 0 | patchtst | 0.055 [0.029, 0.086] | 0.512 [0.441, 0.583] | 200.565 [177.020, 225.602] | 965.523 [941.978, 990.560] | 40 |
| toyota | rul | start_points | 0 | rlinear | 0.383 [0.314, 0.456] | 0.689 [0.619, 0.759] | 521.087 [453.244, 606.417] | 1349.797 [1281.955, 1435.128] | 40 |
| toyota | rul | start_points | 0 | transformer | 0.685 [0.596, 0.773] | 0.747 [0.656, 0.833] | 409.808 [394.995, 424.434] | 487.017 [472.204, 501.642] | 40 |
| toyota | soh | all | 0 | dlinear | 0.895 [0.858, 0.926] | 0.890 [0.853, 0.923] | 0.120 [0.118, 0.123] | 0.117 [0.114, 0.119] | 43 |
| toyota | soh | all | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.877 [0.836, 0.912] | 0.000 [0.000, 0.000] | 0.112 [0.112, 0.112] | 43 |
| toyota | soh | all | 0 | gru | 0.883 [0.838, 0.920] | 0.884 [0.839, 0.921] | 0.122 [0.116, 0.128] | 0.122 [0.117, 0.129] | 43 |
| toyota | soh | all | 0 | itransformer | 0.897 [0.872, 0.919] | 0.908 [0.883, 0.929] | 0.099 [0.086, 0.114] | 0.103 [0.090, 0.118] | 43 |
| toyota | soh | all | 0 | itransformer_sc | 0.890 [0.867, 0.910] | 0.911 [0.889, 0.930] | 0.099 [0.086, 0.115] | 0.107 [0.094, 0.123] | 43 |
| toyota | soh | all | 0 | lgbm | 0.858 [0.809, 0.899] | 0.879 [0.833, 0.918] | 0.098 [0.093, 0.105] | 0.109 [0.104, 0.116] | 43 |
| toyota | soh | all | 0 | lstm | 0.885 [0.843, 0.919] | 0.885 [0.843, 0.920] | 0.125 [0.121, 0.128] | 0.125 [0.121, 0.129] | 43 |
| toyota | soh | all | 0 | nlinear | 0.933 [0.907, 0.955] | 0.915 [0.885, 0.941] | 0.177 [0.169, 0.186] | 0.157 [0.149, 0.166] | 43 |
| toyota | soh | all | 0 | patchtst | 0.860 [0.850, 0.870] | 0.916 [0.905, 0.926] | 0.110 [0.087, 0.139] | 0.122 [0.099, 0.151] | 43 |
| toyota | soh | all | 0 | rlinear | 0.797 [0.767, 0.826] | 0.907 [0.884, 0.928] | 0.154 [0.129, 0.182] | 0.183 [0.158, 0.211] | 43 |
| toyota | soh | all | 0 | transformer | 0.929 [0.896, 0.955] | 0.922 [0.888, 0.951] | 0.211 [0.205, 0.218] | 0.193 [0.187, 0.200] | 43 |
| toyota | soh | start_points | 0 | dlinear | 0.867 [0.797, 0.929] | 0.862 [0.787, 0.926] | 0.127 [0.113, 0.150] | 0.124 [0.110, 0.147] | 43 |
| toyota | soh | start_points | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.901 [0.831, 0.953] | 0.000 [0.000, 0.000] | 0.112 [0.112, 0.112] | 43 |
| toyota | soh | start_points | 0 | gru | 0.895 [0.820, 0.957] | 0.894 [0.820, 0.956] | 0.113 [0.107, 0.120] | 0.114 [0.108, 0.121] | 43 |
| toyota | soh | start_points | 0 | itransformer | 0.902 [0.844, 0.951] | 0.910 [0.856, 0.956] | 0.103 [0.079, 0.136] | 0.108 [0.083, 0.141] | 43 |
| toyota | soh | start_points | 0 | itransformer_sc | 0.921 [0.874, 0.960] | 0.934 [0.891, 0.971] | 0.104 [0.078, 0.138] | 0.112 [0.086, 0.146] | 43 |
| toyota | soh | start_points | 0 | lgbm | 0.849 [0.762, 0.924] | 0.872 [0.791, 0.936] | 0.095 [0.089, 0.103] | 0.106 [0.100, 0.114] | 43 |
| toyota | soh | start_points | 0 | lstm | 0.886 [0.810, 0.949] | 0.887 [0.813, 0.949] | 0.116 [0.113, 0.120] | 0.117 [0.113, 0.120] | 43 |
| toyota | soh | start_points | 0 | nlinear | 0.936 [0.898, 0.970] | 0.915 [0.870, 0.953] | 0.179 [0.158, 0.207] | 0.159 [0.138, 0.187] | 43 |
| toyota | soh | start_points | 0 | patchtst | 0.902 [0.866, 0.936] | 0.948 [0.920, 0.973] | 0.109 [0.078, 0.144] | 0.121 [0.089, 0.156] | 43 |
| toyota | soh | start_points | 0 | rlinear | 0.769 [0.705, 0.831] | 0.883 [0.830, 0.929] | 0.123 [0.070, 0.191] | 0.152 [0.099, 0.220] | 43 |
| toyota | soh | start_points | 0 | transformer | 0.934 [0.883, 0.973] | 0.927 [0.873, 0.970] | 0.196 [0.192, 0.202] | 0.178 [0.173, 0.184] | 43 |
| toyota | soh | all | 0 | dlinear | 0.983 [0.976, 0.989] | 0.983 [0.975, 0.989] | 0.114 [0.114, 0.114] | 0.110 [0.110, 0.110] | 40 |
| toyota | soh | all | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.972 [0.965, 0.977] | 0.000 [0.000, 0.000] | 0.112 [0.112, 0.112] | 40 |
| toyota | soh | all | 0 | gru | 0.719 [0.682, 0.756] | 0.722 [0.686, 0.758] | 0.112 [0.107, 0.116] | 0.112 [0.108, 0.117] | 40 |
| toyota | soh | all | 0 | itransformer | 0.771 [0.754, 0.790] | 0.818 [0.803, 0.834] | 0.085 [0.083, 0.087] | 0.089 [0.087, 0.091] | 40 |
| toyota | soh | all | 0 | itransformer_sc | 0.719 [0.679, 0.759] | 0.834 [0.802, 0.865] | 0.109 [0.104, 0.113] | 0.117 [0.113, 0.121] | 40 |
| toyota | soh | all | 0 | lgbm | 0.973 [0.965, 0.980] | 0.977 [0.969, 0.983] | 0.117 [0.114, 0.120] | 0.128 [0.125, 0.131] | 40 |
| toyota | soh | all | 0 | lstm | 0.969 [0.958, 0.977] | 0.970 [0.960, 0.979] | 0.100 [0.099, 0.101] | 0.100 [0.099, 0.101] | 40 |
| toyota | soh | all | 0 | nlinear | 0.987 [0.981, 0.992] | 0.985 [0.978, 0.990] | 0.152 [0.152, 0.153] | 0.133 [0.132, 0.133] | 40 |
| toyota | soh | all | 0 | patchtst | 0.864 [0.858, 0.871] | 0.968 [0.962, 0.973] | 0.033 [0.030, 0.035] | 0.045 [0.042, 0.047] | 40 |
| toyota | soh | all | 0 | rlinear | 0.891 [0.875, 0.906] | 0.983 [0.976, 0.989] | 0.062 [0.059, 0.066] | 0.091 [0.087, 0.094] | 40 |
| toyota | soh | all | 0 | transformer | 0.989 [0.984, 0.992] | 0.987 [0.982, 0.992] | 0.227 [0.217, 0.239] | 0.209 [0.199, 0.221] | 40 |
| toyota | soh | start_points | 0 | dlinear | 0.950 [0.906, 0.988] | 0.950 [0.906, 0.988] | 0.113 [0.112, 0.114] | 0.110 [0.109, 0.110] | 40 |
| toyota | soh | start_points | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.950 [0.906, 0.988] | 0.000 [0.000, 0.000] | 0.112 [0.112, 0.112] | 40 |
| toyota | soh | start_points | 0 | gru | 0.650 [0.599, 0.700] | 0.649 [0.600, 0.698] | 0.103 [0.099, 0.108] | 0.104 [0.099, 0.109] | 40 |
| toyota | soh | start_points | 0 | itransformer | 0.675 [0.628, 0.722] | 0.730 [0.688, 0.771] | 0.084 [0.081, 0.087] | 0.089 [0.085, 0.092] | 40 |
| toyota | soh | start_points | 0 | itransformer_sc | 0.661 [0.591, 0.730] | 0.790 [0.730, 0.848] | 0.111 [0.106, 0.117] | 0.119 [0.114, 0.125] | 40 |
| toyota | soh | start_points | 0 | lgbm | 0.950 [0.906, 0.988] | 0.950 [0.906, 0.988] | 0.118 [0.114, 0.121] | 0.129 [0.125, 0.132] | 40 |
| toyota | soh | start_points | 0 | lstm | 0.938 [0.894, 0.974] | 0.940 [0.897, 0.976] | 0.094 [0.093, 0.095] | 0.094 [0.093, 0.095] | 40 |
| toyota | soh | start_points | 0 | nlinear | 0.957 [0.921, 0.989] | 0.951 [0.907, 0.988] | 0.147 [0.146, 0.148] | 0.127 [0.126, 0.128] | 40 |
| toyota | soh | start_points | 0 | patchtst | 0.811 [0.759, 0.863] | 0.935 [0.891, 0.971] | 0.026 [0.022, 0.030] | 0.038 [0.034, 0.042] | 40 |
| toyota | soh | start_points | 0 | rlinear | 0.844 [0.787, 0.896] | 0.951 [0.909, 0.988] | 0.030 [0.026, 0.034] | 0.059 [0.055, 0.063] | 40 |
| toyota | soh | start_points | 0 | transformer | 0.969 [0.940, 0.993] | 0.964 [0.929, 0.991] | 0.223 [0.212, 0.235] | 0.205 [0.194, 0.216] | 40 |

![reliability](figures/benchmark_reliability_calce.png)
![reliability](figures/benchmark_reliability_nasa.png)
![reliability](figures/benchmark_reliability_toyota.png)

## Full tables

<details><summary>calce_forecast (455 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | dlinear | 2.938 [2.766, 3.110] | 0/4 cells, 8/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | all | overall | rmse_h1 | elasticnet | 1.912 [1.825, 1.999] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | all | overall | rmse_h1 | gru | 1.936 [1.838, 2.034] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | all | overall | rmse_h1 | itransformer | 1.966 [1.854, 2.083] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | all | overall | rmse_h1 | itransformer_sc | 2.087 [1.924, 2.263] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | all | overall | rmse_h1 | last_slope | 2.686 [2.506, 2.869] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | all | overall | rmse_h1 | lgbm | 1.960 [1.845, 2.075] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | all | overall | rmse_h1 | lstm | 1.936 [1.831, 2.041] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | all | overall | rmse_h1 | nlinear | 2.475 [2.284, 2.662] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | all | overall | rmse_h1 | patchtst | 1.981 [1.886, 2.081] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | all | overall | rmse_h1 | persistence | 2.606 [2.429, 2.783] |  |  | 4 | 5 | 5c5d170c |
| loco | all | overall | rmse_h1 | rlinear | 2.404 [2.230, 2.573] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | all | overall | rmse_h1 | transformer | 2.323 [2.141, 2.524] | 4/4 cells, 19/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | all | overall | rmse_h10 | dlinear | 3.643 [3.593, 3.693] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | all | overall | rmse_h10 | elasticnet | 2.333 [2.263, 2.411] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | all | overall | rmse_h10 | gru | 2.320 [2.210, 2.414] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | all | overall | rmse_h10 | itransformer | 2.306 [2.219, 2.401] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | all | overall | rmse_h10 | itransformer_sc | 2.334 [2.267, 2.426] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | all | overall | rmse_h10 | last_slope | 4.266 [4.097, 4.435] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | all | overall | rmse_h10 | lgbm | 2.303 [2.240, 2.382] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | all | overall | rmse_h10 | lstm | 2.323 [2.202, 2.444] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | all | overall | rmse_h10 | nlinear | 2.546 [2.485, 2.606] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | all | overall | rmse_h10 | patchtst | 2.367 [2.316, 2.438] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | all | overall | rmse_h10 | persistence | 3.071 [3.003, 3.139] |  |  | 4 | 5 | 5c5d170c |
| loco | all | overall | rmse_h10 | rlinear | 2.516 [2.456, 2.566] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | all | overall | rmse_h10 | transformer | 2.600 [2.429, 2.731] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | all | overall | rmse_h100 | dlinear | 8.798 [8.455, 9.134] | 4/4 cells, 16/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | all | overall | rmse_h100 | elasticnet | 4.820 [3.702, 6.053] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | all | overall | rmse_h100 | gru | 4.230 [3.087, 5.407] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | all | overall | rmse_h100 | itransformer | 3.792 [3.263, 4.322] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | all | overall | rmse_h100 | itransformer_sc | 3.769 [3.375, 4.163] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | all | overall | rmse_h100 | last_slope | 25.209 [24.266, 26.151] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | all | overall | rmse_h100 | lgbm | 3.528 [3.089, 4.097] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | all | overall | rmse_h100 | lstm | 3.943 [2.964, 4.925] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | all | overall | rmse_h100 | nlinear | 5.943 [5.562, 6.325] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | all | overall | rmse_h100 | patchtst | 5.537 [4.948, 6.185] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | all | overall | rmse_h100 | persistence | 10.293 [9.591, 10.966] |  |  | 4 | 5 | 5c5d170c |
| loco | all | overall | rmse_h100 | rlinear | 5.744 [5.384, 6.097] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | all | overall | rmse_h100 | transformer | 4.144 [3.252, 5.023] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | all | overall | rmse_h25 | dlinear | 4.926 [4.836, 5.036] | 0/4 cells, 8/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | all | overall | rmse_h25 | elasticnet | 3.100 [2.805, 3.477] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | all | overall | rmse_h25 | gru | 2.778 [2.512, 2.992] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | all | overall | rmse_h25 | itransformer | 2.711 [2.518, 2.904] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | all | overall | rmse_h25 | itransformer_sc | 2.764 [2.627, 2.931] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | all | overall | rmse_h25 | last_slope | 7.632 [7.376, 7.792] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | all | overall | rmse_h25 | lgbm | 2.624 [2.490, 2.845] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | all | overall | rmse_h25 | lstm | 2.741 [2.516, 2.933] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | all | overall | rmse_h25 | nlinear | 3.273 [3.111, 3.436] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | all | overall | rmse_h25 | patchtst | 3.039 [2.903, 3.176] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | all | overall | rmse_h25 | persistence | 4.180 [4.046, 4.314] |  |  | 4 | 5 | 5c5d170c |
| loco | all | overall | rmse_h25 | rlinear | 3.283 [3.129, 3.437] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | all | overall | rmse_h25 | transformer | 3.061 [2.703, 3.401] | 4/4 cells, 18/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | all | overall | rmse_h50 | dlinear | 5.791 [5.671, 5.937] | 4/4 cells, 16/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | all | overall | rmse_h50 | elasticnet | 3.926 [3.081, 5.023] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | all | overall | rmse_h50 | gru | 3.307 [2.631, 3.915] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | all | overall | rmse_h50 | itransformer | 3.133 [2.873, 3.393] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | all | overall | rmse_h50 | itransformer_sc | 3.090 [2.805, 3.480] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | all | overall | rmse_h50 | last_slope | 13.491 [12.984, 13.882] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | all | overall | rmse_h50 | lgbm | 2.840 [2.521, 3.243] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | all | overall | rmse_h50 | lstm | 3.119 [2.595, 3.528] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | all | overall | rmse_h50 | nlinear | 4.194 [3.942, 4.447] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | all | overall | rmse_h50 | patchtst | 3.796 [3.521, 4.071] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | all | overall | rmse_h50 | persistence | 6.278 [5.955, 6.519] |  |  | 4 | 5 | 5c5d170c |
| loco | all | overall | rmse_h50 | rlinear | 4.147 [3.886, 4.408] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | all | overall | rmse_h50 | transformer | 3.557 [2.796, 4.400] | 4/4 cells, 19/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | fixed:200 | rmse_h1 | dlinear | 1.820 [1.403, 2.574] | 0/4 cells, 3/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | fixed:200 | rmse_h1 | elasticnet | 0.292 [0.084, 0.501] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | fixed:200 | rmse_h1 | gru | 0.298 [0.183, 0.430] | 2/4 cells, 12/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | fixed:200 | rmse_h1 | itransformer | 0.307 [0.213, 0.400] | 3/4 cells, 13/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | fixed:200 | rmse_h1 | itransformer_sc | 0.302 [0.170, 0.435] | 3/4 cells, 13/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | fixed:200 | rmse_h1 | last_slope | 0.422 [0.201, 0.609] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | fixed:200 | rmse_h1 | lgbm | 0.251 [0.180, 0.385] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | fixed:200 | rmse_h1 | lstm | 0.331 [0.252, 0.410] | 2/4 cells, 11/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | fixed:200 | rmse_h1 | nlinear | 0.326 [0.174, 0.478] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | fixed:200 | rmse_h1 | patchtst | 0.288 [0.137, 0.440] | 4/4 cells, 16/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | fixed:200 | rmse_h1 | persistence | 0.347 [0.209, 0.485] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | fixed:200 | rmse_h1 | rlinear | 0.295 [0.132, 0.459] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | fixed:200 | rmse_h1 | transformer | 0.389 [0.364, 0.412] | 1/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | fixed:200 | rmse_h10 | dlinear | 2.314 [1.894, 2.958] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | fixed:200 | rmse_h10 | elasticnet | 1.385 [0.195, 3.378] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | fixed:200 | rmse_h10 | gru | 1.181 [0.245, 2.779] | 2/4 cells, 11/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | fixed:200 | rmse_h10 | itransformer | 1.128 [0.174, 2.842] | 2/4 cells, 12/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | fixed:200 | rmse_h10 | itransformer_sc | 1.294 [0.291, 2.962] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | fixed:200 | rmse_h10 | last_slope | 2.318 [0.806, 4.329] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | fixed:200 | rmse_h10 | lgbm | 1.334 [0.307, 3.161] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | fixed:200 | rmse_h10 | lstm | 1.289 [0.257, 3.206] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | fixed:200 | rmse_h10 | nlinear | 1.266 [0.251, 3.199] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | fixed:200 | rmse_h10 | patchtst | 1.401 [0.379, 3.169] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | fixed:200 | rmse_h10 | persistence | 1.344 [0.340, 2.774] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | fixed:200 | rmse_h10 | rlinear | 1.247 [0.176, 3.138] | 2/4 cells, 11/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | fixed:200 | rmse_h10 | transformer | 1.123 [0.298, 2.646] | 3/4 cells, 11/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | fixed:200 | rmse_h100 | dlinear | 2.576 [2.401, 2.750] | 1/4 cells, 9/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | fixed:200 | rmse_h100 | elasticnet | 1.679 [0.437, 3.223] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | fixed:200 | rmse_h100 | gru | 1.405 [0.610, 2.200] | 3/4 cells, 14/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | fixed:200 | rmse_h100 | itransformer | 0.665 [0.525, 0.816] | 4/4 cells, 17/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | fixed:200 | rmse_h100 | itransformer_sc | 0.795 [0.577, 1.012] | 4/4 cells, 19/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | fixed:200 | rmse_h100 | last_slope | 10.695 [6.175, 15.216] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | fixed:200 | rmse_h100 | lgbm | 0.976 [0.292, 1.874] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | fixed:200 | rmse_h100 | lstm | 1.179 [0.440, 2.037] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | fixed:200 | rmse_h100 | nlinear | 0.971 [0.353, 1.912] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | fixed:200 | rmse_h100 | patchtst | 0.852 [0.433, 1.561] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | fixed:200 | rmse_h100 | persistence | 1.897 [1.120, 2.489] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | fixed:200 | rmse_h100 | rlinear | 0.749 [0.397, 1.125] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | fixed:200 | rmse_h100 | transformer | 1.235 [0.523, 2.175] | 3/4 cells, 14/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | fixed:200 | rmse_h25 | dlinear | 4.455 [3.841, 5.070] | 0/4 cells, 1/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | fixed:200 | rmse_h25 | elasticnet | 2.103 [1.036, 3.169] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | fixed:200 | rmse_h25 | gru | 1.978 [1.481, 2.536] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | fixed:200 | rmse_h25 | itransformer | 1.353 [0.882, 1.825] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | fixed:200 | rmse_h25 | itransformer_sc | 1.308 [0.613, 2.002] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | fixed:200 | rmse_h25 | last_slope | 2.579 [0.690, 4.821] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | fixed:200 | rmse_h25 | lgbm | 1.712 [1.190, 2.043] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | fixed:200 | rmse_h25 | lstm | 1.605 [1.074, 2.136] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | fixed:200 | rmse_h25 | nlinear | 1.875 [1.124, 2.626] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | fixed:200 | rmse_h25 | patchtst | 1.388 [0.646, 2.129] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | fixed:200 | rmse_h25 | persistence | 0.840 [0.239, 1.441] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | fixed:200 | rmse_h25 | rlinear | 1.787 [0.929, 2.644] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | fixed:200 | rmse_h25 | transformer | 1.469 [0.788, 2.309] | 0/4 cells, 3/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | fixed:200 | rmse_h50 | dlinear | 2.089 [1.824, 2.521] | 0/4 cells, 4/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | fixed:200 | rmse_h50 | elasticnet | 1.839 [0.588, 3.144] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | fixed:200 | rmse_h50 | gru | 1.204 [0.525, 2.073] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | fixed:200 | rmse_h50 | itransformer | 0.960 [0.609, 1.311] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | fixed:200 | rmse_h50 | itransformer_sc | 1.039 [0.679, 1.270] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | fixed:200 | rmse_h50 | last_slope | 4.995 [1.687, 8.303] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | fixed:200 | rmse_h50 | lgbm | 1.669 [0.872, 2.465] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | fixed:200 | rmse_h50 | lstm | 1.229 [0.696, 1.910] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | fixed:200 | rmse_h50 | nlinear | 1.306 [0.690, 1.921] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | fixed:200 | rmse_h50 | patchtst | 1.132 [0.823, 1.442] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | fixed:200 | rmse_h50 | persistence | 0.844 [0.319, 1.572] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | fixed:200 | rmse_h50 | rlinear | 1.219 [1.019, 1.383] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | fixed:200 | rmse_h50 | transformer | 1.096 [0.589, 1.855] | 1/4 cells, 6/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | fixed:400 | rmse_h1 | dlinear | 1.465 [1.383, 1.595] | 0/4 cells, 1/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | fixed:400 | rmse_h1 | elasticnet | 0.308 [0.156, 0.405] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | fixed:400 | rmse_h1 | gru | 0.201 [0.084, 0.411] | 0/4 cells, 1/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | fixed:400 | rmse_h1 | itransformer | 0.155 [0.068, 0.243] | 0/4 cells, 3/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | fixed:400 | rmse_h1 | itransformer_sc | 0.186 [0.071, 0.301] | 0/4 cells, 2/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | fixed:400 | rmse_h1 | last_slope | 0.081 [0.034, 0.158] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | fixed:400 | rmse_h1 | lgbm | 0.079 [0.024, 0.155] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | fixed:400 | rmse_h1 | lstm | 0.143 [0.069, 0.263] | 0/4 cells, 4/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | fixed:400 | rmse_h1 | nlinear | 0.125 [0.022, 0.227] | 1/4 cells, 4/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | fixed:400 | rmse_h1 | patchtst | 0.183 [0.121, 0.244] | 1/4 cells, 3/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | fixed:400 | rmse_h1 | persistence | 0.080 [0.019, 0.194] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | fixed:400 | rmse_h1 | rlinear | 0.132 [0.044, 0.230] | 1/4 cells, 3/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | fixed:400 | rmse_h1 | transformer | 0.377 [0.303, 0.425] | 0/4 cells, 3/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | fixed:400 | rmse_h10 | dlinear | 2.058 [1.508, 2.609] | 0/4 cells, 4/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | fixed:400 | rmse_h10 | elasticnet | 1.007 [0.844, 1.179] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | fixed:400 | rmse_h10 | gru | 0.697 [0.310, 1.084] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | fixed:400 | rmse_h10 | itransformer | 0.744 [0.511, 0.988] | 3/4 cells, 13/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | fixed:400 | rmse_h10 | itransformer_sc | 0.776 [0.408, 1.144] | 3/4 cells, 14/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | fixed:400 | rmse_h10 | last_slope | 1.629 [1.035, 2.223] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | fixed:400 | rmse_h10 | lgbm | 0.782 [0.543, 1.022] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | fixed:400 | rmse_h10 | lstm | 0.719 [0.257, 1.181] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | fixed:400 | rmse_h10 | nlinear | 0.719 [0.412, 0.963] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | fixed:400 | rmse_h10 | patchtst | 0.641 [0.307, 0.976] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | fixed:400 | rmse_h10 | persistence | 1.009 [0.324, 1.694] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | fixed:400 | rmse_h10 | rlinear | 0.678 [0.216, 1.022] | 2/4 cells, 12/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | fixed:400 | rmse_h10 | transformer | 0.685 [0.355, 1.015] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | fixed:400 | rmse_h100 | dlinear | 3.732 [2.918, 4.546] | 1/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | fixed:400 | rmse_h100 | elasticnet | 2.492 [1.176, 3.851] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | fixed:400 | rmse_h100 | gru | 3.070 [1.901, 4.271] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | fixed:400 | rmse_h100 | itransformer | 2.346 [1.151, 3.442] | 3/4 cells, 16/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | fixed:400 | rmse_h100 | itransformer_sc | 2.676 [1.642, 3.731] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | fixed:400 | rmse_h100 | last_slope | 6.898 [1.827, 11.957] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | fixed:400 | rmse_h100 | lgbm | 2.778 [2.074, 4.036] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | fixed:400 | rmse_h100 | lstm | 2.709 [1.761, 3.657] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | fixed:400 | rmse_h100 | nlinear | 2.516 [1.232, 3.801] | 2/4 cells, 11/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | fixed:400 | rmse_h100 | patchtst | 2.301 [1.061, 3.357] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | fixed:400 | rmse_h100 | persistence | 3.346 [1.619, 5.072] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | fixed:400 | rmse_h100 | rlinear | 2.740 [1.373, 4.106] | 2/4 cells, 8/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | fixed:400 | rmse_h100 | transformer | 3.136 [2.187, 4.086] | 2/4 cells, 11/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | fixed:400 | rmse_h25 | dlinear | 3.562 [2.716, 4.311] | 0/4 cells, 4/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | fixed:400 | rmse_h25 | elasticnet | 1.239 [0.330, 2.331] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | fixed:400 | rmse_h25 | gru | 0.675 [0.253, 1.106] | 2/4 cells, 12/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | fixed:400 | rmse_h25 | itransformer | 1.038 [0.573, 1.542] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | fixed:400 | rmse_h25 | itransformer_sc | 1.052 [0.541, 1.526] | 3/4 cells, 13/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | fixed:400 | rmse_h25 | last_slope | 2.439 [1.474, 3.403] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | fixed:400 | rmse_h25 | lgbm | 0.996 [0.278, 1.892] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | fixed:400 | rmse_h25 | lstm | 0.749 [0.286, 1.211] | 2/4 cells, 13/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | fixed:400 | rmse_h25 | nlinear | 0.851 [0.432, 1.095] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | fixed:400 | rmse_h25 | patchtst | 1.042 [0.565, 1.447] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | fixed:400 | rmse_h25 | persistence | 1.333 [0.586, 2.081] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | fixed:400 | rmse_h25 | rlinear | 0.693 [0.355, 1.049] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | fixed:400 | rmse_h25 | transformer | 1.005 [0.560, 1.450] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | fixed:400 | rmse_h50 | dlinear | 2.205 [1.958, 2.486] | 1/4 cells, 11/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | fixed:400 | rmse_h50 | elasticnet | 1.872 [1.222, 2.522] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | fixed:400 | rmse_h50 | gru | 1.416 [0.453, 2.604] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | fixed:400 | rmse_h50 | itransformer | 0.987 [0.299, 1.829] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | fixed:400 | rmse_h50 | itransformer_sc | 1.002 [0.367, 2.098] | 4/4 cells, 18/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | fixed:400 | rmse_h50 | last_slope | 3.432 [1.337, 4.769] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | fixed:400 | rmse_h50 | lgbm | 0.864 [0.195, 1.625] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | fixed:400 | rmse_h50 | lstm | 1.173 [0.367, 2.235] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | fixed:400 | rmse_h50 | nlinear | 0.629 [0.118, 1.140] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | fixed:400 | rmse_h50 | patchtst | 0.699 [0.378, 1.018] | 3/4 cells, 14/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | fixed:400 | rmse_h50 | persistence | 1.656 [0.742, 2.680] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | fixed:400 | rmse_h50 | rlinear | 0.969 [0.722, 1.283] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | fixed:400 | rmse_h50 | transformer | 1.392 [0.502, 2.780] | 2/4 cells, 11/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | frac:0.3 | rmse_h1 | dlinear | 1.495 [1.298, 1.751] | 0/4 cells, 4/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | frac:0.3 | rmse_h1 | elasticnet | 0.592 [0.486, 0.699] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | frac:0.3 | rmse_h1 | gru | 0.387 [0.160, 0.641] | 1/4 cells, 8/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer | 0.413 [0.169, 0.865] | 2/4 cells, 9/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer_sc | 0.358 [0.113, 0.780] | 2/4 cells, 11/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | frac:0.3 | rmse_h1 | last_slope | 0.474 [0.215, 0.961] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | frac:0.3 | rmse_h1 | lgbm | 0.328 [0.133, 0.712] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | frac:0.3 | rmse_h1 | lstm | 0.439 [0.205, 0.862] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | frac:0.3 | rmse_h1 | nlinear | 0.367 [0.080, 0.821] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | frac:0.3 | rmse_h1 | patchtst | 0.344 [0.100, 0.794] | 3/4 cells, 11/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | frac:0.3 | rmse_h1 | persistence | 0.373 [0.089, 0.866] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | frac:0.3 | rmse_h1 | rlinear | 0.381 [0.087, 0.848] | 2/4 cells, 9/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | frac:0.3 | rmse_h1 | transformer | 0.556 [0.263, 0.857] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | frac:0.3 | rmse_h10 | dlinear | 2.003 [1.929, 2.077] | 0/4 cells, 6/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | frac:0.3 | rmse_h10 | elasticnet | 0.677 [0.325, 1.143] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | frac:0.3 | rmse_h10 | gru | 0.667 [0.367, 0.966] | 3/4 cells, 14/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer | 0.727 [0.364, 0.985] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer_sc | 0.496 [0.188, 0.711] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | frac:0.3 | rmse_h10 | last_slope | 3.126 [1.808, 4.454] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | frac:0.3 | rmse_h10 | lgbm | 0.685 [0.078, 1.293] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | frac:0.3 | rmse_h10 | lstm | 0.689 [0.410, 0.967] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | frac:0.3 | rmse_h10 | nlinear | 0.312 [0.136, 0.591] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | frac:0.3 | rmse_h10 | patchtst | 0.442 [0.251, 0.633] | 3/4 cells, 16/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | frac:0.3 | rmse_h10 | persistence | 0.952 [0.590, 1.315] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | frac:0.3 | rmse_h10 | rlinear | 0.259 [0.109, 0.511] | 3/4 cells, 16/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | frac:0.3 | rmse_h10 | transformer | 0.831 [0.551, 1.079] | 3/4 cells, 11/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | frac:0.3 | rmse_h100 | dlinear | 2.334 [2.001, 2.755] | 0/4 cells, 6/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | frac:0.3 | rmse_h100 | elasticnet | 2.578 [0.941, 4.215] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | frac:0.3 | rmse_h100 | gru | 1.921 [1.023, 2.819] | 1/4 cells, 6/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer | 1.603 [1.024, 2.420] | 1/4 cells, 6/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer_sc | 1.852 [1.201, 2.931] | 0/4 cells, 3/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | frac:0.3 | rmse_h100 | last_slope | 22.123 [7.983, 36.262] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | frac:0.3 | rmse_h100 | lgbm | 2.034 [1.552, 2.481] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | frac:0.3 | rmse_h100 | lstm | 1.800 [0.874, 2.725] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | frac:0.3 | rmse_h100 | nlinear | 3.129 [1.149, 5.940] | 1/4 cells, 4/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | frac:0.3 | rmse_h100 | patchtst | 3.317 [1.835, 5.593] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | frac:0.3 | rmse_h100 | persistence | 0.918 [0.565, 1.150] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | frac:0.3 | rmse_h100 | rlinear | 3.799 [2.123, 6.656] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | frac:0.3 | rmse_h100 | transformer | 1.854 [1.008, 2.699] | 1/4 cells, 3/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | frac:0.3 | rmse_h25 | dlinear | 3.462 [3.040, 4.085] | 0/4 cells, 8/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | frac:0.3 | rmse_h25 | elasticnet | 0.687 [0.163, 1.508] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | frac:0.3 | rmse_h25 | gru | 0.800 [0.349, 1.551] | 3/4 cells, 14/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer | 0.486 [0.178, 1.088] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer_sc | 0.671 [0.275, 1.203] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | frac:0.3 | rmse_h25 | last_slope | 5.620 [1.950, 9.290] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | frac:0.3 | rmse_h25 | lgbm | 0.805 [0.291, 1.319] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | frac:0.3 | rmse_h25 | lstm | 0.616 [0.257, 1.271] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | frac:0.3 | rmse_h25 | nlinear | 0.877 [0.148, 2.119] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | frac:0.3 | rmse_h25 | patchtst | 0.745 [0.193, 1.813] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | frac:0.3 | rmse_h25 | persistence | 0.865 [0.571, 1.180] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | frac:0.3 | rmse_h25 | rlinear | 0.941 [0.183, 2.198] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | frac:0.3 | rmse_h25 | transformer | 0.829 [0.379, 1.640] | 3/4 cells, 13/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | frac:0.3 | rmse_h50 | dlinear | 2.733 [2.224, 3.375] | 0/4 cells, 3/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | frac:0.3 | rmse_h50 | elasticnet | 3.201 [1.386, 5.150] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | frac:0.3 | rmse_h50 | gru | 2.526 [1.360, 4.048] | 1/4 cells, 4/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer | 2.104 [0.715, 3.852] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer_sc | 1.996 [0.554, 4.027] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | frac:0.3 | rmse_h50 | last_slope | 10.522 [4.959, 16.085] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | frac:0.3 | rmse_h50 | lgbm | 2.084 [1.138, 3.778] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | frac:0.3 | rmse_h50 | lstm | 2.312 [0.956, 3.979] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | frac:0.3 | rmse_h50 | nlinear | 2.646 [0.870, 5.347] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | frac:0.3 | rmse_h50 | patchtst | 2.621 [0.943, 4.859] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | frac:0.3 | rmse_h50 | persistence | 1.300 [0.353, 2.350] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | frac:0.3 | rmse_h50 | rlinear | 2.548 [0.842, 5.238] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | frac:0.3 | rmse_h50 | transformer | 2.602 [1.390, 4.358] | 1/4 cells, 4/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | frac:0.5 | rmse_h1 | dlinear | 1.506 [1.166, 1.962] | 1/4 cells, 3/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | frac:0.5 | rmse_h1 | elasticnet | 0.468 [0.264, 0.816] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | frac:0.5 | rmse_h1 | gru | 0.484 [0.154, 0.985] | 2/4 cells, 9/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer | 0.471 [0.049, 0.964] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer_sc | 0.479 [0.069, 0.916] | 2/4 cells, 13/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | frac:0.5 | rmse_h1 | last_slope | 0.642 [0.198, 1.085] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | frac:0.5 | rmse_h1 | lgbm | 0.490 [0.046, 0.994] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | frac:0.5 | rmse_h1 | lstm | 0.536 [0.082, 0.991] | 1/4 cells, 9/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | frac:0.5 | rmse_h1 | nlinear | 0.498 [0.050, 0.946] | 1/4 cells, 11/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | frac:0.5 | rmse_h1 | patchtst | 0.547 [0.072, 1.022] | 1/4 cells, 8/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | frac:0.5 | rmse_h1 | persistence | 0.524 [0.047, 1.016] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | frac:0.5 | rmse_h1 | rlinear | 0.528 [0.093, 0.962] | 1/4 cells, 6/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | frac:0.5 | rmse_h1 | transformer | 0.559 [0.286, 0.923] | 2/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | frac:0.5 | rmse_h10 | dlinear | 2.300 [1.751, 2.776] | 0/4 cells, 4/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | frac:0.5 | rmse_h10 | elasticnet | 0.866 [0.628, 1.189] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | frac:0.5 | rmse_h10 | gru | 0.854 [0.414, 1.349] | 3/4 cells, 17/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer | 0.936 [0.378, 1.268] | 4/4 cells, 18/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer_sc | 0.969 [0.498, 1.271] | 3/4 cells, 16/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | frac:0.5 | rmse_h10 | last_slope | 2.527 [1.938, 3.130] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | frac:0.5 | rmse_h10 | lgbm | 0.641 [0.263, 1.091] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | frac:0.5 | rmse_h10 | lstm | 0.878 [0.345, 1.369] | 3/4 cells, 17/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | frac:0.5 | rmse_h10 | nlinear | 0.819 [0.764, 0.892] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | frac:0.5 | rmse_h10 | patchtst | 0.693 [0.241, 1.145] | 4/4 cells, 19/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | frac:0.5 | rmse_h10 | persistence | 1.354 [0.510, 1.928] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | frac:0.5 | rmse_h10 | rlinear | 0.804 [0.655, 0.954] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | frac:0.5 | rmse_h10 | transformer | 1.053 [0.518, 1.523] | 3/4 cells, 16/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | frac:0.5 | rmse_h100 | dlinear | 2.780 [2.204, 3.808] | 3/4 cells, 12/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | frac:0.5 | rmse_h100 | elasticnet | 2.275 [1.417, 3.134] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | frac:0.5 | rmse_h100 | gru | 1.584 [0.909, 2.459] | 4/4 cells, 19/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer | 1.419 [0.604, 2.344] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer_sc | 1.174 [0.482, 1.962] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | frac:0.5 | rmse_h100 | last_slope | 14.573 [5.467, 22.398] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | frac:0.5 | rmse_h100 | lgbm | 0.975 [0.483, 1.329] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | frac:0.5 | rmse_h100 | lstm | 1.373 [0.534, 2.326] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | frac:0.5 | rmse_h100 | nlinear | 2.591 [1.842, 3.357] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | frac:0.5 | rmse_h100 | patchtst | 2.539 [0.681, 5.230] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | frac:0.5 | rmse_h100 | persistence | 2.842 [2.048, 3.830] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | frac:0.5 | rmse_h100 | rlinear | 2.330 [1.354, 3.241] | 3/4 cells, 14/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | frac:0.5 | rmse_h100 | transformer | 1.324 [0.650, 2.180] | 4/4 cells, 19/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | frac:0.5 | rmse_h25 | dlinear | 3.695 [3.163, 4.501] | 0/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | frac:0.5 | rmse_h25 | elasticnet | 1.276 [0.963, 1.591] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | frac:0.5 | rmse_h25 | gru | 0.931 [0.472, 1.309] | 3/4 cells, 16/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer | 0.874 [0.329, 1.316] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer_sc | 1.143 [0.732, 1.484] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | frac:0.5 | rmse_h25 | last_slope | 4.282 [2.681, 6.100] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | frac:0.5 | rmse_h25 | lgbm | 0.700 [0.268, 1.226] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | frac:0.5 | rmse_h25 | lstm | 1.055 [0.528, 1.487] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | frac:0.5 | rmse_h25 | nlinear | 1.010 [0.315, 1.705] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | frac:0.5 | rmse_h25 | patchtst | 0.847 [0.308, 1.386] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | frac:0.5 | rmse_h25 | persistence | 1.599 [0.788, 2.409] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | frac:0.5 | rmse_h25 | rlinear | 0.931 [0.207, 1.654] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | frac:0.5 | rmse_h25 | transformer | 1.203 [0.579, 1.645] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | frac:0.5 | rmse_h50 | dlinear | 2.255 [1.429, 3.346] | 0/4 cells, 13/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | frac:0.5 | rmse_h50 | elasticnet | 1.618 [0.982, 2.260] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | frac:0.5 | rmse_h50 | gru | 0.944 [0.275, 1.650] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer | 0.937 [0.336, 1.570] | 4/4 cells, 19/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer_sc | 0.641 [0.141, 1.401] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | frac:0.5 | rmse_h50 | last_slope | 7.386 [2.980, 11.306] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | frac:0.5 | rmse_h50 | lgbm | 0.412 [0.117, 0.753] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | frac:0.5 | rmse_h50 | lstm | 0.786 [0.148, 1.441] | 3/4 cells, 16/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | frac:0.5 | rmse_h50 | nlinear | 1.571 [1.131, 1.888] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | frac:0.5 | rmse_h50 | patchtst | 1.229 [0.484, 1.974] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | frac:0.5 | rmse_h50 | persistence | 1.521 [0.930, 2.368] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | frac:0.5 | rmse_h50 | rlinear | 1.451 [0.742, 1.985] | 2/4 cells, 12/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | frac:0.5 | rmse_h50 | transformer | 0.977 [0.409, 1.860] | 4/4 cells, 18/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | frac:0.7 | rmse_h1 | dlinear | 1.842 [1.546, 2.101] | 0/4 cells, 1/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | frac:0.7 | rmse_h1 | elasticnet | 0.369 [0.244, 0.502] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | frac:0.7 | rmse_h1 | gru | 0.148 [0.086, 0.207] | 1/4 cells, 6/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer | 0.149 [0.051, 0.248] | 0/4 cells, 2/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer_sc | 0.187 [0.061, 0.318] | 0/4 cells, 3/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | frac:0.7 | rmse_h1 | last_slope | 0.112 [0.044, 0.200] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | frac:0.7 | rmse_h1 | lgbm | 0.107 [0.020, 0.236] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | frac:0.7 | rmse_h1 | lstm | 0.143 [0.058, 0.241] | 0/4 cells, 4/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | frac:0.7 | rmse_h1 | nlinear | 0.141 [0.035, 0.257] | 1/4 cells, 4/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | frac:0.7 | rmse_h1 | patchtst | 0.227 [0.104, 0.349] | 0/4 cells, 3/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | frac:0.7 | rmse_h1 | persistence | 0.092 [0.023, 0.162] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | frac:0.7 | rmse_h1 | rlinear | 0.198 [0.098, 0.298] | 0/4 cells, 1/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | frac:0.7 | rmse_h1 | transformer | 0.375 [0.258, 0.474] | 0/4 cells, 4/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | frac:0.7 | rmse_h10 | dlinear | 1.657 [1.202, 2.244] | 0/4 cells, 4/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | frac:0.7 | rmse_h10 | elasticnet | 0.843 [0.660, 1.025] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | frac:0.7 | rmse_h10 | gru | 0.530 [0.144, 1.159] | 3/4 cells, 17/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer | 0.559 [0.190, 1.179] | 2/4 cells, 14/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer_sc | 0.491 [0.091, 1.001] | 3/4 cells, 14/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | frac:0.7 | rmse_h10 | last_slope | 0.861 [0.120, 1.788] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | frac:0.7 | rmse_h10 | lgbm | 0.351 [0.014, 0.934] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | frac:0.7 | rmse_h10 | lstm | 0.476 [0.107, 1.185] | 4/4 cells, 17/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | frac:0.7 | rmse_h10 | nlinear | 0.503 [0.059, 0.947] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | frac:0.7 | rmse_h10 | patchtst | 0.595 [0.462, 0.807] | 1/4 cells, 8/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | frac:0.7 | rmse_h10 | persistence | 0.717 [0.237, 1.507] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | frac:0.7 | rmse_h10 | rlinear | 0.574 [0.120, 1.029] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | frac:0.7 | rmse_h10 | transformer | 0.590 [0.331, 1.042] | 2/4 cells, 13/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | frac:0.7 | rmse_h100 | dlinear | 3.533 [2.811, 4.133] | 1/4 cells, 6/20 cell-seeds (vs last_slope) |  | 4 | 5 | cdb2db6a |
| loco | start_points | frac:0.7 | rmse_h100 | elasticnet | 2.959 [1.475, 4.878] | 1/4 cells, 5/20 cell-seeds (vs last_slope) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | frac:0.7 | rmse_h100 | gru | 2.881 [1.002, 4.760] | 1/4 cells, 9/20 cell-seeds (vs last_slope) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer | 2.116 [0.876, 3.356] | 1/4 cells, 6/20 cell-seeds (vs last_slope) |  | 4 | 5 | 7e863277 |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer_sc | 2.276 [0.938, 3.614] | 1/4 cells, 5/20 cell-seeds (vs last_slope) |  | 4 | 5 | 705b0004 |
| loco | start_points | frac:0.7 | rmse_h100 | last_slope | 2.351 [0.391, 5.280] |  |  | 4 | 5 | 58d2d144 |
| loco | start_points | frac:0.7 | rmse_h100 | lgbm | 2.267 [1.086, 3.448] | 1/4 cells, 5/20 cell-seeds (vs last_slope) |  | 4 | 5 | da32cb37 |
| loco | start_points | frac:0.7 | rmse_h100 | lstm | 2.609 [0.750, 4.468] | 1/4 cells, 6/20 cell-seeds (vs last_slope) |  | 4 | 5 | b8a78a86 |
| loco | start_points | frac:0.7 | rmse_h100 | nlinear | 1.672 [0.589, 2.755] | 1/4 cells, 5/20 cell-seeds (vs last_slope) |  | 4 | 5 | 75eaef84 |
| loco | start_points | frac:0.7 | rmse_h100 | patchtst | 1.591 [0.957, 2.378] | 1/4 cells, 7/20 cell-seeds (vs last_slope) |  | 4 | 5 | 809819d5 |
| loco | start_points | frac:0.7 | rmse_h100 | persistence | 3.080 [1.373, 4.710] | 2/4 cells, 10/20 cell-seeds (vs last_slope) |  | 4 | 5 | 5c5d170c |
| loco | start_points | frac:0.7 | rmse_h100 | rlinear | 1.899 [0.354, 3.444] | 2/4 cells, 9/20 cell-seeds (vs last_slope) |  | 4 | 5 | 2a7b694e |
| loco | start_points | frac:0.7 | rmse_h100 | transformer | 2.865 [1.323, 4.407] | 1/4 cells, 5/20 cell-seeds (vs last_slope) |  | 4 | 5 | 57b6a005 |
| loco | start_points | frac:0.7 | rmse_h25 | dlinear | 3.914 [3.818, 4.032] | 0/4 cells, 3/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | frac:0.7 | rmse_h25 | elasticnet | 1.579 [0.648, 2.510] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | frac:0.7 | rmse_h25 | gru | 0.740 [0.564, 0.858] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer | 0.866 [0.448, 1.281] | 2/4 cells, 9/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer_sc | 0.796 [0.259, 1.264] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | frac:0.7 | rmse_h25 | last_slope | 1.577 [0.923, 2.657] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | frac:0.7 | rmse_h25 | lgbm | 0.729 [0.278, 1.042] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | frac:0.7 | rmse_h25 | lstm | 0.800 [0.520, 1.080] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | frac:0.7 | rmse_h25 | nlinear | 0.863 [0.819, 0.906] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | frac:0.7 | rmse_h25 | patchtst | 0.696 [0.216, 1.344] | 2/4 cells, 13/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | frac:0.7 | rmse_h25 | persistence | 0.714 [0.117, 1.649] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | frac:0.7 | rmse_h25 | rlinear | 0.803 [0.711, 0.894] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | frac:0.7 | rmse_h25 | transformer | 1.003 [0.686, 1.253] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | frac:0.7 | rmse_h50 | dlinear | 2.268 [1.902, 2.795] | 0/4 cells, 8/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | frac:0.7 | rmse_h50 | elasticnet | 1.968 [0.687, 3.250] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | frac:0.7 | rmse_h50 | gru | 1.377 [0.795, 1.945] | 1/4 cells, 6/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer | 1.112 [0.753, 1.427] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer_sc | 1.081 [0.812, 1.421] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | frac:0.7 | rmse_h50 | last_slope | 1.873 [1.076, 3.358] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | frac:0.7 | rmse_h50 | lgbm | 0.932 [0.576, 1.288] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | frac:0.7 | rmse_h50 | lstm | 1.293 [0.739, 1.804] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | frac:0.7 | rmse_h50 | nlinear | 0.710 [0.423, 1.196] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | frac:0.7 | rmse_h50 | patchtst | 0.965 [0.400, 1.662] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | frac:0.7 | rmse_h50 | persistence | 1.046 [0.194, 1.898] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | frac:0.7 | rmse_h50 | rlinear | 0.873 [0.439, 1.365] | 2/4 cells, 11/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | frac:0.7 | rmse_h50 | transformer | 1.353 [0.598, 2.107] | 1/4 cells, 9/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | overall | rmse_h1 | dlinear | 1.782 [1.660, 1.940] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | overall | rmse_h1 | elasticnet | 0.443 [0.367, 0.593] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | overall | rmse_h1 | gru | 0.385 [0.232, 0.538] | 2/4 cells, 9/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | overall | rmse_h1 | itransformer | 0.394 [0.198, 0.589] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | overall | rmse_h1 | itransformer_sc | 0.388 [0.199, 0.577] | 3/4 cells, 14/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | overall | rmse_h1 | last_slope | 0.455 [0.240, 0.669] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | overall | rmse_h1 | lgbm | 0.355 [0.160, 0.550] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | overall | rmse_h1 | lstm | 0.411 [0.197, 0.625] | 1/4 cells, 8/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | overall | rmse_h1 | nlinear | 0.388 [0.179, 0.598] | 3/4 cells, 13/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | overall | rmse_h1 | patchtst | 0.422 [0.243, 0.602] | 2/4 cells, 9/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | overall | rmse_h1 | persistence | 0.397 [0.177, 0.617] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | overall | rmse_h1 | rlinear | 0.397 [0.187, 0.607] | 2/4 cells, 11/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | overall | rmse_h1 | transformer | 0.531 [0.370, 0.660] | 0/4 cells, 4/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | overall | rmse_h10 | dlinear | 2.329 [2.203, 2.516] | 0/4 cells, 4/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | overall | rmse_h10 | elasticnet | 1.152 [0.786, 1.794] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | overall | rmse_h10 | gru | 0.994 [0.540, 1.570] | 4/4 cells, 19/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | overall | rmse_h10 | itransformer | 1.049 [0.716, 1.546] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | overall | rmse_h10 | itransformer_sc | 1.046 [0.706, 1.558] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | overall | rmse_h10 | last_slope | 2.474 [2.053, 3.110] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | overall | rmse_h10 | lgbm | 0.991 [0.502, 1.671] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | overall | rmse_h10 | lstm | 1.061 [0.601, 1.694] | 3/4 cells, 16/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | overall | rmse_h10 | nlinear | 0.984 [0.573, 1.613] | 4/4 cells, 18/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | overall | rmse_h10 | patchtst | 1.010 [0.695, 1.582] | 4/4 cells, 19/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | overall | rmse_h10 | persistence | 1.332 [1.082, 1.703] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | overall | rmse_h10 | rlinear | 0.992 [0.625, 1.571] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | overall | rmse_h10 | transformer | 1.062 [0.753, 1.556] | 4/4 cells, 18/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | overall | rmse_h100 | dlinear | 3.249 [2.825, 3.673] | 1/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | overall | rmse_h100 | elasticnet | 2.687 [1.986, 3.824] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | overall | rmse_h100 | gru | 2.469 [1.625, 3.314] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | overall | rmse_h100 | itransformer | 1.857 [1.064, 2.592] | 3/4 cells, 16/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | overall | rmse_h100 | itransformer_sc | 2.017 [1.250, 2.625] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | overall | rmse_h100 | last_slope | 15.247 [12.166, 18.329] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | overall | rmse_h100 | lgbm | 2.059 [1.587, 2.578] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | overall | rmse_h100 | lstm | 2.222 [1.450, 2.995] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | overall | rmse_h100 | nlinear | 2.487 [1.451, 3.581] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | overall | rmse_h100 | patchtst | 2.509 [1.546, 3.727] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | overall | rmse_h100 | persistence | 2.680 [1.781, 3.658] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | overall | rmse_h100 | rlinear | 2.674 [1.592, 3.955] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | overall | rmse_h100 | transformer | 2.382 [1.626, 3.139] | 3/4 cells, 14/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | overall | rmse_h25 | dlinear | 4.088 [3.926, 4.310] | 0/4 cells, 1/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | overall | rmse_h25 | elasticnet | 1.586 [0.999, 2.173] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | overall | rmse_h25 | gru | 1.218 [0.966, 1.470] | 3/4 cells, 11/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | overall | rmse_h25 | itransformer | 1.071 [0.847, 1.382] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | overall | rmse_h25 | itransformer_sc | 1.126 [0.861, 1.405] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | overall | rmse_h25 | last_slope | 4.141 [3.336, 4.947] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | overall | rmse_h25 | lgbm | 1.142 [0.859, 1.541] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | overall | rmse_h25 | lstm | 1.131 [0.923, 1.338] | 3/4 cells, 17/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | overall | rmse_h25 | nlinear | 1.326 [1.093, 1.660] | 3/4 cells, 12/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | overall | rmse_h25 | patchtst | 1.146 [0.895, 1.546] | 3/4 cells, 14/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | overall | rmse_h25 | persistence | 1.317 [1.143, 1.422] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | overall | rmse_h25 | rlinear | 1.278 [1.007, 1.635] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | overall | rmse_h25 | transformer | 1.280 [1.082, 1.485] | 3/4 cells, 12/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |
| loco | start_points | overall | rmse_h50 | dlinear | 2.621 [2.272, 2.890] | 0/4 cells, 7/20 cell-seeds (vs persistence) |  | 4 | 5 | cdb2db6a |
| loco | start_points | overall | rmse_h50 | elasticnet | 2.314 [1.273, 3.356] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 0dfa2e62 |
| loco | start_points | overall | rmse_h50 | gru | 1.799 [1.111, 2.286] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | ed5ee0b9 |
| loco | start_points | overall | rmse_h50 | itransformer | 1.492 [0.997, 2.046] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 7e863277 |
| loco | start_points | overall | rmse_h50 | itransformer_sc | 1.489 [1.031, 2.007] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 705b0004 |
| loco | start_points | overall | rmse_h50 | last_slope | 7.343 [6.361, 8.324] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 58d2d144 |
| loco | start_points | overall | rmse_h50 | lgbm | 1.496 [0.956, 2.036] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | da32cb37 |
| loco | start_points | overall | rmse_h50 | lstm | 1.668 [1.065, 2.137] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | b8a78a86 |
| loco | start_points | overall | rmse_h50 | nlinear | 1.773 [1.163, 2.684] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 75eaef84 |
| loco | start_points | overall | rmse_h50 | patchtst | 1.638 [1.038, 2.538] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 809819d5 |
| loco | start_points | overall | rmse_h50 | persistence | 1.506 [1.020, 1.989] |  |  | 4 | 5 | 5c5d170c |
| loco | start_points | overall | rmse_h50 | rlinear | 1.750 [1.240, 2.648] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 2a7b694e |
| loco | start_points | overall | rmse_h50 | transformer | 1.852 [1.266, 2.326] | 1/4 cells, 6/20 cell-seeds (vs persistence) |  | 4 | 5 | 57b6a005 |

</details>

<details><summary>calce_rul (187 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rul_bias | dlinear | 16.929 [-8.692, 42.293] |  |  | 4 | 5 | 2954d2ac |
| loco | all | overall | rul_bias | elasticnet | 72.029 [-11.748, 208.288] |  |  | 4 | 5 | 96e56f24 |
| loco | all | overall | rul_bias | gru | -3.799 [-61.887, 68.955] |  |  | 4 | 5 | 800a470b |
| loco | all | overall | rul_bias | itransformer | 18.298 [-38.908, 86.338] |  |  | 4 | 5 | cad19238 |
| loco | all | overall | rul_bias | itransformer_sc | 20.543 [-34.649, 86.718] |  |  | 4 | 5 | 8125fe8a |
| loco | all | overall | rul_bias | lgbm | -2.960 [-63.578, 69.990] |  |  | 4 | 5 | c2305071 |
| loco | all | overall | rul_bias | lstm | 9.937 [-45.987, 81.702] |  |  | 4 | 5 | 6c1ef016 |
| loco | all | overall | rul_bias | nlinear | 14.884 [-11.818, 41.586] |  |  | 4 | 5 | 119d8ef1 |
| loco | all | overall | rul_bias | patchtst | 17.915 [-12.201, 48.402] |  |  | 4 | 5 | 65d9f648 |
| loco | all | overall | rul_bias | rlinear | -93.970 [-101.641, -83.310] |  |  | 4 | 5 | bdad0aa4 |
| loco | all | overall | rul_bias | transformer | 11.840 [-47.036, 89.272] |  |  | 4 | 5 | b001f101 |
| loco | all | overall | rul_mae | dlinear | 129.127 [123.850, 134.697] |  |  | 4 | 5 | 2954d2ac |
| loco | all | overall | rul_mae | elasticnet | 155.562 [81.341, 232.171] |  |  | 4 | 5 | 96e56f24 |
| loco | all | overall | rul_mae | gru | 85.032 [62.752, 107.312] |  |  | 4 | 5 | 800a470b |
| loco | all | overall | rul_mae | itransformer | 68.193 [40.047, 100.169] |  |  | 4 | 5 | cad19238 |
| loco | all | overall | rul_mae | itransformer_sc | 67.558 [42.668, 102.179] |  |  | 4 | 5 | 8125fe8a |
| loco | all | overall | rul_mae | lgbm | 74.731 [53.242, 96.522] |  |  | 4 | 5 | c2305071 |
| loco | all | overall | rul_mae | lstm | 72.319 [50.230, 101.873] |  |  | 4 | 5 | 6c1ef016 |
| loco | all | overall | rul_mae | nlinear | 127.936 [124.783, 132.629] |  |  | 4 | 5 | 119d8ef1 |
| loco | all | overall | rul_mae | patchtst | 110.910 [97.504, 121.278] |  |  | 4 | 5 | 65d9f648 |
| loco | all | overall | rul_mae | rlinear | 179.443 [163.112, 198.825] |  |  | 4 | 5 | bdad0aa4 |
| loco | all | overall | rul_mae | transformer | 83.204 [52.577, 113.832] |  |  | 4 | 5 | b001f101 |
| loco | start_points | fixed:200 | rul_bias | dlinear | -120.475 [-154.732, -72.017] |  |  | 4 | 5 | 2954d2ac |
| loco | start_points | fixed:200 | rul_bias | elasticnet | 32.919 [-122.186, 234.188] |  |  | 4 | 5 | 96e56f24 |
| loco | start_points | fixed:200 | rul_bias | gru | -34.053 [-100.068, 59.951] |  |  | 4 | 5 | 800a470b |
| loco | start_points | fixed:200 | rul_bias | itransformer | 4.552 [-75.135, 106.715] |  |  | 4 | 5 | cad19238 |
| loco | start_points | fixed:200 | rul_bias | itransformer_sc | -6.305 [-93.066, 96.196] |  |  | 4 | 5 | 8125fe8a |
| loco | start_points | fixed:200 | rul_bias | lgbm | -36.993 [-122.445, 79.674] |  |  | 4 | 5 | c2305071 |
| loco | start_points | fixed:200 | rul_bias | lstm | -22.217 [-105.562, 79.096] |  |  | 4 | 5 | 6c1ef016 |
| loco | start_points | fixed:200 | rul_bias | nlinear | -134.745 [-167.077, -86.619] |  |  | 4 | 5 | 119d8ef1 |
| loco | start_points | fixed:200 | rul_bias | patchtst | -78.884 [-152.439, -1.991] |  |  | 4 | 5 | 65d9f648 |
| loco | start_points | fixed:200 | rul_bias | rlinear | -214.857 [-297.528, -101.881] |  |  | 4 | 5 | bdad0aa4 |
| loco | start_points | fixed:200 | rul_bias | transformer | 8.214 [-55.034, 103.651] |  |  | 4 | 5 | b001f101 |
| loco | start_points | fixed:200 | rul_mae | dlinear | 120.475 [72.017, 154.732] |  |  | 4 | 5 | 2954d2ac |
| loco | start_points | fixed:200 | rul_mae | elasticnet | 126.666 [13.245, 244.566] |  |  | 4 | 5 | 96e56f24 |
| loco | start_points | fixed:200 | rul_mae | gru | 85.087 [62.043, 108.130] |  |  | 4 | 5 | 800a470b |
| loco | start_points | fixed:200 | rul_mae | itransformer | 85.896 [41.517, 130.721] |  |  | 4 | 5 | cad19238 |
| loco | start_points | fixed:200 | rul_mae | itransformer_sc | 80.712 [26.630, 134.793] |  |  | 4 | 5 | 8125fe8a |
| loco | start_points | fixed:200 | rul_mae | lgbm | 101.589 [68.209, 134.969] |  |  | 4 | 5 | c2305071 |
| loco | start_points | fixed:200 | rul_mae | lstm | 91.011 [48.260, 133.763] |  |  | 4 | 5 | 6c1ef016 |
| loco | start_points | fixed:200 | rul_mae | nlinear | 134.745 [86.619, 167.077] |  |  | 4 | 5 | 119d8ef1 |
| loco | start_points | fixed:200 | rul_mae | patchtst | 98.070 [43.701, 152.439] |  |  | 4 | 5 | 65d9f648 |
| loco | start_points | fixed:200 | rul_mae | rlinear | 214.857 [101.881, 297.528] |  |  | 4 | 5 | bdad0aa4 |
| loco | start_points | fixed:200 | rul_mae | transformer | 68.339 [26.011, 123.973] |  |  | 4 | 5 | b001f101 |
| loco | start_points | fixed:400 | rul_bias | dlinear | 109.514 [59.049, 186.425] |  |  | 4 | 5 | 2954d2ac |
| loco | start_points | fixed:400 | rul_bias | elasticnet | -15.376 [-73.979, 43.226] |  |  | 4 | 5 | 96e56f24 |
| loco | start_points | fixed:400 | rul_bias | gru | 46.383 [-26.666, 119.433] |  |  | 4 | 5 | 800a470b |
| loco | start_points | fixed:400 | rul_bias | itransformer | 22.876 [-42.380, 101.440] |  |  | 4 | 5 | cad19238 |
| loco | start_points | fixed:400 | rul_bias | itransformer_sc | 24.934 [-41.060, 90.929] |  |  | 4 | 5 | 8125fe8a |
| loco | start_points | fixed:400 | rul_bias | lgbm | 35.419 [-41.346, 112.183] |  |  | 4 | 5 | c2305071 |
| loco | start_points | fixed:400 | rul_bias | lstm | 36.710 [-28.472, 101.893] |  |  | 4 | 5 | 6c1ef016 |
| loco | start_points | fixed:400 | rul_bias | nlinear | 107.188 [45.587, 183.722] |  |  | 4 | 5 | 119d8ef1 |
| loco | start_points | fixed:400 | rul_bias | patchtst | 89.948 [20.774, 160.602] |  |  | 4 | 5 | 65d9f648 |
| loco | start_points | fixed:400 | rul_bias | rlinear | 39.916 [-116.379, 196.211] |  |  | 4 | 5 | bdad0aa4 |
| loco | start_points | fixed:400 | rul_bias | transformer | 43.058 [-40.984, 127.100] |  |  | 4 | 5 | b001f101 |
| loco | start_points | fixed:400 | rul_mae | dlinear | 109.514 [59.049, 186.425] |  |  | 4 | 5 | 2954d2ac |
| loco | start_points | fixed:400 | rul_mae | elasticnet | 58.603 [42.482, 89.494] |  |  | 4 | 5 | 96e56f24 |
| loco | start_points | fixed:400 | rul_mae | gru | 73.049 [26.666, 122.747] |  |  | 4 | 5 | 800a470b |
| loco | start_points | fixed:400 | rul_mae | itransformer | 59.628 [19.249, 108.536] |  |  | 4 | 5 | cad19238 |
| loco | start_points | fixed:400 | rul_mae | itransformer_sc | 68.970 [34.033, 96.035] |  |  | 4 | 5 | 8125fe8a |
| loco | start_points | fixed:400 | rul_mae | lgbm | 76.765 [41.346, 112.183] |  |  | 4 | 5 | c2305071 |
| loco | start_points | fixed:400 | rul_mae | lstm | 65.653 [29.413, 101.893] |  |  | 4 | 5 | 6c1ef016 |
| loco | start_points | fixed:400 | rul_mae | nlinear | 107.188 [45.587, 183.722] |  |  | 4 | 5 | 119d8ef1 |
| loco | start_points | fixed:400 | rul_mae | patchtst | 93.283 [30.780, 160.602] |  |  | 4 | 5 | 65d9f648 |
| loco | start_points | fixed:400 | rul_mae | rlinear | 156.295 [116.379, 201.948] |  |  | 4 | 5 | bdad0aa4 |
| loco | start_points | fixed:400 | rul_mae | transformer | 84.944 [42.681, 135.726] |  |  | 4 | 5 | b001f101 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | dlinear | 0.250 [0.000, 0.750] |  |  | 4 | 5 | 2954d2ac |
| loco | start_points | frac:0.3 | alpha_lambda_acc | elasticnet | 0.250 [0.000, 0.750] |  |  | 4 | 5 | 96e56f24 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | gru | 0.350 [0.100, 0.600] |  |  | 4 | 5 | 800a470b |
| loco | start_points | frac:0.3 | alpha_lambda_acc | itransformer | 0.350 [0.050, 0.800] |  |  | 4 | 5 | cad19238 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | itransformer_sc | 0.600 [0.200, 1.000] |  |  | 4 | 5 | 8125fe8a |
| loco | start_points | frac:0.3 | alpha_lambda_acc | lgbm | 0.250 [0.000, 0.750] |  |  | 4 | 5 | c2305071 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | lstm | 0.300 [0.000, 0.600] |  |  | 4 | 5 | 6c1ef016 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | nlinear | 0.250 [0.000, 0.750] |  |  | 4 | 5 | 119d8ef1 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | patchtst | 0.200 [0.000, 0.450] |  |  | 4 | 5 | 65d9f648 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | rlinear | 0.250 [0.000, 0.750] |  |  | 4 | 5 | bdad0aa4 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | transformer | 0.500 [0.000, 1.000] |  |  | 4 | 5 | b001f101 |
| loco | start_points | frac:0.3 | rul_bias | dlinear | -121.151 [-165.065, -44.267] |  |  | 4 | 5 | 2954d2ac |
| loco | start_points | frac:0.3 | rul_bias | elasticnet | 20.386 [-186.235, 339.772] |  |  | 4 | 5 | 96e56f24 |
| loco | start_points | frac:0.3 | rul_bias | gru | -53.898 [-114.454, 33.144] |  |  | 4 | 5 | 800a470b |
| loco | start_points | frac:0.3 | rul_bias | itransformer | -18.562 [-101.003, 63.879] |  |  | 4 | 5 | cad19238 |
| loco | start_points | frac:0.3 | rul_bias | itransformer_sc | -0.222 [-74.583, 74.139] |  |  | 4 | 5 | 8125fe8a |
| loco | start_points | frac:0.3 | rul_bias | lgbm | -48.348 [-98.425, 34.166] |  |  | 4 | 5 | c2305071 |
| loco | start_points | frac:0.3 | rul_bias | lstm | -41.141 [-100.292, 43.064] |  |  | 4 | 5 | 6c1ef016 |
| loco | start_points | frac:0.3 | rul_bias | nlinear | -124.766 [-186.204, -21.900] |  |  | 4 | 5 | 119d8ef1 |
| loco | start_points | frac:0.3 | rul_bias | patchtst | -105.094 [-121.410, -78.563] |  |  | 4 | 5 | 65d9f648 |
| loco | start_points | frac:0.3 | rul_bias | rlinear | -196.619 [-303.409, -89.829] |  |  | 4 | 5 | bdad0aa4 |
| loco | start_points | frac:0.3 | rul_bias | transformer | -18.431 [-90.740, 82.434] |  |  | 4 | 5 | b001f101 |
| loco | start_points | frac:0.3 | rul_mae | dlinear | 121.151 [44.267, 165.065] |  |  | 4 | 5 | 2954d2ac |
| loco | start_points | frac:0.3 | rul_mae | elasticnet | 236.606 [92.378, 431.206] |  |  | 4 | 5 | 96e56f24 |
| loco | start_points | frac:0.3 | rul_mae | gru | 89.862 [74.743, 114.454] |  |  | 4 | 5 | 800a470b |
| loco | start_points | frac:0.3 | rul_mae | itransformer | 82.441 [52.695, 109.352] |  |  | 4 | 5 | cad19238 |
| loco | start_points | frac:0.3 | rul_mae | itransformer_sc | 74.361 [59.414, 89.308] |  |  | 4 | 5 | 8125fe8a |
| loco | start_points | frac:0.3 | rul_mae | lgbm | 84.749 [75.036, 98.425] |  |  | 4 | 5 | c2305071 |
| loco | start_points | frac:0.3 | rul_mae | lstm | 85.543 [63.126, 102.023] |  |  | 4 | 5 | 6c1ef016 |
| loco | start_points | frac:0.3 | rul_mae | nlinear | 138.589 [63.370, 186.204] |  |  | 4 | 5 | 119d8ef1 |
| loco | start_points | frac:0.3 | rul_mae | patchtst | 105.094 [78.563, 121.410] |  |  | 4 | 5 | 65d9f648 |
| loco | start_points | frac:0.3 | rul_mae | rlinear | 196.619 [89.829, 303.409] |  |  | 4 | 5 | bdad0aa4 |
| loco | start_points | frac:0.3 | rul_mae | transformer | 81.681 [46.987, 116.375] |  |  | 4 | 5 | b001f101 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | dlinear | 0.450 [0.100, 0.800] |  |  | 4 | 5 | 2954d2ac |
| loco | start_points | frac:0.5 | alpha_lambda_acc | elasticnet | 0.250 [0.000, 0.750] |  |  | 4 | 5 | 96e56f24 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | gru | 0.650 [0.250, 1.000] |  |  | 4 | 5 | 800a470b |
| loco | start_points | frac:0.5 | alpha_lambda_acc | itransformer | 0.500 [0.000, 1.000] |  |  | 4 | 5 | cad19238 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | itransformer_sc | 0.550 [0.200, 0.900] |  |  | 4 | 5 | 8125fe8a |
| loco | start_points | frac:0.5 | alpha_lambda_acc | lgbm | 0.750 [0.250, 1.000] |  |  | 4 | 5 | c2305071 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | lstm | 0.550 [0.100, 1.000] |  |  | 4 | 5 | 6c1ef016 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | nlinear | 0.250 [0.000, 0.600] |  |  | 4 | 5 | 119d8ef1 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | patchtst | 0.350 [0.000, 0.750] |  |  | 4 | 5 | 65d9f648 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | rlinear | 0.000 [0.000, 0.000] |  |  | 4 | 5 | bdad0aa4 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | transformer | 0.700 [0.250, 1.000] |  |  | 4 | 5 | b001f101 |
| loco | start_points | frac:0.5 | rul_bias | dlinear | -9.782 [-65.633, 46.070] |  |  | 4 | 5 | 2954d2ac |
| loco | start_points | frac:0.5 | rul_bias | elasticnet | 52.903 [-113.798, 330.337] |  |  | 4 | 5 | 96e56f24 |
| loco | start_points | frac:0.5 | rul_bias | gru | 15.487 [-44.089, 102.361] |  |  | 4 | 5 | 800a470b |
| loco | start_points | frac:0.5 | rul_bias | itransformer | 46.788 [-19.549, 113.125] |  |  | 4 | 5 | cad19238 |
| loco | start_points | frac:0.5 | rul_bias | itransformer_sc | 39.139 [-34.026, 137.459] |  |  | 4 | 5 | 8125fe8a |
| loco | start_points | frac:0.5 | rul_bias | lgbm | 16.238 [-43.309, 102.150] |  |  | 4 | 5 | c2305071 |
| loco | start_points | frac:0.5 | rul_bias | lstm | 21.328 [-47.574, 115.618] |  |  | 4 | 5 | 6c1ef016 |
| loco | start_points | frac:0.5 | rul_bias | nlinear | -6.691 [-71.651, 58.269] |  |  | 4 | 5 | 119d8ef1 |
| loco | start_points | frac:0.5 | rul_bias | patchtst | 22.433 [-40.219, 85.085] |  |  | 4 | 5 | 65d9f648 |
| loco | start_points | frac:0.5 | rul_bias | rlinear | -145.775 [-249.616, 0.130] |  |  | 4 | 5 | bdad0aa4 |
| loco | start_points | frac:0.5 | rul_bias | transformer | 42.582 [-31.368, 135.595] |  |  | 4 | 5 | b001f101 |
| loco | start_points | frac:0.5 | rul_mae | dlinear | 55.852 [45.055, 65.633] |  |  | 4 | 5 | 2954d2ac |
| loco | start_points | frac:0.5 | rul_mae | elasticnet | 185.072 [57.829, 383.588] |  |  | 4 | 5 | 96e56f24 |
| loco | start_points | frac:0.5 | rul_mae | gru | 59.683 [16.955, 117.239] |  |  | 4 | 5 | 800a470b |
| loco | start_points | frac:0.5 | rul_mae | itransformer | 70.294 [27.462, 115.905] |  |  | 4 | 5 | cad19238 |
| loco | start_points | frac:0.5 | rul_mae | itransformer_sc | 74.784 [28.509, 150.096] |  |  | 4 | 5 | 8125fe8a |
| loco | start_points | frac:0.5 | rul_mae | lgbm | 59.546 [14.688, 120.643] |  |  | 4 | 5 | c2305071 |
| loco | start_points | frac:0.5 | rul_mae | lstm | 68.528 [21.557, 127.703] |  |  | 4 | 5 | 6c1ef016 |
| loco | start_points | frac:0.5 | rul_mae | nlinear | 64.960 [54.665, 76.414] |  |  | 4 | 5 | 119d8ef1 |
| loco | start_points | frac:0.5 | rul_mae | patchtst | 63.149 [33.356, 85.085] |  |  | 4 | 5 | 65d9f648 |
| loco | start_points | frac:0.5 | rul_mae | rlinear | 185.900 [120.244, 249.616] |  |  | 4 | 5 | bdad0aa4 |
| loco | start_points | frac:0.5 | rul_mae | transformer | 73.950 [26.860, 151.279] |  |  | 4 | 5 | b001f101 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | dlinear | 0.050 [0.000, 0.150] |  |  | 4 | 5 | 2954d2ac |
| loco | start_points | frac:0.7 | alpha_lambda_acc | elasticnet | 0.250 [0.000, 0.750] |  |  | 4 | 5 | 96e56f24 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | gru | 0.200 [0.000, 0.600] |  |  | 4 | 5 | 800a470b |
| loco | start_points | frac:0.7 | alpha_lambda_acc | itransformer | 0.250 [0.000, 0.600] |  |  | 4 | 5 | cad19238 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | itransformer_sc | 0.300 [0.000, 0.600] |  |  | 4 | 5 | 8125fe8a |
| loco | start_points | frac:0.7 | alpha_lambda_acc | lgbm | 0.250 [0.000, 0.750] |  |  | 4 | 5 | c2305071 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | lstm | 0.250 [0.000, 0.750] |  |  | 4 | 5 | 6c1ef016 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | nlinear | 0.250 [0.000, 0.750] |  |  | 4 | 5 | 119d8ef1 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | patchtst | 0.050 [0.000, 0.150] |  |  | 4 | 5 | 65d9f648 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | rlinear | 0.000 [0.000, 0.000] |  |  | 4 | 5 | bdad0aa4 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | transformer | 0.050 [0.000, 0.150] |  |  | 4 | 5 | b001f101 |
| loco | start_points | frac:0.7 | rul_bias | dlinear | 86.699 [49.451, 137.385] |  |  | 4 | 5 | 2954d2ac |
| loco | start_points | frac:0.7 | rul_bias | elasticnet | 10.319 [-63.483, 84.121] |  |  | 4 | 5 | 96e56f24 |
| loco | start_points | frac:0.7 | rul_bias | gru | 35.714 [-46.188, 121.268] |  |  | 4 | 5 | 800a470b |
| loco | start_points | frac:0.7 | rul_bias | itransformer | 41.382 [-47.312, 128.906] |  |  | 4 | 5 | cad19238 |
| loco | start_points | frac:0.7 | rul_bias | itransformer_sc | 31.023 [-35.096, 109.182] |  |  | 4 | 5 | 8125fe8a |
| loco | start_points | frac:0.7 | rul_bias | lgbm | 32.243 [-55.588, 120.074] |  |  | 4 | 5 | c2305071 |
| loco | start_points | frac:0.7 | rul_bias | lstm | 40.922 [-48.016, 129.861] |  |  | 4 | 5 | 6c1ef016 |
| loco | start_points | frac:0.7 | rul_bias | nlinear | 74.500 [27.571, 133.830] |  |  | 4 | 5 | 119d8ef1 |
| loco | start_points | frac:0.7 | rul_bias | patchtst | 97.790 [66.739, 128.396] |  |  | 4 | 5 | 65d9f648 |
| loco | start_points | frac:0.7 | rul_bias | rlinear | -49.038 [-125.962, 100.667] |  |  | 4 | 5 | bdad0aa4 |
| loco | start_points | frac:0.7 | rul_bias | transformer | 36.983 [-54.128, 133.964] |  |  | 4 | 5 | b001f101 |
| loco | start_points | frac:0.7 | rul_mae | dlinear | 86.699 [49.451, 137.385] |  |  | 4 | 5 | 2954d2ac |
| loco | start_points | frac:0.7 | rul_mae | elasticnet | 73.802 [48.724, 95.660] |  |  | 4 | 5 | 96e56f24 |
| loco | start_points | frac:0.7 | rul_mae | gru | 81.902 [36.610, 144.158] |  |  | 4 | 5 | 800a470b |
| loco | start_points | frac:0.7 | rul_mae | itransformer | 84.779 [36.085, 141.521] |  |  | 4 | 5 | cad19238 |
| loco | start_points | frac:0.7 | rul_mae | itransformer_sc | 66.098 [29.618, 118.771] |  |  | 4 | 5 | 8125fe8a |
| loco | start_points | frac:0.7 | rul_mae | lgbm | 87.831 [48.071, 131.499] |  |  | 4 | 5 | c2305071 |
| loco | start_points | frac:0.7 | rul_mae | lstm | 89.580 [30.666, 146.669] |  |  | 4 | 5 | 6c1ef016 |
| loco | start_points | frac:0.7 | rul_mae | nlinear | 74.500 [27.571, 133.830] |  |  | 4 | 5 | 119d8ef1 |
| loco | start_points | frac:0.7 | rul_mae | patchtst | 97.790 [66.739, 128.396] |  |  | 4 | 5 | 65d9f648 |
| loco | start_points | frac:0.7 | rul_mae | rlinear | 136.713 [121.820, 162.357] |  |  | 4 | 5 | bdad0aa4 |
| loco | start_points | frac:0.7 | rul_mae | transformer | 91.111 [54.128, 161.028] |  |  | 4 | 5 | b001f101 |
| loco | start_points | overall | rul_bias | dlinear | -11.039 [-37.801, 13.123] |  |  | 4 | 5 | 2954d2ac |
| loco | start_points | overall | rul_bias | elasticnet | 20.230 [-106.878, 205.323] |  |  | 4 | 5 | 96e56f24 |
| loco | start_points | overall | rul_bias | gru | 1.927 [-61.878, 82.418] |  |  | 4 | 5 | 800a470b |
| loco | start_points | overall | rul_bias | itransformer | 19.407 [-52.636, 97.360] |  |  | 4 | 5 | cad19238 |
| loco | start_points | overall | rul_bias | itransformer_sc | 17.714 [-53.231, 94.594] |  |  | 4 | 5 | 8125fe8a |
| loco | start_points | overall | rul_bias | lgbm | -0.288 [-67.514, 79.782] |  |  | 4 | 5 | c2305071 |
| loco | start_points | overall | rul_bias | lstm | 7.121 [-65.764, 88.228] |  |  | 4 | 5 | 6c1ef016 |
| loco | start_points | overall | rul_bias | nlinear | -16.903 [-38.767, 4.017] |  |  | 4 | 5 | 119d8ef1 |
| loco | start_points | overall | rul_bias | patchtst | 5.239 [-31.278, 41.755] |  |  | 4 | 5 | 65d9f648 |
| loco | start_points | overall | rul_bias | rlinear | -113.274 [-150.554, -71.530] |  |  | 4 | 5 | bdad0aa4 |
| loco | start_points | overall | rul_bias | transformer | 22.481 [-51.349, 111.929] |  |  | 4 | 5 | b001f101 |
| loco | start_points | overall | rul_mae | dlinear | 98.738 [70.053, 122.669] |  |  | 4 | 5 | 2954d2ac |
| loco | start_points | overall | rul_mae | elasticnet | 136.150 [60.142, 235.394] |  |  | 4 | 5 | 96e56f24 |
| loco | start_points | overall | rul_mae | gru | 77.916 [57.871, 111.354] |  |  | 4 | 5 | 800a470b |
| loco | start_points | overall | rul_mae | itransformer | 76.607 [43.841, 116.139] |  |  | 4 | 5 | cad19238 |
| loco | start_points | overall | rul_mae | itransformer_sc | 72.985 [38.624, 111.943] |  |  | 4 | 5 | 8125fe8a |
| loco | start_points | overall | rul_mae | lgbm | 82.096 [61.527, 110.784] |  |  | 4 | 5 | c2305071 |
| loco | start_points | overall | rul_mae | lstm | 80.063 [50.396, 113.203] |  |  | 4 | 5 | 6c1ef016 |
| loco | start_points | overall | rul_mae | nlinear | 103.996 [70.666, 131.870] |  |  | 4 | 5 | 119d8ef1 |
| loco | start_points | overall | rul_mae | patchtst | 91.477 [76.484, 106.470] |  |  | 4 | 5 | 65d9f648 |
| loco | start_points | overall | rul_mae | rlinear | 178.077 [153.136, 203.017] |  |  | 4 | 5 | bdad0aa4 |
| loco | start_points | overall | rul_mae | transformer | 80.005 [49.439, 136.511] |  |  | 4 | 5 | b001f101 |

</details>

<details><summary>calce_soh (84 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse | dlinear | 2.492 [2.307, 2.671] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 3160ba54 |
| loco | all | overall | rmse | elasticnet | 0.658 [0.575, 0.766] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 3ffdca0f |
| loco | all | overall | rmse | gru | 1.712 [1.536, 1.921] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 4604bc09 |
| loco | all | overall | rmse | itransformer | 1.256 [1.212, 1.304] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 0b237c08 |
| loco | all | overall | rmse | itransformer_sc | 1.269 [1.201, 1.338] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 2d772b8f |
| loco | all | overall | rmse | lgbm | 1.193 [1.104, 1.317] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 95b19ba2 |
| loco | all | overall | rmse | lstm | 1.622 [1.409, 1.835] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) |  | 4 | 5 | b7364c34 |
| loco | all | overall | rmse | nlinear | 2.431 [2.243, 2.600] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 65662866 |
| loco | all | overall | rmse | patchtst | 1.957 [1.879, 2.037] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 3bd1f9b9 |
| loco | all | overall | rmse | prev_soh | 2.606 [2.429, 2.783] |  |  | 4 | 5 | a4feb20f |
| loco | all | overall | rmse | rlinear | 2.512 [2.340, 2.690] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 69bff78f |
| loco | all | overall | rmse | transformer | 1.760 [1.637, 1.882] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) |  | 4 | 5 | cb5b78e5 |
| loco | start_points | fixed:200 | rmse | dlinear | 0.500 [0.378, 0.696] | 3/4 cells, 14/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 3160ba54 |
| loco | start_points | fixed:200 | rmse | elasticnet | 0.401 [0.247, 0.582] | 3/4 cells, 15/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 3ffdca0f |
| loco | start_points | fixed:200 | rmse | gru | 0.518 [0.375, 0.735] | 2/4 cells, 10/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 4604bc09 |
| loco | start_points | fixed:200 | rmse | itransformer | 0.253 [0.170, 0.388] | 4/4 cells, 17/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 0b237c08 |
| loco | start_points | fixed:200 | rmse | itransformer_sc | 0.359 [0.255, 0.469] | 2/4 cells, 12/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 2d772b8f |
| loco | start_points | fixed:200 | rmse | lgbm | 0.304 [0.041, 0.566] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 95b19ba2 |
| loco | start_points | fixed:200 | rmse | lstm | 0.565 [0.413, 0.723] | 1/4 cells, 6/20 cell-seeds (vs prev_soh) |  | 4 | 5 | b7364c34 |
| loco | start_points | fixed:200 | rmse | nlinear | 0.512 [0.352, 0.715] | 2/4 cells, 11/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 65662866 |
| loco | start_points | fixed:200 | rmse | patchtst | 0.401 [0.153, 0.688] | 3/4 cells, 13/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 3bd1f9b9 |
| loco | start_points | fixed:200 | rmse | prev_soh | 0.491 [0.256, 0.727] |  |  | 4 | 5 | a4feb20f |
| loco | start_points | fixed:200 | rmse | rlinear | 0.479 [0.330, 0.670] | 2/4 cells, 10/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 69bff78f |
| loco | start_points | fixed:200 | rmse | transformer | 0.505 [0.302, 0.726] | 1/4 cells, 11/20 cell-seeds (vs prev_soh) |  | 4 | 5 | cb5b78e5 |
| loco | start_points | fixed:400 | rmse | dlinear | 0.124 [0.076, 0.181] | 1/4 cells, 4/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 3160ba54 |
| loco | start_points | fixed:400 | rmse | elasticnet | 0.100 [0.052, 0.149] | 1/4 cells, 5/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 3ffdca0f |
| loco | start_points | fixed:400 | rmse | gru | 0.111 [0.052, 0.179] | 1/4 cells, 10/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 4604bc09 |
| loco | start_points | fixed:400 | rmse | itransformer | 0.089 [0.033, 0.165] | 2/4 cells, 11/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 0b237c08 |
| loco | start_points | fixed:400 | rmse | itransformer_sc | 0.090 [0.039, 0.153] | 1/4 cells, 6/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 2d772b8f |
| loco | start_points | fixed:400 | rmse | lgbm | 0.092 [0.023, 0.174] | 2/4 cells, 10/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 95b19ba2 |
| loco | start_points | fixed:400 | rmse | lstm | 0.154 [0.054, 0.281] | 0/4 cells, 4/20 cell-seeds (vs prev_soh) |  | 4 | 5 | b7364c34 |
| loco | start_points | fixed:400 | rmse | nlinear | 0.125 [0.044, 0.220] | 0/4 cells, 3/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 65662866 |
| loco | start_points | fixed:400 | rmse | patchtst | 0.076 [0.029, 0.122] | 1/4 cells, 9/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 3bd1f9b9 |
| loco | start_points | fixed:400 | rmse | prev_soh | 0.091 [0.019, 0.181] |  |  | 4 | 5 | a4feb20f |
| loco | start_points | fixed:400 | rmse | rlinear | 0.114 [0.045, 0.199] | 0/4 cells, 4/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 69bff78f |
| loco | start_points | fixed:400 | rmse | transformer | 0.159 [0.076, 0.313] | 1/4 cells, 7/20 cell-seeds (vs prev_soh) |  | 4 | 5 | cb5b78e5 |
| loco | start_points | frac:0.3 | rmse | dlinear | 0.565 [0.269, 0.861] | 0/4 cells, 0/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 3160ba54 |
| loco | start_points | frac:0.3 | rmse | elasticnet | 0.515 [0.265, 0.765] | 1/4 cells, 5/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 3ffdca0f |
| loco | start_points | frac:0.3 | rmse | gru | 0.485 [0.104, 0.866] | 0/4 cells, 6/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 4604bc09 |
| loco | start_points | frac:0.3 | rmse | itransformer | 0.205 [0.074, 0.426] | 2/4 cells, 11/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 0b237c08 |
| loco | start_points | frac:0.3 | rmse | itransformer_sc | 0.225 [0.057, 0.493] | 3/4 cells, 14/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 2d772b8f |
| loco | start_points | frac:0.3 | rmse | lgbm | 0.315 [0.120, 0.510] | 2/4 cells, 10/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 95b19ba2 |
| loco | start_points | frac:0.3 | rmse | lstm | 0.483 [0.065, 0.902] | 2/4 cells, 10/20 cell-seeds (vs prev_soh) |  | 4 | 5 | b7364c34 |
| loco | start_points | frac:0.3 | rmse | nlinear | 0.554 [0.249, 0.859] | 1/4 cells, 5/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 65662866 |
| loco | start_points | frac:0.3 | rmse | patchtst | 0.422 [0.105, 0.739] | 2/4 cells, 11/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 3bd1f9b9 |
| loco | start_points | frac:0.3 | rmse | prev_soh | 0.429 [0.046, 0.811] |  |  | 4 | 5 | a4feb20f |
| loco | start_points | frac:0.3 | rmse | rlinear | 0.512 [0.186, 0.837] | 1/4 cells, 5/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 69bff78f |
| loco | start_points | frac:0.3 | rmse | transformer | 0.501 [0.134, 0.867] | 0/4 cells, 2/20 cell-seeds (vs prev_soh) |  | 4 | 5 | cb5b78e5 |
| loco | start_points | frac:0.5 | rmse | dlinear | 0.051 [0.021, 0.081] | 3/4 cells, 15/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 3160ba54 |
| loco | start_points | frac:0.5 | rmse | elasticnet | 0.125 [0.084, 0.162] | 2/4 cells, 10/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 3ffdca0f |
| loco | start_points | frac:0.5 | rmse | gru | 0.118 [0.044, 0.244] | 2/4 cells, 12/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 4604bc09 |
| loco | start_points | frac:0.5 | rmse | itransformer | 0.138 [0.023, 0.299] | 3/4 cells, 15/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 0b237c08 |
| loco | start_points | frac:0.5 | rmse | itransformer_sc | 0.145 [0.021, 0.311] | 3/4 cells, 15/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 2d772b8f |
| loco | start_points | frac:0.5 | rmse | lgbm | 0.111 [0.031, 0.190] | 3/4 cells, 15/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 95b19ba2 |
| loco | start_points | frac:0.5 | rmse | lstm | 0.160 [0.029, 0.409] | 2/4 cells, 10/20 cell-seeds (vs prev_soh) |  | 4 | 5 | b7364c34 |
| loco | start_points | frac:0.5 | rmse | nlinear | 0.054 [0.028, 0.080] | 3/4 cells, 18/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 65662866 |
| loco | start_points | frac:0.5 | rmse | patchtst | 0.135 [0.034, 0.267] | 3/4 cells, 15/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 3bd1f9b9 |
| loco | start_points | frac:0.5 | rmse | prev_soh | 0.156 [0.035, 0.291] |  |  | 4 | 5 | a4feb20f |
| loco | start_points | frac:0.5 | rmse | rlinear | 0.068 [0.045, 0.100] | 2/4 cells, 10/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 69bff78f |
| loco | start_points | frac:0.5 | rmse | transformer | 0.126 [0.045, 0.258] | 2/4 cells, 13/20 cell-seeds (vs prev_soh) |  | 4 | 5 | cb5b78e5 |
| loco | start_points | frac:0.7 | rmse | dlinear | 0.091 [0.028, 0.153] | 1/4 cells, 5/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 3160ba54 |
| loco | start_points | frac:0.7 | rmse | elasticnet | 0.061 [0.010, 0.139] | 1/4 cells, 5/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 3ffdca0f |
| loco | start_points | frac:0.7 | rmse | gru | 0.096 [0.051, 0.143] | 1/4 cells, 6/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 4604bc09 |
| loco | start_points | frac:0.7 | rmse | itransformer | 0.062 [0.020, 0.112] | 2/4 cells, 9/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 0b237c08 |
| loco | start_points | frac:0.7 | rmse | itransformer_sc | 0.050 [0.024, 0.072] | 2/4 cells, 9/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 2d772b8f |
| loco | start_points | frac:0.7 | rmse | lgbm | 0.071 [0.031, 0.128] | 1/4 cells, 5/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 95b19ba2 |
| loco | start_points | frac:0.7 | rmse | lstm | 0.146 [0.070, 0.218] | 0/4 cells, 0/20 cell-seeds (vs prev_soh) |  | 4 | 5 | b7364c34 |
| loco | start_points | frac:0.7 | rmse | nlinear | 0.073 [0.017, 0.129] | 2/4 cells, 10/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 65662866 |
| loco | start_points | frac:0.7 | rmse | patchtst | 0.094 [0.027, 0.173] | 1/4 cells, 6/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 3bd1f9b9 |
| loco | start_points | frac:0.7 | rmse | prev_soh | 0.075 [0.005, 0.144] |  |  | 4 | 5 | a4feb20f |
| loco | start_points | frac:0.7 | rmse | rlinear | 0.087 [0.016, 0.158] | 0/4 cells, 5/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 69bff78f |
| loco | start_points | frac:0.7 | rmse | transformer | 0.161 [0.054, 0.267] | 0/4 cells, 2/20 cell-seeds (vs prev_soh) |  | 4 | 5 | cb5b78e5 |
| loco | start_points | overall | rmse | dlinear | 0.362 [0.243, 0.481] | 1/4 cells, 5/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 3160ba54 |
| loco | start_points | overall | rmse | elasticnet | 0.315 [0.219, 0.419] | 2/4 cells, 10/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 3ffdca0f |
| loco | start_points | overall | rmse | gru | 0.366 [0.231, 0.500] | 2/4 cells, 9/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 4604bc09 |
| loco | start_points | overall | rmse | itransformer | 0.192 [0.106, 0.279] | 4/4 cells, 18/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 0b237c08 |
| loco | start_points | overall | rmse | itransformer_sc | 0.235 [0.145, 0.324] | 3/4 cells, 18/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 2d772b8f |
| loco | start_points | overall | rmse | lgbm | 0.242 [0.124, 0.342] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 95b19ba2 |
| loco | start_points | overall | rmse | lstm | 0.407 [0.258, 0.516] | 2/4 cells, 7/20 cell-seeds (vs prev_soh) |  | 4 | 5 | b7364c34 |
| loco | start_points | overall | rmse | nlinear | 0.368 [0.263, 0.472] | 2/4 cells, 11/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 65662866 |
| loco | start_points | overall | rmse | patchtst | 0.310 [0.166, 0.438] | 3/4 cells, 17/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 3bd1f9b9 |
| loco | start_points | overall | rmse | prev_soh | 0.359 [0.261, 0.456] |  |  | 4 | 5 | a4feb20f |
| loco | start_points | overall | rmse | rlinear | 0.349 [0.239, 0.459] | 2/4 cells, 10/20 cell-seeds (vs prev_soh) |  | 4 | 5 | 69bff78f |
| loco | start_points | overall | rmse | transformer | 0.391 [0.278, 0.487] | 0/4 cells, 6/20 cell-seeds (vs prev_soh) |  | 4 | 5 | cb5b78e5 |

</details>

<details><summary>nasa_forecast (455 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | dlinear | 3.641 [3.606, 3.688] | 0/4 cells, 0/20 cell-seeds (vs persistence) | 3.627 | 4 | 5 | 3b67b415 |
| loco | all | overall | rmse_h1 | elasticnet | 0.945 [0.707, 1.183] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 1.228 | 4 | 5 | e1ff5d55 |
| loco | all | overall | rmse_h1 | gru | 2.279 [1.787, 2.772] | 0/4 cells, 0/20 cell-seeds (vs persistence) | 3.030 | 4 | 5 | 9731ae77 |
| loco | all | overall | rmse_h1 | itransformer | 0.915 [0.660, 1.171] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 1.217 | 4 | 5 | 9dedaedf |
| loco | all | overall | rmse_h1 | itransformer_sc | 0.929 [0.681, 1.176] | 4/4 cells, 17/20 cell-seeds (vs persistence) | 1.222 | 4 | 5 | e5cc9a22 |
| loco | all | overall | rmse_h1 | last_slope | 0.992 [0.715, 1.269] | 0/4 cells, 0/20 cell-seeds (vs persistence) | 1.301 | 4 | 5 | 7a0d4ec4 |
| loco | all | overall | rmse_h1 | lgbm | 0.938 [0.700, 1.177] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 1.211 | 4 | 5 | acedf5f4 |
| loco | all | overall | rmse_h1 | lstm | 1.919 [1.475, 2.363] | 0/4 cells, 0/20 cell-seeds (vs persistence) | 2.419 | 4 | 5 | 5494788a |
| loco | all | overall | rmse_h1 | nlinear | 0.948 [0.706, 1.191] | 3/4 cells, 12/20 cell-seeds (vs persistence) | 1.227 | 4 | 5 | b4ecdb12 |
| loco | all | overall | rmse_h1 | patchtst | 0.908 [0.651, 1.165] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 1.217 | 4 | 5 | d75a14c6 |
| loco | all | overall | rmse_h1 | persistence | 0.955 [0.697, 1.213] |  | 1.245 | 4 | 5 | a26a213d |
| loco | all | overall | rmse_h1 | rlinear | 0.959 [0.700, 1.217] | 0/4 cells, 8/20 cell-seeds (vs persistence) | 1.246 | 4 | 5 | 78bc3e35 |
| loco | all | overall | rmse_h1 | transformer | 2.761 [1.698, 4.062] | 0/4 cells, 0/20 cell-seeds (vs persistence) | 4.628 | 4 | 5 | 19b71fc1 |
| loco | all | overall | rmse_h10 | dlinear | 6.802 [6.386, 7.217] | 0/4 cells, 0/20 cell-seeds (vs persistence) | 7.046 | 4 | 5 | 3b67b415 |
| loco | all | overall | rmse_h10 | elasticnet | 2.821 [1.604, 4.037] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 3.630 | 4 | 5 | e1ff5d55 |
| loco | all | overall | rmse_h10 | gru | 2.921 [2.175, 4.002] | 2/4 cells, 8/20 cell-seeds (vs persistence) | 2.767 | 4 | 5 | 9731ae77 |
| loco | all | overall | rmse_h10 | itransformer | 1.732 [1.081, 2.384] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 2.600 | 4 | 5 | 9dedaedf |
| loco | all | overall | rmse_h10 | itransformer_sc | 1.801 [1.205, 2.397] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 2.563 | 4 | 5 | e5cc9a22 |
| loco | all | overall | rmse_h10 | last_slope | 2.986 [2.037, 3.934] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 3.895 | 4 | 5 | 7a0d4ec4 |
| loco | all | overall | rmse_h10 | lgbm | 1.805 [1.302, 2.309] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 2.347 | 4 | 5 | acedf5f4 |
| loco | all | overall | rmse_h10 | lstm | 2.703 [2.283, 3.394] | 2/4 cells, 13/20 cell-seeds (vs persistence) | 2.491 | 4 | 5 | 5494788a |
| loco | all | overall | rmse_h10 | nlinear | 1.921 [1.390, 2.451] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 2.576 | 4 | 5 | b4ecdb12 |
| loco | all | overall | rmse_h10 | patchtst | 1.726 [1.121, 2.332] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 2.515 | 4 | 5 | d75a14c6 |
| loco | all | overall | rmse_h10 | persistence | 2.737 [2.186, 3.288] |  | 3.153 | 4 | 5 | a26a213d |
| loco | all | overall | rmse_h10 | rlinear | 2.076 [1.425, 2.728] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 2.857 | 4 | 5 | 78bc3e35 |
| loco | all | overall | rmse_h10 | transformer | 4.143 [2.826, 6.087] | 0/4 cells, 6/20 cell-seeds (vs persistence) | 7.085 | 4 | 5 | 19b71fc1 |
| loco | all | overall | rmse_h100 | dlinear | 19.437 [17.666, 21.209] | 1/4 cells, 13/20 cell-seeds (vs last_slope) | 18.206 | 4 | 5 | 3b67b415 |
| loco | all | overall | rmse_h100 | elasticnet | 7.512 [3.048, 13.437] | 4/4 cells, 20/20 cell-seeds (vs last_slope) | 3.889 | 4 | 5 | e1ff5d55 |
| loco | all | overall | rmse_h100 | gru | 4.704 [3.204, 6.204] | 4/4 cells, 20/20 cell-seeds (vs last_slope) | 2.853 | 4 | 5 | 9731ae77 |
| loco | all | overall | rmse_h100 | itransformer | 14.185 [13.080, 15.690] | 4/4 cells, 20/20 cell-seeds (vs last_slope) | 12.938 | 4 | 5 | 9dedaedf |
| loco | all | overall | rmse_h100 | itransformer_sc | 9.236 [7.338, 11.439] | 4/4 cells, 20/20 cell-seeds (vs last_slope) | 8.511 | 4 | 5 | e5cc9a22 |
| loco | all | overall | rmse_h100 | last_slope | 20.888 [14.826, 29.272] |  | 14.274 | 4 | 5 | 7a0d4ec4 |
| loco | all | overall | rmse_h100 | lgbm | 3.869 [2.348, 5.389] | 4/4 cells, 20/20 cell-seeds (vs last_slope) | 2.617 | 4 | 5 | acedf5f4 |
| loco | all | overall | rmse_h100 | lstm | 4.855 [2.611, 7.100] | 4/4 cells, 20/20 cell-seeds (vs last_slope) | 2.560 | 4 | 5 | 5494788a |
| loco | all | overall | rmse_h100 | nlinear | 4.364 [3.361, 5.620] | 4/4 cells, 20/20 cell-seeds (vs last_slope) | 3.109 | 4 | 5 | b4ecdb12 |
| loco | all | overall | rmse_h100 | patchtst | 10.048 [6.329, 15.530] | 4/4 cells, 20/20 cell-seeds (vs last_slope) | 8.388 | 4 | 5 | d75a14c6 |
| loco | all | overall | rmse_h100 | persistence | 21.343 [19.065, 23.828] | 1/4 cells, 5/20 cell-seeds (vs last_slope) | 20.144 | 4 | 5 | a26a213d |
| loco | all | overall | rmse_h100 | rlinear | 13.904 [10.763, 17.492] | 4/4 cells, 20/20 cell-seeds (vs last_slope) | 10.129 | 4 | 5 | 78bc3e35 |
| loco | all | overall | rmse_h100 | transformer | 4.910 [2.432, 7.387] | 4/4 cells, 20/20 cell-seeds (vs last_slope) | 2.995 | 4 | 5 | 19b71fc1 |
| loco | all | overall | rmse_h25 | dlinear | 4.263 [4.036, 4.471] | 4/4 cells, 15/20 cell-seeds (vs persistence) | 4.426 | 4 | 5 | 3b67b415 |
| loco | all | overall | rmse_h25 | elasticnet | 5.219 [2.991, 7.555] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 5.867 | 4 | 5 | e1ff5d55 |
| loco | all | overall | rmse_h25 | gru | 4.035 [3.412, 4.657] | 4/4 cells, 18/20 cell-seeds (vs persistence) | 3.671 | 4 | 5 | 9731ae77 |
| loco | all | overall | rmse_h25 | itransformer | 2.601 [1.955, 3.307] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.753 | 4 | 5 | 9dedaedf |
| loco | all | overall | rmse_h25 | itransformer_sc | 2.718 [1.883, 3.553] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.946 | 4 | 5 | e5cc9a22 |
| loco | all | overall | rmse_h25 | last_slope | 5.958 [4.205, 7.710] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 7.523 | 4 | 5 | 7a0d4ec4 |
| loco | all | overall | rmse_h25 | lgbm | 2.652 [2.059, 3.245] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.187 | 4 | 5 | acedf5f4 |
| loco | all | overall | rmse_h25 | lstm | 4.309 [3.512, 5.447] | 4/4 cells, 18/20 cell-seeds (vs persistence) | 3.482 | 4 | 5 | 5494788a |
| loco | all | overall | rmse_h25 | nlinear | 2.896 [2.383, 3.409] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.515 | 4 | 5 | b4ecdb12 |
| loco | all | overall | rmse_h25 | patchtst | 2.543 [1.934, 3.152] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.350 | 4 | 5 | d75a14c6 |
| loco | all | overall | rmse_h25 | persistence | 5.731 [4.913, 6.569] |  | 6.007 | 4 | 5 | a26a213d |
| loco | all | overall | rmse_h25 | rlinear | 3.564 [2.789, 4.339] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 4.677 | 4 | 5 | 78bc3e35 |
| loco | all | overall | rmse_h25 | transformer | 4.442 [3.583, 5.051] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 4.794 | 4 | 5 | 19b71fc1 |
| loco | all | overall | rmse_h50 | dlinear | 11.250 [10.299, 12.159] | 2/4 cells, 12/20 cell-seeds (vs persistence) | 11.168 | 4 | 5 | 3b67b415 |
| loco | all | overall | rmse_h50 | elasticnet | 5.321 [3.447, 7.988] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 4.946 | 4 | 5 | e1ff5d55 |
| loco | all | overall | rmse_h50 | gru | 4.409 [3.333, 5.745] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.657 | 4 | 5 | 9731ae77 |
| loco | all | overall | rmse_h50 | itransformer | 5.378 [5.169, 5.574] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 5.322 | 4 | 5 | 9dedaedf |
| loco | all | overall | rmse_h50 | itransformer_sc | 4.052 [3.721, 4.328] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.563 | 4 | 5 | e5cc9a22 |
| loco | all | overall | rmse_h50 | last_slope | 12.164 [8.884, 15.444] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 14.476 | 4 | 5 | 7a0d4ec4 |
| loco | all | overall | rmse_h50 | lgbm | 3.238 [2.423, 4.261] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.065 | 4 | 5 | acedf5f4 |
| loco | all | overall | rmse_h50 | lstm | 3.577 [3.104, 4.415] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.141 | 4 | 5 | 5494788a |
| loco | all | overall | rmse_h50 | nlinear | 3.461 [2.715, 4.395] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.087 | 4 | 5 | b4ecdb12 |
| loco | all | overall | rmse_h50 | patchtst | 4.020 [2.930, 5.537] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.560 | 4 | 5 | d75a14c6 |
| loco | all | overall | rmse_h50 | persistence | 11.211 [9.697, 12.759] |  | 11.258 | 4 | 5 | a26a213d |
| loco | all | overall | rmse_h50 | rlinear | 6.700 [6.010, 7.359] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 6.835 | 4 | 5 | 78bc3e35 |
| loco | all | overall | rmse_h50 | transformer | 5.448 [4.164, 6.496] | 4/4 cells, 19/20 cell-seeds (vs persistence) | 5.462 | 4 | 5 | 19b71fc1 |
| loco | start_points | fixed:30 | rmse_h1 | dlinear | 3.933 [3.414, 4.373] | 0/4 cells, 5/20 cell-seeds (vs persistence) | 3.137 | 4 | 5 | 3b67b415 |
| loco | start_points | fixed:30 | rmse_h1 | elasticnet | 2.361 [1.240, 3.306] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 0.558 | 4 | 5 | e1ff5d55 |
| loco | start_points | fixed:30 | rmse_h1 | gru | 2.106 [1.339, 3.222] | 2/4 cells, 11/20 cell-seeds (vs persistence) | 1.779 | 4 | 5 | 9731ae77 |
| loco | start_points | fixed:30 | rmse_h1 | itransformer | 2.218 [0.832, 3.435] | 1/4 cells, 5/20 cell-seeds (vs persistence) | 0.173 | 4 | 5 | 9dedaedf |
| loco | start_points | fixed:30 | rmse_h1 | itransformer_sc | 2.195 [0.767, 3.403] | 1/4 cells, 5/20 cell-seeds (vs persistence) | 0.085 | 4 | 5 | e5cc9a22 |
| loco | start_points | fixed:30 | rmse_h1 | last_slope | 2.349 [1.110, 3.513] | 1/4 cells, 5/20 cell-seeds (vs persistence) | 0.537 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | fixed:30 | rmse_h1 | lgbm | 2.296 [0.831, 3.415] | 1/4 cells, 5/20 cell-seeds (vs persistence) | 0.104 | 4 | 5 | acedf5f4 |
| loco | start_points | fixed:30 | rmse_h1 | lstm | 2.606 [1.717, 3.422] | 1/4 cells, 10/20 cell-seeds (vs persistence) | 1.344 | 4 | 5 | 5494788a |
| loco | start_points | fixed:30 | rmse_h1 | nlinear | 2.299 [0.936, 3.395] | 1/4 cells, 5/20 cell-seeds (vs persistence) | 0.283 | 4 | 5 | b4ecdb12 |
| loco | start_points | fixed:30 | rmse_h1 | patchtst | 2.282 [0.957, 3.480] | 1/4 cells, 5/20 cell-seeds (vs persistence) | 0.328 | 4 | 5 | d75a14c6 |
| loco | start_points | fixed:30 | rmse_h1 | persistence | 2.105 [1.142, 2.970] |  | 0.659 | 4 | 5 | a26a213d |
| loco | start_points | fixed:30 | rmse_h1 | rlinear | 2.152 [0.895, 3.304] | 1/4 cells, 7/20 cell-seeds (vs persistence) | 0.311 | 4 | 5 | 78bc3e35 |
| loco | start_points | fixed:30 | rmse_h1 | transformer | 2.196 [1.618, 2.786] | 3/4 cells, 10/20 cell-seeds (vs persistence) | 2.324 | 4 | 5 | 19b71fc1 |
| loco | start_points | fixed:30 | rmse_h10 | dlinear | 6.315 [5.213, 7.775] | 0/4 cells, 0/20 cell-seeds (vs last_slope) | 6.218 | 4 | 5 | 3b67b415 |
| loco | start_points | fixed:30 | rmse_h10 | elasticnet | 2.032 [1.243, 3.311] | 0/4 cells, 0/20 cell-seeds (vs last_slope) | 1.099 | 4 | 5 | e1ff5d55 |
| loco | start_points | fixed:30 | rmse_h10 | gru | 2.131 [1.075, 3.846] | 0/4 cells, 1/20 cell-seeds (vs last_slope) | 1.368 | 4 | 5 | 9731ae77 |
| loco | start_points | fixed:30 | rmse_h10 | itransformer | 1.069 [0.328, 2.088] | 2/4 cells, 10/20 cell-seeds (vs last_slope) | 2.666 | 4 | 5 | 9dedaedf |
| loco | start_points | fixed:30 | rmse_h10 | itransformer_sc | 1.302 [0.535, 2.094] | 2/4 cells, 9/20 cell-seeds (vs last_slope) | 2.537 | 4 | 5 | e5cc9a22 |
| loco | start_points | fixed:30 | rmse_h10 | last_slope | 0.696 [0.129, 1.432] |  | 0.251 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | fixed:30 | rmse_h10 | lgbm | 1.201 [0.326, 2.077] | 1/4 cells, 5/20 cell-seeds (vs last_slope) | 1.804 | 4 | 5 | acedf5f4 |
| loco | start_points | fixed:30 | rmse_h10 | lstm | 2.326 [1.151, 4.056] | 0/4 cells, 3/20 cell-seeds (vs last_slope) | 0.847 | 4 | 5 | 5494788a |
| loco | start_points | fixed:30 | rmse_h10 | nlinear | 1.190 [0.146, 2.458] | 1/4 cells, 5/20 cell-seeds (vs last_slope) | 1.258 | 4 | 5 | b4ecdb12 |
| loco | start_points | fixed:30 | rmse_h10 | patchtst | 0.875 [0.276, 1.681] | 2/4 cells, 10/20 cell-seeds (vs last_slope) | 2.026 | 4 | 5 | d75a14c6 |
| loco | start_points | fixed:30 | rmse_h10 | persistence | 2.367 [1.235, 4.018] | 0/4 cells, 0/20 cell-seeds (vs last_slope) | 0.977 | 4 | 5 | a26a213d |
| loco | start_points | fixed:30 | rmse_h10 | rlinear | 2.103 [1.407, 3.086] | 0/4 cells, 0/20 cell-seeds (vs last_slope) | 1.209 | 4 | 5 | 78bc3e35 |
| loco | start_points | fixed:30 | rmse_h10 | transformer | 2.912 [1.724, 4.312] | 0/4 cells, 2/20 cell-seeds (vs last_slope) | 5.145 | 4 | 5 | 19b71fc1 |
| loco | start_points | fixed:30 | rmse_h100 | dlinear | 19.936 [16.681, 22.906] | 1/4 cells, 5/20 cell-seeds (vs last_slope) | 14.635 | 4 | 5 | 3b67b415 |
| loco | start_points | fixed:30 | rmse_h100 | elasticnet | 7.473 [3.197, 13.573] | 2/4 cells, 10/20 cell-seeds (vs last_slope) | 3.747 | 4 | 5 | e1ff5d55 |
| loco | start_points | fixed:30 | rmse_h100 | gru | 3.156 [1.243, 5.895] | 2/4 cells, 10/20 cell-seeds (vs last_slope) | 1.484 | 4 | 5 | 9731ae77 |
| loco | start_points | fixed:30 | rmse_h100 | itransformer | 13.205 [7.506, 17.853] | 2/4 cells, 10/20 cell-seeds (vs last_slope) | 4.608 | 4 | 5 | 9dedaedf |
| loco | start_points | fixed:30 | rmse_h100 | itransformer_sc | 9.164 [4.701, 13.626] | 2/4 cells, 8/20 cell-seeds (vs last_slope) | 6.175 | 4 | 5 | e5cc9a22 |
| loco | start_points | fixed:30 | rmse_h100 | last_slope | 11.712 [0.440, 29.881] |  | 6.309 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | fixed:30 | rmse_h100 | lgbm | 3.934 [2.536, 5.454] | 2/4 cells, 10/20 cell-seeds (vs last_slope) | 2.833 | 4 | 5 | acedf5f4 |
| loco | start_points | fixed:30 | rmse_h100 | lstm | 4.024 [1.394, 6.654] | 2/4 cells, 12/20 cell-seeds (vs last_slope) | 1.566 | 4 | 5 | 5494788a |
| loco | start_points | fixed:30 | rmse_h100 | nlinear | 4.434 [2.837, 6.032] | 2/4 cells, 11/20 cell-seeds (vs last_slope) | 3.647 | 4 | 5 | b4ecdb12 |
| loco | start_points | fixed:30 | rmse_h100 | patchtst | 6.901 [3.421, 10.381] | 2/4 cells, 10/20 cell-seeds (vs last_slope) | 1.955 | 4 | 5 | d75a14c6 |
| loco | start_points | fixed:30 | rmse_h100 | persistence | 22.041 [19.036, 25.046] | 1/4 cells, 5/20 cell-seeds (vs last_slope) | 18.594 | 4 | 5 | a26a213d |
| loco | start_points | fixed:30 | rmse_h100 | rlinear | 10.555 [4.370, 15.864] | 1/4 cells, 5/20 cell-seeds (vs last_slope) | 9.303 | 4 | 5 | 78bc3e35 |
| loco | start_points | fixed:30 | rmse_h100 | transformer | 4.518 [2.016, 7.021] | 2/4 cells, 11/20 cell-seeds (vs last_slope) | 3.220 | 4 | 5 | 19b71fc1 |
| loco | start_points | fixed:30 | rmse_h25 | dlinear | 3.801 [3.289, 4.137] | 1/4 cells, 8/20 cell-seeds (vs last_slope) | 3.048 | 4 | 5 | 3b67b415 |
| loco | start_points | fixed:30 | rmse_h25 | elasticnet | 4.443 [3.217, 6.214] | 1/4 cells, 5/20 cell-seeds (vs last_slope) | 3.163 | 4 | 5 | e1ff5d55 |
| loco | start_points | fixed:30 | rmse_h25 | gru | 4.103 [2.335, 5.507] | 2/4 cells, 9/20 cell-seeds (vs last_slope) | 1.403 | 4 | 5 | 9731ae77 |
| loco | start_points | fixed:30 | rmse_h25 | itransformer | 1.949 [1.150, 2.748] | 2/4 cells, 9/20 cell-seeds (vs last_slope) | 2.772 | 4 | 5 | 9dedaedf |
| loco | start_points | fixed:30 | rmse_h25 | itransformer_sc | 2.057 [1.272, 3.185] | 2/4 cells, 10/20 cell-seeds (vs last_slope) | 3.697 | 4 | 5 | e5cc9a22 |
| loco | start_points | fixed:30 | rmse_h25 | last_slope | 2.904 [0.640, 6.334] |  | 1.727 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | fixed:30 | rmse_h25 | lgbm | 1.812 [0.667, 2.958] | 3/4 cells, 15/20 cell-seeds (vs last_slope) | 2.694 | 4 | 5 | acedf5f4 |
| loco | start_points | fixed:30 | rmse_h25 | lstm | 4.817 [2.840, 6.393] | 1/4 cells, 7/20 cell-seeds (vs last_slope) | 1.768 | 4 | 5 | 5494788a |
| loco | start_points | fixed:30 | rmse_h25 | nlinear | 2.165 [1.214, 3.686] | 3/4 cells, 14/20 cell-seeds (vs last_slope) | 1.066 | 4 | 5 | b4ecdb12 |
| loco | start_points | fixed:30 | rmse_h25 | patchtst | 1.166 [0.625, 1.593] | 3/4 cells, 12/20 cell-seeds (vs last_slope) | 1.719 | 4 | 5 | d75a14c6 |
| loco | start_points | fixed:30 | rmse_h25 | persistence | 5.609 [4.366, 7.695] | 0/4 cells, 0/20 cell-seeds (vs last_slope) | 4.798 | 4 | 5 | a26a213d |
| loco | start_points | fixed:30 | rmse_h25 | rlinear | 3.369 [1.715, 4.964] | 2/4 cells, 10/20 cell-seeds (vs last_slope) | 1.039 | 4 | 5 | 78bc3e35 |
| loco | start_points | fixed:30 | rmse_h25 | transformer | 4.253 [3.002, 5.503] | 1/4 cells, 5/20 cell-seeds (vs last_slope) | 3.801 | 4 | 5 | 19b71fc1 |
| loco | start_points | fixed:30 | rmse_h50 | dlinear | 15.015 [13.569, 16.953] | 0/4 cells, 1/20 cell-seeds (vs last_slope) | 13.149 | 4 | 5 | 3b67b415 |
| loco | start_points | fixed:30 | rmse_h50 | elasticnet | 5.474 [1.979, 9.705] | 3/4 cells, 15/20 cell-seeds (vs last_slope) | 6.094 | 4 | 5 | e1ff5d55 |
| loco | start_points | fixed:30 | rmse_h50 | gru | 4.077 [1.968, 6.611] | 2/4 cells, 12/20 cell-seeds (vs last_slope) | 3.631 | 4 | 5 | 9731ae77 |
| loco | start_points | fixed:30 | rmse_h50 | itransformer | 6.921 [4.205, 9.413] | 2/4 cells, 10/20 cell-seeds (vs last_slope) | 2.499 | 4 | 5 | 9dedaedf |
| loco | start_points | fixed:30 | rmse_h50 | itransformer_sc | 5.284 [3.104, 7.428] | 2/4 cells, 10/20 cell-seeds (vs last_slope) | 1.884 | 4 | 5 | e5cc9a22 |
| loco | start_points | fixed:30 | rmse_h50 | last_slope | 6.306 [1.574, 11.656] |  | 7.235 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | fixed:30 | rmse_h50 | lgbm | 2.911 [0.945, 5.460] | 3/4 cells, 15/20 cell-seeds (vs last_slope) | 2.932 | 4 | 5 | acedf5f4 |
| loco | start_points | fixed:30 | rmse_h50 | lstm | 3.225 [1.057, 6.429] | 4/4 cells, 18/20 cell-seeds (vs last_slope) | 2.372 | 4 | 5 | 5494788a |
| loco | start_points | fixed:30 | rmse_h50 | nlinear | 2.939 [1.032, 5.847] | 3/4 cells, 15/20 cell-seeds (vs last_slope) | 1.785 | 4 | 5 | b4ecdb12 |
| loco | start_points | fixed:30 | rmse_h50 | patchtst | 3.238 [1.507, 4.969] | 2/4 cells, 10/20 cell-seeds (vs last_slope) | 0.778 | 4 | 5 | d75a14c6 |
| loco | start_points | fixed:30 | rmse_h50 | persistence | 14.185 [12.427, 16.944] | 0/4 cells, 0/20 cell-seeds (vs last_slope) | 13.377 | 4 | 5 | a26a213d |
| loco | start_points | fixed:30 | rmse_h50 | rlinear | 7.857 [4.984, 10.162] | 2/4 cells, 10/20 cell-seeds (vs last_slope) | 3.337 | 4 | 5 | 78bc3e35 |
| loco | start_points | fixed:30 | rmse_h50 | transformer | 5.247 [3.346, 7.589] | 2/4 cells, 12/20 cell-seeds (vs last_slope) | 4.701 | 4 | 5 | 19b71fc1 |
| loco | start_points | fixed:50 | rmse_h1 | dlinear | 3.953 [3.850, 4.055] | 0/4 cells, 2/20 cell-seeds (vs persistence) | 3.836 | 4 | 5 | 3b67b415 |
| loco | start_points | fixed:50 | rmse_h1 | elasticnet | 0.526 [0.349, 0.704] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 0.384 | 4 | 5 | e1ff5d55 |
| loco | start_points | fixed:50 | rmse_h1 | gru | 2.141 [1.699, 2.793] | 0/4 cells, 5/20 cell-seeds (vs persistence) | 3.140 | 4 | 5 | 9731ae77 |
| loco | start_points | fixed:50 | rmse_h1 | itransformer | 0.476 [0.082, 0.870] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 1.087 | 4 | 5 | 9dedaedf |
| loco | start_points | fixed:50 | rmse_h1 | itransformer_sc | 0.454 [0.100, 0.809] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 0.713 | 4 | 5 | e5cc9a22 |
| loco | start_points | fixed:50 | rmse_h1 | last_slope | 0.750 [0.234, 1.464] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 0.104 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | fixed:50 | rmse_h1 | lgbm | 0.525 [0.050, 1.001] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 0.915 | 4 | 5 | acedf5f4 |
| loco | start_points | fixed:50 | rmse_h1 | lstm | 1.247 [0.886, 1.609] | 1/4 cells, 9/20 cell-seeds (vs persistence) | 1.701 | 4 | 5 | 5494788a |
| loco | start_points | fixed:50 | rmse_h1 | nlinear | 0.450 [0.134, 0.766] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 0.607 | 4 | 5 | b4ecdb12 |
| loco | start_points | fixed:50 | rmse_h1 | patchtst | 0.652 [0.175, 1.246] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 1.596 | 4 | 5 | d75a14c6 |
| loco | start_points | fixed:50 | rmse_h1 | persistence | 0.733 [0.375, 1.283] |  | 0.313 | 4 | 5 | a26a213d |
| loco | start_points | fixed:50 | rmse_h1 | rlinear | 0.494 [0.292, 0.786] | 3/4 cells, 16/20 cell-seeds (vs persistence) | 0.444 | 4 | 5 | 78bc3e35 |
| loco | start_points | fixed:50 | rmse_h1 | transformer | 2.338 [1.086, 3.590] | 0/4 cells, 6/20 cell-seeds (vs persistence) | 4.185 | 4 | 5 | 19b71fc1 |
| loco | start_points | fixed:50 | rmse_h10 | dlinear | 7.651 [6.743, 9.183] | 0/4 cells, 2/20 cell-seeds (vs persistence) | 7.129 | 4 | 5 | 3b67b415 |
| loco | start_points | fixed:50 | rmse_h10 | elasticnet | 2.854 [0.575, 5.134] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 5.410 | 4 | 5 | e1ff5d55 |
| loco | start_points | fixed:50 | rmse_h10 | gru | 2.033 [1.038, 3.273] | 4/4 cells, 19/20 cell-seeds (vs persistence) | 2.081 | 4 | 5 | 9731ae77 |
| loco | start_points | fixed:50 | rmse_h10 | itransformer | 1.047 [0.525, 1.565] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 0.322 | 4 | 5 | 9dedaedf |
| loco | start_points | fixed:50 | rmse_h10 | itransformer_sc | 1.899 [1.060, 3.158] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 1.680 | 4 | 5 | e5cc9a22 |
| loco | start_points | fixed:50 | rmse_h10 | last_slope | 6.496 [3.997, 8.995] | 1/4 cells, 5/20 cell-seeds (vs persistence) | 8.191 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | fixed:50 | rmse_h10 | lgbm | 2.036 [0.864, 3.813] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 0.723 | 4 | 5 | acedf5f4 |
| loco | start_points | fixed:50 | rmse_h10 | lstm | 2.679 [1.335, 4.025] | 4/4 cells, 18/20 cell-seeds (vs persistence) | 3.176 | 4 | 5 | 5494788a |
| loco | start_points | fixed:50 | rmse_h10 | nlinear | 2.171 [1.257, 3.558] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 1.893 | 4 | 5 | b4ecdb12 |
| loco | start_points | fixed:50 | rmse_h10 | patchtst | 0.989 [0.796, 1.182] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 0.735 | 4 | 5 | d75a14c6 |
| loco | start_points | fixed:50 | rmse_h10 | persistence | 4.762 [3.862, 6.436] |  | 4.024 | 4 | 5 | a26a213d |
| loco | start_points | fixed:50 | rmse_h10 | rlinear | 2.978 [2.561, 3.742] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 2.548 | 4 | 5 | 78bc3e35 |
| loco | start_points | fixed:50 | rmse_h10 | transformer | 3.747 [1.637, 5.887] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 7.293 | 4 | 5 | 19b71fc1 |
| loco | start_points | fixed:50 | rmse_h100 | dlinear | 20.710 [17.702, 22.936] | 3/3 cells, 9/15 cell-seeds (vs persistence) |  | 3 | 5 | 5fb92db3 |
| loco | start_points | fixed:50 | rmse_h100 | elasticnet | 8.618 [2.733, 16.092] | 3/3 cells, 15/15 cell-seeds (vs persistence) |  | 3 | 5 | 0093ef69 |
| loco | start_points | fixed:50 | rmse_h100 | gru | 5.118 [3.819, 6.606] | 3/3 cells, 15/15 cell-seeds (vs persistence) |  | 3 | 5 | 095381df |
| loco | start_points | fixed:50 | rmse_h100 | itransformer | 11.901 [8.740, 15.885] | 3/3 cells, 15/15 cell-seeds (vs persistence) |  | 3 | 5 | 54867b77 |
| loco | start_points | fixed:50 | rmse_h100 | itransformer_sc | 4.986 [1.858, 9.954] | 3/3 cells, 15/15 cell-seeds (vs persistence) |  | 3 | 5 | fadffff4 |
| loco | start_points | fixed:50 | rmse_h100 | last_slope | 32.235 [15.395, 51.238] | 1/3 cells, 5/15 cell-seeds (vs persistence) |  | 3 | 5 | 1d016fee |
| loco | start_points | fixed:50 | rmse_h100 | lgbm | 4.264 [3.436, 5.788] | 3/3 cells, 15/15 cell-seeds (vs persistence) |  | 3 | 5 | 56599108 |
| loco | start_points | fixed:50 | rmse_h100 | lstm | 5.909 [2.935, 8.712] | 3/3 cells, 15/15 cell-seeds (vs persistence) |  | 3 | 5 | c7c5a204 |
| loco | start_points | fixed:50 | rmse_h100 | nlinear | 4.428 [3.169, 5.184] | 3/3 cells, 15/15 cell-seeds (vs persistence) |  | 3 | 5 | 9c4f0ee4 |
| loco | start_points | fixed:50 | rmse_h100 | patchtst | 6.186 [2.375, 10.034] | 3/3 cells, 14/15 cell-seeds (vs persistence) |  | 3 | 5 | 9a399b76 |
| loco | start_points | fixed:50 | rmse_h100 | persistence | 23.003 [19.038, 25.889] |  |  | 3 | 5 | 63dd8261 |
| loco | start_points | fixed:50 | rmse_h100 | rlinear | 9.186 [4.330, 15.418] | 3/3 cells, 15/15 cell-seeds (vs persistence) |  | 3 | 5 | 2ed486bd |
| loco | start_points | fixed:50 | rmse_h100 | transformer | 3.718 [2.007, 6.577] | 3/3 cells, 15/15 cell-seeds (vs persistence) |  | 3 | 5 | 6424b44c |
| loco | start_points | fixed:50 | rmse_h25 | dlinear | 6.116 [4.769, 8.045] | 4/4 cells, 16/20 cell-seeds (vs persistence) | 4.685 | 4 | 5 | 3b67b415 |
| loco | start_points | fixed:50 | rmse_h25 | elasticnet | 6.023 [1.382, 10.663] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 11.293 | 4 | 5 | e1ff5d55 |
| loco | start_points | fixed:50 | rmse_h25 | gru | 4.310 [2.550, 6.069] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 6.425 | 4 | 5 | 9731ae77 |
| loco | start_points | fixed:50 | rmse_h25 | itransformer | 3.230 [2.295, 4.001] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 1.886 | 4 | 5 | 9dedaedf |
| loco | start_points | fixed:50 | rmse_h25 | itransformer_sc | 4.226 [2.400, 5.951] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 4.823 | 4 | 5 | e5cc9a22 |
| loco | start_points | fixed:50 | rmse_h25 | last_slope | 14.547 [9.163, 19.931] | 1/4 cells, 5/20 cell-seeds (vs persistence) | 20.054 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | fixed:50 | rmse_h25 | lgbm | 4.108 [2.256, 6.491] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 1.888 | 4 | 5 | acedf5f4 |
| loco | start_points | fixed:50 | rmse_h25 | lstm | 4.630 [3.249, 6.167] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 5.026 | 4 | 5 | 5494788a |
| loco | start_points | fixed:50 | rmse_h25 | nlinear | 4.858 [2.635, 7.207] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 5.694 | 4 | 5 | b4ecdb12 |
| loco | start_points | fixed:50 | rmse_h25 | patchtst | 2.272 [1.217, 3.152] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 0.680 | 4 | 5 | d75a14c6 |
| loco | start_points | fixed:50 | rmse_h25 | persistence | 10.212 [8.506, 12.505] |  | 9.637 | 4 | 5 | a26a213d |
| loco | start_points | fixed:50 | rmse_h25 | rlinear | 7.076 [6.361, 7.783] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 6.788 | 4 | 5 | 78bc3e35 |
| loco | start_points | fixed:50 | rmse_h25 | transformer | 4.110 [2.566, 5.883] | 4/4 cells, 19/20 cell-seeds (vs persistence) | 6.563 | 4 | 5 | 19b71fc1 |
| loco | start_points | fixed:50 | rmse_h50 | dlinear | 15.283 [13.899, 16.232] | 1/4 cells, 11/20 cell-seeds (vs persistence) | 15.478 | 4 | 5 | 3b67b415 |
| loco | start_points | fixed:50 | rmse_h50 | elasticnet | 5.304 [2.815, 7.793] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 7.902 | 4 | 5 | e1ff5d55 |
| loco | start_points | fixed:50 | rmse_h50 | gru | 3.019 [1.877, 4.162] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 1.796 | 4 | 5 | 9731ae77 |
| loco | start_points | fixed:50 | rmse_h50 | itransformer | 5.312 [2.860, 7.621] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 5.328 | 4 | 5 | 9dedaedf |
| loco | start_points | fixed:50 | rmse_h50 | itransformer_sc | 4.897 [2.381, 6.697] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 6.943 | 4 | 5 | e5cc9a22 |
| loco | start_points | fixed:50 | rmse_h50 | last_slope | 23.648 [14.338, 32.958] | 1/4 cells, 5/20 cell-seeds (vs persistence) | 36.164 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | fixed:50 | rmse_h50 | lgbm | 3.577 [1.239, 5.362] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 4.954 | 4 | 5 | acedf5f4 |
| loco | start_points | fixed:50 | rmse_h50 | lstm | 2.922 [2.099, 3.557] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.738 | 4 | 5 | 5494788a |
| loco | start_points | fixed:50 | rmse_h50 | nlinear | 4.827 [2.331, 7.112] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 6.122 | 4 | 5 | b4ecdb12 |
| loco | start_points | fixed:50 | rmse_h50 | patchtst | 2.248 [1.423, 3.626] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 1.322 | 4 | 5 | d75a14c6 |
| loco | start_points | fixed:50 | rmse_h50 | persistence | 14.977 [12.995, 16.630] |  | 15.329 | 4 | 5 | a26a213d |
| loco | start_points | fixed:50 | rmse_h50 | rlinear | 10.543 [8.973, 12.093] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 12.237 | 4 | 5 | 78bc3e35 |
| loco | start_points | fixed:50 | rmse_h50 | transformer | 4.504 [3.241, 5.471] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 4.546 | 4 | 5 | 19b71fc1 |
| loco | start_points | frac:0.3 | rmse_h1 | dlinear | 3.475 [2.890, 4.060] | 0/4 cells, 1/20 cell-seeds (vs persistence) | 2.941 | 4 | 5 | 3b67b415 |
| loco | start_points | frac:0.3 | rmse_h1 | elasticnet | 0.323 [0.072, 0.601] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 0.772 | 4 | 5 | e1ff5d55 |
| loco | start_points | frac:0.3 | rmse_h1 | gru | 1.920 [0.869, 2.972] | 0/4 cells, 3/20 cell-seeds (vs persistence) | 2.526 | 4 | 5 | 9731ae77 |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer | 0.190 [0.081, 0.369] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 0.095 | 4 | 5 | 9dedaedf |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer_sc | 0.204 [0.073, 0.325] | 2/4 cells, 12/20 cell-seeds (vs persistence) | 0.233 | 4 | 5 | e5cc9a22 |
| loco | start_points | frac:0.3 | rmse_h1 | last_slope | 0.366 [0.145, 0.587] | 1/4 cells, 5/20 cell-seeds (vs persistence) | 0.263 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | frac:0.3 | rmse_h1 | lgbm | 0.184 [0.126, 0.243] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 0.132 | 4 | 5 | acedf5f4 |
| loco | start_points | frac:0.3 | rmse_h1 | lstm | 1.453 [1.356, 1.591] | 0/4 cells, 1/20 cell-seeds (vs persistence) | 1.412 | 4 | 5 | 5494788a |
| loco | start_points | frac:0.3 | rmse_h1 | nlinear | 0.107 [0.076, 0.130] | 3/4 cells, 14/20 cell-seeds (vs persistence) | 0.058 | 4 | 5 | b4ecdb12 |
| loco | start_points | frac:0.3 | rmse_h1 | patchtst | 0.130 [0.048, 0.212] | 3/4 cells, 14/20 cell-seeds (vs persistence) | 0.159 | 4 | 5 | d75a14c6 |
| loco | start_points | frac:0.3 | rmse_h1 | persistence | 0.262 [0.062, 0.494] |  | 0.216 | 4 | 5 | a26a213d |
| loco | start_points | frac:0.3 | rmse_h1 | rlinear | 0.191 [0.090, 0.313] | 3/4 cells, 12/20 cell-seeds (vs persistence) | 0.058 | 4 | 5 | 78bc3e35 |
| loco | start_points | frac:0.3 | rmse_h1 | transformer | 1.877 [0.945, 2.834] | 0/4 cells, 2/20 cell-seeds (vs persistence) | 2.029 | 4 | 5 | 19b71fc1 |
| loco | start_points | frac:0.3 | rmse_h10 | dlinear | 5.959 [5.075, 6.869] | 0/4 cells, 0/20 cell-seeds (vs persistence) | 7.230 | 4 | 5 | 3b67b415 |
| loco | start_points | frac:0.3 | rmse_h10 | elasticnet | 2.059 [0.360, 3.976] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 5.115 | 4 | 5 | e1ff5d55 |
| loco | start_points | frac:0.3 | rmse_h10 | gru | 2.608 [1.063, 4.233] | 1/4 cells, 8/20 cell-seeds (vs persistence) | 3.097 | 4 | 5 | 9731ae77 |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer | 1.620 [0.592, 2.778] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 0.404 | 4 | 5 | 9dedaedf |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer_sc | 1.531 [1.063, 1.998] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 0.856 | 4 | 5 | e5cc9a22 |
| loco | start_points | frac:0.3 | rmse_h10 | last_slope | 3.289 [2.078, 4.500] | 1/4 cells, 5/20 cell-seeds (vs persistence) | 2.289 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | frac:0.3 | rmse_h10 | lgbm | 1.091 [0.635, 1.556] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 0.471 | 4 | 5 | acedf5f4 |
| loco | start_points | frac:0.3 | rmse_h10 | lstm | 2.930 [2.385, 3.452] | 1/4 cells, 7/20 cell-seeds (vs persistence) | 3.191 | 4 | 5 | 5494788a |
| loco | start_points | frac:0.3 | rmse_h10 | nlinear | 1.408 [1.060, 1.756] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 0.833 | 4 | 5 | b4ecdb12 |
| loco | start_points | frac:0.3 | rmse_h10 | patchtst | 1.301 [0.481, 2.157] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 0.154 | 4 | 5 | d75a14c6 |
| loco | start_points | frac:0.3 | rmse_h10 | persistence | 1.776 [0.447, 3.105] |  | 2.497 | 4 | 5 | a26a213d |
| loco | start_points | frac:0.3 | rmse_h10 | rlinear | 1.512 [0.516, 2.540] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 0.946 | 4 | 5 | 78bc3e35 |
| loco | start_points | frac:0.3 | rmse_h10 | transformer | 3.348 [1.928, 5.036] | 1/4 cells, 7/20 cell-seeds (vs persistence) | 5.760 | 4 | 5 | 19b71fc1 |
| loco | start_points | frac:0.3 | rmse_h100 | dlinear | 19.388 [15.443, 23.438] | 3/4 cells, 12/20 cell-seeds (vs persistence) | 13.531 | 4 | 5 | 3b67b415 |
| loco | start_points | frac:0.3 | rmse_h100 | elasticnet | 7.582 [2.861, 13.998] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 2.343 | 4 | 5 | e1ff5d55 |
| loco | start_points | frac:0.3 | rmse_h100 | gru | 3.739 [1.688, 5.962] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 1.482 | 4 | 5 | 9731ae77 |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer | 13.297 [7.506, 19.324] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 5.228 | 4 | 5 | 9dedaedf |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer_sc | 9.140 [4.654, 14.982] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 7.345 | 4 | 5 | e5cc9a22 |
| loco | start_points | frac:0.3 | rmse_h100 | last_slope | 23.144 [10.125, 30.488] | 1/4 cells, 5/20 cell-seeds (vs persistence) | 30.580 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | frac:0.3 | rmse_h100 | lgbm | 4.630 [4.341, 5.110] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 4.386 | 4 | 5 | acedf5f4 |
| loco | start_points | frac:0.3 | rmse_h100 | lstm | 4.377 [2.611, 6.143] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 2.777 | 4 | 5 | 5494788a |
| loco | start_points | frac:0.3 | rmse_h100 | nlinear | 5.460 [3.770, 7.496] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 4.692 | 4 | 5 | b4ecdb12 |
| loco | start_points | frac:0.3 | rmse_h100 | patchtst | 8.457 [1.873, 15.040] | 4/4 cells, 18/20 cell-seeds (vs persistence) | 17.208 | 4 | 5 | d75a14c6 |
| loco | start_points | frac:0.3 | rmse_h100 | persistence | 21.592 [17.906, 25.277] |  | 17.279 | 4 | 5 | a26a213d |
| loco | start_points | frac:0.3 | rmse_h100 | rlinear | 13.181 [8.599, 20.724] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 10.792 | 4 | 5 | 78bc3e35 |
| loco | start_points | frac:0.3 | rmse_h100 | transformer | 6.061 [2.896, 9.227] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 4.148 | 4 | 5 | 19b71fc1 |
| loco | start_points | frac:0.3 | rmse_h25 | dlinear | 4.047 [3.135, 4.783] | 3/4 cells, 12/20 cell-seeds (vs persistence) | 4.662 | 4 | 5 | 3b67b415 |
| loco | start_points | frac:0.3 | rmse_h25 | elasticnet | 2.417 [1.740, 3.118] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 1.999 | 4 | 5 | e1ff5d55 |
| loco | start_points | frac:0.3 | rmse_h25 | gru | 3.343 [1.831, 4.855] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 1.829 | 4 | 5 | 9731ae77 |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer | 3.566 [2.302, 4.919] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 5.430 | 4 | 5 | 9dedaedf |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer_sc | 3.368 [1.266, 6.341] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 7.812 | 4 | 5 | e5cc9a22 |
| loco | start_points | frac:0.3 | rmse_h25 | last_slope | 6.727 [2.243, 10.150] | 1/4 cells, 5/20 cell-seeds (vs persistence) | 11.114 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | frac:0.3 | rmse_h25 | lgbm | 2.256 [0.609, 4.601] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 5.733 | 4 | 5 | acedf5f4 |
| loco | start_points | frac:0.3 | rmse_h25 | lstm | 4.920 [3.298, 6.542] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 2.373 | 4 | 5 | 5494788a |
| loco | start_points | frac:0.3 | rmse_h25 | nlinear | 1.725 [0.331, 4.141] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 5.319 | 4 | 5 | b4ecdb12 |
| loco | start_points | frac:0.3 | rmse_h25 | patchtst | 3.560 [1.580, 6.991] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 8.633 | 4 | 5 | d75a14c6 |
| loco | start_points | frac:0.3 | rmse_h25 | persistence | 4.666 [2.061, 6.293] |  | 0.850 | 4 | 5 | a26a213d |
| loco | start_points | frac:0.3 | rmse_h25 | rlinear | 3.962 [1.709, 5.650] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 5.168 | 4 | 5 | 78bc3e35 |
| loco | start_points | frac:0.3 | rmse_h25 | transformer | 4.446 [2.743, 6.149] | 1/4 cells, 10/20 cell-seeds (vs persistence) | 2.223 | 4 | 5 | 19b71fc1 |
| loco | start_points | frac:0.3 | rmse_h50 | dlinear | 14.324 [12.205, 16.482] | 1/4 cells, 5/20 cell-seeds (vs last_slope) | 11.395 | 4 | 5 | 3b67b415 |
| loco | start_points | frac:0.3 | rmse_h50 | elasticnet | 3.998 [2.050, 5.506] | 3/4 cells, 15/20 cell-seeds (vs last_slope) | 5.753 | 4 | 5 | e1ff5d55 |
| loco | start_points | frac:0.3 | rmse_h50 | gru | 3.031 [1.627, 4.435] | 3/4 cells, 14/20 cell-seeds (vs last_slope) | 1.658 | 4 | 5 | 9731ae77 |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer | 6.765 [3.543, 9.987] | 3/4 cells, 15/20 cell-seeds (vs last_slope) | 2.351 | 4 | 5 | 9dedaedf |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer_sc | 5.268 [2.884, 8.328] | 3/4 cells, 15/20 cell-seeds (vs last_slope) | 4.081 | 4 | 5 | e5cc9a22 |
| loco | start_points | frac:0.3 | rmse_h50 | last_slope | 10.464 [3.890, 15.179] |  | 12.503 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | frac:0.3 | rmse_h50 | lgbm | 2.434 [0.671, 4.348] | 4/4 cells, 20/20 cell-seeds (vs last_slope) | 1.101 | 4 | 5 | acedf5f4 |
| loco | start_points | frac:0.3 | rmse_h50 | lstm | 2.620 [1.469, 3.542] | 3/4 cells, 15/20 cell-seeds (vs last_slope) | 2.718 | 4 | 5 | 5494788a |
| loco | start_points | frac:0.3 | rmse_h50 | nlinear | 2.751 [0.795, 4.707] | 3/4 cells, 17/20 cell-seeds (vs last_slope) | 0.493 | 4 | 5 | b4ecdb12 |
| loco | start_points | frac:0.3 | rmse_h50 | patchtst | 4.986 [1.516, 8.457] | 3/4 cells, 15/20 cell-seeds (vs last_slope) | 9.318 | 4 | 5 | d75a14c6 |
| loco | start_points | frac:0.3 | rmse_h50 | persistence | 13.452 [11.698, 15.205] | 2/4 cells, 10/20 cell-seeds (vs last_slope) | 11.427 | 4 | 5 | a26a213d |
| loco | start_points | frac:0.3 | rmse_h50 | rlinear | 6.759 [2.367, 11.630] | 3/4 cells, 15/20 cell-seeds (vs last_slope) | 0.490 | 4 | 5 | 78bc3e35 |
| loco | start_points | frac:0.3 | rmse_h50 | transformer | 4.540 [2.825, 6.879] | 3/4 cells, 15/20 cell-seeds (vs last_slope) | 3.675 | 4 | 5 | 19b71fc1 |
| loco | start_points | frac:0.5 | rmse_h1 | dlinear | 3.711 [3.199, 4.086] | 0/4 cells, 6/20 cell-seeds (vs persistence) | 4.165 | 4 | 5 | 3b67b415 |
| loco | start_points | frac:0.5 | rmse_h1 | elasticnet | 1.669 [0.197, 3.142] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 2.995 | 4 | 5 | e1ff5d55 |
| loco | start_points | frac:0.5 | rmse_h1 | gru | 2.146 [1.386, 3.142] | 1/4 cells, 8/20 cell-seeds (vs persistence) | 1.354 | 4 | 5 | 9731ae77 |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer | 2.090 [0.295, 3.885] | 1/4 cells, 5/20 cell-seeds (vs persistence) | 3.844 | 4 | 5 | 9dedaedf |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer_sc | 2.114 [0.333, 3.894] | 1/4 cells, 5/20 cell-seeds (vs persistence) | 3.921 | 4 | 5 | e5cc9a22 |
| loco | start_points | frac:0.5 | rmse_h1 | last_slope | 2.119 [0.305, 3.934] | 1/4 cells, 5/20 cell-seeds (vs persistence) | 3.857 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | frac:0.5 | rmse_h1 | lgbm | 2.030 [0.272, 3.787] | 1/4 cells, 5/20 cell-seeds (vs persistence) | 3.779 | 4 | 5 | acedf5f4 |
| loco | start_points | frac:0.5 | rmse_h1 | lstm | 1.651 [1.091, 2.242] | 2/4 cells, 9/20 cell-seeds (vs persistence) | 1.841 | 4 | 5 | 5494788a |
| loco | start_points | frac:0.5 | rmse_h1 | nlinear | 1.988 [0.233, 3.743] | 1/4 cells, 5/20 cell-seeds (vs persistence) | 3.705 | 4 | 5 | b4ecdb12 |
| loco | start_points | frac:0.5 | rmse_h1 | patchtst | 1.987 [0.112, 3.861] | 1/4 cells, 5/20 cell-seeds (vs persistence) | 3.740 | 4 | 5 | d75a14c6 |
| loco | start_points | frac:0.5 | rmse_h1 | persistence | 1.752 [0.144, 3.360] |  | 3.372 | 4 | 5 | a26a213d |
| loco | start_points | frac:0.5 | rmse_h1 | rlinear | 1.993 [0.230, 3.755] | 1/4 cells, 6/20 cell-seeds (vs persistence) | 3.726 | 4 | 5 | 78bc3e35 |
| loco | start_points | frac:0.5 | rmse_h1 | transformer | 2.796 [1.001, 4.929] | 1/4 cells, 3/20 cell-seeds (vs persistence) | 6.149 | 4 | 5 | 19b71fc1 |
| loco | start_points | frac:0.5 | rmse_h10 | dlinear | 7.402 [6.662, 8.215] | 1/4 cells, 3/20 cell-seeds (vs last_slope) | 6.337 | 4 | 5 | 3b67b415 |
| loco | start_points | frac:0.5 | rmse_h10 | elasticnet | 2.003 [0.989, 3.332] | 3/4 cells, 15/20 cell-seeds (vs last_slope) | 1.882 | 4 | 5 | e1ff5d55 |
| loco | start_points | frac:0.5 | rmse_h10 | gru | 2.789 [1.092, 4.486] | 2/4 cells, 12/20 cell-seeds (vs last_slope) | 4.299 | 4 | 5 | 9731ae77 |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer | 2.364 [0.462, 5.765] | 4/4 cells, 19/20 cell-seeds (vs last_slope) | 7.497 | 4 | 5 | 9dedaedf |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer_sc | 2.675 [0.925, 5.618] | 3/4 cells, 17/20 cell-seeds (vs last_slope) | 7.036 | 4 | 5 | e5cc9a22 |
| loco | start_points | frac:0.5 | rmse_h10 | last_slope | 3.570 [1.260, 6.697] |  | 8.321 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | frac:0.5 | rmse_h10 | lgbm | 2.473 [0.835, 4.736] | 3/4 cells, 15/20 cell-seeds (vs last_slope) | 5.873 | 4 | 5 | acedf5f4 |
| loco | start_points | frac:0.5 | rmse_h10 | lstm | 2.703 [1.071, 4.335] | 2/4 cells, 13/20 cell-seeds (vs last_slope) | 3.755 | 4 | 5 | 5494788a |
| loco | start_points | frac:0.5 | rmse_h10 | nlinear | 2.970 [1.268, 5.050] | 3/4 cells, 13/20 cell-seeds (vs last_slope) | 6.076 | 4 | 5 | b4ecdb12 |
| loco | start_points | frac:0.5 | rmse_h10 | patchtst | 2.483 [0.727, 5.624] | 3/4 cells, 17/20 cell-seeds (vs last_slope) | 7.230 | 4 | 5 | d75a14c6 |
| loco | start_points | frac:0.5 | rmse_h10 | persistence | 3.664 [2.972, 4.463] | 1/4 cells, 5/20 cell-seeds (vs last_slope) | 3.465 | 4 | 5 | a26a213d |
| loco | start_points | frac:0.5 | rmse_h10 | rlinear | 3.663 [1.821, 5.773] | 2/4 cells, 9/20 cell-seeds (vs last_slope) | 6.623 | 4 | 5 | 78bc3e35 |
| loco | start_points | frac:0.5 | rmse_h10 | transformer | 2.755 [1.921, 3.659] | 2/4 cells, 12/20 cell-seeds (vs last_slope) | 4.125 | 4 | 5 | 19b71fc1 |
| loco | start_points | frac:0.5 | rmse_h100 | dlinear | 18.599 [12.275, 22.821] | 3/3 cells, 9/15 cell-seeds (vs persistence) |  | 3 | 5 | 5fb92db3 |
| loco | start_points | frac:0.5 | rmse_h100 | elasticnet | 8.948 [2.639, 16.849] | 3/3 cells, 15/15 cell-seeds (vs persistence) |  | 3 | 5 | 0093ef69 |
| loco | start_points | frac:0.5 | rmse_h100 | gru | 4.201 [2.771, 6.464] | 3/3 cells, 15/15 cell-seeds (vs persistence) |  | 3 | 5 | 095381df |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer | 10.443 [4.834, 13.987] | 3/3 cells, 15/15 cell-seeds (vs persistence) |  | 3 | 5 | 54867b77 |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer_sc | 5.805 [3.227, 8.041] | 3/3 cells, 15/15 cell-seeds (vs persistence) |  | 3 | 5 | fadffff4 |
| loco | start_points | frac:0.5 | rmse_h100 | last_slope | 26.098 [18.310, 39.660] | 1/3 cells, 5/15 cell-seeds (vs persistence) |  | 3 | 5 | 1d016fee |
| loco | start_points | frac:0.5 | rmse_h100 | lgbm | 4.744 [2.104, 6.328] | 3/3 cells, 15/15 cell-seeds (vs persistence) |  | 3 | 5 | 56599108 |
| loco | start_points | frac:0.5 | rmse_h100 | lstm | 4.687 [2.194, 6.606] | 3/3 cells, 15/15 cell-seeds (vs persistence) |  | 3 | 5 | c7c5a204 |
| loco | start_points | frac:0.5 | rmse_h100 | nlinear | 5.439 [3.227, 6.782] | 3/3 cells, 15/15 cell-seeds (vs persistence) |  | 3 | 5 | 9c4f0ee4 |
| loco | start_points | frac:0.5 | rmse_h100 | patchtst | 5.599 [0.834, 10.733] | 3/3 cells, 15/15 cell-seeds (vs persistence) |  | 3 | 5 | 9a399b76 |
| loco | start_points | frac:0.5 | rmse_h100 | persistence | 21.687 [16.103, 26.550] |  |  | 3 | 5 | 63dd8261 |
| loco | start_points | frac:0.5 | rmse_h100 | rlinear | 5.919 [1.189, 10.556] | 3/3 cells, 15/15 cell-seeds (vs persistence) |  | 3 | 5 | 2ed486bd |
| loco | start_points | frac:0.5 | rmse_h100 | transformer | 5.702 [1.323, 8.922] | 3/3 cells, 15/15 cell-seeds (vs persistence) |  | 3 | 5 | 6424b44c |
| loco | start_points | frac:0.5 | rmse_h25 | dlinear | 3.185 [1.967, 4.172] | 3/4 cells, 15/20 cell-seeds (vs last_slope) | 1.285 | 4 | 5 | 3b67b415 |
| loco | start_points | frac:0.5 | rmse_h25 | elasticnet | 3.802 [1.352, 6.253] | 4/4 cells, 20/20 cell-seeds (vs last_slope) | 5.310 | 4 | 5 | e1ff5d55 |
| loco | start_points | frac:0.5 | rmse_h25 | gru | 2.443 [1.662, 3.440] | 3/4 cells, 19/20 cell-seeds (vs last_slope) | 1.773 | 4 | 5 | 9731ae77 |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer | 2.036 [0.532, 3.541] | 4/4 cells, 20/20 cell-seeds (vs last_slope) | 4.311 | 4 | 5 | 9dedaedf |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer_sc | 2.430 [1.634, 3.435] | 4/4 cells, 20/20 cell-seeds (vs last_slope) | 4.030 | 4 | 5 | e5cc9a22 |
| loco | start_points | frac:0.5 | rmse_h25 | last_slope | 6.441 [3.728, 8.000] |  | 8.129 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | frac:0.5 | rmse_h25 | lgbm | 2.169 [0.782, 3.077] | 4/4 cells, 20/20 cell-seeds (vs last_slope) | 2.934 | 4 | 5 | acedf5f4 |
| loco | start_points | frac:0.5 | rmse_h25 | lstm | 3.485 [2.066, 5.712] | 4/4 cells, 18/20 cell-seeds (vs last_slope) | 2.693 | 4 | 5 | 5494788a |
| loco | start_points | frac:0.5 | rmse_h25 | nlinear | 2.331 [0.893, 3.860] | 4/4 cells, 20/20 cell-seeds (vs last_slope) | 2.229 | 4 | 5 | b4ecdb12 |
| loco | start_points | frac:0.5 | rmse_h25 | patchtst | 2.446 [1.579, 3.366] | 4/4 cells, 20/20 cell-seeds (vs last_slope) | 3.841 | 4 | 5 | d75a14c6 |
| loco | start_points | frac:0.5 | rmse_h25 | persistence | 6.722 [4.992, 8.310] | 1/4 cells, 5/20 cell-seeds (vs last_slope) | 4.010 | 4 | 5 | a26a213d |
| loco | start_points | frac:0.5 | rmse_h25 | rlinear | 4.204 [2.765, 5.462] | 4/4 cells, 19/20 cell-seeds (vs last_slope) | 3.988 | 4 | 5 | 78bc3e35 |
| loco | start_points | frac:0.5 | rmse_h25 | transformer | 2.807 [1.945, 3.670] | 3/4 cells, 16/20 cell-seeds (vs last_slope) | 3.334 | 4 | 5 | 19b71fc1 |
| loco | start_points | frac:0.5 | rmse_h50 | dlinear | 12.507 [8.839, 16.174] | 1/4 cells, 10/20 cell-seeds (vs last_slope) | 8.216 | 4 | 5 | 3b67b415 |
| loco | start_points | frac:0.5 | rmse_h50 | elasticnet | 5.555 [2.585, 9.675] | 4/4 cells, 20/20 cell-seeds (vs last_slope) | 5.207 | 4 | 5 | e1ff5d55 |
| loco | start_points | frac:0.5 | rmse_h50 | gru | 3.767 [1.615, 6.172] | 4/4 cells, 20/20 cell-seeds (vs last_slope) | 1.874 | 4 | 5 | 9731ae77 |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer | 4.095 [1.576, 6.614] | 4/4 cells, 20/20 cell-seeds (vs last_slope) | 2.354 | 4 | 5 | 9dedaedf |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer_sc | 4.290 [3.821, 4.800] | 4/4 cells, 20/20 cell-seeds (vs last_slope) | 3.793 | 4 | 5 | e5cc9a22 |
| loco | start_points | frac:0.5 | rmse_h50 | last_slope | 12.312 [9.073, 14.516] |  | 14.191 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | frac:0.5 | rmse_h50 | lgbm | 2.879 [0.624, 5.685] | 4/4 cells, 20/20 cell-seeds (vs last_slope) | 0.037 | 4 | 5 | acedf5f4 |
| loco | start_points | frac:0.5 | rmse_h50 | lstm | 3.456 [1.394, 6.413] | 4/4 cells, 20/20 cell-seeds (vs last_slope) | 1.946 | 4 | 5 | 5494788a |
| loco | start_points | frac:0.5 | rmse_h50 | nlinear | 3.316 [1.329, 6.005] | 4/4 cells, 20/20 cell-seeds (vs last_slope) | 0.833 | 4 | 5 | b4ecdb12 |
| loco | start_points | frac:0.5 | rmse_h50 | patchtst | 2.549 [1.459, 3.587] | 4/4 cells, 20/20 cell-seeds (vs last_slope) | 3.482 | 4 | 5 | d75a14c6 |
| loco | start_points | frac:0.5 | rmse_h50 | persistence | 13.020 [9.963, 16.219] | 1/4 cells, 5/20 cell-seeds (vs last_slope) | 10.087 | 4 | 5 | a26a213d |
| loco | start_points | frac:0.5 | rmse_h50 | rlinear | 5.377 [2.289, 8.465] | 4/4 cells, 20/20 cell-seeds (vs last_slope) | 3.192 | 4 | 5 | 78bc3e35 |
| loco | start_points | frac:0.5 | rmse_h50 | transformer | 5.328 [3.293, 7.570] | 4/4 cells, 19/20 cell-seeds (vs last_slope) | 4.627 | 4 | 5 | 19b71fc1 |
| loco | start_points | frac:0.7 | rmse_h1 | dlinear | 3.326 [2.723, 4.226] | 0/4 cells, 7/20 cell-seeds (vs persistence) | 4.654 | 4 | 5 | 3b67b415 |
| loco | start_points | frac:0.7 | rmse_h1 | elasticnet | 0.994 [0.198, 2.352] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.051 | 4 | 5 | e1ff5d55 |
| loco | start_points | frac:0.7 | rmse_h1 | gru | 1.509 [1.224, 1.736] | 1/4 cells, 6/20 cell-seeds (vs persistence) | 1.751 | 4 | 5 | 9731ae77 |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer | 1.299 [0.150, 3.154] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 4.142 | 4 | 5 | 9dedaedf |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer_sc | 1.350 [0.255, 2.987] | 1/4 cells, 6/20 cell-seeds (vs persistence) | 3.886 | 4 | 5 | e5cc9a22 |
| loco | start_points | frac:0.7 | rmse_h1 | last_slope | 1.460 [0.161, 3.389] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 4.434 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | frac:0.7 | rmse_h1 | lgbm | 1.315 [0.183, 3.065] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 4.007 | 4 | 5 | acedf5f4 |
| loco | start_points | frac:0.7 | rmse_h1 | lstm | 1.121 [0.562, 1.604] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 1.677 | 4 | 5 | 5494788a |
| loco | start_points | frac:0.7 | rmse_h1 | nlinear | 1.295 [0.201, 2.882] | 2/4 cells, 12/20 cell-seeds (vs persistence) | 3.753 | 4 | 5 | b4ecdb12 |
| loco | start_points | frac:0.7 | rmse_h1 | patchtst | 1.433 [0.313, 3.177] | 2/4 cells, 8/20 cell-seeds (vs persistence) | 4.083 | 4 | 5 | d75a14c6 |
| loco | start_points | frac:0.7 | rmse_h1 | persistence | 1.282 [0.357, 2.907] |  | 3.690 | 4 | 5 | a26a213d |
| loco | start_points | frac:0.7 | rmse_h1 | rlinear | 1.248 [0.195, 2.803] | 3/4 cells, 12/20 cell-seeds (vs persistence) | 3.667 | 4 | 5 | 78bc3e35 |
| loco | start_points | frac:0.7 | rmse_h1 | transformer | 3.071 [1.456, 5.665] | 0/4 cells, 4/20 cell-seeds (vs persistence) | 6.930 | 4 | 5 | 19b71fc1 |
| loco | start_points | frac:0.7 | rmse_h10 | dlinear | 6.854 [6.100, 7.608] | 0/4 cells, 2/20 cell-seeds (vs last_slope) | 7.816 | 4 | 5 | 3b67b415 |
| loco | start_points | frac:0.7 | rmse_h10 | elasticnet | 2.743 [1.175, 4.847] | 2/4 cells, 10/20 cell-seeds (vs last_slope) | 5.843 | 4 | 5 | e1ff5d55 |
| loco | start_points | frac:0.7 | rmse_h10 | gru | 1.967 [1.386, 2.448] | 2/4 cells, 11/20 cell-seeds (vs last_slope) | 2.007 | 4 | 5 | 9731ae77 |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer | 0.855 [0.448, 1.263] | 3/4 cells, 15/20 cell-seeds (vs last_slope) | 0.481 | 4 | 5 | 9dedaedf |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer_sc | 1.102 [0.297, 1.907] | 3/4 cells, 15/20 cell-seeds (vs last_slope) | 1.871 | 4 | 5 | e5cc9a22 |
| loco | start_points | frac:0.7 | rmse_h10 | last_slope | 2.002 [0.811, 3.192] |  | 3.435 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | frac:0.7 | rmse_h10 | lgbm | 0.930 [0.543, 1.317] | 3/4 cells, 15/20 cell-seeds (vs last_slope) | 1.510 | 4 | 5 | acedf5f4 |
| loco | start_points | frac:0.7 | rmse_h10 | lstm | 2.125 [1.283, 2.894] | 2/4 cells, 8/20 cell-seeds (vs last_slope) | 3.158 | 4 | 5 | 5494788a |
| loco | start_points | frac:0.7 | rmse_h10 | nlinear | 1.192 [0.424, 2.297] | 3/4 cells, 16/20 cell-seeds (vs last_slope) | 2.891 | 4 | 5 | b4ecdb12 |
| loco | start_points | frac:0.7 | rmse_h10 | patchtst | 0.769 [0.304, 1.234] | 3/4 cells, 15/20 cell-seeds (vs last_slope) | 0.362 | 4 | 5 | d75a14c6 |
| loco | start_points | frac:0.7 | rmse_h10 | persistence | 2.565 [1.535, 3.576] | 1/4 cells, 5/20 cell-seeds (vs last_slope) | 3.998 | 4 | 5 | a26a213d |
| loco | start_points | frac:0.7 | rmse_h10 | rlinear | 1.293 [0.624, 2.220] | 3/4 cells, 16/20 cell-seeds (vs last_slope) | 2.667 | 4 | 5 | 78bc3e35 |
| loco | start_points | frac:0.7 | rmse_h10 | transformer | 3.429 [1.930, 6.194] | 1/4 cells, 8/20 cell-seeds (vs last_slope) | 7.602 | 4 | 5 | 19b71fc1 |
| loco | start_points | frac:0.7 | rmse_h100 | dlinear | 18.404 | 1/1 cells, 3/5 cell-seeds (vs persistence) |  | 1 | 5 | 5862b326 |
| loco | start_points | frac:0.7 | rmse_h100 | elasticnet | 16.308 | 1/1 cells, 5/5 cell-seeds (vs persistence) |  | 1 | 5 | 33dfd99f |
| loco | start_points | frac:0.7 | rmse_h100 | gru | 5.678 | 1/1 cells, 5/5 cell-seeds (vs persistence) |  | 1 | 5 | 5126a869 |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer | 12.000 | 1/1 cells, 5/5 cell-seeds (vs persistence) |  | 1 | 5 | 2d385949 |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer_sc | 5.039 | 1/1 cells, 5/5 cell-seeds (vs persistence) |  | 1 | 5 | e373e8dd |
| loco | start_points | frac:0.7 | rmse_h100 | last_slope | 28.756 | 0/1 cells, 0/5 cell-seeds (vs persistence) |  | 1 | 5 | 5e8799fa |
| loco | start_points | frac:0.7 | rmse_h100 | lgbm | 3.836 | 1/1 cells, 5/5 cell-seeds (vs persistence) |  | 1 | 5 | 2f14e1b6 |
| loco | start_points | frac:0.7 | rmse_h100 | lstm | 6.297 | 1/1 cells, 5/5 cell-seeds (vs persistence) |  | 1 | 5 | 7e5fd4a7 |
| loco | start_points | frac:0.7 | rmse_h100 | nlinear | 2.953 | 1/1 cells, 5/5 cell-seeds (vs persistence) |  | 1 | 5 | a0c56d51 |
| loco | start_points | frac:0.7 | rmse_h100 | patchtst | 5.667 | 1/1 cells, 5/5 cell-seeds (vs persistence) |  | 1 | 5 | fdd94a94 |
| loco | start_points | frac:0.7 | rmse_h100 | persistence | 23.823 |  |  | 1 | 5 | c903ee1c |
| loco | start_points | frac:0.7 | rmse_h100 | rlinear | 18.984 | 1/1 cells, 5/5 cell-seeds (vs persistence) |  | 1 | 5 | 8748118b |
| loco | start_points | frac:0.7 | rmse_h100 | transformer | 3.327 | 1/1 cells, 5/5 cell-seeds (vs persistence) |  | 1 | 5 | 4f3dc93f |
| loco | start_points | frac:0.7 | rmse_h25 | dlinear | 3.550 [2.242, 5.094] | 2/4 cells, 11/20 cell-seeds (vs last_slope) | 3.698 | 4 | 5 | 3b67b415 |
| loco | start_points | frac:0.7 | rmse_h25 | elasticnet | 6.399 [2.537, 10.261] | 0/4 cells, 0/20 cell-seeds (vs last_slope) | 10.123 | 4 | 5 | e1ff5d55 |
| loco | start_points | frac:0.7 | rmse_h25 | gru | 3.649 [1.536, 5.761] | 2/4 cells, 13/20 cell-seeds (vs last_slope) | 5.300 | 4 | 5 | 9731ae77 |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer | 2.489 [0.803, 4.639] | 2/4 cells, 11/20 cell-seeds (vs last_slope) | 2.030 | 4 | 5 | 9dedaedf |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer_sc | 3.186 [1.212, 4.899] | 2/4 cells, 10/20 cell-seeds (vs last_slope) | 4.053 | 4 | 5 | e5cc9a22 |
| loco | start_points | frac:0.7 | rmse_h25 | last_slope | 4.359 [2.028, 8.175] |  | 10.004 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | frac:0.7 | rmse_h25 | lgbm | 3.076 [1.627, 4.733] | 2/4 cells, 10/20 cell-seeds (vs last_slope) | 3.472 | 4 | 5 | acedf5f4 |
| loco | start_points | frac:0.7 | rmse_h25 | lstm | 4.417 [1.563, 7.271] | 2/4 cells, 12/20 cell-seeds (vs last_slope) | 6.102 | 4 | 5 | 5494788a |
| loco | start_points | frac:0.7 | rmse_h25 | nlinear | 3.077 [1.153, 5.002] | 3/4 cells, 15/20 cell-seeds (vs last_slope) | 4.586 | 4 | 5 | b4ecdb12 |
| loco | start_points | frac:0.7 | rmse_h25 | patchtst | 1.801 [0.909, 2.692] | 4/4 cells, 16/20 cell-seeds (vs last_slope) | 0.674 | 4 | 5 | d75a14c6 |
| loco | start_points | frac:0.7 | rmse_h25 | persistence | 7.057 [4.781, 9.333] | 1/4 cells, 5/20 cell-seeds (vs last_slope) | 8.579 | 4 | 5 | a26a213d |
| loco | start_points | frac:0.7 | rmse_h25 | rlinear | 2.625 [0.933, 4.316] | 3/4 cells, 15/20 cell-seeds (vs last_slope) | 4.721 | 4 | 5 | 78bc3e35 |
| loco | start_points | frac:0.7 | rmse_h25 | transformer | 4.045 [2.381, 5.020] | 2/4 cells, 9/20 cell-seeds (vs last_slope) | 5.156 | 4 | 5 | 19b71fc1 |
| loco | start_points | frac:0.7 | rmse_h50 | dlinear | 9.372 [6.655, 11.329] | 4/4 cells, 15/20 cell-seeds (vs persistence) | 11.898 | 4 | 5 | 3b67b415 |
| loco | start_points | frac:0.7 | rmse_h50 | elasticnet | 5.936 [3.745, 8.128] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 9.166 | 4 | 5 | e1ff5d55 |
| loco | start_points | frac:0.7 | rmse_h50 | gru | 3.302 [2.304, 4.186] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.083 | 4 | 5 | 9731ae77 |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer | 2.429 [1.204, 3.578] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.952 | 4 | 5 | 9dedaedf |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer_sc | 3.161 [1.647, 4.675] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 5.289 | 4 | 5 | e5cc9a22 |
| loco | start_points | frac:0.7 | rmse_h50 | last_slope | 11.921 [5.216, 19.355] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 23.634 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | frac:0.7 | rmse_h50 | lgbm | 2.827 [1.960, 3.693] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.447 | 4 | 5 | acedf5f4 |
| loco | start_points | frac:0.7 | rmse_h50 | lstm | 2.814 [2.137, 3.850] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 4.370 | 4 | 5 | 5494788a |
| loco | start_points | frac:0.7 | rmse_h50 | nlinear | 3.227 [1.327, 4.495] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 4.799 | 4 | 5 | b4ecdb12 |
| loco | start_points | frac:0.7 | rmse_h50 | patchtst | 2.190 [1.193, 3.187] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 2.666 | 4 | 5 | d75a14c6 |
| loco | start_points | frac:0.7 | rmse_h50 | persistence | 10.912 [8.091, 13.103] |  | 13.532 | 4 | 5 | a26a213d |
| loco | start_points | frac:0.7 | rmse_h50 | rlinear | 2.346 [0.482, 4.263] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 5.481 | 4 | 5 | 78bc3e35 |
| loco | start_points | frac:0.7 | rmse_h50 | transformer | 4.570 [2.992, 6.148] | 4/4 cells, 17/20 cell-seeds (vs persistence) | 5.837 | 4 | 5 | 19b71fc1 |
| loco | start_points | overall | rmse_h1 | dlinear | 4.010 [3.844, 4.176] | 0/4 cells, 2/20 cell-seeds (vs persistence) | 4.110 | 4 | 5 | 3b67b415 |
| loco | start_points | overall | rmse_h1 | elasticnet | 1.664 [1.265, 2.040] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 1.966 | 4 | 5 | e1ff5d55 |
| loco | start_points | overall | rmse_h1 | gru | 2.323 [1.714, 2.949] | 0/4 cells, 2/20 cell-seeds (vs persistence) | 2.503 | 4 | 5 | 9731ae77 |
| loco | start_points | overall | rmse_h1 | itransformer | 1.820 [1.085, 2.555] | 0/4 cells, 2/20 cell-seeds (vs persistence) | 2.576 | 4 | 5 | 9dedaedf |
| loco | start_points | overall | rmse_h1 | itransformer_sc | 1.809 [1.109, 2.509] | 0/4 cells, 0/20 cell-seeds (vs persistence) | 2.492 | 4 | 5 | e5cc9a22 |
| loco | start_points | overall | rmse_h1 | last_slope | 1.909 [1.139, 2.679] | 0/4 cells, 0/20 cell-seeds (vs persistence) | 2.642 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | overall | rmse_h1 | lgbm | 1.843 [1.196, 2.491] | 0/4 cells, 0/20 cell-seeds (vs persistence) | 2.498 | 4 | 5 | acedf5f4 |
| loco | start_points | overall | rmse_h1 | lstm | 1.966 [1.856, 2.101] | 2/4 cells, 8/20 cell-seeds (vs persistence) | 1.960 | 4 | 5 | 5494788a |
| loco | start_points | overall | rmse_h1 | nlinear | 1.796 [1.165, 2.427] | 0/4 cells, 0/20 cell-seeds (vs persistence) | 2.379 | 4 | 5 | b4ecdb12 |
| loco | start_points | overall | rmse_h1 | patchtst | 1.838 [1.094, 2.583] | 0/4 cells, 1/20 cell-seeds (vs persistence) | 2.584 | 4 | 5 | d75a14c6 |
| loco | start_points | overall | rmse_h1 | persistence | 1.654 [1.057, 2.251] |  | 2.261 | 4 | 5 | a26a213d |
| loco | start_points | overall | rmse_h1 | rlinear | 1.728 [1.041, 2.414] | 1/4 cells, 8/20 cell-seeds (vs persistence) | 2.355 | 4 | 5 | 78bc3e35 |
| loco | start_points | overall | rmse_h1 | transformer | 2.865 [1.604, 4.208] | 0/4 cells, 0/20 cell-seeds (vs persistence) | 4.919 | 4 | 5 | 19b71fc1 |
| loco | start_points | overall | rmse_h10 | dlinear | 7.114 [6.460, 7.878] | 0/4 cells, 0/20 cell-seeds (vs persistence) | 7.220 | 4 | 5 | 3b67b415 |
| loco | start_points | overall | rmse_h10 | elasticnet | 2.633 [1.339, 3.926] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 4.343 | 4 | 5 | e1ff5d55 |
| loco | start_points | overall | rmse_h10 | gru | 2.628 [1.441, 3.814] | 4/4 cells, 15/20 cell-seeds (vs persistence) | 3.087 | 4 | 5 | 9731ae77 |
| loco | start_points | overall | rmse_h10 | itransformer | 1.882 [1.057, 2.953] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 3.579 | 4 | 5 | 9dedaedf |
| loco | start_points | overall | rmse_h10 | itransformer_sc | 2.044 [1.223, 2.975] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 3.554 | 4 | 5 | e5cc9a22 |
| loco | start_points | overall | rmse_h10 | last_slope | 3.935 [2.490, 5.381] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 5.540 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | overall | rmse_h10 | lgbm | 1.906 [1.063, 2.750] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 2.856 | 4 | 5 | acedf5f4 |
| loco | start_points | overall | rmse_h10 | lstm | 2.818 [1.900, 3.804] | 4/4 cells, 16/20 cell-seeds (vs persistence) | 3.083 | 4 | 5 | 5494788a |
| loco | start_points | overall | rmse_h10 | nlinear | 2.115 [1.174, 3.057] | 4/4 cells, 17/20 cell-seeds (vs persistence) | 3.203 | 4 | 5 | b4ecdb12 |
| loco | start_points | overall | rmse_h10 | patchtst | 1.699 [0.965, 2.810] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 3.388 | 4 | 5 | d75a14c6 |
| loco | start_points | overall | rmse_h10 | persistence | 3.348 [2.574, 4.229] |  | 3.206 | 4 | 5 | a26a213d |
| loco | start_points | overall | rmse_h10 | rlinear | 2.666 [2.035, 3.276] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 3.467 | 4 | 5 | 78bc3e35 |
| loco | start_points | overall | rmse_h10 | transformer | 3.573 [2.128, 5.537] | 2/4 cells, 12/20 cell-seeds (vs persistence) | 6.569 | 4 | 5 | 19b71fc1 |
| loco | start_points | overall | rmse_h100 | dlinear | 18.891 [15.512, 22.270] | 4/4 cells, 12/20 cell-seeds (vs persistence) | 14.095 | 4 | 5 | 3b67b415 |
| loco | start_points | overall | rmse_h100 | elasticnet | 7.439 [2.995, 13.332] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.125 | 4 | 5 | e1ff5d55 |
| loco | start_points | overall | rmse_h100 | gru | 4.009 [2.144, 6.143] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 1.518 | 4 | 5 | 9731ae77 |
| loco | start_points | overall | rmse_h100 | itransformer | 11.748 [6.795, 16.451] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 4.930 | 4 | 5 | 9dedaedf |
| loco | start_points | overall | rmse_h100 | itransformer_sc | 7.939 [4.758, 11.754] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 6.790 | 4 | 5 | e5cc9a22 |
| loco | start_points | overall | rmse_h100 | last_slope | 23.985 [14.809, 34.609] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 22.079 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | overall | rmse_h100 | lgbm | 4.269 [3.440, 5.125] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.692 | 4 | 5 | acedf5f4 |
| loco | start_points | overall | rmse_h100 | lstm | 4.606 [2.388, 6.825] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 2.327 | 4 | 5 | 5494788a |
| loco | start_points | overall | rmse_h100 | nlinear | 4.942 [4.141, 5.742] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 4.203 | 4 | 5 | b4ecdb12 |
| loco | start_points | overall | rmse_h100 | patchtst | 8.371 [4.552, 11.467] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 12.282 | 4 | 5 | d75a14c6 |
| loco | start_points | overall | rmse_h100 | persistence | 21.443 [18.142, 24.745] |  | 17.949 | 4 | 5 | a26a213d |
| loco | start_points | overall | rmse_h100 | rlinear | 11.776 [9.574, 15.807] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 10.077 | 4 | 5 | 78bc3e35 |
| loco | start_points | overall | rmse_h100 | transformer | 5.038 [2.825, 7.250] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.819 | 4 | 5 | 19b71fc1 |
| loco | start_points | overall | rmse_h25 | dlinear | 4.686 [4.128, 5.416] | 4/4 cells, 16/20 cell-seeds (vs persistence) | 4.255 | 4 | 5 | 3b67b415 |
| loco | start_points | overall | rmse_h25 | elasticnet | 5.072 [2.427, 7.717] | 3/4 cells, 15/20 cell-seeds (vs persistence) | 7.379 | 4 | 5 | e1ff5d55 |
| loco | start_points | overall | rmse_h25 | gru | 4.169 [3.642, 4.712] | 4/4 cells, 19/20 cell-seeds (vs persistence) | 4.165 | 4 | 5 | 9731ae77 |
| loco | start_points | overall | rmse_h25 | itransformer | 3.054 [2.739, 3.405] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.583 | 4 | 5 | 9dedaedf |
| loco | start_points | overall | rmse_h25 | itransformer_sc | 3.422 [2.259, 4.586] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 5.122 | 4 | 5 | e5cc9a22 |
| loco | start_points | overall | rmse_h25 | last_slope | 8.281 [5.214, 11.347] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 11.788 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | overall | rmse_h25 | lgbm | 3.069 [1.935, 4.203] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.587 | 4 | 5 | acedf5f4 |
| loco | start_points | overall | rmse_h25 | lstm | 4.874 [3.818, 6.532] | 4/4 cells, 19/20 cell-seeds (vs persistence) | 4.236 | 4 | 5 | 5494788a |
| loco | start_points | overall | rmse_h25 | nlinear | 3.220 [1.716, 4.725] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 4.195 | 4 | 5 | b4ecdb12 |
| loco | start_points | overall | rmse_h25 | patchtst | 2.709 [1.994, 3.775] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 4.324 | 4 | 5 | d75a14c6 |
| loco | start_points | overall | rmse_h25 | persistence | 7.261 [6.150, 8.841] |  | 6.423 | 4 | 5 | a26a213d |
| loco | start_points | overall | rmse_h25 | rlinear | 4.756 [4.129, 5.250] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 4.742 | 4 | 5 | 78bc3e35 |
| loco | start_points | overall | rmse_h25 | transformer | 4.335 [3.616, 4.887] | 4/4 cells, 17/20 cell-seeds (vs persistence) | 4.665 | 4 | 5 | 19b71fc1 |
| loco | start_points | overall | rmse_h50 | dlinear | 13.635 [11.939, 15.332] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 12.312 | 4 | 5 | 3b67b415 |
| loco | start_points | overall | rmse_h50 | elasticnet | 5.448 [2.837, 8.060] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 6.983 | 4 | 5 | e1ff5d55 |
| loco | start_points | overall | rmse_h50 | gru | 3.707 [2.278, 5.310] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 2.690 | 4 | 5 | 9731ae77 |
| loco | start_points | overall | rmse_h50 | itransformer | 5.715 [4.163, 7.364] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.530 | 4 | 5 | 9dedaedf |
| loco | start_points | overall | rmse_h50 | itransformer_sc | 5.012 [4.120, 6.229] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 4.768 | 4 | 5 | e5cc9a22 |
| loco | start_points | overall | rmse_h50 | last_slope | 14.573 [9.092, 19.775] | 2/4 cells, 10/20 cell-seeds (vs persistence) | 21.338 | 4 | 5 | 7a0d4ec4 |
| loco | start_points | overall | rmse_h50 | lgbm | 3.325 [2.292, 4.882] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.041 | 4 | 5 | acedf5f4 |
| loco | start_points | overall | rmse_h50 | lstm | 3.408 [2.160, 4.934] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.492 | 4 | 5 | 5494788a |
| loco | start_points | overall | rmse_h50 | nlinear | 3.876 [2.640, 5.600] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 3.605 | 4 | 5 | b4ecdb12 |
| loco | start_points | overall | rmse_h50 | patchtst | 3.600 [2.269, 4.931] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 4.691 | 4 | 5 | d75a14c6 |
| loco | start_points | overall | rmse_h50 | persistence | 13.452 [11.482, 15.613] |  | 12.879 | 4 | 5 | a26a213d |
| loco | start_points | overall | rmse_h50 | rlinear | 7.641 [6.502, 9.484] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 6.357 | 4 | 5 | 78bc3e35 |
| loco | start_points | overall | rmse_h50 | transformer | 5.091 [3.351, 6.748] | 4/4 cells, 20/20 cell-seeds (vs persistence) | 4.923 | 4 | 5 | 19b71fc1 |

</details>

<details><summary>nasa_rul (187 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rul_bias | dlinear | -2.087 [-13.721, 9.739] |  | 3.325 | 4 | 5 | 66a55967 |
| loco | all | overall | rul_bias | elasticnet | 66.081 [30.006, 96.215] |  | 11.698 | 4 | 5 | 17c49e01 |
| loco | all | overall | rul_bias | gru | 1.190 [-21.072, 28.810] |  | 3.655 | 4 | 5 | 4e5a6656 |
| loco | all | overall | rul_bias | itransformer | -0.424 [-16.524, 15.155] |  | 0.578 | 4 | 5 | cf2844f4 |
| loco | all | overall | rul_bias | itransformer_sc | -0.727 [-15.300, 15.043] |  | -1.382 | 4 | 5 | 99bba290 |
| loco | all | overall | rul_bias | lgbm | 0.366 [-15.673, 18.155] |  | 2.420 | 4 | 5 | faab17c4 |
| loco | all | overall | rul_bias | lstm | 3.186 [-12.090, 20.239] |  | -2.095 | 4 | 5 | 86645d26 |
| loco | all | overall | rul_bias | nlinear | -2.825 [-15.619, 10.439] |  | 2.532 | 4 | 5 | 723c6ded |
| loco | all | overall | rul_bias | patchtst | -14.291 [-39.824, 18.055] |  | -11.850 | 4 | 5 | 9aa4edae |
| loco | all | overall | rul_bias | rlinear | -30.680 [-46.910, -14.449] |  | -20.270 | 4 | 5 | b18361de |
| loco | all | overall | rul_bias | transformer | -3.986 [-26.778, 31.978] |  | -18.365 | 4 | 5 | a5a14771 |
| loco | all | overall | rul_mae | dlinear | 15.590 [9.447, 22.489] |  | 7.338 | 4 | 5 | 66a55967 |
| loco | all | overall | rul_mae | elasticnet | 73.095 [33.713, 101.144] |  | 16.025 | 4 | 5 | 17c49e01 |
| loco | all | overall | rul_mae | gru | 25.570 [15.361, 36.340] |  | 15.115 | 4 | 5 | 4e5a6656 |
| loco | all | overall | rul_mae | itransformer | 16.708 [10.672, 22.745] |  | 12.726 | 4 | 5 | cf2844f4 |
| loco | all | overall | rul_mae | itransformer_sc | 17.612 [12.364, 22.860] |  | 12.174 | 4 | 5 | 99bba290 |
| loco | all | overall | rul_mae | lgbm | 19.833 [14.226, 25.439] |  | 12.709 | 4 | 5 | faab17c4 |
| loco | all | overall | rul_mae | lstm | 17.433 [11.508, 23.887] |  | 12.498 | 4 | 5 | 86645d26 |
| loco | all | overall | rul_mae | nlinear | 16.251 [10.278, 23.435] |  | 8.051 | 4 | 5 | 723c6ded |
| loco | all | overall | rul_mae | patchtst | 36.057 [22.341, 46.425] |  | 16.541 | 4 | 5 | 9aa4edae |
| loco | all | overall | rul_mae | rlinear | 35.155 [22.550, 47.760] |  | 27.107 | 4 | 5 | b18361de |
| loco | all | overall | rul_mae | transformer | 31.330 [21.904, 42.150] |  | 21.483 | 4 | 5 | a5a14771 |
| loco | start_points | fixed:30 | rul_bias | dlinear | -9.717 [-28.270, 10.446] |  | -3.067 | 4 | 5 | 66a55967 |
| loco | start_points | fixed:30 | rul_bias | elasticnet | 129.167 [35.019, 223.316] |  | 24.003 | 4 | 5 | 17c49e01 |
| loco | start_points | fixed:30 | rul_bias | gru | -7.037 [-35.240, 28.240] |  | -4.931 | 4 | 5 | 4e5a6656 |
| loco | start_points | fixed:30 | rul_bias | itransformer | -5.328 [-23.096, 13.330] |  | -8.628 | 4 | 5 | cf2844f4 |
| loco | start_points | fixed:30 | rul_bias | itransformer_sc | -5.930 [-26.030, 16.217] |  | -3.468 | 4 | 5 | 99bba290 |
| loco | start_points | fixed:30 | rul_bias | lgbm | -7.320 [-27.760, 18.060] |  | -8.572 | 4 | 5 | faab17c4 |
| loco | start_points | fixed:30 | rul_bias | lstm | 1.285 [-15.986, 18.555] |  | -16.006 | 4 | 5 | 86645d26 |
| loco | start_points | fixed:30 | rul_bias | nlinear | -10.812 [-31.284, 11.268] |  | -3.674 | 4 | 5 | 723c6ded |
| loco | start_points | fixed:30 | rul_bias | patchtst | -30.979 [-76.374, 14.416] |  | -11.338 | 4 | 5 | 9aa4edae |
| loco | start_points | fixed:30 | rul_bias | rlinear | -51.246 [-80.050, -22.441] |  | -32.556 | 4 | 5 | b18361de |
| loco | start_points | fixed:30 | rul_bias | transformer | -16.816 [-49.428, 30.147] |  | -27.779 | 4 | 5 | a5a14771 |
| loco | start_points | fixed:30 | rul_mae | dlinear | 20.087 [7.485, 32.189] |  | 3.067 | 4 | 5 | 66a55967 |
| loco | start_points | fixed:30 | rul_mae | elasticnet | 129.167 [35.019, 223.316] |  | 24.003 | 4 | 5 | 17c49e01 |
| loco | start_points | fixed:30 | rul_mae | gru | 29.745 [14.111, 45.380] |  | 4.931 | 4 | 5 | 4e5a6656 |
| loco | start_points | fixed:30 | rul_mae | itransformer | 15.959 [6.830, 25.088] |  | 8.628 | 4 | 5 | cf2844f4 |
| loco | start_points | fixed:30 | rul_mae | itransformer_sc | 19.274 [8.882, 29.667] |  | 5.280 | 4 | 5 | 99bba290 |
| loco | start_points | fixed:30 | rul_mae | lgbm | 22.019 [12.262, 31.776] |  | 8.572 | 4 | 5 | faab17c4 |
| loco | start_points | fixed:30 | rul_mae | lstm | 17.270 [13.867, 21.959] |  | 16.006 | 4 | 5 | 86645d26 |
| loco | start_points | fixed:30 | rul_mae | nlinear | 21.852 [8.276, 35.657] |  | 3.674 | 4 | 5 | 723c6ded |
| loco | start_points | fixed:30 | rul_mae | patchtst | 51.064 [25.538, 76.374] |  | 11.338 | 4 | 5 | 9aa4edae |
| loco | start_points | fixed:30 | rul_mae | rlinear | 51.246 [22.441, 80.050] |  | 32.556 | 4 | 5 | b18361de |
| loco | start_points | fixed:30 | rul_mae | transformer | 42.674 [31.168, 54.180] |  | 27.779 | 4 | 5 | a5a14771 |
| loco | start_points | fixed:50 | rul_bias | dlinear | -4.644 [-16.512, 6.055] |  | 6.490 | 4 | 5 | 66a55967 |
| loco | start_points | fixed:50 | rul_bias | elasticnet | 45.569 [6.906, 90.344] |  | -3.054 | 4 | 5 | 17c49e01 |
| loco | start_points | fixed:50 | rul_bias | gru | 7.266 [-20.381, 34.981] |  | 19.841 | 4 | 5 | 4e5a6656 |
| loco | start_points | fixed:50 | rul_bias | itransformer | -3.401 [-14.815, 7.765] |  | -7.269 | 4 | 5 | cf2844f4 |
| loco | start_points | fixed:50 | rul_bias | itransformer_sc | -0.918 [-10.516, 5.292] |  | 1.347 | 4 | 5 | 99bba290 |
| loco | start_points | fixed:50 | rul_bias | lgbm | 3.526 [-14.207, 21.085] |  | 6.720 | 4 | 5 | faab17c4 |
| loco | start_points | fixed:50 | rul_bias | lstm | 10.359 [-8.215, 24.709] |  | 11.247 | 4 | 5 | 86645d26 |
| loco | start_points | fixed:50 | rul_bias | nlinear | -6.348 [-19.473, 3.693] |  | 0.853 | 4 | 5 | 723c6ded |
| loco | start_points | fixed:50 | rul_bias | patchtst | -18.984 [-47.651, 9.684] |  | -4.446 | 4 | 5 | 9aa4edae |
| loco | start_points | fixed:50 | rul_bias | rlinear | -34.114 [-59.721, -8.506] |  | -16.513 | 4 | 5 | b18361de |
| loco | start_points | fixed:50 | rul_bias | transformer | -2.739 [-34.213, 39.132] |  | -8.543 | 4 | 5 | a5a14771 |
| loco | start_points | fixed:50 | rul_mae | dlinear | 10.700 [5.915, 19.540] |  | 6.490 | 4 | 5 | 66a55967 |
| loco | start_points | fixed:50 | rul_mae | elasticnet | 47.096 [9.960, 90.344] |  | 3.054 | 4 | 5 | 17c49e01 |
| loco | start_points | fixed:50 | rul_mae | gru | 27.647 [14.936, 42.450] |  | 19.841 | 4 | 5 | 4e5a6656 |
| loco | start_points | fixed:50 | rul_mae | itransformer | 11.981 [7.851, 18.698] |  | 7.269 | 4 | 5 | cf2844f4 |
| loco | start_points | fixed:50 | rul_mae | itransformer_sc | 9.532 [6.433, 13.458] |  | 7.024 | 4 | 5 | 99bba290 |
| loco | start_points | fixed:50 | rul_mae | lgbm | 14.117 [3.699, 24.535] |  | 6.720 | 4 | 5 | faab17c4 |
| loco | start_points | fixed:50 | rul_mae | lstm | 18.822 [12.915, 26.129] |  | 11.247 | 4 | 5 | 86645d26 |
| loco | start_points | fixed:50 | rul_mae | nlinear | 10.065 [2.346, 21.318] |  | 0.950 | 4 | 5 | 723c6ded |
| loco | start_points | fixed:50 | rul_mae | patchtst | 30.890 [13.226, 47.754] |  | 4.446 | 4 | 5 | 9aa4edae |
| loco | start_points | fixed:50 | rul_mae | rlinear | 34.195 [8.670, 59.721] |  | 16.513 | 4 | 5 | b18361de |
| loco | start_points | fixed:50 | rul_mae | transformer | 31.783 [13.137, 50.428] |  | 8.543 | 4 | 5 | a5a14771 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | dlinear | 0.250 [0.000, 0.750] |  | 1.000 | 4 | 5 | 66a55967 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | elasticnet | 0.000 [0.000, 0.000] |  | 0.000 | 4 | 5 | 17c49e01 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | gru | 0.200 [0.000, 0.450] |  | 0.600 | 4 | 5 | 4e5a6656 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | itransformer | 0.450 [0.100, 0.800] |  | 0.800 | 4 | 5 | cf2844f4 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | itransformer_sc | 0.300 [0.000, 0.600] |  | 0.800 | 4 | 5 | 99bba290 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | lgbm | 0.500 [0.000, 1.000] |  | 1.000 | 4 | 5 | faab17c4 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | lstm | 0.300 [0.050, 0.650] |  | 0.200 | 4 | 5 | 86645d26 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | nlinear | 0.250 [0.000, 0.750] |  | 1.000 | 4 | 5 | 723c6ded |
| loco | start_points | frac:0.3 | alpha_lambda_acc | patchtst | 0.100 [0.000, 0.300] |  | 0.400 | 4 | 5 | 9aa4edae |
| loco | start_points | frac:0.3 | alpha_lambda_acc | rlinear | 0.000 [0.000, 0.000] |  | 0.000 | 4 | 5 | b18361de |
| loco | start_points | frac:0.3 | alpha_lambda_acc | transformer | 0.000 [0.000, 0.000] |  | 0.000 | 4 | 5 | a5a14771 |
| loco | start_points | frac:0.3 | rul_bias | dlinear | -9.283 [-24.311, 7.291] |  | -4.567 | 4 | 5 | 66a55967 |
| loco | start_points | frac:0.3 | rul_bias | elasticnet | 211.782 [90.463, 296.931] |  | 22.509 | 4 | 5 | 17c49e01 |
| loco | start_points | frac:0.3 | rul_bias | gru | -7.024 [-31.128, 24.813] |  | -8.151 | 4 | 5 | 4e5a6656 |
| loco | start_points | frac:0.3 | rul_bias | itransformer | -6.555 [-20.131, 10.240] |  | -10.232 | 4 | 5 | cf2844f4 |
| loco | start_points | frac:0.3 | rul_bias | itransformer_sc | -7.153 [-22.666, 11.258] |  | -7.678 | 4 | 5 | 99bba290 |
| loco | start_points | frac:0.3 | rul_bias | lgbm | -7.273 [-22.637, 12.589] |  | -10.335 | 4 | 5 | faab17c4 |
| loco | start_points | frac:0.3 | rul_bias | lstm | 5.468 [-15.748, 26.684] |  | -16.633 | 4 | 5 | 86645d26 |
| loco | start_points | frac:0.3 | rul_bias | nlinear | -8.875 [-25.881, 10.471] |  | -4.035 | 4 | 5 | 723c6ded |
| loco | start_points | frac:0.3 | rul_bias | patchtst | -30.882 [-68.293, 6.530] |  | -15.235 | 4 | 5 | 9aa4edae |
| loco | start_points | frac:0.3 | rul_bias | rlinear | -49.173 [-74.667, -23.679] |  | -33.136 | 4 | 5 | b18361de |
| loco | start_points | frac:0.3 | rul_bias | transformer | -19.609 [-48.246, 23.003] |  | -32.638 | 4 | 5 | a5a14771 |
| loco | start_points | frac:0.3 | rul_mae | dlinear | 17.312 [8.178, 26.224] |  | 4.567 | 4 | 5 | 66a55967 |
| loco | start_points | frac:0.3 | rul_mae | elasticnet | 211.782 [90.463, 296.931] |  | 22.509 | 4 | 5 | 17c49e01 |
| loco | start_points | frac:0.3 | rul_mae | gru | 27.127 [14.757, 39.496] |  | 8.151 | 4 | 5 | 4e5a6656 |
| loco | start_points | frac:0.3 | rul_mae | itransformer | 15.087 [9.774, 20.400] |  | 10.232 | 4 | 5 | cf2844f4 |
| loco | start_points | frac:0.3 | rul_mae | itransformer_sc | 18.478 [11.072, 25.426] |  | 8.379 | 4 | 5 | 99bba290 |
| loco | start_points | frac:0.3 | rul_mae | lgbm | 17.866 [11.770, 23.962] |  | 10.335 | 4 | 5 | faab17c4 |
| loco | start_points | frac:0.3 | rul_mae | lstm | 21.216 [15.748, 29.741] |  | 16.633 | 4 | 5 | 86645d26 |
| loco | start_points | frac:0.3 | rul_mae | nlinear | 19.024 [8.101, 29.315] |  | 4.035 | 4 | 5 | 723c6ded |
| loco | start_points | frac:0.3 | rul_mae | patchtst | 45.029 [21.766, 68.293] |  | 15.235 | 4 | 5 | 9aa4edae |
| loco | start_points | frac:0.3 | rul_mae | rlinear | 49.173 [23.679, 74.667] |  | 33.136 | 4 | 5 | b18361de |
| loco | start_points | frac:0.3 | rul_mae | transformer | 40.699 [33.584, 48.719] |  | 32.638 | 4 | 5 | a5a14771 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | dlinear | 0.250 [0.000, 0.750] |  | 0.000 | 4 | 5 | 66a55967 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | elasticnet | 0.000 [0.000, 0.000] |  | 0.000 | 4 | 5 | 17c49e01 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | gru | 0.450 [0.000, 0.900] |  | 1.000 | 4 | 5 | 4e5a6656 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | itransformer | 0.200 [0.000, 0.600] |  | 0.000 | 4 | 5 | cf2844f4 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | itransformer_sc | 0.200 [0.000, 0.450] |  | 0.200 | 4 | 5 | 99bba290 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | lgbm | 0.500 [0.000, 1.000] |  | 1.000 | 4 | 5 | faab17c4 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | lstm | 0.050 [0.000, 0.150] |  | 0.200 | 4 | 5 | 86645d26 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | nlinear | 0.450 [0.000, 0.900] |  | 0.800 | 4 | 5 | 723c6ded |
| loco | start_points | frac:0.5 | alpha_lambda_acc | patchtst | 0.250 [0.000, 0.750] |  | 1.000 | 4 | 5 | 9aa4edae |
| loco | start_points | frac:0.5 | alpha_lambda_acc | rlinear | 0.000 [0.000, 0.000] |  | 0.000 | 4 | 5 | b18361de |
| loco | start_points | frac:0.5 | alpha_lambda_acc | transformer | 0.100 [0.000, 0.300] |  | 0.000 | 4 | 5 | a5a14771 |
| loco | start_points | frac:0.5 | rul_bias | dlinear | -3.677 [-16.532, 13.048] |  | -10.025 | 4 | 5 | 66a55967 |
| loco | start_points | frac:0.5 | rul_bias | elasticnet | 50.397 [2.743, 105.076] |  | -11.688 | 4 | 5 | 17c49e01 |
| loco | start_points | frac:0.5 | rul_bias | gru | 3.424 [-19.139, 32.354] |  | 0.943 | 4 | 5 | 4e5a6656 |
| loco | start_points | frac:0.5 | rul_bias | itransformer | -2.853 [-20.143, 14.436] |  | -10.789 | 4 | 5 | cf2844f4 |
| loco | start_points | frac:0.5 | rul_bias | itransformer_sc | 1.999 [-15.022, 19.021] |  | -12.055 | 4 | 5 | 99bba290 |
| loco | start_points | frac:0.5 | rul_bias | lgbm | 0.174 [-18.295, 20.665] |  | -5.533 | 4 | 5 | faab17c4 |
| loco | start_points | frac:0.5 | rul_bias | lstm | 1.202 [-18.275, 20.679] |  | -11.336 | 4 | 5 | 86645d26 |
| loco | start_points | frac:0.5 | rul_bias | nlinear | -3.151 [-17.993, 14.818] |  | -6.966 | 4 | 5 | 723c6ded |
| loco | start_points | frac:0.5 | rul_bias | patchtst | -7.469 [-35.574, 21.331] |  | 1.099 | 4 | 5 | 9aa4edae |
| loco | start_points | frac:0.5 | rul_bias | rlinear | -30.356 [-47.093, -13.620] |  | -14.913 | 4 | 5 | b18361de |
| loco | start_points | frac:0.5 | rul_bias | transformer | -2.473 [-23.908, 33.546] |  | -20.963 | 4 | 5 | a5a14771 |
| loco | start_points | frac:0.5 | rul_mae | dlinear | 14.046 [7.546, 20.547] |  | 10.025 | 4 | 5 | 66a55967 |
| loco | start_points | frac:0.5 | rul_mae | elasticnet | 56.241 [20.275, 105.076] |  | 11.688 | 4 | 5 | 17c49e01 |
| loco | start_points | frac:0.5 | rul_mae | gru | 20.313 [5.001, 35.830] |  | 2.932 | 4 | 5 | 4e5a6656 |
| loco | start_points | frac:0.5 | rul_mae | itransformer | 17.313 [9.552, 25.073] |  | 10.789 | 4 | 5 | cf2844f4 |
| loco | start_points | frac:0.5 | rul_mae | itransformer_sc | 17.021 [12.156, 22.402] |  | 12.055 | 4 | 5 | 99bba290 |
| loco | start_points | frac:0.5 | rul_mae | lgbm | 15.443 [3.684, 27.201] |  | 5.533 | 4 | 5 | faab17c4 |
| loco | start_points | frac:0.5 | rul_mae | lstm | 19.477 [14.369, 24.586] |  | 11.336 | 4 | 5 | 86645d26 |
| loco | start_points | frac:0.5 | rul_mae | nlinear | 14.190 [6.277, 22.104] |  | 6.966 | 4 | 5 | 723c6ded |
| loco | start_points | frac:0.5 | rul_mae | patchtst | 28.434 [10.802, 38.925] |  | 2.417 | 4 | 5 | 9aa4edae |
| loco | start_points | frac:0.5 | rul_mae | rlinear | 30.356 [13.620, 47.093] |  | 14.913 | 4 | 5 | b18361de |
| loco | start_points | frac:0.5 | rul_mae | transformer | 28.331 [17.057, 44.027] |  | 20.963 | 4 | 5 | a5a14771 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | dlinear | 0.500 [0.000, 1.000] |  | 1.000 | 4 | 5 | 66a55967 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | elasticnet | 0.250 [0.000, 0.750] |  | 0.000 | 4 | 5 | 17c49e01 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | gru | 0.150 [0.000, 0.450] |  | 0.000 | 4 | 5 | 4e5a6656 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | itransformer | 0.400 [0.000, 0.800] |  | 1.000 | 4 | 5 | cf2844f4 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | itransformer_sc | 0.450 [0.100, 0.800] |  | 0.600 | 4 | 5 | 99bba290 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | lgbm | 0.000 [0.000, 0.000] |  | 0.000 | 4 | 5 | faab17c4 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | lstm | 0.200 [0.000, 0.450] |  | 0.200 | 4 | 5 | 86645d26 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | nlinear | 0.450 [0.000, 0.900] |  | 0.800 | 4 | 5 | 723c6ded |
| loco | start_points | frac:0.7 | alpha_lambda_acc | patchtst | 0.250 [0.000, 0.750] |  | 0.000 | 4 | 5 | 9aa4edae |
| loco | start_points | frac:0.7 | alpha_lambda_acc | rlinear | 0.200 [0.000, 0.600] |  | 0.800 | 4 | 5 | b18361de |
| loco | start_points | frac:0.7 | alpha_lambda_acc | transformer | 0.150 [0.000, 0.300] |  | 0.200 | 4 | 5 | a5a14771 |
| loco | start_points | frac:0.7 | rul_bias | dlinear | 0.159 [-10.395, 7.937] |  | 2.313 | 4 | 5 | 66a55967 |
| loco | start_points | frac:0.7 | rul_bias | elasticnet | 17.312 [-6.190, 42.581] |  | -5.238 | 4 | 5 | 17c49e01 |
| loco | start_points | frac:0.7 | rul_bias | gru | 9.979 [-10.381, 30.919] |  | 18.076 | 4 | 5 | 4e5a6656 |
| loco | start_points | frac:0.7 | rul_bias | itransformer | -0.725 [-15.893, 11.730] |  | 1.615 | 4 | 5 | cf2844f4 |
| loco | start_points | frac:0.7 | rul_bias | itransformer_sc | -2.869 [-14.168, 7.446] |  | -0.999 | 4 | 5 | 99bba290 |
| loco | start_points | frac:0.7 | rul_bias | lgbm | 6.034 [-10.518, 18.770] |  | 12.741 | 4 | 5 | faab17c4 |
| loco | start_points | frac:0.7 | rul_bias | lstm | 2.740 [-12.883, 16.002] |  | 9.299 | 4 | 5 | 86645d26 |
| loco | start_points | frac:0.7 | rul_bias | nlinear | -0.443 [-11.982, 7.535] |  | 3.706 | 4 | 5 | 723c6ded |
| loco | start_points | frac:0.7 | rul_bias | patchtst | -1.072 [-23.546, 24.999] |  | -10.746 | 4 | 5 | 9aa4edae |
| loco | start_points | frac:0.7 | rul_bias | rlinear | -9.908 [-22.516, 2.700] |  | -2.424 | 4 | 5 | b18361de |
| loco | start_points | frac:0.7 | rul_bias | transformer | 10.777 [-8.862, 39.559] |  | -5.499 | 4 | 5 | a5a14771 |
| loco | start_points | frac:0.7 | rul_mae | dlinear | 7.682 [2.936, 12.429] |  | 2.313 | 4 | 5 | 66a55967 |
| loco | start_points | frac:0.7 | rul_mae | elasticnet | 23.502 [6.190, 45.676] |  | 5.238 | 4 | 5 | 17c49e01 |
| loco | start_points | frac:0.7 | rul_mae | gru | 20.525 [8.105, 36.110] |  | 18.076 | 4 | 5 | 4e5a6656 |
| loco | start_points | frac:0.7 | rul_mae | itransformer | 11.037 [3.534, 18.540] |  | 1.906 | 4 | 5 | cf2844f4 |
| loco | start_points | frac:0.7 | rul_mae | itransformer_sc | 9.110 [3.515, 14.877] |  | 3.834 | 4 | 5 | 99bba290 |
| loco | start_points | frac:0.7 | rul_mae | lgbm | 15.169 [9.787, 20.489] |  | 12.741 | 4 | 5 | faab17c4 |
| loco | start_points | frac:0.7 | rul_mae | lstm | 13.834 [7.011, 20.656] |  | 9.306 | 4 | 5 | 86645d26 |
| loco | start_points | frac:0.7 | rul_mae | nlinear | 8.162 [3.117, 13.834] |  | 3.706 | 4 | 5 | 723c6ded |
| loco | start_points | frac:0.7 | rul_mae | patchtst | 20.286 [6.183, 34.389] |  | 10.746 | 4 | 5 | 9aa4edae |
| loco | start_points | frac:0.7 | rul_mae | rlinear | 13.821 [5.125, 23.347] |  | 2.424 | 4 | 5 | b18361de |
| loco | start_points | frac:0.7 | rul_mae | transformer | 20.290 [7.178, 42.799] |  | 7.459 | 4 | 5 | a5a14771 |
| loco | start_points | overall | rul_bias | dlinear | -5.432 [-19.195, 8.558] |  | -1.771 | 4 | 5 | 66a55967 |
| loco | start_points | overall | rul_bias | elasticnet | 90.846 [35.290, 136.401] |  | 5.306 | 4 | 5 | 17c49e01 |
| loco | start_points | overall | rul_bias | gru | 1.322 [-22.311, 30.262] |  | 5.156 | 4 | 5 | 4e5a6656 |
| loco | start_points | overall | rul_bias | itransformer | -3.773 [-18.801, 10.633] |  | -7.061 | 4 | 5 | cf2844f4 |
| loco | start_points | overall | rul_bias | itransformer_sc | -2.974 [-17.538, 11.970] |  | -4.571 | 4 | 5 | 99bba290 |
| loco | start_points | overall | rul_bias | lgbm | -0.972 [-19.052, 18.602] |  | -0.996 | 4 | 5 | faab17c4 |
| loco | start_points | overall | rul_bias | lstm | 4.211 [-11.668, 20.089] |  | -4.686 | 4 | 5 | 86645d26 |
| loco | start_points | overall | rul_bias | nlinear | -5.926 [-21.329, 9.541] |  | -2.023 | 4 | 5 | 723c6ded |
| loco | start_points | overall | rul_bias | patchtst | -17.877 [-48.624, 14.982] |  | -8.133 | 4 | 5 | 9aa4edae |
| loco | start_points | overall | rul_bias | rlinear | -34.959 [-56.810, -13.109] |  | -19.908 | 4 | 5 | b18361de |
| loco | start_points | overall | rul_bias | transformer | -6.172 [-33.509, 33.970] |  | -19.084 | 4 | 5 | a5a14771 |
| loco | start_points | overall | rul_mae | dlinear | 13.965 [7.618, 21.495] |  | 5.293 | 4 | 5 | 66a55967 |
| loco | start_points | overall | rul_mae | elasticnet | 93.558 [41.998, 137.829] |  | 13.298 | 4 | 5 | 17c49e01 |
| loco | start_points | overall | rul_mae | gru | 25.071 [12.047, 38.096] |  | 10.786 | 4 | 5 | 4e5a6656 |
| loco | start_points | overall | rul_mae | itransformer | 14.275 [7.625, 20.932] |  | 7.765 | 4 | 5 | cf2844f4 |
| loco | start_points | overall | rul_mae | itransformer_sc | 14.683 [9.289, 20.078] |  | 7.314 | 4 | 5 | 99bba290 |
| loco | start_points | overall | rul_mae | lgbm | 16.923 [8.253, 25.593] |  | 8.780 | 4 | 5 | faab17c4 |
| loco | start_points | overall | rul_mae | lstm | 18.124 [13.698, 23.461] |  | 12.906 | 4 | 5 | 86645d26 |
| loco | start_points | overall | rul_mae | nlinear | 14.659 [6.909, 23.565] |  | 3.866 | 4 | 5 | 723c6ded |
| loco | start_points | overall | rul_mae | patchtst | 35.141 [17.202, 50.136] |  | 8.836 | 4 | 5 | 9aa4edae |
| loco | start_points | overall | rul_mae | rlinear | 35.758 [14.707, 56.810] |  | 19.908 | 4 | 5 | b18361de |
| loco | start_points | overall | rul_mae | transformer | 32.755 [20.489, 45.022] |  | 19.476 | 4 | 5 | a5a14771 |

</details>

<details><summary>nasa_soh (84 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse | dlinear | 0.940 [0.706, 1.174] | 3/4 cells, 13/20 cell-seeds (vs prev_soh) | 1.202 | 4 | 5 | 5ef63051 |
| loco | all | overall | rmse | elasticnet | 1.240 [0.701, 2.043] | 2/4 cells, 10/20 cell-seeds (vs prev_soh) | 2.473 | 4 | 5 | c3c0651b |
| loco | all | overall | rmse | gru | 2.673 [2.353, 3.075] | 0/4 cells, 0/20 cell-seeds (vs prev_soh) | 3.295 | 4 | 5 | dbed923e |
| loco | all | overall | rmse | itransformer | 0.703 [0.540, 0.866] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) | 0.936 | 4 | 5 | 48e8d64a |
| loco | all | overall | rmse | itransformer_sc | 0.699 [0.563, 0.835] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) | 0.820 | 4 | 5 | 197d4e36 |
| loco | all | overall | rmse | lgbm | 0.928 [0.694, 1.162] | 3/4 cells, 15/20 cell-seeds (vs prev_soh) | 1.184 | 4 | 5 | e72f6de0 |
| loco | all | overall | rmse | lstm | 1.187 [1.141, 1.240] | 1/4 cells, 12/20 cell-seeds (vs prev_soh) | 1.156 | 4 | 5 | 7e0af82e |
| loco | all | overall | rmse | nlinear | 0.933 [0.693, 1.173] | 3/4 cells, 14/20 cell-seeds (vs prev_soh) | 1.203 | 4 | 5 | 1d4b3de0 |
| loco | all | overall | rmse | patchtst | 0.928 [0.656, 1.201] | 3/4 cells, 15/20 cell-seeds (vs prev_soh) | 1.261 | 4 | 5 | ef980b9c |
| loco | all | overall | rmse | prev_soh | 0.955 [0.697, 1.213] |  | 1.245 | 4 | 5 | 0d396b2f |
| loco | all | overall | rmse | rlinear | 0.929 [0.669, 1.189] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) | 1.219 | 4 | 5 | bd5b08dc |
| loco | all | overall | rmse | transformer | 3.666 [2.774, 5.171] | 0/4 cells, 0/20 cell-seeds (vs prev_soh) | 5.909 | 4 | 5 | 078809a4 |
| loco | start_points | fixed:30 | rmse | dlinear | 0.297 [0.156, 0.407] | 2/4 cells, 10/20 cell-seeds (vs prev_soh) | 0.089 | 4 | 5 | 5ef63051 |
| loco | start_points | fixed:30 | rmse | elasticnet | 0.906 [0.116, 2.335] | 2/4 cells, 10/20 cell-seeds (vs prev_soh) | 3.046 | 4 | 5 | c3c0651b |
| loco | start_points | fixed:30 | rmse | gru | 2.587 [1.938, 3.417] | 0/4 cells, 2/20 cell-seeds (vs prev_soh) | 2.154 | 4 | 5 | dbed923e |
| loco | start_points | fixed:30 | rmse | itransformer | 0.191 [0.047, 0.451] | 4/4 cells, 14/20 cell-seeds (vs prev_soh) | 0.086 | 4 | 5 | 48e8d64a |
| loco | start_points | fixed:30 | rmse | itransformer_sc | 0.253 [0.086, 0.520] | 1/4 cells, 7/20 cell-seeds (vs prev_soh) | 0.058 | 4 | 5 | 197d4e36 |
| loco | start_points | fixed:30 | rmse | lgbm | 0.348 [0.152, 0.577] | 1/4 cells, 5/20 cell-seeds (vs prev_soh) | 0.090 | 4 | 5 | e72f6de0 |
| loco | start_points | fixed:30 | rmse | lstm | 0.702 [0.392, 1.012] | 1/4 cells, 5/20 cell-seeds (vs prev_soh) | 0.260 | 4 | 5 | 7e0af82e |
| loco | start_points | fixed:30 | rmse | nlinear | 0.298 [0.121, 0.506] | 2/4 cells, 8/20 cell-seeds (vs prev_soh) | 0.067 | 4 | 5 | 1d4b3de0 |
| loco | start_points | fixed:30 | rmse | patchtst | 0.296 [0.090, 0.657] | 1/4 cells, 5/20 cell-seeds (vs prev_soh) | 0.066 | 4 | 5 | ef980b9c |
| loco | start_points | fixed:30 | rmse | prev_soh | 0.252 [0.064, 0.465] |  | 0.284 | 4 | 5 | 0d396b2f |
| loco | start_points | fixed:30 | rmse | rlinear | 0.262 [0.062, 0.587] | 1/4 cells, 8/20 cell-seeds (vs prev_soh) | 0.027 | 4 | 5 | bd5b08dc |
| loco | start_points | fixed:30 | rmse | transformer | 2.529 [1.580, 3.653] | 0/4 cells, 2/20 cell-seeds (vs prev_soh) | 4.185 | 4 | 5 | 078809a4 |
| loco | start_points | fixed:50 | rmse | dlinear | 0.421 [0.248, 0.594] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) | 0.515 | 4 | 5 | 5ef63051 |
| loco | start_points | fixed:50 | rmse | elasticnet | 0.308 [0.098, 0.557] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) | 0.659 | 4 | 5 | c3c0651b |
| loco | start_points | fixed:50 | rmse | gru | 2.190 [1.895, 2.486] | 0/4 cells, 5/20 cell-seeds (vs prev_soh) | 1.811 | 4 | 5 | dbed923e |
| loco | start_points | fixed:50 | rmse | itransformer | 0.248 [0.141, 0.401] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) | 0.484 | 4 | 5 | 48e8d64a |
| loco | start_points | fixed:50 | rmse | itransformer_sc | 0.373 [0.152, 0.762] | 3/4 cells, 17/20 cell-seeds (vs prev_soh) | 0.964 | 4 | 5 | 197d4e36 |
| loco | start_points | fixed:50 | rmse | lgbm | 0.684 [0.400, 1.140] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) | 0.568 | 4 | 5 | e72f6de0 |
| loco | start_points | fixed:50 | rmse | lstm | 1.040 [0.799, 1.281] | 2/4 cells, 12/20 cell-seeds (vs prev_soh) | 1.202 | 4 | 5 | 7e0af82e |
| loco | start_points | fixed:50 | rmse | nlinear | 0.391 [0.268, 0.513] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) | 0.438 | 4 | 5 | 1d4b3de0 |
| loco | start_points | fixed:50 | rmse | patchtst | 0.186 [0.095, 0.317] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) | 0.387 | 4 | 5 | ef980b9c |
| loco | start_points | fixed:50 | rmse | prev_soh | 1.054 [0.840, 1.418] |  | 0.930 | 4 | 5 | 0d396b2f |
| loco | start_points | fixed:50 | rmse | rlinear | 0.249 [0.145, 0.320] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) | 0.090 | 4 | 5 | bd5b08dc |
| loco | start_points | fixed:50 | rmse | transformer | 2.460 [1.309, 3.784] | 0/4 cells, 6/20 cell-seeds (vs prev_soh) | 4.467 | 4 | 5 | 078809a4 |
| loco | start_points | frac:0.3 | rmse | dlinear | 0.286 [0.228, 0.365] | 3/4 cells, 15/20 cell-seeds (vs prev_soh) | 0.278 | 4 | 5 | 5ef63051 |
| loco | start_points | frac:0.3 | rmse | elasticnet | 0.464 [0.067, 0.862] | 2/4 cells, 10/20 cell-seeds (vs prev_soh) | 1.110 | 4 | 5 | c3c0651b |
| loco | start_points | frac:0.3 | rmse | gru | 2.280 [1.797, 2.676] | 0/4 cells, 1/20 cell-seeds (vs prev_soh) | 2.814 | 4 | 5 | dbed923e |
| loco | start_points | frac:0.3 | rmse | itransformer | 0.235 [0.113, 0.315] | 3/4 cells, 16/20 cell-seeds (vs prev_soh) | 0.329 | 4 | 5 | 48e8d64a |
| loco | start_points | frac:0.3 | rmse | itransformer_sc | 0.295 [0.213, 0.402] | 3/4 cells, 15/20 cell-seeds (vs prev_soh) | 0.452 | 4 | 5 | 197d4e36 |
| loco | start_points | frac:0.3 | rmse | lgbm | 0.417 [0.237, 0.618] | 3/4 cells, 15/20 cell-seeds (vs prev_soh) | 0.469 | 4 | 5 | e72f6de0 |
| loco | start_points | frac:0.3 | rmse | lstm | 0.776 [0.654, 0.954] | 1/4 cells, 10/20 cell-seeds (vs prev_soh) | 0.656 | 4 | 5 | 7e0af82e |
| loco | start_points | frac:0.3 | rmse | nlinear | 0.294 [0.202, 0.392] | 3/4 cells, 16/20 cell-seeds (vs prev_soh) | 0.180 | 4 | 5 | 1d4b3de0 |
| loco | start_points | frac:0.3 | rmse | patchtst | 0.337 [0.143, 0.481] | 3/4 cells, 15/20 cell-seeds (vs prev_soh) | 0.522 | 4 | 5 | ef980b9c |
| loco | start_points | frac:0.3 | rmse | prev_soh | 0.598 [0.257, 0.992] |  | 0.156 | 4 | 5 | 0d396b2f |
| loco | start_points | frac:0.3 | rmse | rlinear | 0.340 [0.128, 0.496] | 3/4 cells, 15/20 cell-seeds (vs prev_soh) | 0.412 | 4 | 5 | bd5b08dc |
| loco | start_points | frac:0.3 | rmse | transformer | 3.026 [2.107, 3.945] | 0/4 cells, 2/20 cell-seeds (vs prev_soh) | 4.020 | 4 | 5 | 078809a4 |
| loco | start_points | frac:0.5 | rmse | dlinear | 0.302 [0.186, 0.410] | 4/4 cells, 19/20 cell-seeds (vs prev_soh) | 0.376 | 4 | 5 | 5ef63051 |
| loco | start_points | frac:0.5 | rmse | elasticnet | 0.470 [0.304, 0.744] | 3/4 cells, 15/20 cell-seeds (vs prev_soh) | 0.881 | 4 | 5 | c3c0651b |
| loco | start_points | frac:0.5 | rmse | gru | 1.844 [1.477, 2.202] | 0/4 cells, 2/20 cell-seeds (vs prev_soh) | 1.984 | 4 | 5 | dbed923e |
| loco | start_points | frac:0.5 | rmse | itransformer | 0.232 [0.082, 0.468] | 4/4 cells, 18/20 cell-seeds (vs prev_soh) | 0.126 | 4 | 5 | 48e8d64a |
| loco | start_points | frac:0.5 | rmse | itransformer_sc | 0.233 [0.073, 0.508] | 3/4 cells, 17/20 cell-seeds (vs prev_soh) | 0.085 | 4 | 5 | 197d4e36 |
| loco | start_points | frac:0.5 | rmse | lgbm | 0.250 [0.065, 0.529] | 3/4 cells, 15/20 cell-seeds (vs prev_soh) | 0.028 | 4 | 5 | e72f6de0 |
| loco | start_points | frac:0.5 | rmse | lstm | 0.953 [0.772, 1.134] | 0/4 cells, 6/20 cell-seeds (vs prev_soh) | 0.845 | 4 | 5 | 7e0af82e |
| loco | start_points | frac:0.5 | rmse | nlinear | 0.277 [0.146, 0.488] | 4/4 cells, 18/20 cell-seeds (vs prev_soh) | 0.218 | 4 | 5 | 1d4b3de0 |
| loco | start_points | frac:0.5 | rmse | patchtst | 0.330 [0.126, 0.660] | 3/4 cells, 15/20 cell-seeds (vs prev_soh) | 0.117 | 4 | 5 | ef980b9c |
| loco | start_points | frac:0.5 | rmse | prev_soh | 0.461 [0.342, 0.562] |  | 0.443 | 4 | 5 | 0d396b2f |
| loco | start_points | frac:0.5 | rmse | rlinear | 0.346 [0.163, 0.621] | 3/4 cells, 13/20 cell-seeds (vs prev_soh) | 0.128 | 4 | 5 | bd5b08dc |
| loco | start_points | frac:0.5 | rmse | transformer | 2.902 [1.966, 4.099] | 0/4 cells, 3/20 cell-seeds (vs prev_soh) | 4.588 | 4 | 5 | 078809a4 |
| loco | start_points | frac:0.7 | rmse | dlinear | 0.371 [0.095, 0.774] | 2/4 cells, 10/20 cell-seeds (vs prev_soh) | 0.124 | 4 | 5 | 5ef63051 |
| loco | start_points | frac:0.7 | rmse | elasticnet | 0.487 [0.055, 0.919] | 1/4 cells, 5/20 cell-seeds (vs prev_soh) | 1.041 | 4 | 5 | c3c0651b |
| loco | start_points | frac:0.7 | rmse | gru | 2.058 [1.536, 2.576] | 0/4 cells, 3/20 cell-seeds (vs prev_soh) | 2.197 | 4 | 5 | dbed923e |
| loco | start_points | frac:0.7 | rmse | itransformer | 0.362 [0.100, 0.710] | 2/4 cells, 11/20 cell-seeds (vs prev_soh) | 0.304 | 4 | 5 | 48e8d64a |
| loco | start_points | frac:0.7 | rmse | itransformer_sc | 0.574 [0.150, 0.998] | 1/4 cells, 5/20 cell-seeds (vs prev_soh) | 0.778 | 4 | 5 | 197d4e36 |
| loco | start_points | frac:0.7 | rmse | lgbm | 0.374 [0.075, 0.784] | 2/4 cells, 10/20 cell-seeds (vs prev_soh) | 0.036 | 4 | 5 | e72f6de0 |
| loco | start_points | frac:0.7 | rmse | lstm | 0.881 [0.665, 1.190] | 0/4 cells, 5/20 cell-seeds (vs prev_soh) | 0.678 | 4 | 5 | 7e0af82e |
| loco | start_points | frac:0.7 | rmse | nlinear | 0.450 [0.234, 0.758] | 1/4 cells, 6/20 cell-seeds (vs prev_soh) | 0.360 | 4 | 5 | 1d4b3de0 |
| loco | start_points | frac:0.7 | rmse | patchtst | 0.488 [0.112, 1.029] | 1/4 cells, 7/20 cell-seeds (vs prev_soh) | 0.412 | 4 | 5 | ef980b9c |
| loco | start_points | frac:0.7 | rmse | prev_soh | 0.349 [0.104, 0.633] |  | 0.349 | 4 | 5 | 0d396b2f |
| loco | start_points | frac:0.7 | rmse | rlinear | 0.498 [0.132, 1.040] | 1/4 cells, 6/20 cell-seeds (vs prev_soh) | 0.405 | 4 | 5 | bd5b08dc |
| loco | start_points | frac:0.7 | rmse | transformer | 3.096 [2.141, 4.050] | 0/4 cells, 2/20 cell-seeds (vs prev_soh) | 4.335 | 4 | 5 | 078809a4 |
| loco | start_points | overall | rmse | dlinear | 0.379 [0.288, 0.536] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) | 0.323 | 4 | 5 | 5ef63051 |
| loco | start_points | overall | rmse | elasticnet | 0.621 [0.186, 1.254] | 3/4 cells, 15/20 cell-seeds (vs prev_soh) | 1.600 | 4 | 5 | c3c0651b |
| loco | start_points | overall | rmse | gru | 2.443 [2.083, 2.769] | 0/4 cells, 0/20 cell-seeds (vs prev_soh) | 2.363 | 4 | 5 | dbed923e |
| loco | start_points | overall | rmse | itransformer | 0.305 [0.142, 0.496] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) | 0.341 | 4 | 5 | 48e8d64a |
| loco | start_points | overall | rmse | itransformer_sc | 0.422 [0.191, 0.652] | 3/4 cells, 15/20 cell-seeds (vs prev_soh) | 0.602 | 4 | 5 | 197d4e36 |
| loco | start_points | overall | rmse | lgbm | 0.476 [0.304, 0.745] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) | 0.332 | 4 | 5 | e72f6de0 |
| loco | start_points | overall | rmse | lstm | 0.981 [0.831, 1.194] | 0/4 cells, 9/20 cell-seeds (vs prev_soh) | 0.817 | 4 | 5 | 7e0af82e |
| loco | start_points | overall | rmse | nlinear | 0.373 [0.281, 0.546] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) | 0.295 | 4 | 5 | 1d4b3de0 |
| loco | start_points | overall | rmse | patchtst | 0.399 [0.223, 0.651] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) | 0.356 | 4 | 5 | ef980b9c |
| loco | start_points | overall | rmse | prev_soh | 0.646 [0.506, 0.809] |  | 0.508 | 4 | 5 | 0d396b2f |
| loco | start_points | overall | rmse | rlinear | 0.406 [0.272, 0.647] | 4/4 cells, 20/20 cell-seeds (vs prev_soh) | 0.274 | 4 | 5 | bd5b08dc |
| loco | start_points | overall | rmse | transformer | 3.126 [2.610, 4.037] | 0/4 cells, 0/20 cell-seeds (vs prev_soh) | 4.509 | 4 | 5 | 078809a4 |

</details>

<details><summary>toyota_forecast (780 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rmse_h1 | dlinear | 0.136 [0.081, 0.200] | p=0.257 (vs last_slope) |  | 43 | 5 | 0b00c3d4 |
| test1 | all | overall | rmse_h1 | elasticnet | 0.134 [0.080, 0.197] | p=0.0143 (vs last_slope) |  | 43 | 5 | 4c070a82 |
| test1 | all | overall | rmse_h1 | gru | 0.176 [0.119, 0.242] | p=2.73e-12 (vs last_slope) |  | 43 | 5 | 74f02c88 |
| test1 | all | overall | rmse_h1 | itransformer | 0.124 [0.073, 0.183] | p=1.75e-11 (vs last_slope) |  | 43 | 5 | 0ce99716 |
| test1 | all | overall | rmse_h1 | itransformer_sc | 0.132 [0.078, 0.196] | p=5.84e-09 (vs last_slope) |  | 43 | 5 | aa089496 |
| test1 | all | overall | rmse_h1 | last_slope | 0.137 [0.081, 0.203] |  |  | 43 | 5 | c733fae1 |
| test1 | all | overall | rmse_h1 | lgbm | 0.133 [0.079, 0.197] | p=0.000139 (vs last_slope) |  | 43 | 5 | 7c413ce2 |
| test1 | all | overall | rmse_h1 | lstm | 0.140 [0.086, 0.203] | p=0.0571 (vs last_slope) |  | 43 | 5 | cc4f6edb |
| test1 | all | overall | rmse_h1 | nlinear | 0.134 [0.079, 0.198] | p=4.16e-09 (vs last_slope) |  | 43 | 5 | 60722fba |
| test1 | all | overall | rmse_h1 | patchtst | 0.130 [0.077, 0.193] | p=5.6e-05 (vs last_slope) |  | 43 | 5 | 73deb6e0 |
| test1 | all | overall | rmse_h1 | persistence | 0.158 [0.106, 0.219] | p=2.91e-05 (vs last_slope) |  | 43 | 5 | 84662b2e |
| test1 | all | overall | rmse_h1 | rlinear | 0.120 [0.074, 0.174] | p=0.0571 (vs last_slope) |  | 43 | 5 | ee0fc6f5 |
| test1 | all | overall | rmse_h1 | transformer | 0.186 [0.135, 0.246] | p=1.75e-11 (vs last_slope) |  | 43 | 5 | eb07a039 |
| test1 | all | overall | rmse_h10 | dlinear | 0.225 [0.164, 0.297] | p=0.000144 (vs last_slope) |  | 43 | 5 | 0b00c3d4 |
| test1 | all | overall | rmse_h10 | elasticnet | 0.197 [0.142, 0.261] | p=1.8e-10 (vs last_slope) |  | 43 | 5 | 4c070a82 |
| test1 | all | overall | rmse_h10 | gru | 0.177 [0.128, 0.233] | p=1.81e-07 (vs last_slope) |  | 43 | 5 | 74f02c88 |
| test1 | all | overall | rmse_h10 | itransformer | 0.157 [0.105, 0.216] | p=1.16e-09 (vs last_slope) |  | 43 | 5 | 0ce99716 |
| test1 | all | overall | rmse_h10 | itransformer_sc | 0.184 [0.129, 0.249] | p=4.38e-09 (vs last_slope) |  | 43 | 5 | aa089496 |
| test1 | all | overall | rmse_h10 | last_slope | 0.265 [0.184, 0.359] |  |  | 43 | 5 | c733fae1 |
| test1 | all | overall | rmse_h10 | lgbm | 0.175 [0.118, 0.242] | p=1.44e-09 (vs last_slope) |  | 43 | 5 | 7c413ce2 |
| test1 | all | overall | rmse_h10 | lstm | 0.177 [0.121, 0.243] | p=2.73e-12 (vs last_slope) |  | 43 | 5 | cc4f6edb |
| test1 | all | overall | rmse_h10 | nlinear | 0.212 [0.147, 0.289] | p=9.78e-11 (vs last_slope) |  | 43 | 5 | 60722fba |
| test1 | all | overall | rmse_h10 | patchtst | 0.173 [0.119, 0.236] | p=4.38e-09 (vs last_slope) |  | 43 | 5 | 73deb6e0 |
| test1 | all | overall | rmse_h10 | persistence | 0.600 [0.526, 0.679] | p=2.24e-08 (vs last_slope) |  | 43 | 5 | 84662b2e |
| test1 | all | overall | rmse_h10 | rlinear | 0.184 [0.132, 0.243] | p=6.25e-11 (vs last_slope) |  | 43 | 5 | ee0fc6f5 |
| test1 | all | overall | rmse_h10 | transformer | 0.212 [0.158, 0.276] | p=0.000879 (vs last_slope) |  | 43 | 5 | eb07a039 |
| test1 | all | overall | rmse_h100 | dlinear | 2.012 [1.660, 2.399] | p=2.19e-09 (vs last_slope) |  | 43 | 5 | 0b00c3d4 |
| test1 | all | overall | rmse_h100 | elasticnet | 1.536 [1.329, 1.749] | p=2.73e-12 (vs last_slope) |  | 43 | 5 | 4c070a82 |
| test1 | all | overall | rmse_h100 | gru | 1.091 [0.889, 1.334] | p=6.93e-10 (vs last_slope) |  | 43 | 5 | 74f02c88 |
| test1 | all | overall | rmse_h100 | itransformer | 0.947 [0.735, 1.243] | p=2.73e-12 (vs last_slope) |  | 43 | 5 | 0ce99716 |
| test1 | all | overall | rmse_h100 | itransformer_sc | 1.266 [1.012, 1.608] | p=4.5e-11 (vs last_slope) |  | 43 | 5 | aa089496 |
| test1 | all | overall | rmse_h100 | last_slope | 2.913 [2.388, 3.474] |  |  | 43 | 5 | c733fae1 |
| test1 | all | overall | rmse_h100 | lgbm | 0.980 [0.760, 1.288] | p=4.09e-12 (vs last_slope) |  | 43 | 5 | 7c413ce2 |
| test1 | all | overall | rmse_h100 | lstm | 1.083 [0.914, 1.270] | p=5.46e-12 (vs last_slope) |  | 43 | 5 | cc4f6edb |
| test1 | all | overall | rmse_h100 | nlinear | 1.858 [1.509, 2.248] | p=2.19e-09 (vs last_slope) |  | 43 | 5 | 60722fba |
| test1 | all | overall | rmse_h100 | patchtst | 1.249 [1.035, 1.560] | p=1.25e-10 (vs last_slope) |  | 43 | 5 | 73deb6e0 |
| test1 | all | overall | rmse_h100 | persistence | 4.332 [3.771, 4.975] | p=3.31e-06 (vs last_slope) |  | 43 | 5 | 84662b2e |
| test1 | all | overall | rmse_h100 | rlinear | 1.738 [1.410, 2.098] | p=1.11e-11 (vs last_slope) |  | 43 | 5 | ee0fc6f5 |
| test1 | all | overall | rmse_h100 | transformer | 1.134 [0.976, 1.301] | p=2.73e-12 (vs last_slope) |  | 43 | 5 | eb07a039 |
| test1 | all | overall | rmse_h200 | dlinear | 4.228 [3.731, 4.737] | p=5.46e-12 (vs last_slope) |  | 42 | 5 | 0b00c3d4 |
| test1 | all | overall | rmse_h200 | elasticnet | 3.001 [2.686, 3.329] | p=6.82e-12 (vs last_slope) |  | 42 | 5 | 4c070a82 |
| test1 | all | overall | rmse_h200 | gru | 2.780 [2.154, 3.675] | p=6e-09 (vs last_slope) |  | 42 | 5 | 74f02c88 |
| test1 | all | overall | rmse_h200 | itransformer | 2.503 [2.110, 2.902] | p=5.46e-12 (vs last_slope) |  | 42 | 5 | 0ce99716 |
| test1 | all | overall | rmse_h200 | itransformer_sc | 2.966 [2.550, 3.392] | p=6.37e-12 (vs last_slope) |  | 42 | 5 | aa089496 |
| test1 | all | overall | rmse_h200 | last_slope | 6.232 [5.167, 7.395] |  |  | 42 | 5 | c733fae1 |
| test1 | all | overall | rmse_h200 | lgbm | 2.184 [1.854, 2.526] | p=5.46e-12 (vs last_slope) |  | 42 | 5 | 7c413ce2 |
| test1 | all | overall | rmse_h200 | lstm | 2.656 [2.211, 3.206] | p=1.72e-09 (vs last_slope) |  | 42 | 5 | cc4f6edb |
| test1 | all | overall | rmse_h200 | nlinear | 3.965 [3.498, 4.446] | p=5.46e-12 (vs last_slope) |  | 42 | 5 | 60722fba |
| test1 | all | overall | rmse_h200 | patchtst | 2.909 [2.520, 3.307] | p=6.37e-12 (vs last_slope) |  | 42 | 5 | 73deb6e0 |
| test1 | all | overall | rmse_h200 | persistence | 6.443 [5.818, 7.082] | p=0.0225 (vs last_slope) |  | 42 | 5 | 84662b2e |
| test1 | all | overall | rmse_h200 | rlinear | 3.597 [3.008, 4.226] | p=6.82e-12 (vs last_slope) |  | 42 | 5 | ee0fc6f5 |
| test1 | all | overall | rmse_h200 | transformer | 2.626 [2.272, 2.996] | p=5.46e-12 (vs last_slope) |  | 42 | 5 | eb07a039 |
| test1 | all | overall | rmse_h50 | dlinear | 0.846 [0.721, 0.980] | p=2.6e-08 (vs last_slope) |  | 43 | 5 | 0b00c3d4 |
| test1 | all | overall | rmse_h50 | elasticnet | 0.655 [0.567, 0.746] | p=2.73e-12 (vs last_slope) |  | 43 | 5 | 4c070a82 |
| test1 | all | overall | rmse_h50 | gru | 0.475 [0.391, 0.569] | p=7.5e-11 (vs last_slope) |  | 43 | 5 | 74f02c88 |
| test1 | all | overall | rmse_h50 | itransformer | 0.402 [0.315, 0.514] | p=1.59e-11 (vs last_slope) |  | 43 | 5 | 0ce99716 |
| test1 | all | overall | rmse_h50 | itransformer_sc | 0.532 [0.434, 0.648] | p=1.92e-10 (vs last_slope) |  | 43 | 5 | aa089496 |
| test1 | all | overall | rmse_h50 | last_slope | 1.202 [0.954, 1.480] |  |  | 43 | 5 | c733fae1 |
| test1 | all | overall | rmse_h50 | lgbm | 0.451 [0.347, 0.586] | p=5.2e-10 (vs last_slope) |  | 43 | 5 | 7c413ce2 |
| test1 | all | overall | rmse_h50 | lstm | 0.501 [0.416, 0.591] | p=2.73e-12 (vs last_slope) |  | 43 | 5 | cc4f6edb |
| test1 | all | overall | rmse_h50 | nlinear | 0.766 [0.628, 0.912] | p=9.09e-12 (vs last_slope) |  | 43 | 5 | 60722fba |
| test1 | all | overall | rmse_h50 | patchtst | 0.537 [0.443, 0.649] | p=1.92e-10 (vs last_slope) |  | 43 | 5 | 73deb6e0 |
| test1 | all | overall | rmse_h50 | persistence | 2.502 [2.179, 2.849] | p=2.87e-08 (vs last_slope) |  | 43 | 5 | 84662b2e |
| test1 | all | overall | rmse_h50 | rlinear | 0.698 [0.574, 0.831] | p=2.73e-12 (vs last_slope) |  | 43 | 5 | ee0fc6f5 |
| test1 | all | overall | rmse_h50 | transformer | 0.513 [0.431, 0.599] | p=2.73e-12 (vs last_slope) |  | 43 | 5 | eb07a039 |
| test1 | start_points | fixed:100 | rmse_h1 | dlinear | 0.014 [0.010, 0.018] | p=0.000317 (vs last_slope) |  | 43 | 5 | 0b00c3d4 |
| test1 | start_points | fixed:100 | rmse_h1 | elasticnet | 0.012 [0.009, 0.016] | p=0.0461 (vs last_slope) |  | 43 | 5 | 4c070a82 |
| test1 | start_points | fixed:100 | rmse_h1 | gru | 0.026 [0.020, 0.033] | p=3.52e-07 (vs last_slope) |  | 43 | 5 | 74f02c88 |
| test1 | start_points | fixed:100 | rmse_h1 | itransformer | 0.010 [0.006, 0.014] | p=1 (vs last_slope) |  | 43 | 5 | 0ce99716 |
| test1 | start_points | fixed:100 | rmse_h1 | itransformer_sc | 0.010 [0.006, 0.015] | p=1 (vs last_slope) |  | 43 | 5 | aa089496 |
| test1 | start_points | fixed:100 | rmse_h1 | last_slope | 0.010 [0.006, 0.015] |  |  | 43 | 5 | c733fae1 |
| test1 | start_points | fixed:100 | rmse_h1 | lgbm | 0.010 [0.006, 0.014] | p=1 (vs last_slope) |  | 43 | 5 | 7c413ce2 |
| test1 | start_points | fixed:100 | rmse_h1 | lstm | 0.014 [0.011, 0.018] | p=0.00104 (vs last_slope) |  | 43 | 5 | cc4f6edb |
| test1 | start_points | fixed:100 | rmse_h1 | nlinear | 0.011 [0.007, 0.015] | p=0.413 (vs last_slope) |  | 43 | 5 | 60722fba |
| test1 | start_points | fixed:100 | rmse_h1 | patchtst | 0.010 [0.006, 0.014] | p=1 (vs last_slope) |  | 43 | 5 | 73deb6e0 |
| test1 | start_points | fixed:100 | rmse_h1 | persistence | 0.012 [0.008, 0.017] | p=1 (vs last_slope) |  | 43 | 5 | 84662b2e |
| test1 | start_points | fixed:100 | rmse_h1 | rlinear | 0.012 [0.008, 0.017] | p=0.00164 (vs last_slope) |  | 43 | 5 | ee0fc6f5 |
| test1 | start_points | fixed:100 | rmse_h1 | transformer | 0.063 [0.059, 0.067] | p=2.73e-12 (vs last_slope) |  | 43 | 5 | eb07a039 |
| test1 | start_points | fixed:100 | rmse_h10 | dlinear | 0.039 [0.033, 0.047] | p=8.34e-06 (vs last_slope) |  | 43 | 5 | 0b00c3d4 |
| test1 | start_points | fixed:100 | rmse_h10 | elasticnet | 0.032 [0.024, 0.043] | p=0.163 (vs last_slope) |  | 43 | 5 | 4c070a82 |
| test1 | start_points | fixed:100 | rmse_h10 | gru | 0.033 [0.026, 0.041] | p=0.00717 (vs last_slope) |  | 43 | 5 | 74f02c88 |
| test1 | start_points | fixed:100 | rmse_h10 | itransformer | 0.021 [0.012, 0.035] | p=1 (vs last_slope) |  | 43 | 5 | 0ce99716 |
| test1 | start_points | fixed:100 | rmse_h10 | itransformer_sc | 0.018 [0.012, 0.024] | p=0.769 (vs last_slope) |  | 43 | 5 | aa089496 |
| test1 | start_points | fixed:100 | rmse_h10 | last_slope | 0.024 [0.015, 0.035] |  |  | 43 | 5 | c733fae1 |
| test1 | start_points | fixed:100 | rmse_h10 | lgbm | 0.025 [0.013, 0.043] | p=1 (vs last_slope) |  | 43 | 5 | 7c413ce2 |
| test1 | start_points | fixed:100 | rmse_h10 | lstm | 0.024 [0.017, 0.033] | p=1 (vs last_slope) |  | 43 | 5 | cc4f6edb |
| test1 | start_points | fixed:100 | rmse_h10 | nlinear | 0.017 [0.011, 0.024] | p=0.277 (vs last_slope) |  | 43 | 5 | 60722fba |
| test1 | start_points | fixed:100 | rmse_h10 | patchtst | 0.017 [0.010, 0.026] | p=0.0999 (vs last_slope) |  | 43 | 5 | 73deb6e0 |
| test1 | start_points | fixed:100 | rmse_h10 | persistence | 0.103 [0.054, 0.182] | p=7.89e-08 (vs last_slope) |  | 43 | 5 | 84662b2e |
| test1 | start_points | fixed:100 | rmse_h10 | rlinear | 0.018 [0.012, 0.026] | p=0.45 (vs last_slope) |  | 43 | 5 | ee0fc6f5 |
| test1 | start_points | fixed:100 | rmse_h10 | transformer | 0.057 [0.048, 0.068] | p=1.17e-10 (vs last_slope) |  | 43 | 5 | eb07a039 |
| test1 | start_points | fixed:100 | rmse_h100 | dlinear | 0.381 [0.356, 0.408] | p=0.00336 (vs last_slope) |  | 42 | 5 | 0b00c3d4 |
| test1 | start_points | fixed:100 | rmse_h100 | elasticnet | 0.459 [0.332, 0.613] | p=0.00586 (vs last_slope) |  | 42 | 5 | 4c070a82 |
| test1 | start_points | fixed:100 | rmse_h100 | gru | 0.235 [0.152, 0.351] | p=1 (vs last_slope) |  | 42 | 5 | 74f02c88 |
| test1 | start_points | fixed:100 | rmse_h100 | itransformer | 0.161 [0.119, 0.208] | p=0.0254 (vs last_slope) |  | 42 | 5 | 0ce99716 |
| test1 | start_points | fixed:100 | rmse_h100 | itransformer_sc | 0.281 [0.193, 0.386] | p=1 (vs last_slope) |  | 42 | 5 | aa089496 |
| test1 | start_points | fixed:100 | rmse_h100 | last_slope | 0.250 [0.172, 0.347] |  |  | 42 | 5 | c733fae1 |
| test1 | start_points | fixed:100 | rmse_h100 | lgbm | 0.133 [0.096, 0.175] | p=0.013 (vs last_slope) |  | 42 | 5 | 7c413ce2 |
| test1 | start_points | fixed:100 | rmse_h100 | lstm | 0.254 [0.151, 0.408] | p=1 (vs last_slope) |  | 42 | 5 | cc4f6edb |
| test1 | start_points | fixed:100 | rmse_h100 | nlinear | 0.219 [0.189, 0.251] | p=1 (vs last_slope) |  | 42 | 5 | 60722fba |
| test1 | start_points | fixed:100 | rmse_h100 | patchtst | 0.256 [0.175, 0.358] | p=1 (vs last_slope) |  | 42 | 5 | 73deb6e0 |
| test1 | start_points | fixed:100 | rmse_h100 | persistence | 0.867 [0.644, 1.149] | p=1.13e-09 (vs last_slope) |  | 42 | 5 | 84662b2e |
| test1 | start_points | fixed:100 | rmse_h100 | rlinear | 0.197 [0.154, 0.242] | p=1 (vs last_slope) |  | 42 | 5 | ee0fc6f5 |
| test1 | start_points | fixed:100 | rmse_h100 | transformer | 0.250 [0.177, 0.343] | p=1 (vs last_slope) |  | 42 | 5 | eb07a039 |
| test1 | start_points | fixed:100 | rmse_h200 | dlinear | 0.991 [0.815, 1.246] | p=0.96 (vs last_slope) |  | 42 | 5 | 0b00c3d4 |
| test1 | start_points | fixed:100 | rmse_h200 | elasticnet | 1.359 [0.999, 1.783] | p=0.155 (vs last_slope) |  | 42 | 5 | 4c070a82 |
| test1 | start_points | fixed:100 | rmse_h200 | gru | 0.910 [0.502, 1.521] | p=0.0199 (vs last_slope) |  | 42 | 5 | 74f02c88 |
| test1 | start_points | fixed:100 | rmse_h200 | itransformer | 0.587 [0.414, 0.792] | p=0.00521 (vs last_slope) |  | 42 | 5 | 0ce99716 |
| test1 | start_points | fixed:100 | rmse_h200 | itransformer_sc | 0.849 [0.649, 1.088] | p=0.587 (vs last_slope) |  | 42 | 5 | aa089496 |
| test1 | start_points | fixed:100 | rmse_h200 | last_slope | 0.913 [0.687, 1.195] |  |  | 42 | 5 | c733fae1 |
| test1 | start_points | fixed:100 | rmse_h200 | lgbm | 0.576 [0.373, 0.834] | p=0.0114 (vs last_slope) |  | 42 | 5 | 7c413ce2 |
| test1 | start_points | fixed:100 | rmse_h200 | lstm | 0.824 [0.456, 1.369] | p=0.0482 (vs last_slope) |  | 42 | 5 | cc4f6edb |
| test1 | start_points | fixed:100 | rmse_h200 | nlinear | 0.930 [0.710, 1.192] | p=0.96 (vs last_slope) |  | 42 | 5 | 60722fba |
| test1 | start_points | fixed:100 | rmse_h200 | patchtst | 0.854 [0.590, 1.164] | p=0.579 (vs last_slope) |  | 42 | 5 | 73deb6e0 |
| test1 | start_points | fixed:100 | rmse_h200 | persistence | 2.152 [1.644, 2.794] | p=9.22e-10 (vs last_slope) |  | 42 | 5 | 84662b2e |
| test1 | start_points | fixed:100 | rmse_h200 | rlinear | 0.674 [0.498, 0.860] | p=0.168 (vs last_slope) |  | 42 | 5 | ee0fc6f5 |
| test1 | start_points | fixed:100 | rmse_h200 | transformer | 0.717 [0.455, 1.056] | p=0.0482 (vs last_slope) |  | 42 | 5 | eb07a039 |
| test1 | start_points | fixed:100 | rmse_h50 | dlinear | 0.358 [0.330, 0.383] | p=3.8e-06 (vs last_slope) |  | 43 | 5 | 0b00c3d4 |
| test1 | start_points | fixed:100 | rmse_h50 | elasticnet | 0.179 [0.126, 0.241] | p=0.0659 (vs last_slope) |  | 43 | 5 | 4c070a82 |
| test1 | start_points | fixed:100 | rmse_h50 | gru | 0.137 [0.070, 0.250] | p=1 (vs last_slope) |  | 43 | 5 | 74f02c88 |
| test1 | start_points | fixed:100 | rmse_h50 | itransformer | 0.101 [0.040, 0.209] | p=0.144 (vs last_slope) |  | 43 | 5 | 0ce99716 |
| test1 | start_points | fixed:100 | rmse_h50 | itransformer_sc | 0.090 [0.064, 0.121] | p=1 (vs last_slope) |  | 43 | 5 | aa089496 |
| test1 | start_points | fixed:100 | rmse_h50 | last_slope | 0.135 [0.065, 0.248] |  |  | 43 | 5 | c733fae1 |
| test1 | start_points | fixed:100 | rmse_h50 | lgbm | 0.132 [0.041, 0.295] | p=0.359 (vs last_slope) |  | 43 | 5 | 7c413ce2 |
| test1 | start_points | fixed:100 | rmse_h50 | lstm | 0.115 [0.064, 0.185] | p=1 (vs last_slope) |  | 43 | 5 | cc4f6edb |
| test1 | start_points | fixed:100 | rmse_h50 | nlinear | 0.071 [0.050, 0.097] | p=0.579 (vs last_slope) |  | 43 | 5 | 60722fba |
| test1 | start_points | fixed:100 | rmse_h50 | patchtst | 0.099 [0.055, 0.170] | p=0.837 (vs last_slope) |  | 43 | 5 | 73deb6e0 |
| test1 | start_points | fixed:100 | rmse_h50 | persistence | 0.576 [0.302, 1.024] | p=6.9e-10 (vs last_slope) |  | 43 | 5 | 84662b2e |
| test1 | start_points | fixed:100 | rmse_h50 | rlinear | 0.065 [0.049, 0.082] | p=0.408 (vs last_slope) |  | 43 | 5 | ee0fc6f5 |
| test1 | start_points | fixed:100 | rmse_h50 | transformer | 0.135 [0.093, 0.190] | p=0.408 (vs last_slope) |  | 43 | 5 | eb07a039 |
| test1 | start_points | frac:0.3 | rmse_h1 | dlinear | 0.019 [0.013, 0.026] | p=0.987 (vs persistence) |  | 43 | 5 | 0b00c3d4 |
| test1 | start_points | frac:0.3 | rmse_h1 | elasticnet | 0.016 [0.011, 0.024] | p=0.384 (vs persistence) |  | 43 | 5 | 4c070a82 |
| test1 | start_points | frac:0.3 | rmse_h1 | gru | 0.048 [0.028, 0.075] | p=7.73e-06 (vs persistence) |  | 43 | 5 | 74f02c88 |
| test1 | start_points | frac:0.3 | rmse_h1 | itransformer | 0.016 [0.010, 0.022] | p=0.0939 (vs persistence) |  | 43 | 5 | 0ce99716 |
| test1 | start_points | frac:0.3 | rmse_h1 | itransformer_sc | 0.017 [0.011, 0.024] | p=0.0896 (vs persistence) |  | 43 | 5 | aa089496 |
| test1 | start_points | frac:0.3 | rmse_h1 | last_slope | 0.023 [0.014, 0.036] | p=0.987 (vs persistence) |  | 43 | 5 | c733fae1 |
| test1 | start_points | frac:0.3 | rmse_h1 | lgbm | 0.015 [0.010, 0.023] | p=0.0162 (vs persistence) |  | 43 | 5 | 7c413ce2 |
| test1 | start_points | frac:0.3 | rmse_h1 | lstm | 0.028 [0.016, 0.045] | p=0.987 (vs persistence) |  | 43 | 5 | cc4f6edb |
| test1 | start_points | frac:0.3 | rmse_h1 | nlinear | 0.016 [0.011, 0.023] | p=0.277 (vs persistence) |  | 43 | 5 | 60722fba |
| test1 | start_points | frac:0.3 | rmse_h1 | patchtst | 0.016 [0.010, 0.024] | p=0.0617 (vs persistence) |  | 43 | 5 | 73deb6e0 |
| test1 | start_points | frac:0.3 | rmse_h1 | persistence | 0.021 [0.014, 0.031] |  |  | 43 | 5 | 84662b2e |
| test1 | start_points | frac:0.3 | rmse_h1 | rlinear | 0.024 [0.014, 0.036] | p=0.987 (vs persistence) |  | 43 | 5 | ee0fc6f5 |
| test1 | start_points | frac:0.3 | rmse_h1 | transformer | 0.070 [0.060, 0.083] | p=9e-11 (vs persistence) |  | 43 | 5 | eb07a039 |
| test1 | start_points | frac:0.3 | rmse_h10 | dlinear | 0.073 [0.046, 0.106] | p=1 (vs last_slope) |  | 43 | 5 | 0b00c3d4 |
| test1 | start_points | frac:0.3 | rmse_h10 | elasticnet | 0.070 [0.042, 0.107] | p=1 (vs last_slope) |  | 43 | 5 | 4c070a82 |
| test1 | start_points | frac:0.3 | rmse_h10 | gru | 0.061 [0.038, 0.090] | p=1 (vs last_slope) |  | 43 | 5 | 74f02c88 |
| test1 | start_points | frac:0.3 | rmse_h10 | itransformer | 0.046 [0.024, 0.075] | p=0.00139 (vs last_slope) |  | 43 | 5 | 0ce99716 |
| test1 | start_points | frac:0.3 | rmse_h10 | itransformer_sc | 0.058 [0.030, 0.093] | p=0.12 (vs last_slope) |  | 43 | 5 | aa089496 |
| test1 | start_points | frac:0.3 | rmse_h10 | last_slope | 0.126 [0.044, 0.263] |  |  | 43 | 5 | c733fae1 |
| test1 | start_points | frac:0.3 | rmse_h10 | lgbm | 0.054 [0.030, 0.083] | p=0.175 (vs last_slope) |  | 43 | 5 | 7c413ce2 |
| test1 | start_points | frac:0.3 | rmse_h10 | lstm | 0.057 [0.033, 0.088] | p=0.394 (vs last_slope) |  | 43 | 5 | cc4f6edb |
| test1 | start_points | frac:0.3 | rmse_h10 | nlinear | 0.060 [0.031, 0.097] | p=0.0507 (vs last_slope) |  | 43 | 5 | 60722fba |
| test1 | start_points | frac:0.3 | rmse_h10 | patchtst | 0.051 [0.027, 0.082] | p=0.0163 (vs last_slope) |  | 43 | 5 | 73deb6e0 |
| test1 | start_points | frac:0.3 | rmse_h10 | persistence | 0.139 [0.092, 0.204] | p=0.0266 (vs last_slope) |  | 43 | 5 | 84662b2e |
| test1 | start_points | frac:0.3 | rmse_h10 | rlinear | 0.053 [0.032, 0.080] | p=0.0266 (vs last_slope) |  | 43 | 5 | ee0fc6f5 |
| test1 | start_points | frac:0.3 | rmse_h10 | transformer | 0.084 [0.057, 0.120] | p=0.561 (vs last_slope) |  | 43 | 5 | eb07a039 |
| test1 | start_points | frac:0.3 | rmse_h100 | dlinear | 0.621 [0.417, 0.934] | p=0.689 (vs last_slope) |  | 43 | 5 | 0b00c3d4 |
| test1 | start_points | frac:0.3 | rmse_h100 | elasticnet | 0.912 [0.654, 1.223] | p=0.352 (vs last_slope) |  | 43 | 5 | 4c070a82 |
| test1 | start_points | frac:0.3 | rmse_h100 | gru | 0.478 [0.277, 0.751] | p=0.00831 (vs last_slope) |  | 43 | 5 | 74f02c88 |
| test1 | start_points | frac:0.3 | rmse_h100 | itransformer | 0.289 [0.203, 0.400] | p=0.000492 (vs last_slope) |  | 43 | 5 | 0ce99716 |
| test1 | start_points | frac:0.3 | rmse_h100 | itransformer_sc | 0.543 [0.333, 0.814] | p=0.0624 (vs last_slope) |  | 43 | 5 | aa089496 |
| test1 | start_points | frac:0.3 | rmse_h100 | last_slope | 1.226 [0.486, 2.447] |  |  | 43 | 5 | c733fae1 |
| test1 | start_points | frac:0.3 | rmse_h100 | lgbm | 0.372 [0.175, 0.681] | p=0.000969 (vs last_slope) |  | 43 | 5 | 7c413ce2 |
| test1 | start_points | frac:0.3 | rmse_h100 | lstm | 0.483 [0.289, 0.724] | p=0.0287 (vs last_slope) |  | 43 | 5 | cc4f6edb |
| test1 | start_points | frac:0.3 | rmse_h100 | nlinear | 0.519 [0.310, 0.823] | p=0.249 (vs last_slope) |  | 43 | 5 | 60722fba |
| test1 | start_points | frac:0.3 | rmse_h100 | patchtst | 0.380 [0.253, 0.550] | p=0.0287 (vs last_slope) |  | 43 | 5 | 73deb6e0 |
| test1 | start_points | frac:0.3 | rmse_h100 | persistence | 1.432 [0.942, 2.189] | p=0.000618 (vs last_slope) |  | 43 | 5 | 84662b2e |
| test1 | start_points | frac:0.3 | rmse_h100 | rlinear | 0.434 [0.270, 0.679] | p=0.0761 (vs last_slope) |  | 43 | 5 | ee0fc6f5 |
| test1 | start_points | frac:0.3 | rmse_h100 | transformer | 0.467 [0.295, 0.663] | p=0.0444 (vs last_slope) |  | 43 | 5 | eb07a039 |
| test1 | start_points | frac:0.3 | rmse_h200 | dlinear | 1.180 [1.002, 1.430] | p=0.098 (vs last_slope) |  | 42 | 5 | 0b00c3d4 |
| test1 | start_points | frac:0.3 | rmse_h200 | elasticnet | 1.909 [1.483, 2.418] | p=0.638 (vs last_slope) |  | 42 | 5 | 4c070a82 |
| test1 | start_points | frac:0.3 | rmse_h200 | gru | 1.448 [0.728, 2.570] | p=0.0209 (vs last_slope) |  | 42 | 5 | 74f02c88 |
| test1 | start_points | frac:0.3 | rmse_h200 | itransformer | 0.921 [0.662, 1.209] | p=0.00163 (vs last_slope) |  | 42 | 5 | 0ce99716 |
| test1 | start_points | frac:0.3 | rmse_h200 | itransformer_sc | 1.256 [0.938, 1.619] | p=0.0957 (vs last_slope) |  | 42 | 5 | aa089496 |
| test1 | start_points | frac:0.3 | rmse_h200 | last_slope | 2.764 [1.374, 5.062] |  |  | 42 | 5 | c733fae1 |
| test1 | start_points | frac:0.3 | rmse_h200 | lgbm | 0.897 [0.530, 1.352] | p=0.0015 (vs last_slope) |  | 42 | 5 | 7c413ce2 |
| test1 | start_points | frac:0.3 | rmse_h200 | lstm | 1.290 [0.733, 2.047] | p=0.0778 (vs last_slope) |  | 42 | 5 | cc4f6edb |
| test1 | start_points | frac:0.3 | rmse_h200 | nlinear | 1.079 [0.861, 1.339] | p=0.0957 (vs last_slope) |  | 42 | 5 | 60722fba |
| test1 | start_points | frac:0.3 | rmse_h200 | patchtst | 1.275 [0.953, 1.634] | p=0.098 (vs last_slope) |  | 42 | 5 | 73deb6e0 |
| test1 | start_points | frac:0.3 | rmse_h200 | persistence | 2.821 [2.267, 3.472] | p=0.000307 (vs last_slope) |  | 42 | 5 | 84662b2e |
| test1 | start_points | frac:0.3 | rmse_h200 | rlinear | 1.279 [0.952, 1.670] | p=0.098 (vs last_slope) |  | 42 | 5 | ee0fc6f5 |
| test1 | start_points | frac:0.3 | rmse_h200 | transformer | 1.158 [0.739, 1.671] | p=0.098 (vs last_slope) |  | 42 | 5 | eb07a039 |
| test1 | start_points | frac:0.3 | rmse_h50 | dlinear | 0.374 [0.321, 0.450] | p=0.00938 (vs last_slope) |  | 43 | 5 | 0b00c3d4 |
| test1 | start_points | frac:0.3 | rmse_h50 | elasticnet | 0.311 [0.226, 0.412] | p=0.329 (vs last_slope) |  | 43 | 5 | 4c070a82 |
| test1 | start_points | frac:0.3 | rmse_h50 | gru | 0.173 [0.095, 0.274] | p=0.00683 (vs last_slope) |  | 43 | 5 | 74f02c88 |
| test1 | start_points | frac:0.3 | rmse_h50 | itransformer | 0.093 [0.066, 0.129] | p=0.000159 (vs last_slope) |  | 43 | 5 | 0ce99716 |
| test1 | start_points | frac:0.3 | rmse_h50 | itransformer_sc | 0.170 [0.102, 0.268] | p=0.0597 (vs last_slope) |  | 43 | 5 | aa089496 |
| test1 | start_points | frac:0.3 | rmse_h50 | last_slope | 0.518 [0.188, 1.077] |  |  | 43 | 5 | c733fae1 |
| test1 | start_points | frac:0.3 | rmse_h50 | lgbm | 0.120 [0.059, 0.219] | p=0.000657 (vs last_slope) |  | 43 | 5 | 7c413ce2 |
| test1 | start_points | frac:0.3 | rmse_h50 | lstm | 0.139 [0.090, 0.202] | p=0.0174 (vs last_slope) |  | 43 | 5 | cc4f6edb |
| test1 | start_points | frac:0.3 | rmse_h50 | nlinear | 0.169 [0.105, 0.259] | p=0.0597 (vs last_slope) |  | 43 | 5 | 60722fba |
| test1 | start_points | frac:0.3 | rmse_h50 | patchtst | 0.124 [0.075, 0.200] | p=0.00938 (vs last_slope) |  | 43 | 5 | 73deb6e0 |
| test1 | start_points | frac:0.3 | rmse_h50 | persistence | 0.614 [0.405, 0.926] | p=0.00081 (vs last_slope) |  | 43 | 5 | 84662b2e |
| test1 | start_points | frac:0.3 | rmse_h50 | rlinear | 0.149 [0.100, 0.217] | p=0.0343 (vs last_slope) |  | 43 | 5 | ee0fc6f5 |
| test1 | start_points | frac:0.3 | rmse_h50 | transformer | 0.164 [0.113, 0.230] | p=0.0597 (vs last_slope) |  | 43 | 5 | eb07a039 |
| test1 | start_points | frac:0.5 | rmse_h1 | dlinear | 0.050 [0.029, 0.075] | p=1 (vs persistence) |  | 43 | 5 | 0b00c3d4 |
| test1 | start_points | frac:0.5 | rmse_h1 | elasticnet | 0.032 [0.019, 0.050] | p=1 (vs persistence) |  | 43 | 5 | 4c070a82 |
| test1 | start_points | frac:0.5 | rmse_h1 | gru | 0.097 [0.055, 0.152] | p=9.99e-07 (vs persistence) |  | 43 | 5 | 74f02c88 |
| test1 | start_points | frac:0.5 | rmse_h1 | itransformer | 0.036 [0.021, 0.055] | p=1 (vs persistence) |  | 43 | 5 | 0ce99716 |
| test1 | start_points | frac:0.5 | rmse_h1 | itransformer_sc | 0.033 [0.020, 0.052] | p=1 (vs persistence) |  | 43 | 5 | aa089496 |
| test1 | start_points | frac:0.5 | rmse_h1 | last_slope | 0.053 [0.024, 0.091] | p=1 (vs persistence) |  | 43 | 5 | c733fae1 |
| test1 | start_points | frac:0.5 | rmse_h1 | lgbm | 0.029 [0.017, 0.047] | p=1 (vs persistence) |  | 43 | 5 | 7c413ce2 |
| test1 | start_points | frac:0.5 | rmse_h1 | lstm | 0.052 [0.031, 0.077] | p=1 (vs persistence) |  | 43 | 5 | cc4f6edb |
| test1 | start_points | frac:0.5 | rmse_h1 | nlinear | 0.033 [0.020, 0.051] | p=1 (vs persistence) |  | 43 | 5 | 60722fba |
| test1 | start_points | frac:0.5 | rmse_h1 | patchtst | 0.031 [0.018, 0.048] | p=1 (vs persistence) |  | 43 | 5 | 73deb6e0 |
| test1 | start_points | frac:0.5 | rmse_h1 | persistence | 0.033 [0.021, 0.051] |  |  | 43 | 5 | 84662b2e |
| test1 | start_points | frac:0.5 | rmse_h1 | rlinear | 0.091 [0.037, 0.160] | p=1 (vs persistence) |  | 43 | 5 | ee0fc6f5 |
| test1 | start_points | frac:0.5 | rmse_h1 | transformer | 0.098 [0.073, 0.128] | p=6.48e-09 (vs persistence) |  | 43 | 5 | eb07a039 |
| test1 | start_points | frac:0.5 | rmse_h10 | dlinear | 0.089 [0.067, 0.113] | p=0.0483 (vs persistence) |  | 43 | 5 | 0b00c3d4 |
| test1 | start_points | frac:0.5 | rmse_h10 | elasticnet | 0.101 [0.070, 0.141] | p=0.116 (vs persistence) |  | 43 | 5 | 4c070a82 |
| test1 | start_points | frac:0.5 | rmse_h10 | gru | 0.104 [0.066, 0.152] | p=0.0426 (vs persistence) |  | 43 | 5 | 74f02c88 |
| test1 | start_points | frac:0.5 | rmse_h10 | itransformer | 0.060 [0.042, 0.081] | p=0.000524 (vs persistence) |  | 43 | 5 | 0ce99716 |
| test1 | start_points | frac:0.5 | rmse_h10 | itransformer_sc | 0.080 [0.054, 0.113] | p=0.0113 (vs persistence) |  | 43 | 5 | aa089496 |
| test1 | start_points | frac:0.5 | rmse_h10 | last_slope | 0.312 [0.081, 0.659] | p=0.189 (vs persistence) |  | 43 | 5 | c733fae1 |
| test1 | start_points | frac:0.5 | rmse_h10 | lgbm | 0.084 [0.050, 0.131] | p=0.0106 (vs persistence) |  | 43 | 5 | 7c413ce2 |
| test1 | start_points | frac:0.5 | rmse_h10 | lstm | 0.107 [0.061, 0.180] | p=0.0426 (vs persistence) |  | 43 | 5 | cc4f6edb |
| test1 | start_points | frac:0.5 | rmse_h10 | nlinear | 0.064 [0.047, 0.083] | p=0.00759 (vs persistence) |  | 43 | 5 | 60722fba |
| test1 | start_points | frac:0.5 | rmse_h10 | patchtst | 0.055 [0.040, 0.072] | p=0.000699 (vs persistence) |  | 43 | 5 | 73deb6e0 |
| test1 | start_points | frac:0.5 | rmse_h10 | persistence | 0.160 [0.111, 0.230] |  |  | 43 | 5 | 84662b2e |
| test1 | start_points | frac:0.5 | rmse_h10 | rlinear | 0.138 [0.059, 0.246] | p=0.0597 (vs persistence) |  | 43 | 5 | ee0fc6f5 |
| test1 | start_points | frac:0.5 | rmse_h10 | transformer | 0.114 [0.090, 0.143] | p=0.189 (vs persistence) |  | 43 | 5 | eb07a039 |
| test1 | start_points | frac:0.5 | rmse_h100 | dlinear | 0.486 [0.430, 0.547] | p=5.46e-11 (vs persistence) |  | 42 | 5 | 0b00c3d4 |
| test1 | start_points | frac:0.5 | rmse_h100 | elasticnet | 1.239 [0.897, 1.651] | p=0.00152 (vs persistence) |  | 42 | 5 | 4c070a82 |
| test1 | start_points | frac:0.5 | rmse_h100 | gru | 0.838 [0.491, 1.276] | p=3.42e-06 (vs persistence) |  | 42 | 5 | 74f02c88 |
| test1 | start_points | frac:0.5 | rmse_h100 | itransformer | 0.605 [0.375, 0.875] | p=9.72e-09 (vs persistence) |  | 42 | 5 | 0ce99716 |
| test1 | start_points | frac:0.5 | rmse_h100 | itransformer_sc | 0.774 [0.447, 1.219] | p=1.65e-07 (vs persistence) |  | 42 | 5 | aa089496 |
| test1 | start_points | frac:0.5 | rmse_h100 | last_slope | 2.997 [0.668, 6.602] | p=0.00152 (vs persistence) |  | 42 | 5 | c733fae1 |
| test1 | start_points | frac:0.5 | rmse_h100 | lgbm | 0.611 [0.363, 0.924] | p=6.84e-07 (vs persistence) |  | 42 | 5 | 7c413ce2 |
| test1 | start_points | frac:0.5 | rmse_h100 | lstm | 0.841 [0.517, 1.228] | p=2.85e-06 (vs persistence) |  | 42 | 5 | cc4f6edb |
| test1 | start_points | frac:0.5 | rmse_h100 | nlinear | 0.399 [0.309, 0.494] | p=7e-11 (vs persistence) |  | 42 | 5 | 60722fba |
| test1 | start_points | frac:0.5 | rmse_h100 | patchtst | 0.501 [0.348, 0.675] | p=2.5e-10 (vs persistence) |  | 42 | 5 | 73deb6e0 |
| test1 | start_points | frac:0.5 | rmse_h100 | persistence | 1.779 [1.495, 2.097] |  |  | 42 | 5 | 84662b2e |
| test1 | start_points | frac:0.5 | rmse_h100 | rlinear | 1.012 [0.535, 1.597] | p=0.000616 (vs persistence) |  | 42 | 5 | ee0fc6f5 |
| test1 | start_points | frac:0.5 | rmse_h100 | transformer | 0.864 [0.538, 1.243] | p=3.42e-06 (vs persistence) |  | 42 | 5 | eb07a039 |
| test1 | start_points | frac:0.5 | rmse_h200 | dlinear | 3.401 [2.593, 4.246] | p=5.46e-11 (vs persistence) |  | 41 | 5 | 0b00c3d4 |
| test1 | start_points | frac:0.5 | rmse_h200 | elasticnet | 2.237 [1.749, 2.775] | p=8.96e-08 (vs persistence) |  | 41 | 5 | 4c070a82 |
| test1 | start_points | frac:0.5 | rmse_h200 | gru | 2.700 [1.904, 3.819] | p=8.96e-08 (vs persistence) |  | 41 | 5 | 74f02c88 |
| test1 | start_points | frac:0.5 | rmse_h200 | itransformer | 2.280 [1.599, 3.056] | p=5.54e-09 (vs persistence) |  | 41 | 5 | 0ce99716 |
| test1 | start_points | frac:0.5 | rmse_h200 | itransformer_sc | 2.792 [1.961, 3.761] | p=1.69e-08 (vs persistence) |  | 41 | 5 | aa089496 |
| test1 | start_points | frac:0.5 | rmse_h200 | last_slope | 8.282 [3.534, 15.660] | p=0.000168 (vs persistence) |  | 41 | 5 | c733fae1 |
| test1 | start_points | frac:0.5 | rmse_h200 | lgbm | 1.646 [1.234, 2.077] | p=1.9e-10 (vs persistence) |  | 41 | 5 | 7c413ce2 |
| test1 | start_points | frac:0.5 | rmse_h200 | lstm | 2.459 [1.844, 3.166] | p=8.09e-09 (vs persistence) |  | 41 | 5 | cc4f6edb |
| test1 | start_points | frac:0.5 | rmse_h200 | nlinear | 3.099 [2.340, 3.897] | p=3e-10 (vs persistence) |  | 41 | 5 | 60722fba |
| test1 | start_points | frac:0.5 | rmse_h200 | patchtst | 2.676 [2.029, 3.404] | p=6.81e-09 (vs persistence) |  | 41 | 5 | 73deb6e0 |
| test1 | start_points | frac:0.5 | rmse_h200 | persistence | 6.269 [5.184, 7.368] |  |  | 41 | 5 | 84662b2e |
| test1 | start_points | frac:0.5 | rmse_h200 | rlinear | 3.614 [2.429, 4.971] | p=1.59e-05 (vs persistence) |  | 41 | 5 | ee0fc6f5 |
| test1 | start_points | frac:0.5 | rmse_h200 | transformer | 2.319 [1.799, 2.891] | p=1.38e-09 (vs persistence) |  | 41 | 5 | eb07a039 |
| test1 | start_points | frac:0.5 | rmse_h50 | dlinear | 0.335 [0.295, 0.379] | p=1.74e-06 (vs persistence) |  | 43 | 5 | 0b00c3d4 |
| test1 | start_points | frac:0.5 | rmse_h50 | elasticnet | 0.575 [0.382, 0.823] | p=0.00176 (vs persistence) |  | 43 | 5 | 4c070a82 |
| test1 | start_points | frac:0.5 | rmse_h50 | gru | 0.352 [0.197, 0.550] | p=2.31e-05 (vs persistence) |  | 43 | 5 | 74f02c88 |
| test1 | start_points | frac:0.5 | rmse_h50 | itransformer | 0.211 [0.134, 0.300] | p=3.12e-10 (vs persistence) |  | 43 | 5 | 0ce99716 |
| test1 | start_points | frac:0.5 | rmse_h50 | itransformer_sc | 0.342 [0.191, 0.540] | p=1.04e-07 (vs persistence) |  | 43 | 5 | aa089496 |
| test1 | start_points | frac:0.5 | rmse_h50 | last_slope | 1.439 [0.291, 3.185] | p=0.00176 (vs persistence) |  | 43 | 5 | c733fae1 |
| test1 | start_points | frac:0.5 | rmse_h50 | lgbm | 0.324 [0.184, 0.499] | p=2.21e-06 (vs persistence) |  | 43 | 5 | 7c413ce2 |
| test1 | start_points | frac:0.5 | rmse_h50 | lstm | 0.381 [0.214, 0.601] | p=2.42e-05 (vs persistence) |  | 43 | 5 | cc4f6edb |
| test1 | start_points | frac:0.5 | rmse_h50 | nlinear | 0.213 [0.169, 0.261] | p=1.36e-11 (vs persistence) |  | 43 | 5 | 60722fba |
| test1 | start_points | frac:0.5 | rmse_h50 | patchtst | 0.191 [0.141, 0.250] | p=2.5e-11 (vs persistence) |  | 43 | 5 | 73deb6e0 |
| test1 | start_points | frac:0.5 | rmse_h50 | persistence | 0.851 [0.603, 1.223] |  |  | 43 | 5 | 84662b2e |
| test1 | start_points | frac:0.5 | rmse_h50 | rlinear | 0.460 [0.234, 0.748] | p=0.000215 (vs persistence) |  | 43 | 5 | ee0fc6f5 |
| test1 | start_points | frac:0.5 | rmse_h50 | transformer | 0.412 [0.247, 0.617] | p=0.000211 (vs persistence) |  | 43 | 5 | eb07a039 |
| test1 | start_points | frac:0.7 | rmse_h1 | dlinear | 0.054 [0.030, 0.085] | p=1 (vs last_slope) |  | 43 | 5 | 0b00c3d4 |
| test1 | start_points | frac:0.7 | rmse_h1 | elasticnet | 0.053 [0.029, 0.083] | p=1 (vs last_slope) |  | 43 | 5 | 4c070a82 |
| test1 | start_points | frac:0.7 | rmse_h1 | gru | 0.073 [0.051, 0.104] | p=0.00107 (vs last_slope) |  | 43 | 5 | 74f02c88 |
| test1 | start_points | frac:0.7 | rmse_h1 | itransformer | 0.051 [0.027, 0.083] | p=0.481 (vs last_slope) |  | 43 | 5 | 0ce99716 |
| test1 | start_points | frac:0.7 | rmse_h1 | itransformer_sc | 0.054 [0.030, 0.085] | p=1 (vs last_slope) |  | 43 | 5 | aa089496 |
| test1 | start_points | frac:0.7 | rmse_h1 | last_slope | 0.056 [0.032, 0.088] |  |  | 43 | 5 | c733fae1 |
| test1 | start_points | frac:0.7 | rmse_h1 | lgbm | 0.052 [0.028, 0.084] | p=0.81 (vs last_slope) |  | 43 | 5 | 7c413ce2 |
| test1 | start_points | frac:0.7 | rmse_h1 | lstm | 0.060 [0.035, 0.092] | p=0.462 (vs last_slope) |  | 43 | 5 | cc4f6edb |
| test1 | start_points | frac:0.7 | rmse_h1 | nlinear | 0.054 [0.031, 0.086] | p=1 (vs last_slope) |  | 43 | 5 | 60722fba |
| test1 | start_points | frac:0.7 | rmse_h1 | patchtst | 0.052 [0.029, 0.083] | p=0.81 (vs last_slope) |  | 43 | 5 | 73deb6e0 |
| test1 | start_points | frac:0.7 | rmse_h1 | persistence | 0.062 [0.039, 0.092] | p=0.648 (vs last_slope) |  | 43 | 5 | 84662b2e |
| test1 | start_points | frac:0.7 | rmse_h1 | rlinear | 0.051 [0.027, 0.082] | p=0.861 (vs last_slope) |  | 43 | 5 | ee0fc6f5 |
| test1 | start_points | frac:0.7 | rmse_h1 | transformer | 0.090 [0.068, 0.118] | p=5.93e-08 (vs last_slope) |  | 43 | 5 | eb07a039 |
| test1 | start_points | frac:0.7 | rmse_h10 | dlinear | 0.128 [0.069, 0.215] | p=0.00837 (vs last_slope) |  | 43 | 5 | 0b00c3d4 |
| test1 | start_points | frac:0.7 | rmse_h10 | elasticnet | 0.104 [0.049, 0.185] | p=1 (vs last_slope) |  | 43 | 5 | 4c070a82 |
| test1 | start_points | frac:0.7 | rmse_h10 | gru | 0.119 [0.055, 0.215] | p=1 (vs last_slope) |  | 43 | 5 | 74f02c88 |
| test1 | start_points | frac:0.7 | rmse_h10 | itransformer | 0.102 [0.040, 0.191] | p=1 (vs last_slope) |  | 43 | 5 | 0ce99716 |
| test1 | start_points | frac:0.7 | rmse_h10 | itransformer_sc | 0.109 [0.050, 0.193] | p=1 (vs last_slope) |  | 43 | 5 | aa089496 |
| test1 | start_points | frac:0.7 | rmse_h10 | last_slope | 0.120 [0.048, 0.236] |  |  | 43 | 5 | c733fae1 |
| test1 | start_points | frac:0.7 | rmse_h10 | lgbm | 0.104 [0.045, 0.190] | p=1 (vs last_slope) |  | 43 | 5 | 7c413ce2 |
| test1 | start_points | frac:0.7 | rmse_h10 | lstm | 0.117 [0.053, 0.211] | p=1 (vs last_slope) |  | 43 | 5 | cc4f6edb |
| test1 | start_points | frac:0.7 | rmse_h10 | nlinear | 0.108 [0.048, 0.195] | p=1 (vs last_slope) |  | 43 | 5 | 60722fba |
| test1 | start_points | frac:0.7 | rmse_h10 | patchtst | 0.104 [0.048, 0.184] | p=1 (vs last_slope) |  | 43 | 5 | 73deb6e0 |
| test1 | start_points | frac:0.7 | rmse_h10 | persistence | 0.366 [0.291, 0.461] | p=6.54e-07 (vs last_slope) |  | 43 | 5 | 84662b2e |
| test1 | start_points | frac:0.7 | rmse_h10 | rlinear | 0.105 [0.046, 0.189] | p=1 (vs last_slope) |  | 43 | 5 | ee0fc6f5 |
| test1 | start_points | frac:0.7 | rmse_h10 | transformer | 0.157 [0.102, 0.237] | p=0.000103 (vs last_slope) |  | 43 | 5 | eb07a039 |
| test1 | start_points | frac:0.7 | rmse_h100 | dlinear | 1.938 [1.508, 2.395] | p=2.84e-07 (vs last_slope) |  | 42 | 5 | 0b00c3d4 |
| test1 | start_points | frac:0.7 | rmse_h100 | elasticnet | 1.249 [0.981, 1.524] | p=2.3e-07 (vs last_slope) |  | 42 | 5 | 4c070a82 |
| test1 | start_points | frac:0.7 | rmse_h100 | gru | 1.228 [0.925, 1.588] | p=4.74e-07 (vs last_slope) |  | 42 | 5 | 74f02c88 |
| test1 | start_points | frac:0.7 | rmse_h100 | itransformer | 0.910 [0.576, 1.373] | p=2.84e-07 (vs last_slope) |  | 42 | 5 | 0ce99716 |
| test1 | start_points | frac:0.7 | rmse_h100 | itransformer_sc | 1.020 [0.745, 1.329] | p=1.36e-10 (vs last_slope) |  | 42 | 5 | aa089496 |
| test1 | start_points | frac:0.7 | rmse_h100 | last_slope | 2.597 [2.022, 3.244] |  |  | 42 | 5 | c733fae1 |
| test1 | start_points | frac:0.7 | rmse_h100 | lgbm | 0.919 [0.698, 1.160] | p=2.76e-08 (vs last_slope) |  | 42 | 5 | 7c413ce2 |
| test1 | start_points | frac:0.7 | rmse_h100 | lstm | 1.200 [0.942, 1.475] | p=2.96e-07 (vs last_slope) |  | 42 | 5 | cc4f6edb |
| test1 | start_points | frac:0.7 | rmse_h100 | nlinear | 1.738 [1.318, 2.179] | p=7.91e-09 (vs last_slope) |  | 42 | 5 | 60722fba |
| test1 | start_points | frac:0.7 | rmse_h100 | patchtst | 1.090 [0.820, 1.378] | p=7.91e-09 (vs last_slope) |  | 42 | 5 | 73deb6e0 |
| test1 | start_points | frac:0.7 | rmse_h100 | persistence | 5.192 [4.513, 5.866] | p=2.77e-08 (vs last_slope) |  | 42 | 5 | 84662b2e |
| test1 | start_points | frac:0.7 | rmse_h100 | rlinear | 1.622 [1.242, 2.029] | p=4.52e-09 (vs last_slope) |  | 42 | 5 | ee0fc6f5 |
| test1 | start_points | frac:0.7 | rmse_h100 | transformer | 1.156 [0.899, 1.427] | p=1.1e-07 (vs last_slope) |  | 42 | 5 | eb07a039 |
| test1 | start_points | frac:0.7 | rmse_h200 | dlinear | 5.113 [3.888, 6.325] | p=0.782 (vs last_slope) |  | 17 | 5 | 0b00c3d4 |
| test1 | start_points | frac:0.7 | rmse_h200 | elasticnet | 2.766 [2.062, 3.471] | p=0.028 (vs last_slope) |  | 17 | 5 | 4c070a82 |
| test1 | start_points | frac:0.7 | rmse_h200 | gru | 2.428 [1.586, 3.425] | p=0.0042 (vs last_slope) |  | 17 | 5 | 74f02c88 |
| test1 | start_points | frac:0.7 | rmse_h200 | itransformer | 1.395 [0.829, 2.039] | p=0.000839 (vs last_slope) |  | 17 | 5 | 0ce99716 |
| test1 | start_points | frac:0.7 | rmse_h200 | itransformer_sc | 2.654 [1.939, 3.431] | p=0.00153 (vs last_slope) |  | 17 | 5 | aa089496 |
| test1 | start_points | frac:0.7 | rmse_h200 | last_slope | 4.960 [3.958, 5.901] |  |  | 17 | 5 | c733fae1 |
| test1 | start_points | frac:0.7 | rmse_h200 | lgbm | 1.753 [1.097, 2.431] | p=0.00192 (vs last_slope) |  | 17 | 5 | 7c413ce2 |
| test1 | start_points | frac:0.7 | rmse_h200 | lstm | 2.381 [1.571, 3.226] | p=0.00203 (vs last_slope) |  | 17 | 5 | cc4f6edb |
| test1 | start_points | frac:0.7 | rmse_h200 | nlinear | 4.780 [3.619, 5.954] | p=0.756 (vs last_slope) |  | 17 | 5 | 60722fba |
| test1 | start_points | frac:0.7 | rmse_h200 | patchtst | 2.448 [1.771, 3.216] | p=0.00427 (vs last_slope) |  | 17 | 5 | 73deb6e0 |
| test1 | start_points | frac:0.7 | rmse_h200 | persistence | 8.965 [7.231, 10.660] | p=0.000183 (vs last_slope) |  | 17 | 5 | 84662b2e |
| test1 | start_points | frac:0.7 | rmse_h200 | rlinear | 3.098 [2.361, 3.895] | p=0.00394 (vs last_slope) |  | 17 | 5 | ee0fc6f5 |
| test1 | start_points | frac:0.7 | rmse_h200 | transformer | 2.161 [1.463, 2.894] | p=0.00192 (vs last_slope) |  | 17 | 5 | eb07a039 |
| test1 | start_points | frac:0.7 | rmse_h50 | dlinear | 0.393 [0.314, 0.485] | p=0.00586 (vs last_slope) |  | 43 | 5 | 0b00c3d4 |
| test1 | start_points | frac:0.7 | rmse_h50 | elasticnet | 0.322 [0.230, 0.429] | p=0.00586 (vs last_slope) |  | 43 | 5 | 4c070a82 |
| test1 | start_points | frac:0.7 | rmse_h50 | gru | 0.403 [0.275, 0.553] | p=0.0321 (vs last_slope) |  | 43 | 5 | 74f02c88 |
| test1 | start_points | frac:0.7 | rmse_h50 | itransformer | 0.344 [0.191, 0.562] | p=0.00188 (vs last_slope) |  | 43 | 5 | 0ce99716 |
| test1 | start_points | frac:0.7 | rmse_h50 | itransformer_sc | 0.257 [0.180, 0.362] | p=5.21e-05 (vs last_slope) |  | 43 | 5 | aa089496 |
| test1 | start_points | frac:0.7 | rmse_h50 | last_slope | 0.580 [0.410, 0.828] |  |  | 43 | 5 | c733fae1 |
| test1 | start_points | frac:0.7 | rmse_h50 | lgbm | 0.353 [0.209, 0.555] | p=0.00304 (vs last_slope) |  | 43 | 5 | 7c413ce2 |
| test1 | start_points | frac:0.7 | rmse_h50 | lstm | 0.383 [0.276, 0.510] | p=0.0156 (vs last_slope) |  | 43 | 5 | cc4f6edb |
| test1 | start_points | frac:0.7 | rmse_h50 | nlinear | 0.360 [0.276, 0.459] | p=0.000449 (vs last_slope) |  | 43 | 5 | 60722fba |
| test1 | start_points | frac:0.7 | rmse_h50 | patchtst | 0.248 [0.178, 0.341] | p=4.93e-05 (vs last_slope) |  | 43 | 5 | 73deb6e0 |
| test1 | start_points | frac:0.7 | rmse_h50 | persistence | 1.975 [1.653, 2.398] | p=2.37e-08 (vs last_slope) |  | 43 | 5 | 84662b2e |
| test1 | start_points | frac:0.7 | rmse_h50 | rlinear | 0.354 [0.263, 0.467] | p=0.000285 (vs last_slope) |  | 43 | 5 | ee0fc6f5 |
| test1 | start_points | frac:0.7 | rmse_h50 | transformer | 0.379 [0.278, 0.499] | p=0.0156 (vs last_slope) |  | 43 | 5 | eb07a039 |
| test1 | start_points | overall | rmse_h1 | dlinear | 0.048 [0.032, 0.066] | p=0.641 (vs persistence) |  | 43 | 5 | 0b00c3d4 |
| test1 | start_points | overall | rmse_h1 | elasticnet | 0.040 [0.027, 0.056] | p=0.0465 (vs persistence) |  | 43 | 5 | 4c070a82 |
| test1 | start_points | overall | rmse_h1 | gru | 0.083 [0.058, 0.116] | p=1.64e-05 (vs persistence) |  | 43 | 5 | 74f02c88 |
| test1 | start_points | overall | rmse_h1 | itransformer | 0.040 [0.026, 0.058] | p=0.00938 (vs persistence) |  | 43 | 5 | 0ce99716 |
| test1 | start_points | overall | rmse_h1 | itransformer_sc | 0.040 [0.027, 0.057] | p=0.0109 (vs persistence) |  | 43 | 5 | aa089496 |
| test1 | start_points | overall | rmse_h1 | last_slope | 0.052 [0.033, 0.074] | p=0.341 (vs persistence) |  | 43 | 5 | c733fae1 |
| test1 | start_points | overall | rmse_h1 | lgbm | 0.039 [0.025, 0.055] | p=0.000317 (vs persistence) |  | 43 | 5 | 7c413ce2 |
| test1 | start_points | overall | rmse_h1 | lstm | 0.054 [0.037, 0.074] | p=0.641 (vs persistence) |  | 43 | 5 | cc4f6edb |
| test1 | start_points | overall | rmse_h1 | nlinear | 0.040 [0.027, 0.057] | p=0.0276 (vs persistence) |  | 43 | 5 | 60722fba |
| test1 | start_points | overall | rmse_h1 | patchtst | 0.039 [0.026, 0.055] | p=0.00147 (vs persistence) |  | 43 | 5 | 73deb6e0 |
| test1 | start_points | overall | rmse_h1 | persistence | 0.045 [0.032, 0.061] |  |  | 43 | 5 | 84662b2e |
| test1 | start_points | overall | rmse_h1 | rlinear | 0.067 [0.038, 0.103] | p=0.641 (vs persistence) |  | 43 | 5 | ee0fc6f5 |
| test1 | start_points | overall | rmse_h1 | transformer | 0.095 [0.079, 0.114] | p=1.8e-08 (vs persistence) |  | 43 | 5 | eb07a039 |
| test1 | start_points | overall | rmse_h10 | dlinear | 0.111 [0.077, 0.153] | p=5.71e-08 (vs persistence) |  | 43 | 5 | 0b00c3d4 |
| test1 | start_points | overall | rmse_h10 | elasticnet | 0.105 [0.070, 0.146] | p=2.78e-07 (vs persistence) |  | 43 | 5 | 4c070a82 |
| test1 | start_points | overall | rmse_h10 | gru | 0.112 [0.072, 0.162] | p=9.01e-07 (vs persistence) |  | 43 | 5 | 74f02c88 |
| test1 | start_points | overall | rmse_h10 | itransformer | 0.082 [0.048, 0.127] | p=2.49e-08 (vs persistence) |  | 43 | 5 | 0ce99716 |
| test1 | start_points | overall | rmse_h10 | itransformer_sc | 0.092 [0.058, 0.135] | p=7.31e-08 (vs persistence) |  | 43 | 5 | aa089496 |
| test1 | start_points | overall | rmse_h10 | last_slope | 0.239 [0.099, 0.422] | p=0.00277 (vs persistence) |  | 43 | 5 | c733fae1 |
| test1 | start_points | overall | rmse_h10 | lgbm | 0.096 [0.059, 0.140] | p=3.63e-07 (vs persistence) |  | 43 | 5 | 7c413ce2 |
| test1 | start_points | overall | rmse_h10 | lstm | 0.112 [0.068, 0.167] | p=9.57e-07 (vs persistence) |  | 43 | 5 | cc4f6edb |
| test1 | start_points | overall | rmse_h10 | nlinear | 0.090 [0.057, 0.134] | p=4.36e-08 (vs persistence) |  | 43 | 5 | 60722fba |
| test1 | start_points | overall | rmse_h10 | patchtst | 0.081 [0.050, 0.120] | p=2.37e-08 (vs persistence) |  | 43 | 5 | 73deb6e0 |
| test1 | start_points | overall | rmse_h10 | persistence | 0.234 [0.180, 0.307] |  |  | 43 | 5 | 84662b2e |
| test1 | start_points | overall | rmse_h10 | rlinear | 0.119 [0.068, 0.181] | p=1.4e-05 (vs persistence) |  | 43 | 5 | ee0fc6f5 |
| test1 | start_points | overall | rmse_h10 | transformer | 0.134 [0.102, 0.173] | p=4.49e-06 (vs persistence) |  | 43 | 5 | eb07a039 |
| test1 | start_points | overall | rmse_h100 | dlinear | 1.276 [1.027, 1.578] | p=5.99e-05 (vs last_slope) |  | 43 | 5 | 0b00c3d4 |
| test1 | start_points | overall | rmse_h100 | elasticnet | 1.231 [1.004, 1.479] | p=0.000144 (vs last_slope) |  | 43 | 5 | 4c070a82 |
| test1 | start_points | overall | rmse_h100 | gru | 0.937 [0.704, 1.212] | p=8.11e-06 (vs last_slope) |  | 43 | 5 | 74f02c88 |
| test1 | start_points | overall | rmse_h100 | itransformer | 0.703 [0.503, 0.942] | p=3.97e-07 (vs last_slope) |  | 43 | 5 | 0ce99716 |
| test1 | start_points | overall | rmse_h100 | itransformer_sc | 0.952 [0.708, 1.248] | p=3.2e-07 (vs last_slope) |  | 43 | 5 | aa089496 |
| test1 | start_points | overall | rmse_h100 | last_slope | 2.867 [1.586, 4.633] |  |  | 43 | 5 | c733fae1 |
| test1 | start_points | overall | rmse_h100 | lgbm | 0.801 [0.567, 1.116] | p=3.16e-07 (vs last_slope) |  | 43 | 5 | 7c413ce2 |
| test1 | start_points | overall | rmse_h100 | lstm | 0.956 [0.747, 1.187] | p=3.47e-05 (vs last_slope) |  | 43 | 5 | cc4f6edb |
| test1 | start_points | overall | rmse_h100 | nlinear | 1.131 [0.886, 1.428] | p=4.36e-07 (vs last_slope) |  | 43 | 5 | 60722fba |
| test1 | start_points | overall | rmse_h100 | patchtst | 0.792 [0.634, 0.968] | p=9.72e-08 (vs last_slope) |  | 43 | 5 | 73deb6e0 |
| test1 | start_points | overall | rmse_h100 | persistence | 3.154 [2.605, 3.867] | p=0.000144 (vs last_slope) |  | 43 | 5 | 84662b2e |
| test1 | start_points | overall | rmse_h100 | rlinear | 1.258 [0.973, 1.574] | p=7.03e-07 (vs last_slope) |  | 43 | 5 | ee0fc6f5 |
| test1 | start_points | overall | rmse_h100 | transformer | 0.957 [0.770, 1.153] | p=5.45e-06 (vs last_slope) |  | 43 | 5 | eb07a039 |
| test1 | start_points | overall | rmse_h200 | dlinear | 3.035 [2.650, 3.424] | p=5.46e-12 (vs persistence) |  | 42 | 5 | 0b00c3d4 |
| test1 | start_points | overall | rmse_h200 | elasticnet | 2.218 [1.889, 2.594] | p=5.65e-10 (vs persistence) |  | 42 | 5 | 4c070a82 |
| test1 | start_points | overall | rmse_h200 | gru | 2.175 [1.543, 3.103] | p=1.38e-08 (vs persistence) |  | 42 | 5 | 74f02c88 |
| test1 | start_points | overall | rmse_h200 | itransformer | 1.678 [1.315, 2.087] | p=9.09e-12 (vs persistence) |  | 42 | 5 | 0ce99716 |
| test1 | start_points | overall | rmse_h200 | itransformer_sc | 2.274 [1.838, 2.768] | p=1.22e-09 (vs persistence) |  | 42 | 5 | aa089496 |
| test1 | start_points | overall | rmse_h200 | last_slope | 6.252 [3.418, 10.551] | p=0.000342 (vs persistence) |  | 42 | 5 | c733fae1 |
| test1 | start_points | overall | rmse_h200 | lgbm | 1.385 [1.090, 1.714] | p=5.46e-12 (vs persistence) |  | 42 | 5 | 7c413ce2 |
| test1 | start_points | overall | rmse_h200 | lstm | 2.001 [1.517, 2.619] | p=1.38e-08 (vs persistence) |  | 42 | 5 | cc4f6edb |
| test1 | start_points | overall | rmse_h200 | nlinear | 2.803 [2.437, 3.172] | p=1.23e-11 (vs persistence) |  | 42 | 5 | 60722fba |
| test1 | start_points | overall | rmse_h200 | patchtst | 2.135 [1.771, 2.516] | p=2.55e-11 (vs persistence) |  | 42 | 5 | 73deb6e0 |
| test1 | start_points | overall | rmse_h200 | persistence | 5.459 [4.855, 6.081] |  |  | 42 | 5 | 84662b2e |
| test1 | start_points | overall | rmse_h200 | rlinear | 2.667 [2.069, 3.336] | p=1.38e-08 (vs persistence) |  | 42 | 5 | ee0fc6f5 |
| test1 | start_points | overall | rmse_h200 | transformer | 1.871 [1.514, 2.273] | p=2.55e-11 (vs persistence) |  | 42 | 5 | eb07a039 |
| test1 | start_points | overall | rmse_h50 | dlinear | 0.428 [0.390, 0.474] | p=0.247 (vs last_slope) |  | 43 | 5 | 0b00c3d4 |
| test1 | start_points | overall | rmse_h50 | elasticnet | 0.441 [0.336, 0.565] | p=0.0705 (vs last_slope) |  | 43 | 5 | 4c070a82 |
| test1 | start_points | overall | rmse_h50 | gru | 0.355 [0.242, 0.482] | p=0.0019 (vs last_slope) |  | 43 | 5 | 74f02c88 |
| test1 | start_points | overall | rmse_h50 | itransformer | 0.250 [0.154, 0.372] | p=7.46e-05 (vs last_slope) |  | 43 | 5 | 0ce99716 |
| test1 | start_points | overall | rmse_h50 | itransformer_sc | 0.286 [0.198, 0.393] | p=2.66e-05 (vs last_slope) |  | 43 | 5 | aa089496 |
| test1 | start_points | overall | rmse_h50 | last_slope | 1.101 [0.460, 1.991] |  |  | 43 | 5 | c733fae1 |
| test1 | start_points | overall | rmse_h50 | lgbm | 0.305 [0.187, 0.465] | p=3.74e-05 (vs last_slope) |  | 43 | 5 | 7c413ce2 |
| test1 | start_points | overall | rmse_h50 | lstm | 0.343 [0.243, 0.461] | p=0.00319 (vs last_slope) |  | 43 | 5 | cc4f6edb |
| test1 | start_points | overall | rmse_h50 | nlinear | 0.272 [0.225, 0.325] | p=3.06e-05 (vs last_slope) |  | 43 | 5 | 60722fba |
| test1 | start_points | overall | rmse_h50 | patchtst | 0.215 [0.165, 0.278] | p=1.09e-06 (vs last_slope) |  | 43 | 5 | 73deb6e0 |
| test1 | start_points | overall | rmse_h50 | persistence | 1.197 [0.940, 1.577] | p=0.00196 (vs last_slope) |  | 43 | 5 | 84662b2e |
| test1 | start_points | overall | rmse_h50 | rlinear | 0.378 [0.265, 0.518] | p=0.000222 (vs last_slope) |  | 43 | 5 | ee0fc6f5 |
| test1 | start_points | overall | rmse_h50 | transformer | 0.357 [0.263, 0.466] | p=0.00445 (vs last_slope) |  | 43 | 5 | eb07a039 |
| test2 | all | overall | rmse_h1 | dlinear | 0.019 [0.016, 0.021] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | all | overall | rmse_h1 | elasticnet | 0.019 [0.017, 0.022] | p=3.82e-11 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | all | overall | rmse_h1 | gru | 0.089 [0.076, 0.106] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | all | overall | rmse_h1 | itransformer | 0.015 [0.013, 0.018] | p=3.94e-06 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | all | overall | rmse_h1 | itransformer_sc | 0.016 [0.013, 0.019] | p=4.51e-05 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | all | overall | rmse_h1 | last_slope | 0.016 [0.014, 0.019] |  |  | 40 | 5 | c733fae1 |
| test2 | all | overall | rmse_h1 | lgbm | 0.020 [0.017, 0.022] | p=8.28e-08 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | all | overall | rmse_h1 | lstm | 0.025 [0.022, 0.027] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | all | overall | rmse_h1 | nlinear | 0.017 [0.014, 0.020] | p=0.0343 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | all | overall | rmse_h1 | patchtst | 0.017 [0.014, 0.019] | p=0.259 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | all | overall | rmse_h1 | persistence | 0.036 [0.034, 0.038] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | all | overall | rmse_h1 | rlinear | 0.018 [0.016, 0.020] | p=0.00432 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | all | overall | rmse_h1 | transformer | 0.113 [0.105, 0.122] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | all | overall | rmse_h10 | dlinear | 0.064 [0.060, 0.068] | p=0.000288 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | all | overall | rmse_h10 | elasticnet | 0.064 [0.058, 0.070] | p=0.014 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | all | overall | rmse_h10 | gru | 0.108 [0.089, 0.130] | p=3.02e-08 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | all | overall | rmse_h10 | itransformer | 0.032 [0.028, 0.037] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | all | overall | rmse_h10 | itransformer_sc | 0.037 [0.032, 0.042] | p=7.28e-11 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | all | overall | rmse_h10 | last_slope | 0.057 [0.051, 0.063] |  |  | 40 | 5 | c733fae1 |
| test2 | all | overall | rmse_h10 | lgbm | 0.061 [0.055, 0.066] | p=0.485 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | all | overall | rmse_h10 | lstm | 0.051 [0.045, 0.058] | p=0.0642 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | all | overall | rmse_h10 | nlinear | 0.046 [0.042, 0.051] | p=4.07e-08 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | all | overall | rmse_h10 | patchtst | 0.033 [0.029, 0.039] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | all | overall | rmse_h10 | persistence | 0.303 [0.281, 0.324] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | all | overall | rmse_h10 | rlinear | 0.045 [0.040, 0.050] | p=1.18e-07 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | all | overall | rmse_h10 | transformer | 0.107 [0.101, 0.113] | p=3.27e-11 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | all | overall | rmse_h100 | dlinear | 0.876 [0.806, 0.949] | p=7.83e-07 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | all | overall | rmse_h100 | elasticnet | 1.064 [0.964, 1.167] | p=0.545 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | all | overall | rmse_h100 | gru | 1.399 [1.226, 1.580] | p=0.0188 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | all | overall | rmse_h100 | itransformer | 0.517 [0.458, 0.575] | p=6e-11 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | all | overall | rmse_h100 | itransformer_sc | 0.486 [0.414, 0.568] | p=9.75e-09 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | all | overall | rmse_h100 | last_slope | 1.032 [0.933, 1.129] |  |  | 40 | 5 | c733fae1 |
| test2 | all | overall | rmse_h100 | lgbm | 0.719 [0.667, 0.777] | p=0.000106 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | all | overall | rmse_h100 | lstm | 0.785 [0.703, 0.882] | p=0.0024 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | all | overall | rmse_h100 | nlinear | 0.745 [0.676, 0.816] | p=6.34e-08 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | all | overall | rmse_h100 | patchtst | 0.541 [0.482, 0.603] | p=9.75e-09 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | all | overall | rmse_h100 | persistence | 2.349 [2.216, 2.473] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | all | overall | rmse_h100 | rlinear | 0.677 [0.602, 0.754] | p=7.83e-07 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | all | overall | rmse_h100 | transformer | 0.606 [0.537, 0.677] | p=9.75e-09 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | all | overall | rmse_h200 | dlinear | 2.105 [1.982, 2.219] | p=3.75e-05 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | all | overall | rmse_h200 | elasticnet | 1.862 [1.647, 2.104] | p=0.000479 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | all | overall | rmse_h200 | gru | 4.087 [3.496, 4.722] | p=0.000176 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | all | overall | rmse_h200 | itransformer | 1.080 [0.930, 1.252] | p=1.16e-08 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | all | overall | rmse_h200 | itransformer_sc | 1.293 [1.115, 1.507] | p=1.19e-05 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | all | overall | rmse_h200 | last_slope | 2.322 [2.142, 2.486] |  |  | 40 | 5 | c733fae1 |
| test2 | all | overall | rmse_h200 | lgbm | 2.033 [1.895, 2.185] | p=0.0147 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | all | overall | rmse_h200 | lstm | 1.919 [1.693, 2.194] | p=0.0081 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | all | overall | rmse_h200 | nlinear | 2.012 [1.898, 2.115] | p=1.02e-05 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | all | overall | rmse_h200 | patchtst | 1.364 [1.239, 1.502] | p=2.76e-07 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | all | overall | rmse_h200 | persistence | 3.713 [3.519, 3.907] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | all | overall | rmse_h200 | rlinear | 1.476 [1.326, 1.653] | p=2.09e-05 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | all | overall | rmse_h200 | transformer | 1.396 [1.271, 1.531] | p=3.38e-09 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | all | overall | rmse_h50 | dlinear | 0.470 [0.448, 0.494] | p=0.000528 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | all | overall | rmse_h50 | elasticnet | 0.491 [0.450, 0.532] | p=9.66e-08 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | all | overall | rmse_h50 | gru | 0.467 [0.407, 0.528] | p=0.183 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | all | overall | rmse_h50 | itransformer | 0.200 [0.174, 0.226] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | all | overall | rmse_h50 | itransformer_sc | 0.180 [0.153, 0.210] | p=1.15e-10 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | all | overall | rmse_h50 | last_slope | 0.397 [0.360, 0.434] |  |  | 40 | 5 | c733fae1 |
| test2 | all | overall | rmse_h50 | lgbm | 0.302 [0.278, 0.327] | p=5.62e-06 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | all | overall | rmse_h50 | lstm | 0.282 [0.253, 0.312] | p=5.62e-06 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | all | overall | rmse_h50 | nlinear | 0.298 [0.270, 0.328] | p=7.83e-07 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | all | overall | rmse_h50 | patchtst | 0.185 [0.165, 0.207] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | all | overall | rmse_h50 | persistence | 1.354 [1.265, 1.437] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | all | overall | rmse_h50 | rlinear | 0.270 [0.239, 0.301] | p=7.83e-07 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | all | overall | rmse_h50 | transformer | 0.281 [0.252, 0.311] | p=7.8e-09 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | start_points | fixed:100 | rmse_h1 | dlinear | 0.012 [0.007, 0.020] | p=0.000284 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | start_points | fixed:100 | rmse_h1 | elasticnet | 0.012 [0.007, 0.021] | p=0.000256 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | start_points | fixed:100 | rmse_h1 | gru | 0.044 [0.039, 0.049] | p=4.07e-08 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | start_points | fixed:100 | rmse_h1 | itransformer | 0.008 [0.004, 0.015] | p=0.921 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | start_points | fixed:100 | rmse_h1 | itransformer_sc | 0.009 [0.004, 0.017] | p=0.923 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | start_points | fixed:100 | rmse_h1 | last_slope | 0.010 [0.004, 0.018] |  |  | 40 | 5 | c733fae1 |
| test2 | start_points | fixed:100 | rmse_h1 | lgbm | 0.011 [0.006, 0.018] | p=0.923 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | start_points | fixed:100 | rmse_h1 | lstm | 0.014 [0.008, 0.023] | p=9.58e-06 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | start_points | fixed:100 | rmse_h1 | nlinear | 0.010 [0.004, 0.018] | p=0.923 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | start_points | fixed:100 | rmse_h1 | patchtst | 0.009 [0.004, 0.015] | p=0.923 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | start_points | fixed:100 | rmse_h1 | persistence | 0.011 [0.005, 0.018] | p=1 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | start_points | fixed:100 | rmse_h1 | rlinear | 0.007 [0.004, 0.011] | p=1 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | start_points | fixed:100 | rmse_h1 | transformer | 0.108 [0.099, 0.120] | p=1.09e-10 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | start_points | fixed:100 | rmse_h10 | dlinear | 0.043 [0.035, 0.054] | p=0.00185 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | start_points | fixed:100 | rmse_h10 | elasticnet | 0.028 [0.019, 0.037] | p=0.825 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | start_points | fixed:100 | rmse_h10 | gru | 0.045 [0.033, 0.060] | p=0.473 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | start_points | fixed:100 | rmse_h10 | itransformer | 0.020 [0.012, 0.030] | p=0.00022 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | start_points | fixed:100 | rmse_h10 | itransformer_sc | 0.020 [0.011, 0.032] | p=0.00022 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | start_points | fixed:100 | rmse_h10 | last_slope | 0.034 [0.023, 0.049] |  |  | 40 | 5 | c733fae1 |
| test2 | start_points | fixed:100 | rmse_h10 | lgbm | 0.047 [0.038, 0.057] | p=0.00911 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | start_points | fixed:100 | rmse_h10 | lstm | 0.039 [0.031, 0.049] | p=0.163 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | start_points | fixed:100 | rmse_h10 | nlinear | 0.029 [0.018, 0.043] | p=0.112 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | start_points | fixed:100 | rmse_h10 | patchtst | 0.019 [0.012, 0.029] | p=0.000145 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | start_points | fixed:100 | rmse_h10 | persistence | 0.045 [0.030, 0.063] | p=0.825 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | start_points | fixed:100 | rmse_h10 | rlinear | 0.020 [0.013, 0.029] | p=0.000145 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | start_points | fixed:100 | rmse_h10 | transformer | 0.094 [0.087, 0.101] | p=5.37e-07 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | start_points | fixed:100 | rmse_h100 | dlinear | 0.510 [0.470, 0.557] | p=1e-10 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | start_points | fixed:100 | rmse_h100 | elasticnet | 0.700 [0.610, 0.798] | p=7.8e-09 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | start_points | fixed:100 | rmse_h100 | gru | 1.029 [0.893, 1.183] | p=4.37e-11 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | start_points | fixed:100 | rmse_h100 | itransformer | 0.089 [0.067, 0.115] | p=8.14e-06 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | start_points | fixed:100 | rmse_h100 | itransformer_sc | 0.216 [0.114, 0.349] | p=0.147 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | start_points | fixed:100 | rmse_h100 | last_slope | 0.204 [0.152, 0.263] |  |  | 40 | 5 | c733fae1 |
| test2 | start_points | fixed:100 | rmse_h100 | lgbm | 0.587 [0.555, 0.627] | p=1.6e-09 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | start_points | fixed:100 | rmse_h100 | lstm | 0.596 [0.498, 0.714] | p=2.24e-09 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | start_points | fixed:100 | rmse_h100 | nlinear | 0.358 [0.294, 0.434] | p=8.14e-06 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | start_points | fixed:100 | rmse_h100 | patchtst | 0.142 [0.109, 0.179] | p=0.181 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | start_points | fixed:100 | rmse_h100 | persistence | 0.440 [0.325, 0.591] | p=0.00022 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | start_points | fixed:100 | rmse_h100 | rlinear | 0.204 [0.124, 0.303] | p=0.181 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | start_points | fixed:100 | rmse_h100 | transformer | 0.199 [0.125, 0.293] | p=0.59 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | start_points | fixed:100 | rmse_h200 | dlinear | 1.280 [1.221, 1.343] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | start_points | fixed:100 | rmse_h200 | elasticnet | 0.978 [0.714, 1.280] | p=0.00338 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | start_points | fixed:100 | rmse_h200 | gru | 2.691 [2.238, 3.210] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | start_points | fixed:100 | rmse_h200 | itransformer | 0.253 [0.164, 0.371] | p=0.0331 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | start_points | fixed:100 | rmse_h200 | itransformer_sc | 0.868 [0.579, 1.238] | p=8.95e-06 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | start_points | fixed:100 | rmse_h200 | last_slope | 0.386 [0.289, 0.493] |  |  | 40 | 5 | c733fae1 |
| test2 | start_points | fixed:100 | rmse_h200 | lgbm | 1.697 [1.565, 1.851] | p=8.19e-11 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | start_points | fixed:100 | rmse_h200 | lstm | 1.283 [0.984, 1.660] | p=1.99e-09 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | start_points | fixed:100 | rmse_h200 | nlinear | 1.556 [1.481, 1.629] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | start_points | fixed:100 | rmse_h200 | patchtst | 0.612 [0.416, 0.859] | p=0.0897 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | start_points | fixed:100 | rmse_h200 | persistence | 0.961 [0.738, 1.252] | p=1.6e-05 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | start_points | fixed:100 | rmse_h200 | rlinear | 0.649 [0.383, 0.986] | p=0.227 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | start_points | fixed:100 | rmse_h200 | transformer | 0.594 [0.415, 0.802] | p=0.184 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | start_points | fixed:100 | rmse_h50 | dlinear | 0.433 [0.415, 0.456] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | start_points | fixed:100 | rmse_h50 | elasticnet | 0.279 [0.249, 0.310] | p=2.79e-05 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | start_points | fixed:100 | rmse_h50 | gru | 0.324 [0.285, 0.366] | p=5.06e-09 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | start_points | fixed:100 | rmse_h50 | itransformer | 0.059 [0.047, 0.071] | p=6.19e-05 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | start_points | fixed:100 | rmse_h50 | itransformer_sc | 0.070 [0.038, 0.109] | p=0.00254 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | start_points | fixed:100 | rmse_h50 | last_slope | 0.121 [0.090, 0.156] |  |  | 40 | 5 | c733fae1 |
| test2 | start_points | fixed:100 | rmse_h50 | lgbm | 0.232 [0.220, 0.245] | p=1.16e-06 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | start_points | fixed:100 | rmse_h50 | lstm | 0.219 [0.192, 0.249] | p=1.84e-06 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | start_points | fixed:100 | rmse_h50 | nlinear | 0.120 [0.091, 0.155] | p=1 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | start_points | fixed:100 | rmse_h50 | patchtst | 0.056 [0.044, 0.067] | p=0.000463 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | start_points | fixed:100 | rmse_h50 | persistence | 0.194 [0.134, 0.273] | p=0.0623 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | start_points | fixed:100 | rmse_h50 | rlinear | 0.086 [0.059, 0.118] | p=0.0461 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | start_points | fixed:100 | rmse_h50 | transformer | 0.094 [0.079, 0.111] | p=1 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | start_points | frac:0.3 | rmse_h1 | dlinear | 0.017 [0.008, 0.028] | p=0.00572 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | start_points | frac:0.3 | rmse_h1 | elasticnet | 0.019 [0.011, 0.030] | p=0.00135 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | start_points | frac:0.3 | rmse_h1 | gru | 0.053 [0.045, 0.064] | p=3.8e-10 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | start_points | frac:0.3 | rmse_h1 | itransformer | 0.014 [0.006, 0.025] | p=1 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | start_points | frac:0.3 | rmse_h1 | itransformer_sc | 0.015 [0.006, 0.026] | p=1 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | start_points | frac:0.3 | rmse_h1 | last_slope | 0.015 [0.007, 0.026] |  |  | 40 | 5 | c733fae1 |
| test2 | start_points | frac:0.3 | rmse_h1 | lgbm | 0.019 [0.010, 0.030] | p=0.00572 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | start_points | frac:0.3 | rmse_h1 | lstm | 0.022 [0.013, 0.033] | p=8.13e-09 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | start_points | frac:0.3 | rmse_h1 | nlinear | 0.016 [0.007, 0.027] | p=0.658 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | start_points | frac:0.3 | rmse_h1 | patchtst | 0.014 [0.006, 0.025] | p=1 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | start_points | frac:0.3 | rmse_h1 | persistence | 0.017 [0.008, 0.028] | p=0.253 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | start_points | frac:0.3 | rmse_h1 | rlinear | 0.014 [0.007, 0.024] | p=1 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | start_points | frac:0.3 | rmse_h1 | transformer | 0.120 [0.110, 0.130] | p=4.37e-11 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | start_points | frac:0.3 | rmse_h10 | dlinear | 0.034 [0.028, 0.042] | p=1.04e-06 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | start_points | frac:0.3 | rmse_h10 | elasticnet | 0.028 [0.022, 0.035] | p=0.00453 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | start_points | frac:0.3 | rmse_h10 | gru | 0.055 [0.043, 0.069] | p=1.1e-09 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | start_points | frac:0.3 | rmse_h10 | itransformer | 0.015 [0.010, 0.022] | p=0.336 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | start_points | frac:0.3 | rmse_h10 | itransformer_sc | 0.018 [0.012, 0.026] | p=0.565 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | start_points | frac:0.3 | rmse_h10 | last_slope | 0.018 [0.013, 0.025] |  |  | 40 | 5 | c733fae1 |
| test2 | start_points | frac:0.3 | rmse_h10 | lgbm | 0.046 [0.036, 0.057] | p=1.59e-06 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | start_points | frac:0.3 | rmse_h10 | lstm | 0.039 [0.031, 0.050] | p=7.38e-07 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | start_points | frac:0.3 | rmse_h10 | nlinear | 0.018 [0.010, 0.029] | p=0.565 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | start_points | frac:0.3 | rmse_h10 | patchtst | 0.014 [0.009, 0.021] | p=0.134 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | start_points | frac:0.3 | rmse_h10 | persistence | 0.060 [0.048, 0.076] | p=1.04e-07 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | start_points | frac:0.3 | rmse_h10 | rlinear | 0.014 [0.009, 0.021] | p=0.199 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | start_points | frac:0.3 | rmse_h10 | transformer | 0.078 [0.072, 0.083] | p=6.55e-11 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | start_points | frac:0.3 | rmse_h100 | dlinear | 0.492 [0.446, 0.546] | p=5.46e-11 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | start_points | frac:0.3 | rmse_h100 | elasticnet | 0.577 [0.479, 0.684] | p=5.46e-11 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | start_points | frac:0.3 | rmse_h100 | gru | 1.312 [1.122, 1.524] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | start_points | frac:0.3 | rmse_h100 | itransformer | 0.145 [0.090, 0.215] | p=0.884 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | start_points | frac:0.3 | rmse_h100 | itransformer_sc | 0.227 [0.121, 0.365] | p=0.969 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | start_points | frac:0.3 | rmse_h100 | last_slope | 0.131 [0.099, 0.168] |  |  | 40 | 5 | c733fae1 |
| test2 | start_points | frac:0.3 | rmse_h100 | lgbm | 0.594 [0.528, 0.674] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | start_points | frac:0.3 | rmse_h100 | lstm | 0.635 [0.497, 0.808] | p=7.28e-11 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | start_points | frac:0.3 | rmse_h100 | nlinear | 0.415 [0.347, 0.495] | p=2.59e-08 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | start_points | frac:0.3 | rmse_h100 | patchtst | 0.155 [0.114, 0.199] | p=0.969 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | start_points | frac:0.3 | rmse_h100 | persistence | 0.577 [0.477, 0.707] | p=3.18e-10 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | start_points | frac:0.3 | rmse_h100 | rlinear | 0.292 [0.206, 0.399] | p=0.00759 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | start_points | frac:0.3 | rmse_h100 | transformer | 0.257 [0.155, 0.388] | p=0.435 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | start_points | frac:0.3 | rmse_h200 | dlinear | 1.220 [1.168, 1.274] | p=3.27e-11 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | start_points | frac:0.3 | rmse_h200 | elasticnet | 0.812 [0.571, 1.106] | p=0.00114 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | start_points | frac:0.3 | rmse_h200 | gru | 3.879 [3.230, 4.607] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | start_points | frac:0.3 | rmse_h200 | itransformer | 0.512 [0.283, 0.805] | p=0.984 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | start_points | frac:0.3 | rmse_h200 | itransformer_sc | 0.831 [0.551, 1.194] | p=0.000877 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | start_points | frac:0.3 | rmse_h200 | last_slope | 0.317 [0.240, 0.404] |  |  | 40 | 5 | c733fae1 |
| test2 | start_points | frac:0.3 | rmse_h200 | lgbm | 1.923 [1.697, 2.182] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | start_points | frac:0.3 | rmse_h200 | lstm | 1.665 [1.291, 2.124] | p=8.91e-10 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | start_points | frac:0.3 | rmse_h200 | nlinear | 1.483 [1.409, 1.557] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | start_points | frac:0.3 | rmse_h200 | patchtst | 0.787 [0.597, 1.023] | p=0.000272 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | start_points | frac:0.3 | rmse_h200 | persistence | 1.260 [1.051, 1.532] | p=2.76e-10 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | start_points | frac:0.3 | rmse_h200 | rlinear | 0.929 [0.673, 1.251] | p=2.96e-05 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | start_points | frac:0.3 | rmse_h200 | transformer | 0.696 [0.470, 0.971] | p=0.0064 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | start_points | frac:0.3 | rmse_h50 | dlinear | 0.404 [0.392, 0.419] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | start_points | frac:0.3 | rmse_h50 | elasticnet | 0.302 [0.269, 0.338] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | start_points | frac:0.3 | rmse_h50 | gru | 0.375 [0.313, 0.441] | p=2.06e-08 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | start_points | frac:0.3 | rmse_h50 | itransformer | 0.060 [0.038, 0.087] | p=0.0741 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | start_points | frac:0.3 | rmse_h50 | itransformer_sc | 0.078 [0.042, 0.122] | p=0.0929 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | start_points | frac:0.3 | rmse_h50 | last_slope | 0.074 [0.053, 0.101] |  |  | 40 | 5 | c733fae1 |
| test2 | start_points | frac:0.3 | rmse_h50 | lgbm | 0.211 [0.190, 0.235] | p=4.05e-07 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | start_points | frac:0.3 | rmse_h50 | lstm | 0.204 [0.163, 0.252] | p=1.98e-06 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | start_points | frac:0.3 | rmse_h50 | nlinear | 0.124 [0.093, 0.159] | p=0.0106 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | start_points | frac:0.3 | rmse_h50 | patchtst | 0.056 [0.037, 0.081] | p=0.0929 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | start_points | frac:0.3 | rmse_h50 | persistence | 0.295 [0.240, 0.364] | p=6e-10 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | start_points | frac:0.3 | rmse_h50 | rlinear | 0.095 [0.065, 0.131] | p=0.452 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | start_points | frac:0.3 | rmse_h50 | transformer | 0.127 [0.100, 0.160] | p=0.0106 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | start_points | frac:0.5 | rmse_h1 | dlinear | 0.010 [0.006, 0.018] | p=0.884 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | start_points | frac:0.5 | rmse_h1 | elasticnet | 0.013 [0.008, 0.021] | p=0.0912 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | start_points | frac:0.5 | rmse_h1 | gru | 0.061 [0.047, 0.084] | p=3.8e-10 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | start_points | frac:0.5 | rmse_h1 | itransformer | 0.008 [0.004, 0.013] | p=0.214 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | start_points | frac:0.5 | rmse_h1 | itransformer_sc | 0.009 [0.005, 0.016] | p=0.884 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | start_points | frac:0.5 | rmse_h1 | last_slope | 0.010 [0.005, 0.017] |  |  | 40 | 5 | c733fae1 |
| test2 | start_points | frac:0.5 | rmse_h1 | lgbm | 0.013 [0.009, 0.019] | p=0.0372 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | start_points | frac:0.5 | rmse_h1 | lstm | 0.014 [0.010, 0.021] | p=3.19e-05 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | start_points | frac:0.5 | rmse_h1 | nlinear | 0.009 [0.005, 0.016] | p=0.884 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | start_points | frac:0.5 | rmse_h1 | patchtst | 0.008 [0.004, 0.013] | p=0.214 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | start_points | frac:0.5 | rmse_h1 | persistence | 0.013 [0.009, 0.020] | p=0.0302 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | start_points | frac:0.5 | rmse_h1 | rlinear | 0.008 [0.005, 0.012] | p=0.6 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | start_points | frac:0.5 | rmse_h1 | transformer | 0.098 [0.089, 0.108] | p=4.37e-11 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | start_points | frac:0.5 | rmse_h10 | dlinear | 0.036 [0.030, 0.044] | p=0.0335 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | start_points | frac:0.5 | rmse_h10 | elasticnet | 0.024 [0.017, 0.033] | p=0.656 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | start_points | frac:0.5 | rmse_h10 | gru | 0.077 [0.056, 0.107] | p=1.54e-05 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | start_points | frac:0.5 | rmse_h10 | itransformer | 0.016 [0.011, 0.023] | p=0.0794 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | start_points | frac:0.5 | rmse_h10 | itransformer_sc | 0.021 [0.015, 0.029] | p=0.443 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | start_points | frac:0.5 | rmse_h10 | last_slope | 0.029 [0.020, 0.041] |  |  | 40 | 5 | c733fae1 |
| test2 | start_points | frac:0.5 | rmse_h10 | lgbm | 0.059 [0.048, 0.071] | p=0.000129 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | start_points | frac:0.5 | rmse_h10 | lstm | 0.047 [0.038, 0.057] | p=0.0101 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | start_points | frac:0.5 | rmse_h10 | nlinear | 0.022 [0.014, 0.032] | p=0.405 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | start_points | frac:0.5 | rmse_h10 | patchtst | 0.016 [0.011, 0.024] | p=0.00753 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | start_points | frac:0.5 | rmse_h10 | persistence | 0.075 [0.063, 0.088] | p=1.16e-05 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | start_points | frac:0.5 | rmse_h10 | rlinear | 0.018 [0.012, 0.026] | p=0.0928 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | start_points | frac:0.5 | rmse_h10 | transformer | 0.087 [0.080, 0.093] | p=9.76e-09 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | start_points | frac:0.5 | rmse_h100 | dlinear | 0.420 [0.384, 0.459] | p=0.000756 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | start_points | frac:0.5 | rmse_h100 | elasticnet | 0.427 [0.317, 0.554] | p=0.0638 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | start_points | frac:0.5 | rmse_h100 | gru | 1.461 [1.247, 1.689] | p=3.06e-10 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | start_points | frac:0.5 | rmse_h100 | itransformer | 0.151 [0.107, 0.210] | p=0.283 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | start_points | frac:0.5 | rmse_h100 | itransformer_sc | 0.201 [0.135, 0.282] | p=0.427 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | start_points | frac:0.5 | rmse_h100 | last_slope | 0.241 [0.176, 0.313] |  |  | 40 | 5 | c733fae1 |
| test2 | start_points | frac:0.5 | rmse_h100 | lgbm | 0.590 [0.512, 0.668] | p=6.46e-06 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | start_points | frac:0.5 | rmse_h100 | lstm | 0.658 [0.545, 0.786] | p=8.63e-06 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | start_points | frac:0.5 | rmse_h100 | nlinear | 0.386 [0.341, 0.435] | p=0.00559 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | start_points | frac:0.5 | rmse_h100 | patchtst | 0.165 [0.125, 0.208] | p=0.4 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | start_points | frac:0.5 | rmse_h100 | persistence | 0.823 [0.706, 0.967] | p=7.42e-09 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | start_points | frac:0.5 | rmse_h100 | rlinear | 0.287 [0.232, 0.351] | p=0.427 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | start_points | frac:0.5 | rmse_h100 | transformer | 0.325 [0.250, 0.415] | p=0.427 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | start_points | frac:0.5 | rmse_h200 | dlinear | 0.978 [0.884, 1.073] | p=0.276 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | start_points | frac:0.5 | rmse_h200 | elasticnet | 1.154 [0.898, 1.469] | p=0.193 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | start_points | frac:0.5 | rmse_h200 | gru | 4.767 [4.075, 5.498] | p=6.55e-11 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | start_points | frac:0.5 | rmse_h200 | itransformer | 0.552 [0.391, 0.759] | p=0.961 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | start_points | frac:0.5 | rmse_h200 | itransformer_sc | 0.595 [0.443, 0.775] | p=0.961 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | start_points | frac:0.5 | rmse_h200 | last_slope | 0.734 [0.559, 0.923] |  |  | 40 | 5 | c733fae1 |
| test2 | start_points | frac:0.5 | rmse_h200 | lgbm | 2.097 [1.806, 2.390] | p=3.48e-07 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | start_points | frac:0.5 | rmse_h200 | lstm | 1.957 [1.647, 2.277] | p=3.49e-06 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | start_points | frac:0.5 | rmse_h200 | nlinear | 1.034 [0.884, 1.185] | p=0.276 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | start_points | frac:0.5 | rmse_h200 | patchtst | 0.641 [0.493, 0.795] | p=0.961 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | start_points | frac:0.5 | rmse_h200 | persistence | 2.027 [1.721, 2.393] | p=2.74e-09 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | start_points | frac:0.5 | rmse_h200 | rlinear | 0.778 [0.626, 0.952] | p=0.961 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | start_points | frac:0.5 | rmse_h200 | transformer | 0.937 [0.763, 1.149] | p=0.961 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | start_points | frac:0.5 | rmse_h50 | dlinear | 0.351 [0.334, 0.370] | p=3.06e-10 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | start_points | frac:0.5 | rmse_h50 | elasticnet | 0.243 [0.204, 0.282] | p=0.000537 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | start_points | frac:0.5 | rmse_h50 | gru | 0.475 [0.397, 0.555] | p=6.43e-08 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | start_points | frac:0.5 | rmse_h50 | itransformer | 0.056 [0.043, 0.071] | p=0.3 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | start_points | frac:0.5 | rmse_h50 | itransformer_sc | 0.065 [0.046, 0.089] | p=0.229 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | start_points | frac:0.5 | rmse_h50 | last_slope | 0.105 [0.072, 0.145] |  |  | 40 | 5 | c733fae1 |
| test2 | start_points | frac:0.5 | rmse_h50 | lgbm | 0.220 [0.188, 0.251] | p=0.000526 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | start_points | frac:0.5 | rmse_h50 | lstm | 0.219 [0.181, 0.260] | p=0.00119 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | start_points | frac:0.5 | rmse_h50 | nlinear | 0.124 [0.101, 0.151] | p=0.229 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | start_points | frac:0.5 | rmse_h50 | patchtst | 0.056 [0.044, 0.069] | p=0.229 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | start_points | frac:0.5 | rmse_h50 | persistence | 0.377 [0.325, 0.443] | p=7.84e-08 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | start_points | frac:0.5 | rmse_h50 | rlinear | 0.097 [0.075, 0.122] | p=0.501 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | start_points | frac:0.5 | rmse_h50 | transformer | 0.128 [0.107, 0.150] | p=0.229 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | start_points | frac:0.7 | rmse_h1 | dlinear | 0.009 [0.005, 0.015] | p=0.0158 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | start_points | frac:0.7 | rmse_h1 | elasticnet | 0.013 [0.009, 0.019] | p=0.00187 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | start_points | frac:0.7 | rmse_h1 | gru | 0.104 [0.076, 0.137] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | start_points | frac:0.7 | rmse_h1 | itransformer | 0.008 [0.004, 0.014] | p=0.952 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | start_points | frac:0.7 | rmse_h1 | itransformer_sc | 0.008 [0.004, 0.014] | p=0.952 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | start_points | frac:0.7 | rmse_h1 | last_slope | 0.008 [0.004, 0.014] |  |  | 40 | 5 | c733fae1 |
| test2 | start_points | frac:0.7 | rmse_h1 | lgbm | 0.013 [0.008, 0.019] | p=0.00559 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | start_points | frac:0.7 | rmse_h1 | lstm | 0.017 [0.012, 0.024] | p=5.46e-11 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | start_points | frac:0.7 | rmse_h1 | nlinear | 0.008 [0.004, 0.014] | p=0.711 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | start_points | frac:0.7 | rmse_h1 | patchtst | 0.008 [0.004, 0.014] | p=0.544 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | start_points | frac:0.7 | rmse_h1 | persistence | 0.017 [0.013, 0.024] | p=7.06e-08 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | start_points | frac:0.7 | rmse_h1 | rlinear | 0.009 [0.005, 0.015] | p=0.544 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | start_points | frac:0.7 | rmse_h1 | transformer | 0.105 [0.096, 0.114] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | start_points | frac:0.7 | rmse_h10 | dlinear | 0.030 [0.029, 0.032] | p=1.83e-05 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | start_points | frac:0.7 | rmse_h10 | elasticnet | 0.018 [0.014, 0.023] | p=0.984 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | start_points | frac:0.7 | rmse_h10 | gru | 0.129 [0.092, 0.175] | p=5.46e-11 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | start_points | frac:0.7 | rmse_h10 | itransformer | 0.013 [0.010, 0.015] | p=0.984 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | start_points | frac:0.7 | rmse_h10 | itransformer_sc | 0.015 [0.012, 0.018] | p=0.984 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | start_points | frac:0.7 | rmse_h10 | last_slope | 0.016 [0.012, 0.021] |  |  | 40 | 5 | c733fae1 |
| test2 | start_points | frac:0.7 | rmse_h10 | lgbm | 0.051 [0.040, 0.063] | p=9.25e-05 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | start_points | frac:0.7 | rmse_h10 | lstm | 0.041 [0.034, 0.048] | p=1.83e-05 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | start_points | frac:0.7 | rmse_h10 | nlinear | 0.013 [0.010, 0.015] | p=0.984 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | start_points | frac:0.7 | rmse_h10 | patchtst | 0.013 [0.010, 0.016] | p=0.984 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | start_points | frac:0.7 | rmse_h10 | persistence | 0.137 [0.120, 0.157] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | start_points | frac:0.7 | rmse_h10 | rlinear | 0.011 [0.009, 0.014] | p=0.103 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | start_points | frac:0.7 | rmse_h10 | transformer | 0.100 [0.092, 0.108] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | start_points | frac:0.7 | rmse_h100 | dlinear | 0.358 [0.334, 0.387] | p=8.36e-05 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | start_points | frac:0.7 | rmse_h100 | elasticnet | 0.500 [0.381, 0.628] | p=1 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | start_points | frac:0.7 | rmse_h100 | gru | 1.562 [1.366, 1.762] | p=2.44e-07 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | start_points | frac:0.7 | rmse_h100 | itransformer | 0.221 [0.184, 0.263] | p=6.75e-09 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | start_points | frac:0.7 | rmse_h100 | itransformer_sc | 0.162 [0.124, 0.201] | p=3.38e-09 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | start_points | frac:0.7 | rmse_h100 | last_slope | 0.552 [0.465, 0.645] |  |  | 40 | 5 | c733fae1 |
| test2 | start_points | frac:0.7 | rmse_h100 | lgbm | 0.548 [0.452, 0.649] | p=1 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | start_points | frac:0.7 | rmse_h100 | lstm | 0.559 [0.489, 0.636] | p=1 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | start_points | frac:0.7 | rmse_h100 | nlinear | 0.171 [0.129, 0.216] | p=7.24e-08 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | start_points | frac:0.7 | rmse_h100 | patchtst | 0.332 [0.266, 0.403] | p=8.36e-05 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | start_points | frac:0.7 | rmse_h100 | persistence | 1.851 [1.624, 2.088] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | start_points | frac:0.7 | rmse_h100 | rlinear | 0.163 [0.114, 0.223] | p=1.75e-08 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | start_points | frac:0.7 | rmse_h100 | transformer | 0.289 [0.241, 0.344] | p=3.22e-05 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | start_points | frac:0.7 | rmse_h200 | dlinear | 2.966 [2.424, 3.548] | p=9.2e-09 (vs last_slope) |  | 38 | 5 | 0b00c3d4 |
| test2 | start_points | frac:0.7 | rmse_h200 | elasticnet | 2.163 [1.609, 2.748] | p=6.19e-06 (vs last_slope) |  | 38 | 5 | 4c070a82 |
| test2 | start_points | frac:0.7 | rmse_h200 | gru | 4.021 [3.329, 4.720] | p=0.473 (vs last_slope) |  | 38 | 5 | 74f02c88 |
| test2 | start_points | frac:0.7 | rmse_h200 | itransformer | 1.222 [0.892, 1.631] | p=8.73e-11 (vs last_slope) |  | 38 | 5 | 0ce99716 |
| test2 | start_points | frac:0.7 | rmse_h200 | itransformer_sc | 1.553 [1.192, 1.958] | p=8.73e-11 (vs last_slope) |  | 38 | 5 | aa089496 |
| test2 | start_points | frac:0.7 | rmse_h200 | last_slope | 3.641 [3.098, 4.238] |  |  | 38 | 5 | c733fae1 |
| test2 | start_points | frac:0.7 | rmse_h200 | lgbm | 1.274 [1.019, 1.550] | p=6.91e-08 (vs last_slope) |  | 38 | 5 | 7c413ce2 |
| test2 | start_points | frac:0.7 | rmse_h200 | lstm | 1.412 [1.135, 1.756] | p=6.91e-08 (vs last_slope) |  | 38 | 5 | cc4f6edb |
| test2 | start_points | frac:0.7 | rmse_h200 | nlinear | 2.606 [2.080, 3.167] | p=6.11e-10 (vs last_slope) |  | 38 | 5 | 60722fba |
| test2 | start_points | frac:0.7 | rmse_h200 | patchtst | 1.640 [1.258, 2.071] | p=1.16e-10 (vs last_slope) |  | 38 | 5 | 73deb6e0 |
| test2 | start_points | frac:0.7 | rmse_h200 | persistence | 6.059 [5.290, 6.846] | p=8.73e-11 (vs last_slope) |  | 38 | 5 | 84662b2e |
| test2 | start_points | frac:0.7 | rmse_h200 | rlinear | 1.777 [1.392, 2.205] | p=8.73e-11 (vs last_slope) |  | 38 | 5 | ee0fc6f5 |
| test2 | start_points | frac:0.7 | rmse_h200 | transformer | 1.544 [1.162, 1.984] | p=1.53e-10 (vs last_slope) |  | 38 | 5 | eb07a039 |
| test2 | start_points | frac:0.7 | rmse_h50 | dlinear | 0.191 [0.170, 0.214] | p=0.0183 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | start_points | frac:0.7 | rmse_h50 | elasticnet | 0.289 [0.255, 0.325] | p=3.48e-07 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | start_points | frac:0.7 | rmse_h50 | gru | 0.528 [0.449, 0.607] | p=2.97e-08 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | start_points | frac:0.7 | rmse_h50 | itransformer | 0.056 [0.046, 0.066] | p=0.000163 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | start_points | frac:0.7 | rmse_h50 | itransformer_sc | 0.059 [0.046, 0.072] | p=0.000707 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | start_points | frac:0.7 | rmse_h50 | last_slope | 0.125 [0.099, 0.155] |  |  | 40 | 5 | c733fae1 |
| test2 | start_points | frac:0.7 | rmse_h50 | lgbm | 0.188 [0.153, 0.223] | p=0.0749 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | start_points | frac:0.7 | rmse_h50 | lstm | 0.175 [0.152, 0.199] | p=0.0333 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | start_points | frac:0.7 | rmse_h50 | nlinear | 0.069 [0.055, 0.084] | p=0.0333 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | start_points | frac:0.7 | rmse_h50 | patchtst | 0.087 [0.070, 0.105] | p=0.0749 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | start_points | frac:0.7 | rmse_h50 | persistence | 0.771 [0.675, 0.874] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | start_points | frac:0.7 | rmse_h50 | rlinear | 0.058 [0.044, 0.074] | p=0.000617 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | start_points | frac:0.7 | rmse_h50 | transformer | 0.133 [0.117, 0.150] | p=0.265 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | start_points | overall | rmse_h1 | dlinear | 0.016 [0.009, 0.023] | p=1.79e-05 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | start_points | overall | rmse_h1 | elasticnet | 0.018 [0.012, 0.025] | p=2.83e-06 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | start_points | overall | rmse_h1 | gru | 0.079 [0.064, 0.099] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | start_points | overall | rmse_h1 | itransformer | 0.013 [0.007, 0.019] | p=0.0601 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | start_points | overall | rmse_h1 | itransformer_sc | 0.014 [0.008, 0.021] | p=0.526 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | start_points | overall | rmse_h1 | last_slope | 0.014 [0.008, 0.022] |  |  | 40 | 5 | c733fae1 |
| test2 | start_points | overall | rmse_h1 | lgbm | 0.018 [0.012, 0.024] | p=0.00124 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | start_points | overall | rmse_h1 | lstm | 0.021 [0.015, 0.028] | p=6.75e-09 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | start_points | overall | rmse_h1 | nlinear | 0.014 [0.008, 0.022] | p=1 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | start_points | overall | rmse_h1 | patchtst | 0.013 [0.007, 0.019] | p=0.526 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | start_points | overall | rmse_h1 | persistence | 0.018 [0.012, 0.025] | p=2.91e-05 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | start_points | overall | rmse_h1 | rlinear | 0.012 [0.008, 0.018] | p=1 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | start_points | overall | rmse_h1 | transformer | 0.115 [0.106, 0.124] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | start_points | overall | rmse_h10 | dlinear | 0.041 [0.036, 0.048] | p=5.29e-05 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | start_points | overall | rmse_h10 | elasticnet | 0.029 [0.024, 0.035] | p=0.368 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | start_points | overall | rmse_h10 | gru | 0.095 [0.073, 0.121] | p=8.13e-09 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | start_points | overall | rmse_h10 | itransformer | 0.020 [0.016, 0.026] | p=2.71e-06 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | start_points | overall | rmse_h10 | itransformer_sc | 0.024 [0.018, 0.030] | p=5.2e-05 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | start_points | overall | rmse_h10 | last_slope | 0.032 [0.025, 0.040] |  |  | 40 | 5 | c733fae1 |
| test2 | start_points | overall | rmse_h10 | lgbm | 0.056 [0.048, 0.064] | p=3.88e-06 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | start_points | overall | rmse_h10 | lstm | 0.046 [0.040, 0.054] | p=0.000265 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | start_points | overall | rmse_h10 | nlinear | 0.026 [0.020, 0.035] | p=0.00221 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | start_points | overall | rmse_h10 | patchtst | 0.020 [0.015, 0.026] | p=1.31e-06 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | start_points | overall | rmse_h10 | persistence | 0.090 [0.078, 0.105] | p=2.2e-09 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | start_points | overall | rmse_h10 | rlinear | 0.020 [0.016, 0.025] | p=4.03e-07 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | start_points | overall | rmse_h10 | transformer | 0.096 [0.091, 0.102] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | start_points | overall | rmse_h100 | dlinear | 0.486 [0.461, 0.514] | p=8.32e-05 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | start_points | overall | rmse_h100 | elasticnet | 0.581 [0.487, 0.685] | p=0.000246 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | start_points | overall | rmse_h100 | gru | 1.373 [1.194, 1.564] | p=6.6e-10 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | start_points | overall | rmse_h100 | itransformer | 0.186 [0.152, 0.228] | p=1.63e-06 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | start_points | overall | rmse_h100 | itransformer_sc | 0.239 [0.165, 0.336] | p=0.000461 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | start_points | overall | rmse_h100 | last_slope | 0.364 [0.324, 0.407] |  |  | 40 | 5 | c733fae1 |
| test2 | start_points | overall | rmse_h100 | lgbm | 0.599 [0.544, 0.662] | p=7.82e-06 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | start_points | overall | rmse_h100 | lstm | 0.635 [0.535, 0.756] | p=0.000137 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | start_points | overall | rmse_h100 | nlinear | 0.363 [0.317, 0.418] | p=0.826 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | start_points | overall | rmse_h100 | patchtst | 0.245 [0.213, 0.279] | p=0.000246 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | start_points | overall | rmse_h100 | persistence | 1.088 [0.945, 1.248] | p=4.37e-11 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | start_points | overall | rmse_h100 | rlinear | 0.265 [0.202, 0.343] | p=0.00253 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | start_points | overall | rmse_h100 | transformer | 0.302 [0.231, 0.390] | p=0.0431 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | start_points | overall | rmse_h200 | dlinear | 1.926 [1.733, 2.137] | p=1 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | start_points | overall | rmse_h200 | elasticnet | 1.537 [1.261, 1.838] | p=0.0413 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | start_points | overall | rmse_h200 | gru | 4.058 [3.451, 4.720] | p=2.79e-05 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | start_points | overall | rmse_h200 | itransformer | 0.868 [0.667, 1.100] | p=2.5e-06 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | start_points | overall | rmse_h200 | itransformer_sc | 1.205 [0.960, 1.497] | p=0.000147 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | start_points | overall | rmse_h200 | last_slope | 1.874 [1.616, 2.152] |  |  | 40 | 5 | c733fae1 |
| test2 | start_points | overall | rmse_h200 | lgbm | 1.872 [1.703, 2.054] | p=1 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | start_points | overall | rmse_h200 | lstm | 1.775 [1.486, 2.118] | p=0.732 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | start_points | overall | rmse_h200 | nlinear | 1.868 [1.699, 2.055] | p=1 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | start_points | overall | rmse_h200 | patchtst | 1.169 [0.977, 1.380] | p=2.01e-05 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | start_points | overall | rmse_h200 | persistence | 3.330 [2.943, 3.720] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | start_points | overall | rmse_h200 | rlinear | 1.304 [1.077, 1.563] | p=0.000229 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | start_points | overall | rmse_h200 | transformer | 1.188 [0.995, 1.399] | p=1.41e-05 (vs last_slope) |  | 40 | 5 | eb07a039 |
| test2 | start_points | overall | rmse_h50 | dlinear | 0.367 [0.354, 0.382] | p=2.18e-11 (vs last_slope) |  | 40 | 5 | 0b00c3d4 |
| test2 | start_points | overall | rmse_h50 | elasticnet | 0.286 [0.256, 0.316] | p=3.89e-08 (vs last_slope) |  | 40 | 5 | 4c070a82 |
| test2 | start_points | overall | rmse_h50 | gru | 0.444 [0.382, 0.508] | p=2e-09 (vs last_slope) |  | 40 | 5 | 74f02c88 |
| test2 | start_points | overall | rmse_h50 | itransformer | 0.070 [0.059, 0.082] | p=4.05e-07 (vs last_slope) |  | 40 | 5 | 0ce99716 |
| test2 | start_points | overall | rmse_h50 | itransformer_sc | 0.084 [0.062, 0.112] | p=0.000272 (vs last_slope) |  | 40 | 5 | aa089496 |
| test2 | start_points | overall | rmse_h50 | last_slope | 0.133 [0.113, 0.154] |  |  | 40 | 5 | c733fae1 |
| test2 | start_points | overall | rmse_h50 | lgbm | 0.222 [0.202, 0.241] | p=2.33e-06 (vs last_slope) |  | 40 | 5 | 7c413ce2 |
| test2 | start_points | overall | rmse_h50 | lstm | 0.213 [0.183, 0.246] | p=0.000353 (vs last_slope) |  | 40 | 5 | cc4f6edb |
| test2 | start_points | overall | rmse_h50 | nlinear | 0.120 [0.098, 0.145] | p=0.628 (vs last_slope) |  | 40 | 5 | 60722fba |
| test2 | start_points | overall | rmse_h50 | patchtst | 0.077 [0.066, 0.089] | p=1.59e-06 (vs last_slope) |  | 40 | 5 | 73deb6e0 |
| test2 | start_points | overall | rmse_h50 | persistence | 0.472 [0.408, 0.547] | p=1e-10 (vs last_slope) |  | 40 | 5 | 84662b2e |
| test2 | start_points | overall | rmse_h50 | rlinear | 0.094 [0.073, 0.119] | p=0.00227 (vs last_slope) |  | 40 | 5 | ee0fc6f5 |
| test2 | start_points | overall | rmse_h50 | transformer | 0.134 [0.115, 0.156] | p=0.952 (vs last_slope) |  | 40 | 5 | eb07a039 |

</details>

<details><summary>toyota_rul (330 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rul_bias | dlinear | -44.260 [-99.273, 0.420] |  |  | 43 | 5 | c066ff8c |
| test1 | all | overall | rul_bias | elasticnet | -12.528 [-64.015, 30.411] |  |  | 43 | 5 | 6228f90c |
| test1 | all | overall | rul_bias | gru | -20.631 [-56.541, 11.310] |  |  | 43 | 5 | 68c083f5 |
| test1 | all | overall | rul_bias | itransformer | -31.525 [-66.927, -2.215] |  |  | 43 | 5 | 1f7dadba |
| test1 | all | overall | rul_bias | itransformer_sc | -28.416 [-61.221, -1.262] |  |  | 43 | 5 | 4a0a69dd |
| test1 | all | overall | rul_bias | lgbm | -23.120 [-50.100, -0.588] |  |  | 43 | 5 | b88b5644 |
| test1 | all | overall | rul_bias | lstm | -9.795 [-39.561, 17.630] |  |  | 43 | 5 | 7a6e2343 |
| test1 | all | overall | rul_bias | nlinear | -44.156 [-99.174, 0.535] |  |  | 43 | 5 | f6a02b2d |
| test1 | all | overall | rul_bias | patchtst | -95.532 [-162.099, -30.432] |  |  | 43 | 5 | 5b64c567 |
| test1 | all | overall | rul_bias | rlinear | -301.601 [-368.495, -243.918] |  |  | 43 | 5 | aa9b25f1 |
| test1 | all | overall | rul_bias | transformer | -12.996 [-50.053, 21.158] |  |  | 43 | 5 | cd2ed4cc |
| test1 | all | overall | rul_mae | dlinear | 134.275 [96.428, 182.072] |  |  | 43 | 5 | c066ff8c |
| test1 | all | overall | rul_mae | elasticnet | 110.004 [78.385, 150.217] |  |  | 43 | 5 | 6228f90c |
| test1 | all | overall | rul_mae | gru | 80.826 [57.844, 108.591] |  |  | 43 | 5 | 68c083f5 |
| test1 | all | overall | rul_mae | itransformer | 78.362 [54.298, 108.739] |  |  | 43 | 5 | 1f7dadba |
| test1 | all | overall | rul_mae | itransformer_sc | 76.097 [53.084, 105.406] |  |  | 43 | 5 | 4a0a69dd |
| test1 | all | overall | rul_mae | lgbm | 57.869 [39.443, 80.381] |  |  | 43 | 5 | b88b5644 |
| test1 | all | overall | rul_mae | lstm | 70.208 [51.137, 93.125] |  |  | 43 | 5 | 7a6e2343 |
| test1 | all | overall | rul_mae | nlinear | 134.312 [96.475, 182.102] |  |  | 43 | 5 | f6a02b2d |
| test1 | all | overall | rul_mae | patchtst | 250.500 [204.828, 304.197] |  |  | 43 | 5 | 5b64c567 |
| test1 | all | overall | rul_mae | rlinear | 339.280 [287.944, 399.732] |  |  | 43 | 5 | aa9b25f1 |
| test1 | all | overall | rul_mae | transformer | 88.107 [64.229, 115.516] |  |  | 43 | 5 | cd2ed4cc |
| test1 | start_points | fixed:100 | rul_bias | dlinear | -221.932 [-343.355, -122.303] |  |  | 43 | 5 | c066ff8c |
| test1 | start_points | fixed:100 | rul_bias | elasticnet | -62.499 [-161.917, 20.467] |  |  | 43 | 5 | 6228f90c |
| test1 | start_points | fixed:100 | rul_bias | gru | -79.038 [-144.022, -25.414] |  |  | 43 | 5 | 68c083f5 |
| test1 | start_points | fixed:100 | rul_bias | itransformer | -66.139 [-138.242, -5.664] |  |  | 43 | 5 | 1f7dadba |
| test1 | start_points | fixed:100 | rul_bias | itransformer_sc | -112.070 [-215.391, -27.295] |  |  | 43 | 5 | 4a0a69dd |
| test1 | start_points | fixed:100 | rul_bias | lgbm | -68.696 [-126.052, -22.520] |  |  | 43 | 5 | b88b5644 |
| test1 | start_points | fixed:100 | rul_bias | lstm | -53.975 [-104.738, -11.548] |  |  | 43 | 5 | 7a6e2343 |
| test1 | start_points | fixed:100 | rul_bias | nlinear | -221.837 [-343.272, -122.228] |  |  | 43 | 5 | f6a02b2d |
| test1 | start_points | fixed:100 | rul_bias | patchtst | -457.366 [-587.807, -346.408] |  |  | 43 | 5 | 5b64c567 |
| test1 | start_points | fixed:100 | rul_bias | rlinear | -595.083 [-723.749, -483.625] |  |  | 43 | 5 | aa9b25f1 |
| test1 | start_points | fixed:100 | rul_bias | transformer | -65.516 [-143.081, 0.340] |  |  | 43 | 5 | cd2ed4cc |
| test1 | start_points | fixed:100 | rul_mae | dlinear | 238.900 [142.043, 357.797] |  |  | 43 | 5 | c066ff8c |
| test1 | start_points | fixed:100 | rul_mae | elasticnet | 186.727 [119.897, 270.325] |  |  | 43 | 5 | 6228f90c |
| test1 | start_points | fixed:100 | rul_mae | gru | 126.724 [81.034, 183.905] |  |  | 43 | 5 | 68c083f5 |
| test1 | start_points | fixed:100 | rul_mae | itransformer | 151.913 [106.292, 210.226] |  |  | 43 | 5 | 1f7dadba |
| test1 | start_points | fixed:100 | rul_mae | itransformer_sc | 192.952 [121.012, 283.806] |  |  | 43 | 5 | 4a0a69dd |
| test1 | start_points | fixed:100 | rul_mae | lgbm | 102.137 [61.111, 154.631] |  |  | 43 | 5 | b88b5644 |
| test1 | start_points | fixed:100 | rul_mae | lstm | 102.593 [68.017, 146.076] |  |  | 43 | 5 | 7a6e2343 |
| test1 | start_points | fixed:100 | rul_mae | nlinear | 238.924 [142.090, 357.833] |  |  | 43 | 5 | f6a02b2d |
| test1 | start_points | fixed:100 | rul_mae | patchtst | 459.701 [349.868, 589.065] |  |  | 43 | 5 | 5b64c567 |
| test1 | start_points | fixed:100 | rul_mae | rlinear | 601.258 [493.876, 726.394] |  |  | 43 | 5 | aa9b25f1 |
| test1 | start_points | fixed:100 | rul_mae | transformer | 147.868 [93.735, 214.277] |  |  | 43 | 5 | cd2ed4cc |
| test1 | start_points | frac:0.3 | alpha_lambda_acc | dlinear | 0.558 [0.419, 0.698] |  |  | 43 | 5 | c066ff8c |
| test1 | start_points | frac:0.3 | alpha_lambda_acc | elasticnet | 0.465 [0.326, 0.605] |  |  | 43 | 5 | 6228f90c |
| test1 | start_points | frac:0.3 | alpha_lambda_acc | gru | 0.642 [0.512, 0.763] |  |  | 43 | 5 | 68c083f5 |
| test1 | start_points | frac:0.3 | alpha_lambda_acc | itransformer | 0.516 [0.377, 0.651] |  |  | 43 | 5 | 1f7dadba |
| test1 | start_points | frac:0.3 | alpha_lambda_acc | itransformer_sc | 0.628 [0.488, 0.758] |  |  | 43 | 5 | 4a0a69dd |
| test1 | start_points | frac:0.3 | alpha_lambda_acc | lgbm | 0.767 [0.628, 0.884] |  |  | 43 | 5 | b88b5644 |
| test1 | start_points | frac:0.3 | alpha_lambda_acc | lstm | 0.679 [0.563, 0.791] |  |  | 43 | 5 | 7a6e2343 |
| test1 | start_points | frac:0.3 | alpha_lambda_acc | nlinear | 0.558 [0.419, 0.698] |  |  | 43 | 5 | f6a02b2d |
| test1 | start_points | frac:0.3 | alpha_lambda_acc | patchtst | 0.112 [0.042, 0.195] |  |  | 43 | 5 | 5b64c567 |
| test1 | start_points | frac:0.3 | alpha_lambda_acc | rlinear | 0.000 [0.000, 0.000] |  |  | 43 | 5 | aa9b25f1 |
| test1 | start_points | frac:0.3 | alpha_lambda_acc | transformer | 0.623 [0.488, 0.753] |  |  | 43 | 5 | cd2ed4cc |
| test1 | start_points | frac:0.3 | rul_bias | dlinear | -118.150 [-201.153, -50.088] |  |  | 43 | 5 | c066ff8c |
| test1 | start_points | frac:0.3 | rul_bias | elasticnet | -36.029 [-109.067, 25.285] |  |  | 43 | 5 | 6228f90c |
| test1 | start_points | frac:0.3 | rul_bias | gru | -47.411 [-97.291, -5.165] |  |  | 43 | 5 | 68c083f5 |
| test1 | start_points | frac:0.3 | rul_bias | itransformer | -66.385 [-120.363, -20.905] |  |  | 43 | 5 | 1f7dadba |
| test1 | start_points | frac:0.3 | rul_bias | itransformer_sc | -68.867 [-122.549, -22.612] |  |  | 43 | 5 | 4a0a69dd |
| test1 | start_points | frac:0.3 | rul_bias | lgbm | -42.904 [-83.573, -8.743] |  |  | 43 | 5 | b88b5644 |
| test1 | start_points | frac:0.3 | rul_bias | lstm | -38.338 [-80.467, -2.337] |  |  | 43 | 5 | 7a6e2343 |
| test1 | start_points | frac:0.3 | rul_bias | nlinear | -118.300 [-201.497, -50.136] |  |  | 43 | 5 | f6a02b2d |
| test1 | start_points | frac:0.3 | rul_bias | patchtst | -195.897 [-312.241, -65.806] |  |  | 43 | 5 | 5b64c567 |
| test1 | start_points | frac:0.3 | rul_bias | rlinear | -473.832 [-561.165, -398.918] |  |  | 43 | 5 | aa9b25f1 |
| test1 | start_points | frac:0.3 | rul_bias | transformer | -37.711 [-88.866, 8.550] |  |  | 43 | 5 | cd2ed4cc |
| test1 | start_points | frac:0.3 | rul_mae | dlinear | 156.910 [95.383, 232.735] |  |  | 43 | 5 | c066ff8c |
| test1 | start_points | frac:0.3 | rul_mae | elasticnet | 143.252 [96.348, 203.087] |  |  | 43 | 5 | 6228f90c |
| test1 | start_points | frac:0.3 | rul_mae | gru | 98.879 [65.277, 141.517] |  |  | 43 | 5 | 68c083f5 |
| test1 | start_points | frac:0.3 | rul_mae | itransformer | 111.156 [73.827, 157.804] |  |  | 43 | 5 | 1f7dadba |
| test1 | start_points | frac:0.3 | rul_mae | itransformer_sc | 112.683 [74.474, 160.316] |  |  | 43 | 5 | 4a0a69dd |
| test1 | start_points | frac:0.3 | rul_mae | lgbm | 78.801 [50.399, 114.186] |  |  | 43 | 5 | b88b5644 |
| test1 | start_points | frac:0.3 | rul_mae | lstm | 87.672 [59.646, 122.986] |  |  | 43 | 5 | 7a6e2343 |
| test1 | start_points | frac:0.3 | rul_mae | nlinear | 157.262 [95.640, 233.355] |  |  | 43 | 5 | f6a02b2d |
| test1 | start_points | frac:0.3 | rul_mae | patchtst | 326.646 [242.859, 431.861] |  |  | 43 | 5 | 5b64c567 |
| test1 | start_points | frac:0.3 | rul_mae | rlinear | 475.003 [400.781, 561.807] |  |  | 43 | 5 | aa9b25f1 |
| test1 | start_points | frac:0.3 | rul_mae | transformer | 108.954 [73.026, 149.343] |  |  | 43 | 5 | cd2ed4cc |
| test1 | start_points | frac:0.5 | alpha_lambda_acc | dlinear | 0.377 [0.237, 0.521] |  |  | 43 | 5 | c066ff8c |
| test1 | start_points | frac:0.5 | alpha_lambda_acc | elasticnet | 0.488 [0.349, 0.628] |  |  | 43 | 5 | 6228f90c |
| test1 | start_points | frac:0.5 | alpha_lambda_acc | gru | 0.507 [0.372, 0.642] |  |  | 43 | 5 | 68c083f5 |
| test1 | start_points | frac:0.5 | alpha_lambda_acc | itransformer | 0.581 [0.447, 0.712] |  |  | 43 | 5 | 1f7dadba |
| test1 | start_points | frac:0.5 | alpha_lambda_acc | itransformer_sc | 0.633 [0.502, 0.758] |  |  | 43 | 5 | 4a0a69dd |
| test1 | start_points | frac:0.5 | alpha_lambda_acc | lgbm | 0.744 [0.605, 0.860] |  |  | 43 | 5 | b88b5644 |
| test1 | start_points | frac:0.5 | alpha_lambda_acc | lstm | 0.558 [0.433, 0.684] |  |  | 43 | 5 | 7a6e2343 |
| test1 | start_points | frac:0.5 | alpha_lambda_acc | nlinear | 0.395 [0.256, 0.535] |  |  | 43 | 5 | f6a02b2d |
| test1 | start_points | frac:0.5 | alpha_lambda_acc | patchtst | 0.260 [0.158, 0.367] |  |  | 43 | 5 | 5b64c567 |
| test1 | start_points | frac:0.5 | alpha_lambda_acc | rlinear | 0.000 [0.000, 0.000] |  |  | 43 | 5 | aa9b25f1 |
| test1 | start_points | frac:0.5 | alpha_lambda_acc | transformer | 0.558 [0.419, 0.698] |  |  | 43 | 5 | cd2ed4cc |
| test1 | start_points | frac:0.5 | rul_bias | dlinear | -2.772 [-59.944, 44.409] |  |  | 43 | 5 | c066ff8c |
| test1 | start_points | frac:0.5 | rul_bias | elasticnet | -6.969 [-58.528, 37.186] |  |  | 43 | 5 | 6228f90c |
| test1 | start_points | frac:0.5 | rul_bias | gru | -7.035 [-48.662, 34.062] |  |  | 43 | 5 | 68c083f5 |
| test1 | start_points | frac:0.5 | rul_bias | itransformer | -34.528 [-67.655, -5.871] |  |  | 43 | 5 | 1f7dadba |
| test1 | start_points | frac:0.5 | rul_bias | itransformer_sc | -5.665 [-26.964, 15.167] |  |  | 43 | 5 | 4a0a69dd |
| test1 | start_points | frac:0.5 | rul_bias | lgbm | -18.908 [-40.903, 1.919] |  |  | 43 | 5 | b88b5644 |
| test1 | start_points | frac:0.5 | rul_bias | lstm | -2.073 [-35.253, 28.910] |  |  | 43 | 5 | 7a6e2343 |
| test1 | start_points | frac:0.5 | rul_bias | nlinear | -3.146 [-60.381, 43.973] |  |  | 43 | 5 | f6a02b2d |
| test1 | start_points | frac:0.5 | rul_bias | patchtst | -82.847 [-148.458, -21.974] |  |  | 43 | 5 | 5b64c567 |
| test1 | start_points | frac:0.5 | rul_bias | rlinear | -280.131 [-366.336, -192.709] |  |  | 43 | 5 | aa9b25f1 |
| test1 | start_points | frac:0.5 | rul_bias | transformer | 8.906 [-23.632, 41.709] |  |  | 43 | 5 | cd2ed4cc |
| test1 | start_points | frac:0.5 | rul_mae | dlinear | 113.537 [79.053, 157.557] |  |  | 43 | 5 | c066ff8c |
| test1 | start_points | frac:0.5 | rul_mae | elasticnet | 103.068 [69.774, 144.333] |  |  | 43 | 5 | 6228f90c |
| test1 | start_points | frac:0.5 | rul_mae | gru | 90.895 [62.212, 125.730] |  |  | 43 | 5 | 68c083f5 |
| test1 | start_points | frac:0.5 | rul_mae | itransformer | 74.526 [52.755, 102.138] |  |  | 43 | 5 | 1f7dadba |
| test1 | start_points | frac:0.5 | rul_mae | itransformer_sc | 56.386 [44.265, 69.592] |  |  | 43 | 5 | 4a0a69dd |
| test1 | start_points | frac:0.5 | rul_mae | lgbm | 55.392 [41.383, 70.806] |  |  | 43 | 5 | b88b5644 |
| test1 | start_points | frac:0.5 | rul_mae | lstm | 75.438 [54.867, 100.339] |  |  | 43 | 5 | 7a6e2343 |
| test1 | start_points | frac:0.5 | rul_mae | nlinear | 113.261 [78.572, 157.412] |  |  | 43 | 5 | f6a02b2d |
| test1 | start_points | frac:0.5 | rul_mae | patchtst | 177.111 [134.349, 227.543] |  |  | 43 | 5 | 5b64c567 |
| test1 | start_points | frac:0.5 | rul_mae | rlinear | 350.356 [294.305, 414.218] |  |  | 43 | 5 | aa9b25f1 |
| test1 | start_points | frac:0.5 | rul_mae | transformer | 80.815 [59.382, 104.355] |  |  | 43 | 5 | cd2ed4cc |
| test1 | start_points | frac:0.7 | alpha_lambda_acc | dlinear | 0.070 [0.000, 0.163] |  |  | 43 | 5 | c066ff8c |
| test1 | start_points | frac:0.7 | alpha_lambda_acc | elasticnet | 0.372 [0.233, 0.512] |  |  | 43 | 5 | 6228f90c |
| test1 | start_points | frac:0.7 | alpha_lambda_acc | gru | 0.498 [0.367, 0.628] |  |  | 43 | 5 | 68c083f5 |
| test1 | start_points | frac:0.7 | alpha_lambda_acc | itransformer | 0.647 [0.516, 0.768] |  |  | 43 | 5 | 1f7dadba |
| test1 | start_points | frac:0.7 | alpha_lambda_acc | itransformer_sc | 0.800 [0.693, 0.898] |  |  | 43 | 5 | 4a0a69dd |
| test1 | start_points | frac:0.7 | alpha_lambda_acc | lgbm | 0.721 [0.581, 0.837] |  |  | 43 | 5 | b88b5644 |
| test1 | start_points | frac:0.7 | alpha_lambda_acc | lstm | 0.642 [0.521, 0.758] |  |  | 43 | 5 | 7a6e2343 |
| test1 | start_points | frac:0.7 | alpha_lambda_acc | nlinear | 0.070 [0.000, 0.163] |  |  | 43 | 5 | f6a02b2d |
| test1 | start_points | frac:0.7 | alpha_lambda_acc | patchtst | 0.172 [0.102, 0.251] |  |  | 43 | 5 | 5b64c567 |
| test1 | start_points | frac:0.7 | alpha_lambda_acc | rlinear | 0.051 [0.000, 0.126] |  |  | 43 | 5 | aa9b25f1 |
| test1 | start_points | frac:0.7 | alpha_lambda_acc | transformer | 0.391 [0.256, 0.530] |  |  | 43 | 5 | cd2ed4cc |
| test1 | start_points | frac:0.7 | rul_bias | dlinear | 84.322 [54.393, 109.057] |  |  | 43 | 5 | c066ff8c |
| test1 | start_points | frac:0.7 | rul_bias | elasticnet | 10.120 [-22.591, 38.979] |  |  | 43 | 5 | 6228f90c |
| test1 | start_points | frac:0.7 | rul_bias | gru | 3.607 [-21.427, 28.688] |  |  | 43 | 5 | 68c083f5 |
| test1 | start_points | frac:0.7 | rul_bias | itransformer | -5.880 [-27.353, 12.341] |  |  | 43 | 5 | 1f7dadba |
| test1 | start_points | frac:0.7 | rul_bias | itransformer_sc | 11.460 [1.661, 21.869] |  |  | 43 | 5 | 4a0a69dd |
| test1 | start_points | frac:0.7 | rul_bias | lgbm | -3.162 [-20.607, 12.096] |  |  | 43 | 5 | b88b5644 |
| test1 | start_points | frac:0.7 | rul_bias | lstm | -0.681 [-20.488, 17.617] |  |  | 43 | 5 | 7a6e2343 |
| test1 | start_points | frac:0.7 | rul_bias | nlinear | 84.594 [54.688, 109.260] |  |  | 43 | 5 | f6a02b2d |
| test1 | start_points | frac:0.7 | rul_bias | patchtst | 37.759 [-54.905, 157.418] |  |  | 43 | 5 | 5b64c567 |
| test1 | start_points | frac:0.7 | rul_bias | rlinear | -167.023 [-211.163, -128.177] |  |  | 43 | 5 | aa9b25f1 |
| test1 | start_points | frac:0.7 | rul_bias | transformer | 22.740 [-2.516, 51.240] |  |  | 43 | 5 | cd2ed4cc |
| test1 | start_points | frac:0.7 | rul_mae | dlinear | 116.460 [103.160, 131.065] |  |  | 43 | 5 | c066ff8c |
| test1 | start_points | frac:0.7 | rul_mae | elasticnet | 68.573 [47.095, 94.489] |  |  | 43 | 5 | 6228f90c |
| test1 | start_points | frac:0.7 | rul_mae | gru | 52.646 [35.441, 74.315] |  |  | 43 | 5 | 68c083f5 |
| test1 | start_points | frac:0.7 | rul_mae | itransformer | 39.725 [25.523, 57.737] |  |  | 43 | 5 | 1f7dadba |
| test1 | start_points | frac:0.7 | rul_mae | itransformer_sc | 26.830 [20.173, 34.566] |  |  | 43 | 5 | 4a0a69dd |
| test1 | start_points | frac:0.7 | rul_mae | lgbm | 34.074 [22.212, 48.577] |  |  | 43 | 5 | b88b5644 |
| test1 | start_points | frac:0.7 | rul_mae | lstm | 39.367 [25.711, 55.823] |  |  | 43 | 5 | 7a6e2343 |
| test1 | start_points | frac:0.7 | rul_mae | nlinear | 116.594 [103.365, 131.051] |  |  | 43 | 5 | f6a02b2d |
| test1 | start_points | frac:0.7 | rul_mae | patchtst | 184.711 [107.691, 289.317] |  |  | 43 | 5 | 5b64c567 |
| test1 | start_points | frac:0.7 | rul_mae | rlinear | 173.956 [138.698, 214.935] |  |  | 43 | 5 | aa9b25f1 |
| test1 | start_points | frac:0.7 | rul_mae | transformer | 62.256 [44.501, 84.829] |  |  | 43 | 5 | cd2ed4cc |
| test1 | start_points | overall | rul_bias | dlinear | -64.633 [-137.044, -5.768] |  |  | 43 | 5 | c066ff8c |
| test1 | start_points | overall | rul_bias | elasticnet | -23.844 [-86.557, 27.948] |  |  | 43 | 5 | 6228f90c |
| test1 | start_points | overall | rul_bias | gru | -32.469 [-75.761, 4.809] |  |  | 43 | 5 | 68c083f5 |
| test1 | start_points | overall | rul_bias | itransformer | -43.233 [-84.291, -8.220] |  |  | 43 | 5 | 1f7dadba |
| test1 | start_points | overall | rul_bias | itransformer_sc | -43.786 [-86.341, -7.933] |  |  | 43 | 5 | 4a0a69dd |
| test1 | start_points | overall | rul_bias | lgbm | -33.418 [-65.451, -6.116] |  |  | 43 | 5 | b88b5644 |
| test1 | start_points | overall | rul_bias | lstm | -23.767 [-58.708, 6.178] |  |  | 43 | 5 | 7a6e2343 |
| test1 | start_points | overall | rul_bias | nlinear | -64.672 [-137.006, -5.787] |  |  | 43 | 5 | f6a02b2d |
| test1 | start_points | overall | rul_bias | patchtst | -174.588 [-257.426, -95.738] |  |  | 43 | 5 | 5b64c567 |
| test1 | start_points | overall | rul_bias | rlinear | -379.017 [-463.393, -305.701] |  |  | 43 | 5 | aa9b25f1 |
| test1 | start_points | overall | rul_bias | transformer | -17.895 [-61.338, 22.204] |  |  | 43 | 5 | cd2ed4cc |
| test1 | start_points | overall | rul_mae | dlinear | 156.452 [108.107, 217.042] |  |  | 43 | 5 | c066ff8c |
| test1 | start_points | overall | rul_mae | elasticnet | 125.405 [85.423, 176.345] |  |  | 43 | 5 | 6228f90c |
| test1 | start_points | overall | rul_mae | gru | 92.286 [64.128, 127.250] |  |  | 43 | 5 | 68c083f5 |
| test1 | start_points | overall | rul_mae | itransformer | 94.330 [67.393, 128.161] |  |  | 43 | 5 | 1f7dadba |
| test1 | start_points | overall | rul_mae | itransformer_sc | 97.213 [68.566, 132.581] |  |  | 43 | 5 | 4a0a69dd |
| test1 | start_points | overall | rul_mae | lgbm | 67.601 [45.610, 94.968] |  |  | 43 | 5 | b88b5644 |
| test1 | start_points | overall | rul_mae | lstm | 76.267 [54.146, 104.259] |  |  | 43 | 5 | 7a6e2343 |
| test1 | start_points | overall | rul_mae | nlinear | 156.510 [108.240, 217.209] |  |  | 43 | 5 | f6a02b2d |
| test1 | start_points | overall | rul_mae | patchtst | 287.042 [234.037, 351.378] |  |  | 43 | 5 | 5b64c567 |
| test1 | start_points | overall | rul_mae | rlinear | 400.143 [333.537, 478.880] |  |  | 43 | 5 | aa9b25f1 |
| test1 | start_points | overall | rul_mae | transformer | 99.973 [71.229, 133.382] |  |  | 43 | 5 | cd2ed4cc |
| test2 | all | overall | rul_bias | dlinear | -167.540 [-212.404, -127.387] |  |  | 40 | 5 | c066ff8c |
| test2 | all | overall | rul_bias | elasticnet | -52.767 [-107.974, -1.619] |  |  | 40 | 5 | 6228f90c |
| test2 | all | overall | rul_bias | gru | -144.993 [-197.063, -96.673] |  |  | 40 | 5 | 68c083f5 |
| test2 | all | overall | rul_bias | itransformer | -36.230 [-71.422, -2.381] |  |  | 40 | 5 | 1f7dadba |
| test2 | all | overall | rul_bias | itransformer_sc | -33.784 [-53.995, -14.294] |  |  | 40 | 5 | 4a0a69dd |
| test2 | all | overall | rul_bias | lgbm | -171.747 [-215.617, -132.459] |  |  | 40 | 5 | b88b5644 |
| test2 | all | overall | rul_bias | lstm | -129.934 [-177.772, -86.976] |  |  | 40 | 5 | 7a6e2343 |
| test2 | all | overall | rul_bias | nlinear | -167.507 [-212.374, -127.358] |  |  | 40 | 5 | f6a02b2d |
| test2 | all | overall | rul_bias | patchtst | -437.991 [-486.825, -393.945] |  |  | 40 | 5 | 5b64c567 |
| test2 | all | overall | rul_bias | rlinear | -488.263 [-538.825, -441.936] |  |  | 40 | 5 | aa9b25f1 |
| test2 | all | overall | rul_bias | transformer | -164.100 [-215.206, -118.095] |  |  | 40 | 5 | cd2ed4cc |
| test2 | all | overall | rul_mae | dlinear | 228.638 [192.558, 270.241] |  |  | 40 | 5 | c066ff8c |
| test2 | all | overall | rul_mae | elasticnet | 144.845 [111.655, 181.870] |  |  | 40 | 5 | 6228f90c |
| test2 | all | overall | rul_mae | gru | 181.852 [144.439, 224.114] |  |  | 40 | 5 | 68c083f5 |
| test2 | all | overall | rul_mae | itransformer | 132.495 [114.716, 152.479] |  |  | 40 | 5 | 1f7dadba |
| test2 | all | overall | rul_mae | itransformer_sc | 119.174 [101.336, 138.518] |  |  | 40 | 5 | 4a0a69dd |
| test2 | all | overall | rul_mae | lgbm | 184.111 [146.696, 226.053] |  |  | 40 | 5 | b88b5644 |
| test2 | all | overall | rul_mae | lstm | 162.489 [126.112, 203.447] |  |  | 40 | 5 | 7a6e2343 |
| test2 | all | overall | rul_mae | nlinear | 228.602 [192.523, 270.195] |  |  | 40 | 5 | f6a02b2d |
| test2 | all | overall | rul_mae | patchtst | 439.806 [396.156, 488.354] |  |  | 40 | 5 | 5b64c567 |
| test2 | all | overall | rul_mae | rlinear | 500.895 [456.237, 550.052] |  |  | 40 | 5 | aa9b25f1 |
| test2 | all | overall | rul_mae | transformer | 197.530 [158.876, 241.623] |  |  | 40 | 5 | cd2ed4cc |
| test2 | start_points | fixed:100 | rul_bias | dlinear | -531.231 [-626.980, -444.332] |  |  | 40 | 5 | c066ff8c |
| test2 | start_points | fixed:100 | rul_bias | elasticnet | -212.430 [-311.900, -121.472] |  |  | 40 | 5 | 6228f90c |
| test2 | start_points | fixed:100 | rul_bias | gru | -349.316 [-444.789, -262.730] |  |  | 40 | 5 | 68c083f5 |
| test2 | start_points | fixed:100 | rul_bias | itransformer | -120.283 [-223.484, -18.632] |  |  | 40 | 5 | 1f7dadba |
| test2 | start_points | fixed:100 | rul_bias | itransformer_sc | -254.649 [-345.576, -171.233] |  |  | 40 | 5 | 4a0a69dd |
| test2 | start_points | fixed:100 | rul_bias | lgbm | -414.917 [-505.041, -333.963] |  |  | 40 | 5 | b88b5644 |
| test2 | start_points | fixed:100 | rul_bias | lstm | -353.845 [-449.767, -267.807] |  |  | 40 | 5 | 7a6e2343 |
| test2 | start_points | fixed:100 | rul_bias | nlinear | -531.150 [-626.914, -444.215] |  |  | 40 | 5 | f6a02b2d |
| test2 | start_points | fixed:100 | rul_bias | patchtst | -824.374 [-922.412, -736.061] |  |  | 40 | 5 | 5b64c567 |
| test2 | start_points | fixed:100 | rul_bias | rlinear | -923.463 [-1022.108, -833.581] |  |  | 40 | 5 | aa9b25f1 |
| test2 | start_points | fixed:100 | rul_bias | transformer | -404.021 [-498.547, -319.142] |  |  | 40 | 5 | cd2ed4cc |
| test2 | start_points | fixed:100 | rul_mae | dlinear | 531.231 [444.332, 626.980] |  |  | 40 | 5 | c066ff8c |
| test2 | start_points | fixed:100 | rul_mae | elasticnet | 263.586 [187.246, 350.342] |  |  | 40 | 5 | 6228f90c |
| test2 | start_points | fixed:100 | rul_mae | gru | 360.466 [278.680, 452.241] |  |  | 40 | 5 | 68c083f5 |
| test2 | start_points | fixed:100 | rul_mae | itransformer | 284.060 [224.437, 350.281] |  |  | 40 | 5 | 1f7dadba |
| test2 | start_points | fixed:100 | rul_mae | itransformer_sc | 273.979 [196.209, 359.777] |  |  | 40 | 5 | 4a0a69dd |
| test2 | start_points | fixed:100 | rul_mae | lgbm | 414.917 [333.963, 505.041] |  |  | 40 | 5 | b88b5644 |
| test2 | start_points | fixed:100 | rul_mae | lstm | 361.932 [279.115, 454.431] |  |  | 40 | 5 | 7a6e2343 |
| test2 | start_points | fixed:100 | rul_mae | nlinear | 531.150 [444.215, 626.914] |  |  | 40 | 5 | f6a02b2d |
| test2 | start_points | fixed:100 | rul_mae | patchtst | 824.374 [736.061, 922.412] |  |  | 40 | 5 | 5b64c567 |
| test2 | start_points | fixed:100 | rul_mae | rlinear | 923.463 [833.581, 1022.108] |  |  | 40 | 5 | aa9b25f1 |
| test2 | start_points | fixed:100 | rul_mae | transformer | 404.021 [319.142, 498.547] |  |  | 40 | 5 | cd2ed4cc |
| test2 | start_points | frac:0.3 | alpha_lambda_acc | dlinear | 0.025 [0.000, 0.075] |  |  | 40 | 5 | c066ff8c |
| test2 | start_points | frac:0.3 | alpha_lambda_acc | elasticnet | 0.450 [0.300, 0.600] |  |  | 40 | 5 | 6228f90c |
| test2 | start_points | frac:0.3 | alpha_lambda_acc | gru | 0.270 [0.155, 0.390] |  |  | 40 | 5 | 68c083f5 |
| test2 | start_points | frac:0.3 | alpha_lambda_acc | itransformer | 0.475 [0.340, 0.615] |  |  | 40 | 5 | 1f7dadba |
| test2 | start_points | frac:0.3 | alpha_lambda_acc | itransformer_sc | 0.540 [0.405, 0.675] |  |  | 40 | 5 | 4a0a69dd |
| test2 | start_points | frac:0.3 | alpha_lambda_acc | lgbm | 0.175 [0.075, 0.300] |  |  | 40 | 5 | b88b5644 |
| test2 | start_points | frac:0.3 | alpha_lambda_acc | lstm | 0.305 [0.190, 0.425] |  |  | 40 | 5 | 7a6e2343 |
| test2 | start_points | frac:0.3 | alpha_lambda_acc | nlinear | 0.025 [0.000, 0.075] |  |  | 40 | 5 | f6a02b2d |
| test2 | start_points | frac:0.3 | alpha_lambda_acc | patchtst | 0.000 [0.000, 0.000] |  |  | 40 | 5 | 5b64c567 |
| test2 | start_points | frac:0.3 | alpha_lambda_acc | rlinear | 0.000 [0.000, 0.000] |  |  | 40 | 5 | aa9b25f1 |
| test2 | start_points | frac:0.3 | alpha_lambda_acc | transformer | 0.240 [0.120, 0.370] |  |  | 40 | 5 | cd2ed4cc |
| test2 | start_points | frac:0.3 | rul_bias | dlinear | -328.151 [-395.010, -267.941] |  |  | 40 | 5 | c066ff8c |
| test2 | start_points | frac:0.3 | rul_bias | elasticnet | -112.012 [-190.197, -39.164] |  |  | 40 | 5 | 6228f90c |
| test2 | start_points | frac:0.3 | rul_bias | gru | -239.075 [-312.254, -170.560] |  |  | 40 | 5 | 68c083f5 |
| test2 | start_points | frac:0.3 | rul_bias | itransformer | -89.291 [-156.457, -22.510] |  |  | 40 | 5 | 1f7dadba |
| test2 | start_points | frac:0.3 | rul_bias | itransformer_sc | -43.804 [-98.573, 13.433] |  |  | 40 | 5 | 4a0a69dd |
| test2 | start_points | frac:0.3 | rul_bias | lgbm | -286.864 [-353.866, -225.713] |  |  | 40 | 5 | b88b5644 |
| test2 | start_points | frac:0.3 | rul_bias | lstm | -234.649 [-305.146, -169.889] |  |  | 40 | 5 | 7a6e2343 |
| test2 | start_points | frac:0.3 | rul_bias | nlinear | -328.121 [-394.945, -267.912] |  |  | 40 | 5 | f6a02b2d |
| test2 | start_points | frac:0.3 | rul_bias | patchtst | -645.687 [-711.650, -585.666] |  |  | 40 | 5 | 5b64c567 |
| test2 | start_points | frac:0.3 | rul_bias | rlinear | -713.790 [-782.849, -650.971] |  |  | 40 | 5 | aa9b25f1 |
| test2 | start_points | frac:0.3 | rul_bias | transformer | -276.122 [-346.355, -212.428] |  |  | 40 | 5 | cd2ed4cc |
| test2 | start_points | frac:0.3 | rul_mae | dlinear | 328.151 [267.941, 395.010] |  |  | 40 | 5 | c066ff8c |
| test2 | start_points | frac:0.3 | rul_mae | elasticnet | 194.827 [141.510, 254.214] |  |  | 40 | 5 | 6228f90c |
| test2 | start_points | frac:0.3 | rul_mae | gru | 261.424 [202.263, 326.586] |  |  | 40 | 5 | 68c083f5 |
| test2 | start_points | frac:0.3 | rul_mae | itransformer | 180.090 [136.261, 226.214] |  |  | 40 | 5 | 1f7dadba |
| test2 | start_points | frac:0.3 | rul_mae | itransformer_sc | 153.074 [122.136, 188.236] |  |  | 40 | 5 | 4a0a69dd |
| test2 | start_points | frac:0.3 | rul_mae | lgbm | 286.864 [225.713, 353.866] |  |  | 40 | 5 | b88b5644 |
| test2 | start_points | frac:0.3 | rul_mae | lstm | 246.427 [186.554, 312.404] |  |  | 40 | 5 | 7a6e2343 |
| test2 | start_points | frac:0.3 | rul_mae | nlinear | 328.121 [267.912, 394.945] |  |  | 40 | 5 | f6a02b2d |
| test2 | start_points | frac:0.3 | rul_mae | patchtst | 645.687 [585.666, 711.650] |  |  | 40 | 5 | 5b64c567 |
| test2 | start_points | frac:0.3 | rul_mae | rlinear | 713.790 [650.971, 782.849] |  |  | 40 | 5 | aa9b25f1 |
| test2 | start_points | frac:0.3 | rul_mae | transformer | 278.064 [215.329, 347.469] |  |  | 40 | 5 | cd2ed4cc |
| test2 | start_points | frac:0.5 | alpha_lambda_acc | dlinear | 0.500 [0.350, 0.650] |  |  | 40 | 5 | c066ff8c |
| test2 | start_points | frac:0.5 | alpha_lambda_acc | elasticnet | 0.500 [0.350, 0.650] |  |  | 40 | 5 | 6228f90c |
| test2 | start_points | frac:0.5 | alpha_lambda_acc | gru | 0.320 [0.205, 0.440] |  |  | 40 | 5 | 68c083f5 |
| test2 | start_points | frac:0.5 | alpha_lambda_acc | itransformer | 0.735 [0.600, 0.855] |  |  | 40 | 5 | 1f7dadba |
| test2 | start_points | frac:0.5 | alpha_lambda_acc | itransformer_sc | 0.835 [0.725, 0.935] |  |  | 40 | 5 | 4a0a69dd |
| test2 | start_points | frac:0.5 | alpha_lambda_acc | lgbm | 0.300 [0.150, 0.450] |  |  | 40 | 5 | b88b5644 |
| test2 | start_points | frac:0.5 | alpha_lambda_acc | lstm | 0.515 [0.375, 0.650] |  |  | 40 | 5 | 7a6e2343 |
| test2 | start_points | frac:0.5 | alpha_lambda_acc | nlinear | 0.500 [0.350, 0.650] |  |  | 40 | 5 | f6a02b2d |
| test2 | start_points | frac:0.5 | alpha_lambda_acc | patchtst | 0.000 [0.000, 0.000] |  |  | 40 | 5 | 5b64c567 |
| test2 | start_points | frac:0.5 | alpha_lambda_acc | rlinear | 0.000 [0.000, 0.000] |  |  | 40 | 5 | aa9b25f1 |
| test2 | start_points | frac:0.5 | alpha_lambda_acc | transformer | 0.315 [0.185, 0.450] |  |  | 40 | 5 | cd2ed4cc |
| test2 | start_points | frac:0.5 | rul_bias | dlinear | -129.164 [-175.722, -87.451] |  |  | 40 | 5 | c066ff8c |
| test2 | start_points | frac:0.5 | rul_bias | elasticnet | -41.501 [-101.038, 14.105] |  |  | 40 | 5 | 6228f90c |
| test2 | start_points | frac:0.5 | rul_bias | gru | -133.880 [-188.367, -82.858] |  |  | 40 | 5 | 68c083f5 |
| test2 | start_points | frac:0.5 | rul_bias | itransformer | -22.427 [-51.954, 7.921] |  |  | 40 | 5 | 1f7dadba |
| test2 | start_points | frac:0.5 | rul_bias | itransformer_sc | 30.412 [8.388, 54.008] |  |  | 40 | 5 | 4a0a69dd |
| test2 | start_points | frac:0.5 | rul_bias | lgbm | -149.904 [-194.480, -109.729] |  |  | 40 | 5 | b88b5644 |
| test2 | start_points | frac:0.5 | rul_bias | lstm | -110.106 [-158.928, -66.470] |  |  | 40 | 5 | 7a6e2343 |
| test2 | start_points | frac:0.5 | rul_bias | nlinear | -129.157 [-175.716, -87.429] |  |  | 40 | 5 | f6a02b2d |
| test2 | start_points | frac:0.5 | rul_bias | patchtst | -436.860 [-486.873, -392.026] |  |  | 40 | 5 | 5b64c567 |
| test2 | start_points | frac:0.5 | rul_bias | rlinear | -504.974 [-554.827, -459.448] |  |  | 40 | 5 | aa9b25f1 |
| test2 | start_points | frac:0.5 | rul_bias | transformer | -155.105 [-208.091, -106.597] |  |  | 40 | 5 | cd2ed4cc |
| test2 | start_points | frac:0.5 | rul_mae | dlinear | 132.525 [91.722, 178.692] |  |  | 40 | 5 | c066ff8c |
| test2 | start_points | frac:0.5 | rul_mae | elasticnet | 140.650 [102.924, 181.899] |  |  | 40 | 5 | 6228f90c |
| test2 | start_points | frac:0.5 | rul_mae | gru | 170.414 [131.613, 213.953] |  |  | 40 | 5 | 68c083f5 |
| test2 | start_points | frac:0.5 | rul_mae | itransformer | 75.052 [55.554, 96.928] |  |  | 40 | 5 | 1f7dadba |
| test2 | start_points | frac:0.5 | rul_mae | itransformer_sc | 62.254 [47.654, 78.965] |  |  | 40 | 5 | 4a0a69dd |
| test2 | start_points | frac:0.5 | rul_mae | lgbm | 153.251 [114.209, 196.369] |  |  | 40 | 5 | b88b5644 |
| test2 | start_points | frac:0.5 | rul_mae | lstm | 132.427 [94.335, 175.666] |  |  | 40 | 5 | 7a6e2343 |
| test2 | start_points | frac:0.5 | rul_mae | nlinear | 132.517 [91.717, 178.682] |  |  | 40 | 5 | f6a02b2d |
| test2 | start_points | frac:0.5 | rul_mae | patchtst | 436.860 [392.026, 486.873] |  |  | 40 | 5 | 5b64c567 |
| test2 | start_points | frac:0.5 | rul_mae | rlinear | 504.974 [459.448, 554.827] |  |  | 40 | 5 | aa9b25f1 |
| test2 | start_points | frac:0.5 | rul_mae | transformer | 172.830 [131.188, 220.697] |  |  | 40 | 5 | cd2ed4cc |
| test2 | start_points | frac:0.7 | alpha_lambda_acc | dlinear | 0.325 [0.200, 0.475] |  |  | 40 | 5 | c066ff8c |
| test2 | start_points | frac:0.7 | alpha_lambda_acc | elasticnet | 0.400 [0.250, 0.550] |  |  | 40 | 5 | 6228f90c |
| test2 | start_points | frac:0.7 | alpha_lambda_acc | gru | 0.370 [0.235, 0.510] |  |  | 40 | 5 | 68c083f5 |
| test2 | start_points | frac:0.7 | alpha_lambda_acc | itransformer | 0.570 [0.425, 0.710] |  |  | 40 | 5 | 1f7dadba |
| test2 | start_points | frac:0.7 | alpha_lambda_acc | itransformer_sc | 0.480 [0.335, 0.625] |  |  | 40 | 5 | 4a0a69dd |
| test2 | start_points | frac:0.7 | alpha_lambda_acc | lgbm | 0.775 [0.650, 0.900] |  |  | 40 | 5 | b88b5644 |
| test2 | start_points | frac:0.7 | alpha_lambda_acc | lstm | 0.695 [0.550, 0.830] |  |  | 40 | 5 | 7a6e2343 |
| test2 | start_points | frac:0.7 | alpha_lambda_acc | nlinear | 0.325 [0.200, 0.475] |  |  | 40 | 5 | f6a02b2d |
| test2 | start_points | frac:0.7 | alpha_lambda_acc | patchtst | 0.020 [0.000, 0.055] |  |  | 40 | 5 | 5b64c567 |
| test2 | start_points | frac:0.7 | alpha_lambda_acc | rlinear | 0.000 [0.000, 0.000] |  |  | 40 | 5 | aa9b25f1 |
| test2 | start_points | frac:0.7 | alpha_lambda_acc | transformer | 0.380 [0.245, 0.520] |  |  | 40 | 5 | cd2ed4cc |
| test2 | start_points | frac:0.7 | rul_bias | dlinear | 53.181 [28.374, 74.492] |  |  | 40 | 5 | c066ff8c |
| test2 | start_points | frac:0.7 | rul_bias | elasticnet | 44.927 [6.337, 82.990] |  |  | 40 | 5 | 6228f90c |
| test2 | start_points | frac:0.7 | rul_bias | gru | -22.034 [-59.496, 14.709] |  |  | 40 | 5 | 68c083f5 |
| test2 | start_points | frac:0.7 | rul_bias | itransformer | 40.358 [22.458, 57.528] |  |  | 40 | 5 | 1f7dadba |
| test2 | start_points | frac:0.7 | rul_bias | itransformer_sc | 70.290 [54.209, 86.978] |  |  | 40 | 5 | 4a0a69dd |
| test2 | start_points | frac:0.7 | rul_bias | lgbm | -26.797 [-46.370, -9.032] |  |  | 40 | 5 | b88b5644 |
| test2 | start_points | frac:0.7 | rul_bias | lstm | 8.838 [-15.835, 31.644] |  |  | 40 | 5 | 7a6e2343 |
| test2 | start_points | frac:0.7 | rul_bias | nlinear | 53.146 [28.353, 74.493] |  |  | 40 | 5 | f6a02b2d |
| test2 | start_points | frac:0.7 | rul_bias | patchtst | -273.524 [-306.655, -241.555] |  |  | 40 | 5 | 5b64c567 |
| test2 | start_points | frac:0.7 | rul_bias | rlinear | -291.450 [-322.438, -262.715] |  |  | 40 | 5 | aa9b25f1 |
| test2 | start_points | frac:0.7 | rul_bias | transformer | -28.197 [-64.400, 6.644] |  |  | 40 | 5 | cd2ed4cc |
| test2 | start_points | frac:0.7 | rul_mae | dlinear | 83.593 [71.552, 95.448] |  |  | 40 | 5 | c066ff8c |
| test2 | start_points | frac:0.7 | rul_mae | elasticnet | 99.159 [73.601, 126.482] |  |  | 40 | 5 | 6228f90c |
| test2 | start_points | frac:0.7 | rul_mae | gru | 96.599 [74.584, 119.871] |  |  | 40 | 5 | 68c083f5 |
| test2 | start_points | frac:0.7 | rul_mae | itransformer | 56.055 [43.534, 69.513] |  |  | 40 | 5 | 1f7dadba |
| test2 | start_points | frac:0.7 | rul_mae | itransformer_sc | 71.219 [55.661, 87.519] |  |  | 40 | 5 | 4a0a69dd |
| test2 | start_points | frac:0.7 | rul_mae | lgbm | 46.146 [32.550, 61.723] |  |  | 40 | 5 | b88b5644 |
| test2 | start_points | frac:0.7 | rul_mae | lstm | 53.717 [37.636, 71.341] |  |  | 40 | 5 | 7a6e2343 |
| test2 | start_points | frac:0.7 | rul_mae | nlinear | 83.569 [71.526, 95.436] |  |  | 40 | 5 | f6a02b2d |
| test2 | start_points | frac:0.7 | rul_mae | patchtst | 273.524 [241.555, 306.655] |  |  | 40 | 5 | 5b64c567 |
| test2 | start_points | frac:0.7 | rul_mae | rlinear | 291.450 [262.715, 322.438] |  |  | 40 | 5 | aa9b25f1 |
| test2 | start_points | frac:0.7 | rul_mae | transformer | 90.868 [68.963, 114.663] |  |  | 40 | 5 | cd2ed4cc |
| test2 | start_points | overall | rul_bias | dlinear | -233.841 [-292.308, -181.454] |  |  | 40 | 5 | c066ff8c |
| test2 | start_points | overall | rul_bias | elasticnet | -80.254 [-148.039, -17.902] |  |  | 40 | 5 | 6228f90c |
| test2 | start_points | overall | rul_bias | gru | -186.076 [-249.281, -127.247] |  |  | 40 | 5 | 68c083f5 |
| test2 | start_points | overall | rul_bias | itransformer | -47.911 [-97.881, 0.480] |  |  | 40 | 5 | 1f7dadba |
| test2 | start_points | overall | rul_bias | itransformer_sc | -49.438 [-80.460, -19.015] |  |  | 40 | 5 | 4a0a69dd |
| test2 | start_points | overall | rul_bias | lgbm | -219.621 [-274.278, -170.523] |  |  | 40 | 5 | b88b5644 |
| test2 | start_points | overall | rul_bias | lstm | -172.441 [-231.704, -119.336] |  |  | 40 | 5 | 7a6e2343 |
| test2 | start_points | overall | rul_bias | nlinear | -233.820 [-292.287, -181.434] |  |  | 40 | 5 | f6a02b2d |
| test2 | start_points | overall | rul_bias | patchtst | -545.111 [-604.655, -491.458] |  |  | 40 | 5 | 5b64c567 |
| test2 | start_points | overall | rul_bias | rlinear | -608.419 [-670.555, -551.652] |  |  | 40 | 5 | aa9b25f1 |
| test2 | start_points | overall | rul_bias | transformer | -215.862 [-278.503, -159.420] |  |  | 40 | 5 | cd2ed4cc |
| test2 | start_points | overall | rul_mae | dlinear | 268.875 [221.856, 322.296] |  |  | 40 | 5 | c066ff8c |
| test2 | start_points | overall | rul_mae | elasticnet | 174.555 [132.039, 222.183] |  |  | 40 | 5 | 6228f90c |
| test2 | start_points | overall | rul_mae | gru | 222.226 [174.619, 275.988] |  |  | 40 | 5 | 68c083f5 |
| test2 | start_points | overall | rul_mae | itransformer | 148.814 [121.862, 178.203] |  |  | 40 | 5 | 1f7dadba |
| test2 | start_points | overall | rul_mae | itransformer_sc | 140.132 [113.587, 169.878] |  |  | 40 | 5 | 4a0a69dd |
| test2 | start_points | overall | rul_mae | lgbm | 225.294 [177.597, 278.713] |  |  | 40 | 5 | b88b5644 |
| test2 | start_points | overall | rul_mae | lstm | 198.626 [151.921, 251.321] |  |  | 40 | 5 | 7a6e2343 |
| test2 | start_points | overall | rul_mae | nlinear | 268.839 [221.819, 322.262] |  |  | 40 | 5 | f6a02b2d |
| test2 | start_points | overall | rul_mae | patchtst | 545.111 [491.458, 604.655] |  |  | 40 | 5 | 5b64c567 |
| test2 | start_points | overall | rul_mae | rlinear | 608.419 [551.652, 670.555] |  |  | 40 | 5 | aa9b25f1 |
| test2 | start_points | overall | rul_mae | transformer | 236.446 [186.416, 293.541] |  |  | 40 | 5 | cd2ed4cc |

</details>

<details><summary>toyota_soh (144 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rmse | dlinear | 0.126 [0.075, 0.186] | p=2.5e-12 (vs prev_soh) |  | 43 | 5 | 3ac7bfd2 |
| test1 | all | overall | rmse | elasticnet | 0.129 [0.077, 0.189] | p=2.5e-12 (vs prev_soh) |  | 43 | 5 | 46575c2e |
| test1 | all | overall | rmse | gru | 0.136 [0.082, 0.199] | p=2.5e-12 (vs prev_soh) |  | 43 | 5 | 3ddf16a8 |
| test1 | all | overall | rmse | itransformer | 0.111 [0.067, 0.163] | p=2.5e-12 (vs prev_soh) |  | 43 | 5 | 86cda30d |
| test1 | all | overall | rmse | itransformer_sc | 0.111 [0.067, 0.163] | p=2.5e-12 (vs prev_soh) |  | 43 | 5 | 38d1aefd |
| test1 | all | overall | rmse | lgbm | 0.133 [0.079, 0.196] | p=2.5e-12 (vs prev_soh) |  | 43 | 5 | ac42ccf2 |
| test1 | all | overall | rmse | lstm | 0.135 [0.082, 0.199] | p=2.5e-12 (vs prev_soh) |  | 43 | 5 | cd05dc09 |
| test1 | all | overall | rmse | nlinear | 0.126 [0.075, 0.185] | p=2.5e-12 (vs prev_soh) |  | 43 | 5 | c114a71d |
| test1 | all | overall | rmse | patchtst | 0.109 [0.066, 0.159] | p=2.5e-12 (vs prev_soh) |  | 43 | 5 | 93bc379a |
| test1 | all | overall | rmse | prev_soh | 0.158 [0.106, 0.219] |  |  | 43 | 5 | 7e056afa |
| test1 | all | overall | rmse | rlinear | 0.124 [0.073, 0.182] | p=2.5e-12 (vs prev_soh) |  | 43 | 5 | e63748eb |
| test1 | all | overall | rmse | transformer | 0.139 [0.085, 0.202] | p=7.5e-12 (vs prev_soh) |  | 43 | 5 | 56c061b1 |
| test1 | start_points | fixed:100 | rmse | dlinear | 0.010 [0.007, 0.015] | p=0.0395 (vs prev_soh) |  | 43 | 5 | 3ac7bfd2 |
| test1 | start_points | fixed:100 | rmse | elasticnet | 0.016 [0.012, 0.020] | p=1 (vs prev_soh) |  | 43 | 5 | 46575c2e |
| test1 | start_points | fixed:100 | rmse | gru | 0.016 [0.010, 0.023] | p=1 (vs prev_soh) |  | 43 | 5 | 3ddf16a8 |
| test1 | start_points | fixed:100 | rmse | itransformer | 0.009 [0.006, 0.013] | p=0.0322 (vs prev_soh) |  | 43 | 5 | 86cda30d |
| test1 | start_points | fixed:100 | rmse | itransformer_sc | 0.009 [0.005, 0.014] | p=0.00371 (vs prev_soh) |  | 43 | 5 | 38d1aefd |
| test1 | start_points | fixed:100 | rmse | lgbm | 0.014 [0.009, 0.019] | p=1 (vs prev_soh) |  | 43 | 5 | ac42ccf2 |
| test1 | start_points | fixed:100 | rmse | lstm | 0.015 [0.009, 0.023] | p=1 (vs prev_soh) |  | 43 | 5 | cd05dc09 |
| test1 | start_points | fixed:100 | rmse | nlinear | 0.012 [0.009, 0.016] | p=1 (vs prev_soh) |  | 43 | 5 | c114a71d |
| test1 | start_points | fixed:100 | rmse | patchtst | 0.008 [0.005, 0.012] | p=0.0018 (vs prev_soh) |  | 43 | 5 | 93bc379a |
| test1 | start_points | fixed:100 | rmse | prev_soh | 0.017 [0.009, 0.026] |  |  | 43 | 5 | 7e056afa |
| test1 | start_points | fixed:100 | rmse | rlinear | 0.009 [0.006, 0.013] | p=0.0127 (vs prev_soh) |  | 43 | 5 | e63748eb |
| test1 | start_points | fixed:100 | rmse | transformer | 0.020 [0.015, 0.027] | p=0.0275 (vs prev_soh) |  | 43 | 5 | 56c061b1 |
| test1 | start_points | frac:0.3 | rmse | dlinear | 0.026 [0.012, 0.050] | p=0.0624 (vs prev_soh) |  | 43 | 5 | 3ac7bfd2 |
| test1 | start_points | frac:0.3 | rmse | elasticnet | 0.031 [0.015, 0.056] | p=0.657 (vs prev_soh) |  | 43 | 5 | 46575c2e |
| test1 | start_points | frac:0.3 | rmse | gru | 0.031 [0.014, 0.059] | p=0.128 (vs prev_soh) |  | 43 | 5 | 3ddf16a8 |
| test1 | start_points | frac:0.3 | rmse | itransformer | 0.018 [0.009, 0.032] | p=0.00058 (vs prev_soh) |  | 43 | 5 | 86cda30d |
| test1 | start_points | frac:0.3 | rmse | itransformer_sc | 0.019 [0.010, 0.034] | p=0.003 (vs prev_soh) |  | 43 | 5 | 38d1aefd |
| test1 | start_points | frac:0.3 | rmse | lgbm | 0.028 [0.011, 0.057] | p=0.0287 (vs prev_soh) |  | 43 | 5 | ac42ccf2 |
| test1 | start_points | frac:0.3 | rmse | lstm | 0.031 [0.014, 0.059] | p=0.0426 (vs prev_soh) |  | 43 | 5 | cd05dc09 |
| test1 | start_points | frac:0.3 | rmse | nlinear | 0.029 [0.014, 0.054] | p=0.628 (vs prev_soh) |  | 43 | 5 | c114a71d |
| test1 | start_points | frac:0.3 | rmse | patchtst | 0.016 [0.009, 0.025] | p=0.000597 (vs prev_soh) |  | 43 | 5 | 93bc379a |
| test1 | start_points | frac:0.3 | rmse | prev_soh | 0.033 [0.016, 0.060] |  |  | 43 | 5 | 7e056afa |
| test1 | start_points | frac:0.3 | rmse | rlinear | 0.025 [0.012, 0.048] | p=0.0984 (vs prev_soh) |  | 43 | 5 | e63748eb |
| test1 | start_points | frac:0.3 | rmse | transformer | 0.035 [0.017, 0.064] | p=0.657 (vs prev_soh) |  | 43 | 5 | 56c061b1 |
| test1 | start_points | frac:0.5 | rmse | dlinear | 0.056 [0.018, 0.122] | p=0.144 (vs prev_soh) |  | 43 | 5 | 3ac7bfd2 |
| test1 | start_points | frac:0.5 | rmse | elasticnet | 0.036 [0.017, 0.066] | p=0.193 (vs prev_soh) |  | 43 | 5 | 46575c2e |
| test1 | start_points | frac:0.5 | rmse | gru | 0.028 [0.018, 0.042] | p=0.112 (vs prev_soh) |  | 43 | 5 | 3ddf16a8 |
| test1 | start_points | frac:0.5 | rmse | itransformer | 0.026 [0.017, 0.038] | p=0.193 (vs prev_soh) |  | 43 | 5 | 86cda30d |
| test1 | start_points | frac:0.5 | rmse | itransformer_sc | 0.022 [0.014, 0.033] | p=0.105 (vs prev_soh) |  | 43 | 5 | 38d1aefd |
| test1 | start_points | frac:0.5 | rmse | lgbm | 0.023 [0.013, 0.037] | p=0.000423 (vs prev_soh) |  | 43 | 5 | ac42ccf2 |
| test1 | start_points | frac:0.5 | rmse | lstm | 0.028 [0.017, 0.042] | p=0.0479 (vs prev_soh) |  | 43 | 5 | cd05dc09 |
| test1 | start_points | frac:0.5 | rmse | nlinear | 0.072 [0.029, 0.129] | p=0.698 (vs prev_soh) |  | 43 | 5 | c114a71d |
| test1 | start_points | frac:0.5 | rmse | patchtst | 0.027 [0.017, 0.039] | p=0.105 (vs prev_soh) |  | 43 | 5 | 93bc379a |
| test1 | start_points | frac:0.5 | rmse | prev_soh | 0.034 [0.023, 0.047] |  |  | 43 | 5 | 7e056afa |
| test1 | start_points | frac:0.5 | rmse | rlinear | 0.079 [0.019, 0.180] | p=0.218 (vs prev_soh) |  | 43 | 5 | e63748eb |
| test1 | start_points | frac:0.5 | rmse | transformer | 0.031 [0.021, 0.044] | p=0.474 (vs prev_soh) |  | 43 | 5 | 56c061b1 |
| test1 | start_points | frac:0.7 | rmse | dlinear | 0.034 [0.026, 0.042] | p=0.296 (vs prev_soh) |  | 43 | 5 | 3ac7bfd2 |
| test1 | start_points | frac:0.7 | rmse | elasticnet | 0.034 [0.023, 0.046] | p=0.296 (vs prev_soh) |  | 43 | 5 | 46575c2e |
| test1 | start_points | frac:0.7 | rmse | gru | 0.034 [0.025, 0.045] | p=0.296 (vs prev_soh) |  | 43 | 5 | 3ddf16a8 |
| test1 | start_points | frac:0.7 | rmse | itransformer | 0.030 [0.022, 0.039] | p=0.0966 (vs prev_soh) |  | 43 | 5 | 86cda30d |
| test1 | start_points | frac:0.7 | rmse | itransformer_sc | 0.034 [0.024, 0.045] | p=0.296 (vs prev_soh) |  | 43 | 5 | 38d1aefd |
| test1 | start_points | frac:0.7 | rmse | lgbm | 0.028 [0.019, 0.038] | p=0.028 (vs prev_soh) |  | 43 | 5 | ac42ccf2 |
| test1 | start_points | frac:0.7 | rmse | lstm | 0.034 [0.025, 0.044] | p=0.202 (vs prev_soh) |  | 43 | 5 | cd05dc09 |
| test1 | start_points | frac:0.7 | rmse | nlinear | 0.034 [0.026, 0.042] | p=0.296 (vs prev_soh) |  | 43 | 5 | c114a71d |
| test1 | start_points | frac:0.7 | rmse | patchtst | 0.035 [0.025, 0.045] | p=0.296 (vs prev_soh) |  | 43 | 5 | 93bc379a |
| test1 | start_points | frac:0.7 | rmse | prev_soh | 0.044 [0.033, 0.055] |  |  | 43 | 5 | 7e056afa |
| test1 | start_points | frac:0.7 | rmse | rlinear | 0.033 [0.025, 0.041] | p=0.202 (vs prev_soh) |  | 43 | 5 | e63748eb |
| test1 | start_points | frac:0.7 | rmse | transformer | 0.036 [0.028, 0.046] | p=0.296 (vs prev_soh) |  | 43 | 5 | 56c061b1 |
| test1 | start_points | overall | rmse | dlinear | 0.047 [0.025, 0.081] | p=0.00783 (vs prev_soh) |  | 43 | 5 | 3ac7bfd2 |
| test1 | start_points | overall | rmse | elasticnet | 0.040 [0.026, 0.058] | p=0.029 (vs prev_soh) |  | 43 | 5 | 46575c2e |
| test1 | start_points | overall | rmse | gru | 0.035 [0.023, 0.051] | p=0.00255 (vs prev_soh) |  | 43 | 5 | 3ddf16a8 |
| test1 | start_points | overall | rmse | itransformer | 0.028 [0.021, 0.037] | p=0.00427 (vs prev_soh) |  | 43 | 5 | 86cda30d |
| test1 | start_points | overall | rmse | itransformer_sc | 0.028 [0.020, 0.038] | p=0.00891 (vs prev_soh) |  | 43 | 5 | 38d1aefd |
| test1 | start_points | overall | rmse | lgbm | 0.031 [0.019, 0.047] | p=6.17e-05 (vs prev_soh) |  | 43 | 5 | ac42ccf2 |
| test1 | start_points | overall | rmse | lstm | 0.035 [0.023, 0.050] | p=0.00255 (vs prev_soh) |  | 43 | 5 | cd05dc09 |
| test1 | start_points | overall | rmse | nlinear | 0.054 [0.031, 0.083] | p=0.138 (vs prev_soh) |  | 43 | 5 | c114a71d |
| test1 | start_points | overall | rmse | patchtst | 0.028 [0.022, 0.037] | p=0.0081 (vs prev_soh) |  | 43 | 5 | 93bc379a |
| test1 | start_points | overall | rmse | prev_soh | 0.041 [0.030, 0.056] |  |  | 43 | 5 | 7e056afa |
| test1 | start_points | overall | rmse | rlinear | 0.057 [0.026, 0.109] | p=0.0085 (vs prev_soh) |  | 43 | 5 | e63748eb |
| test1 | start_points | overall | rmse | transformer | 0.038 [0.027, 0.054] | p=0.138 (vs prev_soh) |  | 43 | 5 | 56c061b1 |
| test2 | all | overall | rmse | dlinear | 0.016 [0.013, 0.018] | p=2e-11 (vs prev_soh) |  | 40 | 5 | 3ac7bfd2 |
| test2 | all | overall | rmse | elasticnet | 0.024 [0.022, 0.026] | p=2.42e-10 (vs prev_soh) |  | 40 | 5 | 46575c2e |
| test2 | all | overall | rmse | gru | 0.049 [0.045, 0.053] | p=3.12e-05 (vs prev_soh) |  | 40 | 5 | 3ddf16a8 |
| test2 | all | overall | rmse | itransformer | 0.023 [0.022, 0.025] | p=1e-09 (vs prev_soh) |  | 40 | 5 | 86cda30d |
| test2 | all | overall | rmse | itransformer_sc | 0.036 [0.033, 0.039] | p=0.9 (vs prev_soh) |  | 40 | 5 | 38d1aefd |
| test2 | all | overall | rmse | lgbm | 0.024 [0.021, 0.026] | p=6e-10 (vs prev_soh) |  | 40 | 5 | ac42ccf2 |
| test2 | all | overall | rmse | lstm | 0.024 [0.022, 0.026] | p=1e-09 (vs prev_soh) |  | 40 | 5 | cd05dc09 |
| test2 | all | overall | rmse | nlinear | 0.017 [0.015, 0.020] | p=2e-11 (vs prev_soh) |  | 40 | 5 | c114a71d |
| test2 | all | overall | rmse | patchtst | 0.014 [0.011, 0.016] | p=2e-11 (vs prev_soh) |  | 40 | 5 | 93bc379a |
| test2 | all | overall | rmse | prev_soh | 0.036 [0.034, 0.038] |  |  | 40 | 5 | 7e056afa |
| test2 | all | overall | rmse | rlinear | 0.015 [0.013, 0.018] | p=2e-11 (vs prev_soh) |  | 40 | 5 | e63748eb |
| test2 | all | overall | rmse | transformer | 0.038 [0.035, 0.040] | p=0.443 (vs prev_soh) |  | 40 | 5 | 56c061b1 |
| test2 | start_points | fixed:100 | rmse | dlinear | 0.012 [0.006, 0.021] | p=0.5 (vs prev_soh) |  | 40 | 5 | 3ac7bfd2 |
| test2 | start_points | fixed:100 | rmse | elasticnet | 0.024 [0.016, 0.033] | p=3.32e-05 (vs prev_soh) |  | 40 | 5 | 46575c2e |
| test2 | start_points | fixed:100 | rmse | gru | 0.037 [0.032, 0.043] | p=2.96e-07 (vs prev_soh) |  | 40 | 5 | 3ddf16a8 |
| test2 | start_points | fixed:100 | rmse | itransformer | 0.024 [0.018, 0.031] | p=8.55e-05 (vs prev_soh) |  | 40 | 5 | 86cda30d |
| test2 | start_points | fixed:100 | rmse | itransformer_sc | 0.030 [0.025, 0.037] | p=4.75e-06 (vs prev_soh) |  | 40 | 5 | 38d1aefd |
| test2 | start_points | fixed:100 | rmse | lgbm | 0.014 [0.008, 0.023] | p=0.866 (vs prev_soh) |  | 40 | 5 | ac42ccf2 |
| test2 | start_points | fixed:100 | rmse | lstm | 0.015 [0.008, 0.023] | p=0.866 (vs prev_soh) |  | 40 | 5 | cd05dc09 |
| test2 | start_points | fixed:100 | rmse | nlinear | 0.014 [0.008, 0.023] | p=0.866 (vs prev_soh) |  | 40 | 5 | c114a71d |
| test2 | start_points | fixed:100 | rmse | patchtst | 0.012 [0.005, 0.021] | p=0.206 (vs prev_soh) |  | 40 | 5 | 93bc379a |
| test2 | start_points | fixed:100 | rmse | prev_soh | 0.013 [0.007, 0.023] |  |  | 40 | 5 | 7e056afa |
| test2 | start_points | fixed:100 | rmse | rlinear | 0.013 [0.006, 0.021] | p=0.5 (vs prev_soh) |  | 40 | 5 | e63748eb |
| test2 | start_points | fixed:100 | rmse | transformer | 0.029 [0.024, 0.035] | p=3.49e-06 (vs prev_soh) |  | 40 | 5 | 56c061b1 |
| test2 | start_points | frac:0.3 | rmse | dlinear | 0.009 [0.004, 0.017] | p=0.00168 (vs prev_soh) |  | 40 | 5 | 3ac7bfd2 |
| test2 | start_points | frac:0.3 | rmse | elasticnet | 0.019 [0.013, 0.027] | p=0.000144 (vs prev_soh) |  | 40 | 5 | 46575c2e |
| test2 | start_points | frac:0.3 | rmse | gru | 0.043 [0.039, 0.048] | p=1.01e-06 (vs prev_soh) |  | 40 | 5 | 3ddf16a8 |
| test2 | start_points | frac:0.3 | rmse | itransformer | 0.024 [0.021, 0.029] | p=0.00168 (vs prev_soh) |  | 40 | 5 | 86cda30d |
| test2 | start_points | frac:0.3 | rmse | itransformer_sc | 0.038 [0.033, 0.042] | p=1.67e-05 (vs prev_soh) |  | 40 | 5 | 38d1aefd |
| test2 | start_points | frac:0.3 | rmse | lgbm | 0.014 [0.010, 0.021] | p=0.132 (vs prev_soh) |  | 40 | 5 | ac42ccf2 |
| test2 | start_points | frac:0.3 | rmse | lstm | 0.015 [0.010, 0.022] | p=0.036 (vs prev_soh) |  | 40 | 5 | cd05dc09 |
| test2 | start_points | frac:0.3 | rmse | nlinear | 0.012 [0.007, 0.019] | p=0.162 (vs prev_soh) |  | 40 | 5 | c114a71d |
| test2 | start_points | frac:0.3 | rmse | patchtst | 0.009 [0.004, 0.016] | p=0.00135 (vs prev_soh) |  | 40 | 5 | 93bc379a |
| test2 | start_points | frac:0.3 | rmse | prev_soh | 0.012 [0.006, 0.019] |  |  | 40 | 5 | 7e056afa |
| test2 | start_points | frac:0.3 | rmse | rlinear | 0.009 [0.004, 0.016] | p=0.00215 (vs prev_soh) |  | 40 | 5 | e63748eb |
| test2 | start_points | frac:0.3 | rmse | transformer | 0.030 [0.026, 0.034] | p=5.28e-06 (vs prev_soh) |  | 40 | 5 | 56c061b1 |
| test2 | start_points | frac:0.5 | rmse | dlinear | 0.013 [0.006, 0.022] | p=0.00447 (vs prev_soh) |  | 40 | 5 | 3ac7bfd2 |
| test2 | start_points | frac:0.5 | rmse | elasticnet | 0.018 [0.011, 0.028] | p=0.136 (vs prev_soh) |  | 40 | 5 | 46575c2e |
| test2 | start_points | frac:0.5 | rmse | gru | 0.051 [0.043, 0.059] | p=4.07e-08 (vs prev_soh) |  | 40 | 5 | 3ddf16a8 |
| test2 | start_points | frac:0.5 | rmse | itransformer | 0.026 [0.022, 0.030] | p=0.00479 (vs prev_soh) |  | 40 | 5 | 86cda30d |
| test2 | start_points | frac:0.5 | rmse | itransformer_sc | 0.045 [0.041, 0.051] | p=4.75e-06 (vs prev_soh) |  | 40 | 5 | 38d1aefd |
| test2 | start_points | frac:0.5 | rmse | lgbm | 0.022 [0.014, 0.033] | p=0.0122 (vs prev_soh) |  | 40 | 5 | ac42ccf2 |
| test2 | start_points | frac:0.5 | rmse | lstm | 0.023 [0.015, 0.033] | p=0.0175 (vs prev_soh) |  | 40 | 5 | cd05dc09 |
| test2 | start_points | frac:0.5 | rmse | nlinear | 0.015 [0.008, 0.024] | p=0.397 (vs prev_soh) |  | 40 | 5 | c114a71d |
| test2 | start_points | frac:0.5 | rmse | patchtst | 0.009 [0.005, 0.016] | p=0.00406 (vs prev_soh) |  | 40 | 5 | 93bc379a |
| test2 | start_points | frac:0.5 | rmse | prev_soh | 0.016 [0.008, 0.026] |  |  | 40 | 5 | 7e056afa |
| test2 | start_points | frac:0.5 | rmse | rlinear | 0.012 [0.005, 0.021] | p=0.00479 (vs prev_soh) |  | 40 | 5 | e63748eb |
| test2 | start_points | frac:0.5 | rmse | transformer | 0.038 [0.031, 0.048] | p=7.84e-08 (vs prev_soh) |  | 40 | 5 | 56c061b1 |
| test2 | start_points | frac:0.7 | rmse | dlinear | 0.007 [0.004, 0.012] | p=1.15e-05 (vs prev_soh) |  | 40 | 5 | 3ac7bfd2 |
| test2 | start_points | frac:0.7 | rmse | elasticnet | 0.012 [0.008, 0.017] | p=0.111 (vs prev_soh) |  | 40 | 5 | 46575c2e |
| test2 | start_points | frac:0.7 | rmse | gru | 0.054 [0.048, 0.060] | p=2e-11 (vs prev_soh) |  | 40 | 5 | 3ddf16a8 |
| test2 | start_points | frac:0.7 | rmse | itransformer | 0.019 [0.016, 0.022] | p=0.249 (vs prev_soh) |  | 40 | 5 | 86cda30d |
| test2 | start_points | frac:0.7 | rmse | itransformer_sc | 0.038 [0.033, 0.043] | p=0.000108 (vs prev_soh) |  | 40 | 5 | 38d1aefd |
| test2 | start_points | frac:0.7 | rmse | lgbm | 0.023 [0.018, 0.029] | p=0.111 (vs prev_soh) |  | 40 | 5 | ac42ccf2 |
| test2 | start_points | frac:0.7 | rmse | lstm | 0.019 [0.014, 0.026] | p=0.283 (vs prev_soh) |  | 40 | 5 | cd05dc09 |
| test2 | start_points | frac:0.7 | rmse | nlinear | 0.010 [0.007, 0.014] | p=0.0014 (vs prev_soh) |  | 40 | 5 | c114a71d |
| test2 | start_points | frac:0.7 | rmse | patchtst | 0.005 [0.004, 0.007] | p=1.15e-05 (vs prev_soh) |  | 40 | 5 | 93bc379a |
| test2 | start_points | frac:0.7 | rmse | prev_soh | 0.016 [0.012, 0.021] |  |  | 40 | 5 | 7e056afa |
| test2 | start_points | frac:0.7 | rmse | rlinear | 0.007 [0.004, 0.011] | p=1.71e-05 (vs prev_soh) |  | 40 | 5 | e63748eb |
| test2 | start_points | frac:0.7 | rmse | transformer | 0.037 [0.032, 0.043] | p=6e-10 (vs prev_soh) |  | 40 | 5 | 56c061b1 |
| test2 | start_points | overall | rmse | dlinear | 0.015 [0.009, 0.021] | p=1.04e-06 (vs prev_soh) |  | 40 | 5 | 3ac7bfd2 |
| test2 | start_points | overall | rmse | elasticnet | 0.022 [0.016, 0.029] | p=0.00673 (vs prev_soh) |  | 40 | 5 | 46575c2e |
| test2 | start_points | overall | rmse | gru | 0.049 [0.045, 0.054] | p=1.1e-09 (vs prev_soh) |  | 40 | 5 | 3ddf16a8 |
| test2 | start_points | overall | rmse | itransformer | 0.025 [0.022, 0.029] | p=0.02 (vs prev_soh) |  | 40 | 5 | 86cda30d |
| test2 | start_points | overall | rmse | itransformer_sc | 0.040 [0.036, 0.044] | p=1.43e-06 (vs prev_soh) |  | 40 | 5 | 38d1aefd |
| test2 | start_points | overall | rmse | lgbm | 0.023 [0.018, 0.030] | p=0.00357 (vs prev_soh) |  | 40 | 5 | ac42ccf2 |
| test2 | start_points | overall | rmse | lstm | 0.022 [0.017, 0.029] | p=0.024 (vs prev_soh) |  | 40 | 5 | cd05dc09 |
| test2 | start_points | overall | rmse | nlinear | 0.016 [0.011, 0.023] | p=0.024 (vs prev_soh) |  | 40 | 5 | c114a71d |
| test2 | start_points | overall | rmse | patchtst | 0.012 [0.007, 0.018] | p=6.1e-08 (vs prev_soh) |  | 40 | 5 | 93bc379a |
| test2 | start_points | overall | rmse | prev_soh | 0.018 [0.013, 0.025] |  |  | 40 | 5 | 7e056afa |
| test2 | start_points | overall | rmse | rlinear | 0.014 [0.009, 0.021] | p=7.67e-06 (vs prev_soh) |  | 40 | 5 | e63748eb |
| test2 | start_points | overall | rmse | transformer | 0.037 [0.033, 0.042] | p=1.27e-09 (vs prev_soh) |  | 40 | 5 | 56c061b1 |

</details>
