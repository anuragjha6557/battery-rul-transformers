# Benchmark tables: smoke_mixed

- Protocol version: 1.1
- Git SHA: e10614fa79
- Seeds: 1  |  unit runs: 12
- Note: n = 4 cells per NASA/CALCE dataset, so the 95 % cluster-bootstrap CI is wide by construction. Toyota rows are over test cells (test1 / test2 separately) with a cell-level bootstrap CI and a Holm-adjusted Wilcoxon p vs the best baseline. All metrics are computed per cell from the logged predictions.

## Headline (kind = overall; RMSE in %SOH, RUL MAE in cycles)

### calce_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | lgbm | 1.939 [1.841, 2.036] | 4/4 cells, 4/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | all | overall | rmse_h1 | nlinear | 2.225 [2.107, 2.344] | 4/4 cells, 4/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | all | overall | rmse_h1 | persistence | 2.606 [2.429, 2.783] |  |  | 4 | 1 | 6e0d77d4 |
| loco | all | overall | rmse_h10 | lgbm | 2.259 [2.187, 2.340] | 4/4 cells, 4/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | all | overall | rmse_h10 | nlinear | 2.643 [2.583, 2.703] | 4/4 cells, 4/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | all | overall | rmse_h10 | persistence | 3.071 [3.003, 3.139] |  |  | 4 | 1 | 6e0d77d4 |
| loco | all | overall | rmse_h50 | lgbm | 2.863 [2.534, 3.188] | 4/4 cells, 4/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | all | overall | rmse_h50 | nlinear | 4.880 [4.717, 5.091] | 4/4 cells, 4/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | all | overall | rmse_h50 | persistence | 6.278 [5.955, 6.519] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | overall | rmse_h1 | lgbm | 0.426 [0.292, 0.597] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | overall | rmse_h1 | nlinear | 0.903 [0.822, 1.044] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | overall | rmse_h1 | persistence | 0.397 [0.177, 0.617] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | overall | rmse_h10 | lgbm | 1.067 [0.577, 1.644] | 3/4 cells, 3/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | overall | rmse_h10 | nlinear | 1.380 [0.894, 1.959] | 2/4 cells, 2/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | overall | rmse_h10 | persistence | 1.332 [1.082, 1.703] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | overall | rmse_h50 | lgbm | 1.625 [1.011, 2.239] | 2/4 cells, 2/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | overall | rmse_h50 | nlinear | 4.043 [3.278, 4.821] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | overall | rmse_h50 | persistence | 1.506 [1.020, 1.989] |  |  | 4 | 1 | 6e0d77d4 |

## Mean rank (dataset x task x split x policy x headline metric)

| model | mean rank | conditions | missing |
|---|---|---|---|
| lgbm | 1.33 | 6 | 0 |
| persistence | 2.17 | 6 | 0 |
| nlinear | 2.50 | 6 | 0 |

## Full tables

<details><summary>calce_forecast (105 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | lgbm | 1.939 [1.841, 2.036] | 4/4 cells, 4/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | all | overall | rmse_h1 | nlinear | 2.225 [2.107, 2.344] | 4/4 cells, 4/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | all | overall | rmse_h1 | persistence | 2.606 [2.429, 2.783] |  |  | 4 | 1 | 6e0d77d4 |
| loco | all | overall | rmse_h10 | lgbm | 2.259 [2.187, 2.340] | 4/4 cells, 4/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | all | overall | rmse_h10 | nlinear | 2.643 [2.583, 2.703] | 4/4 cells, 4/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | all | overall | rmse_h10 | persistence | 3.071 [3.003, 3.139] |  |  | 4 | 1 | 6e0d77d4 |
| loco | all | overall | rmse_h100 | lgbm | 3.469 [2.933, 4.063] | 4/4 cells, 4/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | all | overall | rmse_h100 | nlinear | 6.702 [6.411, 6.946] | 4/4 cells, 4/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | all | overall | rmse_h100 | persistence | 10.293 [9.591, 10.966] |  |  | 4 | 1 | 6e0d77d4 |
| loco | all | overall | rmse_h25 | lgbm | 2.609 [2.444, 2.762] | 4/4 cells, 4/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | all | overall | rmse_h25 | nlinear | 3.850 [3.725, 4.041] | 4/4 cells, 4/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | all | overall | rmse_h25 | persistence | 4.180 [4.046, 4.314] |  |  | 4 | 1 | 6e0d77d4 |
| loco | all | overall | rmse_h50 | lgbm | 2.863 [2.534, 3.188] | 4/4 cells, 4/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | all | overall | rmse_h50 | nlinear | 4.880 [4.717, 5.091] | 4/4 cells, 4/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | all | overall | rmse_h50 | persistence | 6.278 [5.955, 6.519] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | fixed:200 | rmse_h1 | lgbm | 0.206 [0.043, 0.380] | 2/4 cells, 2/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | fixed:200 | rmse_h1 | nlinear | 0.968 [0.612, 1.287] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | fixed:200 | rmse_h1 | persistence | 0.347 [0.209, 0.485] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | fixed:200 | rmse_h10 | lgbm | 1.430 [0.364, 3.277] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | fixed:200 | rmse_h10 | nlinear | 1.859 [0.748, 3.801] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | fixed:200 | rmse_h10 | persistence | 1.344 [0.340, 2.774] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | fixed:200 | rmse_h100 | lgbm | 1.322 [0.628, 2.100] | 3/4 cells, 3/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | fixed:200 | rmse_h100 | nlinear | 3.871 [2.968, 5.352] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | fixed:200 | rmse_h100 | persistence | 1.897 [1.120, 2.489] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | fixed:200 | rmse_h25 | lgbm | 2.235 [1.871, 2.531] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | fixed:200 | rmse_h25 | nlinear | 3.979 [3.621, 4.360] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | fixed:200 | rmse_h25 | persistence | 0.840 [0.239, 1.441] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | fixed:200 | rmse_h50 | lgbm | 1.685 [0.692, 2.276] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | fixed:200 | rmse_h50 | nlinear | 3.937 [3.081, 4.594] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | fixed:200 | rmse_h50 | persistence | 0.844 [0.319, 1.572] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | fixed:400 | rmse_h1 | lgbm | 0.216 [0.046, 0.386] | 2/4 cells, 2/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | fixed:400 | rmse_h1 | nlinear | 1.069 [0.931, 1.325] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | fixed:400 | rmse_h1 | persistence | 0.080 [0.019, 0.194] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | fixed:400 | rmse_h10 | lgbm | 0.786 [0.600, 0.972] | 3/4 cells, 3/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | fixed:400 | rmse_h10 | nlinear | 1.040 [0.488, 1.550] | 2/4 cells, 2/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | fixed:400 | rmse_h10 | persistence | 1.009 [0.324, 1.694] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | fixed:400 | rmse_h100 | lgbm | 2.744 [1.965, 3.899] | 2/4 cells, 2/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | fixed:400 | rmse_h100 | nlinear | 3.060 [1.735, 4.385] | 2/4 cells, 2/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | fixed:400 | rmse_h100 | persistence | 3.346 [1.619, 5.072] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | fixed:400 | rmse_h25 | lgbm | 0.873 [0.339, 1.790] | 2/4 cells, 2/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | fixed:400 | rmse_h25 | nlinear | 3.222 [2.076, 3.967] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | fixed:400 | rmse_h25 | persistence | 1.333 [0.586, 2.081] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | fixed:400 | rmse_h50 | lgbm | 0.961 [0.218, 1.985] | 3/4 cells, 3/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | fixed:400 | rmse_h50 | nlinear | 2.907 [2.065, 3.785] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | fixed:400 | rmse_h50 | persistence | 1.656 [0.742, 2.680] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | frac:0.3 | rmse_h1 | lgbm | 0.688 [0.523, 0.836] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | frac:0.3 | rmse_h1 | nlinear | 0.796 [0.392, 1.201] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | frac:0.3 | rmse_h1 | persistence | 0.373 [0.089, 0.866] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | frac:0.3 | rmse_h10 | lgbm | 1.019 [0.311, 1.869] | 3/4 cells, 3/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | frac:0.3 | rmse_h10 | nlinear | 0.921 [0.376, 1.466] | 2/4 cells, 2/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | frac:0.3 | rmse_h10 | persistence | 0.952 [0.590, 1.315] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | frac:0.3 | rmse_h100 | lgbm | 2.526 [1.865, 3.205] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | frac:0.3 | rmse_h100 | nlinear | 5.860 [4.759, 7.437] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | frac:0.3 | rmse_h100 | persistence | 0.918 [0.565, 1.150] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | frac:0.3 | rmse_h25 | lgbm | 1.245 [0.323, 2.167] | 2/4 cells, 2/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | frac:0.3 | rmse_h25 | nlinear | 2.757 [2.655, 2.851] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | frac:0.3 | rmse_h25 | persistence | 0.865 [0.571, 1.180] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | frac:0.3 | rmse_h50 | lgbm | 2.370 [1.453, 4.071] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | frac:0.3 | rmse_h50 | nlinear | 5.586 [3.713, 7.760] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | frac:0.3 | rmse_h50 | persistence | 1.300 [0.353, 2.350] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | frac:0.5 | rmse_h1 | lgbm | 0.217 [0.059, 0.375] | 2/4 cells, 2/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | frac:0.5 | rmse_h1 | nlinear | 0.786 [0.574, 0.954] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | frac:0.5 | rmse_h1 | persistence | 0.524 [0.047, 1.016] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | frac:0.5 | rmse_h10 | lgbm | 0.362 [0.197, 0.622] | 3/4 cells, 3/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | frac:0.5 | rmse_h10 | nlinear | 0.496 [0.056, 0.936] | 4/4 cells, 4/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | frac:0.5 | rmse_h10 | persistence | 1.354 [0.510, 1.928] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | frac:0.5 | rmse_h100 | lgbm | 1.038 [0.756, 1.339] | 4/4 cells, 4/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | frac:0.5 | rmse_h100 | nlinear | 3.757 [1.993, 5.003] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | frac:0.5 | rmse_h100 | persistence | 2.842 [2.048, 3.830] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | frac:0.5 | rmse_h25 | lgbm | 0.928 [0.790, 1.065] | 3/4 cells, 3/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | frac:0.5 | rmse_h25 | nlinear | 1.997 [1.163, 2.544] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | frac:0.5 | rmse_h25 | persistence | 1.599 [0.788, 2.409] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | frac:0.5 | rmse_h50 | lgbm | 0.462 [0.138, 0.794] | 3/4 cells, 3/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | frac:0.5 | rmse_h50 | nlinear | 3.212 [2.497, 3.879] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | frac:0.5 | rmse_h50 | persistence | 1.521 [0.930, 2.368] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | frac:0.7 | rmse_h1 | lgbm | 0.403 [0.100, 0.813] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | frac:0.7 | rmse_h1 | nlinear | 0.585 [0.305, 0.851] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | frac:0.7 | rmse_h1 | persistence | 0.092 [0.023, 0.162] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | frac:0.7 | rmse_h10 | lgbm | 0.391 [0.119, 0.754] | 3/4 cells, 3/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | frac:0.7 | rmse_h10 | nlinear | 1.070 [0.481, 1.977] | 2/4 cells, 2/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | frac:0.7 | rmse_h10 | persistence | 0.717 [0.237, 1.507] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | frac:0.7 | rmse_h100 | lgbm | 2.575 [1.291, 3.859] | 3/4 cells, 3/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | frac:0.7 | rmse_h100 | nlinear | 3.588 [1.456, 6.029] | 2/4 cells, 2/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | frac:0.7 | rmse_h100 | persistence | 3.080 [1.373, 4.710] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | frac:0.7 | rmse_h25 | lgbm | 0.642 [0.150, 1.135] | 2/4 cells, 2/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | frac:0.7 | rmse_h25 | nlinear | 2.979 [2.062, 3.777] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | frac:0.7 | rmse_h25 | persistence | 0.714 [0.117, 1.649] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | frac:0.7 | rmse_h50 | lgbm | 1.056 [0.518, 1.594] | 2/4 cells, 2/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | frac:0.7 | rmse_h50 | nlinear | 3.620 [2.855, 4.385] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | frac:0.7 | rmse_h50 | persistence | 1.046 [0.194, 1.898] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | overall | rmse_h1 | lgbm | 0.426 [0.292, 0.597] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | overall | rmse_h1 | nlinear | 0.903 [0.822, 1.044] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | overall | rmse_h1 | persistence | 0.397 [0.177, 0.617] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | overall | rmse_h10 | lgbm | 1.067 [0.577, 1.644] | 3/4 cells, 3/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | overall | rmse_h10 | nlinear | 1.380 [0.894, 1.959] | 2/4 cells, 2/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | overall | rmse_h10 | persistence | 1.332 [1.082, 1.703] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | overall | rmse_h100 | lgbm | 2.297 [1.878, 2.716] | 3/4 cells, 3/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | overall | rmse_h100 | nlinear | 4.346 [3.399, 5.300] | 1/4 cells, 1/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | overall | rmse_h100 | persistence | 2.680 [1.781, 3.658] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | overall | rmse_h25 | lgbm | 1.392 [1.064, 1.789] | 2/4 cells, 2/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | overall | rmse_h25 | nlinear | 3.118 [2.803, 3.414] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | overall | rmse_h25 | persistence | 1.317 [1.143, 1.422] |  |  | 4 | 1 | 6e0d77d4 |
| loco | start_points | overall | rmse_h50 | lgbm | 1.625 [1.011, 2.239] | 2/4 cells, 2/4 cell-seeds (vs persistence) |  | 4 | 1 | 34fee0f4 |
| loco | start_points | overall | rmse_h50 | nlinear | 4.043 [3.278, 4.821] | 0/4 cells, 0/4 cell-seeds (vs persistence) |  | 4 | 1 | ed116b64 |
| loco | start_points | overall | rmse_h50 | persistence | 1.506 [1.020, 1.989] |  |  | 4 | 1 | 6e0d77d4 |

</details>
