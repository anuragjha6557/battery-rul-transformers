# Benchmark tables: abl_norm_loss

- Protocol version: 1.1
- Git SHA: fa6ae83c62
- Seeds: 5  |  unit runs: 270
- Note: n = 4 cells per NASA/CALCE dataset, so the 95 % cluster-bootstrap CI is wide by construction. Toyota rows are over test cells (test1 / test2 separately) with a cell-level bootstrap CI and a Holm-adjusted Wilcoxon p vs the best baseline. All metrics are computed per cell from the logged predictions.

## Headline (kind = overall; RMSE in %SOH, RUL MAE in cycles)

### calce_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | itransformer[loss=huber] | 1.947 [1.838, 2.056] |  |  | 4 | 5 | 41d648c8 |
| loco | all | overall | rmse_h1 | itransformer[loss=mse] | 1.939 [1.838, 2.040] |  |  | 4 | 5 | d4824fbc |
| loco | all | overall | rmse_h1 | lstm[quantiles=None,loss=huber] | 2.439 [2.269, 2.617] |  |  | 4 | 5 | 4e98b269 |
| loco | all | overall | rmse_h1 | lstm[quantiles=None,loss=mse] | 2.047 [1.927, 2.169] |  |  | 4 | 5 | ba6a435e |
| loco | all | overall | rmse_h1 | lstm[revin=True] | 2.274 [2.106, 2.441] |  |  | 4 | 5 | 0a2e3a80 |
| loco | all | overall | rmse_h1 | transformer | 1.959 [1.848, 2.071] |  |  | 4 | 5 | dc16fbab |
| loco | all | overall | rmse_h10 | itransformer[loss=huber] | 2.308 [2.220, 2.403] |  |  | 4 | 5 | 41d648c8 |
| loco | all | overall | rmse_h10 | itransformer[loss=mse] | 2.306 [2.220, 2.392] |  |  | 4 | 5 | d4824fbc |
| loco | all | overall | rmse_h10 | lstm[quantiles=None,loss=huber] | 2.728 [2.662, 2.797] |  |  | 4 | 5 | 4e98b269 |
| loco | all | overall | rmse_h10 | lstm[quantiles=None,loss=mse] | 2.431 [2.285, 2.590] |  |  | 4 | 5 | ba6a435e |
| loco | all | overall | rmse_h10 | lstm[revin=True] | 2.612 [2.564, 2.665] |  |  | 4 | 5 | 0a2e3a80 |
| loco | all | overall | rmse_h10 | transformer | 2.324 [2.273, 2.399] |  |  | 4 | 5 | dc16fbab |
| loco | all | overall | rmse_h50 | itransformer[loss=huber] | 3.191 [2.933, 3.450] |  |  | 4 | 5 | 41d648c8 |
| loco | all | overall | rmse_h50 | itransformer[loss=mse] | 3.222 [2.936, 3.509] |  |  | 4 | 5 | d4824fbc |
| loco | all | overall | rmse_h50 | lstm[quantiles=None,loss=huber] | 3.492 [3.224, 3.761] |  |  | 4 | 5 | 4e98b269 |
| loco | all | overall | rmse_h50 | lstm[quantiles=None,loss=mse] | 3.433 [2.683, 4.222] |  |  | 4 | 5 | ba6a435e |
| loco | all | overall | rmse_h50 | lstm[revin=True] | 3.689 [3.422, 3.956] |  |  | 4 | 5 | 0a2e3a80 |
| loco | all | overall | rmse_h50 | transformer | 3.755 [3.524, 4.007] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | overall | rmse_h1 | itransformer[loss=huber] | 0.399 [0.238, 0.559] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | overall | rmse_h1 | itransformer[loss=mse] | 0.502 [0.357, 0.646] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | overall | rmse_h1 | lstm[quantiles=None,loss=huber] | 0.395 [0.213, 0.578] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | overall | rmse_h1 | lstm[quantiles=None,loss=mse] | 0.548 [0.406, 0.768] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | overall | rmse_h1 | lstm[revin=True] | 0.395 [0.183, 0.607] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | overall | rmse_h1 | transformer | 0.406 [0.221, 0.591] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | overall | rmse_h10 | itransformer[loss=huber] | 1.018 [0.665, 1.535] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | overall | rmse_h10 | itransformer[loss=mse] | 0.983 [0.601, 1.561] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | overall | rmse_h10 | lstm[quantiles=None,loss=huber] | 1.067 [0.744, 1.586] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | overall | rmse_h10 | lstm[quantiles=None,loss=mse] | 1.042 [0.668, 1.549] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | overall | rmse_h10 | lstm[revin=True] | 1.156 [0.862, 1.624] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | overall | rmse_h10 | transformer | 1.035 [0.646, 1.559] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | overall | rmse_h50 | itransformer[loss=huber] | 1.491 [0.928, 2.084] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | overall | rmse_h50 | itransformer[loss=mse] | 1.548 [0.968, 2.147] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | overall | rmse_h50 | lstm[quantiles=None,loss=huber] | 1.532 [1.031, 2.007] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | overall | rmse_h50 | lstm[quantiles=None,loss=mse] | 1.943 [1.250, 2.608] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | overall | rmse_h50 | lstm[revin=True] | 1.676 [1.114, 2.267] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | overall | rmse_h50 | transformer | 1.682 [1.359, 2.029] |  |  | 4 | 5 | dc16fbab |

### nasa_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | itransformer[loss=huber] | 0.911 [0.655, 1.167] |  | 1.221 | 4 | 5 | ceba4eba |
| loco | all | overall | rmse_h1 | itransformer[loss=mse] | 0.907 [0.648, 1.166] |  | 1.210 | 4 | 5 | bab8bc6a |
| loco | all | overall | rmse_h1 | lstm[quantiles=None,loss=huber] | 1.168 [0.843, 1.493] |  | 1.533 | 4 | 5 | a556b7e5 |
| loco | all | overall | rmse_h1 | lstm[quantiles=None,loss=mse] | 2.382 [1.823, 3.015] |  | 2.541 | 4 | 5 | 97861f32 |
| loco | all | overall | rmse_h1 | lstm[revin=True] | 0.933 [0.686, 1.180] |  | 1.223 | 4 | 5 | c17ed23c |
| loco | all | overall | rmse_h1 | transformer | 0.925 [0.676, 1.175] |  | 1.217 | 4 | 5 | 20605e71 |
| loco | all | overall | rmse_h10 | itransformer[loss=huber] | 1.678 [1.068, 2.288] |  | 2.532 | 4 | 5 | ceba4eba |
| loco | all | overall | rmse_h10 | itransformer[loss=mse] | 1.681 [1.080, 2.283] |  | 2.426 | 4 | 5 | bab8bc6a |
| loco | all | overall | rmse_h10 | lstm[quantiles=None,loss=huber] | 2.762 [1.927, 3.597] |  | 3.282 | 4 | 5 | a556b7e5 |
| loco | all | overall | rmse_h10 | lstm[quantiles=None,loss=mse] | 4.632 [3.379, 6.000] |  | 5.010 | 4 | 5 | 97861f32 |
| loco | all | overall | rmse_h10 | lstm[revin=True] | 1.779 [1.244, 2.314] |  | 2.347 | 4 | 5 | c17ed23c |
| loco | all | overall | rmse_h10 | transformer | 1.684 [1.152, 2.216] |  | 2.311 | 4 | 5 | 20605e71 |
| loco | all | overall | rmse_h50 | itransformer[loss=huber] | 4.706 [4.584, 4.859] |  | 4.577 | 4 | 5 | ceba4eba |
| loco | all | overall | rmse_h50 | itransformer[loss=mse] | 4.795 [4.718, 4.915] |  | 4.702 | 4 | 5 | bab8bc6a |
| loco | all | overall | rmse_h50 | lstm[quantiles=None,loss=huber] | 3.579 [2.724, 4.580] |  | 2.717 | 4 | 5 | a556b7e5 |
| loco | all | overall | rmse_h50 | lstm[quantiles=None,loss=mse] | 5.052 [3.659, 6.900] |  | 3.336 | 4 | 5 | 97861f32 |
| loco | all | overall | rmse_h50 | lstm[revin=True] | 4.353 [3.983, 4.837] |  | 3.974 | 4 | 5 | c17ed23c |
| loco | all | overall | rmse_h50 | transformer | 3.693 [3.274, 4.237] |  | 4.511 | 4 | 5 | 20605e71 |
| loco | start_points | overall | rmse_h1 | itransformer[loss=huber] | 1.846 [1.096, 2.597] |  | 2.632 | 4 | 5 | ceba4eba |
| loco | start_points | overall | rmse_h1 | itransformer[loss=mse] | 1.780 [1.069, 2.491] |  | 2.506 | 4 | 5 | bab8bc6a |
| loco | start_points | overall | rmse_h1 | lstm[quantiles=None,loss=huber] | 1.759 [1.342, 2.173] |  | 1.950 | 4 | 5 | a556b7e5 |
| loco | start_points | overall | rmse_h1 | lstm[quantiles=None,loss=mse] | 2.576 [1.825, 3.334] |  | 2.544 | 4 | 5 | 97861f32 |
| loco | start_points | overall | rmse_h1 | lstm[revin=True] | 1.796 [1.110, 2.481] |  | 2.547 | 4 | 5 | c17ed23c |
| loco | start_points | overall | rmse_h1 | transformer | 1.819 [1.129, 2.508] |  | 2.518 | 4 | 5 | 20605e71 |
| loco | start_points | overall | rmse_h10 | itransformer[loss=huber] | 1.764 [1.038, 2.792] |  | 3.377 | 4 | 5 | ceba4eba |
| loco | start_points | overall | rmse_h10 | itransformer[loss=mse] | 1.814 [1.127, 2.710] |  | 3.206 | 4 | 5 | bab8bc6a |
| loco | start_points | overall | rmse_h10 | lstm[quantiles=None,loss=huber] | 2.588 [1.625, 3.550] |  | 3.527 | 4 | 5 | a556b7e5 |
| loco | start_points | overall | rmse_h10 | lstm[quantiles=None,loss=mse] | 4.596 [3.264, 6.029] |  | 4.906 | 4 | 5 | 97861f32 |
| loco | start_points | overall | rmse_h10 | lstm[revin=True] | 1.880 [1.200, 2.559] |  | 2.879 | 4 | 5 | c17ed23c |
| loco | start_points | overall | rmse_h10 | transformer | 1.888 [1.188, 2.588] |  | 2.772 | 4 | 5 | 20605e71 |
| loco | start_points | overall | rmse_h50 | itransformer[loss=huber] | 4.515 [2.674, 6.357] |  | 2.057 | 4 | 5 | ceba4eba |
| loco | start_points | overall | rmse_h50 | itransformer[loss=mse] | 4.664 [2.847, 6.480] |  | 2.557 | 4 | 5 | bab8bc6a |
| loco | start_points | overall | rmse_h50 | lstm[quantiles=None,loss=huber] | 3.490 [2.211, 5.231] |  | 3.196 | 4 | 5 | a556b7e5 |
| loco | start_points | overall | rmse_h50 | lstm[quantiles=None,loss=mse] | 5.075 [3.777, 6.569] |  | 3.228 | 4 | 5 | 97861f32 |
| loco | start_points | overall | rmse_h50 | lstm[revin=True] | 4.946 [3.590, 6.188] |  | 2.726 | 4 | 5 | c17ed23c |
| loco | start_points | overall | rmse_h50 | transformer | 3.917 [3.179, 5.013] |  | 3.305 | 4 | 5 | 20605e71 |

### toyota_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rmse_h1 | itransformer[loss=huber] | 0.127 [0.075, 0.187] |  |  | 43 | 5 | 8b749e84 |
| test1 | all | overall | rmse_h1 | itransformer[loss=mse] | 0.128 [0.076, 0.189] |  |  | 43 | 5 | 34919877 |
| test1 | all | overall | rmse_h1 | lstm[quantiles=None,loss=huber] | 0.218 [0.168, 0.274] |  |  | 43 | 5 | f7c2b05c |
| test1 | all | overall | rmse_h1 | lstm[quantiles=None,loss=mse] | 0.242 [0.191, 0.299] |  |  | 43 | 5 | 7ddb85ea |
| test1 | all | overall | rmse_h1 | lstm[revin=True] | 0.134 [0.079, 0.197] |  |  | 43 | 5 | 61016dbc |
| test1 | all | overall | rmse_h1 | transformer | 0.137 [0.081, 0.203] |  |  | 43 | 5 | f64a10ee |
| test1 | all | overall | rmse_h10 | itransformer[loss=huber] | 0.170 [0.116, 0.233] |  |  | 43 | 5 | 8b749e84 |
| test1 | all | overall | rmse_h10 | itransformer[loss=mse] | 0.172 [0.119, 0.234] |  |  | 43 | 5 | 34919877 |
| test1 | all | overall | rmse_h10 | lstm[quantiles=None,loss=huber] | 0.235 [0.177, 0.300] |  |  | 43 | 5 | f7c2b05c |
| test1 | all | overall | rmse_h10 | lstm[quantiles=None,loss=mse] | 0.244 [0.192, 0.302] |  |  | 43 | 5 | 7ddb85ea |
| test1 | all | overall | rmse_h10 | lstm[revin=True] | 0.215 [0.156, 0.280] |  |  | 43 | 5 | 61016dbc |
| test1 | all | overall | rmse_h10 | transformer | 0.284 [0.198, 0.385] |  |  | 43 | 5 | f64a10ee |
| test1 | all | overall | rmse_h50 | itransformer[loss=huber] | 0.448 [0.351, 0.564] |  |  | 43 | 5 | 8b749e84 |
| test1 | all | overall | rmse_h50 | itransformer[loss=mse] | 0.454 [0.361, 0.566] |  |  | 43 | 5 | 34919877 |
| test1 | all | overall | rmse_h50 | lstm[quantiles=None,loss=huber] | 0.704 [0.565, 0.858] |  |  | 43 | 5 | f7c2b05c |
| test1 | all | overall | rmse_h50 | lstm[quantiles=None,loss=mse] | 0.576 [0.491, 0.668] |  |  | 43 | 5 | 7ddb85ea |
| test1 | all | overall | rmse_h50 | lstm[revin=True] | 0.914 [0.752, 1.086] |  |  | 43 | 5 | 61016dbc |
| test1 | all | overall | rmse_h50 | transformer | 1.764 [1.528, 2.016] |  |  | 43 | 5 | f64a10ee |
| test1 | start_points | overall | rmse_h1 | itransformer[loss=huber] | 0.043 [0.029, 0.060] |  |  | 43 | 5 | 8b749e84 |
| test1 | start_points | overall | rmse_h1 | itransformer[loss=mse] | 0.042 [0.029, 0.059] |  |  | 43 | 5 | 34919877 |
| test1 | start_points | overall | rmse_h1 | lstm[quantiles=None,loss=huber] | 0.155 [0.112, 0.212] |  |  | 43 | 5 | f7c2b05c |
| test1 | start_points | overall | rmse_h1 | lstm[quantiles=None,loss=mse] | 0.175 [0.124, 0.239] |  |  | 43 | 5 | 7ddb85ea |
| test1 | start_points | overall | rmse_h1 | lstm[revin=True] | 0.041 [0.027, 0.057] |  |  | 43 | 5 | 61016dbc |
| test1 | start_points | overall | rmse_h1 | transformer | 0.046 [0.029, 0.066] |  |  | 43 | 5 | f64a10ee |
| test1 | start_points | overall | rmse_h10 | itransformer[loss=huber] | 0.095 [0.059, 0.141] |  |  | 43 | 5 | 8b749e84 |
| test1 | start_points | overall | rmse_h10 | itransformer[loss=mse] | 0.094 [0.060, 0.140] |  |  | 43 | 5 | 34919877 |
| test1 | start_points | overall | rmse_h10 | lstm[quantiles=None,loss=huber] | 0.175 [0.117, 0.245] |  |  | 43 | 5 | f7c2b05c |
| test1 | start_points | overall | rmse_h10 | lstm[quantiles=None,loss=mse] | 0.175 [0.134, 0.222] |  |  | 43 | 5 | 7ddb85ea |
| test1 | start_points | overall | rmse_h10 | lstm[revin=True] | 0.117 [0.077, 0.163] |  |  | 43 | 5 | 61016dbc |
| test1 | start_points | overall | rmse_h10 | transformer | 0.257 [0.135, 0.409] |  |  | 43 | 5 | f64a10ee |
| test1 | start_points | overall | rmse_h50 | itransformer[loss=huber] | 0.292 [0.187, 0.425] |  |  | 43 | 5 | 8b749e84 |
| test1 | start_points | overall | rmse_h50 | itransformer[loss=mse] | 0.280 [0.186, 0.400] |  |  | 43 | 5 | 34919877 |
| test1 | start_points | overall | rmse_h50 | lstm[quantiles=None,loss=huber] | 0.474 [0.292, 0.743] |  |  | 43 | 5 | f7c2b05c |
| test1 | start_points | overall | rmse_h50 | lstm[quantiles=None,loss=mse] | 0.375 [0.288, 0.472] |  |  | 43 | 5 | 7ddb85ea |
| test1 | start_points | overall | rmse_h50 | lstm[revin=True] | 0.518 [0.374, 0.685] |  |  | 43 | 5 | 61016dbc |
| test1 | start_points | overall | rmse_h50 | transformer | 1.082 [0.717, 1.529] |  |  | 43 | 5 | f64a10ee |
| test2 | all | overall | rmse_h1 | itransformer[loss=huber] | 0.017 [0.015, 0.019] |  |  | 40 | 5 | 8b749e84 |
| test2 | all | overall | rmse_h1 | itransformer[loss=mse] | 0.016 [0.014, 0.019] |  |  | 40 | 5 | 34919877 |
| test2 | all | overall | rmse_h1 | lstm[quantiles=None,loss=huber] | 0.098 [0.092, 0.104] |  |  | 40 | 5 | f7c2b05c |
| test2 | all | overall | rmse_h1 | lstm[quantiles=None,loss=mse] | 0.159 [0.150, 0.168] |  |  | 40 | 5 | 7ddb85ea |
| test2 | all | overall | rmse_h1 | lstm[revin=True] | 0.017 [0.014, 0.020] |  |  | 40 | 5 | 61016dbc |
| test2 | all | overall | rmse_h1 | transformer | 0.018 [0.015, 0.021] |  |  | 40 | 5 | f64a10ee |
| test2 | all | overall | rmse_h10 | itransformer[loss=huber] | 0.041 [0.037, 0.046] |  |  | 40 | 5 | 8b749e84 |
| test2 | all | overall | rmse_h10 | itransformer[loss=mse] | 0.038 [0.034, 0.043] |  |  | 40 | 5 | 34919877 |
| test2 | all | overall | rmse_h10 | lstm[quantiles=None,loss=huber] | 0.088 [0.083, 0.095] |  |  | 40 | 5 | f7c2b05c |
| test2 | all | overall | rmse_h10 | lstm[quantiles=None,loss=mse] | 0.130 [0.122, 0.140] |  |  | 40 | 5 | 7ddb85ea |
| test2 | all | overall | rmse_h10 | lstm[revin=True] | 0.059 [0.053, 0.064] |  |  | 40 | 5 | 61016dbc |
| test2 | all | overall | rmse_h10 | transformer | 0.109 [0.105, 0.113] |  |  | 40 | 5 | f64a10ee |
| test2 | all | overall | rmse_h50 | itransformer[loss=huber] | 0.227 [0.194, 0.261] |  |  | 40 | 5 | 8b749e84 |
| test2 | all | overall | rmse_h50 | itransformer[loss=mse] | 0.214 [0.184, 0.244] |  |  | 40 | 5 | 34919877 |
| test2 | all | overall | rmse_h50 | lstm[quantiles=None,loss=huber] | 0.287 [0.259, 0.316] |  |  | 40 | 5 | f7c2b05c |
| test2 | all | overall | rmse_h50 | lstm[quantiles=None,loss=mse] | 0.382 [0.352, 0.413] |  |  | 40 | 5 | 7ddb85ea |
| test2 | all | overall | rmse_h50 | lstm[revin=True] | 0.385 [0.337, 0.435] |  |  | 40 | 5 | 61016dbc |
| test2 | all | overall | rmse_h50 | transformer | 0.866 [0.802, 0.927] |  |  | 40 | 5 | f64a10ee |
| test2 | start_points | overall | rmse_h1 | itransformer[loss=huber] | 0.013 [0.007, 0.020] |  |  | 40 | 5 | 8b749e84 |
| test2 | start_points | overall | rmse_h1 | itransformer[loss=mse] | 0.013 [0.008, 0.020] |  |  | 40 | 5 | 34919877 |
| test2 | start_points | overall | rmse_h1 | lstm[quantiles=None,loss=huber] | 0.068 [0.059, 0.077] |  |  | 40 | 5 | f7c2b05c |
| test2 | start_points | overall | rmse_h1 | lstm[quantiles=None,loss=mse] | 0.140 [0.130, 0.150] |  |  | 40 | 5 | 7ddb85ea |
| test2 | start_points | overall | rmse_h1 | lstm[revin=True] | 0.014 [0.008, 0.021] |  |  | 40 | 5 | 61016dbc |
| test2 | start_points | overall | rmse_h1 | transformer | 0.015 [0.009, 0.023] |  |  | 40 | 5 | f64a10ee |
| test2 | start_points | overall | rmse_h10 | itransformer[loss=huber] | 0.022 [0.017, 0.028] |  |  | 40 | 5 | 8b749e84 |
| test2 | start_points | overall | rmse_h10 | itransformer[loss=mse] | 0.023 [0.018, 0.030] |  |  | 40 | 5 | 34919877 |
| test2 | start_points | overall | rmse_h10 | lstm[quantiles=None,loss=huber] | 0.060 [0.054, 0.066] |  |  | 40 | 5 | f7c2b05c |
| test2 | start_points | overall | rmse_h10 | lstm[quantiles=None,loss=mse] | 0.094 [0.085, 0.103] |  |  | 40 | 5 | 7ddb85ea |
| test2 | start_points | overall | rmse_h10 | lstm[revin=True] | 0.031 [0.025, 0.038] |  |  | 40 | 5 | 61016dbc |
| test2 | start_points | overall | rmse_h10 | transformer | 0.111 [0.103, 0.120] |  |  | 40 | 5 | f64a10ee |
| test2 | start_points | overall | rmse_h50 | itransformer[loss=huber] | 0.070 [0.059, 0.084] |  |  | 40 | 5 | 8b749e84 |
| test2 | start_points | overall | rmse_h50 | itransformer[loss=mse] | 0.076 [0.061, 0.095] |  |  | 40 | 5 | 34919877 |
| test2 | start_points | overall | rmse_h50 | lstm[quantiles=None,loss=huber] | 0.129 [0.112, 0.148] |  |  | 40 | 5 | f7c2b05c |
| test2 | start_points | overall | rmse_h50 | lstm[quantiles=None,loss=mse] | 0.252 [0.231, 0.275] |  |  | 40 | 5 | 7ddb85ea |
| test2 | start_points | overall | rmse_h50 | lstm[revin=True] | 0.126 [0.116, 0.137] |  |  | 40 | 5 | 61016dbc |
| test2 | start_points | overall | rmse_h50 | transformer | 0.302 [0.273, 0.339] |  |  | 40 | 5 | f64a10ee |

## Mean rank (dataset x task x split x policy x headline metric)

| model | mean rank | conditions | missing |
|---|---|---|---|
| itransformer[loss=huber] | 1.96 | 24 | 0 |
| itransformer[loss=mse] | 2.00 | 24 | 0 |
| lstm[revin=True] | 3.62 | 24 | 0 |
| lstm[quantiles=None,loss=huber] | 3.96 | 24 | 0 |
| transformer | 4.38 | 24 | 0 |
| lstm[quantiles=None,loss=mse] | 5.08 | 24 | 0 |

## Full tables

<details><summary>calce_forecast (210 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | itransformer[loss=huber] | 1.947 [1.838, 2.056] |  |  | 4 | 5 | 41d648c8 |
| loco | all | overall | rmse_h1 | itransformer[loss=mse] | 1.939 [1.838, 2.040] |  |  | 4 | 5 | d4824fbc |
| loco | all | overall | rmse_h1 | lstm[quantiles=None,loss=huber] | 2.439 [2.269, 2.617] |  |  | 4 | 5 | 4e98b269 |
| loco | all | overall | rmse_h1 | lstm[quantiles=None,loss=mse] | 2.047 [1.927, 2.169] |  |  | 4 | 5 | ba6a435e |
| loco | all | overall | rmse_h1 | lstm[revin=True] | 2.274 [2.106, 2.441] |  |  | 4 | 5 | 0a2e3a80 |
| loco | all | overall | rmse_h1 | transformer | 1.959 [1.848, 2.071] |  |  | 4 | 5 | dc16fbab |
| loco | all | overall | rmse_h10 | itransformer[loss=huber] | 2.308 [2.220, 2.403] |  |  | 4 | 5 | 41d648c8 |
| loco | all | overall | rmse_h10 | itransformer[loss=mse] | 2.306 [2.220, 2.392] |  |  | 4 | 5 | d4824fbc |
| loco | all | overall | rmse_h10 | lstm[quantiles=None,loss=huber] | 2.728 [2.662, 2.797] |  |  | 4 | 5 | 4e98b269 |
| loco | all | overall | rmse_h10 | lstm[quantiles=None,loss=mse] | 2.431 [2.285, 2.590] |  |  | 4 | 5 | ba6a435e |
| loco | all | overall | rmse_h10 | lstm[revin=True] | 2.612 [2.564, 2.665] |  |  | 4 | 5 | 0a2e3a80 |
| loco | all | overall | rmse_h10 | transformer | 2.324 [2.273, 2.399] |  |  | 4 | 5 | dc16fbab |
| loco | all | overall | rmse_h100 | itransformer[loss=huber] | 3.921 [3.409, 4.432] |  |  | 4 | 5 | 41d648c8 |
| loco | all | overall | rmse_h100 | itransformer[loss=mse] | 3.943 [3.412, 4.475] |  |  | 4 | 5 | d4824fbc |
| loco | all | overall | rmse_h100 | lstm[quantiles=None,loss=huber] | 4.143 [3.640, 4.646] |  |  | 4 | 5 | 4e98b269 |
| loco | all | overall | rmse_h100 | lstm[quantiles=None,loss=mse] | 4.151 [3.110, 5.288] |  |  | 4 | 5 | ba6a435e |
| loco | all | overall | rmse_h100 | lstm[revin=True] | 4.952 [4.618, 5.286] |  |  | 4 | 5 | 0a2e3a80 |
| loco | all | overall | rmse_h100 | transformer | 5.453 [4.992, 6.023] |  |  | 4 | 5 | dc16fbab |
| loco | all | overall | rmse_h25 | itransformer[loss=huber] | 2.736 [2.547, 2.924] |  |  | 4 | 5 | 41d648c8 |
| loco | all | overall | rmse_h25 | itransformer[loss=mse] | 2.744 [2.528, 2.960] |  |  | 4 | 5 | d4824fbc |
| loco | all | overall | rmse_h25 | lstm[quantiles=None,loss=huber] | 3.110 [2.967, 3.259] |  |  | 4 | 5 | 4e98b269 |
| loco | all | overall | rmse_h25 | lstm[quantiles=None,loss=mse] | 2.908 [2.566, 3.285] |  |  | 4 | 5 | ba6a435e |
| loco | all | overall | rmse_h25 | lstm[revin=True] | 3.178 [3.074, 3.283] |  |  | 4 | 5 | 0a2e3a80 |
| loco | all | overall | rmse_h25 | transformer | 2.960 [2.818, 3.082] |  |  | 4 | 5 | dc16fbab |
| loco | all | overall | rmse_h50 | itransformer[loss=huber] | 3.191 [2.933, 3.450] |  |  | 4 | 5 | 41d648c8 |
| loco | all | overall | rmse_h50 | itransformer[loss=mse] | 3.222 [2.936, 3.509] |  |  | 4 | 5 | d4824fbc |
| loco | all | overall | rmse_h50 | lstm[quantiles=None,loss=huber] | 3.492 [3.224, 3.761] |  |  | 4 | 5 | 4e98b269 |
| loco | all | overall | rmse_h50 | lstm[quantiles=None,loss=mse] | 3.433 [2.683, 4.222] |  |  | 4 | 5 | ba6a435e |
| loco | all | overall | rmse_h50 | lstm[revin=True] | 3.689 [3.422, 3.956] |  |  | 4 | 5 | 0a2e3a80 |
| loco | all | overall | rmse_h50 | transformer | 3.755 [3.524, 4.007] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | fixed:200 | rmse_h1 | itransformer[loss=huber] | 0.248 [0.112, 0.328] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | fixed:200 | rmse_h1 | itransformer[loss=mse] | 0.236 [0.140, 0.384] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | fixed:200 | rmse_h1 | lstm[quantiles=None,loss=huber] | 0.364 [0.297, 0.449] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | fixed:200 | rmse_h1 | lstm[quantiles=None,loss=mse] | 0.571 [0.272, 0.965] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | fixed:200 | rmse_h1 | lstm[revin=True] | 0.337 [0.200, 0.474] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | fixed:200 | rmse_h1 | transformer | 0.214 [0.026, 0.402] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | fixed:200 | rmse_h10 | itransformer[loss=huber] | 1.136 [0.172, 2.836] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | fixed:200 | rmse_h10 | itransformer[loss=mse] | 1.071 [0.119, 2.912] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | fixed:200 | rmse_h10 | lstm[quantiles=None,loss=huber] | 1.296 [0.359, 2.838] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | fixed:200 | rmse_h10 | lstm[quantiles=None,loss=mse] | 1.277 [0.365, 2.829] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | fixed:200 | rmse_h10 | lstm[revin=True] | 1.357 [0.339, 2.953] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | fixed:200 | rmse_h10 | transformer | 1.072 [0.122, 2.647] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | fixed:200 | rmse_h100 | itransformer[loss=huber] | 0.657 [0.537, 0.777] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | fixed:200 | rmse_h100 | itransformer[loss=mse] | 0.558 [0.384, 0.732] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | fixed:200 | rmse_h100 | lstm[quantiles=None,loss=huber] | 1.031 [0.347, 1.935] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | fixed:200 | rmse_h100 | lstm[quantiles=None,loss=mse] | 1.429 [0.603, 2.260] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | fixed:200 | rmse_h100 | lstm[revin=True] | 1.161 [0.144, 2.178] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | fixed:200 | rmse_h100 | transformer | 1.225 [0.760, 1.690] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | fixed:200 | rmse_h25 | itransformer[loss=huber] | 1.448 [0.943, 1.953] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | fixed:200 | rmse_h25 | itransformer[loss=mse] | 1.631 [1.181, 2.081] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | fixed:200 | rmse_h25 | lstm[quantiles=None,loss=huber] | 1.369 [0.623, 2.115] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | fixed:200 | rmse_h25 | lstm[quantiles=None,loss=mse] | 1.883 [1.108, 2.659] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | fixed:200 | rmse_h25 | lstm[revin=True] | 1.415 [0.607, 2.223] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | fixed:200 | rmse_h25 | transformer | 1.494 [1.160, 1.827] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | fixed:200 | rmse_h50 | itransformer[loss=huber] | 0.906 [0.579, 1.233] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | fixed:200 | rmse_h50 | itransformer[loss=mse] | 0.986 [0.654, 1.310] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | fixed:200 | rmse_h50 | lstm[quantiles=None,loss=huber] | 1.233 [0.749, 1.818] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | fixed:200 | rmse_h50 | lstm[quantiles=None,loss=mse] | 1.546 [0.835, 2.256] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | fixed:200 | rmse_h50 | lstm[revin=True] | 1.492 [1.052, 1.967] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | fixed:200 | rmse_h50 | transformer | 1.265 [0.518, 1.976] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | fixed:400 | rmse_h1 | itransformer[loss=huber] | 0.250 [0.143, 0.357] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | fixed:400 | rmse_h1 | itransformer[loss=mse] | 0.489 [0.181, 1.012] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | fixed:400 | rmse_h1 | lstm[quantiles=None,loss=huber] | 0.206 [0.189, 0.226] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | fixed:400 | rmse_h1 | lstm[quantiles=None,loss=mse] | 0.328 [0.299, 0.358] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | fixed:400 | rmse_h1 | lstm[revin=True] | 0.105 [0.049, 0.204] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | fixed:400 | rmse_h1 | transformer | 0.227 [0.124, 0.372] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | fixed:400 | rmse_h10 | itransformer[loss=huber] | 0.700 [0.488, 0.931] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | fixed:400 | rmse_h10 | itransformer[loss=mse] | 0.651 [0.397, 0.904] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | fixed:400 | rmse_h10 | lstm[quantiles=None,loss=huber] | 0.797 [0.510, 0.996] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | fixed:400 | rmse_h10 | lstm[quantiles=None,loss=mse] | 0.818 [0.687, 0.922] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | fixed:400 | rmse_h10 | lstm[revin=True] | 0.852 [0.411, 1.160] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | fixed:400 | rmse_h10 | transformer | 0.733 [0.488, 0.992] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | fixed:400 | rmse_h100 | itransformer[loss=huber] | 2.158 [1.016, 3.301] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | fixed:400 | rmse_h100 | itransformer[loss=mse] | 2.133 [1.262, 2.997] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | fixed:400 | rmse_h100 | lstm[quantiles=None,loss=huber] | 2.603 [1.919, 3.307] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | fixed:400 | rmse_h100 | lstm[quantiles=None,loss=mse] | 2.703 [1.725, 3.516] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | fixed:400 | rmse_h100 | lstm[revin=True] | 3.090 [2.698, 3.527] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | fixed:400 | rmse_h100 | transformer | 2.674 [1.651, 3.904] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | fixed:400 | rmse_h25 | itransformer[loss=huber] | 1.035 [0.569, 1.473] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | fixed:400 | rmse_h25 | itransformer[loss=mse] | 1.125 [0.800, 1.484] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | fixed:400 | rmse_h25 | lstm[quantiles=None,loss=huber] | 0.846 [0.483, 1.251] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | fixed:400 | rmse_h25 | lstm[quantiles=None,loss=mse] | 0.856 [0.353, 1.386] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | fixed:400 | rmse_h25 | lstm[revin=True] | 1.008 [0.777, 1.239] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | fixed:400 | rmse_h25 | transformer | 0.922 [0.405, 1.439] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | fixed:400 | rmse_h50 | itransformer[loss=huber] | 0.900 [0.292, 1.784] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | fixed:400 | rmse_h50 | itransformer[loss=mse] | 0.743 [0.244, 1.369] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | fixed:400 | rmse_h50 | lstm[quantiles=None,loss=huber] | 1.017 [0.549, 1.568] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | fixed:400 | rmse_h50 | lstm[quantiles=None,loss=mse] | 1.413 [0.709, 2.026] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | fixed:400 | rmse_h50 | lstm[revin=True] | 0.804 [0.209, 1.484] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | fixed:400 | rmse_h50 | transformer | 1.118 [0.398, 1.889] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer[loss=huber] | 0.450 [0.218, 0.813] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer[loss=mse] | 0.596 [0.444, 0.747] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | frac:0.3 | rmse_h1 | lstm[quantiles=None,loss=huber] | 0.401 [0.201, 0.720] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | frac:0.3 | rmse_h1 | lstm[quantiles=None,loss=mse] | 0.564 [0.442, 0.685] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | frac:0.3 | rmse_h1 | lstm[revin=True] | 0.407 [0.142, 0.868] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | frac:0.3 | rmse_h1 | transformer | 0.402 [0.145, 0.834] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer[loss=huber] | 0.729 [0.363, 0.980] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer[loss=mse] | 0.641 [0.333, 0.948] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | frac:0.3 | rmse_h10 | lstm[quantiles=None,loss=huber] | 0.670 [0.257, 0.975] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | frac:0.3 | rmse_h10 | lstm[quantiles=None,loss=mse] | 0.847 [0.589, 1.267] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | frac:0.3 | rmse_h10 | lstm[revin=True] | 0.656 [0.269, 1.015] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | frac:0.3 | rmse_h10 | transformer | 0.830 [0.437, 1.124] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer[loss=huber] | 1.608 [0.520, 2.695] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer[loss=mse] | 1.969 [0.555, 3.383] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | frac:0.3 | rmse_h100 | lstm[quantiles=None,loss=huber] | 1.827 [0.871, 2.910] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | frac:0.3 | rmse_h100 | lstm[quantiles=None,loss=mse] | 2.047 [0.970, 3.125] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | frac:0.3 | rmse_h100 | lstm[revin=True] | 3.489 [2.452, 4.762] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | frac:0.3 | rmse_h100 | transformer | 2.951 [2.339, 3.427] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer[loss=huber] | 0.533 [0.141, 1.239] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer[loss=mse] | 0.635 [0.173, 1.527] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | frac:0.3 | rmse_h25 | lstm[quantiles=None,loss=huber] | 0.657 [0.233, 1.211] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | frac:0.3 | rmse_h25 | lstm[quantiles=None,loss=mse] | 0.841 [0.233, 1.657] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | frac:0.3 | rmse_h25 | lstm[revin=True] | 0.540 [0.065, 1.433] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | frac:0.3 | rmse_h25 | transformer | 0.510 [0.155, 1.039] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer[loss=huber] | 2.229 [0.849, 3.953] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer[loss=mse] | 2.384 [0.814, 4.139] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | frac:0.3 | rmse_h50 | lstm[quantiles=None,loss=huber] | 2.219 [1.045, 3.892] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | frac:0.3 | rmse_h50 | lstm[quantiles=None,loss=mse] | 2.783 [1.356, 4.317] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | frac:0.3 | rmse_h50 | lstm[revin=True] | 2.440 [0.639, 4.561] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | frac:0.3 | rmse_h50 | transformer | 2.440 [0.807, 3.991] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer[loss=huber] | 0.471 [0.125, 0.904] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer[loss=mse] | 0.445 [0.171, 0.838] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | frac:0.5 | rmse_h1 | lstm[quantiles=None,loss=huber] | 0.469 [0.106, 0.970] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | frac:0.5 | rmse_h1 | lstm[quantiles=None,loss=mse] | 0.547 [0.358, 0.859] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | frac:0.5 | rmse_h1 | lstm[revin=True] | 0.503 [0.033, 0.978] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | frac:0.5 | rmse_h1 | transformer | 0.535 [0.169, 1.060] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer[loss=huber] | 0.910 [0.373, 1.311] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer[loss=mse] | 0.796 [0.361, 1.207] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | frac:0.5 | rmse_h10 | lstm[quantiles=None,loss=huber] | 1.022 [0.485, 1.424] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | frac:0.5 | rmse_h10 | lstm[quantiles=None,loss=mse] | 0.730 [0.426, 1.146] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | frac:0.5 | rmse_h10 | lstm[revin=True] | 1.077 [0.485, 1.455] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | frac:0.5 | rmse_h10 | transformer | 1.020 [0.338, 1.723] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer[loss=huber] | 1.213 [0.561, 1.976] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer[loss=mse] | 1.279 [0.600, 2.206] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | frac:0.5 | rmse_h100 | lstm[quantiles=None,loss=huber] | 1.486 [0.719, 2.394] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | frac:0.5 | rmse_h100 | lstm[quantiles=None,loss=mse] | 1.640 [0.655, 2.703] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | frac:0.5 | rmse_h100 | lstm[revin=True] | 1.418 [0.623, 2.425] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | frac:0.5 | rmse_h100 | transformer | 1.035 [0.503, 1.625] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer[loss=huber] | 0.950 [0.501, 1.312] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer[loss=mse] | 0.890 [0.445, 1.174] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | frac:0.5 | rmse_h25 | lstm[quantiles=None,loss=huber] | 1.202 [0.507, 1.710] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | frac:0.5 | rmse_h25 | lstm[quantiles=None,loss=mse] | 1.193 [0.700, 1.558] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | frac:0.5 | rmse_h25 | lstm[revin=True] | 1.136 [0.626, 1.483] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | frac:0.5 | rmse_h25 | transformer | 1.100 [0.377, 2.047] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer[loss=huber] | 0.704 [0.297, 1.347] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer[loss=mse] | 0.788 [0.293, 1.454] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | frac:0.5 | rmse_h50 | lstm[quantiles=None,loss=huber] | 0.864 [0.264, 1.647] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | frac:0.5 | rmse_h50 | lstm[quantiles=None,loss=mse] | 1.100 [0.456, 1.745] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | frac:0.5 | rmse_h50 | lstm[revin=True] | 0.758 [0.401, 1.302] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | frac:0.5 | rmse_h50 | transformer | 0.908 [0.573, 1.252] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer[loss=huber] | 0.193 [0.091, 0.347] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer[loss=mse] | 0.298 [0.154, 0.473] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | frac:0.7 | rmse_h1 | lstm[quantiles=None,loss=huber] | 0.215 [0.088, 0.407] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | frac:0.7 | rmse_h1 | lstm[quantiles=None,loss=mse] | 0.430 [0.267, 0.612] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | frac:0.7 | rmse_h1 | lstm[revin=True] | 0.097 [0.043, 0.169] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | frac:0.7 | rmse_h1 | transformer | 0.165 [0.135, 0.194] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer[loss=huber] | 0.486 [0.119, 1.129] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer[loss=mse] | 0.589 [0.224, 1.074] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | frac:0.7 | rmse_h10 | lstm[quantiles=None,loss=huber] | 0.576 [0.263, 1.024] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | frac:0.7 | rmse_h10 | lstm[quantiles=None,loss=mse] | 0.668 [0.328, 1.055] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | frac:0.7 | rmse_h10 | lstm[revin=True] | 0.684 [0.275, 1.191] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | frac:0.7 | rmse_h10 | transformer | 0.523 [0.139, 1.109] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer[loss=huber] | 2.401 [1.308, 3.494] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer[loss=mse] | 2.255 [1.203, 3.269] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | frac:0.7 | rmse_h100 | lstm[quantiles=None,loss=huber] | 2.237 [0.945, 3.528] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | frac:0.7 | rmse_h100 | lstm[quantiles=None,loss=mse] | 2.783 [1.254, 4.312] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | frac:0.7 | rmse_h100 | lstm[revin=True] | 2.020 [0.646, 3.888] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | frac:0.7 | rmse_h100 | transformer | 2.191 [0.855, 3.259] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer[loss=huber] | 0.924 [0.488, 1.271] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer[loss=mse] | 1.082 [0.564, 1.437] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | frac:0.7 | rmse_h25 | lstm[quantiles=None,loss=huber] | 0.815 [0.398, 1.232] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | frac:0.7 | rmse_h25 | lstm[quantiles=None,loss=mse] | 1.153 [0.644, 1.626] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | frac:0.7 | rmse_h25 | lstm[revin=True] | 1.110 [0.773, 1.491] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | frac:0.7 | rmse_h25 | transformer | 0.767 [0.301, 1.233] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer[loss=huber] | 1.107 [0.811, 1.573] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer[loss=mse] | 1.065 [0.492, 1.872] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | frac:0.7 | rmse_h50 | lstm[quantiles=None,loss=huber] | 0.949 [0.310, 1.757] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | frac:0.7 | rmse_h50 | lstm[quantiles=None,loss=mse] | 1.579 [0.723, 2.436] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | frac:0.7 | rmse_h50 | lstm[revin=True] | 0.988 [0.144, 1.927] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | frac:0.7 | rmse_h50 | transformer | 0.924 [0.292, 1.556] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | overall | rmse_h1 | itransformer[loss=huber] | 0.399 [0.238, 0.559] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | overall | rmse_h1 | itransformer[loss=mse] | 0.502 [0.357, 0.646] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | overall | rmse_h1 | lstm[quantiles=None,loss=huber] | 0.395 [0.213, 0.578] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | overall | rmse_h1 | lstm[quantiles=None,loss=mse] | 0.548 [0.406, 0.768] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | overall | rmse_h1 | lstm[revin=True] | 0.395 [0.183, 0.607] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | overall | rmse_h1 | transformer | 0.406 [0.221, 0.591] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | overall | rmse_h10 | itransformer[loss=huber] | 1.018 [0.665, 1.535] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | overall | rmse_h10 | itransformer[loss=mse] | 0.983 [0.601, 1.561] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | overall | rmse_h10 | lstm[quantiles=None,loss=huber] | 1.067 [0.744, 1.586] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | overall | rmse_h10 | lstm[quantiles=None,loss=mse] | 1.042 [0.668, 1.549] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | overall | rmse_h10 | lstm[revin=True] | 1.156 [0.862, 1.624] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | overall | rmse_h10 | transformer | 1.035 [0.646, 1.559] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | overall | rmse_h100 | itransformer[loss=huber] | 1.899 [1.151, 2.449] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | overall | rmse_h100 | itransformer[loss=mse] | 1.946 [1.139, 2.393] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | overall | rmse_h100 | lstm[quantiles=None,loss=huber] | 2.111 [1.679, 2.643] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | overall | rmse_h100 | lstm[quantiles=None,loss=mse] | 2.387 [1.723, 3.052] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | overall | rmse_h100 | lstm[revin=True] | 2.566 [1.835, 3.298] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | overall | rmse_h100 | transformer | 2.281 [1.823, 2.802] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | overall | rmse_h25 | itransformer[loss=huber] | 1.111 [0.828, 1.453] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | overall | rmse_h25 | itransformer[loss=mse] | 1.204 [0.932, 1.540] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | overall | rmse_h25 | lstm[quantiles=None,loss=huber] | 1.140 [0.909, 1.375] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | overall | rmse_h25 | lstm[quantiles=None,loss=mse] | 1.354 [0.966, 1.742] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | overall | rmse_h25 | lstm[revin=True] | 1.196 [0.935, 1.458] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | overall | rmse_h25 | transformer | 1.112 [0.841, 1.494] |  |  | 4 | 5 | dc16fbab |
| loco | start_points | overall | rmse_h50 | itransformer[loss=huber] | 1.491 [0.928, 2.084] |  |  | 4 | 5 | 41d648c8 |
| loco | start_points | overall | rmse_h50 | itransformer[loss=mse] | 1.548 [0.968, 2.147] |  |  | 4 | 5 | d4824fbc |
| loco | start_points | overall | rmse_h50 | lstm[quantiles=None,loss=huber] | 1.532 [1.031, 2.007] |  |  | 4 | 5 | 4e98b269 |
| loco | start_points | overall | rmse_h50 | lstm[quantiles=None,loss=mse] | 1.943 [1.250, 2.608] |  |  | 4 | 5 | ba6a435e |
| loco | start_points | overall | rmse_h50 | lstm[revin=True] | 1.676 [1.114, 2.267] |  |  | 4 | 5 | 0a2e3a80 |
| loco | start_points | overall | rmse_h50 | transformer | 1.682 [1.359, 2.029] |  |  | 4 | 5 | dc16fbab |

</details>

<details><summary>nasa_forecast (210 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | itransformer[loss=huber] | 0.911 [0.655, 1.167] |  | 1.221 | 4 | 5 | ceba4eba |
| loco | all | overall | rmse_h1 | itransformer[loss=mse] | 0.907 [0.648, 1.166] |  | 1.210 | 4 | 5 | bab8bc6a |
| loco | all | overall | rmse_h1 | lstm[quantiles=None,loss=huber] | 1.168 [0.843, 1.493] |  | 1.533 | 4 | 5 | a556b7e5 |
| loco | all | overall | rmse_h1 | lstm[quantiles=None,loss=mse] | 2.382 [1.823, 3.015] |  | 2.541 | 4 | 5 | 97861f32 |
| loco | all | overall | rmse_h1 | lstm[revin=True] | 0.933 [0.686, 1.180] |  | 1.223 | 4 | 5 | c17ed23c |
| loco | all | overall | rmse_h1 | transformer | 0.925 [0.676, 1.175] |  | 1.217 | 4 | 5 | 20605e71 |
| loco | all | overall | rmse_h10 | itransformer[loss=huber] | 1.678 [1.068, 2.288] |  | 2.532 | 4 | 5 | ceba4eba |
| loco | all | overall | rmse_h10 | itransformer[loss=mse] | 1.681 [1.080, 2.283] |  | 2.426 | 4 | 5 | bab8bc6a |
| loco | all | overall | rmse_h10 | lstm[quantiles=None,loss=huber] | 2.762 [1.927, 3.597] |  | 3.282 | 4 | 5 | a556b7e5 |
| loco | all | overall | rmse_h10 | lstm[quantiles=None,loss=mse] | 4.632 [3.379, 6.000] |  | 5.010 | 4 | 5 | 97861f32 |
| loco | all | overall | rmse_h10 | lstm[revin=True] | 1.779 [1.244, 2.314] |  | 2.347 | 4 | 5 | c17ed23c |
| loco | all | overall | rmse_h10 | transformer | 1.684 [1.152, 2.216] |  | 2.311 | 4 | 5 | 20605e71 |
| loco | all | overall | rmse_h100 | itransformer[loss=huber] | 12.727 [11.257, 14.794] |  | 11.282 | 4 | 5 | ceba4eba |
| loco | all | overall | rmse_h100 | itransformer[loss=mse] | 11.720 [10.052, 13.749] |  | 10.993 | 4 | 5 | bab8bc6a |
| loco | all | overall | rmse_h100 | lstm[quantiles=None,loss=huber] | 4.889 [2.427, 7.350] |  | 2.551 | 4 | 5 | a556b7e5 |
| loco | all | overall | rmse_h100 | lstm[quantiles=None,loss=mse] | 6.219 [3.551, 9.509] |  | 3.714 | 4 | 5 | 97861f32 |
| loco | all | overall | rmse_h100 | lstm[revin=True] | 9.803 [9.080, 11.064] |  | 9.319 | 4 | 5 | c17ed23c |
| loco | all | overall | rmse_h100 | transformer | 8.104 [7.183, 9.325] |  | 7.644 | 4 | 5 | 20605e71 |
| loco | all | overall | rmse_h25 | itransformer[loss=huber] | 2.449 [1.833, 3.165] |  | 3.591 | 4 | 5 | ceba4eba |
| loco | all | overall | rmse_h25 | itransformer[loss=mse] | 2.551 [1.956, 3.210] |  | 3.608 | 4 | 5 | bab8bc6a |
| loco | all | overall | rmse_h25 | lstm[quantiles=None,loss=huber] | 3.754 [3.088, 4.482] |  | 3.992 | 4 | 5 | a556b7e5 |
| loco | all | overall | rmse_h25 | lstm[quantiles=None,loss=mse] | 4.159 [3.556, 4.974] |  | 4.142 | 4 | 5 | 97861f32 |
| loco | all | overall | rmse_h25 | lstm[revin=True] | 2.573 [1.864, 3.283] |  | 3.097 | 4 | 5 | c17ed23c |
| loco | all | overall | rmse_h25 | transformer | 2.216 [1.588, 2.845] |  | 3.130 | 4 | 5 | 20605e71 |
| loco | all | overall | rmse_h50 | itransformer[loss=huber] | 4.706 [4.584, 4.859] |  | 4.577 | 4 | 5 | ceba4eba |
| loco | all | overall | rmse_h50 | itransformer[loss=mse] | 4.795 [4.718, 4.915] |  | 4.702 | 4 | 5 | bab8bc6a |
| loco | all | overall | rmse_h50 | lstm[quantiles=None,loss=huber] | 3.579 [2.724, 4.580] |  | 2.717 | 4 | 5 | a556b7e5 |
| loco | all | overall | rmse_h50 | lstm[quantiles=None,loss=mse] | 5.052 [3.659, 6.900] |  | 3.336 | 4 | 5 | 97861f32 |
| loco | all | overall | rmse_h50 | lstm[revin=True] | 4.353 [3.983, 4.837] |  | 3.974 | 4 | 5 | c17ed23c |
| loco | all | overall | rmse_h50 | transformer | 3.693 [3.274, 4.237] |  | 4.511 | 4 | 5 | 20605e71 |
| loco | start_points | fixed:30 | rmse_h1 | itransformer[loss=huber] | 2.267 [0.916, 3.476] |  | 0.279 | 4 | 5 | ceba4eba |
| loco | start_points | fixed:30 | rmse_h1 | itransformer[loss=mse] | 2.192 [0.893, 3.349] |  | 0.276 | 4 | 5 | bab8bc6a |
| loco | start_points | fixed:30 | rmse_h1 | lstm[quantiles=None,loss=huber] | 2.409 [1.329, 3.260] |  | 0.721 | 4 | 5 | a556b7e5 |
| loco | start_points | fixed:30 | rmse_h1 | lstm[quantiles=None,loss=mse] | 3.124 [2.124, 4.123] |  | 1.729 | 4 | 5 | 97861f32 |
| loco | start_points | fixed:30 | rmse_h1 | lstm[revin=True] | 2.189 [0.846, 3.295] |  | 0.184 | 4 | 5 | c17ed23c |
| loco | start_points | fixed:30 | rmse_h1 | transformer | 2.271 [0.936, 3.383] |  | 0.275 | 4 | 5 | 20605e71 |
| loco | start_points | fixed:30 | rmse_h10 | itransformer[loss=huber] | 1.040 [0.417, 1.816] |  | 2.128 | 4 | 5 | ceba4eba |
| loco | start_points | fixed:30 | rmse_h10 | itransformer[loss=mse] | 1.177 [0.591, 1.967] |  | 2.332 | 4 | 5 | bab8bc6a |
| loco | start_points | fixed:30 | rmse_h10 | lstm[quantiles=None,loss=huber] | 1.961 [0.830, 3.259] |  | 0.361 | 4 | 5 | a556b7e5 |
| loco | start_points | fixed:30 | rmse_h10 | lstm[quantiles=None,loss=mse] | 3.748 [1.422, 6.671] |  | 0.725 | 4 | 5 | 97861f32 |
| loco | start_points | fixed:30 | rmse_h10 | lstm[revin=True] | 1.082 [0.346, 1.817] |  | 1.881 | 4 | 5 | c17ed23c |
| loco | start_points | fixed:30 | rmse_h10 | transformer | 1.042 [0.409, 1.675] |  | 1.741 | 4 | 5 | 20605e71 |
| loco | start_points | fixed:30 | rmse_h100 | itransformer[loss=huber] | 11.343 [4.571, 17.399] |  | 0.891 | 4 | 5 | ceba4eba |
| loco | start_points | fixed:30 | rmse_h100 | itransformer[loss=mse] | 10.037 [3.673, 16.402] |  | 1.273 | 4 | 5 | bab8bc6a |
| loco | start_points | fixed:30 | rmse_h100 | lstm[quantiles=None,loss=huber] | 4.512 [1.050, 7.974] |  | 0.830 | 4 | 5 | a556b7e5 |
| loco | start_points | fixed:30 | rmse_h100 | lstm[quantiles=None,loss=mse] | 5.646 [1.936, 9.923] |  | 1.303 | 4 | 5 | 97861f32 |
| loco | start_points | fixed:30 | rmse_h100 | lstm[revin=True] | 8.761 [4.433, 13.089] |  | 2.681 | 4 | 5 | c17ed23c |
| loco | start_points | fixed:30 | rmse_h100 | transformer | 6.164 [1.471, 10.857] |  | 0.857 | 4 | 5 | 20605e71 |
| loco | start_points | fixed:30 | rmse_h25 | itransformer[loss=huber] | 1.835 [1.015, 2.656] |  | 2.938 | 4 | 5 | ceba4eba |
| loco | start_points | fixed:30 | rmse_h25 | itransformer[loss=mse] | 1.942 [1.093, 2.791] |  | 2.878 | 4 | 5 | bab8bc6a |
| loco | start_points | fixed:30 | rmse_h25 | lstm[quantiles=None,loss=huber] | 3.132 [1.543, 4.190] |  | 0.806 | 4 | 5 | a556b7e5 |
| loco | start_points | fixed:30 | rmse_h25 | lstm[quantiles=None,loss=mse] | 3.902 [2.659, 4.805] |  | 1.983 | 4 | 5 | 97861f32 |
| loco | start_points | fixed:30 | rmse_h25 | lstm[revin=True] | 1.694 [0.818, 2.493] |  | 1.963 | 4 | 5 | c17ed23c |
| loco | start_points | fixed:30 | rmse_h25 | transformer | 1.129 [0.523, 1.525] |  | 1.588 | 4 | 5 | 20605e71 |
| loco | start_points | fixed:30 | rmse_h50 | itransformer[loss=huber] | 5.569 [2.654, 8.483] |  | 1.161 | 4 | 5 | ceba4eba |
| loco | start_points | fixed:30 | rmse_h50 | itransformer[loss=mse] | 5.684 [2.650, 8.719] |  | 1.440 | 4 | 5 | bab8bc6a |
| loco | start_points | fixed:30 | rmse_h50 | lstm[quantiles=None,loss=huber] | 3.283 [1.160, 6.523] |  | 2.369 | 4 | 5 | a556b7e5 |
| loco | start_points | fixed:30 | rmse_h50 | lstm[quantiles=None,loss=mse] | 5.026 [3.397, 7.493] |  | 3.121 | 4 | 5 | 97861f32 |
| loco | start_points | fixed:30 | rmse_h50 | lstm[revin=True] | 5.457 [2.771, 7.055] |  | 1.372 | 4 | 5 | c17ed23c |
| loco | start_points | fixed:30 | rmse_h50 | transformer | 4.141 [2.544, 5.498] |  | 1.606 | 4 | 5 | 20605e71 |
| loco | start_points | fixed:50 | rmse_h1 | itransformer[loss=huber] | 0.529 [0.088, 1.035] |  | 1.344 | 4 | 5 | ceba4eba |
| loco | start_points | fixed:50 | rmse_h1 | itransformer[loss=mse] | 0.567 [0.217, 0.918] |  | 0.964 | 4 | 5 | bab8bc6a |
| loco | start_points | fixed:50 | rmse_h1 | lstm[quantiles=None,loss=huber] | 0.674 [0.390, 0.959] |  | 0.945 | 4 | 5 | a556b7e5 |
| loco | start_points | fixed:50 | rmse_h1 | lstm[quantiles=None,loss=mse] | 1.698 [1.323, 2.073] |  | 2.121 | 4 | 5 | 97861f32 |
| loco | start_points | fixed:50 | rmse_h1 | lstm[revin=True] | 0.601 [0.121, 1.080] |  | 1.328 | 4 | 5 | c17ed23c |
| loco | start_points | fixed:50 | rmse_h1 | transformer | 0.535 [0.115, 0.956] |  | 1.210 | 4 | 5 | 20605e71 |
| loco | start_points | fixed:50 | rmse_h10 | itransformer[loss=huber] | 1.039 [0.826, 1.287] |  | 1.077 | 4 | 5 | ceba4eba |
| loco | start_points | fixed:50 | rmse_h10 | itransformer[loss=mse] | 1.258 [0.614, 1.893] |  | 0.371 | 4 | 5 | bab8bc6a |
| loco | start_points | fixed:50 | rmse_h10 | lstm[quantiles=None,loss=huber] | 2.630 [0.802, 4.459] |  | 4.410 | 4 | 5 | a556b7e5 |
| loco | start_points | fixed:50 | rmse_h10 | lstm[quantiles=None,loss=mse] | 4.703 [3.319, 6.112] |  | 5.163 | 4 | 5 | 97861f32 |
| loco | start_points | fixed:50 | rmse_h10 | lstm[revin=True] | 2.001 [1.173, 3.497] |  | 1.261 | 4 | 5 | c17ed23c |
| loco | start_points | fixed:50 | rmse_h10 | transformer | 1.897 [1.215, 2.903] |  | 1.083 | 4 | 5 | 20605e71 |
| loco | start_points | fixed:50 | rmse_h100 | itransformer[loss=huber] | 9.394 [3.658, 15.100] |  |  | 3 | 5 | 004f6ae6 |
| loco | start_points | fixed:50 | rmse_h100 | itransformer[loss=mse] | 7.384 [1.466, 12.799] |  |  | 3 | 5 | 5d2c32a0 |
| loco | start_points | fixed:50 | rmse_h100 | lstm[quantiles=None,loss=huber] | 5.572 [2.821, 8.772] |  |  | 3 | 5 | 51499bdc |
| loco | start_points | fixed:50 | rmse_h100 | lstm[quantiles=None,loss=mse] | 6.222 [3.828, 9.476] |  |  | 3 | 5 | 7616e61b |
| loco | start_points | fixed:50 | rmse_h100 | lstm[revin=True] | 5.070 [1.871, 9.928] |  |  | 3 | 5 | 07038ea0 |
| loco | start_points | fixed:50 | rmse_h100 | transformer | 6.046 [1.679, 9.773] |  |  | 3 | 5 | 9c14f07e |
| loco | start_points | fixed:50 | rmse_h25 | itransformer[loss=huber] | 2.274 [1.233, 3.091] |  | 0.705 | 4 | 5 | ceba4eba |
| loco | start_points | fixed:50 | rmse_h25 | itransformer[loss=mse] | 2.865 [2.152, 3.616] |  | 1.909 | 4 | 5 | bab8bc6a |
| loco | start_points | fixed:50 | rmse_h25 | lstm[quantiles=None,loss=huber] | 4.432 [1.401, 7.464] |  | 7.610 | 4 | 5 | a556b7e5 |
| loco | start_points | fixed:50 | rmse_h25 | lstm[quantiles=None,loss=mse] | 5.100 [2.921, 7.279] |  | 7.181 | 4 | 5 | 97861f32 |
| loco | start_points | fixed:50 | rmse_h25 | lstm[revin=True] | 3.607 [1.922, 5.670] |  | 1.948 | 4 | 5 | c17ed23c |
| loco | start_points | fixed:50 | rmse_h25 | transformer | 3.657 [2.053, 5.065] |  | 1.386 | 4 | 5 | 20605e71 |
| loco | start_points | fixed:50 | rmse_h50 | itransformer[loss=huber] | 3.421 [1.639, 5.554] |  | 2.257 | 4 | 5 | ceba4eba |
| loco | start_points | fixed:50 | rmse_h50 | itransformer[loss=mse] | 3.738 [1.426, 5.946] |  | 3.376 | 4 | 5 | bab8bc6a |
| loco | start_points | fixed:50 | rmse_h50 | lstm[quantiles=None,loss=huber] | 3.530 [2.350, 4.750] |  | 4.005 | 4 | 5 | a556b7e5 |
| loco | start_points | fixed:50 | rmse_h50 | lstm[quantiles=None,loss=mse] | 4.970 [3.783, 6.157] |  | 3.300 | 4 | 5 | 97861f32 |
| loco | start_points | fixed:50 | rmse_h50 | lstm[revin=True] | 4.686 [2.917, 5.952] |  | 5.187 | 4 | 5 | c17ed23c |
| loco | start_points | fixed:50 | rmse_h50 | transformer | 5.009 [3.867, 6.152] |  | 6.252 | 4 | 5 | 20605e71 |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer[loss=huber] | 0.159 [0.048, 0.327] |  | 0.033 | 4 | 5 | ceba4eba |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer[loss=mse] | 0.203 [0.093, 0.321] |  | 0.043 | 4 | 5 | bab8bc6a |
| loco | start_points | frac:0.3 | rmse_h1 | lstm[quantiles=None,loss=huber] | 0.914 [0.459, 1.603] |  | 0.773 | 4 | 5 | a556b7e5 |
| loco | start_points | frac:0.3 | rmse_h1 | lstm[quantiles=None,loss=mse] | 2.526 [1.376, 4.052] |  | 1.791 | 4 | 5 | 97861f32 |
| loco | start_points | frac:0.3 | rmse_h1 | lstm[revin=True] | 0.194 [0.082, 0.305] |  | 0.154 | 4 | 5 | c17ed23c |
| loco | start_points | frac:0.3 | rmse_h1 | transformer | 0.201 [0.064, 0.385] |  | 0.149 | 4 | 5 | 20605e71 |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer[loss=huber] | 1.413 [0.559, 2.267] |  | 0.391 | 4 | 5 | ceba4eba |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer[loss=mse] | 1.372 [0.386, 2.358] |  | 0.147 | 4 | 5 | bab8bc6a |
| loco | start_points | frac:0.3 | rmse_h10 | lstm[quantiles=None,loss=huber] | 2.722 [1.782, 3.658] |  | 4.022 | 4 | 5 | a556b7e5 |
| loco | start_points | frac:0.3 | rmse_h10 | lstm[quantiles=None,loss=mse] | 4.380 [3.800, 5.033] |  | 5.279 | 4 | 5 | 97861f32 |
| loco | start_points | frac:0.3 | rmse_h10 | lstm[revin=True] | 1.110 [0.528, 1.696] |  | 0.265 | 4 | 5 | c17ed23c |
| loco | start_points | frac:0.3 | rmse_h10 | transformer | 1.741 [1.069, 2.699] |  | 0.917 | 4 | 5 | 20605e71 |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer[loss=huber] | 11.311 [4.060, 18.955] |  | 0.960 | 4 | 5 | ceba4eba |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer[loss=mse] | 9.771 [2.836, 16.884] |  | 0.456 | 4 | 5 | bab8bc6a |
| loco | start_points | frac:0.3 | rmse_h100 | lstm[quantiles=None,loss=huber] | 4.249 [2.420, 6.078] |  | 3.020 | 4 | 5 | a556b7e5 |
| loco | start_points | frac:0.3 | rmse_h100 | lstm[quantiles=None,loss=mse] | 5.724 [4.220, 7.228] |  | 4.633 | 4 | 5 | 97861f32 |
| loco | start_points | frac:0.3 | rmse_h100 | lstm[revin=True] | 9.292 [3.452, 14.388] |  | 0.833 | 4 | 5 | c17ed23c |
| loco | start_points | frac:0.3 | rmse_h100 | transformer | 7.696 [5.753, 10.820] |  | 6.786 | 4 | 5 | 20605e71 |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer[loss=huber] | 3.286 [1.969, 4.870] |  | 5.488 | 4 | 5 | ceba4eba |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer[loss=mse] | 3.468 [2.222, 4.937] |  | 5.528 | 4 | 5 | bab8bc6a |
| loco | start_points | frac:0.3 | rmse_h25 | lstm[quantiles=None,loss=huber] | 2.888 [2.277, 3.475] |  | 2.057 | 4 | 5 | a556b7e5 |
| loco | start_points | frac:0.3 | rmse_h25 | lstm[quantiles=None,loss=mse] | 3.435 [3.130, 3.745] |  | 3.562 | 4 | 5 | 97861f32 |
| loco | start_points | frac:0.3 | rmse_h25 | lstm[revin=True] | 3.058 [2.060, 4.409] |  | 5.027 | 4 | 5 | c17ed23c |
| loco | start_points | frac:0.3 | rmse_h25 | transformer | 3.126 [1.380, 5.337] |  | 6.620 | 4 | 5 | 20605e71 |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer[loss=huber] | 5.534 [2.061, 9.007] |  | 0.865 | 4 | 5 | ceba4eba |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer[loss=mse] | 5.641 [2.233, 9.049] |  | 1.295 | 4 | 5 | bab8bc6a |
| loco | start_points | frac:0.3 | rmse_h50 | lstm[quantiles=None,loss=huber] | 1.856 [1.020, 2.693] |  | 1.010 | 4 | 5 | a556b7e5 |
| loco | start_points | frac:0.3 | rmse_h50 | lstm[quantiles=None,loss=mse] | 4.795 [3.166, 6.299] |  | 2.161 | 4 | 5 | 97861f32 |
| loco | start_points | frac:0.3 | rmse_h50 | lstm[revin=True] | 5.909 [2.916, 8.412] |  | 1.192 | 4 | 5 | c17ed23c |
| loco | start_points | frac:0.3 | rmse_h50 | transformer | 3.640 [2.011, 5.504] |  | 3.181 | 4 | 5 | 20605e71 |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer[loss=huber] | 2.084 [0.289, 3.878] |  | 3.785 | 4 | 5 | ceba4eba |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer[loss=mse] | 1.969 [0.207, 3.730] |  | 3.636 | 4 | 5 | bab8bc6a |
| loco | start_points | frac:0.5 | rmse_h1 | lstm[quantiles=None,loss=huber] | 1.752 [0.507, 2.997] |  | 2.841 | 4 | 5 | a556b7e5 |
| loco | start_points | frac:0.5 | rmse_h1 | lstm[quantiles=None,loss=mse] | 2.022 [0.842, 3.276] |  | 2.385 | 4 | 5 | 97861f32 |
| loco | start_points | frac:0.5 | rmse_h1 | lstm[revin=True] | 2.020 [0.293, 3.747] |  | 3.774 | 4 | 5 | c17ed23c |
| loco | start_points | frac:0.5 | rmse_h1 | transformer | 1.934 [0.199, 3.669] |  | 3.517 | 4 | 5 | 20605e71 |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer[loss=huber] | 2.474 [0.816, 5.573] |  | 7.138 | 4 | 5 | ceba4eba |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer[loss=mse] | 2.287 [0.543, 5.249] |  | 6.708 | 4 | 5 | bab8bc6a |
| loco | start_points | frac:0.5 | rmse_h10 | lstm[quantiles=None,loss=huber] | 1.946 [1.002, 3.197] |  | 1.866 | 4 | 5 | a556b7e5 |
| loco | start_points | frac:0.5 | rmse_h10 | lstm[quantiles=None,loss=mse] | 3.757 [1.705, 6.664] |  | 1.257 | 4 | 5 | 97861f32 |
| loco | start_points | frac:0.5 | rmse_h10 | lstm[revin=True] | 2.316 [0.764, 4.755] |  | 5.984 | 4 | 5 | c17ed23c |
| loco | start_points | frac:0.5 | rmse_h10 | transformer | 2.309 [0.547, 4.671] |  | 5.692 | 4 | 5 | 20605e71 |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer[loss=huber] | 8.119 [2.061, 12.611] |  |  | 3 | 5 | 004f6ae6 |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer[loss=mse] | 5.819 [0.642, 10.743] |  |  | 3 | 5 | 5d2c32a0 |
| loco | start_points | frac:0.5 | rmse_h100 | lstm[quantiles=None,loss=huber] | 5.801 [1.763, 10.174] |  |  | 3 | 5 | 51499bdc |
| loco | start_points | frac:0.5 | rmse_h100 | lstm[quantiles=None,loss=mse] | 6.994 [2.779, 12.374] |  |  | 3 | 5 | 7616e61b |
| loco | start_points | frac:0.5 | rmse_h100 | lstm[revin=True] | 5.816 [3.351, 7.911] |  |  | 3 | 5 | 07038ea0 |
| loco | start_points | frac:0.5 | rmse_h100 | transformer | 5.367 [2.085, 10.837] |  |  | 3 | 5 | 9c14f07e |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer[loss=huber] | 2.263 [0.889, 3.851] |  | 4.795 | 4 | 5 | ceba4eba |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer[loss=mse] | 1.944 [0.569, 3.319] |  | 3.921 | 4 | 5 | bab8bc6a |
| loco | start_points | frac:0.5 | rmse_h25 | lstm[quantiles=None,loss=huber] | 2.313 [1.449, 3.313] |  | 2.362 | 4 | 5 | a556b7e5 |
| loco | start_points | frac:0.5 | rmse_h25 | lstm[quantiles=None,loss=mse] | 3.018 [2.212, 4.103] |  | 2.077 | 4 | 5 | 97861f32 |
| loco | start_points | frac:0.5 | rmse_h25 | lstm[revin=True] | 2.126 [1.506, 2.747] |  | 2.696 | 4 | 5 | c17ed23c |
| loco | start_points | frac:0.5 | rmse_h25 | transformer | 1.617 [0.520, 3.101] |  | 1.124 | 4 | 5 | 20605e71 |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer[loss=huber] | 3.503 [2.098, 4.876] |  | 2.926 | 4 | 5 | ceba4eba |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer[loss=mse] | 3.270 [1.472, 4.942] |  | 2.931 | 4 | 5 | bab8bc6a |
| loco | start_points | frac:0.5 | rmse_h50 | lstm[quantiles=None,loss=huber] | 3.856 [2.044, 6.584] |  | 2.208 | 4 | 5 | a556b7e5 |
| loco | start_points | frac:0.5 | rmse_h50 | lstm[quantiles=None,loss=mse] | 4.636 [2.268, 7.394] |  | 1.445 | 4 | 5 | 97861f32 |
| loco | start_points | frac:0.5 | rmse_h50 | lstm[revin=True] | 3.702 [1.890, 5.515] |  | 1.710 | 4 | 5 | c17ed23c |
| loco | start_points | frac:0.5 | rmse_h50 | transformer | 3.410 [1.419, 5.583] |  | 0.573 | 4 | 5 | 20605e71 |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer[loss=huber] | 1.380 [0.198, 3.263] |  | 4.283 | 4 | 5 | ceba4eba |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer[loss=mse] | 1.326 [0.227, 3.211] |  | 4.134 | 4 | 5 | bab8bc6a |
| loco | start_points | frac:0.7 | rmse_h1 | lstm[quantiles=None,loss=huber] | 0.956 [0.206, 1.998] |  | 2.588 | 4 | 5 | a556b7e5 |
| loco | start_points | frac:0.7 | rmse_h1 | lstm[quantiles=None,loss=mse] | 1.583 [1.181, 2.180] |  | 2.482 | 4 | 5 | 97861f32 |
| loco | start_points | frac:0.7 | rmse_h1 | lstm[revin=True] | 1.357 [0.265, 3.103] |  | 4.047 | 4 | 5 | c17ed23c |
| loco | start_points | frac:0.7 | rmse_h1 | transformer | 1.426 [0.169, 3.236] |  | 4.214 | 4 | 5 | 20605e71 |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer[loss=huber] | 0.736 [0.267, 1.305] |  | 0.187 | 4 | 5 | ceba4eba |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer[loss=mse] | 0.955 [0.694, 1.217] |  | 0.816 | 4 | 5 | bab8bc6a |
| loco | start_points | frac:0.7 | rmse_h10 | lstm[quantiles=None,loss=huber] | 1.977 [0.531, 3.879] |  | 4.700 | 4 | 5 | a556b7e5 |
| loco | start_points | frac:0.7 | rmse_h10 | lstm[quantiles=None,loss=mse] | 3.755 [1.150, 6.361] |  | 7.287 | 4 | 5 | 97861f32 |
| loco | start_points | frac:0.7 | rmse_h10 | lstm[revin=True] | 0.851 [0.507, 1.465] |  | 0.548 | 4 | 5 | c17ed23c |
| loco | start_points | frac:0.7 | rmse_h10 | transformer | 0.992 [0.644, 1.325] |  | 0.949 | 4 | 5 | 20605e71 |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer[loss=huber] | 4.976 |  |  | 1 | 5 | 6ebb81a9 |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer[loss=mse] | 1.304 |  |  | 1 | 5 | fcbe0e5a |
| loco | start_points | frac:0.7 | rmse_h100 | lstm[quantiles=None,loss=huber] | 9.506 |  |  | 1 | 5 | acf9456e |
| loco | start_points | frac:0.7 | rmse_h100 | lstm[quantiles=None,loss=mse] | 10.534 |  |  | 1 | 5 | 7cfb10d7 |
| loco | start_points | frac:0.7 | rmse_h100 | lstm[revin=True] | 5.931 |  |  | 1 | 5 | e1abd4a8 |
| loco | start_points | frac:0.7 | rmse_h100 | transformer | 1.881 |  |  | 1 | 5 | 7067c7cf |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer[loss=huber] | 2.307 [0.665, 4.491] |  | 1.083 | 4 | 5 | ceba4eba |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer[loss=mse] | 2.522 [0.728, 4.869] |  | 1.914 | 4 | 5 | bab8bc6a |
| loco | start_points | frac:0.7 | rmse_h25 | lstm[quantiles=None,loss=huber] | 3.776 [1.583, 5.968] |  | 5.491 | 4 | 5 | a556b7e5 |
| loco | start_points | frac:0.7 | rmse_h25 | lstm[quantiles=None,loss=mse] | 3.910 [2.174, 5.920] |  | 4.186 | 4 | 5 | 97861f32 |
| loco | start_points | frac:0.7 | rmse_h25 | lstm[revin=True] | 2.477 [0.392, 4.766] |  | 0.248 | 4 | 5 | c17ed23c |
| loco | start_points | frac:0.7 | rmse_h25 | transformer | 1.198 [0.429, 1.967] |  | 0.758 | 4 | 5 | 20605e71 |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer[loss=huber] | 2.076 [1.377, 2.673] |  | 1.959 | 4 | 5 | ceba4eba |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer[loss=mse] | 2.250 [1.213, 2.853] |  | 2.848 | 4 | 5 | bab8bc6a |
| loco | start_points | frac:0.7 | rmse_h50 | lstm[quantiles=None,loss=huber] | 3.300 [2.104, 4.325] |  | 4.745 | 4 | 5 | a556b7e5 |
| loco | start_points | frac:0.7 | rmse_h50 | lstm[quantiles=None,loss=mse] | 4.178 [2.948, 5.234] |  | 4.311 | 4 | 5 | 97861f32 |
| loco | start_points | frac:0.7 | rmse_h50 | lstm[revin=True] | 2.943 [1.530, 4.355] |  | 1.365 | 4 | 5 | c17ed23c |
| loco | start_points | frac:0.7 | rmse_h50 | transformer | 1.135 [0.469, 2.129] |  | 0.962 | 4 | 5 | 20605e71 |
| loco | start_points | overall | rmse_h1 | itransformer[loss=huber] | 1.846 [1.096, 2.597] |  | 2.632 | 4 | 5 | ceba4eba |
| loco | start_points | overall | rmse_h1 | itransformer[loss=mse] | 1.780 [1.069, 2.491] |  | 2.506 | 4 | 5 | bab8bc6a |
| loco | start_points | overall | rmse_h1 | lstm[quantiles=None,loss=huber] | 1.759 [1.342, 2.173] |  | 1.950 | 4 | 5 | a556b7e5 |
| loco | start_points | overall | rmse_h1 | lstm[quantiles=None,loss=mse] | 2.576 [1.825, 3.334] |  | 2.544 | 4 | 5 | 97861f32 |
| loco | start_points | overall | rmse_h1 | lstm[revin=True] | 1.796 [1.110, 2.481] |  | 2.547 | 4 | 5 | c17ed23c |
| loco | start_points | overall | rmse_h1 | transformer | 1.819 [1.129, 2.508] |  | 2.518 | 4 | 5 | 20605e71 |
| loco | start_points | overall | rmse_h10 | itransformer[loss=huber] | 1.764 [1.038, 2.792] |  | 3.377 | 4 | 5 | ceba4eba |
| loco | start_points | overall | rmse_h10 | itransformer[loss=mse] | 1.814 [1.127, 2.710] |  | 3.206 | 4 | 5 | bab8bc6a |
| loco | start_points | overall | rmse_h10 | lstm[quantiles=None,loss=huber] | 2.588 [1.625, 3.550] |  | 3.527 | 4 | 5 | a556b7e5 |
| loco | start_points | overall | rmse_h10 | lstm[quantiles=None,loss=mse] | 4.596 [3.264, 6.029] |  | 4.906 | 4 | 5 | 97861f32 |
| loco | start_points | overall | rmse_h10 | lstm[revin=True] | 1.880 [1.200, 2.559] |  | 2.879 | 4 | 5 | c17ed23c |
| loco | start_points | overall | rmse_h10 | transformer | 1.888 [1.188, 2.588] |  | 2.772 | 4 | 5 | 20605e71 |
| loco | start_points | overall | rmse_h100 | itransformer[loss=huber] | 9.481 [3.619, 15.254] |  | 1.040 | 4 | 5 | ceba4eba |
| loco | start_points | overall | rmse_h100 | itransformer[loss=mse] | 8.070 [2.842, 13.298] |  | 1.055 | 4 | 5 | bab8bc6a |
| loco | start_points | overall | rmse_h100 | lstm[quantiles=None,loss=huber] | 4.798 [2.128, 7.468] |  | 2.234 | 4 | 5 | a556b7e5 |
| loco | start_points | overall | rmse_h100 | lstm[quantiles=None,loss=mse] | 6.248 [3.555, 9.672] |  | 3.534 | 4 | 5 | 97861f32 |
| loco | start_points | overall | rmse_h100 | lstm[revin=True] | 7.324 [3.423, 11.212] |  | 2.001 | 4 | 5 | c17ed23c |
| loco | start_points | overall | rmse_h100 | transformer | 6.531 [4.021, 9.684] |  | 4.844 | 4 | 5 | 20605e71 |
| loco | start_points | overall | rmse_h25 | itransformer[loss=huber] | 2.812 [2.333, 3.291] |  | 3.592 | 4 | 5 | ceba4eba |
| loco | start_points | overall | rmse_h25 | itransformer[loss=mse] | 2.946 [2.576, 3.317] |  | 3.539 | 4 | 5 | bab8bc6a |
| loco | start_points | overall | rmse_h25 | lstm[quantiles=None,loss=huber] | 3.760 [2.641, 4.879] |  | 4.456 | 4 | 5 | a556b7e5 |
| loco | start_points | overall | rmse_h25 | lstm[quantiles=None,loss=mse] | 4.386 [3.485, 5.479] |  | 4.449 | 4 | 5 | 97861f32 |
| loco | start_points | overall | rmse_h25 | lstm[revin=True] | 2.926 [2.085, 4.067] |  | 2.845 | 4 | 5 | c17ed23c |
| loco | start_points | overall | rmse_h25 | transformer | 2.705 [2.164, 3.160] |  | 3.172 | 4 | 5 | 20605e71 |
| loco | start_points | overall | rmse_h50 | itransformer[loss=huber] | 4.515 [2.674, 6.357] |  | 2.057 | 4 | 5 | ceba4eba |
| loco | start_points | overall | rmse_h50 | itransformer[loss=mse] | 4.664 [2.847, 6.480] |  | 2.557 | 4 | 5 | bab8bc6a |
| loco | start_points | overall | rmse_h50 | lstm[quantiles=None,loss=huber] | 3.490 [2.211, 5.231] |  | 3.196 | 4 | 5 | a556b7e5 |
| loco | start_points | overall | rmse_h50 | lstm[quantiles=None,loss=mse] | 5.075 [3.777, 6.569] |  | 3.228 | 4 | 5 | 97861f32 |
| loco | start_points | overall | rmse_h50 | lstm[revin=True] | 4.946 [3.590, 6.188] |  | 2.726 | 4 | 5 | c17ed23c |
| loco | start_points | overall | rmse_h50 | transformer | 3.917 [3.179, 5.013] |  | 3.305 | 4 | 5 | 20605e71 |

</details>

<details><summary>toyota_forecast (360 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rmse_h1 | itransformer[loss=huber] | 0.127 [0.075, 0.187] |  |  | 43 | 5 | 8b749e84 |
| test1 | all | overall | rmse_h1 | itransformer[loss=mse] | 0.128 [0.076, 0.189] |  |  | 43 | 5 | 34919877 |
| test1 | all | overall | rmse_h1 | lstm[quantiles=None,loss=huber] | 0.218 [0.168, 0.274] |  |  | 43 | 5 | f7c2b05c |
| test1 | all | overall | rmse_h1 | lstm[quantiles=None,loss=mse] | 0.242 [0.191, 0.299] |  |  | 43 | 5 | 7ddb85ea |
| test1 | all | overall | rmse_h1 | lstm[revin=True] | 0.134 [0.079, 0.197] |  |  | 43 | 5 | 61016dbc |
| test1 | all | overall | rmse_h1 | transformer | 0.137 [0.081, 0.203] |  |  | 43 | 5 | f64a10ee |
| test1 | all | overall | rmse_h10 | itransformer[loss=huber] | 0.170 [0.116, 0.233] |  |  | 43 | 5 | 8b749e84 |
| test1 | all | overall | rmse_h10 | itransformer[loss=mse] | 0.172 [0.119, 0.234] |  |  | 43 | 5 | 34919877 |
| test1 | all | overall | rmse_h10 | lstm[quantiles=None,loss=huber] | 0.235 [0.177, 0.300] |  |  | 43 | 5 | f7c2b05c |
| test1 | all | overall | rmse_h10 | lstm[quantiles=None,loss=mse] | 0.244 [0.192, 0.302] |  |  | 43 | 5 | 7ddb85ea |
| test1 | all | overall | rmse_h10 | lstm[revin=True] | 0.215 [0.156, 0.280] |  |  | 43 | 5 | 61016dbc |
| test1 | all | overall | rmse_h10 | transformer | 0.284 [0.198, 0.385] |  |  | 43 | 5 | f64a10ee |
| test1 | all | overall | rmse_h100 | itransformer[loss=huber] | 1.026 [0.790, 1.353] |  |  | 43 | 5 | 8b749e84 |
| test1 | all | overall | rmse_h100 | itransformer[loss=mse] | 0.998 [0.774, 1.319] |  |  | 43 | 5 | 34919877 |
| test1 | all | overall | rmse_h100 | lstm[quantiles=None,loss=huber] | 1.549 [1.288, 1.823] |  |  | 43 | 5 | f7c2b05c |
| test1 | all | overall | rmse_h100 | lstm[quantiles=None,loss=mse] | 1.210 [1.047, 1.384] |  |  | 43 | 5 | 7ddb85ea |
| test1 | all | overall | rmse_h100 | lstm[revin=True] | 2.713 [2.282, 3.202] |  |  | 43 | 5 | 61016dbc |
| test1 | all | overall | rmse_h100 | transformer | 3.764 [3.274, 4.321] |  |  | 43 | 5 | f64a10ee |
| test1 | all | overall | rmse_h200 | itransformer[loss=huber] | 2.763 [2.344, 3.186] |  |  | 42 | 5 | 8b749e84 |
| test1 | all | overall | rmse_h200 | itransformer[loss=mse] | 2.492 [2.123, 2.865] |  |  | 42 | 5 | 34919877 |
| test1 | all | overall | rmse_h200 | lstm[quantiles=None,loss=huber] | 3.367 [2.952, 3.791] |  |  | 42 | 5 | f7c2b05c |
| test1 | all | overall | rmse_h200 | lstm[quantiles=None,loss=mse] | 2.632 [2.335, 2.945] |  |  | 42 | 5 | 7ddb85ea |
| test1 | all | overall | rmse_h200 | lstm[revin=True] | 5.593 [5.040, 6.163] |  |  | 42 | 5 | 61016dbc |
| test1 | all | overall | rmse_h200 | transformer | 5.957 [5.373, 6.560] |  |  | 42 | 5 | f64a10ee |
| test1 | all | overall | rmse_h50 | itransformer[loss=huber] | 0.448 [0.351, 0.564] |  |  | 43 | 5 | 8b749e84 |
| test1 | all | overall | rmse_h50 | itransformer[loss=mse] | 0.454 [0.361, 0.566] |  |  | 43 | 5 | 34919877 |
| test1 | all | overall | rmse_h50 | lstm[quantiles=None,loss=huber] | 0.704 [0.565, 0.858] |  |  | 43 | 5 | f7c2b05c |
| test1 | all | overall | rmse_h50 | lstm[quantiles=None,loss=mse] | 0.576 [0.491, 0.668] |  |  | 43 | 5 | 7ddb85ea |
| test1 | all | overall | rmse_h50 | lstm[revin=True] | 0.914 [0.752, 1.086] |  |  | 43 | 5 | 61016dbc |
| test1 | all | overall | rmse_h50 | transformer | 1.764 [1.528, 2.016] |  |  | 43 | 5 | f64a10ee |
| test1 | start_points | fixed:100 | rmse_h1 | itransformer[loss=huber] | 0.009 [0.006, 0.013] |  |  | 43 | 5 | 8b749e84 |
| test1 | start_points | fixed:100 | rmse_h1 | itransformer[loss=mse] | 0.010 [0.006, 0.014] |  |  | 43 | 5 | 34919877 |
| test1 | start_points | fixed:100 | rmse_h1 | lstm[quantiles=None,loss=huber] | 0.038 [0.028, 0.050] |  |  | 43 | 5 | f7c2b05c |
| test1 | start_points | fixed:100 | rmse_h1 | lstm[quantiles=None,loss=mse] | 0.071 [0.059, 0.086] |  |  | 43 | 5 | 7ddb85ea |
| test1 | start_points | fixed:100 | rmse_h1 | lstm[revin=True] | 0.010 [0.006, 0.015] |  |  | 43 | 5 | 61016dbc |
| test1 | start_points | fixed:100 | rmse_h1 | transformer | 0.012 [0.009, 0.016] |  |  | 43 | 5 | f64a10ee |
| test1 | start_points | fixed:100 | rmse_h10 | itransformer[loss=huber] | 0.021 [0.012, 0.033] |  |  | 43 | 5 | 8b749e84 |
| test1 | start_points | fixed:100 | rmse_h10 | itransformer[loss=mse] | 0.019 [0.011, 0.028] |  |  | 43 | 5 | 34919877 |
| test1 | start_points | fixed:100 | rmse_h10 | lstm[quantiles=None,loss=huber] | 0.052 [0.040, 0.066] |  |  | 43 | 5 | f7c2b05c |
| test1 | start_points | fixed:100 | rmse_h10 | lstm[quantiles=None,loss=mse] | 0.083 [0.069, 0.100] |  |  | 43 | 5 | 7ddb85ea |
| test1 | start_points | fixed:100 | rmse_h10 | lstm[revin=True] | 0.029 [0.024, 0.036] |  |  | 43 | 5 | 61016dbc |
| test1 | start_points | fixed:100 | rmse_h10 | transformer | 0.121 [0.108, 0.133] |  |  | 43 | 5 | f64a10ee |
| test1 | start_points | fixed:100 | rmse_h100 | itransformer[loss=huber] | 0.180 [0.140, 0.225] |  |  | 42 | 5 | 8b749e84 |
| test1 | start_points | fixed:100 | rmse_h100 | itransformer[loss=mse] | 0.196 [0.148, 0.251] |  |  | 42 | 5 | 34919877 |
| test1 | start_points | fixed:100 | rmse_h100 | lstm[quantiles=None,loss=huber] | 0.197 [0.149, 0.254] |  |  | 42 | 5 | f7c2b05c |
| test1 | start_points | fixed:100 | rmse_h100 | lstm[quantiles=None,loss=mse] | 0.302 [0.212, 0.414] |  |  | 42 | 5 | 7ddb85ea |
| test1 | start_points | fixed:100 | rmse_h100 | lstm[revin=True] | 0.346 [0.234, 0.487] |  |  | 42 | 5 | 61016dbc |
| test1 | start_points | fixed:100 | rmse_h100 | transformer | 0.468 [0.281, 0.710] |  |  | 42 | 5 | f64a10ee |
| test1 | start_points | fixed:100 | rmse_h200 | itransformer[loss=huber] | 0.537 [0.392, 0.706] |  |  | 42 | 5 | 8b749e84 |
| test1 | start_points | fixed:100 | rmse_h200 | itransformer[loss=mse] | 0.664 [0.478, 0.875] |  |  | 42 | 5 | 34919877 |
| test1 | start_points | fixed:100 | rmse_h200 | lstm[quantiles=None,loss=huber] | 0.677 [0.514, 0.897] |  |  | 42 | 5 | f7c2b05c |
| test1 | start_points | fixed:100 | rmse_h200 | lstm[quantiles=None,loss=mse] | 0.864 [0.565, 1.243] |  |  | 42 | 5 | 7ddb85ea |
| test1 | start_points | fixed:100 | rmse_h200 | lstm[revin=True] | 1.638 [1.201, 2.174] |  |  | 42 | 5 | 61016dbc |
| test1 | start_points | fixed:100 | rmse_h200 | transformer | 1.521 [1.029, 2.139] |  |  | 42 | 5 | f64a10ee |
| test1 | start_points | fixed:100 | rmse_h50 | itransformer[loss=huber] | 0.099 [0.046, 0.191] |  |  | 43 | 5 | 8b749e84 |
| test1 | start_points | fixed:100 | rmse_h50 | itransformer[loss=mse] | 0.095 [0.049, 0.171] |  |  | 43 | 5 | 34919877 |
| test1 | start_points | fixed:100 | rmse_h50 | lstm[quantiles=None,loss=huber] | 0.111 [0.068, 0.178] |  |  | 43 | 5 | f7c2b05c |
| test1 | start_points | fixed:100 | rmse_h50 | lstm[quantiles=None,loss=mse] | 0.122 [0.085, 0.166] |  |  | 43 | 5 | 7ddb85ea |
| test1 | start_points | fixed:100 | rmse_h50 | lstm[revin=True] | 0.151 [0.107, 0.212] |  |  | 43 | 5 | 61016dbc |
| test1 | start_points | fixed:100 | rmse_h50 | transformer | 0.411 [0.240, 0.694] |  |  | 43 | 5 | f64a10ee |
| test1 | start_points | frac:0.3 | rmse_h1 | itransformer[loss=huber] | 0.017 [0.012, 0.024] |  |  | 43 | 5 | 8b749e84 |
| test1 | start_points | frac:0.3 | rmse_h1 | itransformer[loss=mse] | 0.018 [0.012, 0.026] |  |  | 43 | 5 | 34919877 |
| test1 | start_points | frac:0.3 | rmse_h1 | lstm[quantiles=None,loss=huber] | 0.089 [0.056, 0.132] |  |  | 43 | 5 | f7c2b05c |
| test1 | start_points | frac:0.3 | rmse_h1 | lstm[quantiles=None,loss=mse] | 0.102 [0.065, 0.151] |  |  | 43 | 5 | 7ddb85ea |
| test1 | start_points | frac:0.3 | rmse_h1 | lstm[revin=True] | 0.016 [0.010, 0.024] |  |  | 43 | 5 | 61016dbc |
| test1 | start_points | frac:0.3 | rmse_h1 | transformer | 0.018 [0.012, 0.025] |  |  | 43 | 5 | f64a10ee |
| test1 | start_points | frac:0.3 | rmse_h10 | itransformer[loss=huber] | 0.048 [0.029, 0.073] |  |  | 43 | 5 | 8b749e84 |
| test1 | start_points | frac:0.3 | rmse_h10 | itransformer[loss=mse] | 0.051 [0.029, 0.077] |  |  | 43 | 5 | 34919877 |
| test1 | start_points | frac:0.3 | rmse_h10 | lstm[quantiles=None,loss=huber] | 0.101 [0.060, 0.161] |  |  | 43 | 5 | f7c2b05c |
| test1 | start_points | frac:0.3 | rmse_h10 | lstm[quantiles=None,loss=mse] | 0.098 [0.071, 0.133] |  |  | 43 | 5 | 7ddb85ea |
| test1 | start_points | frac:0.3 | rmse_h10 | lstm[revin=True] | 0.051 [0.030, 0.081] |  |  | 43 | 5 | 61016dbc |
| test1 | start_points | frac:0.3 | rmse_h10 | transformer | 0.110 [0.091, 0.131] |  |  | 43 | 5 | f64a10ee |
| test1 | start_points | frac:0.3 | rmse_h100 | itransformer[loss=huber] | 0.311 [0.233, 0.398] |  |  | 43 | 5 | 8b749e84 |
| test1 | start_points | frac:0.3 | rmse_h100 | itransformer[loss=mse] | 0.372 [0.244, 0.543] |  |  | 43 | 5 | 34919877 |
| test1 | start_points | frac:0.3 | rmse_h100 | lstm[quantiles=None,loss=huber] | 0.568 [0.357, 0.838] |  |  | 43 | 5 | f7c2b05c |
| test1 | start_points | frac:0.3 | rmse_h100 | lstm[quantiles=None,loss=mse] | 0.586 [0.405, 0.797] |  |  | 43 | 5 | 7ddb85ea |
| test1 | start_points | frac:0.3 | rmse_h100 | lstm[revin=True] | 0.656 [0.343, 1.174] |  |  | 43 | 5 | 61016dbc |
| test1 | start_points | frac:0.3 | rmse_h100 | transformer | 0.890 [0.465, 1.547] |  |  | 43 | 5 | f64a10ee |
| test1 | start_points | frac:0.3 | rmse_h200 | itransformer[loss=huber] | 0.945 [0.655, 1.265] |  |  | 42 | 5 | 8b749e84 |
| test1 | start_points | frac:0.3 | rmse_h200 | itransformer[loss=mse] | 1.093 [0.774, 1.438] |  |  | 42 | 5 | 34919877 |
| test1 | start_points | frac:0.3 | rmse_h200 | lstm[quantiles=None,loss=huber] | 1.047 [0.810, 1.319] |  |  | 42 | 5 | f7c2b05c |
| test1 | start_points | frac:0.3 | rmse_h200 | lstm[quantiles=None,loss=mse] | 1.552 [1.130, 2.052] |  |  | 42 | 5 | 7ddb85ea |
| test1 | start_points | frac:0.3 | rmse_h200 | lstm[revin=True] | 2.224 [1.757, 2.763] |  |  | 42 | 5 | 61016dbc |
| test1 | start_points | frac:0.3 | rmse_h200 | transformer | 2.209 [1.677, 2.827] |  |  | 42 | 5 | f64a10ee |
| test1 | start_points | frac:0.3 | rmse_h50 | itransformer[loss=huber] | 0.103 [0.077, 0.133] |  |  | 43 | 5 | 8b749e84 |
| test1 | start_points | frac:0.3 | rmse_h50 | itransformer[loss=mse] | 0.120 [0.085, 0.163] |  |  | 43 | 5 | 34919877 |
| test1 | start_points | frac:0.3 | rmse_h50 | lstm[quantiles=None,loss=huber] | 0.198 [0.131, 0.282] |  |  | 43 | 5 | f7c2b05c |
| test1 | start_points | frac:0.3 | rmse_h50 | lstm[quantiles=None,loss=mse] | 0.195 [0.132, 0.274] |  |  | 43 | 5 | 7ddb85ea |
| test1 | start_points | frac:0.3 | rmse_h50 | lstm[revin=True] | 0.223 [0.102, 0.398] |  |  | 43 | 5 | 61016dbc |
| test1 | start_points | frac:0.3 | rmse_h50 | transformer | 0.374 [0.208, 0.602] |  |  | 43 | 5 | f64a10ee |
| test1 | start_points | frac:0.5 | rmse_h1 | itransformer[loss=huber] | 0.042 [0.025, 0.062] |  |  | 43 | 5 | 8b749e84 |
| test1 | start_points | frac:0.5 | rmse_h1 | itransformer[loss=mse] | 0.038 [0.022, 0.057] |  |  | 43 | 5 | 34919877 |
| test1 | start_points | frac:0.5 | rmse_h1 | lstm[quantiles=None,loss=huber] | 0.173 [0.094, 0.287] |  |  | 43 | 5 | f7c2b05c |
| test1 | start_points | frac:0.5 | rmse_h1 | lstm[quantiles=None,loss=mse] | 0.203 [0.111, 0.330] |  |  | 43 | 5 | 7ddb85ea |
| test1 | start_points | frac:0.5 | rmse_h1 | lstm[revin=True] | 0.035 [0.021, 0.053] |  |  | 43 | 5 | 61016dbc |
| test1 | start_points | frac:0.5 | rmse_h1 | transformer | 0.046 [0.022, 0.077] |  |  | 43 | 5 | f64a10ee |
| test1 | start_points | frac:0.5 | rmse_h10 | itransformer[loss=huber] | 0.086 [0.058, 0.120] |  |  | 43 | 5 | 8b749e84 |
| test1 | start_points | frac:0.5 | rmse_h10 | itransformer[loss=mse] | 0.081 [0.055, 0.110] |  |  | 43 | 5 | 34919877 |
| test1 | start_points | frac:0.5 | rmse_h10 | lstm[quantiles=None,loss=huber] | 0.198 [0.101, 0.325] |  |  | 43 | 5 | f7c2b05c |
| test1 | start_points | frac:0.5 | rmse_h10 | lstm[quantiles=None,loss=mse] | 0.186 [0.123, 0.268] |  |  | 43 | 5 | 7ddb85ea |
| test1 | start_points | frac:0.5 | rmse_h10 | lstm[revin=True] | 0.128 [0.069, 0.200] |  |  | 43 | 5 | 61016dbc |
| test1 | start_points | frac:0.5 | rmse_h10 | transformer | 0.351 [0.097, 0.671] |  |  | 43 | 5 | f64a10ee |
| test1 | start_points | frac:0.5 | rmse_h100 | itransformer[loss=huber] | 0.786 [0.438, 1.233] |  |  | 42 | 5 | 8b749e84 |
| test1 | start_points | frac:0.5 | rmse_h100 | itransformer[loss=mse] | 0.690 [0.440, 0.975] |  |  | 42 | 5 | 34919877 |
| test1 | start_points | frac:0.5 | rmse_h100 | lstm[quantiles=None,loss=huber] | 1.146 [0.597, 1.927] |  |  | 42 | 5 | f7c2b05c |
| test1 | start_points | frac:0.5 | rmse_h100 | lstm[quantiles=None,loss=mse] | 0.920 [0.617, 1.273] |  |  | 42 | 5 | 7ddb85ea |
| test1 | start_points | frac:0.5 | rmse_h100 | lstm[revin=True] | 1.046 [0.705, 1.446] |  |  | 42 | 5 | 61016dbc |
| test1 | start_points | frac:0.5 | rmse_h100 | transformer | 1.829 [1.139, 2.703] |  |  | 42 | 5 | f64a10ee |
| test1 | start_points | frac:0.5 | rmse_h200 | itransformer[loss=huber] | 2.665 [1.749, 3.820] |  |  | 41 | 5 | 8b749e84 |
| test1 | start_points | frac:0.5 | rmse_h200 | itransformer[loss=mse] | 2.291 [1.625, 3.017] |  |  | 41 | 5 | 34919877 |
| test1 | start_points | frac:0.5 | rmse_h200 | lstm[quantiles=None,loss=huber] | 2.767 [1.983, 3.654] |  |  | 41 | 5 | f7c2b05c |
| test1 | start_points | frac:0.5 | rmse_h200 | lstm[quantiles=None,loss=mse] | 2.229 [1.779, 2.734] |  |  | 41 | 5 | 7ddb85ea |
| test1 | start_points | frac:0.5 | rmse_h200 | lstm[revin=True] | 4.962 [3.957, 6.017] |  |  | 41 | 5 | 61016dbc |
| test1 | start_points | frac:0.5 | rmse_h200 | transformer | 5.443 [4.382, 6.550] |  |  | 41 | 5 | f64a10ee |
| test1 | start_points | frac:0.5 | rmse_h50 | itransformer[loss=huber] | 0.304 [0.177, 0.454] |  |  | 43 | 5 | 8b749e84 |
| test1 | start_points | frac:0.5 | rmse_h50 | itransformer[loss=mse] | 0.260 [0.171, 0.365] |  |  | 43 | 5 | 34919877 |
| test1 | start_points | frac:0.5 | rmse_h50 | lstm[quantiles=None,loss=huber] | 0.634 [0.269, 1.184] |  |  | 43 | 5 | f7c2b05c |
| test1 | start_points | frac:0.5 | rmse_h50 | lstm[quantiles=None,loss=mse] | 0.442 [0.296, 0.626] |  |  | 43 | 5 | 7ddb85ea |
| test1 | start_points | frac:0.5 | rmse_h50 | lstm[revin=True] | 0.482 [0.203, 0.824] |  |  | 43 | 5 | 61016dbc |
| test1 | start_points | frac:0.5 | rmse_h50 | transformer | 1.099 [0.389, 1.976] |  |  | 43 | 5 | f64a10ee |
| test1 | start_points | frac:0.7 | rmse_h1 | itransformer[loss=huber] | 0.051 [0.028, 0.082] |  |  | 43 | 5 | 8b749e84 |
| test1 | start_points | frac:0.7 | rmse_h1 | itransformer[loss=mse] | 0.053 [0.029, 0.085] |  |  | 43 | 5 | 34919877 |
| test1 | start_points | frac:0.7 | rmse_h1 | lstm[quantiles=None,loss=huber] | 0.146 [0.125, 0.176] |  |  | 43 | 5 | f7c2b05c |
| test1 | start_points | frac:0.7 | rmse_h1 | lstm[quantiles=None,loss=mse] | 0.143 [0.115, 0.182] |  |  | 43 | 5 | 7ddb85ea |
| test1 | start_points | frac:0.7 | rmse_h1 | lstm[revin=True] | 0.054 [0.030, 0.084] |  |  | 43 | 5 | 61016dbc |
| test1 | start_points | frac:0.7 | rmse_h1 | transformer | 0.054 [0.030, 0.086] |  |  | 43 | 5 | f64a10ee |
| test1 | start_points | frac:0.7 | rmse_h10 | itransformer[loss=huber] | 0.110 [0.045, 0.202] |  |  | 43 | 5 | 8b749e84 |
| test1 | start_points | frac:0.7 | rmse_h10 | itransformer[loss=mse] | 0.112 [0.049, 0.203] |  |  | 43 | 5 | 34919877 |
| test1 | start_points | frac:0.7 | rmse_h10 | lstm[quantiles=None,loss=huber] | 0.146 [0.095, 0.218] |  |  | 43 | 5 | f7c2b05c |
| test1 | start_points | frac:0.7 | rmse_h10 | lstm[quantiles=None,loss=mse] | 0.164 [0.116, 0.229] |  |  | 43 | 5 | 7ddb85ea |
| test1 | start_points | frac:0.7 | rmse_h10 | lstm[revin=True] | 0.109 [0.055, 0.185] |  |  | 43 | 5 | 61016dbc |
| test1 | start_points | frac:0.7 | rmse_h10 | transformer | 0.131 [0.075, 0.215] |  |  | 43 | 5 | f64a10ee |
| test1 | start_points | frac:0.7 | rmse_h100 | itransformer[loss=huber] | 0.900 [0.544, 1.408] |  |  | 42 | 5 | 8b749e84 |
| test1 | start_points | frac:0.7 | rmse_h100 | itransformer[loss=mse] | 0.945 [0.600, 1.446] |  |  | 42 | 5 | 34919877 |
| test1 | start_points | frac:0.7 | rmse_h100 | lstm[quantiles=None,loss=huber] | 1.348 [1.005, 1.714] |  |  | 42 | 5 | f7c2b05c |
| test1 | start_points | frac:0.7 | rmse_h100 | lstm[quantiles=None,loss=mse] | 1.154 [0.893, 1.425] |  |  | 42 | 5 | 7ddb85ea |
| test1 | start_points | frac:0.7 | rmse_h100 | lstm[revin=True] | 3.203 [2.672, 3.745] |  |  | 42 | 5 | 61016dbc |
| test1 | start_points | frac:0.7 | rmse_h100 | transformer | 4.399 [3.764, 5.033] |  |  | 42 | 5 | f64a10ee |
| test1 | start_points | frac:0.7 | rmse_h200 | itransformer[loss=huber] | 2.084 [1.416, 2.829] |  |  | 17 | 5 | 8b749e84 |
| test1 | start_points | frac:0.7 | rmse_h200 | itransformer[loss=mse] | 1.488 [0.897, 2.145] |  |  | 17 | 5 | 34919877 |
| test1 | start_points | frac:0.7 | rmse_h200 | lstm[quantiles=None,loss=huber] | 3.869 [3.086, 4.686] |  |  | 17 | 5 | f7c2b05c |
| test1 | start_points | frac:0.7 | rmse_h200 | lstm[quantiles=None,loss=mse] | 1.970 [1.306, 2.649] |  |  | 17 | 5 | 7ddb85ea |
| test1 | start_points | frac:0.7 | rmse_h200 | lstm[revin=True] | 7.826 [6.216, 9.391] |  |  | 17 | 5 | 61016dbc |
| test1 | start_points | frac:0.7 | rmse_h200 | transformer | 8.297 [6.588, 9.963] |  |  | 17 | 5 | f64a10ee |
| test1 | start_points | frac:0.7 | rmse_h50 | itransformer[loss=huber] | 0.336 [0.184, 0.563] |  |  | 43 | 5 | 8b749e84 |
| test1 | start_points | frac:0.7 | rmse_h50 | itransformer[loss=mse] | 0.361 [0.212, 0.587] |  |  | 43 | 5 | 34919877 |
| test1 | start_points | frac:0.7 | rmse_h50 | lstm[quantiles=None,loss=huber] | 0.355 [0.270, 0.452] |  |  | 43 | 5 | f7c2b05c |
| test1 | start_points | frac:0.7 | rmse_h50 | lstm[quantiles=None,loss=mse] | 0.371 [0.279, 0.486] |  |  | 43 | 5 | 7ddb85ea |
| test1 | start_points | frac:0.7 | rmse_h50 | lstm[revin=True] | 0.583 [0.484, 0.681] |  |  | 43 | 5 | 61016dbc |
| test1 | start_points | frac:0.7 | rmse_h50 | transformer | 1.240 [1.018, 1.518] |  |  | 43 | 5 | f64a10ee |
| test1 | start_points | overall | rmse_h1 | itransformer[loss=huber] | 0.043 [0.029, 0.060] |  |  | 43 | 5 | 8b749e84 |
| test1 | start_points | overall | rmse_h1 | itransformer[loss=mse] | 0.042 [0.029, 0.059] |  |  | 43 | 5 | 34919877 |
| test1 | start_points | overall | rmse_h1 | lstm[quantiles=None,loss=huber] | 0.155 [0.112, 0.212] |  |  | 43 | 5 | f7c2b05c |
| test1 | start_points | overall | rmse_h1 | lstm[quantiles=None,loss=mse] | 0.175 [0.124, 0.239] |  |  | 43 | 5 | 7ddb85ea |
| test1 | start_points | overall | rmse_h1 | lstm[revin=True] | 0.041 [0.027, 0.057] |  |  | 43 | 5 | 61016dbc |
| test1 | start_points | overall | rmse_h1 | transformer | 0.046 [0.029, 0.066] |  |  | 43 | 5 | f64a10ee |
| test1 | start_points | overall | rmse_h10 | itransformer[loss=huber] | 0.095 [0.059, 0.141] |  |  | 43 | 5 | 8b749e84 |
| test1 | start_points | overall | rmse_h10 | itransformer[loss=mse] | 0.094 [0.060, 0.140] |  |  | 43 | 5 | 34919877 |
| test1 | start_points | overall | rmse_h10 | lstm[quantiles=None,loss=huber] | 0.175 [0.117, 0.245] |  |  | 43 | 5 | f7c2b05c |
| test1 | start_points | overall | rmse_h10 | lstm[quantiles=None,loss=mse] | 0.175 [0.134, 0.222] |  |  | 43 | 5 | 7ddb85ea |
| test1 | start_points | overall | rmse_h10 | lstm[revin=True] | 0.117 [0.077, 0.163] |  |  | 43 | 5 | 61016dbc |
| test1 | start_points | overall | rmse_h10 | transformer | 0.257 [0.135, 0.409] |  |  | 43 | 5 | f64a10ee |
| test1 | start_points | overall | rmse_h100 | itransformer[loss=huber] | 0.775 [0.544, 1.062] |  |  | 43 | 5 | 8b749e84 |
| test1 | start_points | overall | rmse_h100 | itransformer[loss=mse] | 0.789 [0.562, 1.061] |  |  | 43 | 5 | 34919877 |
| test1 | start_points | overall | rmse_h100 | lstm[quantiles=None,loss=huber] | 1.237 [0.920, 1.627] |  |  | 43 | 5 | f7c2b05c |
| test1 | start_points | overall | rmse_h100 | lstm[quantiles=None,loss=mse] | 1.000 [0.811, 1.205] |  |  | 43 | 5 | 7ddb85ea |
| test1 | start_points | overall | rmse_h100 | lstm[revin=True] | 1.993 [1.581, 2.503] |  |  | 43 | 5 | 61016dbc |
| test1 | start_points | overall | rmse_h100 | transformer | 2.802 [2.239, 3.478] |  |  | 43 | 5 | f64a10ee |
| test1 | start_points | overall | rmse_h200 | itransformer[loss=huber] | 1.980 [1.523, 2.533] |  |  | 42 | 5 | 8b749e84 |
| test1 | start_points | overall | rmse_h200 | itransformer[loss=mse] | 1.731 [1.365, 2.129] |  |  | 42 | 5 | 34919877 |
| test1 | start_points | overall | rmse_h200 | lstm[quantiles=None,loss=huber] | 2.410 [2.005, 2.827] |  |  | 42 | 5 | f7c2b05c |
| test1 | start_points | overall | rmse_h200 | lstm[quantiles=None,loss=mse] | 1.900 [1.575, 2.268] |  |  | 42 | 5 | 7ddb85ea |
| test1 | start_points | overall | rmse_h200 | lstm[revin=True] | 4.551 [3.989, 5.108] |  |  | 42 | 5 | 61016dbc |
| test1 | start_points | overall | rmse_h200 | transformer | 4.857 [4.273, 5.456] |  |  | 42 | 5 | f64a10ee |
| test1 | start_points | overall | rmse_h50 | itransformer[loss=huber] | 0.292 [0.187, 0.425] |  |  | 43 | 5 | 8b749e84 |
| test1 | start_points | overall | rmse_h50 | itransformer[loss=mse] | 0.280 [0.186, 0.400] |  |  | 43 | 5 | 34919877 |
| test1 | start_points | overall | rmse_h50 | lstm[quantiles=None,loss=huber] | 0.474 [0.292, 0.743] |  |  | 43 | 5 | f7c2b05c |
| test1 | start_points | overall | rmse_h50 | lstm[quantiles=None,loss=mse] | 0.375 [0.288, 0.472] |  |  | 43 | 5 | 7ddb85ea |
| test1 | start_points | overall | rmse_h50 | lstm[revin=True] | 0.518 [0.374, 0.685] |  |  | 43 | 5 | 61016dbc |
| test1 | start_points | overall | rmse_h50 | transformer | 1.082 [0.717, 1.529] |  |  | 43 | 5 | f64a10ee |
| test2 | all | overall | rmse_h1 | itransformer[loss=huber] | 0.017 [0.015, 0.019] |  |  | 40 | 5 | 8b749e84 |
| test2 | all | overall | rmse_h1 | itransformer[loss=mse] | 0.016 [0.014, 0.019] |  |  | 40 | 5 | 34919877 |
| test2 | all | overall | rmse_h1 | lstm[quantiles=None,loss=huber] | 0.098 [0.092, 0.104] |  |  | 40 | 5 | f7c2b05c |
| test2 | all | overall | rmse_h1 | lstm[quantiles=None,loss=mse] | 0.159 [0.150, 0.168] |  |  | 40 | 5 | 7ddb85ea |
| test2 | all | overall | rmse_h1 | lstm[revin=True] | 0.017 [0.014, 0.020] |  |  | 40 | 5 | 61016dbc |
| test2 | all | overall | rmse_h1 | transformer | 0.018 [0.015, 0.021] |  |  | 40 | 5 | f64a10ee |
| test2 | all | overall | rmse_h10 | itransformer[loss=huber] | 0.041 [0.037, 0.046] |  |  | 40 | 5 | 8b749e84 |
| test2 | all | overall | rmse_h10 | itransformer[loss=mse] | 0.038 [0.034, 0.043] |  |  | 40 | 5 | 34919877 |
| test2 | all | overall | rmse_h10 | lstm[quantiles=None,loss=huber] | 0.088 [0.083, 0.095] |  |  | 40 | 5 | f7c2b05c |
| test2 | all | overall | rmse_h10 | lstm[quantiles=None,loss=mse] | 0.130 [0.122, 0.140] |  |  | 40 | 5 | 7ddb85ea |
| test2 | all | overall | rmse_h10 | lstm[revin=True] | 0.059 [0.053, 0.064] |  |  | 40 | 5 | 61016dbc |
| test2 | all | overall | rmse_h10 | transformer | 0.109 [0.105, 0.113] |  |  | 40 | 5 | f64a10ee |
| test2 | all | overall | rmse_h100 | itransformer[loss=huber] | 0.529 [0.467, 0.592] |  |  | 40 | 5 | 8b749e84 |
| test2 | all | overall | rmse_h100 | itransformer[loss=mse] | 0.506 [0.445, 0.569] |  |  | 40 | 5 | 34919877 |
| test2 | all | overall | rmse_h100 | lstm[quantiles=None,loss=huber] | 0.672 [0.614, 0.734] |  |  | 40 | 5 | f7c2b05c |
| test2 | all | overall | rmse_h100 | lstm[quantiles=None,loss=mse] | 0.748 [0.676, 0.824] |  |  | 40 | 5 | 7ddb85ea |
| test2 | all | overall | rmse_h100 | lstm[revin=True] | 1.250 [1.124, 1.370] |  |  | 40 | 5 | 61016dbc |
| test2 | all | overall | rmse_h100 | transformer | 1.930 [1.804, 2.046] |  |  | 40 | 5 | f64a10ee |
| test2 | all | overall | rmse_h200 | itransformer[loss=huber] | 1.198 [1.074, 1.331] |  |  | 40 | 5 | 8b749e84 |
| test2 | all | overall | rmse_h200 | itransformer[loss=mse] | 1.113 [0.960, 1.296] |  |  | 40 | 5 | 34919877 |
| test2 | all | overall | rmse_h200 | lstm[quantiles=None,loss=huber] | 1.592 [1.476, 1.704] |  |  | 40 | 5 | f7c2b05c |
| test2 | all | overall | rmse_h200 | lstm[quantiles=None,loss=mse] | 1.666 [1.495, 1.853] |  |  | 40 | 5 | 7ddb85ea |
| test2 | all | overall | rmse_h200 | lstm[revin=True] | 3.143 [2.967, 3.305] |  |  | 40 | 5 | 61016dbc |
| test2 | all | overall | rmse_h200 | transformer | 3.300 [3.114, 3.481] |  |  | 40 | 5 | f64a10ee |
| test2 | all | overall | rmse_h50 | itransformer[loss=huber] | 0.227 [0.194, 0.261] |  |  | 40 | 5 | 8b749e84 |
| test2 | all | overall | rmse_h50 | itransformer[loss=mse] | 0.214 [0.184, 0.244] |  |  | 40 | 5 | 34919877 |
| test2 | all | overall | rmse_h50 | lstm[quantiles=None,loss=huber] | 0.287 [0.259, 0.316] |  |  | 40 | 5 | f7c2b05c |
| test2 | all | overall | rmse_h50 | lstm[quantiles=None,loss=mse] | 0.382 [0.352, 0.413] |  |  | 40 | 5 | 7ddb85ea |
| test2 | all | overall | rmse_h50 | lstm[revin=True] | 0.385 [0.337, 0.435] |  |  | 40 | 5 | 61016dbc |
| test2 | all | overall | rmse_h50 | transformer | 0.866 [0.802, 0.927] |  |  | 40 | 5 | f64a10ee |
| test2 | start_points | fixed:100 | rmse_h1 | itransformer[loss=huber] | 0.009 [0.004, 0.015] |  |  | 40 | 5 | 8b749e84 |
| test2 | start_points | fixed:100 | rmse_h1 | itransformer[loss=mse] | 0.008 [0.004, 0.016] |  |  | 40 | 5 | 34919877 |
| test2 | start_points | fixed:100 | rmse_h1 | lstm[quantiles=None,loss=huber] | 0.045 [0.037, 0.055] |  |  | 40 | 5 | f7c2b05c |
| test2 | start_points | fixed:100 | rmse_h1 | lstm[quantiles=None,loss=mse] | 0.090 [0.081, 0.101] |  |  | 40 | 5 | 7ddb85ea |
| test2 | start_points | fixed:100 | rmse_h1 | lstm[revin=True] | 0.010 [0.004, 0.018] |  |  | 40 | 5 | 61016dbc |
| test2 | start_points | fixed:100 | rmse_h1 | transformer | 0.012 [0.006, 0.020] |  |  | 40 | 5 | f64a10ee |
| test2 | start_points | fixed:100 | rmse_h10 | itransformer[loss=huber] | 0.020 [0.011, 0.030] |  |  | 40 | 5 | 8b749e84 |
| test2 | start_points | fixed:100 | rmse_h10 | itransformer[loss=mse] | 0.021 [0.012, 0.032] |  |  | 40 | 5 | 34919877 |
| test2 | start_points | fixed:100 | rmse_h10 | lstm[quantiles=None,loss=huber] | 0.054 [0.046, 0.062] |  |  | 40 | 5 | f7c2b05c |
| test2 | start_points | fixed:100 | rmse_h10 | lstm[quantiles=None,loss=mse] | 0.097 [0.088, 0.107] |  |  | 40 | 5 | 7ddb85ea |
| test2 | start_points | fixed:100 | rmse_h10 | lstm[revin=True] | 0.045 [0.036, 0.057] |  |  | 40 | 5 | 61016dbc |
| test2 | start_points | fixed:100 | rmse_h10 | transformer | 0.139 [0.123, 0.154] |  |  | 40 | 5 | f64a10ee |
| test2 | start_points | fixed:100 | rmse_h100 | itransformer[loss=huber] | 0.085 [0.059, 0.115] |  |  | 40 | 5 | 8b749e84 |
| test2 | start_points | fixed:100 | rmse_h100 | itransformer[loss=mse] | 0.127 [0.084, 0.180] |  |  | 40 | 5 | 34919877 |
| test2 | start_points | fixed:100 | rmse_h100 | lstm[quantiles=None,loss=huber] | 0.184 [0.137, 0.236] |  |  | 40 | 5 | f7c2b05c |
| test2 | start_points | fixed:100 | rmse_h100 | lstm[quantiles=None,loss=mse] | 0.500 [0.437, 0.567] |  |  | 40 | 5 | 7ddb85ea |
| test2 | start_points | fixed:100 | rmse_h100 | lstm[revin=True] | 0.162 [0.133, 0.191] |  |  | 40 | 5 | 61016dbc |
| test2 | start_points | fixed:100 | rmse_h100 | transformer | 0.283 [0.196, 0.396] |  |  | 40 | 5 | f64a10ee |
| test2 | start_points | fixed:100 | rmse_h200 | itransformer[loss=huber] | 0.334 [0.238, 0.446] |  |  | 40 | 5 | 8b749e84 |
| test2 | start_points | fixed:100 | rmse_h200 | itransformer[loss=mse] | 0.512 [0.364, 0.700] |  |  | 40 | 5 | 34919877 |
| test2 | start_points | fixed:100 | rmse_h200 | lstm[quantiles=None,loss=huber] | 0.409 [0.323, 0.508] |  |  | 40 | 5 | f7c2b05c |
| test2 | start_points | fixed:100 | rmse_h200 | lstm[quantiles=None,loss=mse] | 1.179 [0.973, 1.403] |  |  | 40 | 5 | 7ddb85ea |
| test2 | start_points | fixed:100 | rmse_h200 | lstm[revin=True] | 0.497 [0.343, 0.696] |  |  | 40 | 5 | 61016dbc |
| test2 | start_points | fixed:100 | rmse_h200 | transformer | 0.391 [0.175, 0.671] |  |  | 40 | 5 | f64a10ee |
| test2 | start_points | fixed:100 | rmse_h50 | itransformer[loss=huber] | 0.050 [0.036, 0.066] |  |  | 40 | 5 | 8b749e84 |
| test2 | start_points | fixed:100 | rmse_h50 | itransformer[loss=mse] | 0.060 [0.043, 0.080] |  |  | 40 | 5 | 34919877 |
| test2 | start_points | fixed:100 | rmse_h50 | lstm[quantiles=None,loss=huber] | 0.090 [0.074, 0.108] |  |  | 40 | 5 | f7c2b05c |
| test2 | start_points | fixed:100 | rmse_h50 | lstm[quantiles=None,loss=mse] | 0.225 [0.202, 0.249] |  |  | 40 | 5 | 7ddb85ea |
| test2 | start_points | fixed:100 | rmse_h50 | lstm[revin=True] | 0.180 [0.163, 0.198] |  |  | 40 | 5 | 61016dbc |
| test2 | start_points | fixed:100 | rmse_h50 | transformer | 0.353 [0.333, 0.376] |  |  | 40 | 5 | f64a10ee |
| test2 | start_points | frac:0.3 | rmse_h1 | itransformer[loss=huber] | 0.015 [0.006, 0.025] |  |  | 40 | 5 | 8b749e84 |
| test2 | start_points | frac:0.3 | rmse_h1 | itransformer[loss=mse] | 0.015 [0.006, 0.026] |  |  | 40 | 5 | 34919877 |
| test2 | start_points | frac:0.3 | rmse_h1 | lstm[quantiles=None,loss=huber] | 0.053 [0.040, 0.069] |  |  | 40 | 5 | f7c2b05c |
| test2 | start_points | frac:0.3 | rmse_h1 | lstm[quantiles=None,loss=mse] | 0.103 [0.089, 0.119] |  |  | 40 | 5 | 7ddb85ea |
| test2 | start_points | frac:0.3 | rmse_h1 | lstm[revin=True] | 0.015 [0.006, 0.026] |  |  | 40 | 5 | 61016dbc |
| test2 | start_points | frac:0.3 | rmse_h1 | transformer | 0.017 [0.008, 0.028] |  |  | 40 | 5 | f64a10ee |
| test2 | start_points | frac:0.3 | rmse_h10 | itransformer[loss=huber] | 0.018 [0.012, 0.026] |  |  | 40 | 5 | 8b749e84 |
| test2 | start_points | frac:0.3 | rmse_h10 | itransformer[loss=mse] | 0.018 [0.011, 0.027] |  |  | 40 | 5 | 34919877 |
| test2 | start_points | frac:0.3 | rmse_h10 | lstm[quantiles=None,loss=huber] | 0.039 [0.031, 0.049] |  |  | 40 | 5 | f7c2b05c |
| test2 | start_points | frac:0.3 | rmse_h10 | lstm[quantiles=None,loss=mse] | 0.058 [0.049, 0.069] |  |  | 40 | 5 | 7ddb85ea |
| test2 | start_points | frac:0.3 | rmse_h10 | lstm[revin=True] | 0.022 [0.015, 0.031] |  |  | 40 | 5 | 61016dbc |
| test2 | start_points | frac:0.3 | rmse_h10 | transformer | 0.120 [0.110, 0.130] |  |  | 40 | 5 | f64a10ee |
| test2 | start_points | frac:0.3 | rmse_h100 | itransformer[loss=huber] | 0.158 [0.096, 0.239] |  |  | 40 | 5 | 8b749e84 |
| test2 | start_points | frac:0.3 | rmse_h100 | itransformer[loss=mse] | 0.171 [0.098, 0.263] |  |  | 40 | 5 | 34919877 |
| test2 | start_points | frac:0.3 | rmse_h100 | lstm[quantiles=None,loss=huber] | 0.214 [0.151, 0.290] |  |  | 40 | 5 | f7c2b05c |
| test2 | start_points | frac:0.3 | rmse_h100 | lstm[quantiles=None,loss=mse] | 0.473 [0.406, 0.544] |  |  | 40 | 5 | 7ddb85ea |
| test2 | start_points | frac:0.3 | rmse_h100 | lstm[revin=True] | 0.087 [0.068, 0.107] |  |  | 40 | 5 | 61016dbc |
| test2 | start_points | frac:0.3 | rmse_h100 | transformer | 0.184 [0.098, 0.299] |  |  | 40 | 5 | f64a10ee |
| test2 | start_points | frac:0.3 | rmse_h200 | itransformer[loss=huber] | 0.516 [0.291, 0.794] |  |  | 40 | 5 | 8b749e84 |
| test2 | start_points | frac:0.3 | rmse_h200 | itransformer[loss=mse] | 0.617 [0.344, 0.964] |  |  | 40 | 5 | 34919877 |
| test2 | start_points | frac:0.3 | rmse_h200 | lstm[quantiles=None,loss=huber] | 0.593 [0.477, 0.721] |  |  | 40 | 5 | f7c2b05c |
| test2 | start_points | frac:0.3 | rmse_h200 | lstm[quantiles=None,loss=mse] | 0.928 [0.717, 1.161] |  |  | 40 | 5 | 7ddb85ea |
| test2 | start_points | frac:0.3 | rmse_h200 | lstm[revin=True] | 0.787 [0.644, 0.966] |  |  | 40 | 5 | 61016dbc |
| test2 | start_points | frac:0.3 | rmse_h200 | transformer | 0.633 [0.424, 0.906] |  |  | 40 | 5 | f64a10ee |
| test2 | start_points | frac:0.3 | rmse_h50 | itransformer[loss=huber] | 0.065 [0.042, 0.093] |  |  | 40 | 5 | 8b749e84 |
| test2 | start_points | frac:0.3 | rmse_h50 | itransformer[loss=mse] | 0.076 [0.049, 0.108] |  |  | 40 | 5 | 34919877 |
| test2 | start_points | frac:0.3 | rmse_h50 | lstm[quantiles=None,loss=huber] | 0.132 [0.106, 0.163] |  |  | 40 | 5 | f7c2b05c |
| test2 | start_points | frac:0.3 | rmse_h50 | lstm[quantiles=None,loss=mse] | 0.260 [0.226, 0.295] |  |  | 40 | 5 | 7ddb85ea |
| test2 | start_points | frac:0.3 | rmse_h50 | lstm[revin=True] | 0.099 [0.079, 0.122] |  |  | 40 | 5 | 61016dbc |
| test2 | start_points | frac:0.3 | rmse_h50 | transformer | 0.254 [0.227, 0.284] |  |  | 40 | 5 | f64a10ee |
| test2 | start_points | frac:0.5 | rmse_h1 | itransformer[loss=huber] | 0.008 [0.005, 0.014] |  |  | 40 | 5 | 8b749e84 |
| test2 | start_points | frac:0.5 | rmse_h1 | itransformer[loss=mse] | 0.009 [0.005, 0.015] |  |  | 40 | 5 | 34919877 |
| test2 | start_points | frac:0.5 | rmse_h1 | lstm[quantiles=None,loss=huber] | 0.063 [0.057, 0.070] |  |  | 40 | 5 | f7c2b05c |
| test2 | start_points | frac:0.5 | rmse_h1 | lstm[quantiles=None,loss=mse] | 0.126 [0.113, 0.138] |  |  | 40 | 5 | 7ddb85ea |
| test2 | start_points | frac:0.5 | rmse_h1 | lstm[revin=True] | 0.009 [0.005, 0.016] |  |  | 40 | 5 | 61016dbc |
| test2 | start_points | frac:0.5 | rmse_h1 | transformer | 0.009 [0.005, 0.017] |  |  | 40 | 5 | f64a10ee |
| test2 | start_points | frac:0.5 | rmse_h10 | itransformer[loss=huber] | 0.019 [0.014, 0.026] |  |  | 40 | 5 | 8b749e84 |
| test2 | start_points | frac:0.5 | rmse_h10 | itransformer[loss=mse] | 0.020 [0.014, 0.028] |  |  | 40 | 5 | 34919877 |
| test2 | start_points | frac:0.5 | rmse_h10 | lstm[quantiles=None,loss=huber] | 0.059 [0.051, 0.069] |  |  | 40 | 5 | f7c2b05c |
| test2 | start_points | frac:0.5 | rmse_h10 | lstm[quantiles=None,loss=mse] | 0.080 [0.069, 0.093] |  |  | 40 | 5 | 7ddb85ea |
| test2 | start_points | frac:0.5 | rmse_h10 | lstm[revin=True] | 0.019 [0.013, 0.027] |  |  | 40 | 5 | 61016dbc |
| test2 | start_points | frac:0.5 | rmse_h10 | transformer | 0.101 [0.090, 0.112] |  |  | 40 | 5 | f64a10ee |
| test2 | start_points | frac:0.5 | rmse_h100 | itransformer[loss=huber] | 0.194 [0.144, 0.255] |  |  | 40 | 5 | 8b749e84 |
| test2 | start_points | frac:0.5 | rmse_h100 | itransformer[loss=mse] | 0.172 [0.121, 0.239] |  |  | 40 | 5 | 34919877 |
| test2 | start_points | frac:0.5 | rmse_h100 | lstm[quantiles=None,loss=huber] | 0.334 [0.274, 0.398] |  |  | 40 | 5 | f7c2b05c |
| test2 | start_points | frac:0.5 | rmse_h100 | lstm[quantiles=None,loss=mse] | 0.361 [0.282, 0.451] |  |  | 40 | 5 | 7ddb85ea |
| test2 | start_points | frac:0.5 | rmse_h100 | lstm[revin=True] | 0.214 [0.163, 0.267] |  |  | 40 | 5 | 61016dbc |
| test2 | start_points | frac:0.5 | rmse_h100 | transformer | 0.307 [0.196, 0.447] |  |  | 40 | 5 | f64a10ee |
| test2 | start_points | frac:0.5 | rmse_h200 | itransformer[loss=huber] | 0.663 [0.498, 0.852] |  |  | 40 | 5 | 8b749e84 |
| test2 | start_points | frac:0.5 | rmse_h200 | itransformer[loss=mse] | 0.631 [0.472, 0.835] |  |  | 40 | 5 | 34919877 |
| test2 | start_points | frac:0.5 | rmse_h200 | lstm[quantiles=None,loss=huber] | 0.913 [0.751, 1.080] |  |  | 40 | 5 | f7c2b05c |
| test2 | start_points | frac:0.5 | rmse_h200 | lstm[quantiles=None,loss=mse] | 0.984 [0.770, 1.234] |  |  | 40 | 5 | 7ddb85ea |
| test2 | start_points | frac:0.5 | rmse_h200 | lstm[revin=True] | 1.514 [1.263, 1.805] |  |  | 40 | 5 | 61016dbc |
| test2 | start_points | frac:0.5 | rmse_h200 | transformer | 1.398 [1.092, 1.762] |  |  | 40 | 5 | f64a10ee |
| test2 | start_points | frac:0.5 | rmse_h50 | itransformer[loss=huber] | 0.063 [0.050, 0.078] |  |  | 40 | 5 | 8b749e84 |
| test2 | start_points | frac:0.5 | rmse_h50 | itransformer[loss=mse] | 0.065 [0.049, 0.085] |  |  | 40 | 5 | 34919877 |
| test2 | start_points | frac:0.5 | rmse_h50 | lstm[quantiles=None,loss=huber] | 0.131 [0.113, 0.152] |  |  | 40 | 5 | f7c2b05c |
| test2 | start_points | frac:0.5 | rmse_h50 | lstm[quantiles=None,loss=mse] | 0.218 [0.193, 0.244] |  |  | 40 | 5 | 7ddb85ea |
| test2 | start_points | frac:0.5 | rmse_h50 | lstm[revin=True] | 0.048 [0.038, 0.058] |  |  | 40 | 5 | 61016dbc |
| test2 | start_points | frac:0.5 | rmse_h50 | transformer | 0.174 [0.139, 0.217] |  |  | 40 | 5 | f64a10ee |
| test2 | start_points | frac:0.7 | rmse_h1 | itransformer[loss=huber] | 0.008 [0.004, 0.014] |  |  | 40 | 5 | 8b749e84 |
| test2 | start_points | frac:0.7 | rmse_h1 | itransformer[loss=mse] | 0.008 [0.005, 0.015] |  |  | 40 | 5 | 34919877 |
| test2 | start_points | frac:0.7 | rmse_h1 | lstm[quantiles=None,loss=huber] | 0.070 [0.060, 0.082] |  |  | 40 | 5 | f7c2b05c |
| test2 | start_points | frac:0.7 | rmse_h1 | lstm[quantiles=None,loss=mse] | 0.175 [0.161, 0.188] |  |  | 40 | 5 | 7ddb85ea |
| test2 | start_points | frac:0.7 | rmse_h1 | lstm[revin=True] | 0.007 [0.004, 0.014] |  |  | 40 | 5 | 61016dbc |
| test2 | start_points | frac:0.7 | rmse_h1 | transformer | 0.008 [0.004, 0.014] |  |  | 40 | 5 | f64a10ee |
| test2 | start_points | frac:0.7 | rmse_h10 | itransformer[loss=huber] | 0.013 [0.010, 0.016] |  |  | 40 | 5 | 8b749e84 |
| test2 | start_points | frac:0.7 | rmse_h10 | itransformer[loss=mse] | 0.014 [0.011, 0.017] |  |  | 40 | 5 | 34919877 |
| test2 | start_points | frac:0.7 | rmse_h10 | lstm[quantiles=None,loss=huber] | 0.052 [0.045, 0.059] |  |  | 40 | 5 | f7c2b05c |
| test2 | start_points | frac:0.7 | rmse_h10 | lstm[quantiles=None,loss=mse] | 0.090 [0.081, 0.100] |  |  | 40 | 5 | 7ddb85ea |
| test2 | start_points | frac:0.7 | rmse_h10 | lstm[revin=True] | 0.010 [0.008, 0.012] |  |  | 40 | 5 | 61016dbc |
| test2 | start_points | frac:0.7 | rmse_h10 | transformer | 0.056 [0.046, 0.066] |  |  | 40 | 5 | f64a10ee |
| test2 | start_points | frac:0.7 | rmse_h100 | itransformer[loss=huber] | 0.202 [0.162, 0.245] |  |  | 40 | 5 | 8b749e84 |
| test2 | start_points | frac:0.7 | rmse_h100 | itransformer[loss=mse] | 0.196 [0.157, 0.242] |  |  | 40 | 5 | 34919877 |
| test2 | start_points | frac:0.7 | rmse_h100 | lstm[quantiles=None,loss=huber] | 0.312 [0.266, 0.361] |  |  | 40 | 5 | f7c2b05c |
| test2 | start_points | frac:0.7 | rmse_h100 | lstm[quantiles=None,loss=mse] | 0.403 [0.326, 0.487] |  |  | 40 | 5 | 7ddb85ea |
| test2 | start_points | frac:0.7 | rmse_h100 | lstm[revin=True] | 0.837 [0.722, 0.951] |  |  | 40 | 5 | 61016dbc |
| test2 | start_points | frac:0.7 | rmse_h100 | transformer | 1.306 [1.084, 1.535] |  |  | 40 | 5 | f64a10ee |
| test2 | start_points | frac:0.7 | rmse_h200 | itransformer[loss=huber] | 1.473 [1.101, 1.900] |  |  | 38 | 5 | 8b749e84 |
| test2 | start_points | frac:0.7 | rmse_h200 | itransformer[loss=mse] | 1.136 [0.818, 1.522] |  |  | 38 | 5 | 34919877 |
| test2 | start_points | frac:0.7 | rmse_h200 | lstm[quantiles=None,loss=huber] | 2.238 [1.754, 2.766] |  |  | 38 | 5 | f7c2b05c |
| test2 | start_points | frac:0.7 | rmse_h200 | lstm[quantiles=None,loss=mse] | 1.839 [1.389, 2.336] |  |  | 38 | 5 | 7ddb85ea |
| test2 | start_points | frac:0.7 | rmse_h200 | lstm[revin=True] | 5.275 [4.576, 6.000] |  |  | 38 | 5 | 61016dbc |
| test2 | start_points | frac:0.7 | rmse_h200 | transformer | 5.428 [4.660, 6.217] |  |  | 38 | 5 | f64a10ee |
| test2 | start_points | frac:0.7 | rmse_h50 | itransformer[loss=huber] | 0.051 [0.043, 0.059] |  |  | 40 | 5 | 8b749e84 |
| test2 | start_points | frac:0.7 | rmse_h50 | itransformer[loss=mse] | 0.051 [0.041, 0.065] |  |  | 40 | 5 | 34919877 |
| test2 | start_points | frac:0.7 | rmse_h50 | lstm[quantiles=None,loss=huber] | 0.100 [0.080, 0.121] |  |  | 40 | 5 | f7c2b05c |
| test2 | start_points | frac:0.7 | rmse_h50 | lstm[quantiles=None,loss=mse] | 0.227 [0.197, 0.260] |  |  | 40 | 5 | 7ddb85ea |
| test2 | start_points | frac:0.7 | rmse_h50 | lstm[revin=True] | 0.101 [0.082, 0.122] |  |  | 40 | 5 | 61016dbc |
| test2 | start_points | frac:0.7 | rmse_h50 | transformer | 0.307 [0.230, 0.390] |  |  | 40 | 5 | f64a10ee |
| test2 | start_points | overall | rmse_h1 | itransformer[loss=huber] | 0.013 [0.007, 0.020] |  |  | 40 | 5 | 8b749e84 |
| test2 | start_points | overall | rmse_h1 | itransformer[loss=mse] | 0.013 [0.008, 0.020] |  |  | 40 | 5 | 34919877 |
| test2 | start_points | overall | rmse_h1 | lstm[quantiles=None,loss=huber] | 0.068 [0.059, 0.077] |  |  | 40 | 5 | f7c2b05c |
| test2 | start_points | overall | rmse_h1 | lstm[quantiles=None,loss=mse] | 0.140 [0.130, 0.150] |  |  | 40 | 5 | 7ddb85ea |
| test2 | start_points | overall | rmse_h1 | lstm[revin=True] | 0.014 [0.008, 0.021] |  |  | 40 | 5 | 61016dbc |
| test2 | start_points | overall | rmse_h1 | transformer | 0.015 [0.009, 0.023] |  |  | 40 | 5 | f64a10ee |
| test2 | start_points | overall | rmse_h10 | itransformer[loss=huber] | 0.022 [0.017, 0.028] |  |  | 40 | 5 | 8b749e84 |
| test2 | start_points | overall | rmse_h10 | itransformer[loss=mse] | 0.023 [0.018, 0.030] |  |  | 40 | 5 | 34919877 |
| test2 | start_points | overall | rmse_h10 | lstm[quantiles=None,loss=huber] | 0.060 [0.054, 0.066] |  |  | 40 | 5 | f7c2b05c |
| test2 | start_points | overall | rmse_h10 | lstm[quantiles=None,loss=mse] | 0.094 [0.085, 0.103] |  |  | 40 | 5 | 7ddb85ea |
| test2 | start_points | overall | rmse_h10 | lstm[revin=True] | 0.031 [0.025, 0.038] |  |  | 40 | 5 | 61016dbc |
| test2 | start_points | overall | rmse_h10 | transformer | 0.111 [0.103, 0.120] |  |  | 40 | 5 | f64a10ee |
| test2 | start_points | overall | rmse_h100 | itransformer[loss=huber] | 0.196 [0.157, 0.244] |  |  | 40 | 5 | 8b749e84 |
| test2 | start_points | overall | rmse_h100 | itransformer[loss=mse] | 0.199 [0.152, 0.259] |  |  | 40 | 5 | 34919877 |
| test2 | start_points | overall | rmse_h100 | lstm[quantiles=None,loss=huber] | 0.300 [0.257, 0.349] |  |  | 40 | 5 | f7c2b05c |
| test2 | start_points | overall | rmse_h100 | lstm[quantiles=None,loss=mse] | 0.463 [0.400, 0.533] |  |  | 40 | 5 | 7ddb85ea |
| test2 | start_points | overall | rmse_h100 | lstm[revin=True] | 0.453 [0.394, 0.511] |  |  | 40 | 5 | 61016dbc |
| test2 | start_points | overall | rmse_h100 | transformer | 0.717 [0.587, 0.858] |  |  | 40 | 5 | f64a10ee |
| test2 | start_points | overall | rmse_h200 | itransformer[loss=huber] | 1.004 [0.807, 1.219] |  |  | 40 | 5 | 8b749e84 |
| test2 | start_points | overall | rmse_h200 | itransformer[loss=mse] | 0.924 [0.709, 1.175] |  |  | 40 | 5 | 34919877 |
| test2 | start_points | overall | rmse_h200 | lstm[quantiles=None,loss=huber] | 1.361 [1.162, 1.572] |  |  | 40 | 5 | f7c2b05c |
| test2 | start_points | overall | rmse_h200 | lstm[quantiles=None,loss=mse] | 1.413 [1.186, 1.657] |  |  | 40 | 5 | 7ddb85ea |
| test2 | start_points | overall | rmse_h200 | lstm[revin=True] | 2.791 [2.444, 3.138] |  |  | 40 | 5 | 61016dbc |
| test2 | start_points | overall | rmse_h200 | transformer | 2.873 [2.482, 3.260] |  |  | 40 | 5 | f64a10ee |
| test2 | start_points | overall | rmse_h50 | itransformer[loss=huber] | 0.070 [0.059, 0.084] |  |  | 40 | 5 | 8b749e84 |
| test2 | start_points | overall | rmse_h50 | itransformer[loss=mse] | 0.076 [0.061, 0.095] |  |  | 40 | 5 | 34919877 |
| test2 | start_points | overall | rmse_h50 | lstm[quantiles=None,loss=huber] | 0.129 [0.112, 0.148] |  |  | 40 | 5 | f7c2b05c |
| test2 | start_points | overall | rmse_h50 | lstm[quantiles=None,loss=mse] | 0.252 [0.231, 0.275] |  |  | 40 | 5 | 7ddb85ea |
| test2 | start_points | overall | rmse_h50 | lstm[revin=True] | 0.126 [0.116, 0.137] |  |  | 40 | 5 | 61016dbc |
| test2 | start_points | overall | rmse_h50 | transformer | 0.302 [0.273, 0.339] |  |  | 40 | 5 | f64a10ee |

</details>
