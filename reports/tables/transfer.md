# Benchmark tables: transfer

- Protocol version: 1.1
- Git SHA: 0faa8bea89, 3a823886bb
- Seeds: 5  |  unit runs: 320
- Note: n = 4 cells per NASA/CALCE dataset, so the 95 % cluster-bootstrap CI is wide by construction. Toyota rows are over test cells (test1 / test2 separately) with a cell-level bootstrap CI and a Holm-adjusted Wilcoxon p vs the best baseline. All metrics are computed per cell from the logged predictions.

## Headline (kind = overall; RMSE in %SOH, RUL MAE in cycles)

### calce_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | itransformer+ft_full | 2.147 [2.010, 2.291] |  |  | 4 | 5 | 4cf3fdeb |
| loco | all | overall | rmse_h1 | itransformer+ft_head | 2.063 [1.941, 2.186] |  |  | 4 | 5 | ac821815 |
| loco | all | overall | rmse_h1 | itransformer+scratch | 1.975 [1.860, 2.090] |  |  | 4 | 5 | 3f3d5cde |
| loco | all | overall | rmse_h1 | itransformer+zero_shot | 2.213 [2.075, 2.351] |  |  | 4 | 5 | 4c422200 |
| loco | all | overall | rmse_h10 | itransformer+ft_full | 2.374 [2.308, 2.446] |  |  | 4 | 5 | 4cf3fdeb |
| loco | all | overall | rmse_h10 | itransformer+ft_head | 2.468 [2.406, 2.530] |  |  | 4 | 5 | ac821815 |
| loco | all | overall | rmse_h10 | itransformer+scratch | 2.312 [2.226, 2.412] |  |  | 4 | 5 | 3f3d5cde |
| loco | all | overall | rmse_h10 | itransformer+zero_shot | 2.636 [2.560, 2.711] |  |  | 4 | 5 | 4c422200 |
| loco | all | overall | rmse_h50 | itransformer+ft_full | 3.467 [3.235, 3.703] |  |  | 4 | 5 | 4cf3fdeb |
| loco | all | overall | rmse_h50 | itransformer+ft_head | 4.272 [4.001, 4.508] |  |  | 4 | 5 | ac821815 |
| loco | all | overall | rmse_h50 | itransformer+scratch | 3.182 [2.901, 3.463] |  |  | 4 | 5 | 3f3d5cde |
| loco | all | overall | rmse_h50 | itransformer+zero_shot | 5.144 [4.799, 5.482] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | overall | rmse_h1 | itransformer+few_shot | 0.382 [0.165, 0.599] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | overall | rmse_h1 | itransformer+ft_full | 0.381 [0.166, 0.595] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | overall | rmse_h1 | itransformer+ft_head | 0.369 [0.154, 0.583] |  |  | 4 | 5 | ac821815 |
| loco | start_points | overall | rmse_h1 | itransformer+scratch | 0.397 [0.200, 0.594] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | overall | rmse_h1 | itransformer+zero_shot | 0.410 [0.189, 0.632] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | overall | rmse_h10 | itransformer+few_shot | 1.089 [0.712, 1.603] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | overall | rmse_h10 | itransformer+ft_full | 1.101 [0.733, 1.604] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | overall | rmse_h10 | itransformer+ft_head | 1.121 [0.728, 1.611] |  |  | 4 | 5 | ac821815 |
| loco | start_points | overall | rmse_h10 | itransformer+scratch | 1.042 [0.712, 1.544] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | overall | rmse_h10 | itransformer+zero_shot | 1.194 [0.899, 1.530] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | overall | rmse_h50 | itransformer+few_shot | 1.605 [1.120, 2.004] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | overall | rmse_h50 | itransformer+ft_full | 1.631 [1.099, 1.998] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | overall | rmse_h50 | itransformer+ft_head | 1.891 [1.235, 2.668] |  |  | 4 | 5 | ac821815 |
| loco | start_points | overall | rmse_h50 | itransformer+scratch | 1.490 [0.932, 2.088] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | overall | rmse_h50 | itransformer+zero_shot | 1.881 [1.189, 2.712] |  |  | 4 | 5 | 4c422200 |

### calce_rul

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rul_mae | itransformer+ft_full | 95.767 [67.117, 124.417] |  |  | 4 | 5 | b342171a |
| loco | all | overall | rul_mae | itransformer+scratch | 67.386 [44.187, 96.945] |  |  | 4 | 5 | 32ce8aaf |
| loco | all | overall | rul_mae | itransformer+zero_shot | 250.221 [218.587, 273.233] |  |  | 4 | 5 | 445f661c |
| loco | start_points | overall | rul_mae | itransformer+ft_full | 85.694 [49.952, 115.504] |  |  | 4 | 5 | b342171a |
| loco | start_points | overall | rul_mae | itransformer+scratch | 72.675 [45.620, 111.539] |  |  | 4 | 5 | 32ce8aaf |
| loco | start_points | overall | rul_mae | itransformer+zero_shot | 349.360 [201.082, 466.693] |  |  | 4 | 5 | 445f661c |

### nasa_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | itransformer+ft_full | 0.930 [0.681, 1.178] |  | 1.209 | 4 | 5 | b522ed83 |
| loco | all | overall | rmse_h1 | itransformer+ft_head | 0.925 [0.669, 1.181] |  | 1.211 | 4 | 5 | 1d41798d |
| loco | all | overall | rmse_h1 | itransformer+scratch | 0.915 [0.659, 1.170] |  | 1.214 | 4 | 5 | 404d5aeb |
| loco | all | overall | rmse_h1 | itransformer+zero_shot | 1.041 [0.717, 1.364] |  | 1.419 | 4 | 5 | e40d77b4 |
| loco | all | overall | rmse_h10 | itransformer+ft_full | 1.823 [1.233, 2.414] |  | 2.523 | 4 | 5 | b522ed83 |
| loco | all | overall | rmse_h10 | itransformer+ft_head | 1.815 [1.147, 2.483] |  | 2.677 | 4 | 5 | 1d41798d |
| loco | all | overall | rmse_h10 | itransformer+scratch | 1.716 [1.104, 2.329] |  | 2.481 | 4 | 5 | 404d5aeb |
| loco | all | overall | rmse_h10 | itransformer+zero_shot | 2.528 [1.652, 3.405] |  | 3.852 | 4 | 5 | e40d77b4 |
| loco | all | overall | rmse_h50 | itransformer+ft_full | 3.880 [3.565, 4.196] |  | 3.687 | 4 | 5 | b522ed83 |
| loco | all | overall | rmse_h50 | itransformer+ft_head | 7.157 [5.959, 8.361] |  | 7.657 | 4 | 5 | 1d41798d |
| loco | all | overall | rmse_h50 | itransformer+scratch | 5.412 [5.147, 5.677] |  | 5.212 | 4 | 5 | 404d5aeb |
| loco | all | overall | rmse_h50 | itransformer+zero_shot | 8.987 [7.447, 10.527] |  | 9.834 | 4 | 5 | e40d77b4 |
| loco | start_points | overall | rmse_h1 | itransformer+few_shot | 1.838 [1.138, 2.539] |  | 2.518 | 4 | 5 | 29eb14b5 |
| loco | start_points | overall | rmse_h1 | itransformer+ft_full | 1.836 [1.140, 2.532] |  | 2.504 | 4 | 5 | b522ed83 |
| loco | start_points | overall | rmse_h1 | itransformer+ft_head | 1.869 [1.141, 2.597] |  | 2.559 | 4 | 5 | 1d41798d |
| loco | start_points | overall | rmse_h1 | itransformer+scratch | 1.823 [1.087, 2.559] |  | 2.538 | 4 | 5 | 404d5aeb |
| loco | start_points | overall | rmse_h1 | itransformer+zero_shot | 1.745 [1.069, 2.421] |  | 2.295 | 4 | 5 | e40d77b4 |
| loco | start_points | overall | rmse_h10 | itransformer+few_shot | 2.107 [1.430, 2.928] |  | 3.260 | 4 | 5 | 29eb14b5 |
| loco | start_points | overall | rmse_h10 | itransformer+ft_full | 2.145 [1.462, 2.944] |  | 3.254 | 4 | 5 | b522ed83 |
| loco | start_points | overall | rmse_h10 | itransformer+ft_head | 2.072 [1.449, 2.791] |  | 3.147 | 4 | 5 | 1d41798d |
| loco | start_points | overall | rmse_h10 | itransformer+scratch | 1.788 [1.044, 2.834] |  | 3.405 | 4 | 5 | 404d5aeb |
| loco | start_points | overall | rmse_h10 | itransformer+zero_shot | 2.949 [1.904, 4.110] |  | 4.547 | 4 | 5 | e40d77b4 |
| loco | start_points | overall | rmse_h50 | itransformer+few_shot | 4.051 [2.118, 6.291] |  | 4.047 | 4 | 5 | 29eb14b5 |
| loco | start_points | overall | rmse_h50 | itransformer+ft_full | 4.153 [2.213, 6.407] |  | 4.139 | 4 | 5 | b522ed83 |
| loco | start_points | overall | rmse_h50 | itransformer+ft_head | 7.656 [6.198, 9.293] |  | 7.235 | 4 | 5 | 1d41798d |
| loco | start_points | overall | rmse_h50 | itransformer+scratch | 5.727 [4.082, 7.419] |  | 3.324 | 4 | 5 | 404d5aeb |
| loco | start_points | overall | rmse_h50 | itransformer+zero_shot | 8.102 [6.641, 9.631] |  | 8.690 | 4 | 5 | e40d77b4 |

### nasa_rul

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rul_mae | itransformer+ft_full | 16.863 [13.358, 20.188] |  | 21.507 | 4 | 5 | 857965a7 |
| loco | all | overall | rul_mae | itransformer+scratch | 16.805 [9.422, 24.188] |  | 11.188 | 4 | 5 | b7fdf394 |
| loco | all | overall | rul_mae | itransformer+zero_shot | 40.033 [31.177, 48.890] |  | 34.919 | 4 | 5 | 4e26a625 |
| loco | start_points | overall | rul_mae | itransformer+ft_full | 18.755 [14.763, 23.977] |  | 26.441 | 4 | 5 | 857965a7 |
| loco | start_points | overall | rul_mae | itransformer+scratch | 15.805 [9.268, 22.343] |  | 11.148 | 4 | 5 | b7fdf394 |
| loco | start_points | overall | rul_mae | itransformer+zero_shot | 47.303 [24.496, 68.080] |  | 41.394 | 4 | 5 | 4e26a625 |

## Mean rank (dataset x task x split x policy x headline metric)

| model | mean rank | conditions | missing |
|---|---|---|---|
| itransformer+scratch | 1.44 | 16 | 0 |
| itransformer+ft_full | 2.44 | 16 | 0 |
| itransformer+few_shot | 2.50 | 6 | 10 |
| itransformer+ft_head | 3.00 | 12 | 4 |
| itransformer+zero_shot | 3.81 | 16 | 0 |

## Full tables

<details><summary>calce_forecast (170 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | itransformer+ft_full | 2.147 [2.010, 2.291] |  |  | 4 | 5 | 4cf3fdeb |
| loco | all | overall | rmse_h1 | itransformer+ft_head | 2.063 [1.941, 2.186] |  |  | 4 | 5 | ac821815 |
| loco | all | overall | rmse_h1 | itransformer+scratch | 1.975 [1.860, 2.090] |  |  | 4 | 5 | 3f3d5cde |
| loco | all | overall | rmse_h1 | itransformer+zero_shot | 2.213 [2.075, 2.351] |  |  | 4 | 5 | 4c422200 |
| loco | all | overall | rmse_h10 | itransformer+ft_full | 2.374 [2.308, 2.446] |  |  | 4 | 5 | 4cf3fdeb |
| loco | all | overall | rmse_h10 | itransformer+ft_head | 2.468 [2.406, 2.530] |  |  | 4 | 5 | ac821815 |
| loco | all | overall | rmse_h10 | itransformer+scratch | 2.312 [2.226, 2.412] |  |  | 4 | 5 | 3f3d5cde |
| loco | all | overall | rmse_h10 | itransformer+zero_shot | 2.636 [2.560, 2.711] |  |  | 4 | 5 | 4c422200 |
| loco | all | overall | rmse_h100 | itransformer+ft_full | 4.439 [3.812, 5.067] |  |  | 4 | 5 | 4cf3fdeb |
| loco | all | overall | rmse_h100 | itransformer+ft_head | 6.518 [6.041, 6.952] |  |  | 4 | 5 | ac821815 |
| loco | all | overall | rmse_h100 | itransformer+scratch | 3.859 [3.332, 4.386] |  |  | 4 | 5 | 3f3d5cde |
| loco | all | overall | rmse_h100 | itransformer+zero_shot | 8.528 [7.857, 9.341] |  |  | 4 | 5 | 4c422200 |
| loco | all | overall | rmse_h25 | itransformer+ft_full | 2.929 [2.780, 3.063] |  |  | 4 | 5 | 4cf3fdeb |
| loco | all | overall | rmse_h25 | itransformer+ft_head | 3.214 [3.042, 3.368] |  |  | 4 | 5 | ac821815 |
| loco | all | overall | rmse_h25 | itransformer+scratch | 2.737 [2.528, 2.947] |  |  | 4 | 5 | 3f3d5cde |
| loco | all | overall | rmse_h25 | itransformer+zero_shot | 3.713 [3.421, 3.949] |  |  | 4 | 5 | 4c422200 |
| loco | all | overall | rmse_h50 | itransformer+ft_full | 3.467 [3.235, 3.703] |  |  | 4 | 5 | 4cf3fdeb |
| loco | all | overall | rmse_h50 | itransformer+ft_head | 4.272 [4.001, 4.508] |  |  | 4 | 5 | ac821815 |
| loco | all | overall | rmse_h50 | itransformer+scratch | 3.182 [2.901, 3.463] |  |  | 4 | 5 | 3f3d5cde |
| loco | all | overall | rmse_h50 | itransformer+zero_shot | 5.144 [4.799, 5.482] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | fixed:200 | rmse_h1 | itransformer+few_shot | 0.319 [0.190, 0.420] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | fixed:200 | rmse_h1 | itransformer+ft_full | 0.322 [0.193, 0.429] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | fixed:200 | rmse_h1 | itransformer+ft_head | 0.303 [0.144, 0.406] |  |  | 4 | 5 | ac821815 |
| loco | start_points | fixed:200 | rmse_h1 | itransformer+scratch | 0.312 [0.221, 0.404] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | fixed:200 | rmse_h1 | itransformer+zero_shot | 0.278 [0.133, 0.423] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | fixed:200 | rmse_h10 | itransformer+few_shot | 1.213 [0.153, 2.951] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | fixed:200 | rmse_h10 | itransformer+ft_full | 1.212 [0.151, 2.941] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | fixed:200 | rmse_h10 | itransformer+ft_head | 1.182 [0.087, 3.013] |  |  | 4 | 5 | ac821815 |
| loco | start_points | fixed:200 | rmse_h10 | itransformer+scratch | 1.133 [0.200, 2.830] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | fixed:200 | rmse_h10 | itransformer+zero_shot | 1.339 [0.494, 2.675] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | fixed:200 | rmse_h100 | itransformer+few_shot | 0.539 [0.149, 0.928] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | fixed:200 | rmse_h100 | itransformer+ft_full | 0.554 [0.159, 1.003] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | fixed:200 | rmse_h100 | itransformer+ft_head | 1.870 [1.008, 2.732] |  |  | 4 | 5 | ac821815 |
| loco | start_points | fixed:200 | rmse_h100 | itransformer+scratch | 0.734 [0.626, 0.843] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | fixed:200 | rmse_h100 | itransformer+zero_shot | 1.006 [0.461, 1.550] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | fixed:200 | rmse_h25 | itransformer+few_shot | 1.310 [0.738, 1.883] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | fixed:200 | rmse_h25 | itransformer+ft_full | 1.306 [0.730, 1.882] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | fixed:200 | rmse_h25 | itransformer+ft_head | 1.842 [1.198, 2.283] |  |  | 4 | 5 | ac821815 |
| loco | start_points | fixed:200 | rmse_h25 | itransformer+scratch | 1.331 [0.839, 1.823] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | fixed:200 | rmse_h25 | itransformer+zero_shot | 0.939 [0.505, 1.258] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | fixed:200 | rmse_h50 | itransformer+few_shot | 1.169 [0.739, 1.599] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | fixed:200 | rmse_h50 | itransformer+ft_full | 1.172 [0.702, 1.641] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | fixed:200 | rmse_h50 | itransformer+ft_head | 1.596 [0.870, 2.322] |  |  | 4 | 5 | ac821815 |
| loco | start_points | fixed:200 | rmse_h50 | itransformer+scratch | 1.017 [0.649, 1.386] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | fixed:200 | rmse_h50 | itransformer+zero_shot | 0.958 [0.318, 1.652] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | fixed:400 | rmse_h1 | itransformer+few_shot | 0.134 [0.052, 0.278] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | fixed:400 | rmse_h1 | itransformer+ft_full | 0.128 [0.054, 0.242] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | fixed:400 | rmse_h1 | itransformer+ft_head | 0.118 [0.028, 0.208] |  |  | 4 | 5 | ac821815 |
| loco | start_points | fixed:400 | rmse_h1 | itransformer+scratch | 0.166 [0.066, 0.265] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | fixed:400 | rmse_h1 | itransformer+zero_shot | 0.153 [0.030, 0.303] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | fixed:400 | rmse_h10 | itransformer+few_shot | 0.710 [0.385, 1.116] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | fixed:400 | rmse_h10 | itransformer+ft_full | 0.741 [0.373, 1.165] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | fixed:400 | rmse_h10 | itransformer+ft_head | 0.816 [0.430, 1.200] |  |  | 4 | 5 | ac821815 |
| loco | start_points | fixed:400 | rmse_h10 | itransformer+scratch | 0.716 [0.491, 0.964] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | fixed:400 | rmse_h10 | itransformer+zero_shot | 0.803 [0.307, 1.335] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | fixed:400 | rmse_h100 | itransformer+few_shot | 2.570 [1.451, 3.577] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | fixed:400 | rmse_h100 | itransformer+ft_full | 2.762 [1.715, 3.787] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | fixed:400 | rmse_h100 | itransformer+ft_head | 2.758 [1.233, 3.739] |  |  | 4 | 5 | ac821815 |
| loco | start_points | fixed:400 | rmse_h100 | itransformer+scratch | 2.436 [1.338, 3.324] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | fixed:400 | rmse_h100 | itransformer+zero_shot | 2.436 [1.418, 3.453] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | fixed:400 | rmse_h25 | itransformer+few_shot | 0.971 [0.439, 1.503] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | fixed:400 | rmse_h25 | itransformer+ft_full | 1.005 [0.493, 1.516] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | fixed:400 | rmse_h25 | itransformer+ft_head | 0.983 [0.430, 1.535] |  |  | 4 | 5 | ac821815 |
| loco | start_points | fixed:400 | rmse_h25 | itransformer+scratch | 0.972 [0.454, 1.506] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | fixed:400 | rmse_h25 | itransformer+zero_shot | 1.314 [0.924, 1.885] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | fixed:400 | rmse_h50 | itransformer+few_shot | 1.265 [0.468, 2.191] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | fixed:400 | rmse_h50 | itransformer+ft_full | 1.328 [0.480, 2.177] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | fixed:400 | rmse_h50 | itransformer+ft_head | 1.026 [0.386, 1.916] |  |  | 4 | 5 | ac821815 |
| loco | start_points | fixed:400 | rmse_h50 | itransformer+scratch | 1.062 [0.434, 1.863] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | fixed:400 | rmse_h50 | itransformer+zero_shot | 1.107 [0.416, 1.802] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer+few_shot | 0.423 [0.165, 0.845] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer+ft_full | 0.425 [0.173, 0.843] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer+ft_head | 0.441 [0.156, 0.831] |  |  | 4 | 5 | ac821815 |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer+scratch | 0.413 [0.172, 0.866] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer+zero_shot | 0.508 [0.184, 0.837] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer+few_shot | 0.660 [0.272, 1.048] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer+ft_full | 0.681 [0.307, 1.052] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer+ft_head | 0.710 [0.374, 1.046] |  |  | 4 | 5 | ac821815 |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer+scratch | 0.697 [0.349, 0.961] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer+zero_shot | 0.653 [0.234, 1.087] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer+few_shot | 1.258 [0.528, 1.939] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer+ft_full | 1.286 [0.527, 2.017] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer+ft_head | 3.214 [0.520, 6.682] |  |  | 4 | 5 | ac821815 |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer+scratch | 1.470 [0.497, 2.815] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer+zero_shot | 2.766 [0.460, 6.944] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer+few_shot | 0.711 [0.351, 1.192] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer+ft_full | 0.708 [0.353, 1.151] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer+ft_head | 0.910 [0.194, 2.109] |  |  | 4 | 5 | ac821815 |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer+scratch | 0.552 [0.184, 1.147] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer+zero_shot | 1.155 [0.530, 2.105] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer+few_shot | 2.082 [0.986, 3.769] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer+ft_full | 2.065 [0.988, 3.729] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer+ft_head | 2.683 [0.975, 5.439] |  |  | 4 | 5 | ac821815 |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer+scratch | 2.095 [0.819, 3.950] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer+zero_shot | 2.584 [1.015, 5.619] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer+few_shot | 0.508 [0.083, 0.962] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer+ft_full | 0.505 [0.076, 0.956] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer+ft_head | 0.465 [0.048, 0.917] |  |  | 4 | 5 | ac821815 |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer+scratch | 0.473 [0.045, 0.960] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer+zero_shot | 0.554 [0.146, 1.020] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer+few_shot | 0.983 [0.339, 1.427] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer+ft_full | 0.979 [0.322, 1.415] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer+ft_head | 0.988 [0.480, 1.354] |  |  | 4 | 5 | ac821815 |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer+scratch | 0.933 [0.339, 1.309] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer+zero_shot | 1.308 [0.787, 1.649] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer+few_shot | 1.911 [1.197, 2.627] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer+ft_full | 2.022 [1.040, 3.003] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer+ft_head | 0.892 [0.201, 1.584] |  |  | 4 | 5 | ac821815 |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer+scratch | 1.444 [0.663, 2.325] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer+zero_shot | 2.047 [1.053, 3.041] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer+few_shot | 1.052 [0.531, 1.573] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer+ft_full | 1.065 [0.579, 1.534] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer+ft_head | 0.975 [0.508, 1.257] |  |  | 4 | 5 | ac821815 |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer+scratch | 0.862 [0.435, 1.257] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer+zero_shot | 1.306 [0.633, 1.979] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer+few_shot | 0.961 [0.451, 1.665] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer+ft_full | 0.957 [0.340, 1.680] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer+ft_head | 0.606 [0.212, 1.210] |  |  | 4 | 5 | ac821815 |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer+scratch | 0.878 [0.422, 1.461] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer+zero_shot | 0.883 [0.106, 1.808] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer+few_shot | 0.113 [0.059, 0.183] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer+ft_full | 0.098 [0.044, 0.175] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer+ft_head | 0.101 [0.016, 0.187] |  |  | 4 | 5 | ac821815 |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer+scratch | 0.156 [0.060, 0.252] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer+zero_shot | 0.169 [0.070, 0.249] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer+few_shot | 0.546 [0.144, 1.268] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer+ft_full | 0.616 [0.237, 1.311] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer+ft_head | 0.549 [0.133, 1.336] |  |  | 4 | 5 | ac821815 |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer+scratch | 0.590 [0.199, 1.188] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer+zero_shot | 0.640 [0.101, 1.446] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer+few_shot | 2.954 [1.030, 4.879] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer+ft_full | 3.354 [1.156, 5.553] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer+ft_head | 2.695 [1.476, 3.925] |  |  | 4 | 5 | ac821815 |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer+scratch | 2.294 [1.142, 3.446] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer+zero_shot | 3.421 [2.551, 4.506] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer+few_shot | 0.905 [0.415, 1.396] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer+ft_full | 0.922 [0.331, 1.513] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer+ft_head | 1.041 [0.791, 1.438] |  |  | 4 | 5 | ac821815 |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer+scratch | 0.810 [0.373, 1.135] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer+zero_shot | 0.981 [0.232, 1.729] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer+few_shot | 1.307 [0.635, 1.980] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer+ft_full | 1.360 [0.559, 2.162] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer+ft_head | 1.423 [0.789, 1.954] |  |  | 4 | 5 | ac821815 |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer+scratch | 1.029 [0.652, 1.515] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer+zero_shot | 1.474 [0.605, 1.989] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | overall | rmse_h1 | itransformer+few_shot | 0.382 [0.165, 0.599] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | overall | rmse_h1 | itransformer+ft_full | 0.381 [0.166, 0.595] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | overall | rmse_h1 | itransformer+ft_head | 0.369 [0.154, 0.583] |  |  | 4 | 5 | ac821815 |
| loco | start_points | overall | rmse_h1 | itransformer+scratch | 0.397 [0.200, 0.594] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | overall | rmse_h1 | itransformer+zero_shot | 0.410 [0.189, 0.632] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | overall | rmse_h10 | itransformer+few_shot | 1.089 [0.712, 1.603] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | overall | rmse_h10 | itransformer+ft_full | 1.101 [0.733, 1.604] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | overall | rmse_h10 | itransformer+ft_head | 1.121 [0.728, 1.611] |  |  | 4 | 5 | ac821815 |
| loco | start_points | overall | rmse_h10 | itransformer+scratch | 1.042 [0.712, 1.544] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | overall | rmse_h10 | itransformer+zero_shot | 1.194 [0.899, 1.530] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | overall | rmse_h100 | itransformer+few_shot | 2.164 [1.303, 2.931] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | overall | rmse_h100 | itransformer+ft_full | 2.375 [1.325, 3.255] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | overall | rmse_h100 | itransformer+ft_head | 2.749 [1.365, 3.971] |  |  | 4 | 5 | ac821815 |
| loco | start_points | overall | rmse_h100 | itransformer+scratch | 1.940 [1.140, 2.530] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | overall | rmse_h100 | itransformer+zero_shot | 2.853 [1.813, 3.967] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | overall | rmse_h25 | itransformer+few_shot | 1.126 [0.946, 1.353] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | overall | rmse_h25 | itransformer+ft_full | 1.138 [0.956, 1.339] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | overall | rmse_h25 | itransformer+ft_head | 1.334 [1.131, 1.669] |  |  | 4 | 5 | ac821815 |
| loco | start_points | overall | rmse_h25 | itransformer+scratch | 1.043 [0.835, 1.355] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | overall | rmse_h25 | itransformer+zero_shot | 1.313 [1.104, 1.523] |  |  | 4 | 5 | 4c422200 |
| loco | start_points | overall | rmse_h50 | itransformer+few_shot | 1.605 [1.120, 2.004] |  |  | 4 | 5 | ffddb4e3 |
| loco | start_points | overall | rmse_h50 | itransformer+ft_full | 1.631 [1.099, 1.998] |  |  | 4 | 5 | 4cf3fdeb |
| loco | start_points | overall | rmse_h50 | itransformer+ft_head | 1.891 [1.235, 2.668] |  |  | 4 | 5 | ac821815 |
| loco | start_points | overall | rmse_h50 | itransformer+scratch | 1.490 [0.932, 2.088] |  |  | 4 | 5 | 3f3d5cde |
| loco | start_points | overall | rmse_h50 | itransformer+zero_shot | 1.881 [1.189, 2.712] |  |  | 4 | 5 | 4c422200 |

</details>

<details><summary>calce_rul (51 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rul_bias | itransformer+ft_full | 3.961 [-76.658, 80.523] |  |  | 4 | 5 | b342171a |
| loco | all | overall | rul_bias | itransformer+scratch | 16.973 [-35.514, 81.974] |  |  | 4 | 5 | 32ce8aaf |
| loco | all | overall | rul_bias | itransformer+zero_shot | 36.283 [-6.992, 74.166] |  |  | 4 | 5 | 445f661c |
| loco | all | overall | rul_mae | itransformer+ft_full | 95.767 [67.117, 124.417] |  |  | 4 | 5 | b342171a |
| loco | all | overall | rul_mae | itransformer+scratch | 67.386 [44.187, 96.945] |  |  | 4 | 5 | 32ce8aaf |
| loco | all | overall | rul_mae | itransformer+zero_shot | 250.221 [218.587, 273.233] |  |  | 4 | 5 | 445f661c |
| loco | start_points | fixed:200 | rul_bias | itransformer+ft_full | -15.592 [-117.502, 103.441] |  |  | 4 | 5 | b342171a |
| loco | start_points | fixed:200 | rul_bias | itransformer+scratch | 6.072 [-60.030, 100.819] |  |  | 4 | 5 | 32ce8aaf |
| loco | start_points | fixed:200 | rul_bias | itransformer+zero_shot | 478.078 [284.983, 671.173] |  |  | 4 | 5 | 445f661c |
| loco | start_points | fixed:200 | rul_mae | itransformer+ft_full | 90.196 [32.715, 147.677] |  |  | 4 | 5 | b342171a |
| loco | start_points | fixed:200 | rul_mae | itransformer+scratch | 75.788 [40.323, 124.805] |  |  | 4 | 5 | 32ce8aaf |
| loco | start_points | fixed:200 | rul_mae | itransformer+zero_shot | 478.078 [284.983, 671.173] |  |  | 4 | 5 | 445f661c |
| loco | start_points | fixed:400 | rul_bias | itransformer+ft_full | 50.697 [-53.490, 162.451] |  |  | 4 | 5 | b342171a |
| loco | start_points | fixed:400 | rul_bias | itransformer+scratch | 27.783 [-37.850, 94.332] |  |  | 4 | 5 | 32ce8aaf |
| loco | start_points | fixed:400 | rul_bias | itransformer+zero_shot | 204.393 [-43.158, 451.945] |  |  | 4 | 5 | 445f661c |
| loco | start_points | fixed:400 | rul_mae | itransformer+ft_full | 98.966 [32.086, 178.715] |  |  | 4 | 5 | b342171a |
| loco | start_points | fixed:400 | rul_mae | itransformer+scratch | 67.145 [27.781, 109.314] |  |  | 4 | 5 | 32ce8aaf |
| loco | start_points | fixed:400 | rul_mae | itransformer+zero_shot | 247.551 [43.158, 451.945] |  |  | 4 | 5 | 445f661c |
| loco | start_points | frac:0.3 | alpha_lambda_acc | itransformer+ft_full | 0.350 [0.000, 0.750] |  |  | 4 | 5 | b342171a |
| loco | start_points | frac:0.3 | alpha_lambda_acc | itransformer+scratch | 0.450 [0.200, 0.800] |  |  | 4 | 5 | 32ce8aaf |
| loco | start_points | frac:0.3 | alpha_lambda_acc | itransformer+zero_shot | 0.000 [0.000, 0.000] |  |  | 4 | 5 | 445f661c |
| loco | start_points | frac:0.3 | rul_bias | itransformer+ft_full | -47.921 [-130.193, 49.859] |  |  | 4 | 5 | b342171a |
| loco | start_points | frac:0.3 | rul_bias | itransformer+scratch | -13.672 [-87.175, 59.832] |  |  | 4 | 5 | 32ce8aaf |
| loco | start_points | frac:0.3 | rul_bias | itransformer+zero_shot | 152.281 [-220.951, 595.891] |  |  | 4 | 5 | 445f661c |
| loco | start_points | frac:0.3 | rul_mae | itransformer+ft_full | 94.747 [57.418, 139.237] |  |  | 4 | 5 | b342171a |
| loco | start_points | frac:0.3 | rul_mae | itransformer+scratch | 73.503 [50.194, 91.999] |  |  | 4 | 5 | 32ce8aaf |
| loco | start_points | frac:0.3 | rul_mae | itransformer+zero_shot | 373.233 [177.349, 684.565] |  |  | 4 | 5 | 445f661c |
| loco | start_points | frac:0.5 | alpha_lambda_acc | itransformer+ft_full | 0.750 [0.250, 1.000] |  |  | 4 | 5 | b342171a |
| loco | start_points | frac:0.5 | alpha_lambda_acc | itransformer+scratch | 0.550 [0.100, 1.000] |  |  | 4 | 5 | 32ce8aaf |
| loco | start_points | frac:0.5 | alpha_lambda_acc | itransformer+zero_shot | 0.000 [0.000, 0.000] |  |  | 4 | 5 | 445f661c |
| loco | start_points | frac:0.5 | rul_bias | itransformer+ft_full | 36.716 [-24.651, 132.989] |  |  | 4 | 5 | b342171a |
| loco | start_points | frac:0.5 | rul_bias | itransformer+scratch | 47.456 [-6.907, 105.530] |  |  | 4 | 5 | 32ce8aaf |
| loco | start_points | frac:0.5 | rul_bias | itransformer+zero_shot | 230.961 [-119.575, 616.453] |  |  | 4 | 5 | 445f661c |
| loco | start_points | frac:0.5 | rul_mae | itransformer+ft_full | 56.672 [6.588, 135.484] |  |  | 4 | 5 | b342171a |
| loco | start_points | frac:0.5 | rul_mae | itransformer+scratch | 66.674 [23.913, 109.434] |  |  | 4 | 5 | 32ce8aaf |
| loco | start_points | frac:0.5 | rul_mae | itransformer+zero_shot | 350.536 [119.575, 676.241] |  |  | 4 | 5 | 445f661c |
| loco | start_points | frac:0.7 | alpha_lambda_acc | itransformer+ft_full | 0.250 [0.000, 0.750] |  |  | 4 | 5 | b342171a |
| loco | start_points | frac:0.7 | alpha_lambda_acc | itransformer+scratch | 0.350 [0.100, 0.650] |  |  | 4 | 5 | 32ce8aaf |
| loco | start_points | frac:0.7 | alpha_lambda_acc | itransformer+zero_shot | 0.250 [0.000, 0.750] |  |  | 4 | 5 | 445f661c |
| loco | start_points | frac:0.7 | rul_bias | itransformer+ft_full | 45.659 [-38.425, 129.742] |  |  | 4 | 5 | b342171a |
| loco | start_points | frac:0.7 | rul_bias | itransformer+scratch | 39.722 [-41.932, 124.836] |  |  | 4 | 5 | 32ce8aaf |
| loco | start_points | frac:0.7 | rul_bias | itransformer+zero_shot | 261.557 [-35.845, 558.960] |  |  | 4 | 5 | 445f661c |
| loco | start_points | frac:0.7 | rul_mae | itransformer+ft_full | 87.887 [38.012, 129.742] |  |  | 4 | 5 | b342171a |
| loco | start_points | frac:0.7 | rul_mae | itransformer+scratch | 80.268 [40.691, 134.756] |  |  | 4 | 5 | 32ce8aaf |
| loco | start_points | frac:0.7 | rul_mae | itransformer+zero_shot | 297.403 [35.845, 558.960] |  |  | 4 | 5 | 445f661c |
| loco | start_points | overall | rul_bias | itransformer+ft_full | 13.912 [-62.110, 89.933] |  |  | 4 | 5 | b342171a |
| loco | start_points | overall | rul_bias | itransformer+scratch | 21.472 [-43.404, 93.093] |  |  | 4 | 5 | 32ce8aaf |
| loco | start_points | overall | rul_bias | itransformer+zero_shot | 265.454 [122.476, 400.333] |  |  | 4 | 5 | 445f661c |
| loco | start_points | overall | rul_mae | itransformer+ft_full | 85.694 [49.952, 115.504] |  |  | 4 | 5 | b342171a |
| loco | start_points | overall | rul_mae | itransformer+scratch | 72.675 [45.620, 111.539] |  |  | 4 | 5 | 32ce8aaf |
| loco | start_points | overall | rul_mae | itransformer+zero_shot | 349.360 [201.082, 466.693] |  |  | 4 | 5 | 445f661c |

</details>

<details><summary>nasa_forecast (170 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | itransformer+ft_full | 0.930 [0.681, 1.178] |  | 1.209 | 4 | 5 | b522ed83 |
| loco | all | overall | rmse_h1 | itransformer+ft_head | 0.925 [0.669, 1.181] |  | 1.211 | 4 | 5 | 1d41798d |
| loco | all | overall | rmse_h1 | itransformer+scratch | 0.915 [0.659, 1.170] |  | 1.214 | 4 | 5 | 404d5aeb |
| loco | all | overall | rmse_h1 | itransformer+zero_shot | 1.041 [0.717, 1.364] |  | 1.419 | 4 | 5 | e40d77b4 |
| loco | all | overall | rmse_h10 | itransformer+ft_full | 1.823 [1.233, 2.414] |  | 2.523 | 4 | 5 | b522ed83 |
| loco | all | overall | rmse_h10 | itransformer+ft_head | 1.815 [1.147, 2.483] |  | 2.677 | 4 | 5 | 1d41798d |
| loco | all | overall | rmse_h10 | itransformer+scratch | 1.716 [1.104, 2.329] |  | 2.481 | 4 | 5 | 404d5aeb |
| loco | all | overall | rmse_h10 | itransformer+zero_shot | 2.528 [1.652, 3.405] |  | 3.852 | 4 | 5 | e40d77b4 |
| loco | all | overall | rmse_h100 | itransformer+ft_full | 8.404 [6.533, 10.274] |  | 10.246 | 4 | 5 | b522ed83 |
| loco | all | overall | rmse_h100 | itransformer+ft_head | 14.197 [12.604, 15.789] |  | 15.217 | 4 | 5 | 1d41798d |
| loco | all | overall | rmse_h100 | itransformer+scratch | 14.213 [13.092, 15.781] |  | 12.873 | 4 | 5 | 404d5aeb |
| loco | all | overall | rmse_h100 | itransformer+zero_shot | 15.312 [12.973, 17.650] |  | 16.987 | 4 | 5 | e40d77b4 |
| loco | all | overall | rmse_h25 | itransformer+ft_full | 2.696 [1.928, 3.464] |  | 3.842 | 4 | 5 | b522ed83 |
| loco | all | overall | rmse_h25 | itransformer+ft_head | 3.549 [2.489, 4.609] |  | 4.789 | 4 | 5 | 1d41798d |
| loco | all | overall | rmse_h25 | itransformer+scratch | 2.620 [2.013, 3.293] |  | 3.705 | 4 | 5 | 404d5aeb |
| loco | all | overall | rmse_h25 | itransformer+zero_shot | 4.791 [3.413, 6.170] |  | 6.690 | 4 | 5 | e40d77b4 |
| loco | all | overall | rmse_h50 | itransformer+ft_full | 3.880 [3.565, 4.196] |  | 3.687 | 4 | 5 | b522ed83 |
| loco | all | overall | rmse_h50 | itransformer+ft_head | 7.157 [5.959, 8.361] |  | 7.657 | 4 | 5 | 1d41798d |
| loco | all | overall | rmse_h50 | itransformer+scratch | 5.412 [5.147, 5.677] |  | 5.212 | 4 | 5 | 404d5aeb |
| loco | all | overall | rmse_h50 | itransformer+zero_shot | 8.987 [7.447, 10.527] |  | 9.834 | 4 | 5 | e40d77b4 |
| loco | start_points | fixed:30 | rmse_h1 | itransformer+few_shot | 2.275 [0.853, 3.473] |  | 0.165 | 4 | 5 | 29eb14b5 |
| loco | start_points | fixed:30 | rmse_h1 | itransformer+ft_full | 2.277 [0.860, 3.469] |  | 0.172 | 4 | 5 | b522ed83 |
| loco | start_points | fixed:30 | rmse_h1 | itransformer+ft_head | 2.342 [0.989, 3.520] |  | 0.334 | 4 | 5 | 1d41798d |
| loco | start_points | fixed:30 | rmse_h1 | itransformer+scratch | 2.219 [0.765, 3.503] |  | 0.085 | 4 | 5 | 404d5aeb |
| loco | start_points | fixed:30 | rmse_h1 | itransformer+zero_shot | 2.083 [0.889, 3.163] |  | 0.315 | 4 | 5 | e40d77b4 |
| loco | start_points | fixed:30 | rmse_h10 | itransformer+few_shot | 1.040 [0.395, 1.737] |  | 2.063 | 4 | 5 | 29eb14b5 |
| loco | start_points | fixed:30 | rmse_h10 | itransformer+ft_full | 1.048 [0.410, 1.725] |  | 2.040 | 4 | 5 | b522ed83 |
| loco | start_points | fixed:30 | rmse_h10 | itransformer+ft_head | 1.286 [0.700, 1.891] |  | 1.454 | 4 | 5 | 1d41798d |
| loco | start_points | fixed:30 | rmse_h10 | itransformer+scratch | 1.142 [0.374, 2.274] |  | 2.886 | 4 | 5 | 404d5aeb |
| loco | start_points | fixed:30 | rmse_h10 | itransformer+zero_shot | 1.495 [0.984, 2.081] |  | 2.307 | 4 | 5 | e40d77b4 |
| loco | start_points | fixed:30 | rmse_h100 | itransformer+few_shot | 5.143 [3.628, 6.623] |  | 5.621 | 4 | 5 | 29eb14b5 |
| loco | start_points | fixed:30 | rmse_h100 | itransformer+ft_full | 5.361 [3.742, 7.008] |  | 5.831 | 4 | 5 | b522ed83 |
| loco | start_points | fixed:30 | rmse_h100 | itransformer+ft_head | 12.580 [10.277, 14.883] |  | 15.236 | 4 | 5 | 1d41798d |
| loco | start_points | fixed:30 | rmse_h100 | itransformer+scratch | 13.327 [7.381, 17.963] |  | 4.415 | 4 | 5 | 404d5aeb |
| loco | start_points | fixed:30 | rmse_h100 | itransformer+zero_shot | 13.316 [11.054, 16.215] |  | 17.826 | 4 | 5 | e40d77b4 |
| loco | start_points | fixed:30 | rmse_h25 | itransformer+few_shot | 1.349 [0.784, 1.914] |  | 1.940 | 4 | 5 | 29eb14b5 |
| loco | start_points | fixed:30 | rmse_h25 | itransformer+ft_full | 1.388 [0.846, 1.930] |  | 1.933 | 4 | 5 | b522ed83 |
| loco | start_points | fixed:30 | rmse_h25 | itransformer+ft_head | 2.550 [1.606, 3.427] |  | 1.073 | 4 | 5 | 1d41798d |
| loco | start_points | fixed:30 | rmse_h25 | itransformer+scratch | 1.991 [1.137, 2.845] |  | 2.952 | 4 | 5 | 404d5aeb |
| loco | start_points | fixed:30 | rmse_h25 | itransformer+zero_shot | 2.396 [1.146, 3.457] |  | 3.755 | 4 | 5 | e40d77b4 |
| loco | start_points | fixed:30 | rmse_h50 | itransformer+few_shot | 3.201 [0.916, 5.486] |  | 0.531 | 4 | 5 | 29eb14b5 |
| loco | start_points | fixed:30 | rmse_h50 | itransformer+ft_full | 3.248 [0.950, 5.547] |  | 0.496 | 4 | 5 | b522ed83 |
| loco | start_points | fixed:30 | rmse_h50 | itransformer+ft_head | 6.093 [2.964, 8.796] |  | 1.046 | 4 | 5 | 1d41798d |
| loco | start_points | fixed:30 | rmse_h50 | itransformer+scratch | 6.927 [4.023, 9.438] |  | 2.240 | 4 | 5 | 404d5aeb |
| loco | start_points | fixed:30 | rmse_h50 | itransformer+zero_shot | 5.338 [2.423, 8.253] |  | 4.270 | 4 | 5 | e40d77b4 |
| loco | start_points | fixed:50 | rmse_h1 | itransformer+few_shot | 0.506 [0.282, 0.730] |  | 0.713 | 4 | 5 | 29eb14b5 |
| loco | start_points | fixed:50 | rmse_h1 | itransformer+ft_full | 0.519 [0.286, 0.753] |  | 0.689 | 4 | 5 | b522ed83 |
| loco | start_points | fixed:50 | rmse_h1 | itransformer+ft_head | 0.456 [0.097, 0.814] |  | 0.947 | 4 | 5 | 1d41798d |
| loco | start_points | fixed:50 | rmse_h1 | itransformer+scratch | 0.453 [0.079, 0.827] |  | 1.071 | 4 | 5 | 404d5aeb |
| loco | start_points | fixed:50 | rmse_h1 | itransformer+zero_shot | 0.630 [0.185, 1.143] |  | 0.034 | 4 | 5 | e40d77b4 |
| loco | start_points | fixed:50 | rmse_h10 | itransformer+few_shot | 2.484 [2.027, 3.070] |  | 1.905 | 4 | 5 | 29eb14b5 |
| loco | start_points | fixed:50 | rmse_h10 | itransformer+ft_full | 2.599 [2.066, 3.321] |  | 1.911 | 4 | 5 | b522ed83 |
| loco | start_points | fixed:50 | rmse_h10 | itransformer+ft_head | 2.410 [1.903, 3.185] |  | 1.847 | 4 | 5 | 1d41798d |
| loco | start_points | fixed:50 | rmse_h10 | itransformer+scratch | 0.978 [0.480, 1.341] |  | 0.247 | 4 | 5 | 404d5aeb |
| loco | start_points | fixed:50 | rmse_h10 | itransformer+zero_shot | 3.524 [2.936, 4.033] |  | 3.716 | 4 | 5 | e40d77b4 |
| loco | start_points | fixed:50 | rmse_h100 | itransformer+few_shot | 9.179 [1.378, 18.432] |  |  | 3 | 5 | c5d1e9df |
| loco | start_points | fixed:50 | rmse_h100 | itransformer+ft_full | 8.964 [0.741, 18.012] |  |  | 3 | 5 | 1cf0a40c |
| loco | start_points | fixed:50 | rmse_h100 | itransformer+ft_head | 9.452 [3.140, 13.793] |  |  | 3 | 5 | 337e9176 |
| loco | start_points | fixed:50 | rmse_h100 | itransformer+scratch | 12.008 [8.707, 16.052] |  |  | 3 | 5 | 1865f041 |
| loco | start_points | fixed:50 | rmse_h100 | itransformer+zero_shot | 9.359 [2.938, 13.414] |  |  | 3 | 5 | f0c72627 |
| loco | start_points | fixed:50 | rmse_h25 | itransformer+few_shot | 5.015 [4.300, 5.781] |  | 4.909 | 4 | 5 | 29eb14b5 |
| loco | start_points | fixed:50 | rmse_h25 | itransformer+ft_full | 5.166 [4.477, 5.880] |  | 4.958 | 4 | 5 | b522ed83 |
| loco | start_points | fixed:50 | rmse_h25 | itransformer+ft_head | 6.745 [5.675, 7.727] |  | 6.884 | 4 | 5 | 1d41798d |
| loco | start_points | fixed:50 | rmse_h25 | itransformer+scratch | 3.223 [2.297, 4.044] |  | 1.949 | 4 | 5 | 404d5aeb |
| loco | start_points | fixed:50 | rmse_h25 | itransformer+zero_shot | 6.388 [5.030, 7.747] |  | 7.989 | 4 | 5 | e40d77b4 |
| loco | start_points | fixed:50 | rmse_h50 | itransformer+few_shot | 4.312 [1.658, 6.896] |  | 5.084 | 4 | 5 | 29eb14b5 |
| loco | start_points | fixed:50 | rmse_h50 | itransformer+ft_full | 4.363 [1.449, 7.119] |  | 5.134 | 4 | 5 | b522ed83 |
| loco | start_points | fixed:50 | rmse_h50 | itransformer+ft_head | 8.697 [6.090, 11.304] |  | 11.644 | 4 | 5 | 1d41798d |
| loco | start_points | fixed:50 | rmse_h50 | itransformer+scratch | 5.360 [3.176, 7.536] |  | 5.076 | 4 | 5 | 404d5aeb |
| loco | start_points | fixed:50 | rmse_h50 | itransformer+zero_shot | 6.744 [2.680, 10.809] |  | 10.991 | 4 | 5 | e40d77b4 |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer+few_shot | 0.191 [0.087, 0.265] |  | 0.206 | 4 | 5 | 29eb14b5 |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer+ft_full | 0.154 [0.064, 0.240] |  | 0.155 | 4 | 5 | b522ed83 |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer+ft_head | 0.110 [0.035, 0.179] |  | 0.204 | 4 | 5 | 1d41798d |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer+scratch | 0.218 [0.090, 0.404] |  | 0.165 | 4 | 5 | 404d5aeb |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer+zero_shot | 1.199 [0.589, 1.810] |  | 1.549 | 4 | 5 | e40d77b4 |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer+few_shot | 1.656 [1.074, 2.237] |  | 0.943 | 4 | 5 | 29eb14b5 |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer+ft_full | 1.607 [1.040, 2.174] |  | 0.882 | 4 | 5 | b522ed83 |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer+ft_head | 1.238 [0.666, 2.043] |  | 1.165 | 4 | 5 | 1d41798d |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer+scratch | 1.638 [0.705, 2.627] |  | 0.644 | 4 | 5 | 404d5aeb |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer+zero_shot | 2.595 [0.930, 3.559] |  | 3.180 | 4 | 5 | e40d77b4 |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer+few_shot | 7.245 [3.008, 11.481] |  | 12.353 | 4 | 5 | 29eb14b5 |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer+ft_full | 7.515 [3.208, 11.822] |  | 12.565 | 4 | 5 | b522ed83 |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer+ft_head | 10.941 [0.853, 21.028] |  | 0.456 | 4 | 5 | 1d41798d |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer+scratch | 13.397 [7.434, 19.490] |  | 5.109 | 4 | 5 | 404d5aeb |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer+zero_shot | 12.180 [1.141, 23.220] |  | 0.852 | 4 | 5 | e40d77b4 |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer+few_shot | 3.825 [1.713, 6.380] |  | 7.901 | 4 | 5 | 29eb14b5 |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer+ft_full | 3.815 [1.648, 6.391] |  | 7.908 | 4 | 5 | b522ed83 |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer+ft_head | 3.997 [3.479, 4.840] |  | 3.753 | 4 | 5 | 1d41798d |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer+scratch | 3.610 [2.121, 5.197] |  | 5.801 | 4 | 5 | 404d5aeb |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer+zero_shot | 4.528 [2.709, 6.348] |  | 2.180 | 4 | 5 | e40d77b4 |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer+few_shot | 4.873 [2.040, 7.706] |  | 6.266 | 4 | 5 | 29eb14b5 |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer+ft_full | 4.972 [2.122, 7.822] |  | 6.333 | 4 | 5 | b522ed83 |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer+ft_head | 8.432 [4.246, 12.619] |  | 2.745 | 4 | 5 | 1d41798d |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer+scratch | 6.779 [3.560, 9.998] |  | 2.085 | 4 | 5 | 404d5aeb |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer+zero_shot | 8.816 [3.693, 13.940] |  | 2.272 | 4 | 5 | e40d77b4 |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer+few_shot | 2.066 [0.271, 3.861] |  | 3.784 | 4 | 5 | 29eb14b5 |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer+ft_full | 2.065 [0.272, 3.858] |  | 3.782 | 4 | 5 | b522ed83 |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer+ft_head | 2.022 [0.261, 3.783] |  | 3.566 | 4 | 5 | 1d41798d |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer+scratch | 2.080 [0.292, 3.869] |  | 3.727 | 4 | 5 | 404d5aeb |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer+zero_shot | 2.042 [0.394, 3.691] |  | 3.757 | 4 | 5 | e40d77b4 |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer+few_shot | 2.648 [0.704, 5.163] |  | 6.479 | 4 | 5 | 29eb14b5 |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer+ft_full | 2.696 [0.776, 5.166] |  | 6.474 | 4 | 5 | b522ed83 |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer+ft_head | 2.698 [0.672, 5.240] |  | 6.267 | 4 | 5 | 1d41798d |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer+scratch | 2.232 [0.438, 5.342] |  | 6.976 | 4 | 5 | 404d5aeb |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer+zero_shot | 3.403 [1.103, 6.130] |  | 7.694 | 4 | 5 | e40d77b4 |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer+few_shot | 7.561 [4.153, 11.279] |  |  | 3 | 5 | c5d1e9df |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer+ft_full | 7.682 [3.852, 11.462] |  |  | 3 | 5 | 1cf0a40c |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer+ft_head | 10.845 [8.355, 15.231] |  |  | 3 | 5 | 337e9176 |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer+scratch | 10.727 [5.026, 14.162] |  |  | 3 | 5 | 1865f041 |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer+zero_shot | 11.709 [9.347, 15.057] |  |  | 3 | 5 | f0c72627 |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer+few_shot | 2.274 [0.668, 4.326] |  | 2.245 | 4 | 5 | 29eb14b5 |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer+ft_full | 2.377 [0.815, 4.407] |  | 2.286 | 4 | 5 | b522ed83 |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer+ft_head | 3.413 [1.937, 4.987] |  | 2.977 | 4 | 5 | 1d41798d |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer+scratch | 1.823 [0.547, 3.099] |  | 3.389 | 4 | 5 | 404d5aeb |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer+zero_shot | 3.566 [0.431, 6.700] |  | 6.737 | 4 | 5 | e40d77b4 |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer+few_shot | 3.226 [1.193, 7.002] |  | 1.085 | 4 | 5 | 29eb14b5 |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer+ft_full | 3.247 [1.277, 7.097] |  | 1.255 | 4 | 5 | b522ed83 |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer+ft_head | 5.499 [1.858, 9.255] |  | 5.035 | 4 | 5 | 1d41798d |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer+scratch | 4.187 [1.631, 6.742] |  | 2.236 | 4 | 5 | 404d5aeb |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer+zero_shot | 6.579 [1.777, 11.381] |  | 12.038 | 4 | 5 | e40d77b4 |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer+few_shot | 1.365 [0.157, 3.130] |  | 4.100 | 4 | 5 | 29eb14b5 |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer+ft_full | 1.366 [0.172, 3.102] |  | 4.065 | 4 | 5 | b522ed83 |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer+ft_head | 1.519 [0.117, 3.326] |  | 4.357 | 4 | 5 | 1d41798d |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer+scratch | 1.280 [0.156, 3.158] |  | 4.136 | 4 | 5 | 404d5aeb |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer+zero_shot | 0.867 [0.040, 2.351] |  | 3.119 | 4 | 5 | e40d77b4 |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer+few_shot | 0.872 [0.442, 1.330] |  | 1.548 | 4 | 5 | 29eb14b5 |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer+ft_full | 0.868 [0.391, 1.350] |  | 1.555 | 4 | 5 | b522ed83 |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer+ft_head | 0.998 [0.362, 1.592] |  | 1.834 | 4 | 5 | 1d41798d |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer+scratch | 0.680 [0.461, 1.030] |  | 0.582 | 4 | 5 | 404d5aeb |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer+zero_shot | 2.160 [1.110, 3.319] |  | 3.867 | 4 | 5 | e40d77b4 |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer+few_shot | 9.809 |  |  | 1 | 5 | c10e0865 |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer+ft_full | 9.925 |  |  | 1 | 5 | 247469fc |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer+ft_head | 14.329 |  |  | 1 | 5 | 41b69e4d |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer+scratch | 11.225 |  |  | 1 | 5 | b09ccff9 |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer+zero_shot | 17.387 |  |  | 1 | 5 | b1fc463d |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer+few_shot | 2.618 [1.056, 4.180] |  | 3.749 | 4 | 5 | 29eb14b5 |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer+ft_full | 2.697 [1.113, 4.282] |  | 3.842 | 4 | 5 | b522ed83 |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer+ft_head | 3.204 [0.501, 5.908] |  | 5.628 | 4 | 5 | 1d41798d |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer+scratch | 2.319 [0.879, 4.235] |  | 1.976 | 4 | 5 | 404d5aeb |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer+zero_shot | 5.411 [3.254, 7.567] |  | 7.227 | 4 | 5 | e40d77b4 |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer+few_shot | 2.597 [1.646, 3.561] |  | 3.913 | 4 | 5 | 29eb14b5 |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer+ft_full | 2.818 [2.125, 3.751] |  | 4.166 | 4 | 5 | b522ed83 |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer+ft_head | 5.766 [2.881, 8.651] |  | 9.601 | 4 | 5 | 1d41798d |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer+scratch | 2.471 [1.515, 3.442] |  | 3.786 | 4 | 5 | 404d5aeb |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer+zero_shot | 8.071 [7.477, 8.966] |  | 9.408 | 4 | 5 | e40d77b4 |
| loco | start_points | overall | rmse_h1 | itransformer+few_shot | 1.838 [1.138, 2.539] |  | 2.518 | 4 | 5 | 29eb14b5 |
| loco | start_points | overall | rmse_h1 | itransformer+ft_full | 1.836 [1.140, 2.532] |  | 2.504 | 4 | 5 | b522ed83 |
| loco | start_points | overall | rmse_h1 | itransformer+ft_head | 1.869 [1.141, 2.597] |  | 2.559 | 4 | 5 | 1d41798d |
| loco | start_points | overall | rmse_h1 | itransformer+scratch | 1.823 [1.087, 2.559] |  | 2.538 | 4 | 5 | 404d5aeb |
| loco | start_points | overall | rmse_h1 | itransformer+zero_shot | 1.745 [1.069, 2.421] |  | 2.295 | 4 | 5 | e40d77b4 |
| loco | start_points | overall | rmse_h10 | itransformer+few_shot | 2.107 [1.430, 2.928] |  | 3.260 | 4 | 5 | 29eb14b5 |
| loco | start_points | overall | rmse_h10 | itransformer+ft_full | 2.145 [1.462, 2.944] |  | 3.254 | 4 | 5 | b522ed83 |
| loco | start_points | overall | rmse_h10 | itransformer+ft_head | 2.072 [1.449, 2.791] |  | 3.147 | 4 | 5 | 1d41798d |
| loco | start_points | overall | rmse_h10 | itransformer+scratch | 1.788 [1.044, 2.834] |  | 3.405 | 4 | 5 | 404d5aeb |
| loco | start_points | overall | rmse_h10 | itransformer+zero_shot | 2.949 [1.904, 4.110] |  | 4.547 | 4 | 5 | e40d77b4 |
| loco | start_points | overall | rmse_h100 | itransformer+few_shot | 8.080 [4.879, 10.077] |  | 9.596 | 4 | 5 | 29eb14b5 |
| loco | start_points | overall | rmse_h100 | itransformer+ft_full | 8.194 [4.878, 10.170] |  | 9.795 | 4 | 5 | b522ed83 |
| loco | start_points | overall | rmse_h100 | itransformer+ft_head | 12.075 [8.759, 15.580] |  | 10.778 | 4 | 5 | 1d41798d |
| loco | start_points | overall | rmse_h100 | itransformer+scratch | 11.803 [6.708, 16.583] |  | 4.776 | 4 | 5 | 404d5aeb |
| loco | start_points | overall | rmse_h100 | itransformer+zero_shot | 13.123 [9.515, 16.165] |  | 12.619 | 4 | 5 | e40d77b4 |
| loco | start_points | overall | rmse_h25 | itransformer+few_shot | 3.546 [2.684, 4.408] |  | 4.677 | 4 | 5 | 29eb14b5 |
| loco | start_points | overall | rmse_h25 | itransformer+ft_full | 3.623 [2.764, 4.458] |  | 4.708 | 4 | 5 | b522ed83 |
| loco | start_points | overall | rmse_h25 | itransformer+ft_head | 4.454 [3.600, 5.133] |  | 4.542 | 4 | 5 | 1d41798d |
| loco | start_points | overall | rmse_h25 | itransformer+scratch | 2.979 [2.668, 3.369] |  | 3.529 | 4 | 5 | 404d5aeb |
| loco | start_points | overall | rmse_h25 | itransformer+zero_shot | 5.003 [3.844, 5.800] |  | 6.005 | 4 | 5 | e40d77b4 |
| loco | start_points | overall | rmse_h50 | itransformer+few_shot | 4.051 [2.118, 6.291] |  | 4.047 | 4 | 5 | 29eb14b5 |
| loco | start_points | overall | rmse_h50 | itransformer+ft_full | 4.153 [2.213, 6.407] |  | 4.139 | 4 | 5 | b522ed83 |
| loco | start_points | overall | rmse_h50 | itransformer+ft_head | 7.656 [6.198, 9.293] |  | 7.235 | 4 | 5 | 1d41798d |
| loco | start_points | overall | rmse_h50 | itransformer+scratch | 5.727 [4.082, 7.419] |  | 3.324 | 4 | 5 | 404d5aeb |
| loco | start_points | overall | rmse_h50 | itransformer+zero_shot | 8.102 [6.641, 9.631] |  | 8.690 | 4 | 5 | e40d77b4 |

</details>

<details><summary>nasa_rul (51 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rul_bias | itransformer+ft_full | 2.868 [-7.045, 13.499] |  | -2.610 | 4 | 5 | 857965a7 |
| loco | all | overall | rul_bias | itransformer+scratch | -0.268 [-16.306, 16.170] |  | -4.212 | 4 | 5 | b7fdf394 |
| loco | all | overall | rul_bias | itransformer+zero_shot | 7.513 [-3.617, 18.642] |  | -7.268 | 4 | 5 | 4e26a625 |
| loco | all | overall | rul_mae | itransformer+ft_full | 16.863 [13.358, 20.188] |  | 21.507 | 4 | 5 | 857965a7 |
| loco | all | overall | rul_mae | itransformer+scratch | 16.805 [9.422, 24.188] |  | 11.188 | 4 | 5 | b7fdf394 |
| loco | all | overall | rul_mae | itransformer+zero_shot | 40.033 [31.177, 48.890] |  | 34.919 | 4 | 5 | 4e26a625 |
| loco | start_points | fixed:30 | rul_bias | itransformer+ft_full | -9.711 [-28.501, 7.549] |  | -40.123 | 4 | 5 | 857965a7 |
| loco | start_points | fixed:30 | rul_bias | itransformer+scratch | -4.925 [-25.158, 13.993] |  | -6.999 | 4 | 5 | b7fdf394 |
| loco | start_points | fixed:30 | rul_bias | itransformer+zero_shot | 39.552 [-19.282, 98.385] |  | -48.000 | 4 | 5 | 4e26a625 |
| loco | start_points | fixed:30 | rul_mae | itransformer+ft_full | 17.261 [7.549, 32.275] |  | 40.123 | 4 | 5 | 857965a7 |
| loco | start_points | fixed:30 | rul_mae | itransformer+scratch | 16.006 [4.782, 27.230] |  | 6.999 | 4 | 5 | b7fdf394 |
| loco | start_points | fixed:30 | rul_mae | itransformer+zero_shot | 63.552 [28.718, 98.385] |  | 48.000 | 4 | 5 | 4e26a625 |
| loco | start_points | fixed:50 | rul_bias | itransformer+ft_full | 2.816 [-16.257, 13.617] |  | 14.765 | 4 | 5 | 857965a7 |
| loco | start_points | fixed:50 | rul_bias | itransformer+scratch | -1.446 [-15.989, 13.096] |  | -12.978 | 4 | 5 | b7fdf394 |
| loco | start_points | fixed:50 | rul_bias | itransformer+zero_shot | -11.939 [-51.236, 28.570] |  | 43.193 | 4 | 5 | 4e26a625 |
| loco | start_points | fixed:50 | rul_mae | itransformer+ft_full | 15.733 [11.089, 22.492] |  | 14.765 | 4 | 5 | 857965a7 |
| loco | start_points | fixed:50 | rul_mae | itransformer+scratch | 14.543 [12.488, 17.495] |  | 12.978 | 4 | 5 | b7fdf394 |
| loco | start_points | fixed:50 | rul_mae | itransformer+zero_shot | 33.535 [13.149, 53.921] |  | 43.193 | 4 | 5 | 4e26a625 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | itransformer+ft_full | 0.250 [0.000, 0.750] |  | 0.000 | 4 | 5 | 857965a7 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | itransformer+scratch | 0.400 [0.000, 0.800] |  | 0.600 | 4 | 5 | b7fdf394 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | itransformer+zero_shot | 0.000 [0.000, 0.000] |  | 0.000 | 4 | 5 | 4e26a625 |
| loco | start_points | frac:0.3 | rul_bias | itransformer+ft_full | 6.447 [-22.373, 38.334] |  | -30.624 | 4 | 5 | 857965a7 |
| loco | start_points | frac:0.3 | rul_bias | itransformer+scratch | -3.515 [-20.518, 13.778] |  | -9.515 | 4 | 5 | b7fdf394 |
| loco | start_points | frac:0.3 | rul_bias | itransformer+zero_shot | 41.987 [-37.490, 141.074] |  | -55.000 | 4 | 5 | 4e26a625 |
| loco | start_points | frac:0.3 | rul_mae | itransformer+ft_full | 28.819 [14.417, 45.543] |  | 30.624 | 4 | 5 | 857965a7 |
| loco | start_points | frac:0.3 | rul_mae | itransformer+scratch | 15.857 [6.946, 24.767] |  | 9.515 | 4 | 5 | b7fdf394 |
| loco | start_points | frac:0.3 | rul_mae | itransformer+zero_shot | 79.477 [28.736, 158.112] |  | 55.000 | 4 | 5 | 4e26a625 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | itransformer+ft_full | 0.250 [0.000, 0.750] |  | 0.000 | 4 | 5 | 857965a7 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | itransformer+scratch | 0.100 [0.000, 0.300] |  | 0.000 | 4 | 5 | b7fdf394 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | itransformer+zero_shot | 0.000 [0.000, 0.000] |  | 0.000 | 4 | 5 | 4e26a625 |
| loco | start_points | frac:0.5 | rul_bias | itransformer+ft_full | -8.011 [-20.820, 4.798] |  | -24.828 | 4 | 5 | 857965a7 |
| loco | start_points | frac:0.5 | rul_bias | itransformer+scratch | -1.390 [-20.100, 17.320] |  | -15.145 | 4 | 5 | b7fdf394 |
| loco | start_points | frac:0.5 | rul_bias | itransformer+zero_shot | -28.037 [-41.398, -3.019] |  | -39.000 | 4 | 5 | 4e26a625 |
| loco | start_points | frac:0.5 | rul_mae | itransformer+ft_full | 12.920 [5.021, 20.820] |  | 24.828 | 4 | 5 | 857965a7 |
| loco | start_points | frac:0.5 | rul_mae | itransformer+scratch | 18.710 [14.397, 23.023] |  | 15.145 | 4 | 5 | b7fdf394 |
| loco | start_points | frac:0.5 | rul_mae | itransformer+zero_shot | 32.756 [17.174, 41.398] |  | 39.000 | 4 | 5 | 4e26a625 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | itransformer+ft_full | 0.100 [0.000, 0.300] |  | 0.000 | 4 | 5 | 857965a7 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | itransformer+scratch | 0.200 [0.000, 0.600] |  | 0.000 | 4 | 5 | b7fdf394 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | itransformer+zero_shot | 0.000 [0.000, 0.000] |  | 0.000 | 4 | 5 | 4e26a625 |
| loco | start_points | frac:0.7 | rul_bias | itransformer+ft_full | 8.176 [-10.834, 23.733] |  | 21.865 | 4 | 5 | 857965a7 |
| loco | start_points | frac:0.7 | rul_bias | itransformer+scratch | -3.712 [-17.594, 10.170] |  | -11.101 | 4 | 5 | b7fdf394 |
| loco | start_points | frac:0.7 | rul_bias | itransformer+zero_shot | -16.306 [-34.500, 8.332] |  | 21.776 | 4 | 5 | 4e26a625 |
| loco | start_points | frac:0.7 | rul_mae | itransformer+ft_full | 19.043 [10.696, 24.634] |  | 21.865 | 4 | 5 | 857965a7 |
| loco | start_points | frac:0.7 | rul_mae | itransformer+scratch | 13.911 [7.288, 20.840] |  | 11.101 | 4 | 5 | b7fdf394 |
| loco | start_points | frac:0.7 | rul_mae | itransformer+zero_shot | 27.194 [19.888, 34.500] |  | 21.776 | 4 | 5 | 4e26a625 |
| loco | start_points | overall | rul_bias | itransformer+ft_full | -0.057 [-15.127, 15.013] |  | -11.789 | 4 | 5 | 857965a7 |
| loco | start_points | overall | rul_bias | itransformer+scratch | -2.998 [-18.534, 12.539] |  | -11.148 | 4 | 5 | b7fdf394 |
| loco | start_points | overall | rul_bias | itransformer+zero_shot | 5.051 [-11.621, 29.920] |  | -15.406 | 4 | 5 | 4e26a625 |
| loco | start_points | overall | rul_mae | itransformer+ft_full | 18.755 [14.763, 23.977] |  | 26.441 | 4 | 5 | 857965a7 |
| loco | start_points | overall | rul_mae | itransformer+scratch | 15.805 [9.268, 22.343] |  | 11.148 | 4 | 5 | b7fdf394 |
| loco | start_points | overall | rul_mae | itransformer+zero_shot | 47.303 [24.496, 68.080] |  | 41.394 | 4 | 5 | 4e26a625 |

</details>
