# Benchmark tables: abl_calce_clean

- Protocol version: 1.1
- Git SHA: d6c6d4ba64
- Seeds: 5  |  unit runs: 260
- Note: n = 4 cells per NASA/CALCE dataset, so the 95 % cluster-bootstrap CI is wide by construction. Toyota rows are over test cells (test1 / test2 separately) with a cell-level bootstrap CI and a Holm-adjusted Wilcoxon p vs the best baseline. All metrics are computed per cell from the logged predictions.

## Headline (kind = overall; RMSE in %SOH, RUL MAE in cycles)

### calce_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | elasticnet | 0.562 [0.524, 0.612] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | all | overall | rmse_h1 | itransformer | 0.542 [0.504, 0.591] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | all | overall | rmse_h1 | itransformer_sc | 0.553 [0.515, 0.602] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | all | overall | rmse_h1 | lgbm | 0.548 [0.509, 0.597] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | all | overall | rmse_h1 | lstm | 0.582 [0.544, 0.630] | 2/4 cells, 11/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | all | overall | rmse_h1 | nlinear | 0.564 [0.524, 0.614] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | all | overall | rmse_h1 | persistence | 0.575 [0.537, 0.623] |  |  | 4 | 5 | 67153a79 |
| loco | all | overall | rmse_h10 | elasticnet | 1.439 [1.346, 1.532] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | all | overall | rmse_h10 | itransformer | 1.228 [1.085, 1.372] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | all | overall | rmse_h10 | itransformer_sc | 1.263 [1.137, 1.389] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | all | overall | rmse_h10 | lgbm | 1.242 [1.149, 1.331] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | all | overall | rmse_h10 | lstm | 1.342 [1.265, 1.394] | 4/4 cells, 19/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | all | overall | rmse_h10 | nlinear | 1.462 [1.361, 1.559] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | all | overall | rmse_h10 | persistence | 1.731 [1.627, 1.830] |  |  | 4 | 5 | 67153a79 |
| loco | all | overall | rmse_h50 | elasticnet | 3.382 [2.457, 4.537] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | all | overall | rmse_h50 | itransformer | 2.275 [1.968, 2.582] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | all | overall | rmse_h50 | itransformer_sc | 2.141 [1.762, 2.520] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | all | overall | rmse_h50 | lgbm | 1.980 [1.724, 2.370] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | all | overall | rmse_h50 | lstm | 2.341 [1.773, 2.737] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | all | overall | rmse_h50 | nlinear | 3.359 [3.047, 3.671] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | all | overall | rmse_h50 | persistence | 5.704 [5.246, 6.041] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | overall | rmse_h1 | elasticnet | 0.383 [0.180, 0.585] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | overall | rmse_h1 | itransformer | 0.393 [0.187, 0.599] | 3/4 cells, 12/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | overall | rmse_h1 | itransformer_sc | 0.389 [0.175, 0.603] | 2/4 cells, 12/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | overall | rmse_h1 | lgbm | 0.376 [0.164, 0.588] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | overall | rmse_h1 | lstm | 0.406 [0.199, 0.614] | 2/4 cells, 7/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | overall | rmse_h1 | nlinear | 0.403 [0.191, 0.615] | 1/4 cells, 6/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | overall | rmse_h1 | persistence | 0.397 [0.177, 0.617] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | overall | rmse_h10 | elasticnet | 1.160 [0.821, 1.728] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | overall | rmse_h10 | itransformer | 1.071 [0.653, 1.633] | 3/4 cells, 17/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | overall | rmse_h10 | itransformer_sc | 1.060 [0.748, 1.577] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | overall | rmse_h10 | lgbm | 0.922 [0.576, 1.479] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | overall | rmse_h10 | lstm | 1.010 [0.595, 1.579] | 4/4 cells, 17/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | overall | rmse_h10 | nlinear | 1.141 [0.853, 1.667] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | overall | rmse_h10 | persistence | 1.332 [1.082, 1.703] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | overall | rmse_h50 | elasticnet | 2.147 [1.287, 3.007] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | overall | rmse_h50 | itransformer | 1.553 [1.037, 2.154] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | overall | rmse_h50 | itransformer_sc | 1.481 [1.054, 1.988] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | overall | rmse_h50 | lgbm | 1.493 [0.985, 2.029] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | overall | rmse_h50 | lstm | 1.618 [0.992, 2.062] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | overall | rmse_h50 | nlinear | 1.641 [1.180, 2.274] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | overall | rmse_h50 | persistence | 1.506 [1.020, 1.989] |  |  | 4 | 5 | 67153a79 |

### calce_rul

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rul_mae | elasticnet | 170.161 [83.008, 257.314] |  |  | 4 | 5 | 398ca434 |
| loco | all | overall | rul_mae | itransformer | 69.536 [43.516, 102.239] |  |  | 4 | 5 | f70068d0 |
| loco | all | overall | rul_mae | itransformer_sc | 70.277 [43.146, 107.201] |  |  | 4 | 5 | b71a9d43 |
| loco | all | overall | rul_mae | lgbm | 76.046 [52.399, 102.766] |  |  | 4 | 5 | e452e0fa |
| loco | all | overall | rul_mae | lstm | 74.330 [48.766, 106.407] |  |  | 4 | 5 | befe424d |
| loco | all | overall | rul_mae | nlinear | 125.776 [121.998, 129.799] |  |  | 4 | 5 | b21a6eb6 |
| loco | start_points | overall | rul_mae | elasticnet | 139.405 [72.198, 230.263] |  |  | 4 | 5 | 398ca434 |
| loco | start_points | overall | rul_mae | itransformer | 79.694 [48.072, 122.133] |  |  | 4 | 5 | f70068d0 |
| loco | start_points | overall | rul_mae | itransformer_sc | 81.815 [45.506, 119.602] |  |  | 4 | 5 | b71a9d43 |
| loco | start_points | overall | rul_mae | lgbm | 85.329 [58.105, 123.423] |  |  | 4 | 5 | e452e0fa |
| loco | start_points | overall | rul_mae | lstm | 85.038 [52.515, 117.561] |  |  | 4 | 5 | befe424d |
| loco | start_points | overall | rul_mae | nlinear | 98.372 [61.249, 123.680] |  |  | 4 | 5 | b21a6eb6 |

## Mean rank (dataset x task x split x policy x headline metric)

| model | mean rank | conditions | missing |
|---|---|---|---|
| lgbm | 2.12 | 8 | 0 |
| itransformer | 2.38 | 8 | 0 |
| itransformer_sc | 2.38 | 8 | 0 |
| lstm | 4.38 | 8 | 0 |
| elasticnet | 5.25 | 8 | 0 |
| nlinear | 5.38 | 8 | 0 |
| persistence | 5.83 | 6 | 2 |

## Full tables

<details><summary>calce_forecast (245 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | elasticnet | 0.562 [0.524, 0.612] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | all | overall | rmse_h1 | itransformer | 0.542 [0.504, 0.591] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | all | overall | rmse_h1 | itransformer_sc | 0.553 [0.515, 0.602] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | all | overall | rmse_h1 | lgbm | 0.548 [0.509, 0.597] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | all | overall | rmse_h1 | lstm | 0.582 [0.544, 0.630] | 2/4 cells, 11/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | all | overall | rmse_h1 | nlinear | 0.564 [0.524, 0.614] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | all | overall | rmse_h1 | persistence | 0.575 [0.537, 0.623] |  |  | 4 | 5 | 67153a79 |
| loco | all | overall | rmse_h10 | elasticnet | 1.439 [1.346, 1.532] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | all | overall | rmse_h10 | itransformer | 1.228 [1.085, 1.372] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | all | overall | rmse_h10 | itransformer_sc | 1.263 [1.137, 1.389] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | all | overall | rmse_h10 | lgbm | 1.242 [1.149, 1.331] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | all | overall | rmse_h10 | lstm | 1.342 [1.265, 1.394] | 4/4 cells, 19/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | all | overall | rmse_h10 | nlinear | 1.462 [1.361, 1.559] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | all | overall | rmse_h10 | persistence | 1.731 [1.627, 1.830] |  |  | 4 | 5 | 67153a79 |
| loco | all | overall | rmse_h100 | elasticnet | 4.352 [3.282, 5.551] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | all | overall | rmse_h100 | itransformer | 3.482 [3.068, 3.897] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | all | overall | rmse_h100 | itransformer_sc | 3.124 [2.511, 3.737] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | all | overall | rmse_h100 | lgbm | 2.918 [2.505, 3.435] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | all | overall | rmse_h100 | lstm | 3.286 [2.384, 4.134] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | all | overall | rmse_h100 | nlinear | 5.123 [4.784, 5.463] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | all | overall | rmse_h100 | persistence | 9.949 [9.231, 10.667] |  |  | 4 | 5 | 67153a79 |
| loco | all | overall | rmse_h25 | elasticnet | 2.367 [2.173, 2.564] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | all | overall | rmse_h25 | itransformer | 1.755 [1.486, 2.025] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | all | overall | rmse_h25 | itransformer_sc | 1.802 [1.547, 2.057] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | all | overall | rmse_h25 | lgbm | 1.730 [1.537, 1.957] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | all | overall | rmse_h25 | lstm | 1.914 [1.694, 2.037] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | all | overall | rmse_h25 | nlinear | 2.416 [2.222, 2.592] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | all | overall | rmse_h25 | persistence | 3.282 [3.052, 3.442] |  |  | 4 | 5 | 67153a79 |
| loco | all | overall | rmse_h50 | elasticnet | 3.382 [2.457, 4.537] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | all | overall | rmse_h50 | itransformer | 2.275 [1.968, 2.582] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | all | overall | rmse_h50 | itransformer_sc | 2.141 [1.762, 2.520] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | all | overall | rmse_h50 | lgbm | 1.980 [1.724, 2.370] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | all | overall | rmse_h50 | lstm | 2.341 [1.773, 2.737] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | all | overall | rmse_h50 | nlinear | 3.359 [3.047, 3.671] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | all | overall | rmse_h50 | persistence | 5.704 [5.246, 6.041] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | fixed:200 | rmse_h1 | elasticnet | 0.314 [0.234, 0.401] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | fixed:200 | rmse_h1 | itransformer | 0.303 [0.151, 0.455] | 3/4 cells, 16/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | fixed:200 | rmse_h1 | itransformer_sc | 0.320 [0.157, 0.483] | 3/4 cells, 12/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | fixed:200 | rmse_h1 | lgbm | 0.301 [0.155, 0.446] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | fixed:200 | rmse_h1 | lstm | 0.333 [0.219, 0.459] | 2/4 cells, 8/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | fixed:200 | rmse_h1 | nlinear | 0.349 [0.204, 0.513] | 2/4 cells, 9/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | fixed:200 | rmse_h1 | persistence | 0.347 [0.209, 0.485] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | fixed:200 | rmse_h10 | elasticnet | 1.390 [0.393, 3.145] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | fixed:200 | rmse_h10 | itransformer | 1.212 [0.146, 3.021] | 2/4 cells, 12/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | fixed:200 | rmse_h10 | itransformer_sc | 1.278 [0.288, 2.979] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | fixed:200 | rmse_h10 | lgbm | 1.168 [0.144, 2.761] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | fixed:200 | rmse_h10 | lstm | 1.164 [0.221, 2.878] | 2/4 cells, 11/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | fixed:200 | rmse_h10 | nlinear | 1.386 [0.226, 3.236] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | fixed:200 | rmse_h10 | persistence | 1.344 [0.340, 2.774] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | fixed:200 | rmse_h100 | elasticnet | 1.632 [0.574, 2.877] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | fixed:200 | rmse_h100 | itransformer | 0.697 [0.435, 1.066] | 4/4 cells, 18/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | fixed:200 | rmse_h100 | itransformer_sc | 0.701 [0.314, 1.089] | 3/4 cells, 16/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | fixed:200 | rmse_h100 | lgbm | 1.028 [0.301, 1.836] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | fixed:200 | rmse_h100 | lstm | 1.139 [0.503, 1.788] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | fixed:200 | rmse_h100 | nlinear | 1.393 [0.720, 2.404] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | fixed:200 | rmse_h100 | persistence | 1.897 [1.120, 2.489] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | fixed:200 | rmse_h25 | elasticnet | 1.792 [0.835, 2.748] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | fixed:200 | rmse_h25 | itransformer | 1.412 [0.832, 1.991] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | fixed:200 | rmse_h25 | itransformer_sc | 1.499 [0.939, 2.059] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | fixed:200 | rmse_h25 | lgbm | 1.632 [1.217, 2.048] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | fixed:200 | rmse_h25 | lstm | 1.432 [0.826, 2.037] | 0/4 cells, 1/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | fixed:200 | rmse_h25 | nlinear | 1.705 [0.892, 2.519] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | fixed:200 | rmse_h25 | persistence | 0.840 [0.239, 1.441] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | fixed:200 | rmse_h50 | elasticnet | 1.669 [0.654, 2.857] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | fixed:200 | rmse_h50 | itransformer | 1.053 [0.804, 1.312] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | fixed:200 | rmse_h50 | itransformer_sc | 0.887 [0.401, 1.373] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | fixed:200 | rmse_h50 | lgbm | 1.502 [0.834, 2.160] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | fixed:200 | rmse_h50 | lstm | 1.146 [0.584, 1.852] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | fixed:200 | rmse_h50 | nlinear | 1.791 [1.290, 2.246] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | fixed:200 | rmse_h50 | persistence | 0.844 [0.319, 1.572] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | fixed:400 | rmse_h1 | elasticnet | 0.141 [0.087, 0.201] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | fixed:400 | rmse_h1 | itransformer | 0.094 [0.021, 0.221] | 1/4 cells, 8/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | fixed:400 | rmse_h1 | itransformer_sc | 0.104 [0.045, 0.219] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | fixed:400 | rmse_h1 | lgbm | 0.082 [0.011, 0.155] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | fixed:400 | rmse_h1 | lstm | 0.124 [0.038, 0.260] | 0/4 cells, 6/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | fixed:400 | rmse_h1 | nlinear | 0.069 [0.018, 0.143] | 2/4 cells, 11/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | fixed:400 | rmse_h1 | persistence | 0.080 [0.019, 0.194] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | fixed:400 | rmse_h10 | elasticnet | 0.960 [0.771, 1.127] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | fixed:400 | rmse_h10 | itransformer | 0.634 [0.287, 0.981] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | fixed:400 | rmse_h10 | itransformer_sc | 0.700 [0.424, 0.972] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | fixed:400 | rmse_h10 | lgbm | 0.521 [0.372, 0.732] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | fixed:400 | rmse_h10 | lstm | 0.703 [0.258, 1.147] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | fixed:400 | rmse_h10 | nlinear | 0.770 [0.267, 1.126] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | fixed:400 | rmse_h10 | persistence | 1.009 [0.324, 1.694] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | fixed:400 | rmse_h100 | elasticnet | 2.383 [0.856, 3.742] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | fixed:400 | rmse_h100 | itransformer | 2.408 [1.136, 3.819] | 3/4 cells, 17/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | fixed:400 | rmse_h100 | itransformer_sc | 1.580 [0.536, 3.337] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | fixed:400 | rmse_h100 | lgbm | 2.694 [2.056, 3.674] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | fixed:400 | rmse_h100 | lstm | 2.919 [2.076, 4.004] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | fixed:400 | rmse_h100 | nlinear | 2.079 [0.657, 3.703] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | fixed:400 | rmse_h100 | persistence | 3.346 [1.619, 5.072] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | fixed:400 | rmse_h25 | elasticnet | 1.234 [0.507, 2.154] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | fixed:400 | rmse_h25 | itransformer | 0.900 [0.397, 1.404] | 3/4 cells, 14/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | fixed:400 | rmse_h25 | itransformer_sc | 1.080 [0.372, 1.879] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | fixed:400 | rmse_h25 | lgbm | 0.783 [0.275, 1.456] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | fixed:400 | rmse_h25 | lstm | 0.755 [0.372, 1.137] | 2/4 cells, 11/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | fixed:400 | rmse_h25 | nlinear | 0.940 [0.677, 1.246] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | fixed:400 | rmse_h25 | persistence | 1.333 [0.586, 2.081] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | fixed:400 | rmse_h50 | elasticnet | 1.841 [1.149, 2.408] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | fixed:400 | rmse_h50 | itransformer | 0.942 [0.366, 1.995] | 3/4 cells, 17/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | fixed:400 | rmse_h50 | itransformer_sc | 1.282 [0.543, 2.064] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | fixed:400 | rmse_h50 | lgbm | 1.030 [0.252, 1.829] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | fixed:400 | rmse_h50 | lstm | 1.121 [0.266, 2.387] | 3/4 cells, 13/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | fixed:400 | rmse_h50 | nlinear | 0.342 [0.148, 0.576] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | fixed:400 | rmse_h50 | persistence | 1.656 [0.742, 2.680] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | frac:0.3 | rmse_h1 | elasticnet | 0.403 [0.153, 0.824] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer | 0.326 [0.043, 0.867] | 2/4 cells, 11/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer_sc | 0.325 [0.034, 0.891] | 3/4 cells, 13/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | frac:0.3 | rmse_h1 | lgbm | 0.345 [0.081, 0.792] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | frac:0.3 | rmse_h1 | lstm | 0.394 [0.148, 0.840] | 1/4 cells, 7/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | frac:0.3 | rmse_h1 | nlinear | 0.327 [0.028, 0.915] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | frac:0.3 | rmse_h1 | persistence | 0.373 [0.089, 0.866] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | frac:0.3 | rmse_h10 | elasticnet | 0.767 [0.301, 1.074] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer | 0.844 [0.526, 1.141] | 3/4 cells, 14/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer_sc | 0.757 [0.349, 1.051] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | frac:0.3 | rmse_h10 | lgbm | 0.905 [0.579, 1.232] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | frac:0.3 | rmse_h10 | lstm | 0.748 [0.464, 1.059] | 3/4 cells, 12/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | frac:0.3 | rmse_h10 | nlinear | 0.648 [0.295, 0.902] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | frac:0.3 | rmse_h10 | persistence | 0.952 [0.590, 1.315] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | frac:0.3 | rmse_h100 | elasticnet | 2.288 [0.833, 3.628] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer | 1.609 [0.688, 2.579] | 2/4 cells, 9/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer_sc | 1.234 [0.397, 2.248] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | frac:0.3 | rmse_h100 | lgbm | 2.052 [1.426, 2.648] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | frac:0.3 | rmse_h100 | lstm | 1.526 [0.621, 2.432] | 2/4 cells, 7/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | frac:0.3 | rmse_h100 | nlinear | 2.497 [1.543, 4.119] | 0/4 cells, 0/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | frac:0.3 | rmse_h100 | persistence | 0.918 [0.565, 1.150] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | frac:0.3 | rmse_h25 | elasticnet | 0.433 [0.054, 1.089] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer | 0.421 [0.126, 0.972] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer_sc | 0.439 [0.131, 0.785] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | frac:0.3 | rmse_h25 | lgbm | 0.716 [0.298, 1.148] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | frac:0.3 | rmse_h25 | lstm | 0.536 [0.277, 0.917] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | frac:0.3 | rmse_h25 | nlinear | 0.459 [0.098, 1.134] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | frac:0.3 | rmse_h25 | persistence | 0.865 [0.571, 1.180] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | frac:0.3 | rmse_h50 | elasticnet | 2.876 [1.392, 4.495] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer | 2.253 [0.945, 4.081] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer_sc | 1.991 [0.933, 3.554] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | frac:0.3 | rmse_h50 | lgbm | 2.146 [1.048, 3.756] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | frac:0.3 | rmse_h50 | lstm | 2.248 [1.072, 3.814] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | frac:0.3 | rmse_h50 | nlinear | 2.228 [0.705, 4.198] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | frac:0.3 | rmse_h50 | persistence | 1.300 [0.353, 2.350] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | frac:0.5 | rmse_h1 | elasticnet | 0.501 [0.065, 0.988] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer | 0.505 [0.067, 0.977] | 2/4 cells, 12/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer_sc | 0.501 [0.057, 0.944] | 3/4 cells, 14/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | frac:0.5 | rmse_h1 | lgbm | 0.512 [0.049, 0.991] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | frac:0.5 | rmse_h1 | lstm | 0.541 [0.105, 1.033] | 1/4 cells, 6/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | frac:0.5 | rmse_h1 | nlinear | 0.501 [0.022, 0.980] | 2/4 cells, 11/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | frac:0.5 | rmse_h1 | persistence | 0.524 [0.047, 1.016] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | frac:0.5 | rmse_h10 | elasticnet | 1.019 [0.422, 1.495] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer | 0.928 [0.639, 1.140] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer_sc | 0.800 [0.304, 1.184] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | frac:0.5 | rmse_h10 | lgbm | 0.644 [0.249, 0.952] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | frac:0.5 | rmse_h10 | lstm | 0.863 [0.413, 1.288] | 3/4 cells, 16/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | frac:0.5 | rmse_h10 | nlinear | 0.997 [0.595, 1.330] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | frac:0.5 | rmse_h10 | persistence | 1.354 [0.510, 1.928] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | frac:0.5 | rmse_h100 | elasticnet | 2.037 [0.881, 3.110] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer | 1.429 [0.813, 2.046] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer_sc | 1.318 [0.650, 1.947] | 4/4 cells, 17/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | frac:0.5 | rmse_h100 | lgbm | 1.215 [0.623, 1.807] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | frac:0.5 | rmse_h100 | lstm | 1.495 [0.855, 2.168] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | frac:0.5 | rmse_h100 | nlinear | 2.367 [1.192, 3.476] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | frac:0.5 | rmse_h100 | persistence | 2.842 [2.048, 3.830] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | frac:0.5 | rmse_h25 | elasticnet | 1.227 [0.720, 1.615] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer | 0.700 [0.256, 1.145] | 4/4 cells, 19/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer_sc | 0.659 [0.368, 0.951] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | frac:0.5 | rmse_h25 | lgbm | 0.746 [0.398, 1.123] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | frac:0.5 | rmse_h25 | lstm | 0.911 [0.452, 1.281] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | frac:0.5 | rmse_h25 | nlinear | 0.986 [0.244, 1.728] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | frac:0.5 | rmse_h25 | persistence | 1.599 [0.788, 2.409] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | frac:0.5 | rmse_h50 | elasticnet | 1.444 [0.627, 2.261] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer | 0.788 [0.401, 1.372] | 4/4 cells, 19/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer_sc | 0.733 [0.253, 1.213] | 4/4 cells, 19/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | frac:0.5 | rmse_h50 | lgbm | 0.506 [0.165, 0.882] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | frac:0.5 | rmse_h50 | lstm | 0.811 [0.229, 1.393] | 3/4 cells, 16/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | frac:0.5 | rmse_h50 | nlinear | 1.489 [0.913, 2.065] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | frac:0.5 | rmse_h50 | persistence | 1.521 [0.930, 2.368] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | frac:0.7 | rmse_h1 | elasticnet | 0.109 [0.049, 0.207] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer | 0.122 [0.027, 0.218] | 0/4 cells, 4/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer_sc | 0.107 [0.044, 0.178] | 1/4 cells, 7/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | frac:0.7 | rmse_h1 | lgbm | 0.102 [0.029, 0.209] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | frac:0.7 | rmse_h1 | lstm | 0.103 [0.047, 0.166] | 2/4 cells, 8/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | frac:0.7 | rmse_h1 | nlinear | 0.093 [0.030, 0.156] | 2/4 cells, 13/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | frac:0.7 | rmse_h1 | persistence | 0.092 [0.023, 0.162] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | frac:0.7 | rmse_h10 | elasticnet | 0.652 [0.302, 1.168] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer | 0.709 [0.227, 1.192] | 2/4 cells, 12/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer_sc | 0.556 [0.203, 1.194] | 3/4 cells, 16/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | frac:0.7 | rmse_h10 | lgbm | 0.346 [0.124, 0.668] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | frac:0.7 | rmse_h10 | lstm | 0.502 [0.128, 1.180] | 4/4 cells, 18/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | frac:0.7 | rmse_h10 | nlinear | 0.637 [0.229, 1.146] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | frac:0.7 | rmse_h10 | persistence | 0.717 [0.237, 1.507] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | frac:0.7 | rmse_h100 | elasticnet | 2.971 [1.277, 4.748] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer | 2.164 [0.514, 3.814] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer_sc | 1.941 [0.654, 3.367] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | frac:0.7 | rmse_h100 | lgbm | 1.891 [1.108, 2.674] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | frac:0.7 | rmse_h100 | lstm | 2.767 [0.962, 4.573] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | frac:0.7 | rmse_h100 | nlinear | 1.731 [0.509, 2.953] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | frac:0.7 | rmse_h100 | persistence | 3.080 [1.373, 4.710] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | frac:0.7 | rmse_h25 | elasticnet | 1.373 [0.653, 2.093] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer | 1.097 [0.495, 1.699] | 2/4 cells, 8/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer_sc | 1.122 [0.651, 1.594] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | frac:0.7 | rmse_h25 | lgbm | 0.581 [0.307, 0.807] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | frac:0.7 | rmse_h25 | lstm | 0.932 [0.881, 0.991] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | frac:0.7 | rmse_h25 | nlinear | 0.982 [0.801, 1.163] | 1/4 cells, 5/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | frac:0.7 | rmse_h25 | persistence | 0.714 [0.117, 1.649] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | frac:0.7 | rmse_h50 | elasticnet | 1.937 [0.860, 3.014] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer | 1.331 [1.018, 1.643] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer_sc | 1.441 [1.194, 1.752] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | frac:0.7 | rmse_h50 | lgbm | 0.842 [0.352, 1.167] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | frac:0.7 | rmse_h50 | lstm | 1.249 [0.601, 1.897] | 1/4 cells, 8/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | frac:0.7 | rmse_h50 | nlinear | 0.805 [0.346, 1.399] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | frac:0.7 | rmse_h50 | persistence | 1.046 [0.194, 1.898] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | overall | rmse_h1 | elasticnet | 0.383 [0.180, 0.585] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | overall | rmse_h1 | itransformer | 0.393 [0.187, 0.599] | 3/4 cells, 12/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | overall | rmse_h1 | itransformer_sc | 0.389 [0.175, 0.603] | 2/4 cells, 12/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | overall | rmse_h1 | lgbm | 0.376 [0.164, 0.588] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | overall | rmse_h1 | lstm | 0.406 [0.199, 0.614] | 2/4 cells, 7/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | overall | rmse_h1 | nlinear | 0.403 [0.191, 0.615] | 1/4 cells, 6/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | overall | rmse_h1 | persistence | 0.397 [0.177, 0.617] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | overall | rmse_h10 | elasticnet | 1.160 [0.821, 1.728] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | overall | rmse_h10 | itransformer | 1.071 [0.653, 1.633] | 3/4 cells, 17/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | overall | rmse_h10 | itransformer_sc | 1.060 [0.748, 1.577] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | overall | rmse_h10 | lgbm | 0.922 [0.576, 1.479] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | overall | rmse_h10 | lstm | 1.010 [0.595, 1.579] | 4/4 cells, 17/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | overall | rmse_h10 | nlinear | 1.141 [0.853, 1.667] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | overall | rmse_h10 | persistence | 1.332 [1.082, 1.703] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | overall | rmse_h100 | elasticnet | 2.574 [1.863, 3.572] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | overall | rmse_h100 | itransformer | 1.988 [1.246, 2.785] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | overall | rmse_h100 | itransformer_sc | 1.641 [1.059, 2.458] | 4/4 cells, 20/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | overall | rmse_h100 | lgbm | 1.997 [1.700, 2.367] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | overall | rmse_h100 | lstm | 2.255 [1.489, 3.022] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | overall | rmse_h100 | nlinear | 2.255 [1.506, 3.123] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | overall | rmse_h100 | persistence | 2.680 [1.781, 3.658] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | overall | rmse_h25 | elasticnet | 1.402 [0.922, 1.881] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | overall | rmse_h25 | itransformer | 1.048 [0.755, 1.517] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | overall | rmse_h25 | itransformer_sc | 1.107 [0.800, 1.470] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | overall | rmse_h25 | lgbm | 1.011 [0.731, 1.337] | 3/4 cells, 15/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | overall | rmse_h25 | lstm | 1.040 [0.866, 1.246] | 4/4 cells, 18/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | overall | rmse_h25 | nlinear | 1.225 [1.067, 1.427] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | overall | rmse_h25 | persistence | 1.317 [1.143, 1.422] |  |  | 4 | 5 | 67153a79 |
| loco | start_points | overall | rmse_h50 | elasticnet | 2.147 [1.287, 3.007] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 250b3b54 |
| loco | start_points | overall | rmse_h50 | itransformer | 1.553 [1.037, 2.154] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | d10bec5e |
| loco | start_points | overall | rmse_h50 | itransformer_sc | 1.481 [1.054, 1.988] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 724e5bbb |
| loco | start_points | overall | rmse_h50 | lgbm | 1.493 [0.985, 2.029] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | f5a75263 |
| loco | start_points | overall | rmse_h50 | lstm | 1.618 [0.992, 2.062] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | 37ba151d |
| loco | start_points | overall | rmse_h50 | nlinear | 1.641 [1.180, 2.274] | 2/4 cells, 10/20 cell-seeds (vs persistence) |  | 4 | 5 | f81cfef1 |
| loco | start_points | overall | rmse_h50 | persistence | 1.506 [1.020, 1.989] |  |  | 4 | 5 | 67153a79 |

</details>

<details><summary>calce_rul (102 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rul_bias | elasticnet | 88.101 [-7.143, 215.542] |  |  | 4 | 5 | 398ca434 |
| loco | all | overall | rul_bias | itransformer | 17.303 [-42.124, 84.274] |  |  | 4 | 5 | f70068d0 |
| loco | all | overall | rul_bias | itransformer_sc | 22.648 [-37.389, 89.517] |  |  | 4 | 5 | b71a9d43 |
| loco | all | overall | rul_bias | lgbm | 0.268 [-59.724, 78.272] |  |  | 4 | 5 | e452e0fa |
| loco | all | overall | rul_bias | lstm | 8.422 [-52.440, 84.350] |  |  | 4 | 5 | befe424d |
| loco | all | overall | rul_bias | nlinear | 16.774 [-15.966, 49.515] |  |  | 4 | 5 | b21a6eb6 |
| loco | all | overall | rul_mae | elasticnet | 170.161 [83.008, 257.314] |  |  | 4 | 5 | 398ca434 |
| loco | all | overall | rul_mae | itransformer | 69.536 [43.516, 102.239] |  |  | 4 | 5 | f70068d0 |
| loco | all | overall | rul_mae | itransformer_sc | 70.277 [43.146, 107.201] |  |  | 4 | 5 | b71a9d43 |
| loco | all | overall | rul_mae | lgbm | 76.046 [52.399, 102.766] |  |  | 4 | 5 | e452e0fa |
| loco | all | overall | rul_mae | lstm | 74.330 [48.766, 106.407] |  |  | 4 | 5 | befe424d |
| loco | all | overall | rul_mae | nlinear | 125.776 [121.998, 129.799] |  |  | 4 | 5 | b21a6eb6 |
| loco | start_points | fixed:200 | rul_bias | elasticnet | 26.683 [-111.822, 218.045] |  |  | 4 | 5 | 398ca434 |
| loco | start_points | fixed:200 | rul_bias | itransformer | -1.585 [-81.629, 101.269] |  |  | 4 | 5 | f70068d0 |
| loco | start_points | fixed:200 | rul_bias | itransformer_sc | 2.216 [-90.258, 106.720] |  |  | 4 | 5 | b71a9d43 |
| loco | start_points | fixed:200 | rul_bias | lgbm | -31.988 [-120.284, 86.561] |  |  | 4 | 5 | e452e0fa |
| loco | start_points | fixed:200 | rul_bias | lstm | -25.408 [-111.877, 84.321] |  |  | 4 | 5 | befe424d |
| loco | start_points | fixed:200 | rul_bias | nlinear | -130.190 [-180.931, -79.450] |  |  | 4 | 5 | b21a6eb6 |
| loco | start_points | fixed:200 | rul_mae | elasticnet | 138.505 [43.533, 253.606] |  |  | 4 | 5 | 398ca434 |
| loco | start_points | fixed:200 | rul_mae | itransformer | 85.696 [34.240, 141.218] |  |  | 4 | 5 | f70068d0 |
| loco | start_points | fixed:200 | rul_mae | itransformer_sc | 89.377 [35.696, 143.057] |  |  | 4 | 5 | b71a9d43 |
| loco | start_points | fixed:200 | rul_mae | lgbm | 101.642 [62.242, 141.042] |  |  | 4 | 5 | e452e0fa |
| loco | start_points | fixed:200 | rul_mae | lstm | 92.743 [48.668, 136.819] |  |  | 4 | 5 | befe424d |
| loco | start_points | fixed:200 | rul_mae | nlinear | 130.190 [79.450, 180.931] |  |  | 4 | 5 | b21a6eb6 |
| loco | start_points | fixed:400 | rul_bias | elasticnet | -13.546 [-78.394, 51.302] |  |  | 4 | 5 | 398ca434 |
| loco | start_points | fixed:400 | rul_bias | itransformer | 35.121 [-36.304, 106.546] |  |  | 4 | 5 | f70068d0 |
| loco | start_points | fixed:400 | rul_bias | itransformer_sc | 30.337 [-39.212, 99.886] |  |  | 4 | 5 | b71a9d43 |
| loco | start_points | fixed:400 | rul_bias | lgbm | 36.189 [-38.589, 110.966] |  |  | 4 | 5 | e452e0fa |
| loco | start_points | fixed:400 | rul_bias | lstm | 27.268 [-44.975, 99.510] |  |  | 4 | 5 | befe424d |
| loco | start_points | fixed:400 | rul_bias | nlinear | 90.112 [24.386, 179.016] |  |  | 4 | 5 | b21a6eb6 |
| loco | start_points | fixed:400 | rul_mae | elasticnet | 64.848 [50.808, 91.545] |  |  | 4 | 5 | 398ca434 |
| loco | start_points | fixed:400 | rul_mae | itransformer | 72.703 [35.821, 118.585] |  |  | 4 | 5 | f70068d0 |
| loco | start_points | fixed:400 | rul_mae | itransformer_sc | 70.148 [37.932, 101.263] |  |  | 4 | 5 | b71a9d43 |
| loco | start_points | fixed:400 | rul_mae | lgbm | 74.777 [38.589, 110.966] |  |  | 4 | 5 | e452e0fa |
| loco | start_points | fixed:400 | rul_mae | lstm | 72.243 [38.213, 99.510] |  |  | 4 | 5 | befe424d |
| loco | start_points | fixed:400 | rul_mae | nlinear | 90.112 [24.386, 179.016] |  |  | 4 | 5 | b21a6eb6 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | elasticnet | 0.000 [0.000, 0.000] |  |  | 4 | 5 | 398ca434 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | itransformer | 0.450 [0.000, 0.900] |  |  | 4 | 5 | f70068d0 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | itransformer_sc | 0.350 [0.000, 0.750] |  |  | 4 | 5 | b71a9d43 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | lgbm | 0.250 [0.000, 0.750] |  |  | 4 | 5 | e452e0fa |
| loco | start_points | frac:0.3 | alpha_lambda_acc | lstm | 0.050 [0.000, 0.150] |  |  | 4 | 5 | befe424d |
| loco | start_points | frac:0.3 | alpha_lambda_acc | nlinear | 0.250 [0.000, 0.750] |  |  | 4 | 5 | b21a6eb6 |
| loco | start_points | frac:0.3 | rul_bias | elasticnet | -8.362 [-191.128, 295.199] |  |  | 4 | 5 | 398ca434 |
| loco | start_points | frac:0.3 | rul_bias | itransformer | -29.819 [-101.099, 61.196] |  |  | 4 | 5 | f70068d0 |
| loco | start_points | frac:0.3 | rul_bias | itransformer_sc | -20.795 [-109.344, 67.754] |  |  | 4 | 5 | b71a9d43 |
| loco | start_points | frac:0.3 | rul_bias | lgbm | -46.178 [-107.922, 58.759] |  |  | 4 | 5 | e452e0fa |
| loco | start_points | frac:0.3 | rul_bias | lstm | -49.452 [-115.108, 53.719] |  |  | 4 | 5 | befe424d |
| loco | start_points | frac:0.3 | rul_bias | nlinear | -125.536 [-179.017, -57.462] |  |  | 4 | 5 | b21a6eb6 |
| loco | start_points | frac:0.3 | rul_mae | elasticnet | 235.748 [129.157, 386.958] |  |  | 4 | 5 | 398ca434 |
| loco | start_points | frac:0.3 | rul_mae | itransformer | 85.679 [49.528, 111.771] |  |  | 4 | 5 | f70068d0 |
| loco | start_points | frac:0.3 | rul_mae | itransformer_sc | 88.549 [45.136, 117.991] |  |  | 4 | 5 | b71a9d43 |
| loco | start_points | frac:0.3 | rul_mae | lgbm | 101.633 [88.514, 113.895] |  |  | 4 | 5 | e452e0fa |
| loco | start_points | frac:0.3 | rul_mae | lstm | 101.678 [82.707, 120.863] |  |  | 4 | 5 | befe424d |
| loco | start_points | frac:0.3 | rul_mae | nlinear | 125.536 [57.462, 179.017] |  |  | 4 | 5 | b21a6eb6 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | elasticnet | 0.000 [0.000, 0.000] |  |  | 4 | 5 | 398ca434 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | itransformer | 0.600 [0.200, 0.900] |  |  | 4 | 5 | f70068d0 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | itransformer_sc | 0.300 [0.000, 0.750] |  |  | 4 | 5 | b71a9d43 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | lgbm | 0.750 [0.250, 1.000] |  |  | 4 | 5 | e452e0fa |
| loco | start_points | frac:0.5 | alpha_lambda_acc | lstm | 0.450 [0.100, 0.800] |  |  | 4 | 5 | befe424d |
| loco | start_points | frac:0.5 | alpha_lambda_acc | nlinear | 0.250 [0.000, 0.750] |  |  | 4 | 5 | b21a6eb6 |
| loco | start_points | frac:0.5 | rul_bias | elasticnet | 44.862 [-113.118, 319.638] |  |  | 4 | 5 | 398ca434 |
| loco | start_points | frac:0.5 | rul_bias | itransformer | 34.294 [-36.326, 112.886] |  |  | 4 | 5 | f70068d0 |
| loco | start_points | frac:0.5 | rul_bias | itransformer_sc | 41.472 [-40.941, 133.870] |  |  | 4 | 5 | b71a9d43 |
| loco | start_points | frac:0.5 | rul_bias | lgbm | 24.557 [-44.122, 124.419] |  |  | 4 | 5 | e452e0fa |
| loco | start_points | frac:0.5 | rul_bias | lstm | 11.812 [-62.504, 112.988] |  |  | 4 | 5 | befe424d |
| loco | start_points | frac:0.5 | rul_bias | nlinear | -10.878 [-71.980, 50.223] |  |  | 4 | 5 | b21a6eb6 |
| loco | start_points | frac:0.5 | rul_mae | elasticnet | 181.093 [71.935, 358.226] |  |  | 4 | 5 | 398ca434 |
| loco | start_points | frac:0.5 | rul_mae | itransformer | 70.620 [30.613, 131.049] |  |  | 4 | 5 | f70068d0 |
| loco | start_points | frac:0.5 | rul_mae | itransformer_sc | 82.538 [29.117, 149.445] |  |  | 4 | 5 | b71a9d43 |
| loco | start_points | frac:0.5 | rul_mae | lgbm | 68.679 [19.877, 142.036] |  |  | 4 | 5 | e452e0fa |
| loco | start_points | frac:0.5 | rul_mae | lstm | 75.655 [28.558, 135.605] |  |  | 4 | 5 | befe424d |
| loco | start_points | frac:0.5 | rul_mae | nlinear | 61.102 [33.397, 80.181] |  |  | 4 | 5 | b21a6eb6 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | elasticnet | 0.000 [0.000, 0.000] |  |  | 4 | 5 | 398ca434 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | itransformer | 0.250 [0.000, 0.750] |  |  | 4 | 5 | f70068d0 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | itransformer_sc | 0.250 [0.000, 0.600] |  |  | 4 | 5 | b71a9d43 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | lgbm | 0.250 [0.000, 0.750] |  |  | 4 | 5 | e452e0fa |
| loco | start_points | frac:0.7 | alpha_lambda_acc | lstm | 0.250 [0.000, 0.750] |  |  | 4 | 5 | befe424d |
| loco | start_points | frac:0.7 | alpha_lambda_acc | nlinear | 0.250 [0.000, 0.750] |  |  | 4 | 5 | b21a6eb6 |
| loco | start_points | frac:0.7 | rul_bias | elasticnet | 2.428 [-74.406, 79.261] |  |  | 4 | 5 | 398ca434 |
| loco | start_points | frac:0.7 | rul_bias | itransformer | 37.303 [-43.281, 119.166] |  |  | 4 | 5 | f70068d0 |
| loco | start_points | frac:0.7 | rul_bias | itransformer_sc | 27.191 [-48.711, 107.841] |  |  | 4 | 5 | b71a9d43 |
| loco | start_points | frac:0.7 | rul_bias | lgbm | 32.725 [-47.188, 112.637] |  |  | 4 | 5 | e452e0fa |
| loco | start_points | frac:0.7 | rul_bias | lstm | 33.255 [-49.616, 119.351] |  |  | 4 | 5 | befe424d |
| loco | start_points | frac:0.7 | rul_bias | nlinear | 84.919 [24.189, 148.586] |  |  | 4 | 5 | b21a6eb6 |
| loco | start_points | frac:0.7 | rul_mae | elasticnet | 76.834 [41.970, 111.698] |  |  | 4 | 5 | 398ca434 |
| loco | start_points | frac:0.7 | rul_mae | itransformer | 83.771 [33.126, 139.030] |  |  | 4 | 5 | f70068d0 |
| loco | start_points | frac:0.7 | rul_mae | itransformer_sc | 78.462 [39.394, 125.892] |  |  | 4 | 5 | b71a9d43 |
| loco | start_points | frac:0.7 | rul_mae | lgbm | 79.913 [35.508, 133.277] |  |  | 4 | 5 | e452e0fa |
| loco | start_points | frac:0.7 | rul_mae | lstm | 82.870 [33.559, 140.547] |  |  | 4 | 5 | befe424d |
| loco | start_points | frac:0.7 | rul_mae | nlinear | 84.919 [24.189, 148.586] |  |  | 4 | 5 | b21a6eb6 |
| loco | start_points | overall | rul_bias | elasticnet | 10.413 [-113.311, 195.759] |  |  | 4 | 5 | 398ca434 |
| loco | start_points | overall | rul_bias | itransformer | 15.063 [-59.728, 98.990] |  |  | 4 | 5 | f70068d0 |
| loco | start_points | overall | rul_bias | itransformer_sc | 16.084 [-64.351, 98.181] |  |  | 4 | 5 | b71a9d43 |
| loco | start_points | overall | rul_bias | lgbm | 3.061 [-65.331, 93.419] |  |  | 4 | 5 | e452e0fa |
| loco | start_points | overall | rul_bias | lstm | -0.505 [-74.668, 89.177] |  |  | 4 | 5 | befe424d |
| loco | start_points | overall | rul_bias | nlinear | -18.315 [-49.460, 14.089] |  |  | 4 | 5 | b21a6eb6 |
| loco | start_points | overall | rul_mae | elasticnet | 139.405 [72.198, 230.263] |  |  | 4 | 5 | 398ca434 |
| loco | start_points | overall | rul_mae | itransformer | 79.694 [48.072, 122.133] |  |  | 4 | 5 | f70068d0 |
| loco | start_points | overall | rul_mae | itransformer_sc | 81.815 [45.506, 119.602] |  |  | 4 | 5 | b71a9d43 |
| loco | start_points | overall | rul_mae | lgbm | 85.329 [58.105, 123.423] |  |  | 4 | 5 | e452e0fa |
| loco | start_points | overall | rul_mae | lstm | 85.038 [52.515, 117.561] |  |  | 4 | 5 | befe424d |
| loco | start_points | overall | rul_mae | nlinear | 98.372 [61.249, 123.680] |  |  | 4 | 5 | b21a6eb6 |

</details>
