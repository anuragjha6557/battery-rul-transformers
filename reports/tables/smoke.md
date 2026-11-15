# Benchmark tables: smoke

- Protocol version: 1.1
- Git SHA: b10bf00929
- Seeds: 1  |  unit runs: 18
- Note: n = 4 cells per NASA/CALCE dataset, so the 95 % cluster-bootstrap CI is wide by construction. Toyota rows are per official test split (mean over seeds, no CI).

## Headline (forecast RMSE, %SOH, kind = overall)

### calce_forecast

| split | policy | kind | metric | model | mean [95% CI] | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | last_slope | 2.686 [2.506, 2.869] |  | 4 | 1 | 2751ee9f |
| loco | all | overall | rmse_h1 | persistence | 2.606 [2.429, 2.783] |  | 4 | 1 | c77e8f0d |
| loco | all | overall | rmse_h10 | last_slope | 4.266 [4.097, 4.435] |  | 4 | 1 | 2751ee9f |
| loco | all | overall | rmse_h10 | persistence | 3.071 [3.003, 3.139] |  | 4 | 1 | c77e8f0d |
| loco | all | overall | rmse_h50 | last_slope | 13.491 [12.984, 13.882] |  | 4 | 1 | 2751ee9f |
| loco | all | overall | rmse_h50 | persistence | 6.278 [5.955, 6.519] |  | 4 | 1 | c77e8f0d |
| loco | start_points | overall | rmse_h1 | last_slope | 0.455 [0.240, 0.669] |  | 4 | 1 | 2751ee9f |
| loco | start_points | overall | rmse_h1 | persistence | 0.397 [0.177, 0.617] |  | 4 | 1 | c77e8f0d |
| loco | start_points | overall | rmse_h10 | last_slope | 2.474 [2.053, 3.110] |  | 4 | 1 | 2751ee9f |
| loco | start_points | overall | rmse_h10 | persistence | 1.332 [1.082, 1.703] |  | 4 | 1 | c77e8f0d |
| loco | start_points | overall | rmse_h50 | last_slope | 7.343 [6.361, 8.324] |  | 4 | 1 | 2751ee9f |
| loco | start_points | overall | rmse_h50 | persistence | 1.506 [1.020, 1.989] |  | 4 | 1 | c77e8f0d |

### nasa_forecast

| split | policy | kind | metric | model | mean [95% CI] | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | last_slope | 0.992 [0.715, 1.269] | 1.301 | 4 | 1 | ade93415 |
| loco | all | overall | rmse_h1 | persistence | 0.955 [0.697, 1.213] | 1.245 | 4 | 1 | 1c7e63ef |
| loco | all | overall | rmse_h10 | last_slope | 2.986 [2.037, 3.934] | 3.895 | 4 | 1 | ade93415 |
| loco | all | overall | rmse_h10 | persistence | 2.737 [2.186, 3.288] | 3.153 | 4 | 1 | 1c7e63ef |
| loco | all | overall | rmse_h50 | last_slope | 12.164 [8.884, 15.444] | 14.476 | 4 | 1 | ade93415 |
| loco | all | overall | rmse_h50 | persistence | 11.211 [9.697, 12.759] | 11.258 | 4 | 1 | 1c7e63ef |
| loco | start_points | overall | rmse_h1 | last_slope | 1.909 [1.139, 2.679] | 2.642 | 4 | 1 | ade93415 |
| loco | start_points | overall | rmse_h1 | persistence | 1.654 [1.057, 2.251] | 2.261 | 4 | 1 | 1c7e63ef |
| loco | start_points | overall | rmse_h10 | last_slope | 3.935 [2.490, 5.381] | 5.540 | 4 | 1 | ade93415 |
| loco | start_points | overall | rmse_h10 | persistence | 3.348 [2.574, 4.229] | 3.206 | 4 | 1 | 1c7e63ef |
| loco | start_points | overall | rmse_h50 | last_slope | 14.573 [9.092, 19.775] | 21.338 | 4 | 1 | ade93415 |
| loco | start_points | overall | rmse_h50 | persistence | 13.452 [11.482, 15.613] | 12.879 | 4 | 1 | 1c7e63ef |

### toyota_forecast

| split | policy | kind | metric | model | mean [95% CI] | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rmse_h1 | last_slope | 0.247 |  | 1 | 1 | 77403933 |
| test1 | all | overall | rmse_h1 | persistence | 0.244 |  | 1 | 1 | 85a8557f |
| test1 | all | overall | rmse_h10 | last_slope | 0.412 |  | 1 | 1 | 77403933 |
| test1 | all | overall | rmse_h10 | persistence | 0.566 |  | 1 | 1 | 85a8557f |
| test1 | all | overall | rmse_h50 | last_slope | 1.477 |  | 1 | 1 | 77403933 |
| test1 | all | overall | rmse_h50 | persistence | 2.254 |  | 1 | 1 | 85a8557f |
| test1 | start_points | overall | rmse_h1 | last_slope | 0.086 |  | 1 | 1 | 77403933 |
| test1 | start_points | overall | rmse_h1 | persistence | 0.066 |  | 1 | 1 | 85a8557f |
| test1 | start_points | overall | rmse_h10 | last_slope | 0.601 |  | 1 | 1 | 77403933 |
| test1 | start_points | overall | rmse_h10 | persistence | 0.317 |  | 1 | 1 | 85a8557f |
| test1 | start_points | overall | rmse_h50 | last_slope | 2.840 |  | 1 | 1 | 77403933 |
| test1 | start_points | overall | rmse_h50 | persistence | 1.630 |  | 1 | 1 | 85a8557f |
| test2 | all | overall | rmse_h1 | last_slope | 0.020 |  | 1 | 1 | 77403933 |
| test2 | all | overall | rmse_h1 | persistence | 0.036 |  | 1 | 1 | 85a8557f |
| test2 | all | overall | rmse_h10 | last_slope | 0.058 |  | 1 | 1 | 77403933 |
| test2 | all | overall | rmse_h10 | persistence | 0.295 |  | 1 | 1 | 85a8557f |
| test2 | all | overall | rmse_h50 | last_slope | 0.391 |  | 1 | 1 | 77403933 |
| test2 | all | overall | rmse_h50 | persistence | 1.314 |  | 1 | 1 | 85a8557f |
| test2 | start_points | overall | rmse_h1 | last_slope | 0.027 |  | 1 | 1 | 77403933 |
| test2 | start_points | overall | rmse_h1 | persistence | 0.028 |  | 1 | 1 | 85a8557f |
| test2 | start_points | overall | rmse_h10 | last_slope | 0.039 |  | 1 | 1 | 77403933 |
| test2 | start_points | overall | rmse_h10 | persistence | 0.100 |  | 1 | 1 | 85a8557f |
| test2 | start_points | overall | rmse_h50 | last_slope | 0.148 |  | 1 | 1 | 77403933 |
| test2 | start_points | overall | rmse_h50 | persistence | 0.524 |  | 1 | 1 | 85a8557f |

## Full tables

<details><summary>calce_forecast (210 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | mae_h1 | last_slope | 0.976 [0.921, 1.035] |  | 4 | 1 | 2751ee9f |
| loco | all | overall | mae_h1 | persistence | 0.913 [0.859, 0.975] |  | 4 | 1 | c77e8f0d |
| loco | all | overall | mae_h10 | last_slope | 2.614 [2.494, 2.718] |  | 4 | 1 | 2751ee9f |
| loco | all | overall | mae_h10 | persistence | 1.767 [1.704, 1.845] |  | 4 | 1 | c77e8f0d |
| loco | all | overall | mae_h100 | last_slope | 16.634 [16.039, 17.140] |  | 4 | 1 | 2751ee9f |
| loco | all | overall | mae_h100 | persistence | 7.588 [6.946, 8.340] |  | 4 | 1 | c77e8f0d |
| loco | all | overall | mae_h25 | last_slope | 5.067 [4.859, 5.203] |  | 4 | 1 | 2751ee9f |
| loco | all | overall | mae_h25 | persistence | 2.763 [2.634, 2.892] |  | 4 | 1 | c77e8f0d |
| loco | all | overall | mae_h50 | last_slope | 8.837 [8.529, 9.086] |  | 4 | 1 | 2751ee9f |
| loco | all | overall | mae_h50 | persistence | 4.401 [4.086, 4.672] |  | 4 | 1 | c77e8f0d |
| loco | all | overall | rmse_h1 | last_slope | 2.686 [2.506, 2.869] |  | 4 | 1 | 2751ee9f |
| loco | all | overall | rmse_h1 | persistence | 2.606 [2.429, 2.783] |  | 4 | 1 | c77e8f0d |
| loco | all | overall | rmse_h10 | last_slope | 4.266 [4.097, 4.435] |  | 4 | 1 | 2751ee9f |
| loco | all | overall | rmse_h10 | persistence | 3.071 [3.003, 3.139] |  | 4 | 1 | c77e8f0d |
| loco | all | overall | rmse_h100 | last_slope | 25.209 [24.266, 26.151] |  | 4 | 1 | 2751ee9f |
| loco | all | overall | rmse_h100 | persistence | 10.293 [9.591, 10.966] |  | 4 | 1 | c77e8f0d |
| loco | all | overall | rmse_h25 | last_slope | 7.632 [7.376, 7.792] |  | 4 | 1 | 2751ee9f |
| loco | all | overall | rmse_h25 | persistence | 4.180 [4.046, 4.314] |  | 4 | 1 | c77e8f0d |
| loco | all | overall | rmse_h50 | last_slope | 13.491 [12.984, 13.882] |  | 4 | 1 | 2751ee9f |
| loco | all | overall | rmse_h50 | persistence | 6.278 [5.955, 6.519] |  | 4 | 1 | c77e8f0d |
| loco | all | overall | rmse_smooth_h1 | last_slope | 1.967 [1.851, 2.084] |  | 4 | 1 | 2751ee9f |
| loco | all | overall | rmse_smooth_h1 | persistence | 1.852 [1.738, 1.966] |  | 4 | 1 | c77e8f0d |
| loco | all | overall | rmse_smooth_h10 | last_slope | 3.865 [3.693, 4.037] |  | 4 | 1 | 2751ee9f |
| loco | all | overall | rmse_smooth_h10 | persistence | 2.407 [2.342, 2.470] |  | 4 | 1 | c77e8f0d |
| loco | all | overall | rmse_smooth_h100 | last_slope | 25.094 [24.171, 26.016] |  | 4 | 1 | 2751ee9f |
| loco | all | overall | rmse_smooth_h100 | persistence | 9.949 [9.253, 10.647] |  | 4 | 1 | c77e8f0d |
| loco | all | overall | rmse_smooth_h25 | last_slope | 7.394 [7.138, 7.535] |  | 4 | 1 | 2751ee9f |
| loco | all | overall | rmse_smooth_h25 | persistence | 3.612 [3.459, 3.746] |  | 4 | 1 | c77e8f0d |
| loco | all | overall | rmse_smooth_h50 | last_slope | 13.375 [12.842, 13.745] |  | 4 | 1 | 2751ee9f |
| loco | all | overall | rmse_smooth_h50 | persistence | 5.834 [5.421, 6.137] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:200 | mae_h1 | last_slope | 0.422 [0.201, 0.609] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:200 | mae_h1 | persistence | 0.347 [0.209, 0.485] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:200 | mae_h10 | last_slope | 2.318 [0.806, 4.329] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:200 | mae_h10 | persistence | 1.344 [0.340, 2.774] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:200 | mae_h100 | last_slope | 10.695 [6.175, 15.216] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:200 | mae_h100 | persistence | 1.897 [1.120, 2.489] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:200 | mae_h25 | last_slope | 2.579 [0.690, 4.821] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:200 | mae_h25 | persistence | 0.840 [0.239, 1.441] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:200 | mae_h50 | last_slope | 4.995 [1.687, 8.303] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:200 | mae_h50 | persistence | 0.844 [0.319, 1.572] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:200 | rmse_h1 | last_slope | 0.422 [0.201, 0.609] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:200 | rmse_h1 | persistence | 0.347 [0.209, 0.485] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:200 | rmse_h10 | last_slope | 2.318 [0.806, 4.329] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:200 | rmse_h10 | persistence | 1.344 [0.340, 2.774] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:200 | rmse_h100 | last_slope | 10.695 [6.175, 15.216] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:200 | rmse_h100 | persistence | 1.897 [1.120, 2.489] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:200 | rmse_h25 | last_slope | 2.579 [0.690, 4.821] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:200 | rmse_h25 | persistence | 0.840 [0.239, 1.441] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:200 | rmse_h50 | last_slope | 4.995 [1.687, 8.303] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:200 | rmse_h50 | persistence | 0.844 [0.319, 1.572] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:200 | rmse_smooth_h1 | last_slope | 0.326 [0.152, 0.544] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:200 | rmse_smooth_h1 | persistence | 0.250 [0.072, 0.457] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:200 | rmse_smooth_h10 | last_slope | 2.307 [0.806, 4.334] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:200 | rmse_smooth_h10 | persistence | 1.332 [0.330, 2.779] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:200 | rmse_smooth_h100 | last_slope | 10.528 [6.005, 15.052] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:200 | rmse_smooth_h100 | persistence | 1.894 [1.093, 2.487] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:200 | rmse_smooth_h25 | last_slope | 2.594 [0.683, 4.878] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:200 | rmse_smooth_h25 | persistence | 0.848 [0.232, 1.464] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:200 | rmse_smooth_h50 | last_slope | 4.931 [2.014, 7.848] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:200 | rmse_smooth_h50 | persistence | 0.619 [0.228, 1.139] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:400 | mae_h1 | last_slope | 0.081 [0.034, 0.158] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:400 | mae_h1 | persistence | 0.080 [0.019, 0.194] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:400 | mae_h10 | last_slope | 1.629 [1.035, 2.223] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:400 | mae_h10 | persistence | 1.009 [0.324, 1.694] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:400 | mae_h100 | last_slope | 6.898 [1.827, 11.957] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:400 | mae_h100 | persistence | 3.346 [1.619, 5.072] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:400 | mae_h25 | last_slope | 2.439 [1.474, 3.403] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:400 | mae_h25 | persistence | 1.333 [0.586, 2.081] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:400 | mae_h50 | last_slope | 3.432 [1.337, 4.769] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:400 | mae_h50 | persistence | 1.656 [0.742, 2.680] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:400 | rmse_h1 | last_slope | 0.081 [0.034, 0.158] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:400 | rmse_h1 | persistence | 0.080 [0.019, 0.194] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:400 | rmse_h10 | last_slope | 1.629 [1.035, 2.223] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:400 | rmse_h10 | persistence | 1.009 [0.324, 1.694] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:400 | rmse_h100 | last_slope | 6.898 [1.827, 11.957] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:400 | rmse_h100 | persistence | 3.346 [1.619, 5.072] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:400 | rmse_h25 | last_slope | 2.439 [1.474, 3.403] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:400 | rmse_h25 | persistence | 1.333 [0.586, 2.081] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:400 | rmse_h50 | last_slope | 3.432 [1.337, 4.769] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:400 | rmse_h50 | persistence | 1.656 [0.742, 2.680] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:400 | rmse_smooth_h1 | last_slope | 0.104 [0.034, 0.225] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:400 | rmse_smooth_h1 | persistence | 0.076 [0.019, 0.181] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:400 | rmse_smooth_h10 | last_slope | 1.514 [0.866, 2.162] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:400 | rmse_smooth_h10 | persistence | 0.894 [0.155, 1.633] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:400 | rmse_smooth_h100 | last_slope | 6.952 [1.827, 12.011] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:400 | rmse_smooth_h100 | persistence | 3.400 [1.728, 5.072] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:400 | rmse_smooth_h25 | last_slope | 2.422 [1.474, 3.369] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:400 | rmse_smooth_h25 | persistence | 1.316 [0.586, 2.047] |  | 4 | 1 | c77e8f0d |
| loco | start_points | fixed:400 | rmse_smooth_h50 | last_slope | 3.430 [1.334, 4.769] |  | 4 | 1 | 2751ee9f |
| loco | start_points | fixed:400 | rmse_smooth_h50 | persistence | 1.654 [0.742, 2.677] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.3 | mae_h1 | last_slope | 0.474 [0.215, 0.961] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.3 | mae_h1 | persistence | 0.373 [0.089, 0.866] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.3 | mae_h10 | last_slope | 3.126 [1.808, 4.454] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.3 | mae_h10 | persistence | 0.952 [0.590, 1.315] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.3 | mae_h100 | last_slope | 22.123 [7.983, 36.262] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.3 | mae_h100 | persistence | 0.918 [0.565, 1.150] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.3 | mae_h25 | last_slope | 5.620 [1.950, 9.290] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.3 | mae_h25 | persistence | 0.865 [0.571, 1.180] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.3 | mae_h50 | last_slope | 10.522 [4.959, 16.085] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.3 | mae_h50 | persistence | 1.300 [0.353, 2.350] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.3 | rmse_h1 | last_slope | 0.474 [0.215, 0.961] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.3 | rmse_h1 | persistence | 0.373 [0.089, 0.866] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.3 | rmse_h10 | last_slope | 3.126 [1.808, 4.454] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.3 | rmse_h10 | persistence | 0.952 [0.590, 1.315] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.3 | rmse_h100 | last_slope | 22.123 [7.983, 36.262] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.3 | rmse_h100 | persistence | 0.918 [0.565, 1.150] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.3 | rmse_h25 | last_slope | 5.620 [1.950, 9.290] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.3 | rmse_h25 | persistence | 0.865 [0.571, 1.180] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.3 | rmse_h50 | last_slope | 10.522 [4.959, 16.085] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.3 | rmse_h50 | persistence | 1.300 [0.353, 2.350] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.3 | rmse_smooth_h1 | last_slope | 0.684 [0.236, 1.132] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.3 | rmse_smooth_h1 | persistence | 0.497 [0.110, 0.884] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.3 | rmse_smooth_h10 | last_slope | 3.140 [1.815, 4.465] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.3 | rmse_smooth_h10 | persistence | 0.966 [0.603, 1.330] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.3 | rmse_smooth_h100 | last_slope | 22.082 [7.655, 36.509] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.3 | rmse_smooth_h100 | persistence | 1.205 [0.704, 1.706] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.3 | rmse_smooth_h25 | last_slope | 5.838 [2.405, 9.270] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.3 | rmse_smooth_h25 | persistence | 0.635 [0.209, 1.069] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.3 | rmse_smooth_h50 | last_slope | 10.523 [4.959, 16.087] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.3 | rmse_smooth_h50 | persistence | 1.300 [0.352, 2.350] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.5 | mae_h1 | last_slope | 0.642 [0.198, 1.085] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.5 | mae_h1 | persistence | 0.524 [0.047, 1.016] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.5 | mae_h10 | last_slope | 2.527 [1.938, 3.130] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.5 | mae_h10 | persistence | 1.354 [0.510, 1.928] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.5 | mae_h100 | last_slope | 14.573 [5.467, 22.398] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.5 | mae_h100 | persistence | 2.842 [2.048, 3.830] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.5 | mae_h25 | last_slope | 4.282 [2.681, 6.100] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.5 | mae_h25 | persistence | 1.599 [0.788, 2.409] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.5 | mae_h50 | last_slope | 7.386 [2.980, 11.306] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.5 | mae_h50 | persistence | 1.521 [0.930, 2.368] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.5 | rmse_h1 | last_slope | 0.642 [0.198, 1.085] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.5 | rmse_h1 | persistence | 0.524 [0.047, 1.016] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.5 | rmse_h10 | last_slope | 2.527 [1.938, 3.130] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.5 | rmse_h10 | persistence | 1.354 [0.510, 1.928] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.5 | rmse_h100 | last_slope | 14.573 [5.467, 22.398] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.5 | rmse_h100 | persistence | 2.842 [2.048, 3.830] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.5 | rmse_h25 | last_slope | 4.282 [2.681, 6.100] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.5 | rmse_h25 | persistence | 1.599 [0.788, 2.409] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.5 | rmse_h50 | last_slope | 7.386 [2.980, 11.306] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.5 | rmse_h50 | persistence | 1.521 [0.930, 2.368] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.5 | rmse_smooth_h1 | last_slope | 0.622 [0.158, 1.085] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.5 | rmse_smooth_h1 | persistence | 0.504 [0.007, 1.001] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.5 | rmse_smooth_h10 | last_slope | 2.435 [1.938, 3.130] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.5 | rmse_smooth_h10 | persistence | 1.262 [0.510, 1.837] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.5 | rmse_smooth_h100 | last_slope | 14.533 [5.454, 22.324] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.5 | rmse_smooth_h100 | persistence | 2.800 [2.040, 3.735] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.5 | rmse_smooth_h25 | last_slope | 4.239 [2.706, 6.034] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.5 | rmse_smooth_h25 | persistence | 1.542 [0.673, 2.411] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.5 | rmse_smooth_h50 | last_slope | 7.277 [2.956, 11.088] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.5 | rmse_smooth_h50 | persistence | 1.412 [0.882, 2.089] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.7 | mae_h1 | last_slope | 0.112 [0.044, 0.200] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.7 | mae_h1 | persistence | 0.092 [0.023, 0.162] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.7 | mae_h10 | last_slope | 0.861 [0.120, 1.788] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.7 | mae_h10 | persistence | 0.717 [0.237, 1.507] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.7 | mae_h100 | last_slope | 2.351 [0.391, 5.280] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.7 | mae_h100 | persistence | 3.080 [1.373, 4.710] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.7 | mae_h25 | last_slope | 1.577 [0.923, 2.657] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.7 | mae_h25 | persistence | 0.714 [0.117, 1.649] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.7 | mae_h50 | last_slope | 1.873 [1.076, 3.358] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.7 | mae_h50 | persistence | 1.046 [0.194, 1.898] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.7 | rmse_h1 | last_slope | 0.112 [0.044, 0.200] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.7 | rmse_h1 | persistence | 0.092 [0.023, 0.162] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.7 | rmse_h10 | last_slope | 0.861 [0.120, 1.788] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.7 | rmse_h10 | persistence | 0.717 [0.237, 1.507] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.7 | rmse_h100 | last_slope | 2.351 [0.391, 5.280] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.7 | rmse_h100 | persistence | 3.080 [1.373, 4.710] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.7 | rmse_h25 | last_slope | 1.577 [0.923, 2.657] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.7 | rmse_h25 | persistence | 0.714 [0.117, 1.649] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.7 | rmse_h50 | last_slope | 1.873 [1.076, 3.358] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.7 | rmse_h50 | persistence | 1.046 [0.194, 1.898] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.7 | rmse_smooth_h1 | last_slope | 0.077 [0.029, 0.170] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.7 | rmse_smooth_h1 | persistence | 0.046 [0.004, 0.122] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.7 | rmse_smooth_h10 | last_slope | 0.665 [0.164, 1.563] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.7 | rmse_smooth_h10 | persistence | 0.610 [0.172, 1.271] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.7 | rmse_smooth_h100 | last_slope | 2.418 [0.603, 5.254] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.7 | rmse_smooth_h100 | persistence | 2.954 [1.401, 4.363] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.7 | rmse_smooth_h25 | last_slope | 1.556 [0.923, 2.590] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.7 | rmse_smooth_h25 | persistence | 0.693 [0.117, 1.579] |  | 4 | 1 | c77e8f0d |
| loco | start_points | frac:0.7 | rmse_smooth_h50 | last_slope | 1.981 [1.070, 3.220] |  | 4 | 1 | 2751ee9f |
| loco | start_points | frac:0.7 | rmse_smooth_h50 | persistence | 1.007 [0.165, 1.849] |  | 4 | 1 | c77e8f0d |
| loco | start_points | overall | mae_h1 | last_slope | 0.346 [0.183, 0.509] |  | 4 | 1 | 2751ee9f |
| loco | start_points | overall | mae_h1 | persistence | 0.283 [0.120, 0.447] |  | 4 | 1 | c77e8f0d |
| loco | start_points | overall | mae_h10 | last_slope | 2.092 [1.854, 2.484] |  | 4 | 1 | 2751ee9f |
| loco | start_points | overall | mae_h10 | persistence | 1.075 [0.880, 1.318] |  | 4 | 1 | c77e8f0d |
| loco | start_points | overall | mae_h100 | last_slope | 11.328 [9.380, 13.246] |  | 4 | 1 | 2751ee9f |
| loco | start_points | overall | mae_h100 | persistence | 2.416 [1.580, 3.330] |  | 4 | 1 | c77e8f0d |
| loco | start_points | overall | mae_h25 | last_slope | 3.299 [2.819, 3.779] |  | 4 | 1 | 2751ee9f |
| loco | start_points | overall | mae_h25 | persistence | 1.070 [0.854, 1.230] |  | 4 | 1 | c77e8f0d |
| loco | start_points | overall | mae_h50 | last_slope | 5.642 [4.805, 6.318] |  | 4 | 1 | 2751ee9f |
| loco | start_points | overall | mae_h50 | persistence | 1.273 [0.861, 1.723] |  | 4 | 1 | c77e8f0d |
| loco | start_points | overall | rmse_h1 | last_slope | 0.455 [0.240, 0.669] |  | 4 | 1 | 2751ee9f |
| loco | start_points | overall | rmse_h1 | persistence | 0.397 [0.177, 0.617] |  | 4 | 1 | c77e8f0d |
| loco | start_points | overall | rmse_h10 | last_slope | 2.474 [2.053, 3.110] |  | 4 | 1 | 2751ee9f |
| loco | start_points | overall | rmse_h10 | persistence | 1.332 [1.082, 1.703] |  | 4 | 1 | c77e8f0d |
| loco | start_points | overall | rmse_h100 | last_slope | 15.247 [12.166, 18.329] |  | 4 | 1 | 2751ee9f |
| loco | start_points | overall | rmse_h100 | persistence | 2.680 [1.781, 3.658] |  | 4 | 1 | c77e8f0d |
| loco | start_points | overall | rmse_h25 | last_slope | 4.141 [3.336, 4.947] |  | 4 | 1 | 2751ee9f |
| loco | start_points | overall | rmse_h25 | persistence | 1.317 [1.143, 1.422] |  | 4 | 1 | c77e8f0d |
| loco | start_points | overall | rmse_h50 | last_slope | 7.343 [6.361, 8.324] |  | 4 | 1 | 2751ee9f |
| loco | start_points | overall | rmse_h50 | persistence | 1.506 [1.020, 1.989] |  | 4 | 1 | c77e8f0d |
| loco | start_points | overall | rmse_smooth_h1 | last_slope | 0.480 [0.232, 0.727] |  | 4 | 1 | 2751ee9f |
| loco | start_points | overall | rmse_smooth_h1 | persistence | 0.400 [0.168, 0.632] |  | 4 | 1 | c77e8f0d |
| loco | start_points | overall | rmse_smooth_h10 | last_slope | 2.427 [1.981, 2.957] |  | 4 | 1 | 2751ee9f |
| loco | start_points | overall | rmse_smooth_h10 | persistence | 1.280 [1.056, 1.653] |  | 4 | 1 | c77e8f0d |
| loco | start_points | overall | rmse_smooth_h100 | last_slope | 15.252 [12.104, 18.400] |  | 4 | 1 | 2751ee9f |
| loco | start_points | overall | rmse_smooth_h100 | persistence | 2.693 [1.868, 3.548] |  | 4 | 1 | c77e8f0d |
| loco | start_points | overall | rmse_smooth_h25 | last_slope | 4.139 [3.346, 4.932] |  | 4 | 1 | 2751ee9f |
| loco | start_points | overall | rmse_smooth_h25 | persistence | 1.283 [1.119, 1.399] |  | 4 | 1 | c77e8f0d |
| loco | start_points | overall | rmse_smooth_h50 | last_slope | 7.260 [6.203, 8.316] |  | 4 | 1 | 2751ee9f |
| loco | start_points | overall | rmse_smooth_h50 | persistence | 1.422 [0.962, 1.889] |  | 4 | 1 | c77e8f0d |

</details>

<details><summary>nasa_forecast (210 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | mae_h1 | last_slope | 0.539 [0.389, 0.690] | 0.717 | 4 | 1 | ade93415 |
| loco | all | overall | mae_h1 | persistence | 0.580 [0.410, 0.750] | 0.782 | 4 | 1 | 1c7e63ef |
| loco | all | overall | mae_h10 | last_slope | 2.388 [1.634, 3.142] | 3.141 | 4 | 1 | ade93415 |
| loco | all | overall | mae_h10 | persistence | 2.332 [1.870, 2.794] | 2.741 | 4 | 1 | 1c7e63ef |
| loco | all | overall | mae_h100 | last_slope | 17.065 [11.671, 24.799] | 10.838 | 4 | 1 | ade93415 |
| loco | all | overall | mae_h100 | persistence | 21.246 [19.007, 23.682] | 20.043 | 4 | 1 | 1c7e63ef |
| loco | all | overall | mae_h25 | last_slope | 4.666 [3.402, 5.930] | 5.655 | 4 | 1 | ade93415 |
| loco | all | overall | mae_h25 | persistence | 5.128 [4.398, 5.969] | 5.088 | 4 | 1 | 1c7e63ef |
| loco | all | overall | mae_h50 | last_slope | 9.478 [7.071, 11.884] | 10.898 | 4 | 1 | ade93415 |
| loco | all | overall | mae_h50 | persistence | 10.769 [9.370, 12.146] | 10.813 | 4 | 1 | 1c7e63ef |
| loco | all | overall | rmse_h1 | last_slope | 0.992 [0.715, 1.269] | 1.301 | 4 | 1 | ade93415 |
| loco | all | overall | rmse_h1 | persistence | 0.955 [0.697, 1.213] | 1.245 | 4 | 1 | 1c7e63ef |
| loco | all | overall | rmse_h10 | last_slope | 2.986 [2.037, 3.934] | 3.895 | 4 | 1 | ade93415 |
| loco | all | overall | rmse_h10 | persistence | 2.737 [2.186, 3.288] | 3.153 | 4 | 1 | 1c7e63ef |
| loco | all | overall | rmse_h100 | last_slope | 20.888 [14.826, 29.272] | 14.274 | 4 | 1 | ade93415 |
| loco | all | overall | rmse_h100 | persistence | 21.343 [19.065, 23.828] | 20.144 | 4 | 1 | 1c7e63ef |
| loco | all | overall | rmse_h25 | last_slope | 5.958 [4.205, 7.710] | 7.523 | 4 | 1 | ade93415 |
| loco | all | overall | rmse_h25 | persistence | 5.731 [4.913, 6.569] | 6.007 | 4 | 1 | 1c7e63ef |
| loco | all | overall | rmse_h50 | last_slope | 12.164 [8.884, 15.444] | 14.476 | 4 | 1 | ade93415 |
| loco | all | overall | rmse_h50 | persistence | 11.211 [9.697, 12.759] | 11.258 | 4 | 1 | 1c7e63ef |
| loco | all | overall | rmse_smooth_h1 | last_slope | 0.771 [0.542, 0.999] | 1.021 | 4 | 1 | ade93415 |
| loco | all | overall | rmse_smooth_h1 | persistence | 0.752 [0.537, 0.968] | 0.995 | 4 | 1 | 1c7e63ef |
| loco | all | overall | rmse_smooth_h10 | last_slope | 2.920 [1.947, 3.892] | 3.895 | 4 | 1 | ade93415 |
| loco | all | overall | rmse_smooth_h10 | persistence | 2.720 [2.161, 3.279] | 3.174 | 4 | 1 | 1c7e63ef |
| loco | all | overall | rmse_smooth_h100 | last_slope | 20.922 [14.805, 29.340] | 14.190 | 4 | 1 | ade93415 |
| loco | all | overall | rmse_smooth_h100 | persistence | 21.405 [19.130, 23.891] | 20.177 | 4 | 1 | 1c7e63ef |
| loco | all | overall | rmse_smooth_h25 | last_slope | 5.917 [4.159, 7.675] | 7.497 | 4 | 1 | ade93415 |
| loco | all | overall | rmse_smooth_h25 | persistence | 5.776 [4.948, 6.625] | 6.055 | 4 | 1 | 1c7e63ef |
| loco | all | overall | rmse_smooth_h50 | last_slope | 12.088 [8.804, 15.372] | 14.467 | 4 | 1 | ade93415 |
| loco | all | overall | rmse_smooth_h50 | persistence | 11.283 [9.762, 12.833] | 11.347 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:30 | mae_h1 | last_slope | 2.349 [1.110, 3.513] | 0.537 | 4 | 1 | ade93415 |
| loco | start_points | fixed:30 | mae_h1 | persistence | 2.105 [1.142, 2.970] | 0.659 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:30 | mae_h10 | last_slope | 0.696 [0.129, 1.432] | 0.251 | 4 | 1 | ade93415 |
| loco | start_points | fixed:30 | mae_h10 | persistence | 2.367 [1.235, 4.018] | 0.977 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:30 | mae_h100 | last_slope | 11.712 [0.440, 29.881] | 6.309 | 4 | 1 | ade93415 |
| loco | start_points | fixed:30 | mae_h100 | persistence | 22.041 [19.036, 25.046] | 18.594 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:30 | mae_h25 | last_slope | 2.904 [0.640, 6.334] | 1.727 | 4 | 1 | ade93415 |
| loco | start_points | fixed:30 | mae_h25 | persistence | 5.609 [4.366, 7.695] | 4.798 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:30 | mae_h50 | last_slope | 6.306 [1.574, 11.656] | 7.235 | 4 | 1 | ade93415 |
| loco | start_points | fixed:30 | mae_h50 | persistence | 14.185 [12.427, 16.944] | 13.377 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:30 | rmse_h1 | last_slope | 2.349 [1.110, 3.513] | 0.537 | 4 | 1 | ade93415 |
| loco | start_points | fixed:30 | rmse_h1 | persistence | 2.105 [1.142, 2.970] | 0.659 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:30 | rmse_h10 | last_slope | 0.696 [0.129, 1.432] | 0.251 | 4 | 1 | ade93415 |
| loco | start_points | fixed:30 | rmse_h10 | persistence | 2.367 [1.235, 4.018] | 0.977 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:30 | rmse_h100 | last_slope | 11.712 [0.440, 29.881] | 6.309 | 4 | 1 | ade93415 |
| loco | start_points | fixed:30 | rmse_h100 | persistence | 22.041 [19.036, 25.046] | 18.594 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:30 | rmse_h25 | last_slope | 2.904 [0.640, 6.334] | 1.727 | 4 | 1 | ade93415 |
| loco | start_points | fixed:30 | rmse_h25 | persistence | 5.609 [4.366, 7.695] | 4.798 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:30 | rmse_h50 | last_slope | 6.306 [1.574, 11.656] | 7.235 | 4 | 1 | ade93415 |
| loco | start_points | fixed:30 | rmse_h50 | persistence | 14.185 [12.427, 16.944] | 13.377 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:30 | rmse_smooth_h1 | last_slope | 0.663 [0.431, 0.958] | 0.537 | 4 | 1 | ade93415 |
| loco | start_points | fixed:30 | rmse_smooth_h1 | persistence | 0.418 [0.077, 0.759] | 0.659 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:30 | rmse_smooth_h10 | last_slope | 1.164 [0.354, 1.973] | 2.122 | 4 | 1 | ade93415 |
| loco | start_points | fixed:30 | rmse_smooth_h10 | persistence | 2.957 [1.841, 4.096] | 3.350 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:30 | rmse_smooth_h100 | last_slope | 11.676 [0.447, 29.884] | 6.150 | 4 | 1 | ade93415 |
| loco | start_points | fixed:30 | rmse_smooth_h100 | persistence | 21.998 [18.949, 25.046] | 18.435 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:30 | rmse_smooth_h25 | last_slope | 2.632 [0.455, 6.062] | 0.639 | 4 | 1 | ade93415 |
| loco | start_points | fixed:30 | rmse_smooth_h25 | persistence | 5.337 [3.966, 7.567] | 3.710 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:30 | rmse_smooth_h50 | last_slope | 6.239 [1.574, 11.656] | 6.968 | 4 | 1 | ade93415 |
| loco | start_points | fixed:30 | rmse_smooth_h50 | persistence | 14.118 [12.361, 16.944] | 13.110 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:50 | mae_h1 | last_slope | 0.750 [0.234, 1.464] | 0.104 | 4 | 1 | ade93415 |
| loco | start_points | fixed:50 | mae_h1 | persistence | 0.733 [0.375, 1.283] | 0.313 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:50 | mae_h10 | last_slope | 6.496 [3.997, 8.995] | 8.191 | 4 | 1 | ade93415 |
| loco | start_points | fixed:50 | mae_h10 | persistence | 4.762 [3.862, 6.436] | 4.024 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:50 | mae_h100 | last_slope | 32.235 [15.395, 51.238] |  | 3 | 1 | aa576a67 |
| loco | start_points | fixed:50 | mae_h100 | persistence | 23.003 [19.038, 25.889] |  | 3 | 1 | 6583fd6a |
| loco | start_points | fixed:50 | mae_h25 | last_slope | 14.547 [9.163, 19.931] | 20.054 | 4 | 1 | ade93415 |
| loco | start_points | fixed:50 | mae_h25 | persistence | 10.212 [8.506, 12.505] | 9.637 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:50 | mae_h50 | last_slope | 23.648 [14.338, 32.958] | 36.164 | 4 | 1 | ade93415 |
| loco | start_points | fixed:50 | mae_h50 | persistence | 14.977 [12.995, 16.630] | 15.329 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:50 | rmse_h1 | last_slope | 0.750 [0.234, 1.464] | 0.104 | 4 | 1 | ade93415 |
| loco | start_points | fixed:50 | rmse_h1 | persistence | 0.733 [0.375, 1.283] | 0.313 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:50 | rmse_h10 | last_slope | 6.496 [3.997, 8.995] | 8.191 | 4 | 1 | ade93415 |
| loco | start_points | fixed:50 | rmse_h10 | persistence | 4.762 [3.862, 6.436] | 4.024 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:50 | rmse_h100 | last_slope | 32.235 [15.395, 51.238] |  | 3 | 1 | aa576a67 |
| loco | start_points | fixed:50 | rmse_h100 | persistence | 23.003 [19.038, 25.889] |  | 3 | 1 | 6583fd6a |
| loco | start_points | fixed:50 | rmse_h25 | last_slope | 14.547 [9.163, 19.931] | 20.054 | 4 | 1 | ade93415 |
| loco | start_points | fixed:50 | rmse_h25 | persistence | 10.212 [8.506, 12.505] | 9.637 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:50 | rmse_h50 | last_slope | 23.648 [14.338, 32.958] | 36.164 | 4 | 1 | ade93415 |
| loco | start_points | fixed:50 | rmse_h50 | persistence | 14.977 [12.995, 16.630] | 15.329 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:50 | rmse_smooth_h1 | last_slope | 0.828 [0.450, 1.464] | 0.417 | 4 | 1 | ade93415 |
| loco | start_points | fixed:50 | rmse_smooth_h1 | persistence | 0.655 [0.140, 1.283] | 0.000 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:50 | rmse_smooth_h10 | last_slope | 6.496 [3.997, 8.995] | 8.191 | 4 | 1 | ade93415 |
| loco | start_points | fixed:50 | rmse_smooth_h10 | persistence | 4.762 [3.862, 6.436] | 4.024 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:50 | rmse_smooth_h100 | last_slope | 32.235 [15.395, 51.238] |  | 3 | 1 | aa576a67 |
| loco | start_points | fixed:50 | rmse_smooth_h100 | persistence | 23.003 [19.038, 25.889] |  | 3 | 1 | 6583fd6a |
| loco | start_points | fixed:50 | rmse_smooth_h25 | last_slope | 14.547 [9.163, 19.931] | 20.054 | 4 | 1 | ade93415 |
| loco | start_points | fixed:50 | rmse_smooth_h25 | persistence | 10.212 [8.506, 12.505] | 9.637 | 4 | 1 | 1c7e63ef |
| loco | start_points | fixed:50 | rmse_smooth_h50 | last_slope | 23.568 [14.350, 32.786] | 35.820 | 4 | 1 | ade93415 |
| loco | start_points | fixed:50 | rmse_smooth_h50 | persistence | 14.897 [13.002, 16.555] | 14.985 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.3 | mae_h1 | last_slope | 0.366 [0.145, 0.587] | 0.263 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.3 | mae_h1 | persistence | 0.262 [0.062, 0.494] | 0.216 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.3 | mae_h10 | last_slope | 3.289 [2.078, 4.500] | 2.289 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.3 | mae_h10 | persistence | 1.776 [0.447, 3.105] | 2.497 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.3 | mae_h100 | last_slope | 23.144 [10.125, 30.488] | 30.580 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.3 | mae_h100 | persistence | 21.592 [17.906, 25.277] | 17.279 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.3 | mae_h25 | last_slope | 6.727 [2.243, 10.150] | 11.114 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.3 | mae_h25 | persistence | 4.666 [2.061, 6.293] | 0.850 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.3 | mae_h50 | last_slope | 10.464 [3.890, 15.179] | 12.503 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.3 | mae_h50 | persistence | 13.452 [11.698, 15.205] | 11.427 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.3 | rmse_h1 | last_slope | 0.366 [0.145, 0.587] | 0.263 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.3 | rmse_h1 | persistence | 0.262 [0.062, 0.494] | 0.216 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.3 | rmse_h10 | last_slope | 3.289 [2.078, 4.500] | 2.289 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.3 | rmse_h10 | persistence | 1.776 [0.447, 3.105] | 2.497 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.3 | rmse_h100 | last_slope | 23.144 [10.125, 30.488] | 30.580 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.3 | rmse_h100 | persistence | 21.592 [17.906, 25.277] | 17.279 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.3 | rmse_h25 | last_slope | 6.727 [2.243, 10.150] | 11.114 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.3 | rmse_h25 | persistence | 4.666 [2.061, 6.293] | 0.850 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.3 | rmse_h50 | last_slope | 10.464 [3.890, 15.179] | 12.503 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.3 | rmse_h50 | persistence | 13.452 [11.698, 15.205] | 11.427 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.3 | rmse_smooth_h1 | last_slope | 0.552 [0.175, 0.935] | 0.479 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.3 | rmse_smooth_h1 | persistence | 0.341 [0.123, 0.559] | 0.000 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.3 | rmse_smooth_h10 | last_slope | 3.035 [1.684, 4.385] | 2.289 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.3 | rmse_smooth_h10 | persistence | 1.886 [0.811, 2.961] | 2.497 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.3 | rmse_smooth_h100 | last_slope | 23.127 [10.164, 30.617] | 30.580 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.3 | rmse_smooth_h100 | persistence | 21.451 [17.911, 24.991] | 17.279 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.3 | rmse_smooth_h25 | last_slope | 6.672 [2.188, 10.150] | 11.114 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.3 | rmse_smooth_h25 | persistence | 4.720 [2.091, 6.317] | 0.850 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.3 | rmse_smooth_h50 | last_slope | 10.463 [3.886, 15.179] | 12.503 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.3 | rmse_smooth_h50 | persistence | 13.450 [11.695, 15.205] | 11.427 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.5 | mae_h1 | last_slope | 2.119 [0.305, 3.934] | 3.857 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.5 | mae_h1 | persistence | 1.752 [0.144, 3.360] | 3.372 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.5 | mae_h10 | last_slope | 3.570 [1.260, 6.697] | 8.321 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.5 | mae_h10 | persistence | 3.664 [2.972, 4.463] | 3.465 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.5 | mae_h100 | last_slope | 26.098 [18.310, 39.660] |  | 3 | 1 | aa576a67 |
| loco | start_points | frac:0.5 | mae_h100 | persistence | 21.687 [16.103, 26.550] |  | 3 | 1 | 6583fd6a |
| loco | start_points | frac:0.5 | mae_h25 | last_slope | 6.441 [3.728, 8.000] | 8.129 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.5 | mae_h25 | persistence | 6.722 [4.992, 8.310] | 4.010 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.5 | mae_h50 | last_slope | 12.312 [9.073, 14.516] | 14.191 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.5 | mae_h50 | persistence | 13.020 [9.963, 16.219] | 10.087 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.5 | rmse_h1 | last_slope | 2.119 [0.305, 3.934] | 3.857 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.5 | rmse_h1 | persistence | 1.752 [0.144, 3.360] | 3.372 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.5 | rmse_h10 | last_slope | 3.570 [1.260, 6.697] | 8.321 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.5 | rmse_h10 | persistence | 3.664 [2.972, 4.463] | 3.465 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.5 | rmse_h100 | last_slope | 26.098 [18.310, 39.660] |  | 3 | 1 | aa576a67 |
| loco | start_points | frac:0.5 | rmse_h100 | persistence | 21.687 [16.103, 26.550] |  | 3 | 1 | 6583fd6a |
| loco | start_points | frac:0.5 | rmse_h25 | last_slope | 6.441 [3.728, 8.000] | 8.129 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.5 | rmse_h25 | persistence | 6.722 [4.992, 8.310] | 4.010 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.5 | rmse_h50 | last_slope | 12.312 [9.073, 14.516] | 14.191 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.5 | rmse_h50 | persistence | 13.020 [9.963, 16.219] | 10.087 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.5 | rmse_smooth_h1 | last_slope | 0.689 [0.305, 1.199] | 1.484 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.5 | rmse_smooth_h1 | persistence | 0.322 [0.000, 0.749] | 0.999 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.5 | rmse_smooth_h10 | last_slope | 3.571 [1.260, 6.697] | 8.321 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.5 | rmse_smooth_h10 | persistence | 3.665 [2.973, 4.463] | 3.465 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.5 | rmse_smooth_h100 | last_slope | 26.101 [18.318, 39.660] |  | 3 | 1 | aa576a67 |
| loco | start_points | frac:0.5 | rmse_smooth_h100 | persistence | 21.685 [16.095, 26.550] |  | 3 | 1 | 6583fd6a |
| loco | start_points | frac:0.5 | rmse_smooth_h25 | last_slope | 6.581 [3.747, 8.064] | 8.129 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.5 | rmse_smooth_h25 | persistence | 6.869 [5.136, 8.598] | 4.010 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.5 | rmse_smooth_h50 | last_slope | 12.582 [9.249, 14.909] | 14.977 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.5 | rmse_smooth_h50 | persistence | 12.889 [9.561, 16.216] | 9.302 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.7 | mae_h1 | last_slope | 1.460 [0.161, 3.389] | 4.434 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.7 | mae_h1 | persistence | 1.282 [0.357, 2.907] | 3.690 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.7 | mae_h10 | last_slope | 2.002 [0.811, 3.192] | 3.435 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.7 | mae_h10 | persistence | 2.565 [1.535, 3.576] | 3.998 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.7 | mae_h100 | last_slope | 28.756 |  | 1 | 1 | 3bdc1438 |
| loco | start_points | frac:0.7 | mae_h100 | persistence | 23.823 |  | 1 | 1 | 6252a211 |
| loco | start_points | frac:0.7 | mae_h25 | last_slope | 4.359 [2.028, 8.175] | 10.004 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.7 | mae_h25 | persistence | 7.057 [4.781, 9.333] | 8.579 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.7 | mae_h50 | last_slope | 11.921 [5.216, 19.355] | 23.634 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.7 | mae_h50 | persistence | 10.912 [8.091, 13.103] | 13.532 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.7 | rmse_h1 | last_slope | 1.460 [0.161, 3.389] | 4.434 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.7 | rmse_h1 | persistence | 1.282 [0.357, 2.907] | 3.690 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.7 | rmse_h10 | last_slope | 2.002 [0.811, 3.192] | 3.435 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.7 | rmse_h10 | persistence | 2.565 [1.535, 3.576] | 3.998 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.7 | rmse_h100 | last_slope | 28.756 |  | 1 | 1 | 3bdc1438 |
| loco | start_points | frac:0.7 | rmse_h100 | persistence | 23.823 |  | 1 | 1 | 6252a211 |
| loco | start_points | frac:0.7 | rmse_h25 | last_slope | 4.359 [2.028, 8.175] | 10.004 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.7 | rmse_h25 | persistence | 7.057 [4.781, 9.333] | 8.579 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.7 | rmse_h50 | last_slope | 11.921 [5.216, 19.355] | 23.634 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.7 | rmse_h50 | persistence | 10.912 [8.091, 13.103] | 13.532 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.7 | rmse_smooth_h1 | last_slope | 0.467 [0.229, 0.922] | 1.152 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.7 | rmse_smooth_h1 | persistence | 0.447 [0.168, 0.679] | 0.409 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.7 | rmse_smooth_h10 | last_slope | 2.002 [0.811, 3.192] | 3.435 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.7 | rmse_smooth_h10 | persistence | 2.565 [1.535, 3.576] | 3.998 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.7 | rmse_smooth_h100 | last_slope | 28.760 |  | 1 | 1 | 3bdc1438 |
| loco | start_points | frac:0.7 | rmse_smooth_h100 | persistence | 23.819 |  | 1 | 1 | 6252a211 |
| loco | start_points | frac:0.7 | rmse_smooth_h25 | last_slope | 4.426 [2.028, 8.376] | 10.271 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.7 | rmse_smooth_h25 | persistence | 6.990 [4.742, 9.199] | 8.312 | 4 | 1 | 1c7e63ef |
| loco | start_points | frac:0.7 | rmse_smooth_h50 | last_slope | 12.144 [5.212, 20.033] | 24.537 | 4 | 1 | ade93415 |
| loco | start_points | frac:0.7 | rmse_smooth_h50 | persistence | 10.688 [8.086, 12.651] | 12.628 | 4 | 1 | 1c7e63ef |
| loco | start_points | overall | mae_h1 | last_slope | 1.409 [0.753, 2.065] | 1.839 | 4 | 1 | ade93415 |
| loco | start_points | overall | mae_h1 | persistence | 1.227 [0.749, 1.704] | 1.650 | 4 | 1 | 1c7e63ef |
| loco | start_points | overall | mae_h10 | last_slope | 3.211 [2.033, 4.388] | 4.498 | 4 | 1 | ade93415 |
| loco | start_points | overall | mae_h10 | persistence | 3.027 [2.290, 3.709] | 2.992 | 4 | 1 | 1c7e63ef |
| loco | start_points | overall | mae_h100 | last_slope | 21.383 [11.988, 33.067] | 18.444 | 4 | 1 | ade93415 |
| loco | start_points | overall | mae_h100 | persistence | 21.418 [18.112, 24.723] | 17.937 | 4 | 1 | 1c7e63ef |
| loco | start_points | overall | mae_h25 | last_slope | 6.996 [4.107, 9.795] | 10.206 | 4 | 1 | ade93415 |
| loco | start_points | overall | mae_h25 | persistence | 6.853 [5.624, 8.396] | 5.575 | 4 | 1 | 1c7e63ef |
| loco | start_points | overall | mae_h50 | last_slope | 12.930 [7.968, 17.892] | 18.745 | 4 | 1 | ade93415 |
| loco | start_points | overall | mae_h50 | persistence | 13.309 [11.293, 15.482] | 12.750 | 4 | 1 | 1c7e63ef |
| loco | start_points | overall | rmse_h1 | last_slope | 1.909 [1.139, 2.679] | 2.642 | 4 | 1 | ade93415 |
| loco | start_points | overall | rmse_h1 | persistence | 1.654 [1.057, 2.251] | 2.261 | 4 | 1 | 1c7e63ef |
| loco | start_points | overall | rmse_h10 | last_slope | 3.935 [2.490, 5.381] | 5.540 | 4 | 1 | ade93415 |
| loco | start_points | overall | rmse_h10 | persistence | 3.348 [2.574, 4.229] | 3.206 | 4 | 1 | 1c7e63ef |
| loco | start_points | overall | rmse_h100 | last_slope | 23.985 [14.809, 34.609] | 22.079 | 4 | 1 | ade93415 |
| loco | start_points | overall | rmse_h100 | persistence | 21.443 [18.142, 24.745] | 17.949 | 4 | 1 | 1c7e63ef |
| loco | start_points | overall | rmse_h25 | last_slope | 8.281 [5.214, 11.347] | 11.788 | 4 | 1 | ade93415 |
| loco | start_points | overall | rmse_h25 | persistence | 7.261 [6.150, 8.841] | 6.423 | 4 | 1 | 1c7e63ef |
| loco | start_points | overall | rmse_h50 | last_slope | 14.573 [9.092, 19.775] | 21.338 | 4 | 1 | ade93415 |
| loco | start_points | overall | rmse_h50 | persistence | 13.452 [11.482, 15.613] | 12.879 | 4 | 1 | 1c7e63ef |
| loco | start_points | overall | rmse_smooth_h1 | last_slope | 0.731 [0.474, 0.975] | 0.919 | 4 | 1 | ade93415 |
| loco | start_points | overall | rmse_smooth_h1 | persistence | 0.560 [0.352, 0.743] | 0.566 | 4 | 1 | 1c7e63ef |
| loco | start_points | overall | rmse_smooth_h10 | last_slope | 3.908 [2.389, 5.426] | 5.619 | 4 | 1 | ade93415 |
| loco | start_points | overall | rmse_smooth_h10 | persistence | 3.420 [2.667, 4.230] | 3.511 | 4 | 1 | 1c7e63ef |
| loco | start_points | overall | rmse_smooth_h100 | last_slope | 23.966 [14.787, 34.635] | 22.056 | 4 | 1 | ade93415 |
| loco | start_points | overall | rmse_smooth_h100 | persistence | 21.388 [18.099, 24.678] | 17.866 | 4 | 1 | 1c7e63ef |
| loco | start_points | overall | rmse_smooth_h25 | last_slope | 8.310 [5.276, 11.343] | 11.813 | 4 | 1 | ade93415 |
| loco | start_points | overall | rmse_smooth_h25 | persistence | 7.247 [6.042, 8.805] | 6.205 | 4 | 1 | 1c7e63ef |
| loco | start_points | overall | rmse_smooth_h50 | last_slope | 14.634 [9.100, 19.864] | 21.514 | 4 | 1 | ade93415 |
| loco | start_points | overall | rmse_smooth_h50 | persistence | 13.355 [11.498, 15.502] | 12.434 | 4 | 1 | 1c7e63ef |

</details>

<details><summary>toyota_forecast (360 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | mae_h1 | last_slope | 0.042 |  | 1 | 1 | 77403933 |
| test1 | all | overall | mae_h1 | persistence | 0.058 |  | 1 | 1 | 85a8557f |
| test1 | all | overall | mae_h10 | last_slope | 0.114 |  | 1 | 1 | 77403933 |
| test1 | all | overall | mae_h10 | persistence | 0.312 |  | 1 | 1 | 85a8557f |
| test1 | all | overall | mae_h100 | last_slope | 1.434 |  | 1 | 1 | 77403933 |
| test1 | all | overall | mae_h100 | persistence | 2.364 |  | 1 | 1 | 85a8557f |
| test1 | all | overall | mae_h200 | last_slope | 3.258 |  | 1 | 1 | 77403933 |
| test1 | all | overall | mae_h200 | persistence | 3.920 |  | 1 | 1 | 85a8557f |
| test1 | all | overall | mae_h50 | last_slope | 0.581 |  | 1 | 1 | 77403933 |
| test1 | all | overall | mae_h50 | persistence | 1.335 |  | 1 | 1 | 85a8557f |
| test1 | all | overall | rmse_h1 | last_slope | 0.247 |  | 1 | 1 | 77403933 |
| test1 | all | overall | rmse_h1 | persistence | 0.244 |  | 1 | 1 | 85a8557f |
| test1 | all | overall | rmse_h10 | last_slope | 0.412 |  | 1 | 1 | 77403933 |
| test1 | all | overall | rmse_h10 | persistence | 0.566 |  | 1 | 1 | 85a8557f |
| test1 | all | overall | rmse_h100 | last_slope | 3.208 |  | 1 | 1 | 77403933 |
| test1 | all | overall | rmse_h100 | persistence | 3.798 |  | 1 | 1 | 85a8557f |
| test1 | all | overall | rmse_h200 | last_slope | 6.775 |  | 1 | 1 | 77403933 |
| test1 | all | overall | rmse_h200 | persistence | 5.672 |  | 1 | 1 | 85a8557f |
| test1 | all | overall | rmse_h50 | last_slope | 1.477 |  | 1 | 1 | 77403933 |
| test1 | all | overall | rmse_h50 | persistence | 2.254 |  | 1 | 1 | 85a8557f |
| test1 | all | overall | rmse_smooth_h1 | last_slope | 0.184 |  | 1 | 1 | 77403933 |
| test1 | all | overall | rmse_smooth_h1 | persistence | 0.179 |  | 1 | 1 | 85a8557f |
| test1 | all | overall | rmse_smooth_h10 | last_slope | 0.376 |  | 1 | 1 | 77403933 |
| test1 | all | overall | rmse_smooth_h10 | persistence | 0.538 |  | 1 | 1 | 85a8557f |
| test1 | all | overall | rmse_smooth_h100 | last_slope | 3.201 |  | 1 | 1 | 77403933 |
| test1 | all | overall | rmse_smooth_h100 | persistence | 3.790 |  | 1 | 1 | 85a8557f |
| test1 | all | overall | rmse_smooth_h200 | last_slope | 6.766 |  | 1 | 1 | 77403933 |
| test1 | all | overall | rmse_smooth_h200 | persistence | 5.665 |  | 1 | 1 | 85a8557f |
| test1 | all | overall | rmse_smooth_h50 | last_slope | 1.466 |  | 1 | 1 | 77403933 |
| test1 | all | overall | rmse_smooth_h50 | persistence | 2.243 |  | 1 | 1 | 85a8557f |
| test1 | start_points | fixed:100 | mae_h1 | last_slope | 0.010 |  | 1 | 1 | 77403933 |
| test1 | start_points | fixed:100 | mae_h1 | persistence | 0.012 |  | 1 | 1 | 85a8557f |
| test1 | start_points | fixed:100 | mae_h10 | last_slope | 0.024 |  | 1 | 1 | 77403933 |
| test1 | start_points | fixed:100 | mae_h10 | persistence | 0.103 |  | 1 | 1 | 85a8557f |
| test1 | start_points | fixed:100 | mae_h100 | last_slope | 0.250 |  | 1 | 1 | 77403933 |
| test1 | start_points | fixed:100 | mae_h100 | persistence | 0.867 |  | 1 | 1 | 85a8557f |
| test1 | start_points | fixed:100 | mae_h200 | last_slope | 0.913 |  | 1 | 1 | 77403933 |
| test1 | start_points | fixed:100 | mae_h200 | persistence | 2.152 |  | 1 | 1 | 85a8557f |
| test1 | start_points | fixed:100 | mae_h50 | last_slope | 0.135 |  | 1 | 1 | 77403933 |
| test1 | start_points | fixed:100 | mae_h50 | persistence | 0.576 |  | 1 | 1 | 85a8557f |
| test1 | start_points | fixed:100 | rmse_h1 | last_slope | 0.017 |  | 1 | 1 | 77403933 |
| test1 | start_points | fixed:100 | rmse_h1 | persistence | 0.020 |  | 1 | 1 | 85a8557f |
| test1 | start_points | fixed:100 | rmse_h10 | last_slope | 0.041 |  | 1 | 1 | 77403933 |
| test1 | start_points | fixed:100 | rmse_h10 | persistence | 0.252 |  | 1 | 1 | 85a8557f |
| test1 | start_points | fixed:100 | rmse_h100 | last_slope | 0.386 |  | 1 | 1 | 77403933 |
| test1 | start_points | fixed:100 | rmse_h100 | persistence | 1.205 |  | 1 | 1 | 85a8557f |
| test1 | start_points | fixed:100 | rmse_h200 | last_slope | 1.241 |  | 1 | 1 | 77403933 |
| test1 | start_points | fixed:100 | rmse_h200 | persistence | 2.873 |  | 1 | 1 | 85a8557f |
| test1 | start_points | fixed:100 | rmse_h50 | last_slope | 0.356 |  | 1 | 1 | 77403933 |
| test1 | start_points | fixed:100 | rmse_h50 | persistence | 1.435 |  | 1 | 1 | 85a8557f |
| test1 | start_points | fixed:100 | rmse_smooth_h1 | last_slope | 0.013 |  | 1 | 1 | 77403933 |
| test1 | start_points | fixed:100 | rmse_smooth_h1 | persistence | 0.018 |  | 1 | 1 | 85a8557f |
| test1 | start_points | fixed:100 | rmse_smooth_h10 | last_slope | 0.038 |  | 1 | 1 | 77403933 |
| test1 | start_points | fixed:100 | rmse_smooth_h10 | persistence | 0.249 |  | 1 | 1 | 85a8557f |
| test1 | start_points | fixed:100 | rmse_smooth_h100 | last_slope | 0.391 |  | 1 | 1 | 77403933 |
| test1 | start_points | fixed:100 | rmse_smooth_h100 | persistence | 1.209 |  | 1 | 1 | 85a8557f |
| test1 | start_points | fixed:100 | rmse_smooth_h200 | last_slope | 1.241 |  | 1 | 1 | 77403933 |
| test1 | start_points | fixed:100 | rmse_smooth_h200 | persistence | 2.873 |  | 1 | 1 | 85a8557f |
| test1 | start_points | fixed:100 | rmse_smooth_h50 | last_slope | 0.357 |  | 1 | 1 | 77403933 |
| test1 | start_points | fixed:100 | rmse_smooth_h50 | persistence | 1.435 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.3 | mae_h1 | last_slope | 0.023 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.3 | mae_h1 | persistence | 0.021 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.3 | mae_h10 | last_slope | 0.126 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.3 | mae_h10 | persistence | 0.139 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.3 | mae_h100 | last_slope | 1.226 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.3 | mae_h100 | persistence | 1.432 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.3 | mae_h200 | last_slope | 2.764 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.3 | mae_h200 | persistence | 2.821 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.3 | mae_h50 | last_slope | 0.518 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.3 | mae_h50 | persistence | 0.614 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.3 | rmse_h1 | last_slope | 0.045 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.3 | rmse_h1 | persistence | 0.037 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.3 | rmse_h10 | last_slope | 0.426 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.3 | rmse_h10 | persistence | 0.236 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.3 | rmse_h100 | last_slope | 3.856 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.3 | rmse_h100 | persistence | 2.605 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.3 | rmse_h200 | last_slope | 7.361 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.3 | rmse_h200 | persistence | 3.445 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.3 | rmse_h50 | last_slope | 1.773 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.3 | rmse_h50 | persistence | 1.098 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.3 | rmse_smooth_h1 | last_slope | 0.042 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.3 | rmse_smooth_h1 | persistence | 0.033 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.3 | rmse_smooth_h10 | last_slope | 0.391 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.3 | rmse_smooth_h10 | persistence | 0.215 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.3 | rmse_smooth_h100 | last_slope | 3.777 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.3 | rmse_smooth_h100 | persistence | 2.597 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.3 | rmse_smooth_h200 | last_slope | 7.595 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.3 | rmse_smooth_h200 | persistence | 3.458 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.3 | rmse_smooth_h50 | last_slope | 1.827 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.3 | rmse_smooth_h50 | persistence | 1.101 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.5 | mae_h1 | last_slope | 0.053 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.5 | mae_h1 | persistence | 0.033 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.5 | mae_h10 | last_slope | 0.312 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.5 | mae_h10 | persistence | 0.160 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.5 | mae_h100 | last_slope | 2.997 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.5 | mae_h100 | persistence | 1.779 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.5 | mae_h200 | last_slope | 8.282 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.5 | mae_h200 | persistence | 6.269 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.5 | mae_h50 | last_slope | 1.439 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.5 | mae_h50 | persistence | 0.851 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.5 | rmse_h1 | last_slope | 0.125 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.5 | rmse_h1 | persistence | 0.062 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.5 | rmse_h10 | last_slope | 1.068 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.5 | rmse_h10 | persistence | 0.259 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.5 | rmse_h100 | last_slope | 10.750 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.5 | rmse_h100 | persistence | 2.037 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.5 | rmse_h200 | last_slope | 22.423 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.5 | rmse_h200 | persistence | 7.228 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.5 | rmse_h50 | last_slope | 5.305 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.5 | rmse_h50 | persistence | 1.373 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.5 | rmse_smooth_h1 | last_slope | 0.112 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.5 | rmse_smooth_h1 | persistence | 0.029 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.5 | rmse_smooth_h10 | last_slope | 1.067 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.5 | rmse_smooth_h10 | persistence | 0.257 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.5 | rmse_smooth_h100 | last_slope | 10.754 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.5 | rmse_smooth_h100 | persistence | 2.041 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.5 | rmse_smooth_h200 | last_slope | 22.423 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.5 | rmse_smooth_h200 | persistence | 7.229 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.5 | rmse_smooth_h50 | last_slope | 5.305 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.5 | rmse_smooth_h50 | persistence | 1.371 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.7 | mae_h1 | last_slope | 0.056 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.7 | mae_h1 | persistence | 0.062 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.7 | mae_h10 | last_slope | 0.120 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.7 | mae_h10 | persistence | 0.366 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.7 | mae_h100 | last_slope | 2.597 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.7 | mae_h100 | persistence | 5.192 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.7 | mae_h200 | last_slope | 4.960 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.7 | mae_h200 | persistence | 8.965 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.7 | mae_h50 | last_slope | 0.580 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.7 | mae_h50 | persistence | 1.975 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.7 | rmse_h1 | last_slope | 0.109 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.7 | rmse_h1 | persistence | 0.108 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.7 | rmse_h10 | last_slope | 0.344 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.7 | rmse_h10 | persistence | 0.465 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.7 | rmse_h100 | last_slope | 3.304 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.7 | rmse_h100 | persistence | 5.651 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.7 | rmse_h200 | last_slope | 5.384 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.7 | rmse_h200 | persistence | 9.696 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.7 | rmse_h50 | last_slope | 0.920 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.7 | rmse_h50 | persistence | 2.341 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.7 | rmse_smooth_h1 | last_slope | 0.092 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.7 | rmse_smooth_h1 | persistence | 0.092 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.7 | rmse_smooth_h10 | last_slope | 0.205 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.7 | rmse_smooth_h10 | persistence | 0.399 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.7 | rmse_smooth_h100 | last_slope | 3.305 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.7 | rmse_smooth_h100 | persistence | 5.653 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.7 | rmse_smooth_h200 | last_slope | 5.384 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.7 | rmse_smooth_h200 | persistence | 9.697 |  | 1 | 1 | 85a8557f |
| test1 | start_points | frac:0.7 | rmse_smooth_h50 | last_slope | 0.922 |  | 1 | 1 | 77403933 |
| test1 | start_points | frac:0.7 | rmse_smooth_h50 | persistence | 2.345 |  | 1 | 1 | 85a8557f |
| test1 | start_points | overall | mae_h1 | last_slope | 0.036 |  | 1 | 1 | 77403933 |
| test1 | start_points | overall | mae_h1 | persistence | 0.032 |  | 1 | 1 | 85a8557f |
| test1 | start_points | overall | mae_h10 | last_slope | 0.145 |  | 1 | 1 | 77403933 |
| test1 | start_points | overall | mae_h10 | persistence | 0.192 |  | 1 | 1 | 85a8557f |
| test1 | start_points | overall | mae_h100 | last_slope | 1.764 |  | 1 | 1 | 77403933 |
| test1 | start_points | overall | mae_h100 | persistence | 2.312 |  | 1 | 1 | 85a8557f |
| test1 | start_points | overall | mae_h200 | last_slope | 4.072 |  | 1 | 1 | 77403933 |
| test1 | start_points | overall | mae_h200 | persistence | 4.354 |  | 1 | 1 | 85a8557f |
| test1 | start_points | overall | mae_h50 | last_slope | 0.668 |  | 1 | 1 | 77403933 |
| test1 | start_points | overall | mae_h50 | persistence | 1.004 |  | 1 | 1 | 85a8557f |
| test1 | start_points | overall | rmse_h1 | last_slope | 0.086 |  | 1 | 1 | 77403933 |
| test1 | start_points | overall | rmse_h1 | persistence | 0.066 |  | 1 | 1 | 85a8557f |
| test1 | start_points | overall | rmse_h10 | last_slope | 0.601 |  | 1 | 1 | 77403933 |
| test1 | start_points | overall | rmse_h10 | persistence | 0.317 |  | 1 | 1 | 85a8557f |
| test1 | start_points | overall | rmse_h100 | last_slope | 5.937 |  | 1 | 1 | 77403933 |
| test1 | start_points | overall | rmse_h100 | persistence | 3.325 |  | 1 | 1 | 85a8557f |
| test1 | start_points | overall | rmse_h200 | last_slope | 12.850 |  | 1 | 1 | 77403933 |
| test1 | start_points | overall | rmse_h200 | persistence | 5.683 |  | 1 | 1 | 85a8557f |
| test1 | start_points | overall | rmse_h50 | last_slope | 2.840 |  | 1 | 1 | 77403933 |
| test1 | start_points | overall | rmse_h50 | persistence | 1.630 |  | 1 | 1 | 85a8557f |
| test1 | start_points | overall | rmse_smooth_h1 | last_slope | 0.076 |  | 1 | 1 | 77403933 |
| test1 | start_points | overall | rmse_smooth_h1 | persistence | 0.052 |  | 1 | 1 | 85a8557f |
| test1 | start_points | overall | rmse_smooth_h10 | last_slope | 0.578 |  | 1 | 1 | 77403933 |
| test1 | start_points | overall | rmse_smooth_h10 | persistence | 0.289 |  | 1 | 1 | 85a8557f |
| test1 | start_points | overall | rmse_smooth_h100 | last_slope | 5.927 |  | 1 | 1 | 77403933 |
| test1 | start_points | overall | rmse_smooth_h100 | persistence | 3.325 |  | 1 | 1 | 85a8557f |
| test1 | start_points | overall | rmse_smooth_h200 | last_slope | 12.890 |  | 1 | 1 | 77403933 |
| test1 | start_points | overall | rmse_smooth_h200 | persistence | 5.685 |  | 1 | 1 | 85a8557f |
| test1 | start_points | overall | rmse_smooth_h50 | last_slope | 2.849 |  | 1 | 1 | 77403933 |
| test1 | start_points | overall | rmse_smooth_h50 | persistence | 1.632 |  | 1 | 1 | 85a8557f |
| test2 | all | overall | mae_h1 | last_slope | 0.008 |  | 1 | 1 | 77403933 |
| test2 | all | overall | mae_h1 | persistence | 0.021 |  | 1 | 1 | 85a8557f |
| test2 | all | overall | mae_h10 | last_slope | 0.029 |  | 1 | 1 | 77403933 |
| test2 | all | overall | mae_h10 | persistence | 0.170 |  | 1 | 1 | 85a8557f |
| test2 | all | overall | mae_h100 | last_slope | 0.520 |  | 1 | 1 | 77403933 |
| test2 | all | overall | mae_h100 | persistence | 1.415 |  | 1 | 1 | 85a8557f |
| test2 | all | overall | mae_h200 | last_slope | 1.261 |  | 1 | 1 | 77403933 |
| test2 | all | overall | mae_h200 | persistence | 2.436 |  | 1 | 1 | 85a8557f |
| test2 | all | overall | mae_h50 | last_slope | 0.199 |  | 1 | 1 | 77403933 |
| test2 | all | overall | mae_h50 | persistence | 0.778 |  | 1 | 1 | 85a8557f |
| test2 | all | overall | rmse_h1 | last_slope | 0.020 |  | 1 | 1 | 77403933 |
| test2 | all | overall | rmse_h1 | persistence | 0.036 |  | 1 | 1 | 85a8557f |
| test2 | all | overall | rmse_h10 | last_slope | 0.058 |  | 1 | 1 | 77403933 |
| test2 | all | overall | rmse_h10 | persistence | 0.295 |  | 1 | 1 | 85a8557f |
| test2 | all | overall | rmse_h100 | last_slope | 1.015 |  | 1 | 1 | 77403933 |
| test2 | all | overall | rmse_h100 | persistence | 2.272 |  | 1 | 1 | 85a8557f |
| test2 | all | overall | rmse_h200 | last_slope | 2.268 |  | 1 | 1 | 77403933 |
| test2 | all | overall | rmse_h200 | persistence | 3.572 |  | 1 | 1 | 85a8557f |
| test2 | all | overall | rmse_h50 | last_slope | 0.391 |  | 1 | 1 | 77403933 |
| test2 | all | overall | rmse_h50 | persistence | 1.314 |  | 1 | 1 | 85a8557f |
| test2 | all | overall | rmse_smooth_h1 | last_slope | 0.015 |  | 1 | 1 | 77403933 |
| test2 | all | overall | rmse_smooth_h1 | persistence | 0.033 |  | 1 | 1 | 85a8557f |
| test2 | all | overall | rmse_smooth_h10 | last_slope | 0.057 |  | 1 | 1 | 77403933 |
| test2 | all | overall | rmse_smooth_h10 | persistence | 0.294 |  | 1 | 1 | 85a8557f |
| test2 | all | overall | rmse_smooth_h100 | last_slope | 1.015 |  | 1 | 1 | 77403933 |
| test2 | all | overall | rmse_smooth_h100 | persistence | 2.272 |  | 1 | 1 | 85a8557f |
| test2 | all | overall | rmse_smooth_h200 | last_slope | 2.267 |  | 1 | 1 | 77403933 |
| test2 | all | overall | rmse_smooth_h200 | persistence | 3.571 |  | 1 | 1 | 85a8557f |
| test2 | all | overall | rmse_smooth_h50 | last_slope | 0.390 |  | 1 | 1 | 77403933 |
| test2 | all | overall | rmse_smooth_h50 | persistence | 1.313 |  | 1 | 1 | 85a8557f |
| test2 | start_points | fixed:100 | mae_h1 | last_slope | 0.010 |  | 1 | 1 | 77403933 |
| test2 | start_points | fixed:100 | mae_h1 | persistence | 0.011 |  | 1 | 1 | 85a8557f |
| test2 | start_points | fixed:100 | mae_h10 | last_slope | 0.034 |  | 1 | 1 | 77403933 |
| test2 | start_points | fixed:100 | mae_h10 | persistence | 0.045 |  | 1 | 1 | 85a8557f |
| test2 | start_points | fixed:100 | mae_h100 | last_slope | 0.204 |  | 1 | 1 | 77403933 |
| test2 | start_points | fixed:100 | mae_h100 | persistence | 0.440 |  | 1 | 1 | 85a8557f |
| test2 | start_points | fixed:100 | mae_h200 | last_slope | 0.386 |  | 1 | 1 | 77403933 |
| test2 | start_points | fixed:100 | mae_h200 | persistence | 0.961 |  | 1 | 1 | 85a8557f |
| test2 | start_points | fixed:100 | mae_h50 | last_slope | 0.121 |  | 1 | 1 | 77403933 |
| test2 | start_points | fixed:100 | mae_h50 | persistence | 0.194 |  | 1 | 1 | 85a8557f |
| test2 | start_points | fixed:100 | rmse_h1 | last_slope | 0.026 |  | 1 | 1 | 77403933 |
| test2 | start_points | fixed:100 | rmse_h1 | persistence | 0.024 |  | 1 | 1 | 85a8557f |
| test2 | start_points | fixed:100 | rmse_h10 | last_slope | 0.055 |  | 1 | 1 | 77403933 |
| test2 | start_points | fixed:100 | rmse_h10 | persistence | 0.069 |  | 1 | 1 | 85a8557f |
| test2 | start_points | fixed:100 | rmse_h100 | last_slope | 0.272 |  | 1 | 1 | 77403933 |
| test2 | start_points | fixed:100 | rmse_h100 | persistence | 0.615 |  | 1 | 1 | 85a8557f |
| test2 | start_points | fixed:100 | rmse_h200 | last_slope | 0.510 |  | 1 | 1 | 77403933 |
| test2 | start_points | fixed:100 | rmse_h200 | persistence | 1.266 |  | 1 | 1 | 85a8557f |
| test2 | start_points | fixed:100 | rmse_h50 | last_slope | 0.163 |  | 1 | 1 | 77403933 |
| test2 | start_points | fixed:100 | rmse_h50 | persistence | 0.298 |  | 1 | 1 | 85a8557f |
| test2 | start_points | fixed:100 | rmse_smooth_h1 | last_slope | 0.028 |  | 1 | 1 | 77403933 |
| test2 | start_points | fixed:100 | rmse_smooth_h1 | persistence | 0.026 |  | 1 | 1 | 85a8557f |
| test2 | start_points | fixed:100 | rmse_smooth_h10 | last_slope | 0.052 |  | 1 | 1 | 77403933 |
| test2 | start_points | fixed:100 | rmse_smooth_h10 | persistence | 0.066 |  | 1 | 1 | 85a8557f |
| test2 | start_points | fixed:100 | rmse_smooth_h100 | last_slope | 0.277 |  | 1 | 1 | 77403933 |
| test2 | start_points | fixed:100 | rmse_smooth_h100 | persistence | 0.616 |  | 1 | 1 | 85a8557f |
| test2 | start_points | fixed:100 | rmse_smooth_h200 | last_slope | 0.509 |  | 1 | 1 | 77403933 |
| test2 | start_points | fixed:100 | rmse_smooth_h200 | persistence | 1.264 |  | 1 | 1 | 85a8557f |
| test2 | start_points | fixed:100 | rmse_smooth_h50 | last_slope | 0.163 |  | 1 | 1 | 77403933 |
| test2 | start_points | fixed:100 | rmse_smooth_h50 | persistence | 0.298 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.3 | mae_h1 | last_slope | 0.015 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.3 | mae_h1 | persistence | 0.017 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.3 | mae_h10 | last_slope | 0.018 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.3 | mae_h10 | persistence | 0.060 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.3 | mae_h100 | last_slope | 0.131 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.3 | mae_h100 | persistence | 0.577 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.3 | mae_h200 | last_slope | 0.317 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.3 | mae_h200 | persistence | 1.260 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.3 | mae_h50 | last_slope | 0.074 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.3 | mae_h50 | persistence | 0.295 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.3 | rmse_h1 | last_slope | 0.036 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.3 | rmse_h1 | persistence | 0.037 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.3 | rmse_h10 | last_slope | 0.026 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.3 | rmse_h10 | persistence | 0.075 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.3 | rmse_h100 | last_slope | 0.173 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.3 | rmse_h100 | persistence | 0.686 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.3 | rmse_h200 | last_slope | 0.413 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.3 | rmse_h200 | persistence | 1.482 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.3 | rmse_h50 | last_slope | 0.108 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.3 | rmse_h50 | persistence | 0.357 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.3 | rmse_smooth_h1 | last_slope | 0.021 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.3 | rmse_smooth_h1 | persistence | 0.021 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.3 | rmse_smooth_h10 | last_slope | 0.026 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.3 | rmse_smooth_h10 | persistence | 0.075 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.3 | rmse_smooth_h100 | last_slope | 0.170 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.3 | rmse_smooth_h100 | persistence | 0.683 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.3 | rmse_smooth_h200 | last_slope | 0.413 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.3 | rmse_smooth_h200 | persistence | 1.482 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.3 | rmse_smooth_h50 | last_slope | 0.108 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.3 | rmse_smooth_h50 | persistence | 0.357 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.5 | mae_h1 | last_slope | 0.010 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.5 | mae_h1 | persistence | 0.013 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.5 | mae_h10 | last_slope | 0.029 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.5 | mae_h10 | persistence | 0.075 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.5 | mae_h100 | last_slope | 0.241 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.5 | mae_h100 | persistence | 0.823 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.5 | mae_h200 | last_slope | 0.734 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.5 | mae_h200 | persistence | 2.027 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.5 | mae_h50 | last_slope | 0.105 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.5 | mae_h50 | persistence | 0.377 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.5 | rmse_h1 | last_slope | 0.023 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.5 | rmse_h1 | persistence | 0.022 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.5 | rmse_h10 | last_slope | 0.045 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.5 | rmse_h10 | persistence | 0.085 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.5 | rmse_h100 | last_slope | 0.329 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.5 | rmse_h100 | persistence | 0.926 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.5 | rmse_h200 | last_slope | 0.942 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.5 | rmse_h200 | persistence | 2.305 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.5 | rmse_h50 | last_slope | 0.160 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.5 | rmse_h50 | persistence | 0.424 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.5 | rmse_smooth_h1 | last_slope | 0.019 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.5 | rmse_smooth_h1 | persistence | 0.019 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.5 | rmse_smooth_h10 | last_slope | 0.044 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.5 | rmse_smooth_h10 | persistence | 0.082 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.5 | rmse_smooth_h100 | last_slope | 0.329 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.5 | rmse_smooth_h100 | persistence | 0.926 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.5 | rmse_smooth_h200 | last_slope | 0.938 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.5 | rmse_smooth_h200 | persistence | 2.300 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.5 | rmse_smooth_h50 | last_slope | 0.160 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.5 | rmse_smooth_h50 | persistence | 0.424 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.7 | mae_h1 | last_slope | 0.008 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.7 | mae_h1 | persistence | 0.017 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.7 | mae_h10 | last_slope | 0.016 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.7 | mae_h10 | persistence | 0.137 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.7 | mae_h100 | last_slope | 0.552 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.7 | mae_h100 | persistence | 1.851 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.7 | mae_h200 | last_slope | 3.641 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.7 | mae_h200 | persistence | 6.059 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.7 | mae_h50 | last_slope | 0.125 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.7 | mae_h50 | persistence | 0.771 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.7 | rmse_h1 | last_slope | 0.020 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.7 | rmse_h1 | persistence | 0.026 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.7 | rmse_h10 | last_slope | 0.022 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.7 | rmse_h10 | persistence | 0.150 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.7 | rmse_h100 | last_slope | 0.624 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.7 | rmse_h100 | persistence | 2.002 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.7 | rmse_h200 | last_slope | 4.062 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.7 | rmse_h200 | persistence | 6.529 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.7 | rmse_h50 | last_slope | 0.154 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.7 | rmse_h50 | persistence | 0.838 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.7 | rmse_smooth_h1 | last_slope | 0.006 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.7 | rmse_smooth_h1 | persistence | 0.017 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.7 | rmse_smooth_h10 | last_slope | 0.021 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.7 | rmse_smooth_h10 | persistence | 0.150 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.7 | rmse_smooth_h100 | last_slope | 0.624 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.7 | rmse_smooth_h100 | persistence | 2.002 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.7 | rmse_smooth_h200 | last_slope | 4.062 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.7 | rmse_smooth_h200 | persistence | 6.529 |  | 1 | 1 | 85a8557f |
| test2 | start_points | frac:0.7 | rmse_smooth_h50 | last_slope | 0.154 |  | 1 | 1 | 77403933 |
| test2 | start_points | frac:0.7 | rmse_smooth_h50 | persistence | 0.838 |  | 1 | 1 | 85a8557f |
| test2 | start_points | overall | mae_h1 | last_slope | 0.011 |  | 1 | 1 | 77403933 |
| test2 | start_points | overall | mae_h1 | persistence | 0.014 |  | 1 | 1 | 85a8557f |
| test2 | start_points | overall | mae_h10 | last_slope | 0.025 |  | 1 | 1 | 77403933 |
| test2 | start_points | overall | mae_h10 | persistence | 0.079 |  | 1 | 1 | 85a8557f |
| test2 | start_points | overall | mae_h100 | last_slope | 0.282 |  | 1 | 1 | 77403933 |
| test2 | start_points | overall | mae_h100 | persistence | 0.923 |  | 1 | 1 | 85a8557f |
| test2 | start_points | overall | mae_h200 | last_slope | 1.240 |  | 1 | 1 | 77403933 |
| test2 | start_points | overall | mae_h200 | persistence | 2.533 |  | 1 | 1 | 85a8557f |
| test2 | start_points | overall | mae_h50 | last_slope | 0.107 |  | 1 | 1 | 77403933 |
| test2 | start_points | overall | mae_h50 | persistence | 0.409 |  | 1 | 1 | 85a8557f |
| test2 | start_points | overall | rmse_h1 | last_slope | 0.027 |  | 1 | 1 | 77403933 |
| test2 | start_points | overall | rmse_h1 | persistence | 0.028 |  | 1 | 1 | 85a8557f |
| test2 | start_points | overall | rmse_h10 | last_slope | 0.039 |  | 1 | 1 | 77403933 |
| test2 | start_points | overall | rmse_h10 | persistence | 0.100 |  | 1 | 1 | 85a8557f |
| test2 | start_points | overall | rmse_h100 | last_slope | 0.388 |  | 1 | 1 | 77403933 |
| test2 | start_points | overall | rmse_h100 | persistence | 1.195 |  | 1 | 1 | 85a8557f |
| test2 | start_points | overall | rmse_h200 | last_slope | 2.074 |  | 1 | 1 | 77403933 |
| test2 | start_points | overall | rmse_h200 | persistence | 3.544 |  | 1 | 1 | 85a8557f |
| test2 | start_points | overall | rmse_h50 | last_slope | 0.148 |  | 1 | 1 | 77403933 |
| test2 | start_points | overall | rmse_h50 | persistence | 0.524 |  | 1 | 1 | 85a8557f |
| test2 | start_points | overall | rmse_smooth_h1 | last_slope | 0.020 |  | 1 | 1 | 77403933 |
| test2 | start_points | overall | rmse_smooth_h1 | persistence | 0.021 |  | 1 | 1 | 85a8557f |
| test2 | start_points | overall | rmse_smooth_h10 | last_slope | 0.038 |  | 1 | 1 | 77403933 |
| test2 | start_points | overall | rmse_smooth_h10 | persistence | 0.099 |  | 1 | 1 | 85a8557f |
| test2 | start_points | overall | rmse_smooth_h100 | last_slope | 0.388 |  | 1 | 1 | 77403933 |
| test2 | start_points | overall | rmse_smooth_h100 | persistence | 1.195 |  | 1 | 1 | 85a8557f |
| test2 | start_points | overall | rmse_smooth_h200 | last_slope | 2.074 |  | 1 | 1 | 77403933 |
| test2 | start_points | overall | rmse_smooth_h200 | persistence | 3.543 |  | 1 | 1 | 85a8557f |
| test2 | start_points | overall | rmse_smooth_h50 | last_slope | 0.148 |  | 1 | 1 | 77403933 |
| test2 | start_points | overall | rmse_smooth_h50 | persistence | 0.524 |  | 1 | 1 | 85a8557f |

</details>
