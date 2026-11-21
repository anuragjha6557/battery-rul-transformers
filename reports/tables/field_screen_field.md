# Benchmark tables: field_screen_field

- Protocol version: 1.1
- Git SHA: f1b71738cc
- Seeds: 3  |  unit runs: 189
- Note: n = 4 cells per NASA/CALCE dataset, so the 95 % cluster-bootstrap CI is wide by construction. Toyota rows are over test cells (test1 / test2 separately) with a cell-level bootstrap CI and a Holm-adjusted Wilcoxon p vs the best baseline. All metrics are computed per cell from the logged predictions.

## Headline (kind = overall; RMSE in %SOH, RUL MAE in cycles)

### calce_soh

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse | age_only | 6.887 [4.966, 8.809] |  |  | 4 | 3 | 67ef11db |
| loco | all | overall | rmse | elasticnet | 4.591 [1.958, 8.503] |  |  | 4 | 3 | 6e2f4f6f |
| loco | all | overall | rmse | itransformer | 4.711 [3.817, 5.638] |  |  | 4 | 3 | aec9e53f |
| loco | all | overall | rmse | lgbm | 4.406 [2.375, 6.019] |  |  | 4 | 3 | f59939e6 |
| loco | all | overall | rmse | lstm | 3.625 [1.888, 5.554] |  |  | 4 | 3 | 17ba76fe |
| loco | all | overall | rmse | patchtst | 6.863 [5.905, 7.821] |  |  | 4 | 3 | e5744e17 |
| loco | all | overall | rmse | transformer | 3.023 [2.230, 4.294] |  |  | 4 | 3 | 903fa8d9 |
| loco | start_points | overall | rmse | age_only | 1.172 [0.494, 1.884] |  |  | 4 | 3 | 67ef11db |
| loco | start_points | overall | rmse | elasticnet | 3.958 [2.057, 6.057] |  |  | 4 | 3 | 6e2f4f6f |
| loco | start_points | overall | rmse | itransformer | 2.382 [1.526, 3.239] |  |  | 4 | 3 | aec9e53f |
| loco | start_points | overall | rmse | lgbm | 1.707 [0.628, 3.337] |  |  | 4 | 3 | f59939e6 |
| loco | start_points | overall | rmse | lstm | 0.815 [0.597, 1.033] |  |  | 4 | 3 | 17ba76fe |
| loco | start_points | overall | rmse | patchtst | 4.851 [2.480, 7.860] |  |  | 4 | 3 | e5744e17 |
| loco | start_points | overall | rmse | transformer | 1.795 [1.174, 2.872] |  |  | 4 | 3 | 903fa8d9 |

### nasa_soh

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse | age_only | 5.846 [3.492, 8.201] |  | 2.929 | 4 | 3 | 88ee51a9 |
| loco | all | overall | rmse | elasticnet | 3.240 [2.286, 4.235] |  | 4.654 | 4 | 3 | 634142ee |
| loco | all | overall | rmse | itransformer | 5.539 [3.843, 7.244] |  | 4.055 | 4 | 3 | 268259bb |
| loco | all | overall | rmse | lgbm | 4.083 [2.313, 6.693] |  | 1.955 | 4 | 3 | 0b6733af |
| loco | all | overall | rmse | lstm | 3.898 [2.433, 6.070] |  | 2.750 | 4 | 3 | 12d1fe4a |
| loco | all | overall | rmse | patchtst | 7.207 [5.676, 9.382] |  | 5.823 | 4 | 3 | 1771f399 |
| loco | all | overall | rmse | transformer | 9.696 [6.920, 14.145] |  | 6.716 | 4 | 3 | 759ba6fb |
| loco | start_points | overall | rmse | age_only | 5.033 [4.479, 5.367] |  | 4.212 | 4 | 3 | 88ee51a9 |
| loco | start_points | overall | rmse | elasticnet | 2.637 [1.186, 4.421] |  | 2.102 | 4 | 3 | 634142ee |
| loco | start_points | overall | rmse | itransformer | 4.073 [3.460, 4.850] |  | 3.278 | 4 | 3 | 268259bb |
| loco | start_points | overall | rmse | lgbm | 3.601 [1.888, 5.236] |  | 0.957 | 4 | 3 | 0b6733af |
| loco | start_points | overall | rmse | lstm | 3.134 [1.943, 4.402] |  | 1.517 | 4 | 3 | 12d1fe4a |
| loco | start_points | overall | rmse | patchtst | 5.728 [4.063, 8.118] |  | 4.100 | 4 | 3 | 1771f399 |
| loco | start_points | overall | rmse | transformer | 6.743 [6.014, 7.695] |  | 8.189 | 4 | 3 | 759ba6fb |

### toyota_soh

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rmse | age_only | 4.008 [3.665, 4.471] |  |  | 43 | 3 | 688a0f19 |
| test1 | all | overall | rmse | elasticnet | 1.181 [0.963, 1.458] |  |  | 43 | 3 | cfcb82a1 |
| test1 | all | overall | rmse | itransformer | 1.032 [0.805, 1.333] |  |  | 43 | 3 | c40cfa66 |
| test1 | all | overall | rmse | lgbm | 0.947 [0.750, 1.225] |  |  | 43 | 3 | f8e3a325 |
| test1 | all | overall | rmse | lstm | 1.073 [0.796, 1.430] |  |  | 43 | 3 | 5be47980 |
| test1 | all | overall | rmse | patchtst | 1.657 [1.461, 1.886] |  |  | 43 | 3 | 036d0578 |
| test1 | all | overall | rmse | transformer | 0.927 [0.638, 1.291] |  |  | 43 | 3 | de82d262 |
| test1 | start_points | overall | rmse | age_only | 2.168 [1.705, 2.664] |  |  | 43 | 3 | 688a0f19 |
| test1 | start_points | overall | rmse | elasticnet | 0.959 [0.712, 1.266] |  |  | 43 | 3 | cfcb82a1 |
| test1 | start_points | overall | rmse | itransformer | 0.766 [0.562, 1.027] |  |  | 43 | 3 | c40cfa66 |
| test1 | start_points | overall | rmse | lgbm | 0.527 [0.378, 0.722] |  |  | 43 | 3 | f8e3a325 |
| test1 | start_points | overall | rmse | lstm | 0.918 [0.604, 1.329] |  |  | 43 | 3 | 5be47980 |
| test1 | start_points | overall | rmse | patchtst | 1.026 [0.892, 1.165] |  |  | 43 | 3 | 036d0578 |
| test1 | start_points | overall | rmse | transformer | 0.791 [0.504, 1.158] |  |  | 43 | 3 | de82d262 |
| test2 | all | overall | rmse | age_only | 3.673 [3.520, 3.821] |  |  | 40 | 3 | 688a0f19 |
| test2 | all | overall | rmse | elasticnet | 4.155 [4.023, 4.310] |  |  | 40 | 3 | cfcb82a1 |
| test2 | all | overall | rmse | itransformer | 1.550 [1.435, 1.685] |  |  | 40 | 3 | c40cfa66 |
| test2 | all | overall | rmse | lgbm | 2.553 [2.429, 2.684] |  |  | 40 | 3 | f8e3a325 |
| test2 | all | overall | rmse | lstm | 2.196 [2.078, 2.343] |  |  | 40 | 3 | 5be47980 |
| test2 | all | overall | rmse | patchtst | 2.349 [2.223, 2.495] |  |  | 40 | 3 | 036d0578 |
| test2 | all | overall | rmse | transformer | 2.584 [2.468, 2.718] |  |  | 40 | 3 | de82d262 |
| test2 | start_points | overall | rmse | age_only | 3.509 [3.286, 3.718] |  |  | 40 | 3 | 688a0f19 |
| test2 | start_points | overall | rmse | elasticnet | 1.709 [1.519, 1.899] |  |  | 40 | 3 | cfcb82a1 |
| test2 | start_points | overall | rmse | itransformer | 1.293 [1.117, 1.482] |  |  | 40 | 3 | c40cfa66 |
| test2 | start_points | overall | rmse | lgbm | 1.369 [1.180, 1.553] |  |  | 40 | 3 | f8e3a325 |
| test2 | start_points | overall | rmse | lstm | 1.327 [1.198, 1.451] |  |  | 40 | 3 | 5be47980 |
| test2 | start_points | overall | rmse | patchtst | 1.251 [1.053, 1.479] |  |  | 40 | 3 | 036d0578 |
| test2 | start_points | overall | rmse | transformer | 1.371 [1.232, 1.499] |  |  | 40 | 3 | de82d262 |

## Mean rank (dataset x task x split x policy x headline metric)

| model | mean rank | conditions | missing |
|---|---|---|---|
| lstm | 2.50 | 8 | 0 |
| lgbm | 2.88 | 8 | 0 |
| itransformer | 3.25 | 8 | 0 |
| transformer | 4.12 | 8 | 0 |
| elasticnet | 4.38 | 8 | 0 |
| patchtst | 5.12 | 8 | 0 |
| age_only | 5.75 | 8 | 0 |

## Full tables

<details><summary>calce_soh (49 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse | age_only | 6.887 [4.966, 8.809] |  |  | 4 | 3 | 67ef11db |
| loco | all | overall | rmse | elasticnet | 4.591 [1.958, 8.503] |  |  | 4 | 3 | 6e2f4f6f |
| loco | all | overall | rmse | itransformer | 4.711 [3.817, 5.638] |  |  | 4 | 3 | aec9e53f |
| loco | all | overall | rmse | lgbm | 4.406 [2.375, 6.019] |  |  | 4 | 3 | f59939e6 |
| loco | all | overall | rmse | lstm | 3.625 [1.888, 5.554] |  |  | 4 | 3 | 17ba76fe |
| loco | all | overall | rmse | patchtst | 6.863 [5.905, 7.821] |  |  | 4 | 3 | e5744e17 |
| loco | all | overall | rmse | transformer | 3.023 [2.230, 4.294] |  |  | 4 | 3 | 903fa8d9 |
| loco | start_points | fixed:200 | rmse | age_only | 1.381 [0.763, 1.760] |  |  | 4 | 3 | 67ef11db |
| loco | start_points | fixed:200 | rmse | elasticnet | 5.555 [3.183, 9.956] |  |  | 4 | 3 | 6e2f4f6f |
| loco | start_points | fixed:200 | rmse | itransformer | 2.198 [1.151, 4.008] |  |  | 4 | 3 | aec9e53f |
| loco | start_points | fixed:200 | rmse | lgbm | 0.728 [0.357, 0.976] |  |  | 4 | 3 | f59939e6 |
| loco | start_points | fixed:200 | rmse | lstm | 1.025 [0.858, 1.191] |  |  | 4 | 3 | 17ba76fe |
| loco | start_points | fixed:200 | rmse | patchtst | 4.834 [0.997, 10.644] |  |  | 4 | 3 | e5744e17 |
| loco | start_points | fixed:200 | rmse | transformer | 1.194 [0.747, 1.686] |  |  | 4 | 3 | 903fa8d9 |
| loco | start_points | fixed:400 | rmse | age_only | 0.390 [0.127, 0.727] |  |  | 4 | 3 | 67ef11db |
| loco | start_points | fixed:400 | rmse | elasticnet | 1.854 [0.521, 3.724] |  |  | 4 | 3 | 6e2f4f6f |
| loco | start_points | fixed:400 | rmse | itransformer | 1.974 [0.627, 4.038] |  |  | 4 | 3 | aec9e53f |
| loco | start_points | fixed:400 | rmse | lgbm | 0.514 [0.343, 0.770] |  |  | 4 | 3 | f59939e6 |
| loco | start_points | fixed:400 | rmse | lstm | 0.585 [0.304, 0.892] |  |  | 4 | 3 | 17ba76fe |
| loco | start_points | fixed:400 | rmse | patchtst | 2.375 [0.984, 3.766] |  |  | 4 | 3 | e5744e17 |
| loco | start_points | fixed:400 | rmse | transformer | 0.945 [0.455, 1.226] |  |  | 4 | 3 | 903fa8d9 |
| loco | start_points | frac:0.3 | rmse | age_only | 1.300 [0.351, 2.471] |  |  | 4 | 3 | 67ef11db |
| loco | start_points | frac:0.3 | rmse | elasticnet | 4.958 [1.995, 8.815] |  |  | 4 | 3 | 6e2f4f6f |
| loco | start_points | frac:0.3 | rmse | itransformer | 2.317 [1.223, 3.516] |  |  | 4 | 3 | aec9e53f |
| loco | start_points | frac:0.3 | rmse | lgbm | 3.216 [0.671, 7.219] |  |  | 4 | 3 | f59939e6 |
| loco | start_points | frac:0.3 | rmse | lstm | 0.871 [0.436, 1.306] |  |  | 4 | 3 | 17ba76fe |
| loco | start_points | frac:0.3 | rmse | patchtst | 5.032 [2.336, 7.809] |  |  | 4 | 3 | e5744e17 |
| loco | start_points | frac:0.3 | rmse | transformer | 2.694 [1.032, 5.802] |  |  | 4 | 3 | 903fa8d9 |
| loco | start_points | frac:0.5 | rmse | age_only | 1.037 [0.242, 2.422] |  |  | 4 | 3 | 67ef11db |
| loco | start_points | frac:0.5 | rmse | elasticnet | 1.920 [0.787, 3.066] |  |  | 4 | 3 | 6e2f4f6f |
| loco | start_points | frac:0.5 | rmse | itransformer | 1.405 [1.098, 1.712] |  |  | 4 | 3 | aec9e53f |
| loco | start_points | frac:0.5 | rmse | lgbm | 0.661 [0.143, 1.357] |  |  | 4 | 3 | f59939e6 |
| loco | start_points | frac:0.5 | rmse | lstm | 0.619 [0.162, 1.433] |  |  | 4 | 3 | 17ba76fe |
| loco | start_points | frac:0.5 | rmse | patchtst | 4.337 [3.054, 6.022] |  |  | 4 | 3 | e5744e17 |
| loco | start_points | frac:0.5 | rmse | transformer | 0.998 [0.436, 1.770] |  |  | 4 | 3 | 903fa8d9 |
| loco | start_points | frac:0.7 | rmse | age_only | 0.832 [0.212, 1.534] |  |  | 4 | 3 | 67ef11db |
| loco | start_points | frac:0.7 | rmse | elasticnet | 1.950 [0.527, 3.850] |  |  | 4 | 3 | 6e2f4f6f |
| loco | start_points | frac:0.7 | rmse | itransformer | 2.196 [1.342, 2.900] |  |  | 4 | 3 | aec9e53f |
| loco | start_points | frac:0.7 | rmse | lgbm | 0.684 [0.428, 0.876] |  |  | 4 | 3 | f59939e6 |
| loco | start_points | frac:0.7 | rmse | lstm | 0.342 [0.176, 0.508] |  |  | 4 | 3 | 17ba76fe |
| loco | start_points | frac:0.7 | rmse | patchtst | 3.952 [1.693, 5.902] |  |  | 4 | 3 | e5744e17 |
| loco | start_points | frac:0.7 | rmse | transformer | 0.963 [0.753, 1.174] |  |  | 4 | 3 | 903fa8d9 |
| loco | start_points | overall | rmse | age_only | 1.172 [0.494, 1.884] |  |  | 4 | 3 | 67ef11db |
| loco | start_points | overall | rmse | elasticnet | 3.958 [2.057, 6.057] |  |  | 4 | 3 | 6e2f4f6f |
| loco | start_points | overall | rmse | itransformer | 2.382 [1.526, 3.239] |  |  | 4 | 3 | aec9e53f |
| loco | start_points | overall | rmse | lgbm | 1.707 [0.628, 3.337] |  |  | 4 | 3 | f59939e6 |
| loco | start_points | overall | rmse | lstm | 0.815 [0.597, 1.033] |  |  | 4 | 3 | 17ba76fe |
| loco | start_points | overall | rmse | patchtst | 4.851 [2.480, 7.860] |  |  | 4 | 3 | e5744e17 |
| loco | start_points | overall | rmse | transformer | 1.795 [1.174, 2.872] |  |  | 4 | 3 | 903fa8d9 |

</details>

<details><summary>nasa_soh (49 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse | age_only | 5.846 [3.492, 8.201] |  | 2.929 | 4 | 3 | 88ee51a9 |
| loco | all | overall | rmse | elasticnet | 3.240 [2.286, 4.235] |  | 4.654 | 4 | 3 | 634142ee |
| loco | all | overall | rmse | itransformer | 5.539 [3.843, 7.244] |  | 4.055 | 4 | 3 | 268259bb |
| loco | all | overall | rmse | lgbm | 4.083 [2.313, 6.693] |  | 1.955 | 4 | 3 | 0b6733af |
| loco | all | overall | rmse | lstm | 3.898 [2.433, 6.070] |  | 2.750 | 4 | 3 | 12d1fe4a |
| loco | all | overall | rmse | patchtst | 7.207 [5.676, 9.382] |  | 5.823 | 4 | 3 | 1771f399 |
| loco | all | overall | rmse | transformer | 9.696 [6.920, 14.145] |  | 6.716 | 4 | 3 | 759ba6fb |
| loco | start_points | fixed:30 | rmse | age_only | 4.134 [3.969, 4.299] |  | 4.327 | 4 | 3 | 88ee51a9 |
| loco | start_points | fixed:30 | rmse | elasticnet | 2.051 [0.460, 3.641] |  | 0.914 | 4 | 3 | 634142ee |
| loco | start_points | fixed:30 | rmse | itransformer | 2.479 [1.795, 3.163] |  | 3.476 | 4 | 3 | 268259bb |
| loco | start_points | fixed:30 | rmse | lgbm | 3.622 [1.342, 5.901] |  | 0.243 | 4 | 3 | 0b6733af |
| loco | start_points | fixed:30 | rmse | lstm | 3.016 [1.737, 4.177] |  | 1.078 | 4 | 3 | 12d1fe4a |
| loco | start_points | fixed:30 | rmse | patchtst | 3.471 [1.934, 6.398] |  | 1.869 | 4 | 3 | 1771f399 |
| loco | start_points | fixed:30 | rmse | transformer | 6.492 [5.345, 8.060] |  | 8.935 | 4 | 3 | 759ba6fb |
| loco | start_points | fixed:50 | rmse | age_only | 4.566 [3.204, 5.580] |  | 2.579 | 4 | 3 | 88ee51a9 |
| loco | start_points | fixed:50 | rmse | elasticnet | 2.632 [0.884, 4.668] |  | 2.910 | 4 | 3 | 634142ee |
| loco | start_points | fixed:50 | rmse | itransformer | 3.210 [2.199, 4.415] |  | 3.316 | 4 | 3 | 268259bb |
| loco | start_points | fixed:50 | rmse | lgbm | 3.423 [1.372, 5.474] |  | 0.389 | 4 | 3 | 0b6733af |
| loco | start_points | fixed:50 | rmse | lstm | 3.289 [2.309, 3.982] |  | 1.772 | 4 | 3 | 12d1fe4a |
| loco | start_points | fixed:50 | rmse | patchtst | 6.748 [3.618, 11.598] |  | 5.626 | 4 | 3 | 1771f399 |
| loco | start_points | fixed:50 | rmse | transformer | 6.759 [5.554, 7.965] |  | 8.115 | 4 | 3 | 759ba6fb |
| loco | start_points | frac:0.3 | rmse | age_only | 5.236 [4.785, 5.687] |  | 4.570 | 4 | 3 | 88ee51a9 |
| loco | start_points | frac:0.3 | rmse | elasticnet | 2.761 [1.307, 4.639] |  | 2.272 | 4 | 3 | 634142ee |
| loco | start_points | frac:0.3 | rmse | itransformer | 3.583 [2.323, 5.360] |  | 2.003 | 4 | 3 | 268259bb |
| loco | start_points | frac:0.3 | rmse | lgbm | 4.548 [2.344, 7.108] |  | 1.534 | 4 | 3 | 0b6733af |
| loco | start_points | frac:0.3 | rmse | lstm | 3.266 [1.972, 4.522] |  | 1.224 | 4 | 3 | 12d1fe4a |
| loco | start_points | frac:0.3 | rmse | patchtst | 6.289 [3.484, 9.958] |  | 2.803 | 4 | 3 | 1771f399 |
| loco | start_points | frac:0.3 | rmse | transformer | 5.597 [3.388, 7.411] |  | 7.980 | 4 | 3 | 759ba6fb |
| loco | start_points | frac:0.5 | rmse | age_only | 5.305 [4.473, 5.862] |  | 5.811 | 4 | 3 | 88ee51a9 |
| loco | start_points | frac:0.5 | rmse | elasticnet | 2.595 [0.611, 5.067] |  | 1.791 | 4 | 3 | 634142ee |
| loco | start_points | frac:0.5 | rmse | itransformer | 3.279 [1.842, 4.726] |  | 3.833 | 4 | 3 | 268259bb |
| loco | start_points | frac:0.5 | rmse | lgbm | 2.138 [0.599, 3.882] |  | 0.796 | 4 | 3 | 0b6733af |
| loco | start_points | frac:0.5 | rmse | lstm | 2.621 [1.528, 3.953] |  | 1.163 | 4 | 3 | 12d1fe4a |
| loco | start_points | frac:0.5 | rmse | patchtst | 3.321 [2.293, 4.350] |  | 4.634 | 4 | 3 | 1771f399 |
| loco | start_points | frac:0.5 | rmse | transformer | 5.717 [4.781, 7.114] |  | 7.794 | 4 | 3 | 759ba6fb |
| loco | start_points | frac:0.7 | rmse | age_only | 5.452 [3.767, 6.609] |  | 2.946 | 4 | 3 | 88ee51a9 |
| loco | start_points | frac:0.7 | rmse | elasticnet | 2.587 [1.644, 3.819] |  | 2.102 | 4 | 3 | 634142ee |
| loco | start_points | frac:0.7 | rmse | itransformer | 5.273 [3.019, 7.880] |  | 2.283 | 4 | 3 | 268259bb |
| loco | start_points | frac:0.7 | rmse | lgbm | 2.555 [1.009, 4.979] |  | 1.175 | 4 | 3 | 0b6733af |
| loco | start_points | frac:0.7 | rmse | lstm | 2.579 [1.348, 4.930] |  | 1.302 | 4 | 3 | 12d1fe4a |
| loco | start_points | frac:0.7 | rmse | patchtst | 5.049 [2.816, 7.330] |  | 1.845 | 4 | 3 | 1771f399 |
| loco | start_points | frac:0.7 | rmse | transformer | 6.520 [4.784, 8.571] |  | 5.352 | 4 | 3 | 759ba6fb |
| loco | start_points | overall | rmse | age_only | 5.033 [4.479, 5.367] |  | 4.212 | 4 | 3 | 88ee51a9 |
| loco | start_points | overall | rmse | elasticnet | 2.637 [1.186, 4.421] |  | 2.102 | 4 | 3 | 634142ee |
| loco | start_points | overall | rmse | itransformer | 4.073 [3.460, 4.850] |  | 3.278 | 4 | 3 | 268259bb |
| loco | start_points | overall | rmse | lgbm | 3.601 [1.888, 5.236] |  | 0.957 | 4 | 3 | 0b6733af |
| loco | start_points | overall | rmse | lstm | 3.134 [1.943, 4.402] |  | 1.517 | 4 | 3 | 12d1fe4a |
| loco | start_points | overall | rmse | patchtst | 5.728 [4.063, 8.118] |  | 4.100 | 4 | 3 | 1771f399 |
| loco | start_points | overall | rmse | transformer | 6.743 [6.014, 7.695] |  | 8.189 | 4 | 3 | 759ba6fb |

</details>

<details><summary>toyota_soh (84 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rmse | age_only | 4.008 [3.665, 4.471] |  |  | 43 | 3 | 688a0f19 |
| test1 | all | overall | rmse | elasticnet | 1.181 [0.963, 1.458] |  |  | 43 | 3 | cfcb82a1 |
| test1 | all | overall | rmse | itransformer | 1.032 [0.805, 1.333] |  |  | 43 | 3 | c40cfa66 |
| test1 | all | overall | rmse | lgbm | 0.947 [0.750, 1.225] |  |  | 43 | 3 | f8e3a325 |
| test1 | all | overall | rmse | lstm | 1.073 [0.796, 1.430] |  |  | 43 | 3 | 5be47980 |
| test1 | all | overall | rmse | patchtst | 1.657 [1.461, 1.886] |  |  | 43 | 3 | 036d0578 |
| test1 | all | overall | rmse | transformer | 0.927 [0.638, 1.291] |  |  | 43 | 3 | de82d262 |
| test1 | start_points | fixed:100 | rmse | age_only | 0.567 [0.284, 1.052] |  |  | 43 | 3 | 688a0f19 |
| test1 | start_points | fixed:100 | rmse | elasticnet | 0.690 [0.512, 0.913] |  |  | 43 | 3 | cfcb82a1 |
| test1 | start_points | fixed:100 | rmse | itransformer | 0.474 [0.302, 0.747] |  |  | 43 | 3 | c40cfa66 |
| test1 | start_points | fixed:100 | rmse | lgbm | 0.357 [0.208, 0.584] |  |  | 43 | 3 | f8e3a325 |
| test1 | start_points | fixed:100 | rmse | lstm | 0.506 [0.356, 0.720] |  |  | 43 | 3 | 5be47980 |
| test1 | start_points | fixed:100 | rmse | patchtst | 0.793 [0.673, 0.922] |  |  | 43 | 3 | 036d0578 |
| test1 | start_points | fixed:100 | rmse | transformer | 0.339 [0.187, 0.609] |  |  | 43 | 3 | de82d262 |
| test1 | start_points | frac:0.3 | rmse | age_only | 1.299 [0.894, 1.783] |  |  | 43 | 3 | 688a0f19 |
| test1 | start_points | frac:0.3 | rmse | elasticnet | 0.567 [0.434, 0.714] |  |  | 43 | 3 | cfcb82a1 |
| test1 | start_points | frac:0.3 | rmse | itransformer | 0.521 [0.406, 0.648] |  |  | 43 | 3 | c40cfa66 |
| test1 | start_points | frac:0.3 | rmse | lgbm | 0.250 [0.179, 0.334] |  |  | 43 | 3 | f8e3a325 |
| test1 | start_points | frac:0.3 | rmse | lstm | 0.464 [0.373, 0.558] |  |  | 43 | 3 | 5be47980 |
| test1 | start_points | frac:0.3 | rmse | patchtst | 0.570 [0.443, 0.713] |  |  | 43 | 3 | 036d0578 |
| test1 | start_points | frac:0.3 | rmse | transformer | 0.307 [0.234, 0.389] |  |  | 43 | 3 | de82d262 |
| test1 | start_points | frac:0.5 | rmse | age_only | 2.498 [1.876, 3.154] |  |  | 43 | 3 | 688a0f19 |
| test1 | start_points | frac:0.5 | rmse | elasticnet | 0.877 [0.592, 1.245] |  |  | 43 | 3 | cfcb82a1 |
| test1 | start_points | frac:0.5 | rmse | itransformer | 0.807 [0.559, 1.098] |  |  | 43 | 3 | c40cfa66 |
| test1 | start_points | frac:0.5 | rmse | lgbm | 0.496 [0.325, 0.705] |  |  | 43 | 3 | f8e3a325 |
| test1 | start_points | frac:0.5 | rmse | lstm | 1.022 [0.578, 1.627] |  |  | 43 | 3 | 5be47980 |
| test1 | start_points | frac:0.5 | rmse | patchtst | 0.839 [0.640, 1.062] |  |  | 43 | 3 | 036d0578 |
| test1 | start_points | frac:0.5 | rmse | transformer | 0.840 [0.505, 1.274] |  |  | 43 | 3 | de82d262 |
| test1 | start_points | frac:0.7 | rmse | age_only | 2.778 [2.187, 3.412] |  |  | 43 | 3 | 688a0f19 |
| test1 | start_points | frac:0.7 | rmse | elasticnet | 1.098 [0.680, 1.620] |  |  | 43 | 3 | cfcb82a1 |
| test1 | start_points | frac:0.7 | rmse | itransformer | 0.878 [0.597, 1.241] |  |  | 43 | 3 | c40cfa66 |
| test1 | start_points | frac:0.7 | rmse | lgbm | 0.686 [0.480, 0.953] |  |  | 43 | 3 | f8e3a325 |
| test1 | start_points | frac:0.7 | rmse | lstm | 1.040 [0.590, 1.621] |  |  | 43 | 3 | 5be47980 |
| test1 | start_points | frac:0.7 | rmse | patchtst | 1.315 [1.095, 1.539] |  |  | 43 | 3 | 036d0578 |
| test1 | start_points | frac:0.7 | rmse | transformer | 1.100 [0.661, 1.654] |  |  | 43 | 3 | de82d262 |
| test1 | start_points | overall | rmse | age_only | 2.168 [1.705, 2.664] |  |  | 43 | 3 | 688a0f19 |
| test1 | start_points | overall | rmse | elasticnet | 0.959 [0.712, 1.266] |  |  | 43 | 3 | cfcb82a1 |
| test1 | start_points | overall | rmse | itransformer | 0.766 [0.562, 1.027] |  |  | 43 | 3 | c40cfa66 |
| test1 | start_points | overall | rmse | lgbm | 0.527 [0.378, 0.722] |  |  | 43 | 3 | f8e3a325 |
| test1 | start_points | overall | rmse | lstm | 0.918 [0.604, 1.329] |  |  | 43 | 3 | 5be47980 |
| test1 | start_points | overall | rmse | patchtst | 1.026 [0.892, 1.165] |  |  | 43 | 3 | 036d0578 |
| test1 | start_points | overall | rmse | transformer | 0.791 [0.504, 1.158] |  |  | 43 | 3 | de82d262 |
| test2 | all | overall | rmse | age_only | 3.673 [3.520, 3.821] |  |  | 40 | 3 | 688a0f19 |
| test2 | all | overall | rmse | elasticnet | 4.155 [4.023, 4.310] |  |  | 40 | 3 | cfcb82a1 |
| test2 | all | overall | rmse | itransformer | 1.550 [1.435, 1.685] |  |  | 40 | 3 | c40cfa66 |
| test2 | all | overall | rmse | lgbm | 2.553 [2.429, 2.684] |  |  | 40 | 3 | f8e3a325 |
| test2 | all | overall | rmse | lstm | 2.196 [2.078, 2.343] |  |  | 40 | 3 | 5be47980 |
| test2 | all | overall | rmse | patchtst | 2.349 [2.223, 2.495] |  |  | 40 | 3 | 036d0578 |
| test2 | all | overall | rmse | transformer | 2.584 [2.468, 2.718] |  |  | 40 | 3 | de82d262 |
| test2 | start_points | fixed:100 | rmse | age_only | 0.252 [0.146, 0.387] |  |  | 40 | 3 | 688a0f19 |
| test2 | start_points | fixed:100 | rmse | elasticnet | 1.347 [1.152, 1.542] |  |  | 40 | 3 | cfcb82a1 |
| test2 | start_points | fixed:100 | rmse | itransformer | 0.405 [0.326, 0.493] |  |  | 40 | 3 | c40cfa66 |
| test2 | start_points | fixed:100 | rmse | lgbm | 0.539 [0.475, 0.609] |  |  | 40 | 3 | f8e3a325 |
| test2 | start_points | fixed:100 | rmse | lstm | 0.301 [0.235, 0.370] |  |  | 40 | 3 | 5be47980 |
| test2 | start_points | fixed:100 | rmse | patchtst | 1.005 [0.884, 1.128] |  |  | 40 | 3 | 036d0578 |
| test2 | start_points | fixed:100 | rmse | transformer | 0.516 [0.441, 0.592] |  |  | 40 | 3 | de82d262 |
| test2 | start_points | frac:0.3 | rmse | age_only | 2.216 [1.814, 2.689] |  |  | 40 | 3 | 688a0f19 |
| test2 | start_points | frac:0.3 | rmse | elasticnet | 1.720 [1.507, 1.928] |  |  | 40 | 3 | cfcb82a1 |
| test2 | start_points | frac:0.3 | rmse | itransformer | 0.834 [0.695, 0.985] |  |  | 40 | 3 | c40cfa66 |
| test2 | start_points | frac:0.3 | rmse | lgbm | 0.437 [0.354, 0.524] |  |  | 40 | 3 | f8e3a325 |
| test2 | start_points | frac:0.3 | rmse | lstm | 0.842 [0.706, 0.978] |  |  | 40 | 3 | 5be47980 |
| test2 | start_points | frac:0.3 | rmse | patchtst | 0.819 [0.670, 0.984] |  |  | 40 | 3 | 036d0578 |
| test2 | start_points | frac:0.3 | rmse | transformer | 0.935 [0.822, 1.042] |  |  | 40 | 3 | de82d262 |
| test2 | start_points | frac:0.5 | rmse | age_only | 4.875 [4.499, 5.210] |  |  | 40 | 3 | 688a0f19 |
| test2 | start_points | frac:0.5 | rmse | elasticnet | 1.857 [1.611, 2.090] |  |  | 40 | 3 | cfcb82a1 |
| test2 | start_points | frac:0.5 | rmse | itransformer | 1.208 [1.020, 1.417] |  |  | 40 | 3 | c40cfa66 |
| test2 | start_points | frac:0.5 | rmse | lgbm | 1.264 [0.973, 1.567] |  |  | 40 | 3 | f8e3a325 |
| test2 | start_points | frac:0.5 | rmse | lstm | 1.610 [1.440, 1.775] |  |  | 40 | 3 | 5be47980 |
| test2 | start_points | frac:0.5 | rmse | patchtst | 0.933 [0.722, 1.185] |  |  | 40 | 3 | 036d0578 |
| test2 | start_points | frac:0.5 | rmse | transformer | 1.540 [1.368, 1.699] |  |  | 40 | 3 | de82d262 |
| test2 | start_points | frac:0.7 | rmse | age_only | 4.258 [3.958, 4.524] |  |  | 40 | 3 | 688a0f19 |
| test2 | start_points | frac:0.7 | rmse | elasticnet | 1.694 [1.446, 1.954] |  |  | 40 | 3 | cfcb82a1 |
| test2 | start_points | frac:0.7 | rmse | itransformer | 1.952 [1.638, 2.281] |  |  | 40 | 3 | c40cfa66 |
| test2 | start_points | frac:0.7 | rmse | lgbm | 2.198 [1.873, 2.509] |  |  | 40 | 3 | f8e3a325 |
| test2 | start_points | frac:0.7 | rmse | lstm | 1.841 [1.651, 2.031] |  |  | 40 | 3 | 5be47980 |
| test2 | start_points | frac:0.7 | rmse | patchtst | 1.537 [1.140, 1.985] |  |  | 40 | 3 | 036d0578 |
| test2 | start_points | frac:0.7 | rmse | transformer | 1.947 [1.733, 2.144] |  |  | 40 | 3 | de82d262 |
| test2 | start_points | overall | rmse | age_only | 3.509 [3.286, 3.718] |  |  | 40 | 3 | 688a0f19 |
| test2 | start_points | overall | rmse | elasticnet | 1.709 [1.519, 1.899] |  |  | 40 | 3 | cfcb82a1 |
| test2 | start_points | overall | rmse | itransformer | 1.293 [1.117, 1.482] |  |  | 40 | 3 | c40cfa66 |
| test2 | start_points | overall | rmse | lgbm | 1.369 [1.180, 1.553] |  |  | 40 | 3 | f8e3a325 |
| test2 | start_points | overall | rmse | lstm | 1.327 [1.198, 1.451] |  |  | 40 | 3 | 5be47980 |
| test2 | start_points | overall | rmse | patchtst | 1.251 [1.053, 1.479] |  |  | 40 | 3 | 036d0578 |
| test2 | start_points | overall | rmse | transformer | 1.371 [1.232, 1.499] |  |  | 40 | 3 | de82d262 |

</details>
