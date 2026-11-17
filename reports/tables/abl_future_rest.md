# Benchmark tables: abl_future_rest

- Protocol version: 1.1
- Git SHA: 9e6951d7a8
- Seeds: 5  |  unit runs: 240
- Note: n = 4 cells per NASA/CALCE dataset, so the 95 % cluster-bootstrap CI is wide by construction. Toyota rows are over test cells (test1 / test2 separately) with a cell-level bootstrap CI and a Holm-adjusted Wilcoxon p vs the best baseline. All metrics are computed per cell from the logged predictions.

## Headline (kind = overall; RMSE in %SOH, RUL MAE in cycles)

### calce_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | elasticnet | 1.907 [1.824, 1.990] |  |  | 4 | 5 | e4512909 |
| loco | all | overall | rmse_h1 | itransformer | 2.006 [1.877, 2.140] |  |  | 4 | 5 | 6e8e8987 |
| loco | all | overall | rmse_h1 | itransformer_sc | 2.089 [1.945, 2.264] |  |  | 4 | 5 | 8c777c2f |
| loco | all | overall | rmse_h1 | lgbm | 2.052 [1.924, 2.173] |  |  | 4 | 5 | edf9dba9 |
| loco | all | overall | rmse_h1 | lstm | 1.924 [1.829, 2.019] |  |  | 4 | 5 | 46e0307f |
| loco | all | overall | rmse_h1 | transformer | 2.290 [2.128, 2.494] |  |  | 4 | 5 | c550b9cd |
| loco | all | overall | rmse_h10 | elasticnet | 2.324 [2.242, 2.422] |  |  | 4 | 5 | e4512909 |
| loco | all | overall | rmse_h10 | itransformer | 2.288 [2.194, 2.404] |  |  | 4 | 5 | 6e8e8987 |
| loco | all | overall | rmse_h10 | itransformer_sc | 2.311 [2.250, 2.393] |  |  | 4 | 5 | 8c777c2f |
| loco | all | overall | rmse_h10 | lgbm | 2.387 [2.318, 2.457] |  |  | 4 | 5 | edf9dba9 |
| loco | all | overall | rmse_h10 | lstm | 2.247 [2.133, 2.361] |  |  | 4 | 5 | 46e0307f |
| loco | all | overall | rmse_h10 | transformer | 2.564 [2.413, 2.696] |  |  | 4 | 5 | c550b9cd |
| loco | all | overall | rmse_h50 | elasticnet | 3.726 [2.976, 4.556] |  |  | 4 | 5 | e4512909 |
| loco | all | overall | rmse_h50 | itransformer | 2.951 [2.751, 3.188] |  |  | 4 | 5 | 6e8e8987 |
| loco | all | overall | rmse_h50 | itransformer_sc | 2.892 [2.667, 3.194] |  |  | 4 | 5 | 8c777c2f |
| loco | all | overall | rmse_h50 | lgbm | 2.651 [2.320, 3.005] |  |  | 4 | 5 | edf9dba9 |
| loco | all | overall | rmse_h50 | lstm | 2.985 [2.517, 3.464] |  |  | 4 | 5 | 46e0307f |
| loco | all | overall | rmse_h50 | transformer | 3.155 [2.685, 3.626] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | overall | rmse_h1 | elasticnet | 0.478 [0.370, 0.631] |  |  | 4 | 5 | e4512909 |
| loco | start_points | overall | rmse_h1 | itransformer | 0.400 [0.211, 0.588] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | overall | rmse_h1 | itransformer_sc | 0.408 [0.212, 0.605] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | overall | rmse_h1 | lgbm | 0.371 [0.174, 0.568] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | overall | rmse_h1 | lstm | 0.411 [0.212, 0.611] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | overall | rmse_h1 | transformer | 0.519 [0.380, 0.618] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | overall | rmse_h10 | elasticnet | 1.189 [0.707, 1.962] |  |  | 4 | 5 | e4512909 |
| loco | start_points | overall | rmse_h10 | itransformer | 1.040 [0.651, 1.614] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | overall | rmse_h10 | itransformer_sc | 1.025 [0.635, 1.625] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | overall | rmse_h10 | lgbm | 1.111 [0.656, 1.748] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | overall | rmse_h10 | lstm | 1.058 [0.611, 1.771] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | overall | rmse_h10 | transformer | 1.140 [0.719, 1.794] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | overall | rmse_h50 | elasticnet | 2.898 [1.474, 4.634] |  |  | 4 | 5 | e4512909 |
| loco | start_points | overall | rmse_h50 | itransformer | 1.741 [0.970, 2.827] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | overall | rmse_h50 | itransformer_sc | 1.818 [1.023, 2.987] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | overall | rmse_h50 | lgbm | 1.922 [1.146, 2.963] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | overall | rmse_h50 | lstm | 2.061 [1.103, 3.235] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | overall | rmse_h50 | transformer | 2.108 [1.184, 3.142] |  |  | 4 | 5 | c550b9cd |

### nasa_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | elasticnet | 0.938 [0.744, 1.132] |  | 1.093 | 4 | 5 | 1240eca2 |
| loco | all | overall | rmse_h1 | itransformer | 0.857 [0.643, 1.070] |  | 1.067 | 4 | 5 | f438e343 |
| loco | all | overall | rmse_h1 | itransformer_sc | 0.906 [0.667, 1.145] |  | 1.196 | 4 | 5 | 37ed894e |
| loco | all | overall | rmse_h1 | lgbm | 0.852 [0.639, 1.065] |  | 1.027 | 4 | 5 | 5bf5307f |
| loco | all | overall | rmse_h1 | lstm | 1.343 [0.781, 2.003] |  | 2.406 | 4 | 5 | 911aa065 |
| loco | all | overall | rmse_h1 | transformer | 2.299 [1.354, 3.397] |  | 4.043 | 4 | 5 | f91ffc71 |
| loco | all | overall | rmse_h10 | elasticnet | 1.788 [1.316, 2.410] |  | 1.731 | 4 | 5 | 1240eca2 |
| loco | all | overall | rmse_h10 | itransformer | 1.499 [0.996, 2.002] |  | 2.249 | 4 | 5 | f438e343 |
| loco | all | overall | rmse_h10 | itransformer_sc | 1.720 [1.125, 2.316] |  | 2.533 | 4 | 5 | 37ed894e |
| loco | all | overall | rmse_h10 | lgbm | 1.448 [1.000, 1.896] |  | 1.849 | 4 | 5 | 5bf5307f |
| loco | all | overall | rmse_h10 | lstm | 2.034 [1.347, 2.722] |  | 2.756 | 4 | 5 | 911aa065 |
| loco | all | overall | rmse_h10 | transformer | 3.026 [1.993, 4.328] |  | 5.099 | 4 | 5 | f91ffc71 |
| loco | all | overall | rmse_h50 | elasticnet | 4.176 [2.737, 5.413] |  | 4.457 | 4 | 5 | 1240eca2 |
| loco | all | overall | rmse_h50 | itransformer | 5.279 [5.033, 5.525] |  | 5.074 | 4 | 5 | f438e343 |
| loco | all | overall | rmse_h50 | itransformer_sc | 3.836 [3.741, 3.977] |  | 4.047 | 4 | 5 | 37ed894e |
| loco | all | overall | rmse_h50 | lgbm | 3.213 [2.381, 4.186] |  | 3.051 | 4 | 5 | 5bf5307f |
| loco | all | overall | rmse_h50 | lstm | 3.848 [2.957, 4.975] |  | 3.580 | 4 | 5 | 911aa065 |
| loco | all | overall | rmse_h50 | transformer | 4.741 [3.265, 5.689] |  | 5.859 | 4 | 5 | f91ffc71 |
| loco | start_points | overall | rmse_h1 | elasticnet | 1.156 [0.586, 1.727] |  | 2.038 | 4 | 5 | 1240eca2 |
| loco | start_points | overall | rmse_h1 | itransformer | 1.666 [1.064, 2.267] |  | 2.123 | 4 | 5 | f438e343 |
| loco | start_points | overall | rmse_h1 | itransformer_sc | 1.732 [1.100, 2.364] |  | 2.416 | 4 | 5 | 37ed894e |
| loco | start_points | overall | rmse_h1 | lgbm | 1.504 [0.960, 2.048] |  | 1.965 | 4 | 5 | 5bf5307f |
| loco | start_points | overall | rmse_h1 | lstm | 1.292 [0.909, 1.675] |  | 1.850 | 4 | 5 | 911aa065 |
| loco | start_points | overall | rmse_h1 | transformer | 2.133 [1.389, 2.754] |  | 2.900 | 4 | 5 | f91ffc71 |
| loco | start_points | overall | rmse_h10 | elasticnet | 1.898 [1.258, 2.812] |  | 1.766 | 4 | 5 | 1240eca2 |
| loco | start_points | overall | rmse_h10 | itransformer | 1.555 [0.919, 2.563] |  | 3.093 | 4 | 5 | f438e343 |
| loco | start_points | overall | rmse_h10 | itransformer_sc | 1.892 [1.088, 2.831] |  | 3.406 | 4 | 5 | 37ed894e |
| loco | start_points | overall | rmse_h10 | lgbm | 1.470 [0.496, 2.445] |  | 2.485 | 4 | 5 | 5bf5307f |
| loco | start_points | overall | rmse_h10 | lstm | 1.837 [0.923, 2.751] |  | 3.058 | 4 | 5 | 911aa065 |
| loco | start_points | overall | rmse_h10 | transformer | 2.782 [1.714, 4.037] |  | 4.739 | 4 | 5 | f91ffc71 |
| loco | start_points | overall | rmse_h50 | elasticnet | 4.333 [2.184, 6.281] |  | 5.761 | 4 | 5 | 1240eca2 |
| loco | start_points | overall | rmse_h50 | itransformer | 5.656 [4.084, 7.346] |  | 3.497 | 4 | 5 | f438e343 |
| loco | start_points | overall | rmse_h50 | itransformer_sc | 4.520 [3.944, 5.390] |  | 4.147 | 4 | 5 | 37ed894e |
| loco | start_points | overall | rmse_h50 | lgbm | 3.445 [2.483, 5.000] |  | 3.027 | 4 | 5 | 5bf5307f |
| loco | start_points | overall | rmse_h50 | lstm | 3.616 [2.276, 5.293] |  | 3.053 | 4 | 5 | 911aa065 |
| loco | start_points | overall | rmse_h50 | transformer | 4.002 [2.403, 4.936] |  | 4.538 | 4 | 5 | f91ffc71 |

## Mean rank (dataset x task x split x policy x headline metric)

| model | mean rank | conditions | missing |
|---|---|---|---|
| lgbm | 2.17 | 12 | 0 |
| itransformer | 2.92 | 12 | 0 |
| itransformer_sc | 3.17 | 12 | 0 |
| lstm | 3.17 | 12 | 0 |
| elasticnet | 4.17 | 12 | 0 |
| transformer | 5.42 | 12 | 0 |

## Full tables

<details><summary>calce_forecast (210 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | elasticnet | 1.907 [1.824, 1.990] |  |  | 4 | 5 | e4512909 |
| loco | all | overall | rmse_h1 | itransformer | 2.006 [1.877, 2.140] |  |  | 4 | 5 | 6e8e8987 |
| loco | all | overall | rmse_h1 | itransformer_sc | 2.089 [1.945, 2.264] |  |  | 4 | 5 | 8c777c2f |
| loco | all | overall | rmse_h1 | lgbm | 2.052 [1.924, 2.173] |  |  | 4 | 5 | edf9dba9 |
| loco | all | overall | rmse_h1 | lstm | 1.924 [1.829, 2.019] |  |  | 4 | 5 | 46e0307f |
| loco | all | overall | rmse_h1 | transformer | 2.290 [2.128, 2.494] |  |  | 4 | 5 | c550b9cd |
| loco | all | overall | rmse_h10 | elasticnet | 2.324 [2.242, 2.422] |  |  | 4 | 5 | e4512909 |
| loco | all | overall | rmse_h10 | itransformer | 2.288 [2.194, 2.404] |  |  | 4 | 5 | 6e8e8987 |
| loco | all | overall | rmse_h10 | itransformer_sc | 2.311 [2.250, 2.393] |  |  | 4 | 5 | 8c777c2f |
| loco | all | overall | rmse_h10 | lgbm | 2.387 [2.318, 2.457] |  |  | 4 | 5 | edf9dba9 |
| loco | all | overall | rmse_h10 | lstm | 2.247 [2.133, 2.361] |  |  | 4 | 5 | 46e0307f |
| loco | all | overall | rmse_h10 | transformer | 2.564 [2.413, 2.696] |  |  | 4 | 5 | c550b9cd |
| loco | all | overall | rmse_h100 | elasticnet | 4.509 [3.438, 5.360] |  |  | 4 | 5 | e4512909 |
| loco | all | overall | rmse_h100 | itransformer | 3.749 [3.249, 4.270] |  |  | 4 | 5 | 6e8e8987 |
| loco | all | overall | rmse_h100 | itransformer_sc | 3.649 [3.315, 4.045] |  |  | 4 | 5 | 8c777c2f |
| loco | all | overall | rmse_h100 | lgbm | 3.209 [2.595, 3.966] |  |  | 4 | 5 | edf9dba9 |
| loco | all | overall | rmse_h100 | lstm | 3.867 [2.934, 4.886] |  |  | 4 | 5 | 46e0307f |
| loco | all | overall | rmse_h100 | transformer | 3.607 [3.065, 4.065] |  |  | 4 | 5 | c550b9cd |
| loco | all | overall | rmse_h25 | elasticnet | 3.115 [2.762, 3.506] |  |  | 4 | 5 | e4512909 |
| loco | all | overall | rmse_h25 | itransformer | 2.683 [2.475, 2.930] |  |  | 4 | 5 | 6e8e8987 |
| loco | all | overall | rmse_h25 | itransformer_sc | 2.691 [2.577, 2.808] |  |  | 4 | 5 | 8c777c2f |
| loco | all | overall | rmse_h25 | lgbm | 2.557 [2.429, 2.781] |  |  | 4 | 5 | edf9dba9 |
| loco | all | overall | rmse_h25 | lstm | 2.612 [2.367, 2.858] |  |  | 4 | 5 | 46e0307f |
| loco | all | overall | rmse_h25 | transformer | 2.863 [2.593, 3.103] |  |  | 4 | 5 | c550b9cd |
| loco | all | overall | rmse_h50 | elasticnet | 3.726 [2.976, 4.556] |  |  | 4 | 5 | e4512909 |
| loco | all | overall | rmse_h50 | itransformer | 2.951 [2.751, 3.188] |  |  | 4 | 5 | 6e8e8987 |
| loco | all | overall | rmse_h50 | itransformer_sc | 2.892 [2.667, 3.194] |  |  | 4 | 5 | 8c777c2f |
| loco | all | overall | rmse_h50 | lgbm | 2.651 [2.320, 3.005] |  |  | 4 | 5 | edf9dba9 |
| loco | all | overall | rmse_h50 | lstm | 2.985 [2.517, 3.464] |  |  | 4 | 5 | 46e0307f |
| loco | all | overall | rmse_h50 | transformer | 3.155 [2.685, 3.626] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | fixed:200 | rmse_h1 | elasticnet | 0.314 [0.099, 0.529] |  |  | 4 | 5 | e4512909 |
| loco | start_points | fixed:200 | rmse_h1 | itransformer | 0.327 [0.230, 0.411] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | fixed:200 | rmse_h1 | itransformer_sc | 0.305 [0.186, 0.424] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | fixed:200 | rmse_h1 | lgbm | 0.278 [0.189, 0.408] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | fixed:200 | rmse_h1 | lstm | 0.397 [0.272, 0.513] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | fixed:200 | rmse_h1 | transformer | 0.429 [0.272, 0.615] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | fixed:200 | rmse_h10 | elasticnet | 1.564 [0.470, 3.626] |  |  | 4 | 5 | e4512909 |
| loco | start_points | fixed:200 | rmse_h10 | itransformer | 1.158 [0.213, 2.996] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | fixed:200 | rmse_h10 | itransformer_sc | 1.331 [0.308, 3.133] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | fixed:200 | rmse_h10 | lgbm | 1.407 [0.385, 3.226] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | fixed:200 | rmse_h10 | lstm | 1.414 [0.361, 3.351] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | fixed:200 | rmse_h10 | transformer | 1.467 [0.401, 3.342] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | fixed:200 | rmse_h100 | elasticnet | 2.168 [0.956, 3.454] |  |  | 4 | 5 | e4512909 |
| loco | start_points | fixed:200 | rmse_h100 | itransformer | 1.022 [0.503, 1.778] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | fixed:200 | rmse_h100 | itransformer_sc | 1.098 [0.513, 1.850] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | fixed:200 | rmse_h100 | lgbm | 1.766 [0.639, 2.893] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | fixed:200 | rmse_h100 | lstm | 1.770 [0.522, 3.054] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | fixed:200 | rmse_h100 | transformer | 1.701 [0.521, 2.881] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | fixed:200 | rmse_h25 | elasticnet | 2.377 [0.996, 3.896] |  |  | 4 | 5 | e4512909 |
| loco | start_points | fixed:200 | rmse_h25 | itransformer | 1.776 [1.155, 2.398] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | fixed:200 | rmse_h25 | itransformer_sc | 1.568 [0.745, 2.391] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | fixed:200 | rmse_h25 | lgbm | 2.259 [1.308, 3.080] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | fixed:200 | rmse_h25 | lstm | 2.248 [1.290, 3.219] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | fixed:200 | rmse_h25 | transformer | 2.440 [1.234, 3.646] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | fixed:200 | rmse_h50 | elasticnet | 2.571 [1.942, 3.666] |  |  | 4 | 5 | e4512909 |
| loco | start_points | fixed:200 | rmse_h50 | itransformer | 1.370 [0.725, 1.885] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | fixed:200 | rmse_h50 | itransformer_sc | 1.453 [1.065, 1.873] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | fixed:200 | rmse_h50 | lgbm | 2.338 [1.134, 3.265] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | fixed:200 | rmse_h50 | lstm | 1.887 [0.920, 2.835] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | fixed:200 | rmse_h50 | transformer | 2.048 [1.000, 3.096] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | fixed:400 | rmse_h1 | elasticnet | 0.365 [0.187, 0.490] |  |  | 4 | 5 | e4512909 |
| loco | start_points | fixed:400 | rmse_h1 | itransformer | 0.182 [0.080, 0.284] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | fixed:400 | rmse_h1 | itransformer_sc | 0.229 [0.063, 0.394] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | fixed:400 | rmse_h1 | lgbm | 0.082 [0.019, 0.158] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | fixed:400 | rmse_h1 | lstm | 0.188 [0.100, 0.331] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | fixed:400 | rmse_h1 | transformer | 0.390 [0.290, 0.490] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | fixed:400 | rmse_h10 | elasticnet | 0.946 [0.518, 1.374] |  |  | 4 | 5 | e4512909 |
| loco | start_points | fixed:400 | rmse_h10 | itransformer | 0.608 [0.404, 0.906] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | fixed:400 | rmse_h10 | itransformer_sc | 0.623 [0.247, 0.999] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | fixed:400 | rmse_h10 | lgbm | 0.811 [0.577, 0.972] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | fixed:400 | rmse_h10 | lstm | 0.550 [0.263, 0.837] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | fixed:400 | rmse_h10 | transformer | 0.679 [0.373, 0.904] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | fixed:400 | rmse_h100 | elasticnet | 3.298 [1.557, 4.772] |  |  | 4 | 5 | e4512909 |
| loco | start_points | fixed:400 | rmse_h100 | itransformer | 1.652 [0.830, 2.104] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | fixed:400 | rmse_h100 | itransformer_sc | 2.518 [1.337, 3.308] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | fixed:400 | rmse_h100 | lgbm | 1.579 [0.663, 2.699] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | fixed:400 | rmse_h100 | lstm | 2.223 [1.765, 2.787] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | fixed:400 | rmse_h100 | transformer | 2.342 [1.630, 3.087] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | fixed:400 | rmse_h25 | elasticnet | 1.694 [0.334, 3.160] |  |  | 4 | 5 | e4512909 |
| loco | start_points | fixed:400 | rmse_h25 | itransformer | 0.956 [0.344, 1.569] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | fixed:400 | rmse_h25 | itransformer_sc | 0.937 [0.402, 1.472] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | fixed:400 | rmse_h25 | lgbm | 0.949 [0.237, 2.087] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | fixed:400 | rmse_h25 | lstm | 0.970 [0.312, 1.850] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | fixed:400 | rmse_h25 | transformer | 1.367 [0.533, 2.423] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | fixed:400 | rmse_h50 | elasticnet | 2.485 [1.012, 4.346] |  |  | 4 | 5 | e4512909 |
| loco | start_points | fixed:400 | rmse_h50 | itransformer | 0.948 [0.407, 1.490] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | fixed:400 | rmse_h50 | itransformer_sc | 1.079 [0.538, 2.026] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | fixed:400 | rmse_h50 | lgbm | 1.413 [0.256, 2.570] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | fixed:400 | rmse_h50 | lstm | 1.694 [0.640, 2.817] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | fixed:400 | rmse_h50 | transformer | 1.707 [0.722, 2.692] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | frac:0.3 | rmse_h1 | elasticnet | 0.633 [0.514, 0.758] |  |  | 4 | 5 | e4512909 |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer | 0.437 [0.185, 0.844] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer_sc | 0.377 [0.112, 0.800] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | frac:0.3 | rmse_h1 | lgbm | 0.373 [0.131, 0.772] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | frac:0.3 | rmse_h1 | lstm | 0.365 [0.147, 0.790] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | frac:0.3 | rmse_h1 | transformer | 0.539 [0.355, 0.723] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | frac:0.3 | rmse_h10 | elasticnet | 0.623 [0.275, 0.988] |  |  | 4 | 5 | e4512909 |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer | 0.609 [0.254, 0.963] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer_sc | 0.425 [0.206, 0.711] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | frac:0.3 | rmse_h10 | lgbm | 0.626 [0.120, 1.131] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | frac:0.3 | rmse_h10 | lstm | 0.718 [0.593, 0.843] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | frac:0.3 | rmse_h10 | transformer | 0.793 [0.550, 1.038] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | frac:0.3 | rmse_h100 | elasticnet | 3.490 [1.055, 7.050] |  |  | 4 | 5 | e4512909 |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer | 2.251 [0.621, 5.103] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer_sc | 2.784 [0.960, 6.213] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | frac:0.3 | rmse_h100 | lgbm | 2.458 [1.454, 3.637] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | frac:0.3 | rmse_h100 | lstm | 2.351 [0.803, 4.297] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | frac:0.3 | rmse_h100 | transformer | 2.130 [0.404, 4.274] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | frac:0.3 | rmse_h25 | elasticnet | 1.335 [0.269, 2.690] |  |  | 4 | 5 | e4512909 |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer | 0.743 [0.148, 1.745] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer_sc | 0.940 [0.281, 2.021] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | frac:0.3 | rmse_h25 | lgbm | 0.965 [0.274, 1.657] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | frac:0.3 | rmse_h25 | lstm | 0.839 [0.534, 1.389] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | frac:0.3 | rmse_h25 | transformer | 1.050 [0.379, 2.257] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | frac:0.3 | rmse_h50 | elasticnet | 3.617 [1.268, 7.188] |  |  | 4 | 5 | e4512909 |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer | 2.544 [0.739, 5.182] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer_sc | 2.595 [0.502, 5.807] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | frac:0.3 | rmse_h50 | lgbm | 2.680 [1.388, 4.907] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | frac:0.3 | rmse_h50 | lstm | 2.683 [0.754, 5.263] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | frac:0.3 | rmse_h50 | transformer | 2.742 [1.014, 5.113] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | frac:0.5 | rmse_h1 | elasticnet | 0.489 [0.265, 0.804] |  |  | 4 | 5 | e4512909 |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer | 0.465 [0.062, 0.956] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer_sc | 0.497 [0.070, 0.970] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | frac:0.5 | rmse_h1 | lgbm | 0.480 [0.027, 0.992] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | frac:0.5 | rmse_h1 | lstm | 0.509 [0.078, 0.984] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | frac:0.5 | rmse_h1 | transformer | 0.579 [0.323, 0.909] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | frac:0.5 | rmse_h10 | elasticnet | 1.106 [0.879, 1.422] |  |  | 4 | 5 | e4512909 |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer | 0.978 [0.421, 1.384] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer_sc | 0.971 [0.485, 1.344] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | frac:0.5 | rmse_h10 | lgbm | 0.943 [0.288, 1.597] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | frac:0.5 | rmse_h10 | lstm | 0.924 [0.384, 1.465] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | frac:0.5 | rmse_h10 | transformer | 0.965 [0.619, 1.338] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | frac:0.5 | rmse_h100 | elasticnet | 1.550 [0.657, 2.444] |  |  | 4 | 5 | e4512909 |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer | 1.391 [0.767, 2.194] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer_sc | 1.084 [0.771, 1.590] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | frac:0.5 | rmse_h100 | lgbm | 0.897 [0.516, 1.100] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | frac:0.5 | rmse_h100 | lstm | 1.048 [0.198, 1.897] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | frac:0.5 | rmse_h100 | transformer | 1.130 [0.384, 1.876] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | frac:0.5 | rmse_h25 | elasticnet | 1.380 [0.747, 2.014] |  |  | 4 | 5 | e4512909 |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer | 1.010 [0.497, 1.458] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer_sc | 1.114 [0.725, 1.462] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | frac:0.5 | rmse_h25 | lgbm | 0.896 [0.264, 1.527] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | frac:0.5 | rmse_h25 | lstm | 1.286 [0.711, 1.824] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | frac:0.5 | rmse_h25 | transformer | 1.043 [0.667, 1.419] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | frac:0.5 | rmse_h50 | elasticnet | 1.556 [1.004, 2.433] |  |  | 4 | 5 | e4512909 |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer | 0.835 [0.363, 1.307] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer_sc | 0.485 [0.131, 1.073] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | frac:0.5 | rmse_h50 | lgbm | 0.457 [0.149, 0.766] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | frac:0.5 | rmse_h50 | lstm | 0.969 [0.147, 1.791] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | frac:0.5 | rmse_h50 | transformer | 0.903 [0.295, 1.511] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | frac:0.7 | rmse_h1 | elasticnet | 0.394 [0.209, 0.579] |  |  | 4 | 5 | e4512909 |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer | 0.139 [0.042, 0.235] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer_sc | 0.194 [0.065, 0.334] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | frac:0.7 | rmse_h1 | lgbm | 0.111 [0.023, 0.227] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | frac:0.7 | rmse_h1 | lstm | 0.156 [0.098, 0.214] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | frac:0.7 | rmse_h1 | transformer | 0.378 [0.286, 0.502] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | frac:0.7 | rmse_h10 | elasticnet | 0.840 [0.612, 1.192] |  |  | 4 | 5 | e4512909 |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer | 0.605 [0.253, 1.197] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer_sc | 0.480 [0.177, 0.965] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | frac:0.7 | rmse_h10 | lgbm | 0.439 [0.092, 0.970] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | frac:0.7 | rmse_h10 | lstm | 0.532 [0.213, 1.046] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | frac:0.7 | rmse_h10 | transformer | 0.591 [0.276, 0.999] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | frac:0.7 | rmse_h100 | elasticnet | 4.318 [2.875, 5.762] |  |  | 4 | 5 | e4512909 |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer | 2.017 [1.162, 3.227] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer_sc | 1.855 [0.341, 3.368] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | frac:0.7 | rmse_h100 | lgbm | 1.878 [0.608, 3.147] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | frac:0.7 | rmse_h100 | lstm | 2.751 [1.386, 3.803] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | frac:0.7 | rmse_h100 | transformer | 2.757 [1.235, 4.279] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | frac:0.7 | rmse_h25 | elasticnet | 1.781 [0.183, 3.378] |  |  | 4 | 5 | e4512909 |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer | 1.056 [0.492, 1.624] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer_sc | 0.961 [0.446, 1.264] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | frac:0.7 | rmse_h25 | lgbm | 0.696 [0.270, 0.984] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | frac:0.7 | rmse_h25 | lstm | 0.965 [0.477, 1.615] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | frac:0.7 | rmse_h25 | transformer | 1.296 [0.719, 1.858] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | frac:0.7 | rmse_h50 | elasticnet | 3.186 [1.524, 4.847] |  |  | 4 | 5 | e4512909 |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer | 1.520 [0.949, 2.261] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer_sc | 1.433 [0.905, 1.961] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | frac:0.7 | rmse_h50 | lgbm | 1.125 [0.552, 1.727] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | frac:0.7 | rmse_h50 | lstm | 1.718 [0.844, 2.534] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | frac:0.7 | rmse_h50 | transformer | 1.798 [0.965, 2.311] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | overall | rmse_h1 | elasticnet | 0.478 [0.370, 0.631] |  |  | 4 | 5 | e4512909 |
| loco | start_points | overall | rmse_h1 | itransformer | 0.400 [0.211, 0.588] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | overall | rmse_h1 | itransformer_sc | 0.408 [0.212, 0.605] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | overall | rmse_h1 | lgbm | 0.371 [0.174, 0.568] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | overall | rmse_h1 | lstm | 0.411 [0.212, 0.611] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | overall | rmse_h1 | transformer | 0.519 [0.380, 0.618] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | overall | rmse_h10 | elasticnet | 1.189 [0.707, 1.962] |  |  | 4 | 5 | e4512909 |
| loco | start_points | overall | rmse_h10 | itransformer | 1.040 [0.651, 1.614] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | overall | rmse_h10 | itransformer_sc | 1.025 [0.635, 1.625] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | overall | rmse_h10 | lgbm | 1.111 [0.656, 1.748] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | overall | rmse_h10 | lstm | 1.058 [0.611, 1.771] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | overall | rmse_h10 | transformer | 1.140 [0.719, 1.794] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | overall | rmse_h100 | elasticnet | 3.388 [2.104, 4.671] |  |  | 4 | 5 | e4512909 |
| loco | start_points | overall | rmse_h100 | itransformer | 2.055 [1.226, 2.905] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | overall | rmse_h100 | itransformer_sc | 2.329 [1.200, 3.528] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | overall | rmse_h100 | lgbm | 1.971 [1.251, 2.553] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | overall | rmse_h100 | lstm | 2.346 [1.460, 3.081] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | overall | rmse_h100 | transformer | 2.395 [1.542, 3.029] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | overall | rmse_h25 | elasticnet | 1.968 [1.121, 3.087] |  |  | 4 | 5 | e4512909 |
| loco | start_points | overall | rmse_h25 | itransformer | 1.277 [0.950, 1.838] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | overall | rmse_h25 | itransformer_sc | 1.240 [0.836, 1.780] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | overall | rmse_h25 | lgbm | 1.382 [0.897, 1.991] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | overall | rmse_h25 | lstm | 1.463 [0.998, 2.012] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | overall | rmse_h25 | transformer | 1.693 [1.140, 2.371] |  |  | 4 | 5 | c550b9cd |
| loco | start_points | overall | rmse_h50 | elasticnet | 2.898 [1.474, 4.634] |  |  | 4 | 5 | e4512909 |
| loco | start_points | overall | rmse_h50 | itransformer | 1.741 [0.970, 2.827] |  |  | 4 | 5 | 6e8e8987 |
| loco | start_points | overall | rmse_h50 | itransformer_sc | 1.818 [1.023, 2.987] |  |  | 4 | 5 | 8c777c2f |
| loco | start_points | overall | rmse_h50 | lgbm | 1.922 [1.146, 2.963] |  |  | 4 | 5 | edf9dba9 |
| loco | start_points | overall | rmse_h50 | lstm | 2.061 [1.103, 3.235] |  |  | 4 | 5 | 46e0307f |
| loco | start_points | overall | rmse_h50 | transformer | 2.108 [1.184, 3.142] |  |  | 4 | 5 | c550b9cd |

</details>

<details><summary>nasa_forecast (210 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | elasticnet | 0.938 [0.744, 1.132] |  | 1.093 | 4 | 5 | 1240eca2 |
| loco | all | overall | rmse_h1 | itransformer | 0.857 [0.643, 1.070] |  | 1.067 | 4 | 5 | f438e343 |
| loco | all | overall | rmse_h1 | itransformer_sc | 0.906 [0.667, 1.145] |  | 1.196 | 4 | 5 | 37ed894e |
| loco | all | overall | rmse_h1 | lgbm | 0.852 [0.639, 1.065] |  | 1.027 | 4 | 5 | 5bf5307f |
| loco | all | overall | rmse_h1 | lstm | 1.343 [0.781, 2.003] |  | 2.406 | 4 | 5 | 911aa065 |
| loco | all | overall | rmse_h1 | transformer | 2.299 [1.354, 3.397] |  | 4.043 | 4 | 5 | f91ffc71 |
| loco | all | overall | rmse_h10 | elasticnet | 1.788 [1.316, 2.410] |  | 1.731 | 4 | 5 | 1240eca2 |
| loco | all | overall | rmse_h10 | itransformer | 1.499 [0.996, 2.002] |  | 2.249 | 4 | 5 | f438e343 |
| loco | all | overall | rmse_h10 | itransformer_sc | 1.720 [1.125, 2.316] |  | 2.533 | 4 | 5 | 37ed894e |
| loco | all | overall | rmse_h10 | lgbm | 1.448 [1.000, 1.896] |  | 1.849 | 4 | 5 | 5bf5307f |
| loco | all | overall | rmse_h10 | lstm | 2.034 [1.347, 2.722] |  | 2.756 | 4 | 5 | 911aa065 |
| loco | all | overall | rmse_h10 | transformer | 3.026 [1.993, 4.328] |  | 5.099 | 4 | 5 | f91ffc71 |
| loco | all | overall | rmse_h100 | elasticnet | 6.725 [2.659, 11.291] |  | 2.548 | 4 | 5 | 1240eca2 |
| loco | all | overall | rmse_h100 | itransformer | 13.905 [13.003, 15.603] |  | 12.956 | 4 | 5 | f438e343 |
| loco | all | overall | rmse_h100 | itransformer_sc | 8.917 [7.132, 10.677] |  | 8.701 | 4 | 5 | 37ed894e |
| loco | all | overall | rmse_h100 | lgbm | 3.893 [2.472, 5.313] |  | 2.694 | 4 | 5 | 5bf5307f |
| loco | all | overall | rmse_h100 | lstm | 4.958 [3.228, 6.404] |  | 4.717 | 4 | 5 | 911aa065 |
| loco | all | overall | rmse_h100 | transformer | 6.363 [3.772, 8.380] |  | 8.961 | 4 | 5 | f91ffc71 |
| loco | all | overall | rmse_h25 | elasticnet | 3.408 [2.232, 4.584] |  | 2.792 | 4 | 5 | 1240eca2 |
| loco | all | overall | rmse_h25 | itransformer | 2.468 [1.906, 3.297] |  | 3.760 | 4 | 5 | f438e343 |
| loco | all | overall | rmse_h25 | itransformer_sc | 2.657 [1.608, 3.988] |  | 4.737 | 4 | 5 | 37ed894e |
| loco | all | overall | rmse_h25 | lgbm | 2.349 [1.779, 2.919] |  | 2.853 | 4 | 5 | 5bf5307f |
| loco | all | overall | rmse_h25 | lstm | 3.047 [2.103, 3.992] |  | 3.856 | 4 | 5 | 911aa065 |
| loco | all | overall | rmse_h25 | transformer | 3.865 [3.070, 4.661] |  | 4.458 | 4 | 5 | f91ffc71 |
| loco | all | overall | rmse_h50 | elasticnet | 4.176 [2.737, 5.413] |  | 4.457 | 4 | 5 | 1240eca2 |
| loco | all | overall | rmse_h50 | itransformer | 5.279 [5.033, 5.525] |  | 5.074 | 4 | 5 | f438e343 |
| loco | all | overall | rmse_h50 | itransformer_sc | 3.836 [3.741, 3.977] |  | 4.047 | 4 | 5 | 37ed894e |
| loco | all | overall | rmse_h50 | lgbm | 3.213 [2.381, 4.186] |  | 3.051 | 4 | 5 | 5bf5307f |
| loco | all | overall | rmse_h50 | lstm | 3.848 [2.957, 4.975] |  | 3.580 | 4 | 5 | 911aa065 |
| loco | all | overall | rmse_h50 | transformer | 4.741 [3.265, 5.689] |  | 5.859 | 4 | 5 | f91ffc71 |
| loco | start_points | fixed:30 | rmse_h1 | elasticnet | 1.221 [0.579, 1.863] |  | 0.401 | 4 | 5 | 1240eca2 |
| loco | start_points | fixed:30 | rmse_h1 | itransformer | 2.137 [0.784, 3.295] |  | 0.131 | 4 | 5 | f438e343 |
| loco | start_points | fixed:30 | rmse_h1 | itransformer_sc | 2.126 [0.819, 3.180] |  | 0.154 | 4 | 5 | 37ed894e |
| loco | start_points | fixed:30 | rmse_h1 | lgbm | 1.924 [0.786, 2.885] |  | 0.241 | 4 | 5 | 5bf5307f |
| loco | start_points | fixed:30 | rmse_h1 | lstm | 1.454 [1.170, 1.672] |  | 1.535 | 4 | 5 | 911aa065 |
| loco | start_points | fixed:30 | rmse_h1 | transformer | 1.808 [1.201, 2.414] |  | 1.160 | 4 | 5 | f91ffc71 |
| loco | start_points | fixed:30 | rmse_h10 | elasticnet | 1.702 [0.708, 3.139] |  | 1.505 | 4 | 5 | 1240eca2 |
| loco | start_points | fixed:30 | rmse_h10 | itransformer | 0.986 [0.298, 1.839] |  | 2.351 | 4 | 5 | f438e343 |
| loco | start_points | fixed:30 | rmse_h10 | itransformer_sc | 1.139 [0.524, 1.754] |  | 1.889 | 4 | 5 | 37ed894e |
| loco | start_points | fixed:30 | rmse_h10 | lgbm | 0.767 [0.042, 1.929] |  | 0.016 | 4 | 5 | 5bf5307f |
| loco | start_points | fixed:30 | rmse_h10 | lstm | 1.210 [0.689, 1.998] |  | 1.052 | 4 | 5 | 911aa065 |
| loco | start_points | fixed:30 | rmse_h10 | transformer | 1.768 [1.344, 2.336] |  | 1.486 | 4 | 5 | f91ffc71 |
| loco | start_points | fixed:30 | rmse_h100 | elasticnet | 6.636 [2.822, 11.448] |  | 2.343 | 4 | 5 | 1240eca2 |
| loco | start_points | fixed:30 | rmse_h100 | itransformer | 13.187 [7.512, 17.814] |  | 4.636 | 4 | 5 | f438e343 |
| loco | start_points | fixed:30 | rmse_h100 | itransformer_sc | 8.740 [4.442, 13.038] |  | 5.403 | 4 | 5 | 37ed894e |
| loco | start_points | fixed:30 | rmse_h100 | lgbm | 4.125 [2.980, 5.604] |  | 3.065 | 4 | 5 | 5bf5307f |
| loco | start_points | fixed:30 | rmse_h100 | lstm | 4.086 [2.154, 6.017] |  | 2.790 | 4 | 5 | 911aa065 |
| loco | start_points | fixed:30 | rmse_h100 | transformer | 7.374 [3.453, 12.184] |  | 14.304 | 4 | 5 | f91ffc71 |
| loco | start_points | fixed:30 | rmse_h25 | elasticnet | 4.699 [3.714, 5.758] |  | 6.227 | 4 | 5 | 1240eca2 |
| loco | start_points | fixed:30 | rmse_h25 | itransformer | 1.998 [1.062, 2.934] |  | 3.139 | 4 | 5 | f438e343 |
| loco | start_points | fixed:30 | rmse_h25 | itransformer_sc | 1.860 [0.960, 2.965] |  | 3.468 | 4 | 5 | 37ed894e |
| loco | start_points | fixed:30 | rmse_h25 | lgbm | 1.605 [0.701, 3.230] |  | 0.856 | 4 | 5 | 5bf5307f |
| loco | start_points | fixed:30 | rmse_h25 | lstm | 2.781 [1.872, 3.793] |  | 2.384 | 4 | 5 | 911aa065 |
| loco | start_points | fixed:30 | rmse_h25 | transformer | 4.034 [3.114, 4.895] |  | 3.714 | 4 | 5 | f91ffc71 |
| loco | start_points | fixed:30 | rmse_h50 | elasticnet | 5.211 [2.126, 8.297] |  | 8.684 | 4 | 5 | 1240eca2 |
| loco | start_points | fixed:30 | rmse_h50 | itransformer | 6.816 [3.982, 9.362] |  | 2.221 | 4 | 5 | f438e343 |
| loco | start_points | fixed:30 | rmse_h50 | itransformer_sc | 4.920 [2.647, 6.966] |  | 1.252 | 4 | 5 | 37ed894e |
| loco | start_points | fixed:30 | rmse_h50 | lgbm | 3.049 [1.341, 5.384] |  | 2.871 | 4 | 5 | 5bf5307f |
| loco | start_points | fixed:30 | rmse_h50 | lstm | 3.773 [2.069, 6.208] |  | 1.957 | 4 | 5 | 911aa065 |
| loco | start_points | fixed:30 | rmse_h50 | transformer | 3.463 [2.655, 4.433] |  | 3.160 | 4 | 5 | f91ffc71 |
| loco | start_points | fixed:50 | rmse_h1 | elasticnet | 0.543 [0.152, 0.935] |  | 0.837 | 4 | 5 | 1240eca2 |
| loco | start_points | fixed:50 | rmse_h1 | itransformer | 0.388 [0.095, 0.681] |  | 0.733 | 4 | 5 | f438e343 |
| loco | start_points | fixed:50 | rmse_h1 | itransformer_sc | 0.441 [0.077, 0.805] |  | 0.660 | 4 | 5 | 37ed894e |
| loco | start_points | fixed:50 | rmse_h1 | lgbm | 0.346 [0.012, 0.845] |  | 0.238 | 4 | 5 | 5bf5307f |
| loco | start_points | fixed:50 | rmse_h1 | lstm | 0.619 [0.390, 0.867] |  | 0.968 | 4 | 5 | 911aa065 |
| loco | start_points | fixed:50 | rmse_h1 | transformer | 2.300 [1.346, 3.254] |  | 3.215 | 4 | 5 | f91ffc71 |
| loco | start_points | fixed:50 | rmse_h10 | elasticnet | 1.929 [0.924, 3.034] |  | 0.577 | 4 | 5 | 1240eca2 |
| loco | start_points | fixed:50 | rmse_h10 | itransformer | 0.622 [0.328, 0.853] |  | 0.166 | 4 | 5 | f438e343 |
| loco | start_points | fixed:50 | rmse_h10 | itransformer_sc | 1.528 [0.855, 2.713] |  | 1.084 | 4 | 5 | 37ed894e |
| loco | start_points | fixed:50 | rmse_h10 | lgbm | 1.384 [0.281, 2.856] |  | 1.330 | 4 | 5 | 5bf5307f |
| loco | start_points | fixed:50 | rmse_h10 | lstm | 1.838 [0.714, 3.129] |  | 2.010 | 4 | 5 | 911aa065 |
| loco | start_points | fixed:50 | rmse_h10 | transformer | 2.707 [1.768, 3.646] |  | 3.627 | 4 | 5 | f91ffc71 |
| loco | start_points | fixed:50 | rmse_h100 | elasticnet | 8.190 [3.309, 13.820] |  |  | 3 | 5 | ec50cca0 |
| loco | start_points | fixed:50 | rmse_h100 | itransformer | 11.497 [7.817, 15.739] |  |  | 3 | 5 | b20eedac |
| loco | start_points | fixed:50 | rmse_h100 | itransformer_sc | 3.937 [1.622, 7.914] |  |  | 3 | 5 | bfc1efae |
| loco | start_points | fixed:50 | rmse_h100 | lgbm | 4.292 [3.491, 5.750] |  |  | 3 | 5 | e0211c7a |
| loco | start_points | fixed:50 | rmse_h100 | lstm | 5.573 [2.809, 7.716] |  |  | 3 | 5 | 14edf761 |
| loco | start_points | fixed:50 | rmse_h100 | transformer | 4.561 [2.105, 6.592] |  |  | 3 | 5 | 2572f5dc |
| loco | start_points | fixed:50 | rmse_h25 | elasticnet | 4.168 [2.707, 5.202] |  | 4.359 | 4 | 5 | 1240eca2 |
| loco | start_points | fixed:50 | rmse_h25 | itransformer | 2.865 [2.167, 3.692] |  | 1.895 | 4 | 5 | f438e343 |
| loco | start_points | fixed:50 | rmse_h25 | itransformer_sc | 3.423 [2.024, 5.008] |  | 3.524 | 4 | 5 | 37ed894e |
| loco | start_points | fixed:50 | rmse_h25 | lgbm | 3.206 [1.207, 5.431] |  | 2.719 | 4 | 5 | 5bf5307f |
| loco | start_points | fixed:50 | rmse_h25 | lstm | 3.191 [1.263, 5.752] |  | 2.787 | 4 | 5 | 911aa065 |
| loco | start_points | fixed:50 | rmse_h25 | transformer | 4.069 [1.983, 6.655] |  | 4.256 | 4 | 5 | f91ffc71 |
| loco | start_points | fixed:50 | rmse_h50 | elasticnet | 3.481 [1.316, 4.726] |  | 4.856 | 4 | 5 | 1240eca2 |
| loco | start_points | fixed:50 | rmse_h50 | itransformer | 5.257 [2.670, 7.643] |  | 5.401 | 4 | 5 | f438e343 |
| loco | start_points | fixed:50 | rmse_h50 | itransformer_sc | 4.120 [2.287, 5.296] |  | 5.472 | 4 | 5 | 37ed894e |
| loco | start_points | fixed:50 | rmse_h50 | lgbm | 3.940 [2.183, 5.335] |  | 4.983 | 4 | 5 | 5bf5307f |
| loco | start_points | fixed:50 | rmse_h50 | lstm | 3.331 [1.989, 4.686] |  | 2.841 | 4 | 5 | 911aa065 |
| loco | start_points | fixed:50 | rmse_h50 | transformer | 3.236 [1.806, 4.665] |  | 4.261 | 4 | 5 | f91ffc71 |
| loco | start_points | frac:0.3 | rmse_h1 | elasticnet | 0.126 [0.113, 0.140] |  | 0.146 | 4 | 5 | 1240eca2 |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer | 0.183 [0.083, 0.328] |  | 0.075 | 4 | 5 | f438e343 |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer_sc | 0.169 [0.070, 0.280] |  | 0.143 | 4 | 5 | 37ed894e |
| loco | start_points | frac:0.3 | rmse_h1 | lgbm | 0.113 [0.049, 0.165] |  | 0.014 | 4 | 5 | 5bf5307f |
| loco | start_points | frac:0.3 | rmse_h1 | lstm | 1.101 [0.855, 1.439] |  | 1.585 | 4 | 5 | 911aa065 |
| loco | start_points | frac:0.3 | rmse_h1 | transformer | 1.849 [1.135, 2.516] |  | 1.930 | 4 | 5 | f91ffc71 |
| loco | start_points | frac:0.3 | rmse_h10 | elasticnet | 1.441 [1.062, 2.076] |  | 1.053 | 4 | 5 | 1240eca2 |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer | 1.304 [0.416, 2.192] |  | 0.188 | 4 | 5 | f438e343 |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer_sc | 1.218 [0.580, 1.794] |  | 0.185 | 4 | 5 | 37ed894e |
| loco | start_points | frac:0.3 | rmse_h10 | lgbm | 0.399 [0.064, 0.733] |  | 0.046 | 4 | 5 | 5bf5307f |
| loco | start_points | frac:0.3 | rmse_h10 | lstm | 1.580 [0.689, 3.064] |  | 3.774 | 4 | 5 | 911aa065 |
| loco | start_points | frac:0.3 | rmse_h10 | transformer | 1.988 [1.157, 2.918] |  | 3.278 | 4 | 5 | f91ffc71 |
| loco | start_points | frac:0.3 | rmse_h100 | elasticnet | 6.828 [2.731, 12.194] |  | 1.601 | 4 | 5 | 1240eca2 |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer | 13.390 [7.633, 19.359] |  | 5.421 | 4 | 5 | f438e343 |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer_sc | 8.640 [4.935, 13.651] |  | 5.397 | 4 | 5 | 37ed894e |
| loco | start_points | frac:0.3 | rmse_h100 | lgbm | 4.679 [4.289, 5.164] |  | 4.562 | 4 | 5 | 5bf5307f |
| loco | start_points | frac:0.3 | rmse_h100 | lstm | 4.988 [3.636, 5.827] |  | 5.501 | 4 | 5 | 911aa065 |
| loco | start_points | frac:0.3 | rmse_h100 | transformer | 7.503 [3.711, 10.845] |  | 12.189 | 4 | 5 | f91ffc71 |
| loco | start_points | frac:0.3 | rmse_h25 | elasticnet | 3.414 [2.208, 4.619] |  | 2.116 | 4 | 5 | 1240eca2 |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer | 3.392 [1.868, 4.861] |  | 5.361 | 4 | 5 | f438e343 |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer_sc | 3.099 [1.036, 5.945] |  | 7.252 | 4 | 5 | 37ed894e |
| loco | start_points | frac:0.3 | rmse_h25 | lgbm | 2.189 [0.654, 3.724] |  | 4.672 | 4 | 5 | 5bf5307f |
| loco | start_points | frac:0.3 | rmse_h25 | lstm | 3.006 [1.259, 4.753] |  | 3.760 | 4 | 5 | 911aa065 |
| loco | start_points | frac:0.3 | rmse_h25 | transformer | 4.187 [3.069, 5.912] |  | 6.742 | 4 | 5 | f91ffc71 |
| loco | start_points | frac:0.3 | rmse_h50 | elasticnet | 3.952 [1.535, 6.965] |  | 3.480 | 4 | 5 | 1240eca2 |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer | 6.821 [3.694, 9.948] |  | 2.443 | 4 | 5 | f438e343 |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer_sc | 4.895 [2.759, 7.328] |  | 2.730 | 4 | 5 | 37ed894e |
| loco | start_points | frac:0.3 | rmse_h50 | lgbm | 2.814 [0.897, 5.111] |  | 1.027 | 4 | 5 | 5bf5307f |
| loco | start_points | frac:0.3 | rmse_h50 | lstm | 2.903 [1.484, 4.321] |  | 1.543 | 4 | 5 | 911aa065 |
| loco | start_points | frac:0.3 | rmse_h50 | transformer | 4.171 [1.467, 6.823] |  | 4.278 | 4 | 5 | f91ffc71 |
| loco | start_points | frac:0.5 | rmse_h1 | elasticnet | 1.240 [0.039, 2.441] |  | 2.776 | 4 | 5 | 1240eca2 |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer | 1.833 [0.297, 3.369] |  | 2.985 | 4 | 5 | f438e343 |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer_sc | 1.995 [0.336, 3.653] |  | 3.759 | 4 | 5 | 37ed894e |
| loco | start_points | frac:0.5 | rmse_h1 | lgbm | 1.712 [0.318, 3.107] |  | 2.961 | 4 | 5 | 5bf5307f |
| loco | start_points | frac:0.5 | rmse_h1 | lstm | 1.105 [0.419, 1.791] |  | 1.853 | 4 | 5 | 911aa065 |
| loco | start_points | frac:0.5 | rmse_h1 | transformer | 1.576 [0.924, 2.186] |  | 2.130 | 4 | 5 | f91ffc71 |
| loco | start_points | frac:0.5 | rmse_h10 | elasticnet | 2.356 [1.090, 3.622] |  | 3.356 | 4 | 5 | 1240eca2 |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer | 2.141 [0.479, 5.028] |  | 6.437 | 4 | 5 | f438e343 |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer_sc | 2.695 [1.014, 5.616] |  | 7.134 | 4 | 5 | 37ed894e |
| loco | start_points | frac:0.5 | rmse_h10 | lgbm | 2.261 [0.662, 4.108] |  | 5.171 | 4 | 5 | 5bf5307f |
| loco | start_points | frac:0.5 | rmse_h10 | lstm | 1.503 [0.815, 2.192] |  | 1.975 | 4 | 5 | 911aa065 |
| loco | start_points | frac:0.5 | rmse_h10 | transformer | 2.792 [1.419, 4.666] |  | 5.708 | 4 | 5 | f91ffc71 |
| loco | start_points | frac:0.5 | rmse_h100 | elasticnet | 8.326 [2.943, 14.163] |  |  | 3 | 5 | ec50cca0 |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer | 10.347 [4.715, 13.843] |  |  | 3 | 5 | b20eedac |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer_sc | 4.793 [3.481, 6.264] |  |  | 3 | 5 | bfc1efae |
| loco | start_points | frac:0.5 | rmse_h100 | lgbm | 4.720 [1.984, 6.450] |  |  | 3 | 5 | e0211c7a |
| loco | start_points | frac:0.5 | rmse_h100 | lstm | 4.885 [2.018, 6.495] |  |  | 3 | 5 | 14edf761 |
| loco | start_points | frac:0.5 | rmse_h100 | transformer | 5.390 [2.256, 8.090] |  |  | 3 | 5 | 2572f5dc |
| loco | start_points | frac:0.5 | rmse_h25 | elasticnet | 3.430 [1.983, 4.571] |  | 3.577 | 4 | 5 | 1240eca2 |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer | 1.715 [0.515, 2.916] |  | 3.239 | 4 | 5 | f438e343 |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer_sc | 2.531 [1.490, 4.466] |  | 5.447 | 4 | 5 | 37ed894e |
| loco | start_points | frac:0.5 | rmse_h25 | lgbm | 2.241 [1.520, 3.429] |  | 1.395 | 4 | 5 | 5bf5307f |
| loco | start_points | frac:0.5 | rmse_h25 | lstm | 2.166 [1.018, 3.649] |  | 1.852 | 4 | 5 | 911aa065 |
| loco | start_points | frac:0.5 | rmse_h25 | transformer | 2.922 [2.264, 3.988] |  | 2.606 | 4 | 5 | f91ffc71 |
| loco | start_points | frac:0.5 | rmse_h50 | elasticnet | 4.130 [1.337, 6.807] |  | 4.998 | 4 | 5 | 1240eca2 |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer | 3.754 [0.911, 6.597] |  | 1.186 | 4 | 5 | f438e343 |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer_sc | 4.098 [3.339, 4.858] |  | 5.218 | 4 | 5 | 37ed894e |
| loco | start_points | frac:0.5 | rmse_h50 | lgbm | 3.085 [0.863, 5.628] |  | 0.168 | 4 | 5 | 5bf5307f |
| loco | start_points | frac:0.5 | rmse_h50 | lstm | 3.646 [1.392, 6.401] |  | 2.955 | 4 | 5 | 911aa065 |
| loco | start_points | frac:0.5 | rmse_h50 | transformer | 3.760 [1.756, 5.135] |  | 4.049 | 4 | 5 | f91ffc71 |
| loco | start_points | frac:0.7 | rmse_h1 | elasticnet | 1.175 [0.257, 2.700] |  | 3.491 | 4 | 5 | 1240eca2 |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer | 1.109 [0.164, 2.779] |  | 3.608 | 4 | 5 | f438e343 |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer_sc | 1.254 [0.244, 2.942] |  | 3.811 | 4 | 5 | 37ed894e |
| loco | start_points | frac:0.7 | rmse_h1 | lgbm | 1.006 [0.153, 2.486] |  | 3.230 | 4 | 5 | 5bf5307f |
| loco | start_points | frac:0.7 | rmse_h1 | lstm | 1.039 [0.565, 1.589] |  | 1.843 | 4 | 5 | 911aa065 |
| loco | start_points | frac:0.7 | rmse_h1 | transformer | 1.665 [0.867, 2.728] |  | 3.247 | 4 | 5 | f91ffc71 |
| loco | start_points | frac:0.7 | rmse_h10 | elasticnet | 1.442 [0.916, 2.207] |  | 0.794 | 4 | 5 | 1240eca2 |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer | 0.649 [0.569, 0.716] |  | 0.685 | 4 | 5 | f438e343 |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer_sc | 0.966 [0.500, 1.433] |  | 1.337 | 4 | 5 | 37ed894e |
| loco | start_points | frac:0.7 | rmse_h10 | lgbm | 1.014 [0.584, 1.443] |  | 1.535 | 4 | 5 | 5bf5307f |
| loco | start_points | frac:0.7 | rmse_h10 | lstm | 1.810 [0.764, 3.522] |  | 4.372 | 4 | 5 | 911aa065 |
| loco | start_points | frac:0.7 | rmse_h10 | transformer | 2.462 [1.350, 4.392] |  | 5.357 | 4 | 5 | f91ffc71 |
| loco | start_points | frac:0.7 | rmse_h100 | elasticnet | 13.691 |  |  | 1 | 5 | 1b666084 |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer | 8.716 |  |  | 1 | 5 | 36c62a57 |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer_sc | 2.310 |  |  | 1 | 5 | ef7ac00c |
| loco | start_points | frac:0.7 | rmse_h100 | lgbm | 3.734 |  |  | 1 | 5 | 6c14a8e8 |
| loco | start_points | frac:0.7 | rmse_h100 | lstm | 6.480 |  |  | 1 | 5 | 888867a0 |
| loco | start_points | frac:0.7 | rmse_h100 | transformer | 3.678 |  |  | 1 | 5 | eba1faee |
| loco | start_points | frac:0.7 | rmse_h25 | elasticnet | 4.015 [1.363, 6.448] |  | 3.519 | 4 | 5 | 1240eca2 |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer | 1.749 [0.924, 2.573] |  | 2.198 | 4 | 5 | f438e343 |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer_sc | 2.399 [1.356, 3.441] |  | 2.935 | 4 | 5 | 37ed894e |
| loco | start_points | frac:0.7 | rmse_h25 | lgbm | 2.747 [1.694, 3.818] |  | 3.217 | 4 | 5 | 5bf5307f |
| loco | start_points | frac:0.7 | rmse_h25 | lstm | 3.465 [1.591, 5.339] |  | 4.533 | 4 | 5 | 911aa065 |
| loco | start_points | frac:0.7 | rmse_h25 | transformer | 3.594 [2.159, 5.603] |  | 2.801 | 4 | 5 | f91ffc71 |
| loco | start_points | frac:0.7 | rmse_h50 | elasticnet | 3.991 [2.328, 5.204] |  | 5.467 | 4 | 5 | 1240eca2 |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer | 2.195 [1.157, 3.660] |  | 4.326 | 4 | 5 | f438e343 |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer_sc | 2.409 [1.553, 3.500] |  | 4.048 | 4 | 5 | 37ed894e |
| loco | start_points | frac:0.7 | rmse_h50 | lgbm | 2.727 [1.808, 3.646] |  | 3.415 | 4 | 5 | 5bf5307f |
| loco | start_points | frac:0.7 | rmse_h50 | lstm | 3.073 [2.459, 3.781] |  | 4.202 | 4 | 5 | 911aa065 |
| loco | start_points | frac:0.7 | rmse_h50 | transformer | 3.705 [2.100, 5.309] |  | 5.282 | 4 | 5 | f91ffc71 |
| loco | start_points | overall | rmse_h1 | elasticnet | 1.156 [0.586, 1.727] |  | 2.038 | 4 | 5 | 1240eca2 |
| loco | start_points | overall | rmse_h1 | itransformer | 1.666 [1.064, 2.267] |  | 2.123 | 4 | 5 | f438e343 |
| loco | start_points | overall | rmse_h1 | itransformer_sc | 1.732 [1.100, 2.364] |  | 2.416 | 4 | 5 | 37ed894e |
| loco | start_points | overall | rmse_h1 | lgbm | 1.504 [0.960, 2.048] |  | 1.965 | 4 | 5 | 5bf5307f |
| loco | start_points | overall | rmse_h1 | lstm | 1.292 [0.909, 1.675] |  | 1.850 | 4 | 5 | 911aa065 |
| loco | start_points | overall | rmse_h1 | transformer | 2.133 [1.389, 2.754] |  | 2.900 | 4 | 5 | f91ffc71 |
| loco | start_points | overall | rmse_h10 | elasticnet | 1.898 [1.258, 2.812] |  | 1.766 | 4 | 5 | 1240eca2 |
| loco | start_points | overall | rmse_h10 | itransformer | 1.555 [0.919, 2.563] |  | 3.093 | 4 | 5 | f438e343 |
| loco | start_points | overall | rmse_h10 | itransformer_sc | 1.892 [1.088, 2.831] |  | 3.406 | 4 | 5 | 37ed894e |
| loco | start_points | overall | rmse_h10 | lgbm | 1.470 [0.496, 2.445] |  | 2.485 | 4 | 5 | 5bf5307f |
| loco | start_points | overall | rmse_h10 | lstm | 1.837 [0.923, 2.751] |  | 3.058 | 4 | 5 | 911aa065 |
| loco | start_points | overall | rmse_h10 | transformer | 2.782 [1.714, 4.037] |  | 4.739 | 4 | 5 | f91ffc71 |
| loco | start_points | overall | rmse_h100 | elasticnet | 6.698 [2.688, 11.469] |  | 2.006 | 4 | 5 | 1240eca2 |
| loco | start_points | overall | rmse_h100 | itransformer | 11.564 [6.862, 16.218] |  | 5.046 | 4 | 5 | f438e343 |
| loco | start_points | overall | rmse_h100 | itransformer_sc | 7.107 [4.376, 10.415] |  | 5.413 | 4 | 5 | 37ed894e |
| loco | start_points | overall | rmse_h100 | lgbm | 4.346 [3.633, 5.201] |  | 3.887 | 4 | 5 | 5bf5307f |
| loco | start_points | overall | rmse_h100 | lstm | 4.913 [3.346, 6.384] |  | 4.415 | 4 | 5 | 911aa065 |
| loco | start_points | overall | rmse_h100 | transformer | 7.342 [3.598, 11.609] |  | 13.335 | 4 | 5 | f91ffc71 |
| loco | start_points | overall | rmse_h25 | elasticnet | 4.097 [2.691, 5.257] |  | 4.182 | 4 | 5 | 1240eca2 |
| loco | start_points | overall | rmse_h25 | itransformer | 2.646 [2.150, 3.175] |  | 3.424 | 4 | 5 | f438e343 |
| loco | start_points | overall | rmse_h25 | itransformer_sc | 2.969 [1.891, 4.130] |  | 4.846 | 4 | 5 | 37ed894e |
| loco | start_points | overall | rmse_h25 | lgbm | 2.630 [1.581, 3.796] |  | 2.907 | 4 | 5 | 5bf5307f |
| loco | start_points | overall | rmse_h25 | lstm | 3.219 [1.818, 4.706] |  | 3.575 | 4 | 5 | 911aa065 |
| loco | start_points | overall | rmse_h25 | transformer | 4.134 [3.073, 5.196] |  | 4.671 | 4 | 5 | f91ffc71 |
| loco | start_points | overall | rmse_h50 | elasticnet | 4.333 [2.184, 6.281] |  | 5.761 | 4 | 5 | 1240eca2 |
| loco | start_points | overall | rmse_h50 | itransformer | 5.656 [4.084, 7.346] |  | 3.497 | 4 | 5 | f438e343 |
| loco | start_points | overall | rmse_h50 | itransformer_sc | 4.520 [3.944, 5.390] |  | 4.147 | 4 | 5 | 37ed894e |
| loco | start_points | overall | rmse_h50 | lgbm | 3.445 [2.483, 5.000] |  | 3.027 | 4 | 5 | 5bf5307f |
| loco | start_points | overall | rmse_h50 | lstm | 3.616 [2.276, 5.293] |  | 3.053 | 4 | 5 | 911aa065 |
| loco | start_points | overall | rmse_h50 | transformer | 4.002 [2.403, 4.936] |  | 4.538 | 4 | 5 | f91ffc71 |

</details>
