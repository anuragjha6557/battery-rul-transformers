# Benchmark tables: field_final

- Protocol version: 1.1
- Git SHA: 64d082226c, b2cd5c678b, eecc261b52
- Seeds: 5  |  unit runs: 945
- Note: n = 4 cells per NASA/CALCE dataset, so the 95 % cluster-bootstrap CI is wide by construction. Toyota rows are over test cells (test1 / test2 separately) with a cell-level bootstrap CI and a Holm-adjusted Wilcoxon p vs the best baseline. All metrics are computed per cell from the logged predictions.

## Headline (kind = overall; RMSE in %SOH, RUL MAE in cycles)

### calce_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | age_only | 6.873 [4.934, 8.813] |  |  | 4 | 5 | 73b85c3a |
| loco | all | overall | rmse_h1 | elasticnet | 3.562 [1.885, 6.210] |  |  | 4 | 5 | 03fa40ae |
| loco | all | overall | rmse_h1 | itransformer[lookback=32] | 3.684 [2.797, 4.436] |  |  | 4 | 5 | 2307abf0 |
| loco | all | overall | rmse_h1 | lgbm | 4.368 [2.423, 5.559] |  |  | 4 | 5 | 4d728772 |
| loco | all | overall | rmse_h1 | lstm[lookback=128] | 1.674 [1.336, 1.938] |  |  | 4 | 5 | 02033d0f |
| loco | all | overall | rmse_h1 | patchtst[lookback=32] | 7.017 [6.756, 7.378] |  |  | 4 | 5 | 91d56bb1 |
| loco | all | overall | rmse_h1 | transformer[lookback=32] | 2.478 [1.913, 3.307] |  |  | 4 | 5 | e3e3015f |
| loco | all | overall | rmse_h10 | age_only | 6.899 [4.946, 8.851] |  |  | 4 | 5 | 73b85c3a |
| loco | all | overall | rmse_h10 | elasticnet | 3.305 [2.165, 5.183] |  |  | 4 | 5 | 03fa40ae |
| loco | all | overall | rmse_h10 | itransformer[lookback=32] | 3.841 [3.048, 4.586] |  |  | 4 | 5 | 2307abf0 |
| loco | all | overall | rmse_h10 | lgbm | 4.191 [2.694, 5.428] |  |  | 4 | 5 | 4d728772 |
| loco | all | overall | rmse_h10 | lstm[lookback=128] | 1.968 [1.807, 2.177] |  |  | 4 | 5 | 02033d0f |
| loco | all | overall | rmse_h10 | patchtst[lookback=32] | 7.315 [6.969, 7.803] |  |  | 4 | 5 | 91d56bb1 |
| loco | all | overall | rmse_h10 | transformer[lookback=32] | 2.604 [2.238, 3.268] |  |  | 4 | 5 | e3e3015f |
| loco | all | overall | rmse_h50 | age_only | 7.082 [5.105, 9.059] |  |  | 4 | 5 | 73b85c3a |
| loco | all | overall | rmse_h50 | elasticnet | 2.768 [2.517, 2.963] |  |  | 4 | 5 | 03fa40ae |
| loco | all | overall | rmse_h50 | itransformer[lookback=32] | 3.961 [3.328, 4.594] |  |  | 4 | 5 | 2307abf0 |
| loco | all | overall | rmse_h50 | lgbm | 4.686 [3.351, 5.880] |  |  | 4 | 5 | 4d728772 |
| loco | all | overall | rmse_h50 | lstm[lookback=128] | 2.828 [2.549, 3.266] |  |  | 4 | 5 | 02033d0f |
| loco | all | overall | rmse_h50 | patchtst[lookback=32] | 8.267 [7.736, 8.798] |  |  | 4 | 5 | 91d56bb1 |
| loco | all | overall | rmse_h50 | transformer[lookback=32] | 3.223 [2.935, 3.677] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | overall | rmse_h1 | age_only | 1.043 [0.445, 1.477] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | overall | rmse_h1 | elasticnet | 3.150 [1.718, 4.801] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | overall | rmse_h1 | itransformer[lookback=32] | 1.663 [1.030, 2.297] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | overall | rmse_h1 | lgbm | 1.764 [0.596, 3.696] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | overall | rmse_h1 | lstm[lookback=128] | 0.801 [0.613, 1.010] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | overall | rmse_h1 | patchtst[lookback=32] | 2.864 [2.548, 3.264] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | overall | rmse_h1 | transformer[lookback=32] | 1.124 [0.967, 1.257] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | overall | rmse_h10 | age_only | 1.447 [1.076, 1.830] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | overall | rmse_h10 | elasticnet | 2.388 [1.787, 2.880] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | overall | rmse_h10 | itransformer[lookback=32] | 1.812 [1.193, 2.345] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | overall | rmse_h10 | lgbm | 1.944 [0.692, 3.413] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | overall | rmse_h10 | lstm[lookback=128] | 1.234 [0.726, 1.742] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | overall | rmse_h10 | patchtst[lookback=32] | 2.946 [2.462, 3.429] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | overall | rmse_h10 | transformer[lookback=32] | 1.071 [0.662, 1.621] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | overall | rmse_h50 | age_only | 1.134 [0.361, 1.907] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | overall | rmse_h50 | elasticnet | 2.487 [1.508, 3.253] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | overall | rmse_h50 | itransformer[lookback=32] | 1.718 [1.527, 1.909] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | overall | rmse_h50 | lgbm | 2.062 [0.982, 3.551] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | overall | rmse_h50 | lstm[lookback=128] | 1.252 [0.630, 1.875] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | overall | rmse_h50 | patchtst[lookback=32] | 3.678 [2.911, 4.372] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | overall | rmse_h50 | transformer[lookback=32] | 1.566 [1.142, 1.990] |  |  | 4 | 5 | e3e3015f |

### calce_rul

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rul_mae | age_only | 50.686 [32.535, 68.837] |  |  | 4 | 5 | 64f14627 |
| loco | all | overall | rul_mae | elasticnet | 32546.551 [50.238, 97401.429] |  |  | 4 | 5 | ed886871 |
| loco | all | overall | rul_mae | itransformer[lookback=32] | 50.621 [30.520, 70.722] |  |  | 4 | 5 | d354e3ac |
| loco | all | overall | rul_mae | lgbm | 65.737 [36.423, 94.973] |  |  | 4 | 5 | 84487083 |
| loco | all | overall | rul_mae | lstm[lookback=128] | 52.452 [38.404, 66.500] |  |  | 4 | 5 | 077064c2 |
| loco | all | overall | rul_mae | patchtst[lookback=32] | 98.347 [91.345, 105.115] |  |  | 4 | 5 | c63195d9 |
| loco | all | overall | rul_mae | transformer[lookback=32] | 53.985 [30.568, 77.583] |  |  | 4 | 5 | e9787753 |
| loco | start_points | overall | rul_mae | age_only | 51.750 [33.000, 70.500] |  |  | 4 | 5 | 64f14627 |
| loco | start_points | overall | rul_mae | elasticnet | 282.069 [55.304, 577.120] |  |  | 4 | 5 | ed886871 |
| loco | start_points | overall | rul_mae | itransformer[lookback=32] | 51.827 [26.411, 77.244] |  |  | 4 | 5 | d354e3ac |
| loco | start_points | overall | rul_mae | lgbm | 66.149 [28.321, 109.437] |  |  | 4 | 5 | 84487083 |
| loco | start_points | overall | rul_mae | lstm[lookback=128] | 54.920 [36.941, 71.199] |  |  | 4 | 5 | 077064c2 |
| loco | start_points | overall | rul_mae | patchtst[lookback=32] | 102.407 [86.356, 121.254] |  |  | 4 | 5 | c63195d9 |
| loco | start_points | overall | rul_mae | transformer[lookback=32] | 55.418 [30.120, 85.680] |  |  | 4 | 5 | e9787753 |

### calce_soh

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse | age_only | 6.887 [4.966, 8.809] |  |  | 4 | 5 | b6c4b34b |
| loco | all | overall | rmse | elasticnet | 3.603 [2.142, 5.766] |  |  | 4 | 5 | 548a83f2 |
| loco | all | overall | rmse | itransformer[lookback=32] | 3.283 [2.464, 4.057] |  |  | 4 | 5 | 36cc1330 |
| loco | all | overall | rmse | lgbm | 4.146 [2.276, 5.591] |  |  | 4 | 5 | 47c70266 |
| loco | all | overall | rmse | lstm[lookback=32] | 2.066 [1.468, 2.770] |  |  | 4 | 5 | ea07bc2d |
| loco | all | overall | rmse | patchtst[lookback=32] | 8.185 [7.955, 8.421] |  |  | 4 | 5 | a4c8516a |
| loco | all | overall | rmse | transformer[lookback=128] | 2.945 [2.340, 3.932] |  |  | 4 | 5 | a9f5efc8 |
| loco | start_points | overall | rmse | age_only | 1.172 [0.494, 1.884] |  |  | 4 | 5 | b6c4b34b |
| loco | start_points | overall | rmse | elasticnet | 2.410 [1.258, 3.637] |  |  | 4 | 5 | 548a83f2 |
| loco | start_points | overall | rmse | itransformer[lookback=32] | 1.412 [1.336, 1.488] |  |  | 4 | 5 | 36cc1330 |
| loco | start_points | overall | rmse | lgbm | 1.473 [0.671, 2.785] |  |  | 4 | 5 | 47c70266 |
| loco | start_points | overall | rmse | lstm[lookback=32] | 0.873 [0.665, 1.140] |  |  | 4 | 5 | ea07bc2d |
| loco | start_points | overall | rmse | patchtst[lookback=32] | 4.508 [3.327, 5.688] |  |  | 4 | 5 | a4c8516a |
| loco | start_points | overall | rmse | transformer[lookback=128] | 2.835 [1.245, 5.724] |  |  | 4 | 5 | a9f5efc8 |

### nasa_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | age_only | 5.882 [3.514, 8.250] |  | 2.968 | 4 | 5 | c73b7eaf |
| loco | all | overall | rmse_h1 | elasticnet | 2.491 [1.100, 4.051] |  | 4.970 | 4 | 5 | bf90a8cb |
| loco | all | overall | rmse_h1 | itransformer[lookback=64] | 5.829 [4.764, 6.890] |  | 6.097 | 4 | 5 | 40d3fd6c |
| loco | all | overall | rmse_h1 | lgbm | 3.374 [1.630, 6.032] |  | 2.216 | 4 | 5 | abf2d8ec |
| loco | all | overall | rmse_h1 | lstm[lookback=64] | 4.250 [2.865, 5.971] |  | 4.334 | 4 | 5 | ef7822ad |
| loco | all | overall | rmse_h1 | patchtst[lookback=64] | 6.306 [4.860, 8.169] |  | 6.357 | 4 | 5 | 84b85da9 |
| loco | all | overall | rmse_h1 | transformer[lookback=64] | 7.368 [4.927, 9.810] |  | 8.914 | 4 | 5 | 7fb96153 |
| loco | all | overall | rmse_h10 | age_only | 6.044 [3.617, 8.471] |  | 3.057 | 4 | 5 | c73b7eaf |
| loco | all | overall | rmse_h10 | elasticnet | 4.884 [3.352, 5.845] |  | 5.355 | 4 | 5 | bf90a8cb |
| loco | all | overall | rmse_h10 | itransformer[lookback=64] | 5.555 [4.480, 6.876] |  | 5.524 | 4 | 5 | 40d3fd6c |
| loco | all | overall | rmse_h10 | lgbm | 4.370 [2.848, 6.830] |  | 3.190 | 4 | 5 | abf2d8ec |
| loco | all | overall | rmse_h10 | lstm[lookback=64] | 5.837 [3.778, 7.896] |  | 7.221 | 4 | 5 | ef7822ad |
| loco | all | overall | rmse_h10 | patchtst[lookback=64] | 6.447 [5.580, 7.886] |  | 5.999 | 4 | 5 | 84b85da9 |
| loco | all | overall | rmse_h10 | transformer[lookback=64] | 7.119 [5.077, 10.062] |  | 6.731 | 4 | 5 | 7fb96153 |
| loco | all | overall | rmse_h50 | age_only | 6.281 [3.206, 9.356] |  | 2.381 | 4 | 5 | c73b7eaf |
| loco | all | overall | rmse_h50 | elasticnet | 7.743 [4.087, 11.400] |  | 10.124 | 4 | 5 | bf90a8cb |
| loco | all | overall | rmse_h50 | itransformer[lookback=64] | 5.825 [4.315, 7.475] |  | 4.820 | 4 | 5 | 40d3fd6c |
| loco | all | overall | rmse_h50 | lgbm | 6.471 [3.486, 9.991] |  | 2.541 | 4 | 5 | abf2d8ec |
| loco | all | overall | rmse_h50 | lstm[lookback=64] | 5.621 [3.548, 8.323] |  | 5.175 | 4 | 5 | ef7822ad |
| loco | all | overall | rmse_h50 | patchtst[lookback=64] | 6.157 [4.744, 7.873] |  | 5.600 | 4 | 5 | 84b85da9 |
| loco | all | overall | rmse_h50 | transformer[lookback=64] | 8.469 [6.172, 12.632] |  | 6.639 | 4 | 5 | 7fb96153 |
| loco | start_points | overall | rmse_h1 | age_only | 5.204 [4.184, 6.009] |  | 3.744 | 4 | 5 | c73b7eaf |
| loco | start_points | overall | rmse_h1 | elasticnet | 1.959 [1.027, 2.892] |  | 3.012 | 4 | 5 | bf90a8cb |
| loco | start_points | overall | rmse_h1 | itransformer[lookback=64] | 5.459 [4.101, 6.816] |  | 6.929 | 4 | 5 | 40d3fd6c |
| loco | start_points | overall | rmse_h1 | lgbm | 2.401 [1.134, 3.360] |  | 2.771 | 4 | 5 | abf2d8ec |
| loco | start_points | overall | rmse_h1 | lstm[lookback=64] | 3.941 [3.236, 4.749] |  | 4.078 | 4 | 5 | ef7822ad |
| loco | start_points | overall | rmse_h1 | patchtst[lookback=64] | 5.383 [4.239, 6.527] |  | 6.264 | 4 | 5 | 84b85da9 |
| loco | start_points | overall | rmse_h1 | transformer[lookback=64] | 5.131 [3.950, 6.303] |  | 4.625 | 4 | 5 | 7fb96153 |
| loco | start_points | overall | rmse_h10 | age_only | 5.482 [4.007, 6.737] |  | 3.331 | 4 | 5 | c73b7eaf |
| loco | start_points | overall | rmse_h10 | elasticnet | 4.883 [2.297, 7.470] |  | 2.716 | 4 | 5 | bf90a8cb |
| loco | start_points | overall | rmse_h10 | itransformer[lookback=64] | 4.822 [4.130, 5.246] |  | 5.312 | 4 | 5 | 40d3fd6c |
| loco | start_points | overall | rmse_h10 | lgbm | 4.416 [3.236, 5.728] |  | 3.917 | 4 | 5 | abf2d8ec |
| loco | start_points | overall | rmse_h10 | lstm[lookback=64] | 4.081 [2.263, 5.960] |  | 4.676 | 4 | 5 | ef7822ad |
| loco | start_points | overall | rmse_h10 | patchtst[lookback=64] | 5.269 [4.017, 6.522] |  | 7.100 | 4 | 5 | 84b85da9 |
| loco | start_points | overall | rmse_h10 | transformer[lookback=64] | 5.408 [3.848, 7.101] |  | 4.205 | 4 | 5 | 7fb96153 |
| loco | start_points | overall | rmse_h50 | age_only | 6.121 [3.882, 8.360] |  | 3.333 | 4 | 5 | c73b7eaf |
| loco | start_points | overall | rmse_h50 | elasticnet | 7.935 [3.805, 12.066] |  | 11.486 | 4 | 5 | bf90a8cb |
| loco | start_points | overall | rmse_h50 | itransformer[lookback=64] | 5.255 [4.129, 6.275] |  | 5.452 | 4 | 5 | 40d3fd6c |
| loco | start_points | overall | rmse_h50 | lgbm | 5.234 [2.958, 7.562] |  | 2.004 | 4 | 5 | abf2d8ec |
| loco | start_points | overall | rmse_h50 | lstm[lookback=64] | 5.599 [2.906, 8.495] |  | 5.781 | 4 | 5 | ef7822ad |
| loco | start_points | overall | rmse_h50 | patchtst[lookback=64] | 5.117 [4.356, 5.820] |  | 6.067 | 4 | 5 | 84b85da9 |
| loco | start_points | overall | rmse_h50 | transformer[lookback=64] | 7.938 [5.563, 12.172] |  | 6.033 | 4 | 5 | 7fb96153 |

### nasa_rul

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rul_mae | age_only | 33.755 [26.091, 41.419] |  | 28.000 | 4 | 5 | 8d5ddbd0 |
| loco | all | overall | rul_mae | elasticnet | 535.263 [20.352, 1489.929] |  | 18.502 | 4 | 5 | 6825caea |
| loco | all | overall | rul_mae | itransformer[lookback=64] | 15.129 [9.880, 20.379] |  | 7.942 | 4 | 5 | 7437407c |
| loco | all | overall | rul_mae | lgbm | 24.255 [18.203, 30.205] |  | 15.302 | 4 | 5 | aceee9e9 |
| loco | all | overall | rul_mae | lstm[lookback=64] | 21.285 [12.364, 30.555] |  | 9.931 | 4 | 5 | dec42eab |
| loco | all | overall | rul_mae | patchtst[lookback=64] | 17.759 [12.524, 22.993] |  | 10.042 | 4 | 5 | b6c4743e |
| loco | all | overall | rul_mae | transformer[lookback=64] | 27.248 [17.767, 38.198] |  | 14.371 | 4 | 5 | de016c87 |
| loco | start_points | overall | rul_mae | age_only | 36.500 [28.000, 45.000] |  | 28.000 | 4 | 5 | 8d5ddbd0 |
| loco | start_points | overall | rul_mae | elasticnet | 833.699 [19.888, 2407.345] |  | 19.113 | 4 | 5 | 6825caea |
| loco | start_points | overall | rul_mae | itransformer[lookback=64] | 11.599 [6.987, 16.211] |  | 5.157 | 4 | 5 | 7437407c |
| loco | start_points | overall | rul_mae | lgbm | 22.768 [14.238, 31.298] |  | 10.544 | 4 | 5 | aceee9e9 |
| loco | start_points | overall | rul_mae | lstm[lookback=64] | 22.408 [11.982, 32.834] |  | 9.172 | 4 | 5 | dec42eab |
| loco | start_points | overall | rul_mae | patchtst[lookback=64] | 15.622 [10.305, 18.786] |  | 7.681 | 4 | 5 | b6c4743e |
| loco | start_points | overall | rul_mae | transformer[lookback=64] | 27.638 [15.789, 39.487] |  | 9.660 | 4 | 5 | de016c87 |

### nasa_soh

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse | age_only | 5.846 [3.492, 8.201] |  | 2.929 | 4 | 5 | b53084f5 |
| loco | all | overall | rmse | elasticnet | 5.418 [2.669, 8.031] |  | 9.019 | 4 | 5 | 0e2331e6 |
| loco | all | overall | rmse | itransformer[lookback=64] | 4.592 [3.263, 5.922] |  | 5.284 | 4 | 5 | a696c19a |
| loco | all | overall | rmse | lgbm | 3.942 [2.615, 6.502] |  | 2.631 | 4 | 5 | 701596ac |
| loco | all | overall | rmse | lstm[lookback=64] | 4.223 [3.262, 5.850] |  | 3.269 | 4 | 5 | 24f86fa7 |
| loco | all | overall | rmse | patchtst[lookback=64] | 6.256 [4.478, 8.210] |  | 6.760 | 4 | 5 | 5f3ce529 |
| loco | all | overall | rmse | transformer[lookback=64] | 7.774 [5.051, 10.559] |  | 11.530 | 4 | 5 | 3b27876b |
| loco | start_points | overall | rmse | age_only | 5.033 [4.479, 5.367] |  | 4.212 | 4 | 5 | b53084f5 |
| loco | start_points | overall | rmse | elasticnet | 5.621 [2.732, 7.712] |  | 7.034 | 4 | 5 | 0e2331e6 |
| loco | start_points | overall | rmse | itransformer[lookback=64] | 3.779 [2.940, 4.962] |  | 5.511 | 4 | 5 | a696c19a |
| loco | start_points | overall | rmse | lgbm | 3.259 [2.382, 4.136] |  | 1.932 | 4 | 5 | 701596ac |
| loco | start_points | overall | rmse | lstm[lookback=64] | 3.584 [2.540, 4.607] |  | 1.959 | 4 | 5 | 24f86fa7 |
| loco | start_points | overall | rmse | patchtst[lookback=64] | 5.565 [4.874, 6.559] |  | 6.995 | 4 | 5 | 5f3ce529 |
| loco | start_points | overall | rmse | transformer[lookback=64] | 5.828 [4.622, 6.983] |  | 5.406 | 4 | 5 | 3b27876b |

### toyota_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rmse_h1 | age_only | 4.011 [3.667, 4.476] |  |  | 43 | 5 | 7d094294 |
| test1 | all | overall | rmse_h1 | elasticnet | 1.187 [0.966, 1.467] |  |  | 43 | 5 | 910f2d53 |
| test1 | all | overall | rmse_h1 | itransformer[lookback=32] | 1.120 [0.912, 1.378] |  |  | 43 | 5 | 7ab9b903 |
| test1 | all | overall | rmse_h1 | lgbm | 0.977 [0.781, 1.253] |  |  | 43 | 5 | c867ad3f |
| test1 | all | overall | rmse_h1 | lstm[lookback=128] | 0.807 [0.598, 1.070] |  |  | 43 | 5 | 3bc20cea |
| test1 | all | overall | rmse_h1 | patchtst[lookback=128] | 1.487 [1.285, 1.719] |  |  | 43 | 5 | 1a28f12a |
| test1 | all | overall | rmse_h1 | transformer[lookback=32] | 0.738 [0.562, 0.956] |  |  | 43 | 5 | a3e9d648 |
| test1 | all | overall | rmse_h10 | age_only | 4.046 [3.693, 4.527] |  |  | 43 | 5 | 7d094294 |
| test1 | all | overall | rmse_h10 | elasticnet | 1.205 [0.975, 1.497] |  |  | 43 | 5 | 910f2d53 |
| test1 | all | overall | rmse_h10 | itransformer[lookback=32] | 1.080 [0.867, 1.356] |  |  | 43 | 5 | 7ab9b903 |
| test1 | all | overall | rmse_h10 | lgbm | 0.939 [0.752, 1.209] |  |  | 43 | 5 | c867ad3f |
| test1 | all | overall | rmse_h10 | lstm[lookback=128] | 0.788 [0.566, 1.073] |  |  | 43 | 5 | 3bc20cea |
| test1 | all | overall | rmse_h10 | patchtst[lookback=128] | 1.524 [1.325, 1.747] |  |  | 43 | 5 | 1a28f12a |
| test1 | all | overall | rmse_h10 | transformer[lookback=32] | 0.750 [0.559, 0.995] |  |  | 43 | 5 | a3e9d648 |
| test1 | all | overall | rmse_h50 | age_only | 4.219 [3.817, 4.783] |  |  | 43 | 5 | 7d094294 |
| test1 | all | overall | rmse_h50 | elasticnet | 1.418 [1.099, 1.829] |  |  | 43 | 5 | 910f2d53 |
| test1 | all | overall | rmse_h50 | itransformer[lookback=32] | 1.255 [0.976, 1.634] |  |  | 43 | 5 | 7ab9b903 |
| test1 | all | overall | rmse_h50 | lgbm | 0.927 [0.704, 1.263] |  |  | 43 | 5 | c867ad3f |
| test1 | all | overall | rmse_h50 | lstm[lookback=128] | 0.999 [0.699, 1.427] |  |  | 43 | 5 | 3bc20cea |
| test1 | all | overall | rmse_h50 | patchtst[lookback=128] | 1.698 [1.478, 1.958] |  |  | 43 | 5 | 1a28f12a |
| test1 | all | overall | rmse_h50 | transformer[lookback=32] | 1.033 [0.758, 1.432] |  |  | 43 | 5 | a3e9d648 |
| test1 | start_points | overall | rmse_h1 | age_only | 2.180 [1.715, 2.676] |  |  | 43 | 5 | 7d094294 |
| test1 | start_points | overall | rmse_h1 | elasticnet | 0.936 [0.687, 1.247] |  |  | 43 | 5 | 910f2d53 |
| test1 | start_points | overall | rmse_h1 | itransformer[lookback=32] | 0.866 [0.679, 1.081] |  |  | 43 | 5 | 7ab9b903 |
| test1 | start_points | overall | rmse_h1 | lgbm | 0.548 [0.382, 0.762] |  |  | 43 | 5 | c867ad3f |
| test1 | start_points | overall | rmse_h1 | lstm[lookback=128] | 0.603 [0.405, 0.848] |  |  | 43 | 5 | 3bc20cea |
| test1 | start_points | overall | rmse_h1 | patchtst[lookback=128] | 0.996 [0.844, 1.174] |  |  | 43 | 5 | 1a28f12a |
| test1 | start_points | overall | rmse_h1 | transformer[lookback=32] | 0.620 [0.434, 0.849] |  |  | 43 | 5 | a3e9d648 |
| test1 | start_points | overall | rmse_h10 | age_only | 2.208 [1.713, 2.750] |  |  | 43 | 5 | 7d094294 |
| test1 | start_points | overall | rmse_h10 | elasticnet | 0.955 [0.687, 1.296] |  |  | 43 | 5 | 910f2d53 |
| test1 | start_points | overall | rmse_h10 | itransformer[lookback=32] | 0.902 [0.684, 1.159] |  |  | 43 | 5 | 7ab9b903 |
| test1 | start_points | overall | rmse_h10 | lgbm | 0.570 [0.392, 0.809] |  |  | 43 | 5 | c867ad3f |
| test1 | start_points | overall | rmse_h10 | lstm[lookback=128] | 0.659 [0.430, 0.951] |  |  | 43 | 5 | 3bc20cea |
| test1 | start_points | overall | rmse_h10 | patchtst[lookback=128] | 1.037 [0.878, 1.222] |  |  | 43 | 5 | 1a28f12a |
| test1 | start_points | overall | rmse_h10 | transformer[lookback=32] | 0.651 [0.444, 0.913] |  |  | 43 | 5 | a3e9d648 |
| test1 | start_points | overall | rmse_h50 | age_only | 2.420 [1.806, 3.205] |  |  | 43 | 5 | 7d094294 |
| test1 | start_points | overall | rmse_h50 | elasticnet | 1.236 [0.853, 1.719] |  |  | 43 | 5 | 910f2d53 |
| test1 | start_points | overall | rmse_h50 | itransformer[lookback=32] | 1.149 [0.827, 1.586] |  |  | 43 | 5 | 7ab9b903 |
| test1 | start_points | overall | rmse_h50 | lgbm | 0.713 [0.456, 1.131] |  |  | 43 | 5 | c867ad3f |
| test1 | start_points | overall | rmse_h50 | lstm[lookback=128] | 0.909 [0.547, 1.419] |  |  | 43 | 5 | 3bc20cea |
| test1 | start_points | overall | rmse_h50 | patchtst[lookback=128] | 1.329 [1.095, 1.609] |  |  | 43 | 5 | 1a28f12a |
| test1 | start_points | overall | rmse_h50 | transformer[lookback=32] | 0.905 [0.562, 1.396] |  |  | 43 | 5 | a3e9d648 |
| test2 | all | overall | rmse_h1 | age_only | 3.679 [3.525, 3.827] |  |  | 40 | 5 | 7d094294 |
| test2 | all | overall | rmse_h1 | elasticnet | 3.949 [3.821, 4.100] |  |  | 40 | 5 | 910f2d53 |
| test2 | all | overall | rmse_h1 | itransformer[lookback=32] | 1.557 [1.426, 1.696] |  |  | 40 | 5 | 7ab9b903 |
| test2 | all | overall | rmse_h1 | lgbm | 2.515 [2.390, 2.644] |  |  | 40 | 5 | c867ad3f |
| test2 | all | overall | rmse_h1 | lstm[lookback=128] | 2.278 [2.117, 2.464] |  |  | 40 | 5 | 3bc20cea |
| test2 | all | overall | rmse_h1 | patchtst[lookback=128] | 2.411 [2.295, 2.543] |  |  | 40 | 5 | 1a28f12a |
| test2 | all | overall | rmse_h1 | transformer[lookback=32] | 2.511 [2.369, 2.682] |  |  | 40 | 5 | a3e9d648 |
| test2 | all | overall | rmse_h10 | age_only | 3.696 [3.542, 3.844] |  |  | 40 | 5 | 7d094294 |
| test2 | all | overall | rmse_h10 | elasticnet | 4.071 [3.947, 4.217] |  |  | 40 | 5 | 910f2d53 |
| test2 | all | overall | rmse_h10 | itransformer[lookback=32] | 1.544 [1.414, 1.683] |  |  | 40 | 5 | 7ab9b903 |
| test2 | all | overall | rmse_h10 | lgbm | 2.542 [2.408, 2.679] |  |  | 40 | 5 | c867ad3f |
| test2 | all | overall | rmse_h10 | lstm[lookback=128] | 2.186 [2.037, 2.352] |  |  | 40 | 5 | 3bc20cea |
| test2 | all | overall | rmse_h10 | patchtst[lookback=128] | 2.449 [2.337, 2.578] |  |  | 40 | 5 | 1a28f12a |
| test2 | all | overall | rmse_h10 | transformer[lookback=32] | 2.956 [2.796, 3.151] |  |  | 40 | 5 | a3e9d648 |
| test2 | all | overall | rmse_h50 | age_only | 3.774 [3.621, 3.921] |  |  | 40 | 5 | 7d094294 |
| test2 | all | overall | rmse_h50 | elasticnet | 4.223 [4.026, 4.438] |  |  | 40 | 5 | 910f2d53 |
| test2 | all | overall | rmse_h50 | itransformer[lookback=32] | 1.903 [1.781, 2.029] |  |  | 40 | 5 | 7ab9b903 |
| test2 | all | overall | rmse_h50 | lgbm | 2.446 [2.306, 2.586] |  |  | 40 | 5 | c867ad3f |
| test2 | all | overall | rmse_h50 | lstm[lookback=128] | 2.200 [2.073, 2.341] |  |  | 40 | 5 | 3bc20cea |
| test2 | all | overall | rmse_h50 | patchtst[lookback=128] | 2.779 [2.683, 2.889] |  |  | 40 | 5 | 1a28f12a |
| test2 | all | overall | rmse_h50 | transformer[lookback=32] | 2.740 [2.524, 2.985] |  |  | 40 | 5 | a3e9d648 |
| test2 | start_points | overall | rmse_h1 | age_only | 3.520 [3.296, 3.727] |  |  | 40 | 5 | 7d094294 |
| test2 | start_points | overall | rmse_h1 | elasticnet | 1.734 [1.546, 1.923] |  |  | 40 | 5 | 910f2d53 |
| test2 | start_points | overall | rmse_h1 | itransformer[lookback=32] | 1.463 [1.283, 1.649] |  |  | 40 | 5 | 7ab9b903 |
| test2 | start_points | overall | rmse_h1 | lgbm | 1.400 [1.209, 1.586] |  |  | 40 | 5 | c867ad3f |
| test2 | start_points | overall | rmse_h1 | lstm[lookback=128] | 0.799 [0.706, 0.898] |  |  | 40 | 5 | 3bc20cea |
| test2 | start_points | overall | rmse_h1 | patchtst[lookback=128] | 1.139 [0.943, 1.372] |  |  | 40 | 5 | 1a28f12a |
| test2 | start_points | overall | rmse_h1 | transformer[lookback=32] | 1.243 [1.124, 1.355] |  |  | 40 | 5 | a3e9d648 |
| test2 | start_points | overall | rmse_h10 | age_only | 3.543 [3.330, 3.741] |  |  | 40 | 5 | 7d094294 |
| test2 | start_points | overall | rmse_h10 | elasticnet | 1.770 [1.583, 1.958] |  |  | 40 | 5 | 910f2d53 |
| test2 | start_points | overall | rmse_h10 | itransformer[lookback=32] | 1.442 [1.259, 1.631] |  |  | 40 | 5 | 7ab9b903 |
| test2 | start_points | overall | rmse_h10 | lgbm | 1.494 [1.287, 1.695] |  |  | 40 | 5 | c867ad3f |
| test2 | start_points | overall | rmse_h10 | lstm[lookback=128] | 0.876 [0.776, 0.976] |  |  | 40 | 5 | 3bc20cea |
| test2 | start_points | overall | rmse_h10 | patchtst[lookback=128] | 1.216 [1.018, 1.451] |  |  | 40 | 5 | 1a28f12a |
| test2 | start_points | overall | rmse_h10 | transformer[lookback=32] | 1.286 [1.155, 1.411] |  |  | 40 | 5 | a3e9d648 |
| test2 | start_points | overall | rmse_h50 | age_only | 3.594 [3.411, 3.767] |  |  | 40 | 5 | 7d094294 |
| test2 | start_points | overall | rmse_h50 | elasticnet | 1.851 [1.659, 2.038] |  |  | 40 | 5 | 910f2d53 |
| test2 | start_points | overall | rmse_h50 | itransformer[lookback=32] | 1.827 [1.642, 2.014] |  |  | 40 | 5 | 7ab9b903 |
| test2 | start_points | overall | rmse_h50 | lgbm | 1.719 [1.493, 1.936] |  |  | 40 | 5 | c867ad3f |
| test2 | start_points | overall | rmse_h50 | lstm[lookback=128] | 1.049 [0.928, 1.169] |  |  | 40 | 5 | 3bc20cea |
| test2 | start_points | overall | rmse_h50 | patchtst[lookback=128] | 1.599 [1.401, 1.831] |  |  | 40 | 5 | 1a28f12a |
| test2 | start_points | overall | rmse_h50 | transformer[lookback=32] | 1.370 [1.230, 1.506] |  |  | 40 | 5 | a3e9d648 |

### toyota_rul

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rul_mae | age_only | 236.073 [183.453, 298.130] |  |  | 43 | 5 | 576359ba |
| test1 | all | overall | rul_mae | elasticnet | 79.739 [58.521, 105.986] |  |  | 43 | 5 | e50c3707 |
| test1 | all | overall | rul_mae | itransformer[lookback=32] | 55.774 [44.839, 68.935] |  |  | 43 | 5 | b27d640a |
| test1 | all | overall | rul_mae | lgbm | 51.187 [38.059, 66.581] |  |  | 43 | 5 | baa7bf55 |
| test1 | all | overall | rul_mae | lstm[lookback=128] | 54.431 [42.184, 67.652] |  |  | 43 | 5 | 47f91b8d |
| test1 | all | overall | rul_mae | patchtst[lookback=128] | 99.480 [77.405, 127.415] |  |  | 43 | 5 | 67ad156f |
| test1 | all | overall | rul_mae | transformer[lookback=32] | 58.697 [44.806, 74.348] |  |  | 43 | 5 | 24fcd90b |
| test1 | start_points | overall | rul_mae | age_only | 252.663 [191.340, 327.323] |  |  | 43 | 5 | 576359ba |
| test1 | start_points | overall | rul_mae | elasticnet | 98.348 [70.593, 132.509] |  |  | 43 | 5 | e50c3707 |
| test1 | start_points | overall | rul_mae | itransformer[lookback=32] | 64.395 [49.131, 82.910] |  |  | 43 | 5 | b27d640a |
| test1 | start_points | overall | rul_mae | lgbm | 58.766 [42.670, 77.927] |  |  | 43 | 5 | baa7bf55 |
| test1 | start_points | overall | rul_mae | lstm[lookback=128] | 62.539 [47.900, 78.254] |  |  | 43 | 5 | 47f91b8d |
| test1 | start_points | overall | rul_mae | patchtst[lookback=128] | 108.571 [86.032, 135.270] |  |  | 43 | 5 | 67ad156f |
| test1 | start_points | overall | rul_mae | transformer[lookback=32] | 69.020 [51.221, 89.011] |  |  | 43 | 5 | 24fcd90b |
| test2 | all | overall | rul_mae | age_only | 259.429 [201.101, 324.658] |  |  | 40 | 5 | 576359ba |
| test2 | all | overall | rul_mae | elasticnet | 124.898 [95.315, 159.474] |  |  | 40 | 5 | e50c3707 |
| test2 | all | overall | rul_mae | itransformer[lookback=32] | 145.854 [113.607, 182.338] |  |  | 40 | 5 | b27d640a |
| test2 | all | overall | rul_mae | lgbm | 153.228 [125.299, 185.710] |  |  | 40 | 5 | baa7bf55 |
| test2 | all | overall | rul_mae | lstm[lookback=128] | 156.332 [127.005, 189.367] |  |  | 40 | 5 | 47f91b8d |
| test2 | all | overall | rul_mae | patchtst[lookback=128] | 245.471 [205.506, 290.332] |  |  | 40 | 5 | 67ad156f |
| test2 | all | overall | rul_mae | transformer[lookback=32] | 161.539 [127.163, 200.671] |  |  | 40 | 5 | 24fcd90b |
| test2 | start_points | overall | rul_mae | age_only | 300.581 [229.922, 379.256] |  |  | 40 | 5 | 576359ba |
| test2 | start_points | overall | rul_mae | elasticnet | 143.990 [105.595, 189.483] |  |  | 40 | 5 | e50c3707 |
| test2 | start_points | overall | rul_mae | itransformer[lookback=32] | 172.977 [131.696, 218.394] |  |  | 40 | 5 | b27d640a |
| test2 | start_points | overall | rul_mae | lgbm | 152.063 [116.871, 192.907] |  |  | 40 | 5 | baa7bf55 |
| test2 | start_points | overall | rul_mae | lstm[lookback=128] | 175.680 [139.591, 215.968] |  |  | 40 | 5 | 47f91b8d |
| test2 | start_points | overall | rul_mae | patchtst[lookback=128] | 285.235 [236.635, 340.083] |  |  | 40 | 5 | 67ad156f |
| test2 | start_points | overall | rul_mae | transformer[lookback=32] | 185.780 [141.719, 236.248] |  |  | 40 | 5 | 24fcd90b |

### toyota_soh

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rmse | age_only | 4.008 [3.665, 4.471] |  |  | 43 | 5 | cd1211f0 |
| test1 | all | overall | rmse | elasticnet | 1.181 [0.963, 1.458] |  |  | 43 | 5 | 1f049d74 |
| test1 | all | overall | rmse | itransformer[lookback=128] | 1.061 [0.814, 1.391] |  |  | 43 | 5 | f6b438b9 |
| test1 | all | overall | rmse | lgbm | 0.947 [0.750, 1.225] |  |  | 43 | 5 | 7345cc3d |
| test1 | all | overall | rmse | lstm[lookback=32] | 1.074 [0.796, 1.434] |  |  | 43 | 5 | 3ad2c3cb |
| test1 | all | overall | rmse | patchtst[lookback=128] | 1.643 [1.458, 1.854] |  |  | 43 | 5 | 271523a9 |
| test1 | all | overall | rmse | transformer[lookback=32] | 0.907 [0.621, 1.266] |  |  | 43 | 5 | e1e42381 |
| test1 | start_points | overall | rmse | age_only | 2.168 [1.705, 2.664] |  |  | 43 | 5 | cd1211f0 |
| test1 | start_points | overall | rmse | elasticnet | 0.959 [0.712, 1.266] |  |  | 43 | 5 | 1f049d74 |
| test1 | start_points | overall | rmse | itransformer[lookback=128] | 0.857 [0.645, 1.136] |  |  | 43 | 5 | f6b438b9 |
| test1 | start_points | overall | rmse | lgbm | 0.527 [0.378, 0.722] |  |  | 43 | 5 | 7345cc3d |
| test1 | start_points | overall | rmse | lstm[lookback=32] | 0.915 [0.599, 1.329] |  |  | 43 | 5 | 3ad2c3cb |
| test1 | start_points | overall | rmse | patchtst[lookback=128] | 1.124 [0.968, 1.290] |  |  | 43 | 5 | 271523a9 |
| test1 | start_points | overall | rmse | transformer[lookback=32] | 0.808 [0.482, 1.230] |  |  | 43 | 5 | e1e42381 |
| test2 | all | overall | rmse | age_only | 3.673 [3.520, 3.821] |  |  | 40 | 5 | cd1211f0 |
| test2 | all | overall | rmse | elasticnet | 4.155 [4.023, 4.310] |  |  | 40 | 5 | 1f049d74 |
| test2 | all | overall | rmse | itransformer[lookback=128] | 1.554 [1.417, 1.727] |  |  | 40 | 5 | f6b438b9 |
| test2 | all | overall | rmse | lgbm | 2.553 [2.429, 2.684] |  |  | 40 | 5 | 7345cc3d |
| test2 | all | overall | rmse | lstm[lookback=32] | 2.188 [2.072, 2.331] |  |  | 40 | 5 | 3ad2c3cb |
| test2 | all | overall | rmse | patchtst[lookback=128] | 2.676 [2.569, 2.799] |  |  | 40 | 5 | 271523a9 |
| test2 | all | overall | rmse | transformer[lookback=32] | 2.532 [2.435, 2.644] |  |  | 40 | 5 | e1e42381 |
| test2 | start_points | overall | rmse | age_only | 3.509 [3.286, 3.718] |  |  | 40 | 5 | cd1211f0 |
| test2 | start_points | overall | rmse | elasticnet | 1.709 [1.519, 1.899] |  |  | 40 | 5 | 1f049d74 |
| test2 | start_points | overall | rmse | itransformer[lookback=128] | 1.183 [0.992, 1.404] |  |  | 40 | 5 | f6b438b9 |
| test2 | start_points | overall | rmse | lgbm | 1.369 [1.180, 1.553] |  |  | 40 | 5 | 7345cc3d |
| test2 | start_points | overall | rmse | lstm[lookback=32] | 1.324 [1.194, 1.449] |  |  | 40 | 5 | 3ad2c3cb |
| test2 | start_points | overall | rmse | patchtst[lookback=128] | 1.253 [1.051, 1.493] |  |  | 40 | 5 | 271523a9 |
| test2 | start_points | overall | rmse | transformer[lookback=32] | 1.479 [1.339, 1.610] |  |  | 40 | 5 | e1e42381 |

## Mean rank (dataset x task x split x policy x headline metric)

| model | mean rank | conditions | missing |
|---|---|---|---|
| itransformer[lookback=128] | 2.00 | 4 | 36 |
| lstm[lookback=128] | 2.08 | 24 | 16 |
| lstm[lookback=32] | 2.50 | 6 | 34 |
| lstm[lookback=64] | 2.60 | 10 | 30 |
| itransformer[lookback=64] | 3.00 | 10 | 30 |
| transformer[lookback=32] | 3.00 | 28 | 12 |
| lgbm | 3.15 | 40 | 0 |
| itransformer[lookback=32] | 3.27 | 26 | 14 |
| transformer[lookback=128] | 4.00 | 2 | 38 |
| patchtst[lookback=64] | 4.20 | 10 | 30 |
| patchtst[lookback=128] | 4.85 | 20 | 20 |
| elasticnet | 4.92 | 40 | 0 |
| age_only | 5.58 | 40 | 0 |
| transformer[lookback=64] | 6.20 | 10 | 30 |
| patchtst[lookback=32] | 6.70 | 10 | 30 |

## Calibration (90 % intervals; PICP target 0.90 +/- 0.05; MPIW in %SOH or cycles)

Raw = stored (0.05, 0.95) quantiles; cal = CQR with pooled inner-val residuals (PROTOCOL §3/§5). Models without inner-val predictions (GPR) have raw only. mean [95% cluster-bootstrap CI over cells].

| dataset | task | policy | horizon | model | PICP raw | PICP cal | MPIW raw | MPIW cal | cells |
|---|---|---|---|---|---|---|---|---|---|
| calce | forecast | all | 1 | elasticnet | 0.000 [0.000, 0.000] | 0.904 [0.825, 0.969] | 0.000 [0.000, 0.000] | 8.589 [7.948, 9.495] | 4 |
| calce | forecast | all | 1 | itransformer[lookback=32] | 0.918 [0.873, 0.962] | 0.901 [0.842, 0.960] | 13.644 [12.467, 14.822] | 12.918 [11.342, 14.495] | 4 |
| calce | forecast | all | 1 | lgbm | 0.838 [0.698, 0.939] | 0.923 [0.857, 0.980] | 23.451 [20.444, 27.254] | 26.268 [23.539, 30.354] | 4 |
| calce | forecast | all | 1 | lstm[lookback=128] | 0.786 [0.688, 0.843] | 0.881 [0.763, 0.958] | 4.341 [3.834, 4.938] | 5.714 [5.024, 6.279] | 4 |
| calce | forecast | all | 1 | transformer[lookback=32] | 0.969 [0.955, 0.984] | 0.933 [0.916, 0.956] | 10.233 [8.999, 11.366] | 8.632 [7.446, 9.819] | 4 |
| calce | forecast | all | 10 | elasticnet | 0.000 [0.000, 0.000] | 0.895 [0.839, 0.951] | 0.000 [0.000, 0.000] | 8.453 [7.846, 9.225] | 4 |
| calce | forecast | all | 10 | itransformer[lookback=32] | 0.914 [0.874, 0.953] | 0.903 [0.852, 0.954] | 14.016 [12.618, 15.415] | 13.727 [11.888, 15.566] | 4 |
| calce | forecast | all | 10 | lgbm | 0.817 [0.646, 0.928] | 0.945 [0.889, 0.994] | 25.133 [20.849, 30.939] | 28.828 [24.903, 33.970] | 4 |
| calce | forecast | all | 10 | lstm[lookback=128] | 0.818 [0.761, 0.876] | 0.898 [0.833, 0.941] | 5.166 [4.412, 5.632] | 6.215 [5.683, 6.747] | 4 |
| calce | forecast | all | 10 | transformer[lookback=32] | 0.963 [0.955, 0.970] | 0.942 [0.931, 0.950] | 10.999 [8.988, 13.201] | 9.842 [8.429, 11.505] | 4 |
| calce | forecast | all | 25 | elasticnet | 0.000 [0.000, 0.000] | 0.916 [0.874, 0.945] | 0.000 [0.000, 0.000] | 9.241 [9.023, 9.625] | 4 |
| calce | forecast | all | 25 | itransformer[lookback=32] | 0.910 [0.871, 0.948] | 0.905 [0.861, 0.950] | 14.007 [12.480, 15.534] | 13.967 [12.197, 15.703] | 4 |
| calce | forecast | all | 25 | lgbm | 0.795 [0.631, 0.918] | 0.959 [0.921, 0.992] | 22.459 [16.960, 29.166] | 27.248 [21.664, 32.717] | 4 |
| calce | forecast | all | 25 | lstm[lookback=128] | 0.805 [0.721, 0.889] | 0.900 [0.856, 0.945] | 5.947 [4.959, 7.168] | 7.431 [6.547, 8.525] | 4 |
| calce | forecast | all | 25 | transformer[lookback=32] | 0.960 [0.947, 0.967] | 0.932 [0.917, 0.948] | 11.587 [9.556, 14.447] | 10.177 [8.511, 12.610] | 4 |
| calce | forecast | all | 50 | elasticnet | 0.000 [0.000, 0.000] | 0.913 [0.870, 0.937] | 0.000 [0.000, 0.000] | 10.214 [9.492, 10.648] | 4 |
| calce | forecast | all | 50 | itransformer[lookback=32] | 0.913 [0.865, 0.961] | 0.905 [0.850, 0.959] | 14.678 [13.024, 16.100] | 14.256 [12.406, 15.944] | 4 |
| calce | forecast | all | 50 | lgbm | 0.790 [0.641, 0.936] | 0.944 [0.891, 0.987] | 25.429 [22.260, 29.270] | 30.767 [26.766, 34.061] | 4 |
| calce | forecast | all | 50 | lstm[lookback=128] | 0.787 [0.682, 0.893] | 0.893 [0.825, 0.960] | 6.413 [5.163, 7.886] | 8.283 [6.888, 9.740] | 4 |
| calce | forecast | all | 50 | transformer[lookback=32] | 0.933 [0.902, 0.965] | 0.916 [0.870, 0.957] | 11.621 [9.283, 14.839] | 10.856 [8.702, 13.953] | 4 |
| calce | forecast | all | 100 | elasticnet | 0.000 [0.000, 0.000] | 0.923 [0.861, 0.986] | 0.000 [0.000, 0.000] | 12.993 [12.372, 13.518] | 4 |
| calce | forecast | all | 100 | itransformer[lookback=32] | 0.903 [0.849, 0.956] | 0.903 [0.844, 0.961] | 15.535 [14.036, 17.035] | 15.602 [13.933, 17.200] | 4 |
| calce | forecast | all | 100 | lgbm | 0.725 [0.595, 0.855] | 0.928 [0.877, 0.978] | 22.624 [16.974, 25.854] | 29.979 [25.083, 33.607] | 4 |
| calce | forecast | all | 100 | lstm[lookback=128] | 0.778 [0.665, 0.892] | 0.910 [0.841, 0.979] | 6.960 [5.936, 8.097] | 9.479 [8.365, 10.594] | 4 |
| calce | forecast | all | 100 | transformer[lookback=32] | 0.935 [0.892, 0.977] | 0.930 [0.879, 0.981] | 11.969 [10.328, 13.786] | 11.675 [10.473, 12.877] | 4 |
| calce | forecast | start_points | 1 | elasticnet | 0.000 [0.000, 0.000] | 0.850 [0.700, 1.000] | 0.000 [0.000, 0.000] | 8.589 [7.948, 9.495] | 4 |
| calce | forecast | start_points | 1 | itransformer[lookback=32] | 0.960 [0.910, 1.000] | 0.960 [0.910, 1.000] | 13.488 [12.084, 14.752] | 12.761 [10.926, 14.584] | 4 |
| calce | forecast | start_points | 1 | lgbm | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 18.594 [16.786, 21.643] | 21.411 [19.544, 24.647] | 4 |
| calce | forecast | start_points | 1 | lstm[lookback=128] | 0.850 [0.690, 0.980] | 0.990 [0.970, 1.000] | 3.166 [2.833, 3.500] | 4.539 [3.807, 5.064] | 4 |
| calce | forecast | start_points | 1 | transformer[lookback=32] | 0.990 [0.970, 1.000] | 0.950 [0.920, 0.980] | 7.851 [7.485, 8.152] | 6.250 [6.075, 6.517] | 4 |
| calce | forecast | start_points | 10 | elasticnet | 0.000 [0.000, 0.000] | 0.900 [0.800, 1.000] | 0.000 [0.000, 0.000] | 8.453 [7.846, 9.225] | 4 |
| calce | forecast | start_points | 10 | itransformer[lookback=32] | 0.990 [0.970, 1.000] | 0.960 [0.880, 1.000] | 13.340 [11.635, 15.285] | 13.051 [10.788, 15.869] | 4 |
| calce | forecast | start_points | 10 | lgbm | 0.900 [0.800, 1.000] | 0.950 [0.850, 1.000] | 21.039 [17.252, 26.643] | 24.735 [21.306, 29.675] | 4 |
| calce | forecast | start_points | 10 | lstm[lookback=128] | 0.770 [0.540, 1.000] | 0.910 [0.820, 1.000] | 3.667 [3.188, 4.269] | 4.716 [3.899, 5.407] | 4 |
| calce | forecast | start_points | 10 | transformer[lookback=32] | 0.980 [0.940, 1.000] | 0.980 [0.940, 1.000] | 8.390 [7.454, 9.802] | 7.233 [6.539, 8.256] | 4 |
| calce | forecast | start_points | 25 | elasticnet | 0.000 [0.000, 0.000] | 1.000 [1.000, 1.000] | 0.000 [0.000, 0.000] | 9.241 [9.023, 9.625] | 4 |
| calce | forecast | start_points | 25 | itransformer[lookback=32] | 0.990 [0.970, 1.000] | 0.990 [0.970, 1.000] | 13.181 [11.148, 15.351] | 13.141 [10.786, 15.874] | 4 |
| calce | forecast | start_points | 25 | lgbm | 0.700 [0.500, 0.900] | 1.000 [1.000, 1.000] | 18.665 [14.509, 24.869] | 23.455 [19.214, 28.420] | 4 |
| calce | forecast | start_points | 25 | lstm[lookback=128] | 0.840 [0.640, 1.000] | 0.940 [0.850, 1.000] | 3.904 [3.483, 4.360] | 5.388 [4.833, 5.880] | 4 |
| calce | forecast | start_points | 25 | transformer[lookback=32] | 0.970 [0.910, 1.000] | 0.980 [0.940, 1.000] | 8.863 [7.753, 10.355] | 7.452 [6.411, 8.621] | 4 |
| calce | forecast | start_points | 50 | elasticnet | 0.000 [0.000, 0.000] | 0.950 [0.850, 1.000] | 0.000 [0.000, 0.000] | 10.214 [9.492, 10.648] | 4 |
| calce | forecast | start_points | 50 | itransformer[lookback=32] | 1.000 [1.000, 1.000] | 0.990 [0.970, 1.000] | 13.458 [11.211, 15.772] | 13.037 [10.553, 15.727] | 4 |
| calce | forecast | start_points | 50 | lgbm | 0.700 [0.500, 0.900] | 0.950 [0.850, 1.000] | 21.019 [18.082, 24.822] | 26.357 [22.588, 29.651] | 4 |
| calce | forecast | start_points | 50 | lstm[lookback=128] | 0.810 [0.620, 1.000] | 0.890 [0.780, 1.000] | 4.324 [3.773, 4.993] | 6.194 [5.299, 7.089] | 4 |
| calce | forecast | start_points | 50 | transformer[lookback=32] | 0.920 [0.820, 1.000] | 0.930 [0.820, 1.000] | 8.902 [7.809, 10.106] | 8.138 [7.148, 9.302] | 4 |
| calce | forecast | start_points | 100 | elasticnet | 0.000 [0.000, 0.000] | 0.900 [0.700, 1.000] | 0.000 [0.000, 0.000] | 12.993 [12.372, 13.518] | 4 |
| calce | forecast | start_points | 100 | itransformer[lookback=32] | 0.990 [0.970, 1.000] | 0.980 [0.940, 1.000] | 13.787 [12.229, 15.225] | 13.854 [12.079, 15.489] | 4 |
| calce | forecast | start_points | 100 | lgbm | 0.800 [0.650, 0.950] | 1.000 [1.000, 1.000] | 18.265 [13.699, 21.105] | 25.620 [21.740, 28.499] | 4 |
| calce | forecast | start_points | 100 | lstm[lookback=128] | 0.835 [0.580, 1.000] | 0.900 [0.700, 1.000] | 5.003 [4.245, 5.761] | 7.522 [6.563, 8.481] | 4 |
| calce | forecast | start_points | 100 | transformer[lookback=32] | 0.920 [0.760, 1.000] | 0.920 [0.760, 1.000] | 9.507 [8.546, 10.467] | 9.212 [7.550, 10.781] | 4 |
| calce | rul | all | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.755 [0.510, 1.000] | 0.000 [0.000, 0.000] | 1795.954 [369.755, 3485.546] | 4 |
| calce | rul | all | 0 | itransformer[lookback=32] | 0.683 [0.363, 0.991] | 0.673 [0.318, 0.984] | 139.476 [120.276, 158.676] | 147.522 [115.274, 179.770] | 4 |
| calce | rul | all | 0 | lgbm | 0.780 [0.663, 0.921] | 0.865 [0.730, 1.000] | 349.139 [295.039, 399.093] | 409.060 [355.352, 451.680] | 4 |
| calce | rul | all | 0 | lstm[lookback=128] | 0.604 [0.292, 0.916] | 0.684 [0.398, 0.969] | 140.114 [111.408, 176.401] | 157.290 [121.008, 201.094] | 4 |
| calce | rul | all | 0 | transformer[lookback=32] | 0.726 [0.382, 0.951] | 0.776 [0.504, 0.974] | 197.585 [140.365, 243.746] | 221.254 [173.783, 265.215] | 4 |
| calce | rul | start_points | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.700 [0.400, 1.000] | 0.000 [0.000, 0.000] | 1795.954 [369.755, 3485.546] | 4 |
| calce | rul | start_points | 0 | itransformer[lookback=32] | 0.640 [0.280, 1.000] | 0.620 [0.240, 1.000] | 141.498 [121.026, 161.970] | 149.544 [116.025, 183.064] | 4 |
| calce | rul | start_points | 0 | lgbm | 0.900 [0.700, 1.000] | 0.900 [0.700, 1.000] | 324.971 [266.301, 379.364] | 384.892 [326.614, 431.451] | 4 |
| calce | rul | start_points | 0 | lstm[lookback=128] | 0.490 [0.120, 0.860] | 0.600 [0.240, 0.960] | 125.774 [97.006, 156.729] | 142.950 [106.607, 181.422] | 4 |
| calce | rul | start_points | 0 | transformer[lookback=32] | 0.690 [0.320, 0.950] | 0.730 [0.430, 0.940] | 198.170 [137.537, 245.932] | 221.838 [170.955, 271.525] | 4 |
| calce | soh | all | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.919 [0.873, 0.960] | 0.000 [0.000, 0.000] | 9.029 [8.123, 9.924] | 4 |
| calce | soh | all | 0 | itransformer[lookback=32] | 0.914 [0.864, 0.963] | 0.906 [0.845, 0.966] | 9.744 [8.549, 10.939] | 9.475 [8.351, 10.599] | 4 |
| calce | soh | all | 0 | lgbm | 0.864 [0.741, 0.946] | 0.942 [0.902, 0.985] | 24.032 [19.418, 27.791] | 26.021 [21.864, 29.618] | 4 |
| calce | soh | all | 0 | lstm[lookback=32] | 0.805 [0.690, 0.888] | 0.875 [0.775, 0.948] | 4.856 [4.268, 5.449] | 5.744 [5.236, 6.253] | 4 |
| calce | soh | all | 0 | transformer[lookback=128] | 0.905 [0.883, 0.928] | 0.911 [0.881, 0.942] | 9.551 [7.845, 11.628] | 9.596 [7.624, 11.838] | 4 |
| calce | soh | start_points | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.950 [0.850, 1.000] | 0.000 [0.000, 0.000] | 9.029 [8.123, 9.924] | 4 |
| calce | soh | start_points | 0 | itransformer[lookback=32] | 0.990 [0.970, 1.000] | 0.990 [0.970, 1.000] | 8.923 [7.436, 10.715] | 8.654 [6.912, 10.585] | 4 |
| calce | soh | start_points | 0 | lgbm | 0.850 [0.700, 1.000] | 1.000 [1.000, 1.000] | 19.877 [16.011, 23.107] | 21.866 [18.457, 24.934] | 4 |
| calce | soh | start_points | 0 | lstm[lookback=32] | 0.900 [0.840, 0.960] | 0.950 [0.880, 1.000] | 2.983 [2.864, 3.103] | 3.872 [3.731, 4.023] | 4 |
| calce | soh | start_points | 0 | transformer[lookback=128] | 0.940 [0.920, 0.980] | 0.930 [0.890, 0.980] | 8.891 [5.968, 14.128] | 8.936 [5.909, 14.333] | 4 |
| nasa | forecast | all | 1 | elasticnet | 0.000 [0.000, 0.000] | 0.785 [0.439, 0.994] | 0.000 [0.000, 0.000] | 8.638 [7.484, 10.154] | 4 |
| nasa | forecast | all | 1 | itransformer[lookback=64] | 0.807 [0.599, 0.948] | 0.829 [0.583, 0.988] | 22.411 [16.873, 27.949] | 26.625 [18.503, 34.698] | 4 |
| nasa | forecast | all | 1 | lgbm | 0.652 [0.466, 0.838] | 0.873 [0.620, 1.000] | 14.349 [12.587, 16.110] | 23.308 [21.233, 25.383] | 4 |
| nasa | forecast | all | 1 | lstm[lookback=64] | 0.841 [0.576, 0.995] | 0.858 [0.593, 0.997] | 19.881 [15.569, 24.324] | 21.437 [16.679, 26.571] | 4 |
| nasa | forecast | all | 1 | transformer[lookback=64] | 0.916 [0.788, 0.991] | 0.898 [0.743, 0.993] | 36.359 [28.629, 44.089] | 38.640 [32.249, 46.583] | 4 |
| nasa | forecast | all | 10 | elasticnet | 0.000 [0.000, 0.000] | 0.912 [0.737, 1.000] | 0.000 [0.000, 0.000] | 18.507 [13.976, 22.720] | 4 |
| nasa | forecast | all | 10 | itransformer[lookback=64] | 0.809 [0.575, 0.954] | 0.834 [0.583, 0.988] | 21.531 [16.925, 25.981] | 25.972 [17.918, 33.165] | 4 |
| nasa | forecast | all | 10 | lgbm | 0.628 [0.401, 0.843] | 0.843 [0.528, 1.000] | 13.192 [11.607, 14.776] | 23.857 [20.675, 25.898] | 4 |
| nasa | forecast | all | 10 | lstm[lookback=64] | 0.797 [0.531, 0.966] | 0.829 [0.587, 0.996] | 23.016 [18.619, 26.877] | 27.160 [20.727, 33.001] | 4 |
| nasa | forecast | all | 10 | transformer[lookback=64] | 0.908 [0.835, 0.960] | 0.928 [0.851, 0.983] | 37.579 [31.117, 46.860] | 41.379 [34.966, 51.586] | 4 |
| nasa | forecast | all | 25 | elasticnet | 0.000 [0.000, 0.000] | 1.000 [1.000, 1.000] | 0.000 [0.000, 0.000] | 27.731 [23.637, 34.304] | 4 |
| nasa | forecast | all | 25 | itransformer[lookback=64] | 0.816 [0.543, 0.960] | 0.829 [0.526, 0.989] | 20.929 [16.253, 25.606] | 24.643 [17.230, 31.256] | 4 |
| nasa | forecast | all | 25 | lgbm | 0.683 [0.417, 0.895] | 0.846 [0.537, 1.000] | 13.955 [11.668, 15.771] | 26.415 [22.460, 29.938] | 4 |
| nasa | forecast | all | 25 | lstm[lookback=64] | 0.829 [0.581, 0.986] | 0.875 [0.638, 0.997] | 19.914 [17.222, 23.963] | 24.852 [20.285, 28.616] | 4 |
| nasa | forecast | all | 25 | transformer[lookback=64] | 0.906 [0.819, 0.984] | 0.890 [0.831, 0.950] | 32.713 [24.168, 39.941] | 35.661 [29.063, 43.450] | 4 |
| nasa | forecast | all | 50 | elasticnet | 0.000 [0.000, 0.000] | 0.893 [0.679, 1.000] | 0.000 [0.000, 0.000] | 30.426 [26.596, 34.655] | 4 |
| nasa | forecast | all | 50 | itransformer[lookback=64] | 0.765 [0.457, 0.957] | 0.805 [0.480, 0.989] | 21.599 [17.226, 25.971] | 26.740 [19.024, 33.061] | 4 |
| nasa | forecast | all | 50 | lgbm | 0.656 [0.342, 0.904] | 0.828 [0.484, 1.000] | 13.145 [9.951, 16.948] | 27.880 [20.822, 33.525] | 4 |
| nasa | forecast | all | 50 | lstm[lookback=64] | 0.838 [0.550, 0.996] | 0.851 [0.584, 0.999] | 23.804 [18.565, 28.142] | 28.859 [21.201, 35.026] | 4 |
| nasa | forecast | all | 50 | transformer[lookback=64] | 0.796 [0.749, 0.844] | 0.901 [0.807, 0.986] | 28.647 [22.382, 34.912] | 34.364 [28.720, 40.009] | 4 |
| nasa | forecast | all | 100 | elasticnet | 0.000 [0.000, 0.000] | 0.750 [0.250, 1.000] | 0.000 [0.000, 0.000] | 26.834 [17.954, 33.094] | 4 |
| nasa | forecast | all | 100 | itransformer[lookback=64] | 0.770 [0.401, 0.965] | 0.809 [0.427, 1.000] | 24.678 [16.996, 32.360] | 34.491 [22.677, 45.782] | 4 |
| nasa | forecast | all | 100 | lgbm | 0.520 [0.177, 0.863] | 0.750 [0.250, 1.000] | 11.232 [8.109, 14.355] | 28.499 [18.425, 34.149] | 4 |
| nasa | forecast | all | 100 | lstm[lookback=64] | 0.682 [0.365, 1.000] | 0.823 [0.519, 1.000] | 23.783 [18.610, 27.750] | 36.819 [27.018, 44.241] | 4 |
| nasa | forecast | all | 100 | transformer[lookback=64] | 0.801 [0.533, 1.000] | 0.802 [0.581, 1.000] | 28.571 [23.614, 32.741] | 34.044 [24.777, 42.568] | 4 |
| nasa | forecast | start_points | 1 | elasticnet | 0.000 [0.000, 0.000] | 0.938 [0.812, 1.000] | 0.000 [0.000, 0.000] | 8.638 [7.484, 10.154] | 4 |
| nasa | forecast | start_points | 1 | itransformer[lookback=64] | 0.896 [0.833, 0.942] | 0.933 [0.850, 1.000] | 25.031 [17.473, 32.588] | 29.245 [19.152, 39.338] | 4 |
| nasa | forecast | start_points | 1 | lgbm | 0.750 [0.438, 1.000] | 1.000 [1.000, 1.000] | 15.232 [13.292, 18.233] | 24.191 [20.589, 27.652] | 4 |
| nasa | forecast | start_points | 1 | lstm[lookback=64] | 0.867 [0.600, 1.000] | 0.825 [0.550, 1.000] | 18.815 [13.369, 23.813] | 20.371 [14.478, 26.059] | 4 |
| nasa | forecast | start_points | 1 | transformer[lookback=64] | 0.917 [0.750, 1.000] | 0.854 [0.600, 1.000] | 25.268 [23.033, 28.337] | 27.549 [23.633, 31.636] | 4 |
| nasa | forecast | start_points | 10 | elasticnet | 0.000 [0.000, 0.000] | 1.000 [1.000, 1.000] | 0.000 [0.000, 0.000] | 18.507 [13.976, 22.720] | 4 |
| nasa | forecast | start_points | 10 | itransformer[lookback=64] | 0.930 [0.840, 0.990] | 0.970 [0.910, 1.000] | 23.369 [18.767, 28.404] | 27.811 [19.761, 36.761] | 4 |
| nasa | forecast | start_points | 10 | lgbm | 0.600 [0.300, 0.900] | 1.000 [1.000, 1.000] | 14.430 [12.769, 15.681] | 25.096 [21.024, 27.326] | 4 |
| nasa | forecast | start_points | 10 | lstm[lookback=64] | 0.790 [0.430, 1.000] | 0.790 [0.430, 1.000] | 22.880 [15.912, 27.329] | 27.025 [17.856, 33.427] | 4 |
| nasa | forecast | start_points | 10 | transformer[lookback=64] | 0.950 [0.850, 1.000] | 0.960 [0.910, 1.000] | 27.160 [22.477, 35.157] | 30.961 [24.371, 40.458] | 4 |
| nasa | forecast | start_points | 25 | elasticnet | 0.000 [0.000, 0.000] | 1.000 [1.000, 1.000] | 0.000 [0.000, 0.000] | 27.731 [23.637, 34.304] | 4 |
| nasa | forecast | start_points | 25 | itransformer[lookback=64] | 0.900 [0.830, 0.950] | 0.930 [0.820, 1.000] | 24.633 [19.162, 30.105] | 28.347 [19.962, 35.948] | 4 |
| nasa | forecast | start_points | 25 | lgbm | 0.750 [0.650, 0.800] | 1.000 [1.000, 1.000] | 14.497 [11.759, 16.267] | 26.958 [22.341, 31.368] | 4 |
| nasa | forecast | start_points | 25 | lstm[lookback=64] | 0.780 [0.390, 0.990] | 0.820 [0.490, 1.000] | 19.267 [14.035, 24.475] | 24.205 [17.346, 29.128] | 4 |
| nasa | forecast | start_points | 25 | transformer[lookback=64] | 0.860 [0.680, 0.980] | 0.880 [0.760, 1.000] | 24.319 [19.522, 29.916] | 27.268 [21.836, 34.285] | 4 |
| nasa | forecast | start_points | 50 | elasticnet | 0.000 [0.000, 0.000] | 0.850 [0.550, 1.000] | 0.000 [0.000, 0.000] | 30.426 [26.596, 34.655] | 4 |
| nasa | forecast | start_points | 50 | itransformer[lookback=64] | 0.820 [0.610, 1.000] | 0.840 [0.610, 1.000] | 23.615 [17.689, 28.922] | 28.756 [19.125, 36.763] | 4 |
| nasa | forecast | start_points | 50 | lgbm | 0.650 [0.350, 0.900] | 0.950 [0.850, 1.000] | 12.687 [9.354, 16.567] | 27.421 [20.443, 33.144] | 4 |
| nasa | forecast | start_points | 50 | lstm[lookback=64] | 0.780 [0.400, 1.000] | 0.810 [0.460, 1.000] | 23.907 [18.035, 29.570] | 28.962 [20.672, 36.621] | 4 |
| nasa | forecast | start_points | 50 | transformer[lookback=64] | 0.740 [0.650, 0.820] | 0.880 [0.700, 1.000] | 23.100 [20.003, 28.527] | 28.817 [25.381, 34.730] | 4 |
| nasa | forecast | start_points | 100 | elasticnet | 0.000 [0.000, 0.000] | 0.750 [0.250, 1.000] | 0.000 [0.000, 0.000] | 26.834 [17.954, 33.094] | 4 |
| nasa | forecast | start_points | 100 | itransformer[lookback=64] | 0.750 [0.387, 0.950] | 0.820 [0.460, 1.000] | 27.727 [17.829, 37.626] | 37.540 [23.613, 51.048] | 4 |
| nasa | forecast | start_points | 100 | lgbm | 0.625 [0.250, 1.000] | 0.750 [0.250, 1.000] | 11.150 [7.994, 14.305] | 28.417 [18.306, 34.083] | 4 |
| nasa | forecast | start_points | 100 | lstm[lookback=64] | 0.650 [0.300, 1.000] | 0.835 [0.580, 1.000] | 22.341 [17.030, 27.363] | 35.376 [25.738, 42.989] | 4 |
| nasa | forecast | start_points | 100 | transformer[lookback=64] | 0.790 [0.520, 1.000] | 0.785 [0.570, 1.000] | 27.395 [22.173, 31.002] | 32.868 [23.336, 40.666] | 4 |
| nasa | rul | all | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.785 [0.356, 1.000] | 0.000 [0.000, 0.000] | 4891.846 [678.611, 11418.528] | 4 |
| nasa | rul | all | 0 | itransformer[lookback=64] | 0.773 [0.629, 0.918] | 0.855 [0.746, 0.964] | 55.797 [48.462, 63.131] | 65.209 [54.854, 80.192] | 4 |
| nasa | rul | all | 0 | lgbm | 0.667 [0.424, 0.911] | 0.870 [0.736, 1.000] | 65.181 [57.233, 73.128] | 101.593 [81.831, 125.077] | 4 |
| nasa | rul | all | 0 | lstm[lookback=64] | 0.728 [0.487, 0.878] | 0.783 [0.502, 0.952] | 62.184 [57.669, 67.545] | 70.407 [65.634, 74.770] | 4 |
| nasa | rul | all | 0 | transformer[lookback=64] | 0.609 [0.401, 0.773] | 0.651 [0.406, 0.860] | 61.781 [58.648, 64.914] | 71.766 [56.328, 90.538] | 4 |
| nasa | rul | start_points | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.750 [0.250, 1.000] | 0.000 [0.000, 0.000] | 4891.846 [678.611, 11418.528] | 4 |
| nasa | rul | start_points | 0 | itransformer[lookback=64] | 0.860 [0.720, 1.000] | 0.910 [0.790, 1.000] | 56.358 [47.262, 65.685] | 65.770 [52.973, 83.780] | 4 |
| nasa | rul | start_points | 0 | lgbm | 0.650 [0.300, 1.000] | 0.900 [0.700, 1.000] | 62.906 [55.003, 71.050] | 99.319 [79.516, 122.255] | 4 |
| nasa | rul | start_points | 0 | lstm[lookback=64] | 0.700 [0.520, 0.880] | 0.800 [0.550, 1.000] | 59.531 [54.098, 64.113] | 67.753 [61.376, 74.130] | 4 |
| nasa | rul | start_points | 0 | transformer[lookback=64] | 0.610 [0.320, 0.900] | 0.690 [0.400, 0.980] | 62.093 [58.502, 65.609] | 72.078 [56.144, 91.689] | 4 |
| nasa | soh | all | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.886 [0.664, 1.000] | 0.000 [0.000, 0.000] | 30.984 [13.177, 48.792] | 4 |
| nasa | soh | all | 0 | itransformer[lookback=64] | 0.787 [0.526, 0.962] | 0.799 [0.511, 0.981] | 16.841 [12.303, 20.826] | 18.539 [12.329, 23.995] | 4 |
| nasa | soh | all | 0 | lgbm | 0.659 [0.350, 0.901] | 0.880 [0.639, 1.000] | 7.924 [6.176, 9.671] | 18.598 [14.431, 22.317] | 4 |
| nasa | soh | all | 0 | lstm[lookback=64] | 0.742 [0.335, 0.967] | 0.767 [0.348, 0.996] | 14.903 [10.991, 18.453] | 17.253 [11.852, 21.816] | 4 |
| nasa | soh | all | 0 | transformer[lookback=64] | 0.981 [0.956, 1.000] | 0.931 [0.878, 0.979] | 46.652 [43.756, 49.134] | 43.209 [40.318, 46.100] | 4 |
| nasa | soh | start_points | 0 | elasticnet | 0.000 [0.000, 0.000] | 1.000 [1.000, 1.000] | 0.000 [0.000, 0.000] | 30.984 [13.177, 48.792] | 4 |
| nasa | soh | start_points | 0 | itransformer[lookback=64] | 0.920 [0.810, 0.990] | 0.910 [0.810, 0.980] | 18.476 [12.989, 24.478] | 20.174 [13.015, 27.647] | 4 |
| nasa | soh | start_points | 0 | lgbm | 0.850 [0.700, 1.000] | 1.000 [1.000, 1.000] | 10.224 [7.533, 12.915] | 20.898 [15.856, 25.085] | 4 |
| nasa | soh | start_points | 0 | lstm[lookback=64] | 0.780 [0.420, 0.980] | 0.810 [0.430, 1.000] | 15.465 [10.661, 19.120] | 17.815 [11.521, 22.929] | 4 |
| nasa | soh | start_points | 0 | transformer[lookback=64] | 0.970 [0.940, 1.000] | 0.910 [0.840, 0.980] | 42.514 [35.239, 49.444] | 39.071 [33.501, 43.894] | 4 |
| toyota | forecast | all | 1 | elasticnet | 0.000 [0.000, 0.000] | 0.895 [0.846, 0.935] | 0.000 [0.000, 0.000] | 3.765 [3.765, 3.765] | 43 |
| toyota | forecast | all | 1 | itransformer[lookback=32] | 0.929 [0.884, 0.965] | 0.912 [0.864, 0.952] | 4.318 [4.126, 4.519] | 3.983 [3.791, 4.184] | 43 |
| toyota | forecast | all | 1 | lgbm | 0.876 [0.839, 0.910] | 0.958 [0.930, 0.979] | 5.190 [4.927, 5.483] | 5.620 [5.357, 5.913] | 43 |
| toyota | forecast | all | 1 | lstm[lookback=128] | 0.885 [0.827, 0.936] | 0.916 [0.864, 0.960] | 2.495 [2.265, 2.757] | 2.814 [2.584, 3.076] | 43 |
| toyota | forecast | all | 1 | transformer[lookback=32] | 0.956 [0.918, 0.986] | 0.950 [0.910, 0.982] | 3.621 [3.464, 3.818] | 3.380 [3.223, 3.577] | 43 |
| toyota | forecast | all | 10 | elasticnet | 0.000 [0.000, 0.000] | 0.894 [0.842, 0.937] | 0.000 [0.000, 0.000] | 3.822 [3.822, 3.822] | 43 |
| toyota | forecast | all | 10 | itransformer[lookback=32] | 0.920 [0.870, 0.960] | 0.913 [0.861, 0.954] | 4.125 [3.967, 4.290] | 3.986 [3.828, 4.151] | 43 |
| toyota | forecast | all | 10 | lgbm | 0.879 [0.841, 0.914] | 0.957 [0.929, 0.979] | 4.772 [4.508, 5.072] | 5.193 [4.929, 5.493] | 43 |
| toyota | forecast | all | 10 | lstm[lookback=128] | 0.876 [0.818, 0.927] | 0.919 [0.868, 0.963] | 2.091 [1.926, 2.283] | 2.541 [2.376, 2.733] | 43 |
| toyota | forecast | all | 10 | transformer[lookback=32] | 0.952 [0.911, 0.985] | 0.946 [0.903, 0.982] | 3.760 [3.585, 3.980] | 3.507 [3.332, 3.727] | 43 |
| toyota | forecast | all | 50 | elasticnet | 0.000 [0.000, 0.000] | 0.890 [0.831, 0.936] | 0.000 [0.000, 0.000] | 4.441 [4.441, 4.441] | 43 |
| toyota | forecast | all | 50 | itransformer[lookback=32] | 0.902 [0.841, 0.951] | 0.895 [0.833, 0.946] | 4.587 [4.394, 4.787] | 4.434 [4.240, 4.634] | 43 |
| toyota | forecast | all | 50 | lgbm | 0.841 [0.787, 0.889] | 0.937 [0.895, 0.968] | 4.616 [4.312, 4.962] | 5.030 [4.726, 5.376] | 43 |
| toyota | forecast | all | 50 | lstm[lookback=128] | 0.855 [0.790, 0.913] | 0.904 [0.844, 0.953] | 2.433 [2.244, 2.644] | 2.886 [2.697, 3.097] | 43 |
| toyota | forecast | all | 50 | transformer[lookback=32] | 0.936 [0.883, 0.974] | 0.938 [0.886, 0.976] | 3.788 [3.585, 4.028] | 3.904 [3.701, 4.144] | 43 |
| toyota | forecast | all | 100 | elasticnet | 0.000 [0.000, 0.000] | 0.890 [0.829, 0.938] | 0.000 [0.000, 0.000] | 5.745 [5.745, 5.745] | 43 |
| toyota | forecast | all | 100 | itransformer[lookback=32] | 0.880 [0.810, 0.939] | 0.887 [0.817, 0.944] | 5.353 [5.113, 5.602] | 5.485 [5.245, 5.734] | 43 |
| toyota | forecast | all | 100 | lgbm | 0.802 [0.740, 0.856] | 0.918 [0.864, 0.956] | 4.856 [4.479, 5.260] | 5.577 [5.200, 5.981] | 43 |
| toyota | forecast | all | 100 | lstm[lookback=128] | 0.889 [0.830, 0.936] | 0.907 [0.848, 0.953] | 3.747 [3.438, 4.090] | 3.988 [3.679, 4.331] | 43 |
| toyota | forecast | all | 100 | transformer[lookback=32] | 0.922 [0.866, 0.963] | 0.928 [0.872, 0.968] | 4.485 [4.269, 4.734] | 4.715 [4.499, 4.964] | 43 |
| toyota | forecast | all | 200 | elasticnet | 0.000 [0.000, 0.000] | 0.916 [0.867, 0.954] | 0.000 [0.000, 0.000] | 8.635 [8.635, 8.635] | 42 |
| toyota | forecast | all | 200 | itransformer[lookback=32] | 0.877 [0.807, 0.934] | 0.884 [0.815, 0.940] | 7.767 [7.337, 8.239] | 7.968 [7.538, 8.440] | 42 |
| toyota | forecast | all | 200 | lgbm | 0.828 [0.758, 0.887] | 0.925 [0.869, 0.963] | 5.842 [5.412, 6.299] | 7.200 [6.770, 7.657] | 42 |
| toyota | forecast | all | 200 | lstm[lookback=128] | 0.900 [0.846, 0.943] | 0.922 [0.870, 0.961] | 5.185 [4.765, 5.651] | 5.630 [5.210, 6.097] | 42 |
| toyota | forecast | all | 200 | transformer[lookback=32] | 0.921 [0.866, 0.962] | 0.929 [0.876, 0.968] | 6.567 [6.175, 6.985] | 6.786 [6.394, 7.204] | 42 |
| toyota | forecast | start_points | 1 | elasticnet | 0.000 [0.000, 0.000] | 0.936 [0.884, 0.977] | 0.000 [0.000, 0.000] | 3.765 [3.765, 3.765] | 43 |
| toyota | forecast | start_points | 1 | itransformer[lookback=32] | 0.916 [0.864, 0.960] | 0.902 [0.845, 0.951] | 3.732 [3.544, 3.923] | 3.397 [3.209, 3.588] | 43 |
| toyota | forecast | start_points | 1 | lgbm | 0.872 [0.814, 0.924] | 0.977 [0.948, 1.000] | 3.942 [3.728, 4.197] | 4.372 [4.158, 4.627] | 43 |
| toyota | forecast | start_points | 1 | lstm[lookback=128] | 0.873 [0.807, 0.933] | 0.914 [0.857, 0.964] | 2.254 [2.029, 2.503] | 2.572 [2.348, 2.822] | 43 |
| toyota | forecast | start_points | 1 | transformer[lookback=32] | 0.952 [0.905, 0.990] | 0.945 [0.894, 0.986] | 3.296 [3.141, 3.488] | 3.055 [2.900, 3.247] | 43 |
| toyota | forecast | start_points | 10 | elasticnet | 0.000 [0.000, 0.000] | 0.942 [0.884, 0.988] | 0.000 [0.000, 0.000] | 3.822 [3.822, 3.822] | 43 |
| toyota | forecast | start_points | 10 | itransformer[lookback=32] | 0.906 [0.842, 0.958] | 0.898 [0.833, 0.951] | 3.626 [3.470, 3.789] | 3.488 [3.331, 3.650] | 43 |
| toyota | forecast | start_points | 10 | lgbm | 0.890 [0.826, 0.942] | 0.977 [0.948, 1.000] | 3.719 [3.486, 4.001] | 4.140 [3.907, 4.422] | 43 |
| toyota | forecast | start_points | 10 | lstm[lookback=128] | 0.877 [0.809, 0.937] | 0.916 [0.860, 0.965] | 1.737 [1.566, 1.932] | 2.187 [2.016, 2.382] | 43 |
| toyota | forecast | start_points | 10 | transformer[lookback=32] | 0.945 [0.894, 0.987] | 0.938 [0.884, 0.985] | 3.498 [3.341, 3.696] | 3.245 [3.088, 3.443] | 43 |
| toyota | forecast | start_points | 50 | elasticnet | 0.000 [0.000, 0.000] | 0.936 [0.872, 0.983] | 0.000 [0.000, 0.000] | 4.441 [4.441, 4.441] | 43 |
| toyota | forecast | start_points | 50 | itransformer[lookback=32] | 0.895 [0.827, 0.952] | 0.890 [0.819, 0.949] | 4.146 [3.940, 4.356] | 3.993 [3.787, 4.203] | 43 |
| toyota | forecast | start_points | 50 | lgbm | 0.872 [0.797, 0.936] | 0.965 [0.913, 1.000] | 3.630 [3.288, 4.047] | 4.043 [3.702, 4.461] | 43 |
| toyota | forecast | start_points | 50 | lstm[lookback=128] | 0.830 [0.756, 0.898] | 0.900 [0.836, 0.955] | 2.020 [1.817, 2.249] | 2.473 [2.270, 2.702] | 43 |
| toyota | forecast | start_points | 50 | transformer[lookback=32] | 0.928 [0.866, 0.976] | 0.930 [0.869, 0.977] | 3.356 [3.169, 3.583] | 3.473 [3.285, 3.699] | 43 |
| toyota | forecast | start_points | 100 | elasticnet | 0.000 [0.000, 0.000] | 0.907 [0.837, 0.965] | 0.000 [0.000, 0.000] | 5.745 [5.745, 5.745] | 43 |
| toyota | forecast | start_points | 100 | itransformer[lookback=32] | 0.876 [0.803, 0.937] | 0.887 [0.817, 0.945] | 4.966 [4.733, 5.211] | 5.098 [4.865, 5.343] | 43 |
| toyota | forecast | start_points | 100 | lgbm | 0.855 [0.779, 0.919] | 0.942 [0.884, 0.988] | 4.220 [3.786, 4.694] | 4.941 [4.507, 5.416] | 43 |
| toyota | forecast | start_points | 100 | lstm[lookback=128] | 0.883 [0.820, 0.934] | 0.906 [0.843, 0.956] | 3.337 [3.009, 3.707] | 3.578 [3.250, 3.948] | 43 |
| toyota | forecast | start_points | 100 | transformer[lookback=32] | 0.924 [0.863, 0.971] | 0.929 [0.867, 0.976] | 4.150 [3.922, 4.415] | 4.380 [4.153, 4.646] | 43 |
| toyota | forecast | start_points | 200 | elasticnet | 0.000 [0.000, 0.000] | 0.921 [0.857, 0.970] | 0.000 [0.000, 0.000] | 8.635 [8.635, 8.635] | 42 |
| toyota | forecast | start_points | 200 | itransformer[lookback=32] | 0.871 [0.796, 0.936] | 0.883 [0.813, 0.942] | 7.516 [7.083, 7.994] | 7.717 [7.284, 8.196] | 42 |
| toyota | forecast | start_points | 200 | lgbm | 0.861 [0.778, 0.935] | 0.938 [0.879, 0.982] | 5.548 [5.104, 6.020] | 6.907 [6.463, 7.379] | 42 |
| toyota | forecast | start_points | 200 | lstm[lookback=128] | 0.902 [0.840, 0.952] | 0.931 [0.871, 0.973] | 4.954 [4.497, 5.434] | 5.399 [4.942, 5.879] | 42 |
| toyota | forecast | start_points | 200 | transformer[lookback=32] | 0.908 [0.842, 0.960] | 0.919 [0.854, 0.968] | 6.330 [5.918, 6.759] | 6.549 [6.138, 6.979] | 42 |
| toyota | forecast | all | 1 | elasticnet | 0.000 [0.000, 0.000] | 0.551 [0.466, 0.634] | 0.000 [0.000, 0.000] | 3.765 [3.765, 3.765] | 40 |
| toyota | forecast | all | 1 | itransformer[lookback=32] | 0.797 [0.762, 0.832] | 0.753 [0.715, 0.791] | 4.220 [4.078, 4.375] | 3.886 [3.743, 4.040] | 40 |
| toyota | forecast | all | 1 | lgbm | 0.803 [0.736, 0.866] | 0.924 [0.886, 0.956] | 5.582 [5.408, 5.796] | 6.012 [5.838, 6.226] | 40 |
| toyota | forecast | all | 1 | lstm[lookback=128] | 0.726 [0.682, 0.766] | 0.783 [0.743, 0.818] | 2.878 [2.733, 3.047] | 3.197 [3.052, 3.366] | 40 |
| toyota | forecast | all | 1 | transformer[lookback=32] | 0.641 [0.590, 0.693] | 0.588 [0.536, 0.642] | 3.588 [3.499, 3.699] | 3.347 [3.258, 3.458] | 40 |
| toyota | forecast | all | 10 | elasticnet | 0.000 [0.000, 0.000] | 0.554 [0.471, 0.636] | 0.000 [0.000, 0.000] | 3.822 [3.822, 3.822] | 40 |
| toyota | forecast | all | 10 | itransformer[lookback=32] | 0.793 [0.758, 0.825] | 0.775 [0.740, 0.809] | 3.922 [3.801, 4.052] | 3.784 [3.662, 3.913] | 40 |
| toyota | forecast | all | 10 | lgbm | 0.733 [0.657, 0.808] | 0.886 [0.836, 0.931] | 5.369 [5.189, 5.588] | 5.790 [5.610, 6.010] | 40 |
| toyota | forecast | all | 10 | lstm[lookback=128] | 0.555 [0.498, 0.613] | 0.688 [0.636, 0.739] | 2.203 [2.113, 2.301] | 2.653 [2.563, 2.751] | 40 |
| toyota | forecast | all | 10 | transformer[lookback=32] | 0.708 [0.668, 0.749] | 0.691 [0.646, 0.735] | 4.069 [3.910, 4.268] | 3.816 [3.657, 4.015] | 40 |
| toyota | forecast | all | 50 | elasticnet | 0.000 [0.000, 0.000] | 0.662 [0.596, 0.725] | 0.000 [0.000, 0.000] | 4.441 [4.441, 4.441] | 40 |
| toyota | forecast | all | 50 | itransformer[lookback=32] | 0.701 [0.663, 0.740] | 0.682 [0.643, 0.721] | 4.285 [4.146, 4.435] | 4.131 [3.992, 4.282] | 40 |
| toyota | forecast | all | 50 | lgbm | 0.734 [0.647, 0.818] | 0.854 [0.793, 0.911] | 5.289 [5.079, 5.541] | 5.702 [5.493, 5.955] | 40 |
| toyota | forecast | all | 50 | lstm[lookback=128] | 0.593 [0.543, 0.645] | 0.698 [0.652, 0.746] | 2.427 [2.306, 2.565] | 2.880 [2.759, 3.018] | 40 |
| toyota | forecast | all | 50 | transformer[lookback=32] | 0.571 [0.506, 0.637] | 0.592 [0.532, 0.653] | 3.570 [3.456, 3.714] | 3.687 [3.572, 3.831] | 40 |
| toyota | forecast | all | 100 | elasticnet | 0.000 [0.000, 0.000] | 0.829 [0.794, 0.862] | 0.000 [0.000, 0.000] | 5.745 [5.745, 5.745] | 40 |
| toyota | forecast | all | 100 | itransformer[lookback=32] | 0.596 [0.549, 0.644] | 0.610 [0.563, 0.658] | 4.553 [4.414, 4.709] | 4.685 [4.545, 4.841] | 40 |
| toyota | forecast | all | 100 | lgbm | 0.684 [0.596, 0.771] | 0.875 [0.820, 0.924] | 6.222 [5.936, 6.535] | 6.944 [6.657, 7.256] | 40 |
| toyota | forecast | all | 100 | lstm[lookback=128] | 0.599 [0.546, 0.654] | 0.671 [0.620, 0.724] | 3.237 [3.096, 3.386] | 3.478 [3.337, 3.627] | 40 |
| toyota | forecast | all | 100 | transformer[lookback=32] | 0.605 [0.565, 0.648] | 0.636 [0.593, 0.682] | 3.982 [3.868, 4.116] | 4.212 [4.098, 4.346] | 40 |
| toyota | forecast | all | 200 | elasticnet | 0.000 [0.000, 0.000] | 0.928 [0.892, 0.957] | 0.000 [0.000, 0.000] | 8.635 [8.635, 8.635] | 40 |
| toyota | forecast | all | 200 | itransformer[lookback=32] | 0.632 [0.570, 0.694] | 0.646 [0.582, 0.710] | 7.479 [7.129, 7.838] | 7.680 [7.330, 8.039] | 40 |
| toyota | forecast | all | 200 | lgbm | 0.697 [0.621, 0.769] | 0.947 [0.909, 0.979] | 7.941 [7.494, 8.405] | 9.300 [8.852, 9.763] | 40 |
| toyota | forecast | all | 200 | lstm[lookback=128] | 0.690 [0.636, 0.743] | 0.774 [0.728, 0.818] | 3.980 [3.793, 4.189] | 4.426 [4.239, 4.634] | 40 |
| toyota | forecast | all | 200 | transformer[lookback=32] | 0.656 [0.596, 0.716] | 0.696 [0.636, 0.755] | 5.434 [5.255, 5.629] | 5.654 [5.475, 5.848] | 40 |
| toyota | forecast | start_points | 1 | elasticnet | 0.000 [0.000, 0.000] | 0.613 [0.500, 0.725] | 0.000 [0.000, 0.000] | 3.765 [3.765, 3.765] | 40 |
| toyota | forecast | start_points | 1 | itransformer[lookback=32] | 0.761 [0.713, 0.810] | 0.706 [0.656, 0.756] | 3.576 [3.445, 3.714] | 3.241 [3.110, 3.379] | 40 |
| toyota | forecast | start_points | 1 | lgbm | 0.844 [0.769, 0.912] | 0.931 [0.881, 0.975] | 4.651 [4.478, 4.866] | 5.081 [4.908, 5.296] | 40 |
| toyota | forecast | start_points | 1 | lstm[lookback=128] | 0.787 [0.733, 0.839] | 0.855 [0.805, 0.899] | 2.390 [2.247, 2.557] | 2.709 [2.566, 2.876] | 40 |
| toyota | forecast | start_points | 1 | transformer[lookback=32] | 0.681 [0.615, 0.747] | 0.616 [0.549, 0.684] | 3.148 [3.090, 3.214] | 2.907 [2.849, 2.973] | 40 |
| toyota | forecast | start_points | 10 | elasticnet | 0.000 [0.000, 0.000] | 0.606 [0.494, 0.713] | 0.000 [0.000, 0.000] | 3.822 [3.822, 3.822] | 40 |
| toyota | forecast | start_points | 10 | itransformer[lookback=32] | 0.774 [0.733, 0.812] | 0.754 [0.710, 0.796] | 3.408 [3.281, 3.543] | 3.269 [3.142, 3.405] | 40 |
| toyota | forecast | start_points | 10 | lgbm | 0.731 [0.637, 0.825] | 0.900 [0.844, 0.950] | 4.460 [4.286, 4.673] | 4.881 [4.708, 5.094] | 40 |
| toyota | forecast | start_points | 10 | lstm[lookback=128] | 0.578 [0.501, 0.656] | 0.735 [0.667, 0.801] | 1.806 [1.718, 1.904] | 2.256 [2.168, 2.354] | 40 |
| toyota | forecast | start_points | 10 | transformer[lookback=32] | 0.739 [0.688, 0.790] | 0.719 [0.660, 0.778] | 3.317 [3.232, 3.417] | 3.064 [2.979, 3.164] | 40 |
| toyota | forecast | start_points | 50 | elasticnet | 0.000 [0.000, 0.000] | 0.706 [0.613, 0.794] | 0.000 [0.000, 0.000] | 4.441 [4.441, 4.441] | 40 |
| toyota | forecast | start_points | 50 | itransformer[lookback=32] | 0.688 [0.645, 0.731] | 0.664 [0.620, 0.708] | 3.784 [3.659, 3.915] | 3.630 [3.506, 3.762] | 40 |
| toyota | forecast | start_points | 50 | lgbm | 0.706 [0.606, 0.800] | 0.844 [0.775, 0.906] | 4.360 [4.143, 4.628] | 4.774 [4.557, 5.041] | 40 |
| toyota | forecast | start_points | 50 | lstm[lookback=128] | 0.588 [0.520, 0.659] | 0.724 [0.664, 0.784] | 2.054 [1.936, 2.192] | 2.507 [2.389, 2.645] | 40 |
| toyota | forecast | start_points | 50 | transformer[lookback=32] | 0.569 [0.490, 0.650] | 0.585 [0.509, 0.664] | 3.182 [3.118, 3.256] | 3.299 [3.234, 3.373] | 40 |
| toyota | forecast | start_points | 100 | elasticnet | 0.000 [0.000, 0.000] | 0.894 [0.850, 0.931] | 0.000 [0.000, 0.000] | 5.745 [5.745, 5.745] | 40 |
| toyota | forecast | start_points | 100 | itransformer[lookback=32] | 0.583 [0.526, 0.641] | 0.596 [0.540, 0.655] | 4.226 [4.086, 4.370] | 4.358 [4.218, 4.502] | 40 |
| toyota | forecast | start_points | 100 | lgbm | 0.662 [0.562, 0.762] | 0.875 [0.819, 0.925] | 5.496 [5.174, 5.853] | 6.217 [5.895, 6.574] | 40 |
| toyota | forecast | start_points | 100 | lstm[lookback=128] | 0.576 [0.506, 0.649] | 0.660 [0.597, 0.725] | 2.917 [2.771, 3.077] | 3.157 [3.012, 3.318] | 40 |
| toyota | forecast | start_points | 100 | transformer[lookback=32] | 0.561 [0.506, 0.621] | 0.606 [0.547, 0.669] | 3.671 [3.580, 3.772] | 3.901 [3.810, 4.003] | 40 |
| toyota | forecast | start_points | 200 | elasticnet | 0.000 [0.000, 0.000] | 0.950 [0.912, 0.981] | 0.000 [0.000, 0.000] | 8.635 [8.635, 8.635] | 40 |
| toyota | forecast | start_points | 200 | itransformer[lookback=32] | 0.615 [0.536, 0.694] | 0.615 [0.537, 0.695] | 7.439 [7.089, 7.797] | 7.641 [7.290, 7.999] | 40 |
| toyota | forecast | start_points | 200 | lgbm | 0.713 [0.631, 0.794] | 0.944 [0.894, 0.981] | 7.951 [7.524, 8.388] | 9.310 [8.883, 9.746] | 40 |
| toyota | forecast | start_points | 200 | lstm[lookback=128] | 0.689 [0.625, 0.753] | 0.787 [0.734, 0.838] | 3.908 [3.709, 4.124] | 4.354 [4.155, 4.569] | 40 |
| toyota | forecast | start_points | 200 | transformer[lookback=32] | 0.659 [0.594, 0.725] | 0.700 [0.636, 0.764] | 5.355 [5.183, 5.542] | 5.574 [5.402, 5.761] | 40 |
| toyota | rul | all | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.948 [0.907, 0.980] | 0.000 [0.000, 0.000] | 547.048 [547.048, 547.048] | 43 |
| toyota | rul | all | 0 | itransformer[lookback=32] | 0.880 [0.820, 0.926] | 0.962 [0.934, 0.984] | 211.216 [189.353, 236.815] | 298.692 [276.829, 324.291] | 43 |
| toyota | rul | all | 0 | lgbm | 0.835 [0.767, 0.895] | 0.958 [0.921, 0.989] | 299.039 [262.491, 343.136] | 474.614 [438.066, 518.712] | 43 |
| toyota | rul | all | 0 | lstm[lookback=128] | 0.821 [0.750, 0.884] | 0.940 [0.894, 0.976] | 160.048 [143.621, 178.789] | 337.600 [321.172, 356.341] | 43 |
| toyota | rul | all | 0 | transformer[lookback=32] | 0.829 [0.760, 0.890] | 0.953 [0.916, 0.982] | 204.108 [186.913, 224.970] | 378.659 [361.464, 399.521] | 43 |
| toyota | rul | start_points | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.930 [0.878, 0.971] | 0.000 [0.000, 0.000] | 547.048 [547.048, 547.048] | 43 |
| toyota | rul | start_points | 0 | itransformer[lookback=32] | 0.860 [0.790, 0.920] | 0.944 [0.901, 0.979] | 223.533 [196.322, 255.456] | 311.009 [283.798, 342.932] | 43 |
| toyota | rul | start_points | 0 | lgbm | 0.843 [0.762, 0.913] | 0.942 [0.895, 0.988] | 304.732 [255.155, 364.933] | 480.308 [430.731, 540.509] | 43 |
| toyota | rul | start_points | 0 | lstm[lookback=128] | 0.778 [0.695, 0.853] | 0.924 [0.862, 0.973] | 170.561 [149.715, 194.387] | 348.112 [327.267, 371.939] | 43 |
| toyota | rul | start_points | 0 | transformer[lookback=32] | 0.792 [0.708, 0.866] | 0.936 [0.887, 0.976] | 222.273 [199.862, 249.152] | 396.824 [374.413, 423.703] | 43 |
| toyota | rul | all | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.901 [0.843, 0.951] | 0.000 [0.000, 0.000] | 547.048 [547.048, 547.048] | 40 |
| toyota | rul | all | 0 | itransformer[lookback=32] | 0.585 [0.512, 0.656] | 0.731 [0.654, 0.805] | 239.370 [225.820, 253.078] | 326.846 [313.296, 340.554] | 40 |
| toyota | rul | all | 0 | lgbm | 0.826 [0.780, 0.868] | 0.922 [0.875, 0.963] | 640.797 [617.219, 663.668] | 816.372 [792.795, 839.244] | 40 |
| toyota | rul | all | 0 | lstm[lookback=128] | 0.377 [0.314, 0.444] | 0.734 [0.663, 0.804] | 179.244 [167.587, 191.471] | 356.796 [345.138, 369.023] | 40 |
| toyota | rul | all | 0 | transformer[lookback=32] | 0.494 [0.427, 0.562] | 0.764 [0.687, 0.839] | 217.165 [206.955, 227.798] | 391.716 [381.506, 402.349] | 40 |
| toyota | rul | start_points | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.869 [0.787, 0.938] | 0.000 [0.000, 0.000] | 547.048 [547.048, 547.048] | 40 |
| toyota | rul | start_points | 0 | itransformer[lookback=32] | 0.573 [0.464, 0.677] | 0.677 [0.570, 0.780] | 264.383 [249.070, 280.285] | 351.859 [336.546, 367.761] | 40 |
| toyota | rul | start_points | 0 | lgbm | 0.856 [0.787, 0.919] | 0.900 [0.838, 0.956] | 677.888 [647.731, 706.554] | 853.464 [823.306, 882.129] | 40 |
| toyota | rul | start_points | 0 | lstm[lookback=128] | 0.389 [0.303, 0.480] | 0.666 [0.575, 0.755] | 195.208 [180.731, 210.561] | 372.759 [358.282, 388.113] | 40 |
| toyota | rul | start_points | 0 | transformer[lookback=32] | 0.516 [0.421, 0.614] | 0.704 [0.606, 0.799] | 235.320 [222.713, 248.303] | 409.871 [397.265, 422.854] | 40 |
| toyota | soh | all | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.895 [0.845, 0.938] | 0.000 [0.000, 0.000] | 3.703 [3.703, 3.703] | 43 |
| toyota | soh | all | 0 | itransformer[lookback=128] | 0.909 [0.858, 0.950] | 0.925 [0.875, 0.963] | 3.602 [3.492, 3.742] | 3.808 [3.698, 3.947] | 43 |
| toyota | soh | all | 0 | lgbm | 0.898 [0.860, 0.933] | 0.962 [0.934, 0.985] | 4.549 [4.265, 4.884] | 4.902 [4.619, 5.237] | 43 |
| toyota | soh | all | 0 | lstm[lookback=32] | 0.892 [0.842, 0.935] | 0.908 [0.859, 0.950] | 3.905 [3.662, 4.175] | 4.027 [3.784, 4.297] | 43 |
| toyota | soh | all | 0 | transformer[lookback=32] | 0.898 [0.844, 0.946] | 0.919 [0.869, 0.962] | 2.809 [2.574, 3.078] | 3.065 [2.831, 3.334] | 43 |
| toyota | soh | start_points | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.930 [0.878, 0.977] | 0.000 [0.000, 0.000] | 3.703 [3.703, 3.703] | 43 |
| toyota | soh | start_points | 0 | itransformer[lookback=128] | 0.905 [0.838, 0.958] | 0.929 [0.869, 0.977] | 3.353 [3.254, 3.467] | 3.559 [3.460, 3.673] | 43 |
| toyota | soh | start_points | 0 | lgbm | 0.907 [0.849, 0.959] | 0.971 [0.942, 0.994] | 3.607 [3.364, 3.902] | 3.961 [3.718, 4.256] | 43 |
| toyota | soh | start_points | 0 | lstm[lookback=32] | 0.885 [0.827, 0.936] | 0.910 [0.853, 0.958] | 2.551 [2.345, 2.795] | 2.672 [2.466, 2.917] | 43 |
| toyota | soh | start_points | 0 | transformer[lookback=32] | 0.892 [0.828, 0.950] | 0.916 [0.858, 0.967] | 2.231 [2.013, 2.478] | 2.488 [2.270, 2.735] | 43 |
| toyota | soh | all | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.549 [0.460, 0.634] | 0.000 [0.000, 0.000] | 3.703 [3.703, 3.703] | 40 |
| toyota | soh | all | 0 | itransformer[lookback=128] | 0.780 [0.733, 0.819] | 0.814 [0.769, 0.852] | 3.728 [3.680, 3.777] | 3.934 [3.886, 3.983] | 40 |
| toyota | soh | all | 0 | lgbm | 0.729 [0.654, 0.801] | 0.857 [0.802, 0.906] | 5.133 [4.925, 5.392] | 5.486 [5.278, 5.745] | 40 |
| toyota | soh | all | 0 | lstm[lookback=32] | 0.671 [0.609, 0.731] | 0.709 [0.651, 0.765] | 3.250 [3.151, 3.356] | 3.372 [3.272, 3.477] | 40 |
| toyota | soh | all | 0 | transformer[lookback=32] | 0.490 [0.405, 0.576] | 0.546 [0.466, 0.624] | 3.133 [2.967, 3.324] | 3.390 [3.224, 3.581] | 40 |
| toyota | soh | start_points | 0 | elasticnet | 0.000 [0.000, 0.000] | 0.581 [0.456, 0.700] | 0.000 [0.000, 0.000] | 3.703 [3.703, 3.703] | 40 |
| toyota | soh | start_points | 0 | itransformer[lookback=128] | 0.829 [0.772, 0.880] | 0.874 [0.824, 0.918] | 3.418 [3.359, 3.478] | 3.624 [3.564, 3.684] | 40 |
| toyota | soh | start_points | 0 | lgbm | 0.688 [0.581, 0.787] | 0.850 [0.769, 0.925] | 4.220 [4.011, 4.479] | 4.573 [4.364, 4.833] | 40 |
| toyota | soh | start_points | 0 | lstm[lookback=32] | 0.720 [0.645, 0.796] | 0.780 [0.713, 0.846] | 2.780 [2.665, 2.906] | 2.902 [2.787, 3.028] | 40 |
| toyota | soh | start_points | 0 | transformer[lookback=32] | 0.480 [0.369, 0.593] | 0.547 [0.444, 0.652] | 2.390 [2.234, 2.568] | 2.647 [2.490, 2.825] | 40 |

![reliability](figures/field_final_reliability_calce.png)
![reliability](figures/field_final_reliability_nasa.png)
![reliability](figures/field_final_reliability_toyota.png)

## Full tables

<details><summary>calce_forecast (245 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | age_only | 6.873 [4.934, 8.813] |  |  | 4 | 5 | 73b85c3a |
| loco | all | overall | rmse_h1 | elasticnet | 3.562 [1.885, 6.210] |  |  | 4 | 5 | 03fa40ae |
| loco | all | overall | rmse_h1 | itransformer[lookback=32] | 3.684 [2.797, 4.436] |  |  | 4 | 5 | 2307abf0 |
| loco | all | overall | rmse_h1 | lgbm | 4.368 [2.423, 5.559] |  |  | 4 | 5 | 4d728772 |
| loco | all | overall | rmse_h1 | lstm[lookback=128] | 1.674 [1.336, 1.938] |  |  | 4 | 5 | 02033d0f |
| loco | all | overall | rmse_h1 | patchtst[lookback=32] | 7.017 [6.756, 7.378] |  |  | 4 | 5 | 91d56bb1 |
| loco | all | overall | rmse_h1 | transformer[lookback=32] | 2.478 [1.913, 3.307] |  |  | 4 | 5 | e3e3015f |
| loco | all | overall | rmse_h10 | age_only | 6.899 [4.946, 8.851] |  |  | 4 | 5 | 73b85c3a |
| loco | all | overall | rmse_h10 | elasticnet | 3.305 [2.165, 5.183] |  |  | 4 | 5 | 03fa40ae |
| loco | all | overall | rmse_h10 | itransformer[lookback=32] | 3.841 [3.048, 4.586] |  |  | 4 | 5 | 2307abf0 |
| loco | all | overall | rmse_h10 | lgbm | 4.191 [2.694, 5.428] |  |  | 4 | 5 | 4d728772 |
| loco | all | overall | rmse_h10 | lstm[lookback=128] | 1.968 [1.807, 2.177] |  |  | 4 | 5 | 02033d0f |
| loco | all | overall | rmse_h10 | patchtst[lookback=32] | 7.315 [6.969, 7.803] |  |  | 4 | 5 | 91d56bb1 |
| loco | all | overall | rmse_h10 | transformer[lookback=32] | 2.604 [2.238, 3.268] |  |  | 4 | 5 | e3e3015f |
| loco | all | overall | rmse_h100 | age_only | 7.251 [5.239, 9.263] |  |  | 4 | 5 | 73b85c3a |
| loco | all | overall | rmse_h100 | elasticnet | 5.108 [2.463, 9.447] |  |  | 4 | 5 | 03fa40ae |
| loco | all | overall | rmse_h100 | itransformer[lookback=32] | 4.464 [3.770, 5.158] |  |  | 4 | 5 | 2307abf0 |
| loco | all | overall | rmse_h100 | lgbm | 4.753 [3.921, 5.585] |  |  | 4 | 5 | 4d728772 |
| loco | all | overall | rmse_h100 | lstm[lookback=128] | 2.771 [2.408, 3.134] |  |  | 4 | 5 | 02033d0f |
| loco | all | overall | rmse_h100 | patchtst[lookback=32] | 9.592 [8.868, 10.124] |  |  | 4 | 5 | 91d56bb1 |
| loco | all | overall | rmse_h100 | transformer[lookback=32] | 3.009 [2.786, 3.232] |  |  | 4 | 5 | e3e3015f |
| loco | all | overall | rmse_h25 | age_only | 6.974 [5.011, 8.937] |  |  | 4 | 5 | 73b85c3a |
| loco | all | overall | rmse_h25 | elasticnet | 2.895 [2.430, 3.600] |  |  | 4 | 5 | 03fa40ae |
| loco | all | overall | rmse_h25 | itransformer[lookback=32] | 3.974 [3.369, 4.583] |  |  | 4 | 5 | 2307abf0 |
| loco | all | overall | rmse_h25 | lgbm | 4.665 [3.082, 6.116] |  |  | 4 | 5 | 4d728772 |
| loco | all | overall | rmse_h25 | lstm[lookback=128] | 2.438 [2.362, 2.581] |  |  | 4 | 5 | 02033d0f |
| loco | all | overall | rmse_h25 | patchtst[lookback=32] | 7.676 [7.182, 8.290] |  |  | 4 | 5 | 91d56bb1 |
| loco | all | overall | rmse_h25 | transformer[lookback=32] | 2.894 [2.594, 3.320] |  |  | 4 | 5 | e3e3015f |
| loco | all | overall | rmse_h50 | age_only | 7.082 [5.105, 9.059] |  |  | 4 | 5 | 73b85c3a |
| loco | all | overall | rmse_h50 | elasticnet | 2.768 [2.517, 2.963] |  |  | 4 | 5 | 03fa40ae |
| loco | all | overall | rmse_h50 | itransformer[lookback=32] | 3.961 [3.328, 4.594] |  |  | 4 | 5 | 2307abf0 |
| loco | all | overall | rmse_h50 | lgbm | 4.686 [3.351, 5.880] |  |  | 4 | 5 | 4d728772 |
| loco | all | overall | rmse_h50 | lstm[lookback=128] | 2.828 [2.549, 3.266] |  |  | 4 | 5 | 02033d0f |
| loco | all | overall | rmse_h50 | patchtst[lookback=32] | 8.267 [7.736, 8.798] |  |  | 4 | 5 | 91d56bb1 |
| loco | all | overall | rmse_h50 | transformer[lookback=32] | 3.223 [2.935, 3.677] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | fixed:200 | rmse_h1 | age_only | 1.076 [0.402, 1.546] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | fixed:200 | rmse_h1 | elasticnet | 4.001 [2.113, 7.265] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | fixed:200 | rmse_h1 | itransformer[lookback=32] | 1.506 [0.806, 2.206] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | fixed:200 | rmse_h1 | lgbm | 0.277 [0.061, 0.494] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | fixed:200 | rmse_h1 | lstm[lookback=128] | 0.650 [0.275, 1.278] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | fixed:200 | rmse_h1 | patchtst[lookback=32] | 1.759 [1.435, 2.082] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | fixed:200 | rmse_h1 | transformer[lookback=32] | 0.777 [0.615, 0.947] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | fixed:200 | rmse_h10 | age_only | 1.369 [0.863, 1.874] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | fixed:200 | rmse_h10 | elasticnet | 3.030 [1.684, 4.375] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | fixed:200 | rmse_h10 | itransformer[lookback=32] | 1.472 [0.958, 2.092] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | fixed:200 | rmse_h10 | lgbm | 1.026 [0.186, 2.326] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | fixed:200 | rmse_h10 | lstm[lookback=128] | 1.446 [0.559, 2.526] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | fixed:200 | rmse_h10 | patchtst[lookback=32] | 2.109 [1.131, 3.668] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | fixed:200 | rmse_h10 | transformer[lookback=32] | 1.276 [0.464, 2.495] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | fixed:200 | rmse_h100 | age_only | 0.884 [0.100, 1.667] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | fixed:200 | rmse_h100 | elasticnet | 5.673 [0.684, 14.576] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | fixed:200 | rmse_h100 | itransformer[lookback=32] | 1.804 [1.311, 2.611] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | fixed:200 | rmse_h100 | lgbm | 1.153 [0.187, 2.432] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | fixed:200 | rmse_h100 | lstm[lookback=128] | 0.626 [0.482, 0.856] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | fixed:200 | rmse_h100 | patchtst[lookback=32] | 1.929 [0.995, 2.862] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | fixed:200 | rmse_h100 | transformer[lookback=32] | 0.817 [0.711, 0.931] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | fixed:200 | rmse_h25 | age_only | 0.691 [0.275, 1.510] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | fixed:200 | rmse_h25 | elasticnet | 1.894 [0.929, 2.778] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | fixed:200 | rmse_h25 | itransformer[lookback=32] | 1.577 [1.301, 2.006] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | fixed:200 | rmse_h25 | lgbm | 2.152 [1.485, 3.131] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | fixed:200 | rmse_h25 | lstm[lookback=128] | 1.028 [0.574, 1.440] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | fixed:200 | rmse_h25 | patchtst[lookback=32] | 2.241 [1.531, 3.184] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | fixed:200 | rmse_h25 | transformer[lookback=32] | 1.135 [0.879, 1.381] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | fixed:200 | rmse_h50 | age_only | 1.308 [0.404, 2.507] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | fixed:200 | rmse_h50 | elasticnet | 2.880 [1.157, 5.222] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | fixed:200 | rmse_h50 | itransformer[lookback=32] | 1.493 [1.153, 1.864] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | fixed:200 | rmse_h50 | lgbm | 2.020 [0.183, 4.034] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | fixed:200 | rmse_h50 | lstm[lookback=128] | 0.841 [0.216, 2.050] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | fixed:200 | rmse_h50 | patchtst[lookback=32] | 2.103 [1.335, 2.830] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | fixed:200 | rmse_h50 | transformer[lookback=32] | 1.099 [0.463, 1.978] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | fixed:400 | rmse_h1 | age_only | 0.458 [0.115, 0.801] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | fixed:400 | rmse_h1 | elasticnet | 1.843 [0.850, 2.855] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | fixed:400 | rmse_h1 | itransformer[lookback=32] | 1.144 [0.697, 1.941] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | fixed:400 | rmse_h1 | lgbm | 0.807 [0.530, 1.136] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | fixed:400 | rmse_h1 | lstm[lookback=128] | 0.605 [0.484, 0.718] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | fixed:400 | rmse_h1 | patchtst[lookback=32] | 2.966 [1.957, 3.811] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | fixed:400 | rmse_h1 | transformer[lookback=32] | 1.322 [0.889, 1.800] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | fixed:400 | rmse_h10 | age_only | 1.359 [0.948, 1.759] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | fixed:400 | rmse_h10 | elasticnet | 1.629 [0.537, 2.721] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | fixed:400 | rmse_h10 | itransformer[lookback=32] | 1.132 [0.572, 1.892] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | fixed:400 | rmse_h10 | lgbm | 1.258 [0.465, 2.051] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | fixed:400 | rmse_h10 | lstm[lookback=128] | 1.039 [0.365, 1.713] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | fixed:400 | rmse_h10 | patchtst[lookback=32] | 2.903 [2.154, 3.349] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | fixed:400 | rmse_h10 | transformer[lookback=32] | 0.873 [0.306, 1.441] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | fixed:400 | rmse_h100 | age_only | 2.210 [1.190, 3.224] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | fixed:400 | rmse_h100 | elasticnet | 2.785 [1.570, 4.397] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | fixed:400 | rmse_h100 | itransformer[lookback=32] | 2.195 [1.207, 3.253] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | fixed:400 | rmse_h100 | lgbm | 2.380 [1.351, 3.459] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | fixed:400 | rmse_h100 | lstm[lookback=128] | 2.615 [1.235, 3.927] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | fixed:400 | rmse_h100 | patchtst[lookback=32] | 5.386 [2.724, 7.663] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | fixed:400 | rmse_h100 | transformer[lookback=32] | 1.934 [0.481, 3.428] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | fixed:400 | rmse_h25 | age_only | 1.809 [0.866, 2.748] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | fixed:400 | rmse_h25 | elasticnet | 1.998 [0.653, 3.843] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | fixed:400 | rmse_h25 | itransformer[lookback=32] | 1.659 [1.271, 2.025] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | fixed:400 | rmse_h25 | lgbm | 1.451 [0.383, 2.585] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | fixed:400 | rmse_h25 | lstm[lookback=128] | 1.386 [0.366, 2.580] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | fixed:400 | rmse_h25 | patchtst[lookback=32] | 3.595 [3.294, 3.896] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | fixed:400 | rmse_h25 | transformer[lookback=32] | 1.731 [0.898, 2.962] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | fixed:400 | rmse_h50 | age_only | 1.259 [0.017, 2.502] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | fixed:400 | rmse_h50 | elasticnet | 2.353 [0.425, 4.281] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | fixed:400 | rmse_h50 | itransformer[lookback=32] | 1.797 [1.336, 2.691] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | fixed:400 | rmse_h50 | lgbm | 1.233 [0.330, 2.137] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | fixed:400 | rmse_h50 | lstm[lookback=128] | 1.584 [0.591, 2.578] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | fixed:400 | rmse_h50 | patchtst[lookback=32] | 3.858 [2.932, 4.751] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | fixed:400 | rmse_h50 | transformer[lookback=32] | 1.964 [1.040, 2.988] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | frac:0.3 | rmse_h1 | age_only | 0.926 [0.248, 1.629] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | frac:0.3 | rmse_h1 | elasticnet | 4.130 [1.452, 7.632] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer[lookback=32] | 1.823 [0.969, 2.678] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | frac:0.3 | rmse_h1 | lgbm | 3.011 [0.307, 8.002] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | frac:0.3 | rmse_h1 | lstm[lookback=128] | 0.752 [0.363, 1.141] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | frac:0.3 | rmse_h1 | patchtst[lookback=32] | 1.476 [1.032, 1.868] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | frac:0.3 | rmse_h1 | transformer[lookback=32] | 0.750 [0.658, 0.833] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | frac:0.3 | rmse_h10 | age_only | 1.457 [0.758, 2.214] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | frac:0.3 | rmse_h10 | elasticnet | 2.848 [1.207, 4.687] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer[lookback=32] | 1.813 [0.933, 2.692] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | frac:0.3 | rmse_h10 | lgbm | 3.387 [0.951, 7.258] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | frac:0.3 | rmse_h10 | lstm[lookback=128] | 1.246 [0.923, 1.632] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | frac:0.3 | rmse_h10 | patchtst[lookback=32] | 1.667 [1.110, 2.350] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | frac:0.3 | rmse_h10 | transformer[lookback=32] | 1.130 [0.731, 1.577] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | frac:0.3 | rmse_h100 | age_only | 1.232 [0.192, 3.128] |  |  | 3 | 5 | 2c5af0da |
| loco | start_points | frac:0.3 | rmse_h100 | elasticnet | 10.865 [1.778, 28.194] |  |  | 3 | 5 | 81107c86 |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer[lookback=32] | 1.350 [0.913, 2.001] |  |  | 3 | 5 | 5bfbd832 |
| loco | start_points | frac:0.3 | rmse_h100 | lgbm | 2.247 [0.166, 4.301] |  |  | 3 | 5 | 65247683 |
| loco | start_points | frac:0.3 | rmse_h100 | lstm[lookback=128] | 1.119 [0.196, 2.666] |  |  | 3 | 5 | 868e9fd7 |
| loco | start_points | frac:0.3 | rmse_h100 | patchtst[lookback=32] | 2.316 [1.549, 3.301] |  |  | 3 | 5 | f5f035d7 |
| loco | start_points | frac:0.3 | rmse_h100 | transformer[lookback=32] | 1.167 [0.512, 2.470] |  |  | 3 | 5 | c08c2614 |
| loco | start_points | frac:0.3 | rmse_h25 | age_only | 1.516 [0.949, 2.084] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | frac:0.3 | rmse_h25 | elasticnet | 1.329 [0.938, 1.620] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer[lookback=32] | 1.963 [1.033, 2.978] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | frac:0.3 | rmse_h25 | lgbm | 2.795 [0.499, 6.414] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | frac:0.3 | rmse_h25 | lstm[lookback=128] | 1.004 [0.273, 1.735] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | frac:0.3 | rmse_h25 | patchtst[lookback=32] | 1.586 [1.263, 1.807] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | frac:0.3 | rmse_h25 | transformer[lookback=32] | 0.601 [0.397, 0.804] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | frac:0.3 | rmse_h50 | age_only | 0.967 [0.228, 1.707] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | frac:0.3 | rmse_h50 | elasticnet | 2.562 [1.052, 4.072] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer[lookback=32] | 1.271 [0.570, 2.051] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | frac:0.3 | rmse_h50 | lgbm | 3.309 [1.540, 6.237] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | frac:0.3 | rmse_h50 | lstm[lookback=128] | 1.485 [0.498, 2.494] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | frac:0.3 | rmse_h50 | patchtst[lookback=32] | 2.879 [1.656, 4.102] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | frac:0.3 | rmse_h50 | transformer[lookback=32] | 1.658 [1.052, 2.248] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | frac:0.5 | rmse_h1 | age_only | 1.211 [0.265, 2.157] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | frac:0.5 | rmse_h1 | elasticnet | 1.725 [1.039, 2.665] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer[lookback=32] | 1.728 [0.769, 2.686] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | frac:0.5 | rmse_h1 | lgbm | 0.558 [0.121, 0.996] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | frac:0.5 | rmse_h1 | lstm[lookback=128] | 0.822 [0.466, 1.221] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | frac:0.5 | rmse_h1 | patchtst[lookback=32] | 2.641 [1.977, 3.305] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | frac:0.5 | rmse_h1 | transformer[lookback=32] | 0.727 [0.435, 1.019] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | frac:0.5 | rmse_h10 | age_only | 1.391 [0.526, 2.120] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | frac:0.5 | rmse_h10 | elasticnet | 1.227 [0.446, 1.995] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer[lookback=32] | 2.162 [1.258, 3.066] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | frac:0.5 | rmse_h10 | lgbm | 0.763 [0.401, 1.102] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | frac:0.5 | rmse_h10 | lstm[lookback=128] | 1.169 [0.567, 1.772] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | frac:0.5 | rmse_h10 | patchtst[lookback=32] | 2.618 [2.004, 3.483] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | frac:0.5 | rmse_h10 | transformer[lookback=32] | 0.734 [0.421, 1.010] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | frac:0.5 | rmse_h100 | age_only | 0.693 [0.324, 1.014] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | frac:0.5 | rmse_h100 | elasticnet | 1.802 [1.012, 2.425] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer[lookback=32] | 2.192 [1.604, 2.741] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | frac:0.5 | rmse_h100 | lgbm | 0.600 [0.174, 1.026] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | frac:0.5 | rmse_h100 | lstm[lookback=128] | 0.552 [0.412, 0.771] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | frac:0.5 | rmse_h100 | patchtst[lookback=32] | 3.256 [2.399, 4.103] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | frac:0.5 | rmse_h100 | transformer[lookback=32] | 0.717 [0.463, 0.905] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | frac:0.5 | rmse_h25 | age_only | 1.289 [0.456, 2.121] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | frac:0.5 | rmse_h25 | elasticnet | 1.398 [0.982, 1.687] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer[lookback=32] | 1.973 [1.435, 2.511] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | frac:0.5 | rmse_h25 | lgbm | 1.006 [0.438, 1.489] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | frac:0.5 | rmse_h25 | lstm[lookback=128] | 1.052 [0.658, 1.446] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | frac:0.5 | rmse_h25 | patchtst[lookback=32] | 2.810 [2.037, 3.783] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | frac:0.5 | rmse_h25 | transformer[lookback=32] | 0.900 [0.566, 1.234] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | frac:0.5 | rmse_h50 | age_only | 0.798 [0.372, 1.409] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | frac:0.5 | rmse_h50 | elasticnet | 0.452 [0.296, 0.609] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer[lookback=32] | 1.727 [1.394, 2.039] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | frac:0.5 | rmse_h50 | lgbm | 0.483 [0.239, 0.674] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | frac:0.5 | rmse_h50 | lstm[lookback=128] | 0.488 [0.369, 0.698] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | frac:0.5 | rmse_h50 | patchtst[lookback=32] | 2.785 [1.830, 3.753] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | frac:0.5 | rmse_h50 | transformer[lookback=32] | 0.577 [0.314, 0.810] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | frac:0.7 | rmse_h1 | age_only | 0.885 [0.221, 1.568] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | frac:0.7 | rmse_h1 | elasticnet | 1.487 [0.536, 2.438] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer[lookback=32] | 1.126 [0.543, 1.710] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | frac:0.7 | rmse_h1 | lgbm | 1.012 [0.527, 1.571] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | frac:0.7 | rmse_h1 | lstm[lookback=128] | 0.695 [0.512, 0.903] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | frac:0.7 | rmse_h1 | patchtst[lookback=32] | 3.133 [2.072, 4.447] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | frac:0.7 | rmse_h1 | transformer[lookback=32] | 1.329 [1.090, 1.572] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | frac:0.7 | rmse_h10 | age_only | 1.145 [0.642, 1.649] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | frac:0.7 | rmse_h10 | elasticnet | 1.176 [0.458, 1.893] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer[lookback=32] | 1.338 [0.899, 1.789] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | frac:0.7 | rmse_h10 | lgbm | 0.858 [0.615, 1.101] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | frac:0.7 | rmse_h10 | lstm[lookback=128] | 0.724 [0.516, 0.951] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | frac:0.7 | rmse_h10 | patchtst[lookback=32] | 3.131 [2.140, 4.358] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | frac:0.7 | rmse_h10 | transformer[lookback=32] | 0.774 [0.465, 1.101] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | frac:0.7 | rmse_h100 | age_only | 1.701 [0.880, 2.522] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | frac:0.7 | rmse_h100 | elasticnet | 1.948 [1.004, 3.061] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer[lookback=32] | 2.284 [1.692, 2.850] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | frac:0.7 | rmse_h100 | lgbm | 1.733 [1.090, 2.242] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | frac:0.7 | rmse_h100 | lstm[lookback=128] | 2.059 [0.796, 3.352] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | frac:0.7 | rmse_h100 | patchtst[lookback=32] | 4.725 [3.153, 6.125] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | frac:0.7 | rmse_h100 | transformer[lookback=32] | 1.825 [0.995, 3.118] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | frac:0.7 | rmse_h25 | age_only | 1.033 [0.366, 1.588] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | frac:0.7 | rmse_h25 | elasticnet | 1.319 [0.379, 2.259] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer[lookback=32] | 0.980 [0.572, 1.412] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | frac:0.7 | rmse_h25 | lgbm | 0.744 [0.032, 1.456] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | frac:0.7 | rmse_h25 | lstm[lookback=128] | 0.650 [0.340, 1.193] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | frac:0.7 | rmse_h25 | patchtst[lookback=32] | 3.439 [2.374, 4.954] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | frac:0.7 | rmse_h25 | transformer[lookback=32] | 1.261 [0.539, 2.437] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | frac:0.7 | rmse_h50 | age_only | 0.732 [0.254, 1.514] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | frac:0.7 | rmse_h50 | elasticnet | 1.540 [0.319, 2.760] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer[lookback=32] | 1.078 [0.876, 1.414] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | frac:0.7 | rmse_h50 | lgbm | 0.530 [0.087, 1.326] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | frac:0.7 | rmse_h50 | lstm[lookback=128] | 0.812 [0.414, 1.433] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | frac:0.7 | rmse_h50 | patchtst[lookback=32] | 4.056 [2.493, 6.410] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | frac:0.7 | rmse_h50 | transformer[lookback=32] | 1.341 [0.769, 1.913] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | overall | rmse_h1 | age_only | 1.043 [0.445, 1.477] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | overall | rmse_h1 | elasticnet | 3.150 [1.718, 4.801] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | overall | rmse_h1 | itransformer[lookback=32] | 1.663 [1.030, 2.297] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | overall | rmse_h1 | lgbm | 1.764 [0.596, 3.696] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | overall | rmse_h1 | lstm[lookback=128] | 0.801 [0.613, 1.010] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | overall | rmse_h1 | patchtst[lookback=32] | 2.864 [2.548, 3.264] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | overall | rmse_h1 | transformer[lookback=32] | 1.124 [0.967, 1.257] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | overall | rmse_h10 | age_only | 1.447 [1.076, 1.830] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | overall | rmse_h10 | elasticnet | 2.388 [1.787, 2.880] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | overall | rmse_h10 | itransformer[lookback=32] | 1.812 [1.193, 2.345] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | overall | rmse_h10 | lgbm | 1.944 [0.692, 3.413] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | overall | rmse_h10 | lstm[lookback=128] | 1.234 [0.726, 1.742] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | overall | rmse_h10 | patchtst[lookback=32] | 2.946 [2.462, 3.429] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | overall | rmse_h10 | transformer[lookback=32] | 1.071 [0.662, 1.621] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | overall | rmse_h100 | age_only | 1.579 [1.061, 2.289] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | overall | rmse_h100 | elasticnet | 5.406 [1.468, 11.946] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | overall | rmse_h100 | itransformer[lookback=32] | 2.242 [1.911, 2.564] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | overall | rmse_h100 | lgbm | 1.907 [1.290, 2.495] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | overall | rmse_h100 | lstm[lookback=128] | 1.727 [0.964, 2.551] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | overall | rmse_h100 | patchtst[lookback=32] | 4.370 [3.554, 5.598] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | overall | rmse_h100 | transformer[lookback=32] | 1.534 [0.801, 2.435] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | overall | rmse_h25 | age_only | 1.498 [1.215, 1.781] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | overall | rmse_h25 | elasticnet | 1.788 [1.320, 2.536] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | overall | rmse_h25 | itransformer[lookback=32] | 1.925 [1.442, 2.329] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | overall | rmse_h25 | lgbm | 2.079 [1.084, 3.447] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | overall | rmse_h25 | lstm[lookback=128] | 1.234 [0.914, 1.653] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | overall | rmse_h25 | patchtst[lookback=32] | 3.183 [2.555, 3.811] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | overall | rmse_h25 | transformer[lookback=32] | 1.317 [0.914, 1.967] |  |  | 4 | 5 | e3e3015f |
| loco | start_points | overall | rmse_h50 | age_only | 1.134 [0.361, 1.907] |  |  | 4 | 5 | 73b85c3a |
| loco | start_points | overall | rmse_h50 | elasticnet | 2.487 [1.508, 3.253] |  |  | 4 | 5 | 03fa40ae |
| loco | start_points | overall | rmse_h50 | itransformer[lookback=32] | 1.718 [1.527, 1.909] |  |  | 4 | 5 | 2307abf0 |
| loco | start_points | overall | rmse_h50 | lgbm | 2.062 [0.982, 3.551] |  |  | 4 | 5 | 4d728772 |
| loco | start_points | overall | rmse_h50 | lstm[lookback=128] | 1.252 [0.630, 1.875] |  |  | 4 | 5 | 02033d0f |
| loco | start_points | overall | rmse_h50 | patchtst[lookback=32] | 3.678 [2.911, 4.372] |  |  | 4 | 5 | 91d56bb1 |
| loco | start_points | overall | rmse_h50 | transformer[lookback=32] | 1.566 [1.142, 1.990] |  |  | 4 | 5 | e3e3015f |

</details>

<details><summary>calce_rul (119 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rul_bias | age_only | 3.814 [-46.873, 54.500] |  |  | 4 | 5 | 64f14627 |
| loco | all | overall | rul_bias | elasticnet | 32514.563 [-12.358, 97386.689] |  |  | 4 | 5 | ed886871 |
| loco | all | overall | rul_bias | itransformer[lookback=32] | 4.892 [-43.684, 53.467] |  |  | 4 | 5 | d354e3ac |
| loco | all | overall | rul_bias | lgbm | 1.938 [-54.656, 71.547] |  |  | 4 | 5 | 84487083 |
| loco | all | overall | rul_bias | lstm[lookback=128] | -2.788 [-54.120, 48.543] |  |  | 4 | 5 | 077064c2 |
| loco | all | overall | rul_bias | patchtst[lookback=32] | 10.289 [-45.447, 66.025] |  |  | 4 | 5 | c63195d9 |
| loco | all | overall | rul_bias | transformer[lookback=32] | 2.065 [-50.088, 57.994] |  |  | 4 | 5 | e9787753 |
| loco | all | overall | rul_mae | age_only | 50.686 [32.535, 68.837] |  |  | 4 | 5 | 64f14627 |
| loco | all | overall | rul_mae | elasticnet | 32546.551 [50.238, 97401.429] |  |  | 4 | 5 | ed886871 |
| loco | all | overall | rul_mae | itransformer[lookback=32] | 50.621 [30.520, 70.722] |  |  | 4 | 5 | d354e3ac |
| loco | all | overall | rul_mae | lgbm | 65.737 [36.423, 94.973] |  |  | 4 | 5 | 84487083 |
| loco | all | overall | rul_mae | lstm[lookback=128] | 52.452 [38.404, 66.500] |  |  | 4 | 5 | 077064c2 |
| loco | all | overall | rul_mae | patchtst[lookback=32] | 98.347 [91.345, 105.115] |  |  | 4 | 5 | c63195d9 |
| loco | all | overall | rul_mae | transformer[lookback=32] | 53.985 [30.568, 77.583] |  |  | 4 | 5 | e9787753 |
| loco | start_points | fixed:200 | rul_bias | age_only | 2.750 [-49.000, 54.500] |  |  | 4 | 5 | 64f14627 |
| loco | start_points | fixed:200 | rul_bias | elasticnet | 125.211 [-90.945, 342.334] |  |  | 4 | 5 | ed886871 |
| loco | start_points | fixed:200 | rul_bias | itransformer[lookback=32] | 8.957 [-42.243, 62.747] |  |  | 4 | 5 | d354e3ac |
| loco | start_points | fixed:200 | rul_bias | lgbm | -8.939 [-84.460, 87.538] |  |  | 4 | 5 | 84487083 |
| loco | start_points | fixed:200 | rul_bias | lstm[lookback=128] | -11.673 [-66.546, 43.199] |  |  | 4 | 5 | 077064c2 |
| loco | start_points | fixed:200 | rul_bias | patchtst[lookback=32] | 20.835 [-51.490, 122.824] |  |  | 4 | 5 | c63195d9 |
| loco | start_points | fixed:200 | rul_bias | transformer[lookback=32] | 4.976 [-49.133, 60.028] |  |  | 4 | 5 | e9787753 |
| loco | start_points | fixed:200 | rul_mae | age_only | 51.750 [33.000, 70.500] |  |  | 4 | 5 | 64f14627 |
| loco | start_points | fixed:200 | rul_mae | elasticnet | 216.156 [89.421, 387.807] |  |  | 4 | 5 | ed886871 |
| loco | start_points | fixed:200 | rul_mae | itransformer[lookback=32] | 51.200 [25.537, 76.863] |  |  | 4 | 5 | d354e3ac |
| loco | start_points | fixed:200 | rul_mae | lgbm | 76.175 [29.895, 122.454] |  |  | 4 | 5 | 84487083 |
| loco | start_points | fixed:200 | rul_mae | lstm[lookback=128] | 56.924 [38.491, 72.366] |  |  | 4 | 5 | 077064c2 |
| loco | start_points | fixed:200 | rul_mae | patchtst[lookback=32] | 72.627 [24.846, 133.272] |  |  | 4 | 5 | c63195d9 |
| loco | start_points | fixed:200 | rul_mae | transformer[lookback=32] | 54.109 [31.377, 78.494] |  |  | 4 | 5 | e9787753 |
| loco | start_points | fixed:400 | rul_bias | age_only | 2.750 [-49.000, 54.500] |  |  | 4 | 5 | 64f14627 |
| loco | start_points | fixed:400 | rul_bias | elasticnet | 50.610 [-44.326, 145.546] |  |  | 4 | 5 | ed886871 |
| loco | start_points | fixed:400 | rul_bias | itransformer[lookback=32] | -2.040 [-53.984, 51.588] |  |  | 4 | 5 | d354e3ac |
| loco | start_points | fixed:400 | rul_bias | lgbm | 19.527 [-39.692, 89.294] |  |  | 4 | 5 | 84487083 |
| loco | start_points | fixed:400 | rul_bias | lstm[lookback=128] | -5.689 [-60.253, 48.875] |  |  | 4 | 5 | 077064c2 |
| loco | start_points | fixed:400 | rul_bias | patchtst[lookback=32] | 14.566 [-76.637, 74.749] |  |  | 4 | 5 | c63195d9 |
| loco | start_points | fixed:400 | rul_bias | transformer[lookback=32] | 4.986 [-52.293, 62.266] |  |  | 4 | 5 | e9787753 |
| loco | start_points | fixed:400 | rul_mae | age_only | 51.750 [33.000, 70.500] |  |  | 4 | 5 | 64f14627 |
| loco | start_points | fixed:400 | rul_mae | elasticnet | 94.936 [44.326, 163.371] |  |  | 4 | 5 | ed886871 |
| loco | start_points | fixed:400 | rul_mae | itransformer[lookback=32] | 42.447 [11.851, 73.043] |  |  | 4 | 5 | d354e3ac |
| loco | start_points | fixed:400 | rul_mae | lgbm | 59.219 [30.856, 106.754] |  |  | 4 | 5 | 84487083 |
| loco | start_points | fixed:400 | rul_mae | lstm[lookback=128] | 54.564 [37.080, 71.093] |  |  | 4 | 5 | 077064c2 |
| loco | start_points | fixed:400 | rul_mae | patchtst[lookback=32] | 74.039 [45.585, 102.493] |  |  | 4 | 5 | c63195d9 |
| loco | start_points | fixed:400 | rul_mae | transformer[lookback=32] | 57.280 [37.607, 81.898] |  |  | 4 | 5 | e9787753 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | age_only | 0.750 [0.250, 1.000] |  |  | 4 | 5 | 64f14627 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | elasticnet | 0.250 [0.000, 0.750] |  |  | 4 | 5 | ed886871 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | itransformer[lookback=32] | 0.750 [0.400, 1.000] |  |  | 4 | 5 | d354e3ac |
| loco | start_points | frac:0.3 | alpha_lambda_acc | lgbm | 0.500 [0.000, 1.000] |  |  | 4 | 5 | 84487083 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | lstm[lookback=128] | 0.950 [0.850, 1.000] |  |  | 4 | 5 | 077064c2 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | patchtst[lookback=32] | 0.200 [0.000, 0.600] |  |  | 4 | 5 | c63195d9 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | transformer[lookback=32] | 0.750 [0.250, 1.000] |  |  | 4 | 5 | e9787753 |
| loco | start_points | frac:0.3 | rul_bias | age_only | 2.750 [-49.000, 54.500] |  |  | 4 | 5 | 64f14627 |
| loco | start_points | frac:0.3 | rul_bias | elasticnet | 853.850 [-62.745, 2278.948] |  |  | 4 | 5 | ed886871 |
| loco | start_points | frac:0.3 | rul_bias | itransformer[lookback=32] | 2.516 [-55.655, 60.687] |  |  | 4 | 5 | d354e3ac |
| loco | start_points | frac:0.3 | rul_bias | lgbm | -21.035 [-96.318, 63.670] |  |  | 4 | 5 | 84487083 |
| loco | start_points | frac:0.3 | rul_bias | lstm[lookback=128] | -15.889 [-67.930, 36.152] |  |  | 4 | 5 | 077064c2 |
| loco | start_points | frac:0.3 | rul_bias | patchtst[lookback=32] | -104.143 [-173.152, -1.046] |  |  | 4 | 5 | c63195d9 |
| loco | start_points | frac:0.3 | rul_bias | transformer[lookback=32] | 3.788 [-48.004, 59.749] |  |  | 4 | 5 | e9787753 |
| loco | start_points | frac:0.3 | rul_mae | age_only | 51.750 [33.000, 70.500] |  |  | 4 | 5 | 64f14627 |
| loco | start_points | frac:0.3 | rul_mae | elasticnet | 916.594 [62.745, 2310.320] |  |  | 4 | 5 | ed886871 |
| loco | start_points | frac:0.3 | rul_mae | itransformer[lookback=32] | 58.171 [41.355, 74.986] |  |  | 4 | 5 | d354e3ac |
| loco | start_points | frac:0.3 | rul_mae | lgbm | 73.602 [26.426, 116.747] |  |  | 4 | 5 | 84487083 |
| loco | start_points | frac:0.3 | rul_mae | lstm[lookback=128] | 54.838 [32.421, 74.695] |  |  | 4 | 5 | 077064c2 |
| loco | start_points | frac:0.3 | rul_mae | patchtst[lookback=32] | 128.804 [75.028, 173.152] |  |  | 4 | 5 | c63195d9 |
| loco | start_points | frac:0.3 | rul_mae | transformer[lookback=32] | 51.792 [28.058, 78.215] |  |  | 4 | 5 | e9787753 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | age_only | 0.500 [0.000, 1.000] |  |  | 4 | 5 | 64f14627 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | elasticnet | 0.250 [0.000, 0.750] |  |  | 4 | 5 | ed886871 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | itransformer[lookback=32] | 0.600 [0.200, 1.000] |  |  | 4 | 5 | d354e3ac |
| loco | start_points | frac:0.5 | alpha_lambda_acc | lgbm | 0.750 [0.250, 1.000] |  |  | 4 | 5 | 84487083 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | lstm[lookback=128] | 0.450 [0.000, 0.900] |  |  | 4 | 5 | 077064c2 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | patchtst[lookback=32] | 0.200 [0.000, 0.450] |  |  | 4 | 5 | c63195d9 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | transformer[lookback=32] | 0.650 [0.250, 1.000] |  |  | 4 | 5 | e9787753 |
| loco | start_points | frac:0.5 | rul_bias | age_only | 2.750 [-49.000, 54.500] |  |  | 4 | 5 | 64f14627 |
| loco | start_points | frac:0.5 | rul_bias | elasticnet | 40.717 [-45.048, 126.481] |  |  | 4 | 5 | ed886871 |
| loco | start_points | frac:0.5 | rul_bias | itransformer[lookback=32] | 6.455 [-43.708, 60.106] |  |  | 4 | 5 | d354e3ac |
| loco | start_points | frac:0.5 | rul_bias | lgbm | 12.790 [-43.968, 96.747] |  |  | 4 | 5 | 84487083 |
| loco | start_points | frac:0.5 | rul_bias | lstm[lookback=128] | -4.520 [-56.662, 47.622] |  |  | 4 | 5 | 077064c2 |
| loco | start_points | frac:0.5 | rul_bias | patchtst[lookback=32] | 2.151 [-121.294, 135.035] |  |  | 4 | 5 | c63195d9 |
| loco | start_points | frac:0.5 | rul_bias | transformer[lookback=32] | 8.498 [-51.275, 69.645] |  |  | 4 | 5 | e9787753 |
| loco | start_points | frac:0.5 | rul_mae | age_only | 51.750 [33.000, 70.500] |  |  | 4 | 5 | 64f14627 |
| loco | start_points | frac:0.5 | rul_mae | elasticnet | 85.764 [39.160, 141.885] |  |  | 4 | 5 | ed886871 |
| loco | start_points | frac:0.5 | rul_mae | itransformer[lookback=32] | 50.163 [25.897, 74.428] |  |  | 4 | 5 | d354e3ac |
| loco | start_points | frac:0.5 | rul_mae | lgbm | 58.574 [14.410, 117.346] |  |  | 4 | 5 | 84487083 |
| loco | start_points | frac:0.5 | rul_mae | lstm[lookback=128] | 53.059 [35.316, 70.131] |  |  | 4 | 5 | 077064c2 |
| loco | start_points | frac:0.5 | rul_mae | patchtst[lookback=32] | 128.812 [76.144, 188.998] |  |  | 4 | 5 | c63195d9 |
| loco | start_points | frac:0.5 | rul_mae | transformer[lookback=32] | 59.773 [35.188, 92.857] |  |  | 4 | 5 | e9787753 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | age_only | 0.250 [0.000, 0.750] |  |  | 4 | 5 | 64f14627 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | elasticnet | 0.250 [0.000, 0.750] |  |  | 4 | 5 | ed886871 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | itransformer[lookback=32] | 0.350 [0.000, 0.750] |  |  | 4 | 5 | d354e3ac |
| loco | start_points | frac:0.7 | alpha_lambda_acc | lgbm | 0.500 [0.000, 1.000] |  |  | 4 | 5 | 84487083 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | lstm[lookback=128] | 0.250 [0.000, 0.600] |  |  | 4 | 5 | 077064c2 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | patchtst[lookback=32] | 0.150 [0.000, 0.300] |  |  | 4 | 5 | c63195d9 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | transformer[lookback=32] | 0.250 [0.000, 0.750] |  |  | 4 | 5 | e9787753 |
| loco | start_points | frac:0.7 | rul_bias | age_only | 2.750 [-49.000, 54.500] |  |  | 4 | 5 | 64f14627 |
| loco | start_points | frac:0.7 | rul_bias | elasticnet | 63.433 [-33.458, 200.484] |  |  | 4 | 5 | ed886871 |
| loco | start_points | frac:0.7 | rul_bias | itransformer[lookback=32] | 1.349 [-60.884, 58.504] |  |  | 4 | 5 | d354e3ac |
| loco | start_points | frac:0.7 | rul_bias | lgbm | 19.775 [-43.401, 97.709] |  |  | 4 | 5 | 84487083 |
| loco | start_points | frac:0.7 | rul_bias | lstm[lookback=128] | -3.955 [-59.168, 51.257] |  |  | 4 | 5 | 077064c2 |
| loco | start_points | frac:0.7 | rul_bias | patchtst[lookback=32] | -38.656 [-120.513, 76.701] |  |  | 4 | 5 | c63195d9 |
| loco | start_points | frac:0.7 | rul_bias | transformer[lookback=32] | 1.914 [-51.566, 67.462] |  |  | 4 | 5 | e9787753 |
| loco | start_points | frac:0.7 | rul_mae | age_only | 51.750 [33.000, 70.500] |  |  | 4 | 5 | 64f14627 |
| loco | start_points | frac:0.7 | rul_mae | elasticnet | 96.892 [24.789, 216.505] |  |  | 4 | 5 | ed886871 |
| loco | start_points | frac:0.7 | rul_mae | itransformer[lookback=32] | 57.156 [27.414, 86.897] |  |  | 4 | 5 | d354e3ac |
| loco | start_points | frac:0.7 | rul_mae | lgbm | 63.176 [29.263, 114.885] |  |  | 4 | 5 | 84487083 |
| loco | start_points | frac:0.7 | rul_mae | lstm[lookback=128] | 55.212 [37.562, 72.290] |  |  | 4 | 5 | 077064c2 |
| loco | start_points | frac:0.7 | rul_mae | patchtst[lookback=32] | 107.752 [82.583, 132.920] |  |  | 4 | 5 | c63195d9 |
| loco | start_points | frac:0.7 | rul_mae | transformer[lookback=32] | 54.136 [21.280, 89.563] |  |  | 4 | 5 | e9787753 |
| loco | start_points | overall | rul_bias | age_only | 2.750 [-49.000, 54.500] |  |  | 4 | 5 | 64f14627 |
| loco | start_points | overall | rul_bias | elasticnet | 226.764 [-55.304, 549.468] |  |  | 4 | 5 | ed886871 |
| loco | start_points | overall | rul_bias | itransformer[lookback=32] | 3.447 [-47.993, 55.724] |  |  | 4 | 5 | d354e3ac |
| loco | start_points | overall | rul_bias | lgbm | 4.424 [-60.690, 86.992] |  |  | 4 | 5 | 84487083 |
| loco | start_points | overall | rul_bias | lstm[lookback=128] | -8.345 [-62.112, 45.421] |  |  | 4 | 5 | 077064c2 |
| loco | start_points | overall | rul_bias | patchtst[lookback=32] | -21.050 [-88.403, 77.231] |  |  | 4 | 5 | c63195d9 |
| loco | start_points | overall | rul_bias | transformer[lookback=32] | 4.833 [-50.454, 61.791] |  |  | 4 | 5 | e9787753 |
| loco | start_points | overall | rul_mae | age_only | 51.750 [33.000, 70.500] |  |  | 4 | 5 | 64f14627 |
| loco | start_points | overall | rul_mae | elasticnet | 282.069 [55.304, 577.120] |  |  | 4 | 5 | ed886871 |
| loco | start_points | overall | rul_mae | itransformer[lookback=32] | 51.827 [26.411, 77.244] |  |  | 4 | 5 | d354e3ac |
| loco | start_points | overall | rul_mae | lgbm | 66.149 [28.321, 109.437] |  |  | 4 | 5 | 84487083 |
| loco | start_points | overall | rul_mae | lstm[lookback=128] | 54.920 [36.941, 71.199] |  |  | 4 | 5 | 077064c2 |
| loco | start_points | overall | rul_mae | patchtst[lookback=32] | 102.407 [86.356, 121.254] |  |  | 4 | 5 | c63195d9 |
| loco | start_points | overall | rul_mae | transformer[lookback=32] | 55.418 [30.120, 85.680] |  |  | 4 | 5 | e9787753 |

</details>

<details><summary>calce_soh (49 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse | age_only | 6.887 [4.966, 8.809] |  |  | 4 | 5 | b6c4b34b |
| loco | all | overall | rmse | elasticnet | 3.603 [2.142, 5.766] |  |  | 4 | 5 | 548a83f2 |
| loco | all | overall | rmse | itransformer[lookback=32] | 3.283 [2.464, 4.057] |  |  | 4 | 5 | 36cc1330 |
| loco | all | overall | rmse | lgbm | 4.146 [2.276, 5.591] |  |  | 4 | 5 | 47c70266 |
| loco | all | overall | rmse | lstm[lookback=32] | 2.066 [1.468, 2.770] |  |  | 4 | 5 | ea07bc2d |
| loco | all | overall | rmse | patchtst[lookback=32] | 8.185 [7.955, 8.421] |  |  | 4 | 5 | a4c8516a |
| loco | all | overall | rmse | transformer[lookback=128] | 2.945 [2.340, 3.932] |  |  | 4 | 5 | a9f5efc8 |
| loco | start_points | fixed:200 | rmse | age_only | 1.381 [0.763, 1.760] |  |  | 4 | 5 | b6c4b34b |
| loco | start_points | fixed:200 | rmse | elasticnet | 2.265 [1.001, 3.529] |  |  | 4 | 5 | 548a83f2 |
| loco | start_points | fixed:200 | rmse | itransformer[lookback=32] | 1.383 [0.832, 1.758] |  |  | 4 | 5 | 36cc1330 |
| loco | start_points | fixed:200 | rmse | lgbm | 0.511 [0.168, 0.853] |  |  | 4 | 5 | 47c70266 |
| loco | start_points | fixed:200 | rmse | lstm[lookback=32] | 1.078 [0.757, 1.452] |  |  | 4 | 5 | ea07bc2d |
| loco | start_points | fixed:200 | rmse | patchtst[lookback=32] | 3.556 [1.374, 5.737] |  |  | 4 | 5 | a4c8516a |
| loco | start_points | fixed:200 | rmse | transformer[lookback=128] | 3.391 [0.978, 7.895] |  |  | 4 | 5 | a9f5efc8 |
| loco | start_points | fixed:400 | rmse | age_only | 0.390 [0.127, 0.727] |  |  | 4 | 5 | b6c4b34b |
| loco | start_points | fixed:400 | rmse | elasticnet | 1.587 [0.582, 3.196] |  |  | 4 | 5 | 548a83f2 |
| loco | start_points | fixed:400 | rmse | itransformer[lookback=32] | 0.645 [0.377, 1.018] |  |  | 4 | 5 | 36cc1330 |
| loco | start_points | fixed:400 | rmse | lgbm | 0.609 [0.406, 0.811] |  |  | 4 | 5 | 47c70266 |
| loco | start_points | fixed:400 | rmse | lstm[lookback=32] | 0.599 [0.335, 0.946] |  |  | 4 | 5 | ea07bc2d |
| loco | start_points | fixed:400 | rmse | patchtst[lookback=32] | 3.319 [1.903, 5.076] |  |  | 4 | 5 | a4c8516a |
| loco | start_points | fixed:400 | rmse | transformer[lookback=128] | 1.339 [0.824, 1.855] |  |  | 4 | 5 | a9f5efc8 |
| loco | start_points | frac:0.3 | rmse | age_only | 1.300 [0.351, 2.471] |  |  | 4 | 5 | b6c4b34b |
| loco | start_points | frac:0.3 | rmse | elasticnet | 3.100 [1.320, 4.627] |  |  | 4 | 5 | 548a83f2 |
| loco | start_points | frac:0.3 | rmse | itransformer[lookback=32] | 1.124 [0.894, 1.483] |  |  | 4 | 5 | 36cc1330 |
| loco | start_points | frac:0.3 | rmse | lgbm | 2.689 [0.694, 5.972] |  |  | 4 | 5 | 47c70266 |
| loco | start_points | frac:0.3 | rmse | lstm[lookback=32] | 0.890 [0.542, 1.406] |  |  | 4 | 5 | ea07bc2d |
| loco | start_points | frac:0.3 | rmse | patchtst[lookback=32] | 2.065 [1.085, 3.045] |  |  | 4 | 5 | a4c8516a |
| loco | start_points | frac:0.3 | rmse | transformer[lookback=128] | 4.058 [0.996, 9.463] |  |  | 4 | 5 | a9f5efc8 |
| loco | start_points | frac:0.5 | rmse | age_only | 1.037 [0.242, 2.422] |  |  | 4 | 5 | b6c4b34b |
| loco | start_points | frac:0.5 | rmse | elasticnet | 2.207 [0.876, 3.577] |  |  | 4 | 5 | 548a83f2 |
| loco | start_points | frac:0.5 | rmse | itransformer[lookback=32] | 1.632 [1.141, 2.139] |  |  | 4 | 5 | 36cc1330 |
| loco | start_points | frac:0.5 | rmse | lgbm | 0.573 [0.114, 1.114] |  |  | 4 | 5 | 47c70266 |
| loco | start_points | frac:0.5 | rmse | lstm[lookback=32] | 0.650 [0.108, 1.526] |  |  | 4 | 5 | ea07bc2d |
| loco | start_points | frac:0.5 | rmse | patchtst[lookback=32] | 4.062 [2.804, 5.320] |  |  | 4 | 5 | a4c8516a |
| loco | start_points | frac:0.5 | rmse | transformer[lookback=128] | 0.808 [0.293, 1.453] |  |  | 4 | 5 | a9f5efc8 |
| loco | start_points | frac:0.7 | rmse | age_only | 0.832 [0.212, 1.534] |  |  | 4 | 5 | b6c4b34b |
| loco | start_points | frac:0.7 | rmse | elasticnet | 1.569 [0.448, 3.027] |  |  | 4 | 5 | 548a83f2 |
| loco | start_points | frac:0.7 | rmse | itransformer[lookback=32] | 1.035 [0.712, 1.452] |  |  | 4 | 5 | 36cc1330 |
| loco | start_points | frac:0.7 | rmse | lgbm | 0.677 [0.388, 0.965] |  |  | 4 | 5 | 47c70266 |
| loco | start_points | frac:0.7 | rmse | lstm[lookback=32] | 0.531 [0.337, 0.688] |  |  | 4 | 5 | ea07bc2d |
| loco | start_points | frac:0.7 | rmse | patchtst[lookback=32] | 5.137 [2.518, 7.755] |  |  | 4 | 5 | a4c8516a |
| loco | start_points | frac:0.7 | rmse | transformer[lookback=128] | 1.288 [1.140, 1.470] |  |  | 4 | 5 | a9f5efc8 |
| loco | start_points | overall | rmse | age_only | 1.172 [0.494, 1.884] |  |  | 4 | 5 | b6c4b34b |
| loco | start_points | overall | rmse | elasticnet | 2.410 [1.258, 3.637] |  |  | 4 | 5 | 548a83f2 |
| loco | start_points | overall | rmse | itransformer[lookback=32] | 1.412 [1.336, 1.488] |  |  | 4 | 5 | 36cc1330 |
| loco | start_points | overall | rmse | lgbm | 1.473 [0.671, 2.785] |  |  | 4 | 5 | 47c70266 |
| loco | start_points | overall | rmse | lstm[lookback=32] | 0.873 [0.665, 1.140] |  |  | 4 | 5 | ea07bc2d |
| loco | start_points | overall | rmse | patchtst[lookback=32] | 4.508 [3.327, 5.688] |  |  | 4 | 5 | a4c8516a |
| loco | start_points | overall | rmse | transformer[lookback=128] | 2.835 [1.245, 5.724] |  |  | 4 | 5 | a9f5efc8 |

</details>

<details><summary>nasa_forecast (245 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse_h1 | age_only | 5.882 [3.514, 8.250] |  | 2.968 | 4 | 5 | c73b7eaf |
| loco | all | overall | rmse_h1 | elasticnet | 2.491 [1.100, 4.051] |  | 4.970 | 4 | 5 | bf90a8cb |
| loco | all | overall | rmse_h1 | itransformer[lookback=64] | 5.829 [4.764, 6.890] |  | 6.097 | 4 | 5 | 40d3fd6c |
| loco | all | overall | rmse_h1 | lgbm | 3.374 [1.630, 6.032] |  | 2.216 | 4 | 5 | abf2d8ec |
| loco | all | overall | rmse_h1 | lstm[lookback=64] | 4.250 [2.865, 5.971] |  | 4.334 | 4 | 5 | ef7822ad |
| loco | all | overall | rmse_h1 | patchtst[lookback=64] | 6.306 [4.860, 8.169] |  | 6.357 | 4 | 5 | 84b85da9 |
| loco | all | overall | rmse_h1 | transformer[lookback=64] | 7.368 [4.927, 9.810] |  | 8.914 | 4 | 5 | 7fb96153 |
| loco | all | overall | rmse_h10 | age_only | 6.044 [3.617, 8.471] |  | 3.057 | 4 | 5 | c73b7eaf |
| loco | all | overall | rmse_h10 | elasticnet | 4.884 [3.352, 5.845] |  | 5.355 | 4 | 5 | bf90a8cb |
| loco | all | overall | rmse_h10 | itransformer[lookback=64] | 5.555 [4.480, 6.876] |  | 5.524 | 4 | 5 | 40d3fd6c |
| loco | all | overall | rmse_h10 | lgbm | 4.370 [2.848, 6.830] |  | 3.190 | 4 | 5 | abf2d8ec |
| loco | all | overall | rmse_h10 | lstm[lookback=64] | 5.837 [3.778, 7.896] |  | 7.221 | 4 | 5 | ef7822ad |
| loco | all | overall | rmse_h10 | patchtst[lookback=64] | 6.447 [5.580, 7.886] |  | 5.999 | 4 | 5 | 84b85da9 |
| loco | all | overall | rmse_h10 | transformer[lookback=64] | 7.119 [5.077, 10.062] |  | 6.731 | 4 | 5 | 7fb96153 |
| loco | all | overall | rmse_h100 | age_only | 6.062 [1.917, 10.208] |  | 1.036 | 4 | 5 | c73b7eaf |
| loco | all | overall | rmse_h100 | elasticnet | 6.869 [2.148, 11.590] |  | 3.319 | 4 | 5 | bf90a8cb |
| loco | all | overall | rmse_h100 | itransformer[lookback=64] | 6.696 [4.251, 9.784] |  | 3.415 | 4 | 5 | 40d3fd6c |
| loco | all | overall | rmse_h100 | lgbm | 6.263 [2.496, 10.030] |  | 2.341 | 4 | 5 | abf2d8ec |
| loco | all | overall | rmse_h100 | lstm[lookback=64] | 6.613 [3.029, 10.719] |  | 3.513 | 4 | 5 | ef7822ad |
| loco | all | overall | rmse_h100 | patchtst[lookback=64] | 5.762 [3.250, 8.859] |  | 2.602 | 4 | 5 | 84b85da9 |
| loco | all | overall | rmse_h100 | transformer[lookback=64] | 6.853 [3.807, 10.955] |  | 4.663 | 4 | 5 | 7fb96153 |
| loco | all | overall | rmse_h25 | age_only | 6.243 [3.643, 8.842] |  | 3.014 | 4 | 5 | c73b7eaf |
| loco | all | overall | rmse_h25 | elasticnet | 4.823 [3.146, 6.820] |  | 4.531 | 4 | 5 | bf90a8cb |
| loco | all | overall | rmse_h25 | itransformer[lookback=64] | 5.470 [4.214, 6.959] |  | 4.550 | 4 | 5 | 40d3fd6c |
| loco | all | overall | rmse_h25 | lgbm | 5.569 [3.507, 8.454] |  | 3.182 | 4 | 5 | abf2d8ec |
| loco | all | overall | rmse_h25 | lstm[lookback=64] | 5.462 [3.715, 7.887] |  | 4.672 | 4 | 5 | ef7822ad |
| loco | all | overall | rmse_h25 | patchtst[lookback=64] | 6.054 [4.580, 7.965] |  | 5.004 | 4 | 5 | 84b85da9 |
| loco | all | overall | rmse_h25 | transformer[lookback=64] | 7.309 [5.000, 9.619] |  | 8.540 | 4 | 5 | 7fb96153 |
| loco | all | overall | rmse_h50 | age_only | 6.281 [3.206, 9.356] |  | 2.381 | 4 | 5 | c73b7eaf |
| loco | all | overall | rmse_h50 | elasticnet | 7.743 [4.087, 11.400] |  | 10.124 | 4 | 5 | bf90a8cb |
| loco | all | overall | rmse_h50 | itransformer[lookback=64] | 5.825 [4.315, 7.475] |  | 4.820 | 4 | 5 | 40d3fd6c |
| loco | all | overall | rmse_h50 | lgbm | 6.471 [3.486, 9.991] |  | 2.541 | 4 | 5 | abf2d8ec |
| loco | all | overall | rmse_h50 | lstm[lookback=64] | 5.621 [3.548, 8.323] |  | 5.175 | 4 | 5 | ef7822ad |
| loco | all | overall | rmse_h50 | patchtst[lookback=64] | 6.157 [4.744, 7.873] |  | 5.600 | 4 | 5 | 84b85da9 |
| loco | all | overall | rmse_h50 | transformer[lookback=64] | 8.469 [6.172, 12.632] |  | 6.639 | 4 | 5 | 7fb96153 |
| loco | start_points | fixed:30 | rmse_h1 | age_only | 4.987 |  | 4.987 | 1 | 5 | c199885d |
| loco | start_points | fixed:30 | rmse_h1 | elasticnet | 4.925 |  | 4.925 | 1 | 5 | bb98bdfc |
| loco | start_points | fixed:30 | rmse_h1 | itransformer[lookback=64] | 2.138 |  | 2.138 | 1 | 5 | a757adae |
| loco | start_points | fixed:30 | rmse_h1 | lgbm | 1.556 |  | 1.556 | 1 | 5 | abe3e4df |
| loco | start_points | fixed:30 | rmse_h1 | lstm[lookback=64] | 2.881 |  | 2.881 | 1 | 5 | 1fff1e34 |
| loco | start_points | fixed:30 | rmse_h1 | patchtst[lookback=64] | 3.848 |  | 3.848 | 1 | 5 | dcba2a14 |
| loco | start_points | fixed:30 | rmse_h1 | transformer[lookback=64] | 3.461 |  | 3.461 | 1 | 5 | 03d8ba8b |
| loco | start_points | fixed:30 | rmse_h10 | age_only | 4.811 [2.930, 6.325] |  | 2.174 | 4 | 5 | c73b7eaf |
| loco | start_points | fixed:30 | rmse_h10 | elasticnet | 4.550 [1.139, 7.961] |  | 0.383 | 4 | 5 | bf90a8cb |
| loco | start_points | fixed:30 | rmse_h10 | itransformer[lookback=64] | 3.292 [2.461, 4.431] |  | 2.246 | 4 | 5 | 40d3fd6c |
| loco | start_points | fixed:30 | rmse_h10 | lgbm | 5.034 [3.881, 6.187] |  | 4.223 | 4 | 5 | abf2d8ec |
| loco | start_points | fixed:30 | rmse_h10 | lstm[lookback=64] | 3.867 [2.842, 5.672] |  | 2.951 | 4 | 5 | ef7822ad |
| loco | start_points | fixed:30 | rmse_h10 | patchtst[lookback=64] | 4.426 [3.314, 5.614] |  | 4.193 | 4 | 5 | 84b85da9 |
| loco | start_points | fixed:30 | rmse_h10 | transformer[lookback=64] | 5.240 [2.834, 7.646] |  | 3.315 | 4 | 5 | 7fb96153 |
| loco | start_points | fixed:30 | rmse_h100 | age_only | 5.055 [1.099, 9.010] |  | 0.413 | 4 | 5 | c73b7eaf |
| loco | start_points | fixed:30 | rmse_h100 | elasticnet | 7.148 [2.998, 11.297] |  | 4.776 | 4 | 5 | bf90a8cb |
| loco | start_points | fixed:30 | rmse_h100 | itransformer[lookback=64] | 5.661 [3.564, 7.758] |  | 3.752 | 4 | 5 | 40d3fd6c |
| loco | start_points | fixed:30 | rmse_h100 | lgbm | 4.934 [0.728, 9.140] |  | 0.681 | 4 | 5 | abf2d8ec |
| loco | start_points | fixed:30 | rmse_h100 | lstm[lookback=64] | 5.076 [1.499, 8.652] |  | 1.824 | 4 | 5 | ef7822ad |
| loco | start_points | fixed:30 | rmse_h100 | patchtst[lookback=64] | 4.167 [2.477, 6.814] |  | 2.164 | 4 | 5 | 84b85da9 |
| loco | start_points | fixed:30 | rmse_h100 | transformer[lookback=64] | 5.595 [2.318, 9.248] |  | 2.849 | 4 | 5 | 7fb96153 |
| loco | start_points | fixed:30 | rmse_h25 | age_only | 5.694 [3.634, 7.913] |  | 2.946 | 4 | 5 | c73b7eaf |
| loco | start_points | fixed:30 | rmse_h25 | elasticnet | 4.733 [3.146, 7.495] |  | 3.034 | 4 | 5 | bf90a8cb |
| loco | start_points | fixed:30 | rmse_h25 | itransformer[lookback=64] | 5.798 [4.100, 7.957] |  | 3.665 | 4 | 5 | 40d3fd6c |
| loco | start_points | fixed:30 | rmse_h25 | lgbm | 5.540 [3.369, 7.710] |  | 2.888 | 4 | 5 | abf2d8ec |
| loco | start_points | fixed:30 | rmse_h25 | lstm[lookback=64] | 5.747 [3.688, 7.925] |  | 2.939 | 4 | 5 | ef7822ad |
| loco | start_points | fixed:30 | rmse_h25 | patchtst[lookback=64] | 4.113 [2.478, 5.889] |  | 3.061 | 4 | 5 | 84b85da9 |
| loco | start_points | fixed:30 | rmse_h25 | transformer[lookback=64] | 6.720 [5.573, 8.625] |  | 5.421 | 4 | 5 | 7fb96153 |
| loco | start_points | fixed:30 | rmse_h50 | age_only | 6.279 [3.955, 8.676] |  | 2.950 | 4 | 5 | c73b7eaf |
| loco | start_points | fixed:30 | rmse_h50 | elasticnet | 7.561 [2.724, 12.398] |  | 11.321 | 4 | 5 | bf90a8cb |
| loco | start_points | fixed:30 | rmse_h50 | itransformer[lookback=64] | 3.505 [1.466, 6.308] |  | 0.891 | 4 | 5 | 40d3fd6c |
| loco | start_points | fixed:30 | rmse_h50 | lgbm | 6.005 [2.290, 8.799] |  | 0.622 | 4 | 5 | abf2d8ec |
| loco | start_points | fixed:30 | rmse_h50 | lstm[lookback=64] | 5.522 [2.601, 8.643] |  | 2.264 | 4 | 5 | ef7822ad |
| loco | start_points | fixed:30 | rmse_h50 | patchtst[lookback=64] | 4.326 [2.814, 5.839] |  | 3.008 | 4 | 5 | 84b85da9 |
| loco | start_points | fixed:30 | rmse_h50 | transformer[lookback=64] | 7.682 [4.632, 12.175] |  | 3.844 | 4 | 5 | 7fb96153 |
| loco | start_points | fixed:50 | rmse_h1 | age_only | 4.494 [2.506, 6.482] |  | 1.777 | 4 | 5 | c73b7eaf |
| loco | start_points | fixed:50 | rmse_h1 | elasticnet | 2.009 [0.961, 3.058] |  | 3.008 | 4 | 5 | bf90a8cb |
| loco | start_points | fixed:50 | rmse_h1 | itransformer[lookback=64] | 5.855 [2.668, 10.500] |  | 13.065 | 4 | 5 | 40d3fd6c |
| loco | start_points | fixed:50 | rmse_h1 | lgbm | 2.196 [0.781, 3.335] |  | 2.048 | 4 | 5 | abf2d8ec |
| loco | start_points | fixed:50 | rmse_h1 | lstm[lookback=64] | 4.328 [3.816, 4.969] |  | 4.375 | 4 | 5 | ef7822ad |
| loco | start_points | fixed:50 | rmse_h1 | patchtst[lookback=64] | 6.910 [4.054, 9.766] |  | 10.092 | 4 | 5 | 84b85da9 |
| loco | start_points | fixed:50 | rmse_h1 | transformer[lookback=64] | 5.717 [4.714, 6.721] |  | 5.115 | 4 | 5 | 7fb96153 |
| loco | start_points | fixed:50 | rmse_h10 | age_only | 5.623 [2.923, 8.323] |  | 1.980 | 4 | 5 | c73b7eaf |
| loco | start_points | fixed:50 | rmse_h10 | elasticnet | 4.393 [1.641, 7.145] |  | 2.232 | 4 | 5 | bf90a8cb |
| loco | start_points | fixed:50 | rmse_h10 | itransformer[lookback=64] | 4.844 [2.776, 7.106] |  | 8.015 | 4 | 5 | 40d3fd6c |
| loco | start_points | fixed:50 | rmse_h10 | lgbm | 4.171 [1.836, 6.633] |  | 1.670 | 4 | 5 | abf2d8ec |
| loco | start_points | fixed:50 | rmse_h10 | lstm[lookback=64] | 4.479 [1.783, 7.693] |  | 4.766 | 4 | 5 | ef7822ad |
| loco | start_points | fixed:50 | rmse_h10 | patchtst[lookback=64] | 5.164 [3.135, 6.975] |  | 6.907 | 4 | 5 | 84b85da9 |
| loco | start_points | fixed:50 | rmse_h10 | transformer[lookback=64] | 5.659 [3.151, 8.521] |  | 3.225 | 4 | 5 | 7fb96153 |
| loco | start_points | fixed:50 | rmse_h100 | age_only | 7.970 [2.295, 12.326] |  |  | 3 | 5 | 8f262774 |
| loco | start_points | fixed:50 | rmse_h100 | elasticnet | 8.291 [0.880, 13.859] |  |  | 3 | 5 | 84aa07d0 |
| loco | start_points | fixed:50 | rmse_h100 | itransformer[lookback=64] | 6.703 [2.707, 11.423] |  |  | 3 | 5 | 4f3d804a |
| loco | start_points | fixed:50 | rmse_h100 | lgbm | 6.730 [0.650, 13.602] |  |  | 3 | 5 | ee523342 |
| loco | start_points | fixed:50 | rmse_h100 | lstm[lookback=64] | 7.284 [2.154, 13.039] |  |  | 3 | 5 | 2c332743 |
| loco | start_points | fixed:50 | rmse_h100 | patchtst[lookback=64] | 5.582 [3.396, 9.095] |  |  | 3 | 5 | e69d12de |
| loco | start_points | fixed:50 | rmse_h100 | transformer[lookback=64] | 7.371 [1.756, 13.644] |  |  | 3 | 5 | bf8e6091 |
| loco | start_points | fixed:50 | rmse_h25 | age_only | 6.235 [3.397, 9.074] |  | 2.197 | 4 | 5 | c73b7eaf |
| loco | start_points | fixed:50 | rmse_h25 | elasticnet | 4.205 [1.253, 7.682] |  | 3.933 | 4 | 5 | bf90a8cb |
| loco | start_points | fixed:50 | rmse_h25 | itransformer[lookback=64] | 5.492 [3.710, 8.842] |  | 10.521 | 4 | 5 | 40d3fd6c |
| loco | start_points | fixed:50 | rmse_h25 | lgbm | 4.466 [1.740, 8.071] |  | 1.656 | 4 | 5 | abf2d8ec |
| loco | start_points | fixed:50 | rmse_h25 | lstm[lookback=64] | 5.155 [2.554, 9.071] |  | 2.677 | 4 | 5 | ef7822ad |
| loco | start_points | fixed:50 | rmse_h25 | patchtst[lookback=64] | 4.708 [2.763, 6.739] |  | 7.594 | 4 | 5 | 84b85da9 |
| loco | start_points | fixed:50 | rmse_h25 | transformer[lookback=64] | 7.062 [4.717, 9.606] |  | 7.875 | 4 | 5 | 7fb96153 |
| loco | start_points | fixed:50 | rmse_h50 | age_only | 6.064 [3.805, 8.322] |  | 3.432 | 4 | 5 | c73b7eaf |
| loco | start_points | fixed:50 | rmse_h50 | elasticnet | 8.305 [4.098, 12.513] |  | 12.902 | 4 | 5 | bf90a8cb |
| loco | start_points | fixed:50 | rmse_h50 | itransformer[lookback=64] | 5.406 [3.874, 8.017] |  | 9.316 | 4 | 5 | 40d3fd6c |
| loco | start_points | fixed:50 | rmse_h50 | lgbm | 4.988 [2.593, 7.669] |  | 2.268 | 4 | 5 | abf2d8ec |
| loco | start_points | fixed:50 | rmse_h50 | lstm[lookback=64] | 5.155 [2.339, 7.248] |  | 6.334 | 4 | 5 | ef7822ad |
| loco | start_points | fixed:50 | rmse_h50 | patchtst[lookback=64] | 3.647 [2.110, 5.663] |  | 6.599 | 4 | 5 | 84b85da9 |
| loco | start_points | fixed:50 | rmse_h50 | transformer[lookback=64] | 8.205 [5.274, 12.526] |  | 7.294 | 4 | 5 | 7fb96153 |
| loco | start_points | frac:0.3 | rmse_h1 | age_only | 5.169 [4.913, 5.426] |  | 4.829 | 4 | 5 | c73b7eaf |
| loco | start_points | frac:0.3 | rmse_h1 | elasticnet | 1.884 [1.063, 3.075] |  | 1.574 | 4 | 5 | bf90a8cb |
| loco | start_points | frac:0.3 | rmse_h1 | itransformer[lookback=64] | 4.891 [3.018, 7.190] |  | 2.461 | 4 | 5 | 40d3fd6c |
| loco | start_points | frac:0.3 | rmse_h1 | lgbm | 2.343 [0.887, 4.070] |  | 2.259 | 4 | 5 | abf2d8ec |
| loco | start_points | frac:0.3 | rmse_h1 | lstm[lookback=64] | 3.875 [2.757, 4.992] |  | 2.788 | 4 | 5 | ef7822ad |
| loco | start_points | frac:0.3 | rmse_h1 | patchtst[lookback=64] | 4.016 [2.453, 5.579] |  | 2.354 | 4 | 5 | 84b85da9 |
| loco | start_points | frac:0.3 | rmse_h1 | transformer[lookback=64] | 4.993 [3.366, 6.620] |  | 3.585 | 4 | 5 | 7fb96153 |
| loco | start_points | frac:0.3 | rmse_h10 | age_only | 5.267 [4.808, 5.727] |  | 5.877 | 4 | 5 | c73b7eaf |
| loco | start_points | frac:0.3 | rmse_h10 | elasticnet | 4.936 [1.525, 8.348] |  | 0.648 | 4 | 5 | bf90a8cb |
| loco | start_points | frac:0.3 | rmse_h10 | itransformer[lookback=64] | 4.649 [2.870, 7.049] |  | 2.451 | 4 | 5 | 40d3fd6c |
| loco | start_points | frac:0.3 | rmse_h10 | lgbm | 4.001 [3.480, 4.657] |  | 3.572 | 4 | 5 | abf2d8ec |
| loco | start_points | frac:0.3 | rmse_h10 | lstm[lookback=64] | 3.547 [2.261, 4.833] |  | 4.497 | 4 | 5 | ef7822ad |
| loco | start_points | frac:0.3 | rmse_h10 | patchtst[lookback=64] | 5.071 [4.342, 5.764] |  | 3.871 | 4 | 5 | 84b85da9 |
| loco | start_points | frac:0.3 | rmse_h10 | transformer[lookback=64] | 5.155 [3.952, 6.357] |  | 3.973 | 4 | 5 | 7fb96153 |
| loco | start_points | frac:0.3 | rmse_h100 | age_only | 5.517 [1.256, 9.777] |  | 0.850 | 4 | 5 | c73b7eaf |
| loco | start_points | frac:0.3 | rmse_h100 | elasticnet | 6.623 [1.960, 11.286] |  | 2.323 | 4 | 5 | bf90a8cb |
| loco | start_points | frac:0.3 | rmse_h100 | itransformer[lookback=64] | 6.065 [3.830, 7.696] |  | 2.723 | 4 | 5 | 40d3fd6c |
| loco | start_points | frac:0.3 | rmse_h100 | lgbm | 5.346 [1.985, 8.708] |  | 3.683 | 4 | 5 | abf2d8ec |
| loco | start_points | frac:0.3 | rmse_h100 | lstm[lookback=64] | 5.628 [2.315, 9.154] |  | 3.388 | 4 | 5 | ef7822ad |
| loco | start_points | frac:0.3 | rmse_h100 | patchtst[lookback=64] | 4.083 [1.947, 6.552] |  | 2.111 | 4 | 5 | 84b85da9 |
| loco | start_points | frac:0.3 | rmse_h100 | transformer[lookback=64] | 6.047 [2.621, 10.063] |  | 3.724 | 4 | 5 | 7fb96153 |
| loco | start_points | frac:0.3 | rmse_h25 | age_only | 4.639 [2.036, 6.498] |  | 0.668 | 4 | 5 | c73b7eaf |
| loco | start_points | frac:0.3 | rmse_h25 | elasticnet | 6.376 [3.906, 8.846] |  | 9.583 | 4 | 5 | bf90a8cb |
| loco | start_points | frac:0.3 | rmse_h25 | itransformer[lookback=64] | 4.101 [3.058, 5.221] |  | 5.848 | 4 | 5 | 40d3fd6c |
| loco | start_points | frac:0.3 | rmse_h25 | lgbm | 5.826 [3.674, 7.979] |  | 8.035 | 4 | 5 | abf2d8ec |
| loco | start_points | frac:0.3 | rmse_h25 | lstm[lookback=64] | 6.084 [4.977, 7.490] |  | 6.076 | 4 | 5 | ef7822ad |
| loco | start_points | frac:0.3 | rmse_h25 | patchtst[lookback=64] | 3.921 [2.506, 5.336] |  | 1.674 | 4 | 5 | 84b85da9 |
| loco | start_points | frac:0.3 | rmse_h25 | transformer[lookback=64] | 5.951 [5.089, 7.230] |  | 4.926 | 4 | 5 | 7fb96153 |
| loco | start_points | frac:0.3 | rmse_h50 | age_only | 5.867 [2.963, 8.766] |  | 1.874 | 4 | 5 | c73b7eaf |
| loco | start_points | frac:0.3 | rmse_h50 | elasticnet | 7.057 [2.793, 11.320] |  | 9.002 | 4 | 5 | bf90a8cb |
| loco | start_points | frac:0.3 | rmse_h50 | itransformer[lookback=64] | 4.169 [2.832, 5.998] |  | 2.450 | 4 | 5 | 40d3fd6c |
| loco | start_points | frac:0.3 | rmse_h50 | lgbm | 5.831 [3.786, 7.188] |  | 2.850 | 4 | 5 | abf2d8ec |
| loco | start_points | frac:0.3 | rmse_h50 | lstm[lookback=64] | 5.921 [3.181, 9.747] |  | 4.732 | 4 | 5 | ef7822ad |
| loco | start_points | frac:0.3 | rmse_h50 | patchtst[lookback=64] | 4.282 [2.917, 5.714] |  | 4.197 | 4 | 5 | 84b85da9 |
| loco | start_points | frac:0.3 | rmse_h50 | transformer[lookback=64] | 7.518 [3.788, 12.777] |  | 2.791 | 4 | 5 | 7fb96153 |
| loco | start_points | frac:0.5 | rmse_h1 | age_only | 4.669 [2.174, 6.141] |  | 2.174 | 3 | 5 | dc4d60ac |
| loco | start_points | frac:0.5 | rmse_h1 | elasticnet | 1.105 [0.715, 1.561] |  | 0.715 | 3 | 5 | 0d847724 |
| loco | start_points | frac:0.5 | rmse_h1 | itransformer[lookback=64] | 4.289 [1.910, 5.878] |  | 1.910 | 3 | 5 | ca74e1cc |
| loco | start_points | frac:0.5 | rmse_h1 | lgbm | 3.051 [0.801, 4.359] |  | 4.359 | 3 | 5 | 93b1dc00 |
| loco | start_points | frac:0.5 | rmse_h1 | lstm[lookback=64] | 3.364 [2.475, 4.169] |  | 4.169 | 3 | 5 | 1a0f1a71 |
| loco | start_points | frac:0.5 | rmse_h1 | patchtst[lookback=64] | 4.636 [3.386, 5.806] |  | 4.716 | 3 | 5 | 6cd1d184 |
| loco | start_points | frac:0.5 | rmse_h1 | transformer[lookback=64] | 4.293 [2.091, 5.768] |  | 5.020 | 3 | 5 | b424f5ae |
| loco | start_points | frac:0.5 | rmse_h10 | age_only | 5.172 [2.822, 6.531] |  | 1.648 | 4 | 5 | c73b7eaf |
| loco | start_points | frac:0.5 | rmse_h10 | elasticnet | 4.649 [2.953, 6.346] |  | 4.012 | 4 | 5 | bf90a8cb |
| loco | start_points | frac:0.5 | rmse_h10 | itransformer[lookback=64] | 3.571 [3.099, 4.226] |  | 3.091 | 4 | 5 | 40d3fd6c |
| loco | start_points | frac:0.5 | rmse_h10 | lgbm | 4.754 [2.155, 6.702] |  | 6.579 | 4 | 5 | abf2d8ec |
| loco | start_points | frac:0.5 | rmse_h10 | lstm[lookback=64] | 2.849 [1.178, 5.232] |  | 2.463 | 4 | 5 | ef7822ad |
| loco | start_points | frac:0.5 | rmse_h10 | patchtst[lookback=64] | 3.891 [2.547, 5.495] |  | 4.117 | 4 | 5 | 84b85da9 |
| loco | start_points | frac:0.5 | rmse_h10 | transformer[lookback=64] | 4.773 [2.956, 6.801] |  | 2.703 | 4 | 5 | 7fb96153 |
| loco | start_points | frac:0.5 | rmse_h100 | age_only | 7.929 [2.802, 10.513] |  |  | 3 | 5 | 8f262774 |
| loco | start_points | frac:0.5 | rmse_h100 | elasticnet | 7.536 [0.571, 12.470] |  |  | 3 | 5 | 84aa07d0 |
| loco | start_points | frac:0.5 | rmse_h100 | itransformer[lookback=64] | 6.455 [2.511, 8.756] |  |  | 3 | 5 | 4f3d804a |
| loco | start_points | frac:0.5 | rmse_h100 | lgbm | 5.390 [0.304, 10.779] |  |  | 3 | 5 | ee523342 |
| loco | start_points | frac:0.5 | rmse_h100 | lstm[lookback=64] | 5.824 [1.328, 10.241] |  |  | 3 | 5 | 2c332743 |
| loco | start_points | frac:0.5 | rmse_h100 | patchtst[lookback=64] | 6.287 [2.891, 8.084] |  |  | 3 | 5 | e69d12de |
| loco | start_points | frac:0.5 | rmse_h100 | transformer[lookback=64] | 6.516 [1.719, 11.381] |  |  | 3 | 5 | bf8e6091 |
| loco | start_points | frac:0.5 | rmse_h25 | age_only | 5.978 [3.673, 8.091] |  | 2.814 | 4 | 5 | c73b7eaf |
| loco | start_points | frac:0.5 | rmse_h25 | elasticnet | 4.255 [1.667, 6.551] |  | 5.361 | 4 | 5 | bf90a8cb |
| loco | start_points | frac:0.5 | rmse_h25 | itransformer[lookback=64] | 4.013 [2.587, 5.027] |  | 1.938 | 4 | 5 | 40d3fd6c |
| loco | start_points | frac:0.5 | rmse_h25 | lgbm | 4.142 [2.402, 5.881] |  | 2.863 | 4 | 5 | abf2d8ec |
| loco | start_points | frac:0.5 | rmse_h25 | lstm[lookback=64] | 4.535 [2.677, 7.332] |  | 3.995 | 4 | 5 | ef7822ad |
| loco | start_points | frac:0.5 | rmse_h25 | patchtst[lookback=64] | 2.467 [1.622, 3.312] |  | 1.350 | 4 | 5 | 84b85da9 |
| loco | start_points | frac:0.5 | rmse_h25 | transformer[lookback=64] | 6.582 [4.913, 8.506] |  | 6.909 | 4 | 5 | 7fb96153 |
| loco | start_points | frac:0.5 | rmse_h50 | age_only | 6.107 [3.807, 8.407] |  | 3.435 | 4 | 5 | c73b7eaf |
| loco | start_points | frac:0.5 | rmse_h50 | elasticnet | 7.805 [3.570, 12.041] |  | 10.607 | 4 | 5 | bf90a8cb |
| loco | start_points | frac:0.5 | rmse_h50 | itransformer[lookback=64] | 4.694 [2.511, 6.878] |  | 2.592 | 4 | 5 | 40d3fd6c |
| loco | start_points | frac:0.5 | rmse_h50 | lgbm | 4.463 [1.564, 7.944] |  | 0.544 | 4 | 5 | abf2d8ec |
| loco | start_points | frac:0.5 | rmse_h50 | lstm[lookback=64] | 5.211 [2.026, 8.711] |  | 6.248 | 4 | 5 | ef7822ad |
| loco | start_points | frac:0.5 | rmse_h50 | patchtst[lookback=64] | 5.156 [3.991, 6.322] |  | 3.784 | 4 | 5 | 84b85da9 |
| loco | start_points | frac:0.5 | rmse_h50 | transformer[lookback=64] | 7.669 [4.915, 12.240] |  | 5.967 | 4 | 5 | 7fb96153 |
| loco | start_points | frac:0.7 | rmse_h1 | age_only | 5.909 [5.473, 6.297] |  |  | 3 | 5 | 8f262774 |
| loco | start_points | frac:0.7 | rmse_h1 | elasticnet | 0.442 [0.038, 0.741] |  |  | 3 | 5 | 84aa07d0 |
| loco | start_points | frac:0.7 | rmse_h1 | itransformer[lookback=64] | 4.327 [3.030, 6.537] |  |  | 3 | 5 | 4f3d804a |
| loco | start_points | frac:0.7 | rmse_h1 | lgbm | 1.553 [0.744, 2.066] |  |  | 3 | 5 | ee523342 |
| loco | start_points | frac:0.7 | rmse_h1 | lstm[lookback=64] | 2.255 [1.045, 4.319] |  |  | 3 | 5 | 2c332743 |
| loco | start_points | frac:0.7 | rmse_h1 | patchtst[lookback=64] | 2.271 [1.075, 4.131] |  |  | 3 | 5 | e69d12de |
| loco | start_points | frac:0.7 | rmse_h1 | transformer[lookback=64] | 3.849 [1.831, 7.083] |  |  | 3 | 5 | bf8e6091 |
| loco | start_points | frac:0.7 | rmse_h10 | age_only | 5.789 [4.030, 7.548] |  | 3.096 | 4 | 5 | c73b7eaf |
| loco | start_points | frac:0.7 | rmse_h10 | elasticnet | 4.544 [2.393, 7.701] |  | 3.904 | 4 | 5 | bf90a8cb |
| loco | start_points | frac:0.7 | rmse_h10 | itransformer[lookback=64] | 4.433 [3.272, 5.681] |  | 6.439 | 4 | 5 | 40d3fd6c |
| loco | start_points | frac:0.7 | rmse_h10 | lgbm | 2.483 [0.731, 4.555] |  | 0.226 | 4 | 5 | abf2d8ec |
| loco | start_points | frac:0.7 | rmse_h10 | lstm[lookback=64] | 4.102 [1.844, 6.359] |  | 5.896 | 4 | 5 | ef7822ad |
| loco | start_points | frac:0.7 | rmse_h10 | patchtst[lookback=64] | 4.872 [2.084, 9.128] |  | 11.469 | 4 | 5 | 84b85da9 |
| loco | start_points | frac:0.7 | rmse_h10 | transformer[lookback=64] | 4.505 [2.704, 6.490] |  | 5.031 | 4 | 5 | 7fb96153 |
| loco | start_points | frac:0.7 | rmse_h100 | age_only | 11.756 |  |  | 1 | 5 | 77d48faf |
| loco | start_points | frac:0.7 | rmse_h100 | elasticnet | 12.848 |  |  | 1 | 5 | 969eec4d |
| loco | start_points | frac:0.7 | rmse_h100 | itransformer[lookback=64] | 9.218 |  |  | 1 | 5 | 11b18716 |
| loco | start_points | frac:0.7 | rmse_h100 | lgbm | 12.544 |  |  | 1 | 5 | 4a1902d9 |
| loco | start_points | frac:0.7 | rmse_h100 | lstm[lookback=64] | 12.539 |  |  | 1 | 5 | 61e1dd67 |
| loco | start_points | frac:0.7 | rmse_h100 | patchtst[lookback=64] | 7.646 |  |  | 1 | 5 | 4b5d0267 |
| loco | start_points | frac:0.7 | rmse_h100 | transformer[lookback=64] | 11.750 |  |  | 1 | 5 | bd1da845 |
| loco | start_points | frac:0.7 | rmse_h25 | age_only | 6.070 [3.563, 8.577] |  | 2.950 | 4 | 5 | c73b7eaf |
| loco | start_points | frac:0.7 | rmse_h25 | elasticnet | 4.331 [2.922, 6.143] |  | 2.682 | 4 | 5 | bf90a8cb |
| loco | start_points | frac:0.7 | rmse_h25 | itransformer[lookback=64] | 5.280 [3.694, 6.694] |  | 4.996 | 4 | 5 | 40d3fd6c |
| loco | start_points | frac:0.7 | rmse_h25 | lgbm | 3.647 [1.180, 6.846] |  | 1.436 | 4 | 5 | abf2d8ec |
| loco | start_points | frac:0.7 | rmse_h25 | lstm[lookback=64] | 4.401 [1.528, 8.631] |  | 2.614 | 4 | 5 | ef7822ad |
| loco | start_points | frac:0.7 | rmse_h25 | patchtst[lookback=64] | 5.448 [2.784, 7.879] |  | 8.503 | 4 | 5 | 84b85da9 |
| loco | start_points | frac:0.7 | rmse_h25 | transformer[lookback=64] | 6.545 [3.087, 10.004] |  | 8.572 | 4 | 5 | 7fb96153 |
| loco | start_points | frac:0.7 | rmse_h50 | age_only | 5.762 [3.131, 8.393] |  | 4.446 | 4 | 5 | c73b7eaf |
| loco | start_points | frac:0.7 | rmse_h50 | elasticnet | 8.409 [5.184, 11.634] |  | 13.095 | 4 | 5 | bf90a8cb |
| loco | start_points | frac:0.7 | rmse_h50 | itransformer[lookback=64] | 4.713 [3.354, 5.874] |  | 6.013 | 4 | 5 | 40d3fd6c |
| loco | start_points | frac:0.7 | rmse_h50 | lgbm | 3.589 [1.589, 5.590] |  | 2.478 | 4 | 5 | abf2d8ec |
| loco | start_points | frac:0.7 | rmse_h50 | lstm[lookback=64] | 4.171 [2.113, 6.229] |  | 6.221 | 4 | 5 | ef7822ad |
| loco | start_points | frac:0.7 | rmse_h50 | patchtst[lookback=64] | 5.262 [2.296, 8.214] |  | 9.528 | 4 | 5 | 84b85da9 |
| loco | start_points | frac:0.7 | rmse_h50 | transformer[lookback=64] | 7.351 [3.569, 10.892] |  | 7.911 | 4 | 5 | 7fb96153 |
| loco | start_points | overall | rmse_h1 | age_only | 5.204 [4.184, 6.009] |  | 3.744 | 4 | 5 | c73b7eaf |
| loco | start_points | overall | rmse_h1 | elasticnet | 1.959 [1.027, 2.892] |  | 3.012 | 4 | 5 | bf90a8cb |
| loco | start_points | overall | rmse_h1 | itransformer[lookback=64] | 5.459 [4.101, 6.816] |  | 6.929 | 4 | 5 | 40d3fd6c |
| loco | start_points | overall | rmse_h1 | lgbm | 2.401 [1.134, 3.360] |  | 2.771 | 4 | 5 | abf2d8ec |
| loco | start_points | overall | rmse_h1 | lstm[lookback=64] | 3.941 [3.236, 4.749] |  | 4.078 | 4 | 5 | ef7822ad |
| loco | start_points | overall | rmse_h1 | patchtst[lookback=64] | 5.383 [4.239, 6.527] |  | 6.264 | 4 | 5 | 84b85da9 |
| loco | start_points | overall | rmse_h1 | transformer[lookback=64] | 5.131 [3.950, 6.303] |  | 4.625 | 4 | 5 | 7fb96153 |
| loco | start_points | overall | rmse_h10 | age_only | 5.482 [4.007, 6.737] |  | 3.331 | 4 | 5 | c73b7eaf |
| loco | start_points | overall | rmse_h10 | elasticnet | 4.883 [2.297, 7.470] |  | 2.716 | 4 | 5 | bf90a8cb |
| loco | start_points | overall | rmse_h10 | itransformer[lookback=64] | 4.822 [4.130, 5.246] |  | 5.312 | 4 | 5 | 40d3fd6c |
| loco | start_points | overall | rmse_h10 | lgbm | 4.416 [3.236, 5.728] |  | 3.917 | 4 | 5 | abf2d8ec |
| loco | start_points | overall | rmse_h10 | lstm[lookback=64] | 4.081 [2.263, 5.960] |  | 4.676 | 4 | 5 | ef7822ad |
| loco | start_points | overall | rmse_h10 | patchtst[lookback=64] | 5.269 [4.017, 6.522] |  | 7.100 | 4 | 5 | 84b85da9 |
| loco | start_points | overall | rmse_h10 | transformer[lookback=64] | 5.408 [3.848, 7.101] |  | 4.205 | 4 | 5 | 7fb96153 |
| loco | start_points | overall | rmse_h100 | age_only | 5.788 [1.426, 10.150] |  | 0.668 | 4 | 5 | c73b7eaf |
| loco | start_points | overall | rmse_h100 | elasticnet | 6.930 [2.445, 11.416] |  | 3.756 | 4 | 5 | bf90a8cb |
| loco | start_points | overall | rmse_h100 | itransformer[lookback=64] | 6.268 [4.397, 8.434] |  | 3.639 | 4 | 5 | 40d3fd6c |
| loco | start_points | overall | rmse_h100 | lgbm | 5.346 [1.598, 9.365] |  | 2.648 | 4 | 5 | abf2d8ec |
| loco | start_points | overall | rmse_h100 | lstm[lookback=64] | 5.691 [2.268, 9.377] |  | 2.855 | 4 | 5 | ef7822ad |
| loco | start_points | overall | rmse_h100 | patchtst[lookback=64] | 5.022 [2.947, 7.438] |  | 2.249 | 4 | 5 | 84b85da9 |
| loco | start_points | overall | rmse_h100 | transformer[lookback=64] | 5.975 [2.562, 9.950] |  | 3.384 | 4 | 5 | 7fb96153 |
| loco | start_points | overall | rmse_h25 | age_only | 5.802 [3.467, 8.061] |  | 2.473 | 4 | 5 | c73b7eaf |
| loco | start_points | overall | rmse_h25 | elasticnet | 5.048 [3.202, 7.153] |  | 5.522 | 4 | 5 | bf90a8cb |
| loco | start_points | overall | rmse_h25 | itransformer[lookback=64] | 5.767 [5.210, 6.348] |  | 6.665 | 4 | 5 | 40d3fd6c |
| loco | start_points | overall | rmse_h25 | lgbm | 5.182 [3.546, 6.818] |  | 4.145 | 4 | 5 | abf2d8ec |
| loco | start_points | overall | rmse_h25 | lstm[lookback=64] | 5.559 [3.990, 8.304] |  | 4.241 | 4 | 5 | ef7822ad |
| loco | start_points | overall | rmse_h25 | patchtst[lookback=64] | 4.887 [4.284, 5.405] |  | 5.598 | 4 | 5 | 84b85da9 |
| loco | start_points | overall | rmse_h25 | transformer[lookback=64] | 6.875 [5.052, 8.863] |  | 7.376 | 4 | 5 | 7fb96153 |
| loco | start_points | overall | rmse_h50 | age_only | 6.121 [3.882, 8.360] |  | 3.333 | 4 | 5 | c73b7eaf |
| loco | start_points | overall | rmse_h50 | elasticnet | 7.935 [3.805, 12.066] |  | 11.486 | 4 | 5 | bf90a8cb |
| loco | start_points | overall | rmse_h50 | itransformer[lookback=64] | 5.255 [4.129, 6.275] |  | 5.452 | 4 | 5 | 40d3fd6c |
| loco | start_points | overall | rmse_h50 | lgbm | 5.234 [2.958, 7.562] |  | 2.004 | 4 | 5 | abf2d8ec |
| loco | start_points | overall | rmse_h50 | lstm[lookback=64] | 5.599 [2.906, 8.495] |  | 5.781 | 4 | 5 | ef7822ad |
| loco | start_points | overall | rmse_h50 | patchtst[lookback=64] | 5.117 [4.356, 5.820] |  | 6.067 | 4 | 5 | 84b85da9 |
| loco | start_points | overall | rmse_h50 | transformer[lookback=64] | 7.938 [5.563, 12.172] |  | 6.033 | 4 | 5 | 7fb96153 |

</details>

<details><summary>nasa_rul (119 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rul_bias | age_only | 2.745 [-31.010, 36.500] |  | 28.000 | 4 | 5 | 8d5ddbd0 |
| loco | all | overall | rul_bias | elasticnet | 515.100 [-19.973, 1479.940] |  | -17.754 | 4 | 5 | 6825caea |
| loco | all | overall | rul_bias | itransformer[lookback=64] | 1.567 [-10.426, 14.790] |  | 2.782 | 4 | 5 | 7437407c |
| loco | all | overall | rul_bias | lgbm | 1.612 [-16.261, 22.354] |  | 5.968 | 4 | 5 | aceee9e9 |
| loco | all | overall | rul_bias | lstm[lookback=64] | 0.957 [-17.573, 23.678] |  | 3.166 | 4 | 5 | dec42eab |
| loco | all | overall | rul_bias | patchtst[lookback=64] | 2.233 [-13.404, 17.763] |  | 4.797 | 4 | 5 | b6c4743e |
| loco | all | overall | rul_bias | transformer[lookback=64] | 1.513 [-22.114, 28.438] |  | 6.403 | 4 | 5 | de016c87 |
| loco | all | overall | rul_mae | age_only | 33.755 [26.091, 41.419] |  | 28.000 | 4 | 5 | 8d5ddbd0 |
| loco | all | overall | rul_mae | elasticnet | 535.263 [20.352, 1489.929] |  | 18.502 | 4 | 5 | 6825caea |
| loco | all | overall | rul_mae | itransformer[lookback=64] | 15.129 [9.880, 20.379] |  | 7.942 | 4 | 5 | 7437407c |
| loco | all | overall | rul_mae | lgbm | 24.255 [18.203, 30.205] |  | 15.302 | 4 | 5 | aceee9e9 |
| loco | all | overall | rul_mae | lstm[lookback=64] | 21.285 [12.364, 30.555] |  | 9.931 | 4 | 5 | dec42eab |
| loco | all | overall | rul_mae | patchtst[lookback=64] | 17.759 [12.524, 22.993] |  | 10.042 | 4 | 5 | b6c4743e |
| loco | all | overall | rul_mae | transformer[lookback=64] | 27.248 [17.767, 38.198] |  | 14.371 | 4 | 5 | de016c87 |
| loco | start_points | fixed:30 | rul_bias | age_only | -0.500 [-37.500, 36.500] |  | 28.000 | 4 | 5 | 8d5ddbd0 |
| loco | start_points | fixed:30 | rul_bias | elasticnet | 849.111 [-29.201, 2501.476] |  | -24.251 | 4 | 5 | 6825caea |
| loco | start_points | fixed:30 | rul_bias | itransformer[lookback=64] | -0.074 [-14.078, 13.017] |  | -3.424 | 4 | 5 | 7437407c |
| loco | start_points | fixed:30 | rul_bias | lgbm | -9.120 [-37.245, 19.005] |  | 3.781 | 4 | 5 | aceee9e9 |
| loco | start_points | fixed:30 | rul_bias | lstm[lookback=64] | -9.546 [-35.709, 22.038] |  | -6.410 | 4 | 5 | dec42eab |
| loco | start_points | fixed:30 | rul_bias | patchtst[lookback=64] | 8.270 [-7.315, 23.781] |  | 2.672 | 4 | 5 | b6c4743e |
| loco | start_points | fixed:30 | rul_bias | transformer[lookback=64] | -11.639 [-44.144, 23.137] |  | -1.413 | 4 | 5 | de016c87 |
| loco | start_points | fixed:30 | rul_mae | age_only | 37.000 [28.000, 46.000] |  | 28.000 | 4 | 5 | 8d5ddbd0 |
| loco | start_points | fixed:30 | rul_mae | elasticnet | 878.312 [29.201, 2516.076] |  | 24.251 | 4 | 5 | 6825caea |
| loco | start_points | fixed:30 | rul_mae | itransformer[lookback=64] | 13.621 [7.203, 20.403] |  | 5.063 | 4 | 5 | 7437407c |
| loco | start_points | fixed:30 | rul_mae | lgbm | 28.125 [11.393, 40.282] |  | 3.781 | 4 | 5 | aceee9e9 |
| loco | start_points | fixed:30 | rul_mae | lstm[lookback=64] | 28.986 [16.594, 41.351] |  | 9.717 | 4 | 5 | dec42eab |
| loco | start_points | fixed:30 | rul_mae | patchtst[lookback=64] | 15.686 [6.221, 26.617] |  | 3.486 | 4 | 5 | b6c4743e |
| loco | start_points | fixed:30 | rul_mae | transformer[lookback=64] | 34.509 [15.738, 47.769] |  | 6.601 | 4 | 5 | de016c87 |
| loco | start_points | fixed:50 | rul_bias | age_only | -0.500 [-37.500, 36.500] |  | 28.000 | 4 | 5 | 8d5ddbd0 |
| loco | start_points | fixed:50 | rul_bias | elasticnet | 967.851 [-17.699, 2902.107] |  | -12.557 | 4 | 5 | 6825caea |
| loco | start_points | fixed:50 | rul_bias | itransformer[lookback=64] | -1.524 [-8.218, 5.171] |  | -8.595 | 4 | 5 | 7437407c |
| loco | start_points | fixed:50 | rul_bias | lgbm | 2.797 [-21.736, 27.330] |  | 16.444 | 4 | 5 | aceee9e9 |
| loco | start_points | fixed:50 | rul_bias | lstm[lookback=64] | 1.249 [-22.505, 27.823] |  | 8.812 | 4 | 5 | dec42eab |
| loco | start_points | fixed:50 | rul_bias | patchtst[lookback=64] | 1.259 [-13.363, 19.656] |  | -10.331 | 4 | 5 | b6c4743e |
| loco | start_points | fixed:50 | rul_bias | transformer[lookback=64] | 1.943 [-27.989, 34.193] |  | 11.783 | 4 | 5 | de016c87 |
| loco | start_points | fixed:50 | rul_mae | age_only | 37.000 [28.000, 46.000] |  | 28.000 | 4 | 5 | 8d5ddbd0 |
| loco | start_points | fixed:50 | rul_mae | elasticnet | 985.550 [17.699, 2910.957] |  | 12.557 | 4 | 5 | 6825caea |
| loco | start_points | fixed:50 | rul_mae | itransformer[lookback=64] | 7.331 [6.096, 8.566] |  | 8.595 | 4 | 5 | 7437407c |
| loco | start_points | fixed:50 | rul_mae | lgbm | 24.533 [14.934, 34.132] |  | 16.444 | 4 | 5 | aceee9e9 |
| loco | start_points | fixed:50 | rul_mae | lstm[lookback=64] | 24.178 [11.397, 36.958] |  | 10.509 | 4 | 5 | dec42eab |
| loco | start_points | fixed:50 | rul_mae | patchtst[lookback=64] | 15.005 [6.828, 24.822] |  | 10.331 | 4 | 5 | b6c4743e |
| loco | start_points | fixed:50 | rul_mae | transformer[lookback=64] | 29.932 [15.456, 44.409] |  | 11.783 | 4 | 5 | de016c87 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | age_only | 0.000 [0.000, 0.000] |  | 0.000 | 4 | 5 | 8d5ddbd0 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | elasticnet | 0.000 [0.000, 0.000] |  | 0.000 | 4 | 5 | 6825caea |
| loco | start_points | frac:0.3 | alpha_lambda_acc | itransformer[lookback=64] | 0.600 [0.200, 0.900] |  | 1.000 | 4 | 5 | 7437407c |
| loco | start_points | frac:0.3 | alpha_lambda_acc | lgbm | 0.000 [0.000, 0.000] |  | 0.000 | 4 | 5 | aceee9e9 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | lstm[lookback=64] | 0.200 [0.000, 0.600] |  | 0.800 | 4 | 5 | dec42eab |
| loco | start_points | frac:0.3 | alpha_lambda_acc | patchtst[lookback=64] | 0.450 [0.100, 0.850] |  | 0.400 | 4 | 5 | b6c4743e |
| loco | start_points | frac:0.3 | alpha_lambda_acc | transformer[lookback=64] | 0.200 [0.000, 0.600] |  | 0.800 | 4 | 5 | de016c87 |
| loco | start_points | frac:0.3 | rul_bias | age_only | -0.500 [-37.500, 36.500] |  | 28.000 | 4 | 5 | 8d5ddbd0 |
| loco | start_points | frac:0.3 | rul_bias | elasticnet | 907.801 [-23.928, 2636.883] |  | -27.789 | 4 | 5 | 6825caea |
| loco | start_points | frac:0.3 | rul_bias | itransformer[lookback=64] | 7.151 [-8.345, 22.826] |  | 2.474 | 4 | 5 | 7437407c |
| loco | start_points | frac:0.3 | rul_bias | lgbm | -12.210 [-33.597, 15.183] |  | -11.611 | 4 | 5 | aceee9e9 |
| loco | start_points | frac:0.3 | rul_bias | lstm[lookback=64] | -6.305 [-30.727, 22.479] |  | -0.853 | 4 | 5 | dec42eab |
| loco | start_points | frac:0.3 | rul_bias | patchtst[lookback=64] | 11.856 [-3.617, 25.693] |  | 11.553 | 4 | 5 | b6c4743e |
| loco | start_points | frac:0.3 | rul_bias | transformer[lookback=64] | -11.607 [-39.980, 18.676] |  | -2.956 | 4 | 5 | de016c87 |
| loco | start_points | frac:0.3 | rul_mae | age_only | 37.000 [28.000, 46.000] |  | 28.000 | 4 | 5 | 8d5ddbd0 |
| loco | start_points | frac:0.3 | rul_mae | elasticnet | 931.729 [23.928, 2648.847] |  | 27.789 | 4 | 5 | 6825caea |
| loco | start_points | frac:0.3 | rul_mae | itransformer[lookback=64] | 15.071 [6.929, 25.075] |  | 4.256 | 4 | 5 | 7437407c |
| loco | start_points | frac:0.3 | rul_mae | lgbm | 27.193 [16.200, 35.811] |  | 11.611 | 4 | 5 | aceee9e9 |
| loco | start_points | frac:0.3 | rul_mae | lstm[lookback=64] | 26.527 [14.458, 38.597] |  | 7.568 | 4 | 5 | dec42eab |
| loco | start_points | frac:0.3 | rul_mae | patchtst[lookback=64] | 16.839 [10.760, 25.693] |  | 11.553 | 4 | 5 | b6c4743e |
| loco | start_points | frac:0.3 | rul_mae | transformer[lookback=64] | 30.586 [13.542, 42.586] |  | 5.893 | 4 | 5 | de016c87 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | age_only | 0.000 [0.000, 0.000] |  | 0.000 | 4 | 5 | 8d5ddbd0 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | elasticnet | 0.000 [0.000, 0.000] |  | 0.000 | 4 | 5 | 6825caea |
| loco | start_points | frac:0.5 | alpha_lambda_acc | itransformer[lookback=64] | 0.400 [0.000, 0.800] |  | 1.000 | 4 | 5 | 7437407c |
| loco | start_points | frac:0.5 | alpha_lambda_acc | lgbm | 0.250 [0.000, 0.750] |  | 1.000 | 4 | 5 | aceee9e9 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | lstm[lookback=64] | 0.400 [0.100, 0.700] |  | 0.800 | 4 | 5 | dec42eab |
| loco | start_points | frac:0.5 | alpha_lambda_acc | patchtst[lookback=64] | 0.150 [0.000, 0.450] |  | 0.600 | 4 | 5 | b6c4743e |
| loco | start_points | frac:0.5 | alpha_lambda_acc | transformer[lookback=64] | 0.150 [0.000, 0.450] |  | 0.600 | 4 | 5 | de016c87 |
| loco | start_points | frac:0.5 | rul_bias | age_only | -0.500 [-37.500, 36.500] |  | 28.000 | 4 | 5 | 8d5ddbd0 |
| loco | start_points | frac:0.5 | rul_bias | elasticnet | 950.273 [-17.932, 2790.582] |  | -21.709 | 4 | 5 | 6825caea |
| loco | start_points | frac:0.5 | rul_bias | itransformer[lookback=64] | -5.136 [-19.637, 8.343] |  | 3.063 | 4 | 5 | 7437407c |
| loco | start_points | frac:0.5 | rul_bias | lgbm | 0.862 [-16.094, 22.863] |  | 1.409 | 4 | 5 | aceee9e9 |
| loco | start_points | frac:0.5 | rul_bias | lstm[lookback=64] | -0.479 [-18.870, 25.662] |  | -7.426 | 4 | 5 | dec42eab |
| loco | start_points | frac:0.5 | rul_bias | patchtst[lookback=64] | -5.618 [-21.662, 10.426] |  | 6.837 | 4 | 5 | b6c4743e |
| loco | start_points | frac:0.5 | rul_bias | transformer[lookback=64] | 1.008 [-21.815, 28.256] |  | 4.513 | 4 | 5 | de016c87 |
| loco | start_points | frac:0.5 | rul_mae | age_only | 37.000 [28.000, 46.000] |  | 28.000 | 4 | 5 | 8d5ddbd0 |
| loco | start_points | frac:0.5 | rul_mae | elasticnet | 968.205 [17.932, 2799.548] |  | 21.709 | 4 | 5 | 6825caea |
| loco | start_points | frac:0.5 | rul_mae | itransformer[lookback=64] | 13.877 [6.896, 22.909] |  | 4.654 | 4 | 5 | 7437407c |
| loco | start_points | frac:0.5 | rul_mae | lgbm | 16.957 [6.296, 28.480] |  | 1.409 | 4 | 5 | aceee9e9 |
| loco | start_points | frac:0.5 | rul_mae | lstm[lookback=64] | 19.092 [8.229, 30.178] |  | 7.426 | 4 | 5 | dec42eab |
| loco | start_points | frac:0.5 | rul_mae | patchtst[lookback=64] | 16.044 [9.791, 22.006] |  | 6.837 | 4 | 5 | b6c4743e |
| loco | start_points | frac:0.5 | rul_mae | transformer[lookback=64] | 23.756 [12.332, 36.465] |  | 8.245 | 4 | 5 | de016c87 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | age_only | 0.000 [0.000, 0.000] |  | 0.000 | 4 | 5 | 8d5ddbd0 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | elasticnet | 0.000 [0.000, 0.000] |  | 0.000 | 4 | 5 | 6825caea |
| loco | start_points | frac:0.7 | alpha_lambda_acc | itransformer[lookback=64] | 0.500 [0.100, 0.900] |  | 0.800 | 4 | 5 | 7437407c |
| loco | start_points | frac:0.7 | alpha_lambda_acc | lgbm | 0.250 [0.000, 0.750] |  | 0.000 | 4 | 5 | aceee9e9 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | lstm[lookback=64] | 0.150 [0.000, 0.300] |  | 0.000 | 4 | 5 | dec42eab |
| loco | start_points | frac:0.7 | alpha_lambda_acc | patchtst[lookback=64] | 0.200 [0.000, 0.400] |  | 0.400 | 4 | 5 | b6c4743e |
| loco | start_points | frac:0.7 | alpha_lambda_acc | transformer[lookback=64] | 0.300 [0.000, 0.750] |  | 0.000 | 4 | 5 | de016c87 |
| loco | start_points | frac:0.7 | rul_bias | age_only | 2.000 [-32.500, 36.500] |  | 28.000 | 4 | 5 | 8d5ddbd0 |
| loco | start_points | frac:0.7 | rul_bias | elasticnet | 394.016 [-10.681, 1159.777] |  | -9.260 | 4 | 5 | 6825caea |
| loco | start_points | frac:0.7 | rul_bias | itransformer[lookback=64] | -0.268 [-9.160, 8.809] |  | 1.995 | 4 | 5 | 7437407c |
| loco | start_points | frac:0.7 | rul_bias | lgbm | 10.931 [-4.280, 25.633] |  | 19.476 | 4 | 5 | aceee9e9 |
| loco | start_points | frac:0.7 | rul_bias | lstm[lookback=64] | 3.838 [-8.429, 16.189] |  | 8.710 | 4 | 5 | dec42eab |
| loco | start_points | frac:0.7 | rul_bias | patchtst[lookback=64] | 0.871 [-14.192, 15.961] |  | -5.693 | 4 | 5 | b6c4743e |
| loco | start_points | frac:0.7 | rul_bias | transformer[lookback=64] | 12.986 [-6.193, 35.978] |  | 15.776 | 4 | 5 | de016c87 |
| loco | start_points | frac:0.7 | rul_mae | age_only | 34.500 [28.000, 41.000] |  | 28.000 | 4 | 5 | 8d5ddbd0 |
| loco | start_points | frac:0.7 | rul_mae | elasticnet | 404.697 [10.681, 1165.117] |  | 9.260 | 4 | 5 | 6825caea |
| loco | start_points | frac:0.7 | rul_mae | itransformer[lookback=64] | 8.095 [3.395, 12.796] |  | 3.219 | 4 | 5 | 7437407c |
| loco | start_points | frac:0.7 | rul_mae | lgbm | 17.031 [8.361, 26.893] |  | 19.476 | 4 | 5 | aceee9e9 |
| loco | start_points | frac:0.7 | rul_mae | lstm[lookback=64] | 13.255 [8.603, 20.285] |  | 10.641 | 4 | 5 | dec42eab |
| loco | start_points | frac:0.7 | rul_mae | patchtst[lookback=64] | 14.534 [6.789, 22.280] |  | 6.197 | 4 | 5 | b6c4743e |
| loco | start_points | frac:0.7 | rul_mae | transformer[lookback=64] | 19.405 [5.724, 39.145] |  | 15.776 | 4 | 5 | de016c87 |
| loco | start_points | overall | rul_bias | age_only | 0.000 [-36.500, 36.500] |  | 28.000 | 4 | 5 | 8d5ddbd0 |
| loco | start_points | overall | rul_bias | elasticnet | 813.810 [-19.888, 2397.401] |  | -19.113 | 4 | 5 | 6825caea |
| loco | start_points | overall | rul_bias | itransformer[lookback=64] | 0.030 [-12.084, 11.055] |  | -0.898 | 4 | 5 | 7437407c |
| loco | start_points | overall | rul_bias | lgbm | -1.348 [-22.489, 21.248] |  | 5.900 | 4 | 5 | aceee9e9 |
| loco | start_points | overall | rul_bias | lstm[lookback=64] | -2.249 [-22.674, 22.838] |  | 0.567 | 4 | 5 | dec42eab |
| loco | start_points | overall | rul_bias | patchtst[lookback=64] | 3.327 [-10.423, 14.835] |  | 1.008 | 4 | 5 | b6c4743e |
| loco | start_points | overall | rul_bias | transformer[lookback=64] | -1.462 [-28.024, 28.048] |  | 5.540 | 4 | 5 | de016c87 |
| loco | start_points | overall | rul_mae | age_only | 36.500 [28.000, 45.000] |  | 28.000 | 4 | 5 | 8d5ddbd0 |
| loco | start_points | overall | rul_mae | elasticnet | 833.699 [19.888, 2407.345] |  | 19.113 | 4 | 5 | 6825caea |
| loco | start_points | overall | rul_mae | itransformer[lookback=64] | 11.599 [6.987, 16.211] |  | 5.157 | 4 | 5 | 7437407c |
| loco | start_points | overall | rul_mae | lgbm | 22.768 [14.238, 31.298] |  | 10.544 | 4 | 5 | aceee9e9 |
| loco | start_points | overall | rul_mae | lstm[lookback=64] | 22.408 [11.982, 32.834] |  | 9.172 | 4 | 5 | dec42eab |
| loco | start_points | overall | rul_mae | patchtst[lookback=64] | 15.622 [10.305, 18.786] |  | 7.681 | 4 | 5 | b6c4743e |
| loco | start_points | overall | rul_mae | transformer[lookback=64] | 27.638 [15.789, 39.487] |  | 9.660 | 4 | 5 | de016c87 |

</details>

<details><summary>nasa_soh (49 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse | age_only | 5.846 [3.492, 8.201] |  | 2.929 | 4 | 5 | b53084f5 |
| loco | all | overall | rmse | elasticnet | 5.418 [2.669, 8.031] |  | 9.019 | 4 | 5 | 0e2331e6 |
| loco | all | overall | rmse | itransformer[lookback=64] | 4.592 [3.263, 5.922] |  | 5.284 | 4 | 5 | a696c19a |
| loco | all | overall | rmse | lgbm | 3.942 [2.615, 6.502] |  | 2.631 | 4 | 5 | 701596ac |
| loco | all | overall | rmse | lstm[lookback=64] | 4.223 [3.262, 5.850] |  | 3.269 | 4 | 5 | 24f86fa7 |
| loco | all | overall | rmse | patchtst[lookback=64] | 6.256 [4.478, 8.210] |  | 6.760 | 4 | 5 | 5f3ce529 |
| loco | all | overall | rmse | transformer[lookback=64] | 7.774 [5.051, 10.559] |  | 11.530 | 4 | 5 | 3b27876b |
| loco | start_points | fixed:30 | rmse | age_only | 4.134 [3.969, 4.299] |  | 4.327 | 4 | 5 | b53084f5 |
| loco | start_points | fixed:30 | rmse | elasticnet | 4.290 [2.014, 6.163] |  | 4.175 | 4 | 5 | 0e2331e6 |
| loco | start_points | fixed:30 | rmse | itransformer[lookback=64] | 2.714 [1.436, 3.924] |  | 2.344 | 4 | 5 | a696c19a |
| loco | start_points | fixed:30 | rmse | lgbm | 3.679 [2.715, 4.435] |  | 2.173 | 4 | 5 | 701596ac |
| loco | start_points | fixed:30 | rmse | lstm[lookback=64] | 3.405 [1.645, 4.683] |  | 0.892 | 4 | 5 | 24f86fa7 |
| loco | start_points | fixed:30 | rmse | patchtst[lookback=64] | 4.731 [3.056, 6.221] |  | 2.042 | 4 | 5 | 5f3ce529 |
| loco | start_points | fixed:30 | rmse | transformer[lookback=64] | 4.990 [3.726, 6.253] |  | 3.899 | 4 | 5 | 3b27876b |
| loco | start_points | fixed:50 | rmse | age_only | 4.566 [3.204, 5.580] |  | 2.579 | 4 | 5 | b53084f5 |
| loco | start_points | fixed:50 | rmse | elasticnet | 5.695 [2.527, 8.369] |  | 8.009 | 4 | 5 | 0e2331e6 |
| loco | start_points | fixed:50 | rmse | itransformer[lookback=64] | 4.533 [2.563, 7.531] |  | 8.902 | 4 | 5 | a696c19a |
| loco | start_points | fixed:50 | rmse | lgbm | 2.844 [1.153, 4.798] |  | 0.473 | 4 | 5 | 701596ac |
| loco | start_points | fixed:50 | rmse | lstm[lookback=64] | 3.392 [2.520, 4.215] |  | 2.089 | 4 | 5 | 24f86fa7 |
| loco | start_points | fixed:50 | rmse | patchtst[lookback=64] | 6.006 [4.678, 7.913] |  | 8.748 | 4 | 5 | 5f3ce529 |
| loco | start_points | fixed:50 | rmse | transformer[lookback=64] | 5.862 [4.656, 7.705] |  | 5.122 | 4 | 5 | 3b27876b |
| loco | start_points | frac:0.3 | rmse | age_only | 5.236 [4.785, 5.687] |  | 4.570 | 4 | 5 | b53084f5 |
| loco | start_points | frac:0.3 | rmse | elasticnet | 5.727 [3.229, 7.695] |  | 7.751 | 4 | 5 | 0e2331e6 |
| loco | start_points | frac:0.3 | rmse | itransformer[lookback=64] | 2.959 [1.706, 4.827] |  | 1.471 | 4 | 5 | a696c19a |
| loco | start_points | frac:0.3 | rmse | lgbm | 4.249 [3.416, 5.269] |  | 3.633 | 4 | 5 | 701596ac |
| loco | start_points | frac:0.3 | rmse | lstm[lookback=64] | 3.636 [1.915, 5.317] |  | 0.885 | 4 | 5 | 24f86fa7 |
| loco | start_points | frac:0.3 | rmse | patchtst[lookback=64] | 2.998 [1.299, 4.597] |  | 0.650 | 4 | 5 | 5f3ce529 |
| loco | start_points | frac:0.3 | rmse | transformer[lookback=64] | 5.860 [3.891, 7.830] |  | 3.723 | 4 | 5 | 3b27876b |
| loco | start_points | frac:0.5 | rmse | age_only | 5.305 [4.473, 5.862] |  | 5.811 | 4 | 5 | b53084f5 |
| loco | start_points | frac:0.5 | rmse | elasticnet | 5.837 [2.264, 8.695] |  | 7.077 | 4 | 5 | 0e2331e6 |
| loco | start_points | frac:0.5 | rmse | itransformer[lookback=64] | 1.815 [1.184, 2.344] |  | 2.207 | 4 | 5 | a696c19a |
| loco | start_points | frac:0.5 | rmse | lgbm | 2.123 [1.012, 3.225] |  | 0.423 | 4 | 5 | 701596ac |
| loco | start_points | frac:0.5 | rmse | lstm[lookback=64] | 3.253 [2.132, 4.430] |  | 1.664 | 4 | 5 | 24f86fa7 |
| loco | start_points | frac:0.5 | rmse | patchtst[lookback=64] | 4.553 [2.753, 6.353] |  | 2.125 | 4 | 5 | 5f3ce529 |
| loco | start_points | frac:0.5 | rmse | transformer[lookback=64] | 5.519 [4.335, 6.743] |  | 4.975 | 4 | 5 | 3b27876b |
| loco | start_points | frac:0.7 | rmse | age_only | 5.452 [3.767, 6.609] |  | 2.946 | 4 | 5 | b53084f5 |
| loco | start_points | frac:0.7 | rmse | elasticnet | 6.086 [3.358, 8.285] |  | 7.460 | 4 | 5 | 0e2331e6 |
| loco | start_points | frac:0.7 | rmse | itransformer[lookback=64] | 3.256 [1.768, 5.538] |  | 6.764 | 4 | 5 | a696c19a |
| loco | start_points | frac:0.7 | rmse | lgbm | 2.063 [0.855, 3.760] |  | 0.576 | 4 | 5 | 701596ac |
| loco | start_points | frac:0.7 | rmse | lstm[lookback=64] | 3.128 [2.204, 4.760] |  | 2.403 | 4 | 5 | 24f86fa7 |
| loco | start_points | frac:0.7 | rmse | patchtst[lookback=64] | 4.924 [1.324, 9.646] |  | 12.338 | 4 | 5 | 5f3ce529 |
| loco | start_points | frac:0.7 | rmse | transformer[lookback=64] | 5.068 [3.493, 6.635] |  | 7.276 | 4 | 5 | 3b27876b |
| loco | start_points | overall | rmse | age_only | 5.033 [4.479, 5.367] |  | 4.212 | 4 | 5 | b53084f5 |
| loco | start_points | overall | rmse | elasticnet | 5.621 [2.732, 7.712] |  | 7.034 | 4 | 5 | 0e2331e6 |
| loco | start_points | overall | rmse | itransformer[lookback=64] | 3.779 [2.940, 4.962] |  | 5.511 | 4 | 5 | a696c19a |
| loco | start_points | overall | rmse | lgbm | 3.259 [2.382, 4.136] |  | 1.932 | 4 | 5 | 701596ac |
| loco | start_points | overall | rmse | lstm[lookback=64] | 3.584 [2.540, 4.607] |  | 1.959 | 4 | 5 | 24f86fa7 |
| loco | start_points | overall | rmse | patchtst[lookback=64] | 5.565 [4.874, 6.559] |  | 6.995 | 4 | 5 | 5f3ce529 |
| loco | start_points | overall | rmse | transformer[lookback=64] | 5.828 [4.622, 6.983] |  | 5.406 | 4 | 5 | 3b27876b |

</details>

<details><summary>toyota_forecast (420 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rmse_h1 | age_only | 4.011 [3.667, 4.476] |  |  | 43 | 5 | 7d094294 |
| test1 | all | overall | rmse_h1 | elasticnet | 1.187 [0.966, 1.467] |  |  | 43 | 5 | 910f2d53 |
| test1 | all | overall | rmse_h1 | itransformer[lookback=32] | 1.120 [0.912, 1.378] |  |  | 43 | 5 | 7ab9b903 |
| test1 | all | overall | rmse_h1 | lgbm | 0.977 [0.781, 1.253] |  |  | 43 | 5 | c867ad3f |
| test1 | all | overall | rmse_h1 | lstm[lookback=128] | 0.807 [0.598, 1.070] |  |  | 43 | 5 | 3bc20cea |
| test1 | all | overall | rmse_h1 | patchtst[lookback=128] | 1.487 [1.285, 1.719] |  |  | 43 | 5 | 1a28f12a |
| test1 | all | overall | rmse_h1 | transformer[lookback=32] | 0.738 [0.562, 0.956] |  |  | 43 | 5 | a3e9d648 |
| test1 | all | overall | rmse_h10 | age_only | 4.046 [3.693, 4.527] |  |  | 43 | 5 | 7d094294 |
| test1 | all | overall | rmse_h10 | elasticnet | 1.205 [0.975, 1.497] |  |  | 43 | 5 | 910f2d53 |
| test1 | all | overall | rmse_h10 | itransformer[lookback=32] | 1.080 [0.867, 1.356] |  |  | 43 | 5 | 7ab9b903 |
| test1 | all | overall | rmse_h10 | lgbm | 0.939 [0.752, 1.209] |  |  | 43 | 5 | c867ad3f |
| test1 | all | overall | rmse_h10 | lstm[lookback=128] | 0.788 [0.566, 1.073] |  |  | 43 | 5 | 3bc20cea |
| test1 | all | overall | rmse_h10 | patchtst[lookback=128] | 1.524 [1.325, 1.747] |  |  | 43 | 5 | 1a28f12a |
| test1 | all | overall | rmse_h10 | transformer[lookback=32] | 0.750 [0.559, 0.995] |  |  | 43 | 5 | a3e9d648 |
| test1 | all | overall | rmse_h100 | age_only | 4.479 [3.990, 5.187] |  |  | 43 | 5 | 7d094294 |
| test1 | all | overall | rmse_h100 | elasticnet | 1.862 [1.421, 2.476] |  |  | 43 | 5 | 910f2d53 |
| test1 | all | overall | rmse_h100 | itransformer[lookback=32] | 1.725 [1.312, 2.311] |  |  | 43 | 5 | 7ab9b903 |
| test1 | all | overall | rmse_h100 | lgbm | 1.162 [0.873, 1.615] |  |  | 43 | 5 | c867ad3f |
| test1 | all | overall | rmse_h100 | lstm[lookback=128] | 1.329 [0.932, 1.904] |  |  | 43 | 5 | 3bc20cea |
| test1 | all | overall | rmse_h100 | patchtst[lookback=128] | 2.222 [1.876, 2.711] |  |  | 43 | 5 | 1a28f12a |
| test1 | all | overall | rmse_h100 | transformer[lookback=32] | 1.337 [0.953, 1.920] |  |  | 43 | 5 | a3e9d648 |
| test1 | all | overall | rmse_h200 | age_only | 4.696 [4.345, 5.133] |  |  | 42 | 5 | 7d094294 |
| test1 | all | overall | rmse_h200 | elasticnet | 2.229 [1.938, 2.574] |  |  | 42 | 5 | 910f2d53 |
| test1 | all | overall | rmse_h200 | itransformer[lookback=32] | 2.570 [2.151, 3.053] |  |  | 42 | 5 | 7ab9b903 |
| test1 | all | overall | rmse_h200 | lgbm | 1.642 [1.409, 1.926] |  |  | 42 | 5 | c867ad3f |
| test1 | all | overall | rmse_h200 | lstm[lookback=128] | 1.646 [1.324, 2.012] |  |  | 42 | 5 | 3bc20cea |
| test1 | all | overall | rmse_h200 | patchtst[lookback=128] | 3.451 [3.163, 3.813] |  |  | 42 | 5 | 1a28f12a |
| test1 | all | overall | rmse_h200 | transformer[lookback=32] | 1.720 [1.381, 2.108] |  |  | 42 | 5 | a3e9d648 |
| test1 | all | overall | rmse_h50 | age_only | 4.219 [3.817, 4.783] |  |  | 43 | 5 | 7d094294 |
| test1 | all | overall | rmse_h50 | elasticnet | 1.418 [1.099, 1.829] |  |  | 43 | 5 | 910f2d53 |
| test1 | all | overall | rmse_h50 | itransformer[lookback=32] | 1.255 [0.976, 1.634] |  |  | 43 | 5 | 7ab9b903 |
| test1 | all | overall | rmse_h50 | lgbm | 0.927 [0.704, 1.263] |  |  | 43 | 5 | c867ad3f |
| test1 | all | overall | rmse_h50 | lstm[lookback=128] | 0.999 [0.699, 1.427] |  |  | 43 | 5 | 3bc20cea |
| test1 | all | overall | rmse_h50 | patchtst[lookback=128] | 1.698 [1.478, 1.958] |  |  | 43 | 5 | 1a28f12a |
| test1 | all | overall | rmse_h50 | transformer[lookback=32] | 1.033 [0.758, 1.432] |  |  | 43 | 5 | a3e9d648 |
| test1 | start_points | fixed:100 | rmse_h1 | age_only | 0.573 [0.287, 1.060] |  |  | 43 | 5 | 7d094294 |
| test1 | start_points | fixed:100 | rmse_h1 | elasticnet | 0.592 [0.412, 0.815] |  |  | 43 | 5 | 910f2d53 |
| test1 | start_points | fixed:100 | rmse_h1 | itransformer[lookback=32] | 0.435 [0.305, 0.624] |  |  | 43 | 5 | 7ab9b903 |
| test1 | start_points | fixed:100 | rmse_h1 | lgbm | 0.362 [0.201, 0.620] |  |  | 43 | 5 | c867ad3f |
| test1 | start_points | fixed:100 | rmse_h1 | lstm[lookback=128] | 0.300 [0.161, 0.540] |  |  | 43 | 5 | 3bc20cea |
| test1 | start_points | fixed:100 | rmse_h1 | patchtst[lookback=128] | 0.713 [0.577, 0.863] |  |  | 43 | 5 | 1a28f12a |
| test1 | start_points | fixed:100 | rmse_h1 | transformer[lookback=32] | 0.365 [0.225, 0.591] |  |  | 43 | 5 | a3e9d648 |
| test1 | start_points | fixed:100 | rmse_h10 | age_only | 0.651 [0.326, 1.206] |  |  | 43 | 5 | 7d094294 |
| test1 | start_points | fixed:100 | rmse_h10 | elasticnet | 0.614 [0.410, 0.878] |  |  | 43 | 5 | 910f2d53 |
| test1 | start_points | fixed:100 | rmse_h10 | itransformer[lookback=32] | 0.490 [0.329, 0.738] |  |  | 43 | 5 | 7ab9b903 |
| test1 | start_points | fixed:100 | rmse_h10 | lgbm | 0.362 [0.188, 0.656] |  |  | 43 | 5 | c867ad3f |
| test1 | start_points | fixed:100 | rmse_h10 | lstm[lookback=128] | 0.330 [0.160, 0.624] |  |  | 43 | 5 | 3bc20cea |
| test1 | start_points | fixed:100 | rmse_h10 | patchtst[lookback=128] | 0.757 [0.607, 0.927] |  |  | 43 | 5 | 1a28f12a |
| test1 | start_points | fixed:100 | rmse_h10 | transformer[lookback=32] | 0.389 [0.222, 0.669] |  |  | 43 | 5 | a3e9d648 |
| test1 | start_points | fixed:100 | rmse_h100 | age_only | 0.880 [0.641, 1.202] |  |  | 42 | 5 | 7d094294 |
| test1 | start_points | fixed:100 | rmse_h100 | elasticnet | 0.787 [0.456, 1.269] |  |  | 42 | 5 | 910f2d53 |
| test1 | start_points | fixed:100 | rmse_h100 | itransformer[lookback=32] | 0.636 [0.457, 0.851] |  |  | 42 | 5 | 7ab9b903 |
| test1 | start_points | fixed:100 | rmse_h100 | lgbm | 0.321 [0.211, 0.461] |  |  | 42 | 5 | c867ad3f |
| test1 | start_points | fixed:100 | rmse_h100 | lstm[lookback=128] | 0.347 [0.220, 0.519] |  |  | 42 | 5 | 3bc20cea |
| test1 | start_points | fixed:100 | rmse_h100 | patchtst[lookback=128] | 1.024 [0.803, 1.280] |  |  | 42 | 5 | 1a28f12a |
| test1 | start_points | fixed:100 | rmse_h100 | transformer[lookback=32] | 0.411 [0.284, 0.588] |  |  | 42 | 5 | a3e9d648 |
| test1 | start_points | fixed:100 | rmse_h200 | age_only | 1.521 [1.076, 2.124] |  |  | 42 | 5 | 7d094294 |
| test1 | start_points | fixed:100 | rmse_h200 | elasticnet | 1.240 [0.760, 1.889] |  |  | 42 | 5 | 910f2d53 |
| test1 | start_points | fixed:100 | rmse_h200 | itransformer[lookback=32] | 1.222 [0.883, 1.643] |  |  | 42 | 5 | 7ab9b903 |
| test1 | start_points | fixed:100 | rmse_h200 | lgbm | 0.546 [0.335, 0.848] |  |  | 42 | 5 | c867ad3f |
| test1 | start_points | fixed:100 | rmse_h200 | lstm[lookback=128] | 0.615 [0.388, 0.944] |  |  | 42 | 5 | 3bc20cea |
| test1 | start_points | fixed:100 | rmse_h200 | patchtst[lookback=128] | 1.406 [1.042, 1.889] |  |  | 42 | 5 | 1a28f12a |
| test1 | start_points | fixed:100 | rmse_h200 | transformer[lookback=32] | 0.685 [0.423, 1.076] |  |  | 42 | 5 | a3e9d648 |
| test1 | start_points | fixed:100 | rmse_h50 | age_only | 1.011 [0.488, 1.911] |  |  | 43 | 5 | 7d094294 |
| test1 | start_points | fixed:100 | rmse_h50 | elasticnet | 0.780 [0.415, 1.286] |  |  | 43 | 5 | 910f2d53 |
| test1 | start_points | fixed:100 | rmse_h50 | itransformer[lookback=32] | 0.691 [0.390, 1.173] |  |  | 43 | 5 | 7ab9b903 |
| test1 | start_points | fixed:100 | rmse_h50 | lgbm | 0.494 [0.196, 1.005] |  |  | 43 | 5 | c867ad3f |
| test1 | start_points | fixed:100 | rmse_h50 | lstm[lookback=128] | 0.523 [0.212, 1.065] |  |  | 43 | 5 | 3bc20cea |
| test1 | start_points | fixed:100 | rmse_h50 | patchtst[lookback=128] | 1.003 [0.755, 1.333] |  |  | 43 | 5 | 1a28f12a |
| test1 | start_points | fixed:100 | rmse_h50 | transformer[lookback=32] | 0.576 [0.261, 1.109] |  |  | 43 | 5 | a3e9d648 |
| test1 | start_points | frac:0.3 | rmse_h1 | age_only | 1.308 [0.898, 1.796] |  |  | 43 | 5 | 7d094294 |
| test1 | start_points | frac:0.3 | rmse_h1 | elasticnet | 0.575 [0.441, 0.719] |  |  | 43 | 5 | 910f2d53 |
| test1 | start_points | frac:0.3 | rmse_h1 | itransformer[lookback=32] | 0.562 [0.447, 0.692] |  |  | 43 | 5 | 7ab9b903 |
| test1 | start_points | frac:0.3 | rmse_h1 | lgbm | 0.248 [0.174, 0.338] |  |  | 43 | 5 | c867ad3f |
| test1 | start_points | frac:0.3 | rmse_h1 | lstm[lookback=128] | 0.268 [0.207, 0.336] |  |  | 43 | 5 | 3bc20cea |
| test1 | start_points | frac:0.3 | rmse_h1 | patchtst[lookback=128] | 0.564 [0.455, 0.693] |  |  | 43 | 5 | 1a28f12a |
| test1 | start_points | frac:0.3 | rmse_h1 | transformer[lookback=32] | 0.311 [0.251, 0.381] |  |  | 43 | 5 | a3e9d648 |
| test1 | start_points | frac:0.3 | rmse_h10 | age_only | 1.373 [0.954, 1.874] |  |  | 43 | 5 | 7d094294 |
| test1 | start_points | frac:0.3 | rmse_h10 | elasticnet | 0.582 [0.446, 0.735] |  |  | 43 | 5 | 910f2d53 |
| test1 | start_points | frac:0.3 | rmse_h10 | itransformer[lookback=32] | 0.594 [0.449, 0.766] |  |  | 43 | 5 | 7ab9b903 |
| test1 | start_points | frac:0.3 | rmse_h10 | lgbm | 0.269 [0.190, 0.363] |  |  | 43 | 5 | c867ad3f |
| test1 | start_points | frac:0.3 | rmse_h10 | lstm[lookback=128] | 0.305 [0.222, 0.402] |  |  | 43 | 5 | 3bc20cea |
| test1 | start_points | frac:0.3 | rmse_h10 | patchtst[lookback=128] | 0.583 [0.468, 0.718] |  |  | 43 | 5 | 1a28f12a |
| test1 | start_points | frac:0.3 | rmse_h10 | transformer[lookback=32] | 0.334 [0.242, 0.444] |  |  | 43 | 5 | a3e9d648 |
| test1 | start_points | frac:0.3 | rmse_h100 | age_only | 2.242 [1.515, 3.168] |  |  | 43 | 5 | 7d094294 |
| test1 | start_points | frac:0.3 | rmse_h100 | elasticnet | 1.132 [0.699, 1.783] |  |  | 43 | 5 | 910f2d53 |
| test1 | start_points | frac:0.3 | rmse_h100 | itransformer[lookback=32] | 1.153 [0.707, 1.818] |  |  | 43 | 5 | 7ab9b903 |
| test1 | start_points | frac:0.3 | rmse_h100 | lgbm | 0.642 [0.307, 1.171] |  |  | 43 | 5 | c867ad3f |
| test1 | start_points | frac:0.3 | rmse_h100 | lstm[lookback=128] | 0.744 [0.365, 1.346] |  |  | 43 | 5 | 3bc20cea |
| test1 | start_points | frac:0.3 | rmse_h100 | patchtst[lookback=128] | 1.292 [0.897, 1.812] |  |  | 43 | 5 | 1a28f12a |
| test1 | start_points | frac:0.3 | rmse_h100 | transformer[lookback=32] | 0.774 [0.372, 1.406] |  |  | 43 | 5 | a3e9d648 |
| test1 | start_points | frac:0.3 | rmse_h200 | age_only | 3.124 [2.380, 3.896] |  |  | 42 | 5 | 7d094294 |
| test1 | start_points | frac:0.3 | rmse_h200 | elasticnet | 1.140 [0.819, 1.561] |  |  | 42 | 5 | 910f2d53 |
| test1 | start_points | frac:0.3 | rmse_h200 | itransformer[lookback=32] | 1.350 [0.930, 1.867] |  |  | 42 | 5 | 7ab9b903 |
| test1 | start_points | frac:0.3 | rmse_h200 | lgbm | 0.606 [0.372, 0.915] |  |  | 42 | 5 | c867ad3f |
| test1 | start_points | frac:0.3 | rmse_h200 | lstm[lookback=128] | 0.736 [0.492, 1.070] |  |  | 42 | 5 | 3bc20cea |
| test1 | start_points | frac:0.3 | rmse_h200 | patchtst[lookback=128] | 1.993 [1.508, 2.524] |  |  | 42 | 5 | 1a28f12a |
| test1 | start_points | frac:0.3 | rmse_h200 | transformer[lookback=32] | 0.868 [0.570, 1.277] |  |  | 42 | 5 | a3e9d648 |
| test1 | start_points | frac:0.3 | rmse_h50 | age_only | 1.731 [1.222, 2.337] |  |  | 43 | 5 | 7d094294 |
| test1 | start_points | frac:0.3 | rmse_h50 | elasticnet | 0.765 [0.537, 1.083] |  |  | 43 | 5 | 910f2d53 |
| test1 | start_points | frac:0.3 | rmse_h50 | itransformer[lookback=32] | 0.791 [0.529, 1.144] |  |  | 43 | 5 | 7ab9b903 |
| test1 | start_points | frac:0.3 | rmse_h50 | lgbm | 0.380 [0.234, 0.574] |  |  | 43 | 5 | c867ad3f |
| test1 | start_points | frac:0.3 | rmse_h50 | lstm[lookback=128] | 0.469 [0.276, 0.749] |  |  | 43 | 5 | 3bc20cea |
| test1 | start_points | frac:0.3 | rmse_h50 | patchtst[lookback=128] | 0.813 [0.641, 1.011] |  |  | 43 | 5 | 1a28f12a |
| test1 | start_points | frac:0.3 | rmse_h50 | transformer[lookback=32] | 0.510 [0.303, 0.815] |  |  | 43 | 5 | a3e9d648 |
| test1 | start_points | frac:0.5 | rmse_h1 | age_only | 2.502 [1.871, 3.167] |  |  | 43 | 5 | 7d094294 |
| test1 | start_points | frac:0.5 | rmse_h1 | elasticnet | 0.898 [0.596, 1.284] |  |  | 43 | 5 | 910f2d53 |
| test1 | start_points | frac:0.5 | rmse_h1 | itransformer[lookback=32] | 0.882 [0.623, 1.180] |  |  | 43 | 5 | 7ab9b903 |
| test1 | start_points | frac:0.5 | rmse_h1 | lgbm | 0.548 [0.352, 0.791] |  |  | 43 | 5 | c867ad3f |
| test1 | start_points | frac:0.5 | rmse_h1 | lstm[lookback=128] | 0.656 [0.429, 0.941] |  |  | 43 | 5 | 3bc20cea |
| test1 | start_points | frac:0.5 | rmse_h1 | patchtst[lookback=128] | 0.842 [0.601, 1.136] |  |  | 43 | 5 | 1a28f12a |
| test1 | start_points | frac:0.5 | rmse_h1 | transformer[lookback=32] | 0.635 [0.424, 0.898] |  |  | 43 | 5 | a3e9d648 |
| test1 | start_points | frac:0.5 | rmse_h10 | age_only | 2.582 [1.924, 3.273] |  |  | 43 | 5 | 7d094294 |
| test1 | start_points | frac:0.5 | rmse_h10 | elasticnet | 0.963 [0.622, 1.404] |  |  | 43 | 5 | 910f2d53 |
| test1 | start_points | frac:0.5 | rmse_h10 | itransformer[lookback=32] | 0.919 [0.629, 1.246] |  |  | 43 | 5 | 7ab9b903 |
| test1 | start_points | frac:0.5 | rmse_h10 | lgbm | 0.593 [0.384, 0.852] |  |  | 43 | 5 | c867ad3f |
| test1 | start_points | frac:0.5 | rmse_h10 | lstm[lookback=128] | 0.722 [0.455, 1.054] |  |  | 43 | 5 | 3bc20cea |
| test1 | start_points | frac:0.5 | rmse_h10 | patchtst[lookback=128] | 0.865 [0.622, 1.161] |  |  | 43 | 5 | 1a28f12a |
| test1 | start_points | frac:0.5 | rmse_h10 | transformer[lookback=32] | 0.641 [0.406, 0.931] |  |  | 43 | 5 | a3e9d648 |
| test1 | start_points | frac:0.5 | rmse_h100 | age_only | 2.987 [2.364, 3.628] |  |  | 42 | 5 | 7d094294 |
| test1 | start_points | frac:0.5 | rmse_h100 | elasticnet | 1.438 [0.997, 2.015] |  |  | 42 | 5 | 910f2d53 |
| test1 | start_points | frac:0.5 | rmse_h100 | itransformer[lookback=32] | 1.409 [1.031, 1.856] |  |  | 42 | 5 | 7ab9b903 |
| test1 | start_points | frac:0.5 | rmse_h100 | lgbm | 0.749 [0.588, 0.930] |  |  | 42 | 5 | c867ad3f |
| test1 | start_points | frac:0.5 | rmse_h100 | lstm[lookback=128] | 0.968 [0.605, 1.459] |  |  | 42 | 5 | 3bc20cea |
| test1 | start_points | frac:0.5 | rmse_h100 | patchtst[lookback=128] | 1.425 [1.043, 1.874] |  |  | 42 | 5 | 1a28f12a |
| test1 | start_points | frac:0.5 | rmse_h100 | transformer[lookback=32] | 1.067 [0.730, 1.495] |  |  | 42 | 5 | a3e9d648 |
| test1 | start_points | frac:0.5 | rmse_h200 | age_only | 3.493 [2.955, 4.039] |  |  | 41 | 5 | 7d094294 |
| test1 | start_points | frac:0.5 | rmse_h200 | elasticnet | 2.181 [1.665, 2.765] |  |  | 41 | 5 | 910f2d53 |
| test1 | start_points | frac:0.5 | rmse_h200 | itransformer[lookback=32] | 2.217 [1.617, 2.898] |  |  | 41 | 5 | 7ab9b903 |
| test1 | start_points | frac:0.5 | rmse_h200 | lgbm | 1.707 [1.287, 2.175] |  |  | 41 | 5 | c867ad3f |
| test1 | start_points | frac:0.5 | rmse_h200 | lstm[lookback=128] | 1.610 [1.069, 2.292] |  |  | 41 | 5 | 3bc20cea |
| test1 | start_points | frac:0.5 | rmse_h200 | patchtst[lookback=128] | 2.252 [1.725, 2.828] |  |  | 41 | 5 | 1a28f12a |
| test1 | start_points | frac:0.5 | rmse_h200 | transformer[lookback=32] | 1.846 [1.222, 2.617] |  |  | 41 | 5 | a3e9d648 |
| test1 | start_points | frac:0.5 | rmse_h50 | age_only | 2.909 [2.165, 3.728] |  |  | 43 | 5 | 7d094294 |
| test1 | start_points | frac:0.5 | rmse_h50 | elasticnet | 1.277 [0.794, 1.886] |  |  | 43 | 5 | 910f2d53 |
| test1 | start_points | frac:0.5 | rmse_h50 | itransformer[lookback=32] | 1.212 [0.820, 1.684] |  |  | 43 | 5 | 7ab9b903 |
| test1 | start_points | frac:0.5 | rmse_h50 | lgbm | 0.708 [0.449, 1.069] |  |  | 43 | 5 | c867ad3f |
| test1 | start_points | frac:0.5 | rmse_h50 | lstm[lookback=128] | 0.938 [0.523, 1.469] |  |  | 43 | 5 | 3bc20cea |
| test1 | start_points | frac:0.5 | rmse_h50 | patchtst[lookback=128] | 1.111 [0.816, 1.454] |  |  | 43 | 5 | 1a28f12a |
| test1 | start_points | frac:0.5 | rmse_h50 | transformer[lookback=32] | 0.938 [0.557, 1.435] |  |  | 43 | 5 | a3e9d648 |
| test1 | start_points | frac:0.7 | rmse_h1 | age_only | 2.799 [2.214, 3.433] |  |  | 43 | 5 | 7d094294 |
| test1 | start_points | frac:0.7 | rmse_h1 | elasticnet | 1.066 [0.659, 1.582] |  |  | 43 | 5 | 910f2d53 |
| test1 | start_points | frac:0.7 | rmse_h1 | itransformer[lookback=32] | 1.048 [0.779, 1.361] |  |  | 43 | 5 | 7ab9b903 |
| test1 | start_points | frac:0.7 | rmse_h1 | lgbm | 0.685 [0.462, 0.974] |  |  | 43 | 5 | c867ad3f |
| test1 | start_points | frac:0.7 | rmse_h1 | lstm[lookback=128] | 0.798 [0.516, 1.148] |  |  | 43 | 5 | 3bc20cea |
| test1 | start_points | frac:0.7 | rmse_h1 | patchtst[lookback=128] | 1.174 [0.912, 1.465] |  |  | 43 | 5 | 1a28f12a |
| test1 | start_points | frac:0.7 | rmse_h1 | transformer[lookback=32] | 0.800 [0.528, 1.139] |  |  | 43 | 5 | a3e9d648 |
| test1 | start_points | frac:0.7 | rmse_h10 | age_only | 2.816 [2.203, 3.509] |  |  | 42 | 5 | 7d094294 |
| test1 | start_points | frac:0.7 | rmse_h10 | elasticnet | 1.074 [0.652, 1.610] |  |  | 42 | 5 | 910f2d53 |
| test1 | start_points | frac:0.7 | rmse_h10 | itransformer[lookback=32] | 1.100 [0.804, 1.452] |  |  | 42 | 5 | 7ab9b903 |
| test1 | start_points | frac:0.7 | rmse_h10 | lgbm | 0.733 [0.496, 1.047] |  |  | 42 | 5 | c867ad3f |
| test1 | start_points | frac:0.7 | rmse_h10 | lstm[lookback=128] | 0.885 [0.563, 1.299] |  |  | 42 | 5 | 3bc20cea |
| test1 | start_points | frac:0.7 | rmse_h10 | patchtst[lookback=128] | 1.234 [0.944, 1.552] |  |  | 42 | 5 | 1a28f12a |
| test1 | start_points | frac:0.7 | rmse_h10 | transformer[lookback=32] | 0.869 [0.566, 1.255] |  |  | 42 | 5 | a3e9d648 |
| test1 | start_points | frac:0.7 | rmse_h100 | age_only | 2.980 [2.277, 3.817] |  |  | 42 | 5 | 7d094294 |
| test1 | start_points | frac:0.7 | rmse_h100 | elasticnet | 1.528 [1.062, 2.083] |  |  | 42 | 5 | 910f2d53 |
| test1 | start_points | frac:0.7 | rmse_h100 | itransformer[lookback=32] | 1.455 [1.133, 1.825] |  |  | 42 | 5 | 7ab9b903 |
| test1 | start_points | frac:0.7 | rmse_h100 | lgbm | 0.966 [0.754, 1.188] |  |  | 42 | 5 | c867ad3f |
| test1 | start_points | frac:0.7 | rmse_h100 | lstm[lookback=128] | 1.128 [0.817, 1.490] |  |  | 42 | 5 | 3bc20cea |
| test1 | start_points | frac:0.7 | rmse_h100 | patchtst[lookback=128] | 2.020 [1.591, 2.492] |  |  | 42 | 5 | 1a28f12a |
| test1 | start_points | frac:0.7 | rmse_h100 | transformer[lookback=32] | 0.998 [0.740, 1.291] |  |  | 42 | 5 | a3e9d648 |
| test1 | start_points | frac:0.7 | rmse_h200 | age_only | 5.001 [3.417, 6.768] |  |  | 17 | 5 | 7d094294 |
| test1 | start_points | frac:0.7 | rmse_h200 | elasticnet | 2.257 [1.627, 2.959] |  |  | 17 | 5 | 910f2d53 |
| test1 | start_points | frac:0.7 | rmse_h200 | itransformer[lookback=32] | 3.059 [1.880, 4.303] |  |  | 17 | 5 | 7ab9b903 |
| test1 | start_points | frac:0.7 | rmse_h200 | lgbm | 2.462 [1.598, 3.421] |  |  | 17 | 5 | c867ad3f |
| test1 | start_points | frac:0.7 | rmse_h200 | lstm[lookback=128] | 1.714 [1.043, 2.514] |  |  | 17 | 5 | 3bc20cea |
| test1 | start_points | frac:0.7 | rmse_h200 | patchtst[lookback=128] | 4.034 [2.472, 5.765] |  |  | 17 | 5 | 1a28f12a |
| test1 | start_points | frac:0.7 | rmse_h200 | transformer[lookback=32] | 1.929 [1.193, 2.786] |  |  | 17 | 5 | a3e9d648 |
| test1 | start_points | frac:0.7 | rmse_h50 | age_only | 2.758 [2.030, 3.754] |  |  | 43 | 5 | 7d094294 |
| test1 | start_points | frac:0.7 | rmse_h50 | elasticnet | 1.345 [0.817, 1.973] |  |  | 43 | 5 | 910f2d53 |
| test1 | start_points | frac:0.7 | rmse_h50 | itransformer[lookback=32] | 1.283 [0.892, 1.794] |  |  | 43 | 5 | 7ab9b903 |
| test1 | start_points | frac:0.7 | rmse_h50 | lgbm | 0.910 [0.582, 1.442] |  |  | 43 | 5 | c867ad3f |
| test1 | start_points | frac:0.7 | rmse_h50 | lstm[lookback=128] | 1.195 [0.725, 1.833] |  |  | 43 | 5 | 3bc20cea |
| test1 | start_points | frac:0.7 | rmse_h50 | patchtst[lookback=128] | 1.572 [1.190, 2.002] |  |  | 43 | 5 | 1a28f12a |
| test1 | start_points | frac:0.7 | rmse_h50 | transformer[lookback=32] | 1.138 [0.696, 1.741] |  |  | 43 | 5 | a3e9d648 |
| test1 | start_points | overall | rmse_h1 | age_only | 2.180 [1.715, 2.676] |  |  | 43 | 5 | 7d094294 |
| test1 | start_points | overall | rmse_h1 | elasticnet | 0.936 [0.687, 1.247] |  |  | 43 | 5 | 910f2d53 |
| test1 | start_points | overall | rmse_h1 | itransformer[lookback=32] | 0.866 [0.679, 1.081] |  |  | 43 | 5 | 7ab9b903 |
| test1 | start_points | overall | rmse_h1 | lgbm | 0.548 [0.382, 0.762] |  |  | 43 | 5 | c867ad3f |
| test1 | start_points | overall | rmse_h1 | lstm[lookback=128] | 0.603 [0.405, 0.848] |  |  | 43 | 5 | 3bc20cea |
| test1 | start_points | overall | rmse_h1 | patchtst[lookback=128] | 0.996 [0.844, 1.174] |  |  | 43 | 5 | 1a28f12a |
| test1 | start_points | overall | rmse_h1 | transformer[lookback=32] | 0.620 [0.434, 0.849] |  |  | 43 | 5 | a3e9d648 |
| test1 | start_points | overall | rmse_h10 | age_only | 2.208 [1.713, 2.750] |  |  | 43 | 5 | 7d094294 |
| test1 | start_points | overall | rmse_h10 | elasticnet | 0.955 [0.687, 1.296] |  |  | 43 | 5 | 910f2d53 |
| test1 | start_points | overall | rmse_h10 | itransformer[lookback=32] | 0.902 [0.684, 1.159] |  |  | 43 | 5 | 7ab9b903 |
| test1 | start_points | overall | rmse_h10 | lgbm | 0.570 [0.392, 0.809] |  |  | 43 | 5 | c867ad3f |
| test1 | start_points | overall | rmse_h10 | lstm[lookback=128] | 0.659 [0.430, 0.951] |  |  | 43 | 5 | 3bc20cea |
| test1 | start_points | overall | rmse_h10 | patchtst[lookback=128] | 1.037 [0.878, 1.222] |  |  | 43 | 5 | 1a28f12a |
| test1 | start_points | overall | rmse_h10 | transformer[lookback=32] | 0.651 [0.444, 0.913] |  |  | 43 | 5 | a3e9d648 |
| test1 | start_points | overall | rmse_h100 | age_only | 3.019 [2.389, 3.884] |  |  | 43 | 5 | 7d094294 |
| test1 | start_points | overall | rmse_h100 | elasticnet | 1.686 [1.178, 2.371] |  |  | 43 | 5 | 910f2d53 |
| test1 | start_points | overall | rmse_h100 | itransformer[lookback=32] | 1.576 [1.130, 2.220] |  |  | 43 | 5 | 7ab9b903 |
| test1 | start_points | overall | rmse_h100 | lgbm | 0.977 [0.660, 1.490] |  |  | 43 | 5 | c867ad3f |
| test1 | start_points | overall | rmse_h100 | lstm[lookback=128] | 1.174 [0.739, 1.791] |  |  | 43 | 5 | 3bc20cea |
| test1 | start_points | overall | rmse_h100 | patchtst[lookback=128] | 1.875 [1.507, 2.350] |  |  | 43 | 5 | 1a28f12a |
| test1 | start_points | overall | rmse_h100 | transformer[lookback=32] | 1.186 [0.762, 1.817] |  |  | 43 | 5 | a3e9d648 |
| test1 | start_points | overall | rmse_h200 | age_only | 3.477 [2.951, 4.075] |  |  | 42 | 5 | 7d094294 |
| test1 | start_points | overall | rmse_h200 | elasticnet | 1.974 [1.575, 2.438] |  |  | 42 | 5 | 910f2d53 |
| test1 | start_points | overall | rmse_h200 | itransformer[lookback=32] | 2.167 [1.711, 2.661] |  |  | 42 | 5 | 7ab9b903 |
| test1 | start_points | overall | rmse_h200 | lgbm | 1.536 [1.232, 1.880] |  |  | 42 | 5 | c867ad3f |
| test1 | start_points | overall | rmse_h200 | lstm[lookback=128] | 1.428 [1.053, 1.858] |  |  | 42 | 5 | 3bc20cea |
| test1 | start_points | overall | rmse_h200 | patchtst[lookback=128] | 2.686 [2.260, 3.162] |  |  | 42 | 5 | 1a28f12a |
| test1 | start_points | overall | rmse_h200 | transformer[lookback=32] | 1.638 [1.205, 2.140] |  |  | 42 | 5 | a3e9d648 |
| test1 | start_points | overall | rmse_h50 | age_only | 2.420 [1.806, 3.205] |  |  | 43 | 5 | 7d094294 |
| test1 | start_points | overall | rmse_h50 | elasticnet | 1.236 [0.853, 1.719] |  |  | 43 | 5 | 910f2d53 |
| test1 | start_points | overall | rmse_h50 | itransformer[lookback=32] | 1.149 [0.827, 1.586] |  |  | 43 | 5 | 7ab9b903 |
| test1 | start_points | overall | rmse_h50 | lgbm | 0.713 [0.456, 1.131] |  |  | 43 | 5 | c867ad3f |
| test1 | start_points | overall | rmse_h50 | lstm[lookback=128] | 0.909 [0.547, 1.419] |  |  | 43 | 5 | 3bc20cea |
| test1 | start_points | overall | rmse_h50 | patchtst[lookback=128] | 1.329 [1.095, 1.609] |  |  | 43 | 5 | 1a28f12a |
| test1 | start_points | overall | rmse_h50 | transformer[lookback=32] | 0.905 [0.562, 1.396] |  |  | 43 | 5 | a3e9d648 |
| test2 | all | overall | rmse_h1 | age_only | 3.679 [3.525, 3.827] |  |  | 40 | 5 | 7d094294 |
| test2 | all | overall | rmse_h1 | elasticnet | 3.949 [3.821, 4.100] |  |  | 40 | 5 | 910f2d53 |
| test2 | all | overall | rmse_h1 | itransformer[lookback=32] | 1.557 [1.426, 1.696] |  |  | 40 | 5 | 7ab9b903 |
| test2 | all | overall | rmse_h1 | lgbm | 2.515 [2.390, 2.644] |  |  | 40 | 5 | c867ad3f |
| test2 | all | overall | rmse_h1 | lstm[lookback=128] | 2.278 [2.117, 2.464] |  |  | 40 | 5 | 3bc20cea |
| test2 | all | overall | rmse_h1 | patchtst[lookback=128] | 2.411 [2.295, 2.543] |  |  | 40 | 5 | 1a28f12a |
| test2 | all | overall | rmse_h1 | transformer[lookback=32] | 2.511 [2.369, 2.682] |  |  | 40 | 5 | a3e9d648 |
| test2 | all | overall | rmse_h10 | age_only | 3.696 [3.542, 3.844] |  |  | 40 | 5 | 7d094294 |
| test2 | all | overall | rmse_h10 | elasticnet | 4.071 [3.947, 4.217] |  |  | 40 | 5 | 910f2d53 |
| test2 | all | overall | rmse_h10 | itransformer[lookback=32] | 1.544 [1.414, 1.683] |  |  | 40 | 5 | 7ab9b903 |
| test2 | all | overall | rmse_h10 | lgbm | 2.542 [2.408, 2.679] |  |  | 40 | 5 | c867ad3f |
| test2 | all | overall | rmse_h10 | lstm[lookback=128] | 2.186 [2.037, 2.352] |  |  | 40 | 5 | 3bc20cea |
| test2 | all | overall | rmse_h10 | patchtst[lookback=128] | 2.449 [2.337, 2.578] |  |  | 40 | 5 | 1a28f12a |
| test2 | all | overall | rmse_h10 | transformer[lookback=32] | 2.956 [2.796, 3.151] |  |  | 40 | 5 | a3e9d648 |
| test2 | all | overall | rmse_h100 | age_only | 3.879 [3.727, 4.024] |  |  | 40 | 5 | 7d094294 |
| test2 | all | overall | rmse_h100 | elasticnet | 3.111 [2.689, 3.595] |  |  | 40 | 5 | 910f2d53 |
| test2 | all | overall | rmse_h100 | itransformer[lookback=32] | 2.578 [2.378, 2.781] |  |  | 40 | 5 | 7ab9b903 |
| test2 | all | overall | rmse_h100 | lgbm | 2.412 [2.259, 2.566] |  |  | 40 | 5 | c867ad3f |
| test2 | all | overall | rmse_h100 | lstm[lookback=128] | 1.665 [1.539, 1.808] |  |  | 40 | 5 | 3bc20cea |
| test2 | all | overall | rmse_h100 | patchtst[lookback=128] | 3.028 [2.876, 3.189] |  |  | 40 | 5 | 1a28f12a |
| test2 | all | overall | rmse_h100 | transformer[lookback=32] | 2.331 [2.140, 2.549] |  |  | 40 | 5 | a3e9d648 |
| test2 | all | overall | rmse_h200 | age_only | 4.112 [3.964, 4.254] |  |  | 40 | 5 | 7d094294 |
| test2 | all | overall | rmse_h200 | elasticnet | 2.247 [2.056, 2.459] |  |  | 40 | 5 | 910f2d53 |
| test2 | all | overall | rmse_h200 | itransformer[lookback=32] | 3.876 [3.414, 4.347] |  |  | 40 | 5 | 7ab9b903 |
| test2 | all | overall | rmse_h200 | lgbm | 2.501 [2.318, 2.681] |  |  | 40 | 5 | c867ad3f |
| test2 | all | overall | rmse_h200 | lstm[lookback=128] | 1.978 [1.810, 2.157] |  |  | 40 | 5 | 3bc20cea |
| test2 | all | overall | rmse_h200 | patchtst[lookback=128] | 3.984 [3.717, 4.246] |  |  | 40 | 5 | 1a28f12a |
| test2 | all | overall | rmse_h200 | transformer[lookback=32] | 2.588 [2.323, 2.862] |  |  | 40 | 5 | a3e9d648 |
| test2 | all | overall | rmse_h50 | age_only | 3.774 [3.621, 3.921] |  |  | 40 | 5 | 7d094294 |
| test2 | all | overall | rmse_h50 | elasticnet | 4.223 [4.026, 4.438] |  |  | 40 | 5 | 910f2d53 |
| test2 | all | overall | rmse_h50 | itransformer[lookback=32] | 1.903 [1.781, 2.029] |  |  | 40 | 5 | 7ab9b903 |
| test2 | all | overall | rmse_h50 | lgbm | 2.446 [2.306, 2.586] |  |  | 40 | 5 | c867ad3f |
| test2 | all | overall | rmse_h50 | lstm[lookback=128] | 2.200 [2.073, 2.341] |  |  | 40 | 5 | 3bc20cea |
| test2 | all | overall | rmse_h50 | patchtst[lookback=128] | 2.779 [2.683, 2.889] |  |  | 40 | 5 | 1a28f12a |
| test2 | all | overall | rmse_h50 | transformer[lookback=32] | 2.740 [2.524, 2.985] |  |  | 40 | 5 | a3e9d648 |
| test2 | start_points | fixed:100 | rmse_h1 | age_only | 0.260 [0.153, 0.396] |  |  | 40 | 5 | 7d094294 |
| test2 | start_points | fixed:100 | rmse_h1 | elasticnet | 1.181 [0.991, 1.371] |  |  | 40 | 5 | 910f2d53 |
| test2 | start_points | fixed:100 | rmse_h1 | itransformer[lookback=32] | 0.352 [0.291, 0.420] |  |  | 40 | 5 | 7ab9b903 |
| test2 | start_points | fixed:100 | rmse_h1 | lgbm | 0.589 [0.503, 0.679] |  |  | 40 | 5 | c867ad3f |
| test2 | start_points | fixed:100 | rmse_h1 | lstm[lookback=128] | 0.333 [0.284, 0.385] |  |  | 40 | 5 | 3bc20cea |
| test2 | start_points | fixed:100 | rmse_h1 | patchtst[lookback=128] | 0.529 [0.434, 0.630] |  |  | 40 | 5 | 1a28f12a |
| test2 | start_points | fixed:100 | rmse_h1 | transformer[lookback=32] | 0.546 [0.458, 0.637] |  |  | 40 | 5 | a3e9d648 |
| test2 | start_points | fixed:100 | rmse_h10 | age_only | 0.315 [0.203, 0.456] |  |  | 40 | 5 | 7d094294 |
| test2 | start_points | fixed:100 | rmse_h10 | elasticnet | 1.186 [1.000, 1.373] |  |  | 40 | 5 | 910f2d53 |
| test2 | start_points | fixed:100 | rmse_h10 | itransformer[lookback=32] | 0.342 [0.280, 0.410] |  |  | 40 | 5 | 7ab9b903 |
| test2 | start_points | fixed:100 | rmse_h10 | lgbm | 0.590 [0.506, 0.677] |  |  | 40 | 5 | c867ad3f |
| test2 | start_points | fixed:100 | rmse_h10 | lstm[lookback=128] | 0.353 [0.306, 0.401] |  |  | 40 | 5 | 3bc20cea |
| test2 | start_points | fixed:100 | rmse_h10 | patchtst[lookback=128] | 0.592 [0.489, 0.704] |  |  | 40 | 5 | 1a28f12a |
| test2 | start_points | fixed:100 | rmse_h10 | transformer[lookback=32] | 0.585 [0.492, 0.682] |  |  | 40 | 5 | a3e9d648 |
| test2 | start_points | fixed:100 | rmse_h100 | age_only | 0.899 [0.764, 1.073] |  |  | 40 | 5 | 7d094294 |
| test2 | start_points | fixed:100 | rmse_h100 | elasticnet | 0.808 [0.659, 0.965] |  |  | 40 | 5 | 910f2d53 |
| test2 | start_points | fixed:100 | rmse_h100 | itransformer[lookback=32] | 0.584 [0.485, 0.694] |  |  | 40 | 5 | 7ab9b903 |
| test2 | start_points | fixed:100 | rmse_h100 | lgbm | 0.792 [0.671, 0.914] |  |  | 40 | 5 | c867ad3f |
| test2 | start_points | fixed:100 | rmse_h100 | lstm[lookback=128] | 0.417 [0.355, 0.485] |  |  | 40 | 5 | 3bc20cea |
| test2 | start_points | fixed:100 | rmse_h100 | patchtst[lookback=128] | 0.807 [0.681, 0.951] |  |  | 40 | 5 | 1a28f12a |
| test2 | start_points | fixed:100 | rmse_h100 | transformer[lookback=32] | 1.021 [0.904, 1.141] |  |  | 40 | 5 | a3e9d648 |
| test2 | start_points | fixed:100 | rmse_h200 | age_only | 1.869 [1.755, 2.017] |  |  | 40 | 5 | 7d094294 |
| test2 | start_points | fixed:100 | rmse_h200 | elasticnet | 0.517 [0.400, 0.638] |  |  | 40 | 5 | 910f2d53 |
| test2 | start_points | fixed:100 | rmse_h200 | itransformer[lookback=32] | 0.956 [0.768, 1.156] |  |  | 40 | 5 | 7ab9b903 |
| test2 | start_points | fixed:100 | rmse_h200 | lgbm | 1.123 [0.957, 1.292] |  |  | 40 | 5 | c867ad3f |
| test2 | start_points | fixed:100 | rmse_h200 | lstm[lookback=128] | 0.509 [0.440, 0.582] |  |  | 40 | 5 | 3bc20cea |
| test2 | start_points | fixed:100 | rmse_h200 | patchtst[lookback=128] | 1.333 [1.119, 1.566] |  |  | 40 | 5 | 1a28f12a |
| test2 | start_points | fixed:100 | rmse_h200 | transformer[lookback=32] | 1.118 [0.971, 1.281] |  |  | 40 | 5 | a3e9d648 |
| test2 | start_points | fixed:100 | rmse_h50 | age_only | 0.565 [0.439, 0.726] |  |  | 40 | 5 | 7d094294 |
| test2 | start_points | fixed:100 | rmse_h50 | elasticnet | 1.100 [0.911, 1.289] |  |  | 40 | 5 | 910f2d53 |
| test2 | start_points | fixed:100 | rmse_h50 | itransformer[lookback=32] | 0.400 [0.320, 0.488] |  |  | 40 | 5 | 7ab9b903 |
| test2 | start_points | fixed:100 | rmse_h50 | lgbm | 0.562 [0.496, 0.627] |  |  | 40 | 5 | c867ad3f |
| test2 | start_points | fixed:100 | rmse_h50 | lstm[lookback=128] | 0.409 [0.345, 0.477] |  |  | 40 | 5 | 3bc20cea |
| test2 | start_points | fixed:100 | rmse_h50 | patchtst[lookback=128] | 0.765 [0.641, 0.898] |  |  | 40 | 5 | 1a28f12a |
| test2 | start_points | fixed:100 | rmse_h50 | transformer[lookback=32] | 0.598 [0.500, 0.699] |  |  | 40 | 5 | a3e9d648 |
| test2 | start_points | frac:0.3 | rmse_h1 | age_only | 2.223 [1.819, 2.700] |  |  | 40 | 5 | 7d094294 |
| test2 | start_points | frac:0.3 | rmse_h1 | elasticnet | 1.832 [1.612, 2.044] |  |  | 40 | 5 | 910f2d53 |
| test2 | start_points | frac:0.3 | rmse_h1 | itransformer[lookback=32] | 0.644 [0.525, 0.777] |  |  | 40 | 5 | 7ab9b903 |
| test2 | start_points | frac:0.3 | rmse_h1 | lgbm | 0.520 [0.439, 0.601] |  |  | 40 | 5 | c867ad3f |
| test2 | start_points | frac:0.3 | rmse_h1 | lstm[lookback=128] | 0.481 [0.390, 0.585] |  |  | 40 | 5 | 3bc20cea |
| test2 | start_points | frac:0.3 | rmse_h1 | patchtst[lookback=128] | 0.945 [0.797, 1.102] |  |  | 40 | 5 | 1a28f12a |
| test2 | start_points | frac:0.3 | rmse_h1 | transformer[lookback=32] | 0.951 [0.823, 1.074] |  |  | 40 | 5 | a3e9d648 |
| test2 | start_points | frac:0.3 | rmse_h10 | age_only | 2.316 [1.919, 2.782] |  |  | 40 | 5 | 7d094294 |
| test2 | start_points | frac:0.3 | rmse_h10 | elasticnet | 1.848 [1.632, 2.057] |  |  | 40 | 5 | 910f2d53 |
| test2 | start_points | frac:0.3 | rmse_h10 | itransformer[lookback=32] | 0.627 [0.501, 0.775] |  |  | 40 | 5 | 7ab9b903 |
| test2 | start_points | frac:0.3 | rmse_h10 | lgbm | 0.631 [0.513, 0.751] |  |  | 40 | 5 | c867ad3f |
| test2 | start_points | frac:0.3 | rmse_h10 | lstm[lookback=128] | 0.534 [0.438, 0.637] |  |  | 40 | 5 | 3bc20cea |
| test2 | start_points | frac:0.3 | rmse_h10 | patchtst[lookback=128] | 1.002 [0.847, 1.165] |  |  | 40 | 5 | 1a28f12a |
| test2 | start_points | frac:0.3 | rmse_h10 | transformer[lookback=32] | 0.929 [0.788, 1.069] |  |  | 40 | 5 | a3e9d648 |
| test2 | start_points | frac:0.3 | rmse_h100 | age_only | 3.799 [3.311, 4.301] |  |  | 40 | 5 | 7d094294 |
| test2 | start_points | frac:0.3 | rmse_h100 | elasticnet | 1.452 [1.236, 1.657] |  |  | 40 | 5 | 910f2d53 |
| test2 | start_points | frac:0.3 | rmse_h100 | itransformer[lookback=32] | 1.241 [1.050, 1.444] |  |  | 40 | 5 | 7ab9b903 |
| test2 | start_points | frac:0.3 | rmse_h100 | lgbm | 1.095 [0.917, 1.271] |  |  | 40 | 5 | c867ad3f |
| test2 | start_points | frac:0.3 | rmse_h100 | lstm[lookback=128] | 0.588 [0.475, 0.715] |  |  | 40 | 5 | 3bc20cea |
| test2 | start_points | frac:0.3 | rmse_h100 | patchtst[lookback=128] | 1.992 [1.673, 2.304] |  |  | 40 | 5 | 1a28f12a |
| test2 | start_points | frac:0.3 | rmse_h100 | transformer[lookback=32] | 1.161 [0.992, 1.327] |  |  | 40 | 5 | a3e9d648 |
| test2 | start_points | frac:0.3 | rmse_h200 | age_only | 5.437 [5.101, 5.697] |  |  | 40 | 5 | 7d094294 |
| test2 | start_points | frac:0.3 | rmse_h200 | elasticnet | 1.169 [0.913, 1.431] |  |  | 40 | 5 | 910f2d53 |
| test2 | start_points | frac:0.3 | rmse_h200 | itransformer[lookback=32] | 2.254 [1.831, 2.679] |  |  | 40 | 5 | 7ab9b903 |
| test2 | start_points | frac:0.3 | rmse_h200 | lgbm | 1.500 [1.282, 1.720] |  |  | 40 | 5 | c867ad3f |
| test2 | start_points | frac:0.3 | rmse_h200 | lstm[lookback=128] | 0.790 [0.633, 0.961] |  |  | 40 | 5 | 3bc20cea |
| test2 | start_points | frac:0.3 | rmse_h200 | patchtst[lookback=128] | 4.339 [3.820, 4.849] |  |  | 40 | 5 | 1a28f12a |
| test2 | start_points | frac:0.3 | rmse_h200 | transformer[lookback=32] | 1.586 [1.360, 1.824] |  |  | 40 | 5 | a3e9d648 |
| test2 | start_points | frac:0.3 | rmse_h50 | age_only | 2.845 [2.432, 3.304] |  |  | 40 | 5 | 7d094294 |
| test2 | start_points | frac:0.3 | rmse_h50 | elasticnet | 1.761 [1.547, 1.967] |  |  | 40 | 5 | 910f2d53 |
| test2 | start_points | frac:0.3 | rmse_h50 | itransformer[lookback=32] | 0.789 [0.638, 0.964] |  |  | 40 | 5 | 7ab9b903 |
| test2 | start_points | frac:0.3 | rmse_h50 | lgbm | 0.680 [0.544, 0.822] |  |  | 40 | 5 | c867ad3f |
| test2 | start_points | frac:0.3 | rmse_h50 | lstm[lookback=128] | 0.565 [0.465, 0.671] |  |  | 40 | 5 | 3bc20cea |
| test2 | start_points | frac:0.3 | rmse_h50 | patchtst[lookback=128] | 1.366 [1.157, 1.580] |  |  | 40 | 5 | 1a28f12a |
| test2 | start_points | frac:0.3 | rmse_h50 | transformer[lookback=32] | 0.881 [0.744, 1.019] |  |  | 40 | 5 | a3e9d648 |
| test2 | start_points | frac:0.5 | rmse_h1 | age_only | 4.902 [4.528, 5.234] |  |  | 40 | 5 | 7d094294 |
| test2 | start_points | frac:0.5 | rmse_h1 | elasticnet | 1.941 [1.689, 2.180] |  |  | 40 | 5 | 910f2d53 |
| test2 | start_points | frac:0.5 | rmse_h1 | itransformer[lookback=32] | 1.287 [1.102, 1.479] |  |  | 40 | 5 | 7ab9b903 |
| test2 | start_points | frac:0.5 | rmse_h1 | lgbm | 1.354 [1.080, 1.634] |  |  | 40 | 5 | c867ad3f |
| test2 | start_points | frac:0.5 | rmse_h1 | lstm[lookback=128] | 0.789 [0.664, 0.928] |  |  | 40 | 5 | 3bc20cea |
| test2 | start_points | frac:0.5 | rmse_h1 | patchtst[lookback=128] | 0.822 [0.618, 1.068] |  |  | 40 | 5 | 1a28f12a |
| test2 | start_points | frac:0.5 | rmse_h1 | transformer[lookback=32] | 1.356 [1.208, 1.498] |  |  | 40 | 5 | a3e9d648 |
| test2 | start_points | frac:0.5 | rmse_h10 | age_only | 4.998 [4.636, 5.309] |  |  | 40 | 5 | 7d094294 |
| test2 | start_points | frac:0.5 | rmse_h10 | elasticnet | 1.999 [1.744, 2.241] |  |  | 40 | 5 | 910f2d53 |
| test2 | start_points | frac:0.5 | rmse_h10 | itransformer[lookback=32] | 1.280 [1.099, 1.470] |  |  | 40 | 5 | 7ab9b903 |
| test2 | start_points | frac:0.5 | rmse_h10 | lgbm | 1.482 [1.182, 1.791] |  |  | 40 | 5 | c867ad3f |
| test2 | start_points | frac:0.5 | rmse_h10 | lstm[lookback=128] | 0.870 [0.738, 1.005] |  |  | 40 | 5 | 3bc20cea |
| test2 | start_points | frac:0.5 | rmse_h10 | patchtst[lookback=128] | 0.879 [0.674, 1.120] |  |  | 40 | 5 | 1a28f12a |
| test2 | start_points | frac:0.5 | rmse_h10 | transformer[lookback=32] | 1.406 [1.239, 1.566] |  |  | 40 | 5 | a3e9d648 |
| test2 | start_points | frac:0.5 | rmse_h100 | age_only | 4.899 [4.566, 5.150] |  |  | 40 | 5 | 7d094294 |
| test2 | start_points | frac:0.5 | rmse_h100 | elasticnet | 2.374 [2.113, 2.632] |  |  | 40 | 5 | 910f2d53 |
| test2 | start_points | frac:0.5 | rmse_h100 | itransformer[lookback=32] | 2.682 [2.318, 3.051] |  |  | 40 | 5 | 7ab9b903 |
| test2 | start_points | frac:0.5 | rmse_h100 | lgbm | 2.389 [2.038, 2.761] |  |  | 40 | 5 | c867ad3f |
| test2 | start_points | frac:0.5 | rmse_h100 | lstm[lookback=128] | 1.421 [1.233, 1.609] |  |  | 40 | 5 | 3bc20cea |
| test2 | start_points | frac:0.5 | rmse_h100 | patchtst[lookback=128] | 2.060 [1.732, 2.390] |  |  | 40 | 5 | 1a28f12a |
| test2 | start_points | frac:0.5 | rmse_h100 | transformer[lookback=32] | 2.320 [2.071, 2.557] |  |  | 40 | 5 | a3e9d648 |
| test2 | start_points | frac:0.5 | rmse_h200 | age_only | 4.310 [4.014, 4.591] |  |  | 40 | 5 | 7d094294 |
| test2 | start_points | frac:0.5 | rmse_h200 | elasticnet | 3.134 [2.710, 3.566] |  |  | 40 | 5 | 910f2d53 |
| test2 | start_points | frac:0.5 | rmse_h200 | itransformer[lookback=32] | 4.897 [4.211, 5.615] |  |  | 40 | 5 | 7ab9b903 |
| test2 | start_points | frac:0.5 | rmse_h200 | lgbm | 2.894 [2.465, 3.315] |  |  | 40 | 5 | c867ad3f |
| test2 | start_points | frac:0.5 | rmse_h200 | lstm[lookback=128] | 2.435 [2.091, 2.795] |  |  | 40 | 5 | 3bc20cea |
| test2 | start_points | frac:0.5 | rmse_h200 | patchtst[lookback=128] | 4.321 [3.825, 4.814] |  |  | 40 | 5 | 1a28f12a |
| test2 | start_points | frac:0.5 | rmse_h200 | transformer[lookback=32] | 3.447 [3.003, 3.896] |  |  | 40 | 5 | a3e9d648 |
| test2 | start_points | frac:0.5 | rmse_h50 | age_only | 5.172 [4.877, 5.406] |  |  | 40 | 5 | 7d094294 |
| test2 | start_points | frac:0.5 | rmse_h50 | elasticnet | 2.219 [1.953, 2.471] |  |  | 40 | 5 | 910f2d53 |
| test2 | start_points | frac:0.5 | rmse_h50 | itransformer[lookback=32] | 1.728 [1.505, 1.952] |  |  | 40 | 5 | 7ab9b903 |
| test2 | start_points | frac:0.5 | rmse_h50 | lgbm | 1.836 [1.492, 2.189] |  |  | 40 | 5 | c867ad3f |
| test2 | start_points | frac:0.5 | rmse_h50 | lstm[lookback=128] | 1.101 [0.942, 1.260] |  |  | 40 | 5 | 3bc20cea |
| test2 | start_points | frac:0.5 | rmse_h50 | patchtst[lookback=128] | 1.239 [1.003, 1.492] |  |  | 40 | 5 | 1a28f12a |
| test2 | start_points | frac:0.5 | rmse_h50 | transformer[lookback=32] | 1.521 [1.337, 1.701] |  |  | 40 | 5 | a3e9d648 |
| test2 | start_points | frac:0.7 | rmse_h1 | age_only | 4.255 [3.955, 4.522] |  |  | 40 | 5 | 7d094294 |
| test2 | start_points | frac:0.7 | rmse_h1 | elasticnet | 1.686 [1.434, 1.946] |  |  | 40 | 5 | 910f2d53 |
| test2 | start_points | frac:0.7 | rmse_h1 | itransformer[lookback=32] | 2.383 [2.036, 2.736] |  |  | 40 | 5 | 7ab9b903 |
| test2 | start_points | frac:0.7 | rmse_h1 | lgbm | 2.205 [1.873, 2.523] |  |  | 40 | 5 | c867ad3f |
| test2 | start_points | frac:0.7 | rmse_h1 | lstm[lookback=128] | 1.166 [1.020, 1.311] |  |  | 40 | 5 | 3bc20cea |
| test2 | start_points | frac:0.7 | rmse_h1 | patchtst[lookback=128] | 1.441 [1.013, 1.930] |  |  | 40 | 5 | 1a28f12a |
| test2 | start_points | frac:0.7 | rmse_h1 | transformer[lookback=32] | 1.709 [1.547, 1.860] |  |  | 40 | 5 | a3e9d648 |
| test2 | start_points | frac:0.7 | rmse_h10 | age_only | 4.178 [3.893, 4.440] |  |  | 40 | 5 | 7d094294 |
| test2 | start_points | frac:0.7 | rmse_h10 | elasticnet | 1.744 [1.491, 2.002] |  |  | 40 | 5 | 910f2d53 |
| test2 | start_points | frac:0.7 | rmse_h10 | itransformer[lookback=32] | 2.359 [2.017, 2.708] |  |  | 40 | 5 | 7ab9b903 |
| test2 | start_points | frac:0.7 | rmse_h10 | lgbm | 2.325 [1.987, 2.650] |  |  | 40 | 5 | c867ad3f |
| test2 | start_points | frac:0.7 | rmse_h10 | lstm[lookback=128] | 1.287 [1.128, 1.448] |  |  | 40 | 5 | 3bc20cea |
| test2 | start_points | frac:0.7 | rmse_h10 | patchtst[lookback=128] | 1.533 [1.086, 2.040] |  |  | 40 | 5 | 1a28f12a |
| test2 | start_points | frac:0.7 | rmse_h10 | transformer[lookback=32] | 1.768 [1.582, 1.946] |  |  | 40 | 5 | a3e9d648 |
| test2 | start_points | frac:0.7 | rmse_h100 | age_only | 3.157 [2.854, 3.450] |  |  | 40 | 5 | 7d094294 |
| test2 | start_points | frac:0.7 | rmse_h100 | elasticnet | 1.874 [1.537, 2.229] |  |  | 40 | 5 | 910f2d53 |
| test2 | start_points | frac:0.7 | rmse_h100 | itransformer[lookback=32] | 3.796 [3.293, 4.303] |  |  | 40 | 5 | 7ab9b903 |
| test2 | start_points | frac:0.7 | rmse_h100 | lgbm | 2.772 [2.354, 3.175] |  |  | 40 | 5 | c867ad3f |
| test2 | start_points | frac:0.7 | rmse_h100 | lstm[lookback=128] | 1.818 [1.586, 2.060] |  |  | 40 | 5 | 3bc20cea |
| test2 | start_points | frac:0.7 | rmse_h100 | patchtst[lookback=128] | 2.911 [2.430, 3.421] |  |  | 40 | 5 | 1a28f12a |
| test2 | start_points | frac:0.7 | rmse_h100 | transformer[lookback=32] | 2.763 [2.484, 3.028] |  |  | 40 | 5 | a3e9d648 |
| test2 | start_points | frac:0.7 | rmse_h200 | age_only | 2.092 [1.566, 2.644] |  |  | 38 | 5 | 7d094294 |
| test2 | start_points | frac:0.7 | rmse_h200 | elasticnet | 1.389 [1.015, 1.823] |  |  | 38 | 5 | 910f2d53 |
| test2 | start_points | frac:0.7 | rmse_h200 | itransformer[lookback=32] | 4.786 [3.935, 5.627] |  |  | 38 | 5 | 7ab9b903 |
| test2 | start_points | frac:0.7 | rmse_h200 | lgbm | 1.443 [1.106, 1.806] |  |  | 38 | 5 | c867ad3f |
| test2 | start_points | frac:0.7 | rmse_h200 | lstm[lookback=128] | 2.240 [1.802, 2.727] |  |  | 38 | 5 | 3bc20cea |
| test2 | start_points | frac:0.7 | rmse_h200 | patchtst[lookback=128] | 2.405 [1.823, 3.042] |  |  | 38 | 5 | 1a28f12a |
| test2 | start_points | frac:0.7 | rmse_h200 | transformer[lookback=32] | 2.843 [2.322, 3.375] |  |  | 38 | 5 | a3e9d648 |
| test2 | start_points | frac:0.7 | rmse_h50 | age_only | 3.765 [3.507, 4.017] |  |  | 40 | 5 | 7d094294 |
| test2 | start_points | frac:0.7 | rmse_h50 | elasticnet | 1.919 [1.652, 2.187] |  |  | 40 | 5 | 910f2d53 |
| test2 | start_points | frac:0.7 | rmse_h50 | itransformer[lookback=32] | 2.920 [2.564, 3.277] |  |  | 40 | 5 | 7ab9b903 |
| test2 | start_points | frac:0.7 | rmse_h50 | lgbm | 2.642 [2.282, 2.985] |  |  | 40 | 5 | c867ad3f |
| test2 | start_points | frac:0.7 | rmse_h50 | lstm[lookback=128] | 1.524 [1.320, 1.729] |  |  | 40 | 5 | 3bc20cea |
| test2 | start_points | frac:0.7 | rmse_h50 | patchtst[lookback=128] | 2.007 [1.528, 2.536] |  |  | 40 | 5 | 1a28f12a |
| test2 | start_points | frac:0.7 | rmse_h50 | transformer[lookback=32] | 1.914 [1.704, 2.113] |  |  | 40 | 5 | a3e9d648 |
| test2 | start_points | overall | rmse_h1 | age_only | 3.520 [3.296, 3.727] |  |  | 40 | 5 | 7d094294 |
| test2 | start_points | overall | rmse_h1 | elasticnet | 1.734 [1.546, 1.923] |  |  | 40 | 5 | 910f2d53 |
| test2 | start_points | overall | rmse_h1 | itransformer[lookback=32] | 1.463 [1.283, 1.649] |  |  | 40 | 5 | 7ab9b903 |
| test2 | start_points | overall | rmse_h1 | lgbm | 1.400 [1.209, 1.586] |  |  | 40 | 5 | c867ad3f |
| test2 | start_points | overall | rmse_h1 | lstm[lookback=128] | 0.799 [0.706, 0.898] |  |  | 40 | 5 | 3bc20cea |
| test2 | start_points | overall | rmse_h1 | patchtst[lookback=128] | 1.139 [0.943, 1.372] |  |  | 40 | 5 | 1a28f12a |
| test2 | start_points | overall | rmse_h1 | transformer[lookback=32] | 1.243 [1.124, 1.355] |  |  | 40 | 5 | a3e9d648 |
| test2 | start_points | overall | rmse_h10 | age_only | 3.543 [3.330, 3.741] |  |  | 40 | 5 | 7d094294 |
| test2 | start_points | overall | rmse_h10 | elasticnet | 1.770 [1.583, 1.958] |  |  | 40 | 5 | 910f2d53 |
| test2 | start_points | overall | rmse_h10 | itransformer[lookback=32] | 1.442 [1.259, 1.631] |  |  | 40 | 5 | 7ab9b903 |
| test2 | start_points | overall | rmse_h10 | lgbm | 1.494 [1.287, 1.695] |  |  | 40 | 5 | c867ad3f |
| test2 | start_points | overall | rmse_h10 | lstm[lookback=128] | 0.876 [0.776, 0.976] |  |  | 40 | 5 | 3bc20cea |
| test2 | start_points | overall | rmse_h10 | patchtst[lookback=128] | 1.216 [1.018, 1.451] |  |  | 40 | 5 | 1a28f12a |
| test2 | start_points | overall | rmse_h10 | transformer[lookback=32] | 1.286 [1.155, 1.411] |  |  | 40 | 5 | a3e9d648 |
| test2 | start_points | overall | rmse_h100 | age_only | 3.612 [3.410, 3.808] |  |  | 40 | 5 | 7d094294 |
| test2 | start_points | overall | rmse_h100 | elasticnet | 1.802 [1.604, 1.990] |  |  | 40 | 5 | 910f2d53 |
| test2 | start_points | overall | rmse_h100 | itransformer[lookback=32] | 2.538 [2.281, 2.799] |  |  | 40 | 5 | 7ab9b903 |
| test2 | start_points | overall | rmse_h100 | lgbm | 2.032 [1.794, 2.265] |  |  | 40 | 5 | c867ad3f |
| test2 | start_points | overall | rmse_h100 | lstm[lookback=128] | 1.269 [1.138, 1.397] |  |  | 40 | 5 | 3bc20cea |
| test2 | start_points | overall | rmse_h100 | patchtst[lookback=128] | 2.296 [2.102, 2.508] |  |  | 40 | 5 | 1a28f12a |
| test2 | start_points | overall | rmse_h100 | transformer[lookback=32] | 2.004 [1.823, 2.173] |  |  | 40 | 5 | a3e9d648 |
| test2 | start_points | overall | rmse_h200 | age_only | 3.904 [3.817, 3.990] |  |  | 40 | 5 | 7d094294 |
| test2 | start_points | overall | rmse_h200 | elasticnet | 1.959 [1.726, 2.214] |  |  | 40 | 5 | 910f2d53 |
| test2 | start_points | overall | rmse_h200 | itransformer[lookback=32] | 3.741 [3.234, 4.257] |  |  | 40 | 5 | 7ab9b903 |
| test2 | start_points | overall | rmse_h200 | lgbm | 2.002 [1.783, 2.225] |  |  | 40 | 5 | c867ad3f |
| test2 | start_points | overall | rmse_h200 | lstm[lookback=128] | 1.835 [1.606, 2.073] |  |  | 40 | 5 | 3bc20cea |
| test2 | start_points | overall | rmse_h200 | patchtst[lookback=128] | 3.588 [3.275, 3.897] |  |  | 40 | 5 | 1a28f12a |
| test2 | start_points | overall | rmse_h200 | transformer[lookback=32] | 2.515 [2.217, 2.813] |  |  | 40 | 5 | a3e9d648 |
| test2 | start_points | overall | rmse_h50 | age_only | 3.594 [3.411, 3.767] |  |  | 40 | 5 | 7d094294 |
| test2 | start_points | overall | rmse_h50 | elasticnet | 1.851 [1.659, 2.038] |  |  | 40 | 5 | 910f2d53 |
| test2 | start_points | overall | rmse_h50 | itransformer[lookback=32] | 1.827 [1.642, 2.014] |  |  | 40 | 5 | 7ab9b903 |
| test2 | start_points | overall | rmse_h50 | lgbm | 1.719 [1.493, 1.936] |  |  | 40 | 5 | c867ad3f |
| test2 | start_points | overall | rmse_h50 | lstm[lookback=128] | 1.049 [0.928, 1.169] |  |  | 40 | 5 | 3bc20cea |
| test2 | start_points | overall | rmse_h50 | patchtst[lookback=128] | 1.599 [1.401, 1.831] |  |  | 40 | 5 | 1a28f12a |
| test2 | start_points | overall | rmse_h50 | transformer[lookback=32] | 1.370 [1.230, 1.506] |  |  | 40 | 5 | a3e9d648 |

</details>

<details><summary>toyota_rul (210 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rul_bias | age_only | 41.880 [-53.785, 126.823] |  |  | 43 | 5 | 576359ba |
| test1 | all | overall | rul_bias | elasticnet | -14.721 [-45.661, 11.157] |  |  | 43 | 5 | e50c3707 |
| test1 | all | overall | rul_bias | itransformer[lookback=32] | -7.245 [-25.956, 9.842] |  |  | 43 | 5 | b27d640a |
| test1 | all | overall | rul_bias | lgbm | -14.206 [-33.572, 2.650] |  |  | 43 | 5 | baa7bf55 |
| test1 | all | overall | rul_bias | lstm[lookback=128] | -6.048 [-24.409, 12.473] |  |  | 43 | 5 | 47f91b8d |
| test1 | all | overall | rul_bias | patchtst[lookback=128] | -7.923 [-43.262, 21.803] |  |  | 43 | 5 | 67ad156f |
| test1 | all | overall | rul_bias | transformer[lookback=32] | -5.874 [-25.031, 12.664] |  |  | 43 | 5 | 24fcd90b |
| test1 | all | overall | rul_mae | age_only | 236.073 [183.453, 298.130] |  |  | 43 | 5 | 576359ba |
| test1 | all | overall | rul_mae | elasticnet | 79.739 [58.521, 105.986] |  |  | 43 | 5 | e50c3707 |
| test1 | all | overall | rul_mae | itransformer[lookback=32] | 55.774 [44.839, 68.935] |  |  | 43 | 5 | b27d640a |
| test1 | all | overall | rul_mae | lgbm | 51.187 [38.059, 66.581] |  |  | 43 | 5 | baa7bf55 |
| test1 | all | overall | rul_mae | lstm[lookback=128] | 54.431 [42.184, 67.652] |  |  | 43 | 5 | 47f91b8d |
| test1 | all | overall | rul_mae | patchtst[lookback=128] | 99.480 [77.405, 127.415] |  |  | 43 | 5 | 67ad156f |
| test1 | all | overall | rul_mae | transformer[lookback=32] | 58.697 [44.806, 74.348] |  |  | 43 | 5 | 24fcd90b |
| test1 | start_points | fixed:100 | rul_bias | age_only | 9.721 [-116.467, 116.674] |  |  | 43 | 5 | 576359ba |
| test1 | start_points | fixed:100 | rul_bias | elasticnet | -47.264 [-135.605, 29.167] |  |  | 43 | 5 | e50c3707 |
| test1 | start_points | fixed:100 | rul_bias | itransformer[lookback=32] | -44.548 [-89.535, -5.411] |  |  | 43 | 5 | b27d640a |
| test1 | start_points | fixed:100 | rul_bias | lgbm | -48.279 [-99.684, -5.503] |  |  | 43 | 5 | baa7bf55 |
| test1 | start_points | fixed:100 | rul_bias | lstm[lookback=128] | -27.149 [-69.420, 12.683] |  |  | 43 | 5 | 47f91b8d |
| test1 | start_points | fixed:100 | rul_bias | patchtst[lookback=128] | -11.455 [-79.319, 47.193] |  |  | 43 | 5 | 67ad156f |
| test1 | start_points | fixed:100 | rul_bias | transformer[lookback=32] | -38.828 [-97.602, 13.048] |  |  | 43 | 5 | 24fcd90b |
| test1 | start_points | fixed:100 | rul_mae | age_only | 268.233 [193.837, 361.187] |  |  | 43 | 5 | 576359ba |
| test1 | start_points | fixed:100 | rul_mae | elasticnet | 174.582 [117.721, 245.998] |  |  | 43 | 5 | e50c3707 |
| test1 | start_points | fixed:100 | rul_mae | itransformer[lookback=32] | 99.708 [70.268, 135.391] |  |  | 43 | 5 | b27d640a |
| test1 | start_points | fixed:100 | rul_mae | lgbm | 101.711 [67.998, 144.862] |  |  | 43 | 5 | baa7bf55 |
| test1 | start_points | fixed:100 | rul_mae | lstm[lookback=128] | 98.051 [69.864, 129.538] |  |  | 43 | 5 | 47f91b8d |
| test1 | start_points | fixed:100 | rul_mae | patchtst[lookback=128] | 152.557 [113.184, 202.640] |  |  | 43 | 5 | 67ad156f |
| test1 | start_points | fixed:100 | rul_mae | transformer[lookback=32] | 121.127 [81.523, 168.595] |  |  | 43 | 5 | 24fcd90b |
| test1 | start_points | frac:0.3 | alpha_lambda_acc | age_only | 0.163 [0.070, 0.279] |  |  | 43 | 5 | 576359ba |
| test1 | start_points | frac:0.3 | alpha_lambda_acc | elasticnet | 0.512 [0.372, 0.674] |  |  | 43 | 5 | e50c3707 |
| test1 | start_points | frac:0.3 | alpha_lambda_acc | itransformer[lookback=32] | 0.777 [0.670, 0.874] |  |  | 43 | 5 | b27d640a |
| test1 | start_points | frac:0.3 | alpha_lambda_acc | lgbm | 0.814 [0.698, 0.930] |  |  | 43 | 5 | baa7bf55 |
| test1 | start_points | frac:0.3 | alpha_lambda_acc | lstm[lookback=128] | 0.744 [0.623, 0.856] |  |  | 43 | 5 | 47f91b8d |
| test1 | start_points | frac:0.3 | alpha_lambda_acc | patchtst[lookback=128] | 0.442 [0.335, 0.549] |  |  | 43 | 5 | 67ad156f |
| test1 | start_points | frac:0.3 | alpha_lambda_acc | transformer[lookback=32] | 0.698 [0.572, 0.819] |  |  | 43 | 5 | 24fcd90b |
| test1 | start_points | frac:0.3 | rul_bias | age_only | 9.721 [-116.467, 116.674] |  |  | 43 | 5 | 576359ba |
| test1 | start_points | frac:0.3 | rul_bias | elasticnet | -19.202 [-74.687, 28.461] |  |  | 43 | 5 | e50c3707 |
| test1 | start_points | frac:0.3 | rul_bias | itransformer[lookback=32] | -15.591 [-46.414, 11.816] |  |  | 43 | 5 | b27d640a |
| test1 | start_points | frac:0.3 | rul_bias | lgbm | -26.081 [-57.003, 1.233] |  |  | 43 | 5 | baa7bf55 |
| test1 | start_points | frac:0.3 | rul_bias | lstm[lookback=128] | -19.346 [-49.333, 9.368] |  |  | 43 | 5 | 47f91b8d |
| test1 | start_points | frac:0.3 | rul_bias | patchtst[lookback=128] | -19.056 [-79.891, 34.817] |  |  | 43 | 5 | 67ad156f |
| test1 | start_points | frac:0.3 | rul_bias | transformer[lookback=32] | -11.075 [-44.625, 19.846] |  |  | 43 | 5 | 24fcd90b |
| test1 | start_points | frac:0.3 | rul_mae | age_only | 268.233 [193.837, 361.187] |  |  | 43 | 5 | 576359ba |
| test1 | start_points | frac:0.3 | rul_mae | elasticnet | 112.621 [77.644, 155.323] |  |  | 43 | 5 | e50c3707 |
| test1 | start_points | frac:0.3 | rul_mae | itransformer[lookback=32] | 71.983 [53.313, 94.046] |  |  | 43 | 5 | b27d640a |
| test1 | start_points | frac:0.3 | rul_mae | lgbm | 66.800 [45.666, 90.931] |  |  | 43 | 5 | baa7bf55 |
| test1 | start_points | frac:0.3 | rul_mae | lstm[lookback=128] | 73.484 [53.811, 94.832] |  |  | 43 | 5 | 47f91b8d |
| test1 | start_points | frac:0.3 | rul_mae | patchtst[lookback=128] | 138.190 [102.732, 181.467] |  |  | 43 | 5 | 67ad156f |
| test1 | start_points | frac:0.3 | rul_mae | transformer[lookback=32] | 78.954 [58.270, 102.087] |  |  | 43 | 5 | 24fcd90b |
| test1 | start_points | frac:0.5 | alpha_lambda_acc | age_only | 0.093 [0.023, 0.186] |  |  | 43 | 5 | 576359ba |
| test1 | start_points | frac:0.5 | alpha_lambda_acc | elasticnet | 0.674 [0.535, 0.814] |  |  | 43 | 5 | e50c3707 |
| test1 | start_points | frac:0.5 | alpha_lambda_acc | itransformer[lookback=32] | 0.744 [0.628, 0.851] |  |  | 43 | 5 | b27d640a |
| test1 | start_points | frac:0.5 | alpha_lambda_acc | lgbm | 0.791 [0.651, 0.907] |  |  | 43 | 5 | baa7bf55 |
| test1 | start_points | frac:0.5 | alpha_lambda_acc | lstm[lookback=128] | 0.781 [0.684, 0.865] |  |  | 43 | 5 | 47f91b8d |
| test1 | start_points | frac:0.5 | alpha_lambda_acc | patchtst[lookback=128] | 0.581 [0.484, 0.674] |  |  | 43 | 5 | 67ad156f |
| test1 | start_points | frac:0.5 | alpha_lambda_acc | transformer[lookback=32] | 0.860 [0.763, 0.944] |  |  | 43 | 5 | 24fcd90b |
| test1 | start_points | frac:0.5 | rul_bias | age_only | 26.953 [-78.494, 120.279] |  |  | 43 | 5 | 576359ba |
| test1 | start_points | frac:0.5 | rul_bias | elasticnet | -28.759 [-55.857, -4.059] |  |  | 43 | 5 | e50c3707 |
| test1 | start_points | frac:0.5 | rul_bias | itransformer[lookback=32] | -14.335 [-34.400, 4.857] |  |  | 43 | 5 | b27d640a |
| test1 | start_points | frac:0.5 | rul_bias | lgbm | -17.671 [-33.109, -3.287] |  |  | 43 | 5 | baa7bf55 |
| test1 | start_points | frac:0.5 | rul_bias | lstm[lookback=128] | -11.266 [-29.910, 8.319] |  |  | 43 | 5 | 47f91b8d |
| test1 | start_points | frac:0.5 | rul_bias | patchtst[lookback=128] | -17.188 [-47.900, 10.319] |  |  | 43 | 5 | 67ad156f |
| test1 | start_points | frac:0.5 | rul_bias | transformer[lookback=32] | -12.810 [-29.925, 4.243] |  |  | 43 | 5 | 24fcd90b |
| test1 | start_points | frac:0.5 | rul_mae | age_only | 251.000 [191.299, 322.307] |  |  | 43 | 5 | 576359ba |
| test1 | start_points | frac:0.5 | rul_mae | elasticnet | 65.915 [47.968, 86.295] |  |  | 43 | 5 | e50c3707 |
| test1 | start_points | frac:0.5 | rul_mae | itransformer[lookback=32] | 52.082 [39.805, 65.819] |  |  | 43 | 5 | b27d640a |
| test1 | start_points | frac:0.5 | rul_mae | lgbm | 38.014 [27.461, 49.215] |  |  | 43 | 5 | baa7bf55 |
| test1 | start_points | frac:0.5 | rul_mae | lstm[lookback=128] | 48.808 [36.763, 62.405] |  |  | 43 | 5 | 47f91b8d |
| test1 | start_points | frac:0.5 | rul_mae | patchtst[lookback=128] | 75.895 [57.324, 97.515] |  |  | 43 | 5 | 67ad156f |
| test1 | start_points | frac:0.5 | rul_mae | transformer[lookback=32] | 43.229 [31.824, 56.446] |  |  | 43 | 5 | 24fcd90b |
| test1 | start_points | frac:0.7 | alpha_lambda_acc | age_only | 0.093 [0.023, 0.186] |  |  | 43 | 5 | 576359ba |
| test1 | start_points | frac:0.7 | alpha_lambda_acc | elasticnet | 0.628 [0.488, 0.767] |  |  | 43 | 5 | e50c3707 |
| test1 | start_points | frac:0.7 | alpha_lambda_acc | itransformer[lookback=32] | 0.735 [0.609, 0.842] |  |  | 43 | 5 | b27d640a |
| test1 | start_points | frac:0.7 | alpha_lambda_acc | lgbm | 0.767 [0.628, 0.884] |  |  | 43 | 5 | baa7bf55 |
| test1 | start_points | frac:0.7 | alpha_lambda_acc | lstm[lookback=128] | 0.740 [0.633, 0.837] |  |  | 43 | 5 | 47f91b8d |
| test1 | start_points | frac:0.7 | alpha_lambda_acc | patchtst[lookback=128] | 0.321 [0.233, 0.414] |  |  | 43 | 5 | 67ad156f |
| test1 | start_points | frac:0.7 | alpha_lambda_acc | transformer[lookback=32] | 0.758 [0.632, 0.874] |  |  | 43 | 5 | 24fcd90b |
| test1 | start_points | frac:0.7 | rul_bias | age_only | 54.767 [-25.699, 129.628] |  |  | 43 | 5 | 576359ba |
| test1 | start_points | frac:0.7 | rul_bias | elasticnet | 6.228 [-10.972, 22.036] |  |  | 43 | 5 | e50c3707 |
| test1 | start_points | frac:0.7 | rul_bias | itransformer[lookback=32] | 5.144 [-9.965, 19.810] |  |  | 43 | 5 | b27d640a |
| test1 | start_points | frac:0.7 | rul_bias | lgbm | 8.183 [-4.501, 19.988] |  |  | 43 | 5 | baa7bf55 |
| test1 | start_points | frac:0.7 | rul_bias | lstm[lookback=128] | 13.415 [2.151, 26.293] |  |  | 43 | 5 | 47f91b8d |
| test1 | start_points | frac:0.7 | rul_bias | patchtst[lookback=128] | 5.233 [-16.852, 27.826] |  |  | 43 | 5 | 67ad156f |
| test1 | start_points | frac:0.7 | rul_bias | transformer[lookback=32] | 14.705 [1.577, 29.108] |  |  | 43 | 5 | 24fcd90b |
| test1 | start_points | frac:0.7 | rul_mae | age_only | 223.186 [182.767, 267.213] |  |  | 43 | 5 | 576359ba |
| test1 | start_points | frac:0.7 | rul_mae | elasticnet | 40.275 [29.506, 53.212] |  |  | 43 | 5 | e50c3707 |
| test1 | start_points | frac:0.7 | rul_mae | itransformer[lookback=32] | 33.807 [23.875, 45.569] |  |  | 43 | 5 | b27d640a |
| test1 | start_points | frac:0.7 | rul_mae | lgbm | 28.539 [20.220, 38.604] |  |  | 43 | 5 | baa7bf55 |
| test1 | start_points | frac:0.7 | rul_mae | lstm[lookback=128] | 29.812 [21.313, 40.278] |  |  | 43 | 5 | 47f91b8d |
| test1 | start_points | frac:0.7 | rul_mae | patchtst[lookback=128] | 67.641 [56.573, 79.839] |  |  | 43 | 5 | 67ad156f |
| test1 | start_points | frac:0.7 | rul_mae | transformer[lookback=32] | 32.771 [22.957, 44.240] |  |  | 43 | 5 | 24fcd90b |
| test1 | start_points | overall | rul_bias | age_only | 25.291 [-82.925, 120.471] |  |  | 43 | 5 | 576359ba |
| test1 | start_points | overall | rul_bias | elasticnet | -22.249 [-64.730, 13.110] |  |  | 43 | 5 | e50c3707 |
| test1 | start_points | overall | rul_bias | itransformer[lookback=32] | -17.333 [-42.353, 4.907] |  |  | 43 | 5 | b27d640a |
| test1 | start_points | overall | rul_bias | lgbm | -20.962 [-44.536, -0.863] |  |  | 43 | 5 | baa7bf55 |
| test1 | start_points | overall | rul_bias | lstm[lookback=128] | -11.086 [-33.142, 10.679] |  |  | 43 | 5 | 47f91b8d |
| test1 | start_points | overall | rul_bias | patchtst[lookback=128] | -10.616 [-49.677, 23.633] |  |  | 43 | 5 | 67ad156f |
| test1 | start_points | overall | rul_bias | transformer[lookback=32] | -12.002 [-35.606, 10.089] |  |  | 43 | 5 | 24fcd90b |
| test1 | start_points | overall | rul_mae | age_only | 252.663 [191.340, 327.323] |  |  | 43 | 5 | 576359ba |
| test1 | start_points | overall | rul_mae | elasticnet | 98.348 [70.593, 132.509] |  |  | 43 | 5 | e50c3707 |
| test1 | start_points | overall | rul_mae | itransformer[lookback=32] | 64.395 [49.131, 82.910] |  |  | 43 | 5 | b27d640a |
| test1 | start_points | overall | rul_mae | lgbm | 58.766 [42.670, 77.927] |  |  | 43 | 5 | baa7bf55 |
| test1 | start_points | overall | rul_mae | lstm[lookback=128] | 62.539 [47.900, 78.254] |  |  | 43 | 5 | 47f91b8d |
| test1 | start_points | overall | rul_mae | patchtst[lookback=128] | 108.571 [86.032, 135.270] |  |  | 43 | 5 | 67ad156f |
| test1 | start_points | overall | rul_mae | transformer[lookback=32] | 69.020 [51.221, 89.011] |  |  | 43 | 5 | 24fcd90b |
| test2 | all | overall | rul_bias | age_only | -247.929 [-315.555, -184.557] |  |  | 40 | 5 | 576359ba |
| test2 | all | overall | rul_bias | elasticnet | -63.732 [-106.005, -26.213] |  |  | 40 | 5 | e50c3707 |
| test2 | all | overall | rul_bias | itransformer[lookback=32] | -97.262 [-144.405, -52.891] |  |  | 40 | 5 | b27d640a |
| test2 | all | overall | rul_bias | lgbm | -24.654 [-65.064, 10.465] |  |  | 40 | 5 | baa7bf55 |
| test2 | all | overall | rul_bias | lstm[lookback=128] | -63.433 [-109.214, -16.079] |  |  | 40 | 5 | 47f91b8d |
| test2 | all | overall | rul_bias | patchtst[lookback=128] | -219.215 [-265.666, -177.419] |  |  | 40 | 5 | 67ad156f |
| test2 | all | overall | rul_bias | transformer[lookback=32] | -123.384 [-167.264, -83.106] |  |  | 40 | 5 | 24fcd90b |
| test2 | all | overall | rul_mae | age_only | 259.429 [201.101, 324.658] |  |  | 40 | 5 | 576359ba |
| test2 | all | overall | rul_mae | elasticnet | 124.898 [95.315, 159.474] |  |  | 40 | 5 | e50c3707 |
| test2 | all | overall | rul_mae | itransformer[lookback=32] | 145.854 [113.607, 182.338] |  |  | 40 | 5 | b27d640a |
| test2 | all | overall | rul_mae | lgbm | 153.228 [125.299, 185.710] |  |  | 40 | 5 | baa7bf55 |
| test2 | all | overall | rul_mae | lstm[lookback=128] | 156.332 [127.005, 189.367] |  |  | 40 | 5 | 47f91b8d |
| test2 | all | overall | rul_mae | patchtst[lookback=128] | 245.471 [205.506, 290.332] |  |  | 40 | 5 | 67ad156f |
| test2 | all | overall | rul_mae | transformer[lookback=32] | 161.539 [127.163, 200.671] |  |  | 40 | 5 | 24fcd90b |
| test2 | start_points | fixed:100 | rul_bias | age_only | -313.000 [-410.929, -223.671] |  |  | 40 | 5 | 576359ba |
| test2 | start_points | fixed:100 | rul_bias | elasticnet | -231.942 [-322.701, -153.398] |  |  | 40 | 5 | e50c3707 |
| test2 | start_points | fixed:100 | rul_bias | itransformer[lookback=32] | -211.768 [-303.570, -125.364] |  |  | 40 | 5 | b27d640a |
| test2 | start_points | fixed:100 | rul_bias | lgbm | -273.554 [-371.284, -186.721] |  |  | 40 | 5 | baa7bf55 |
| test2 | start_points | fixed:100 | rul_bias | lstm[lookback=128] | -98.748 [-201.355, 9.020] |  |  | 40 | 5 | 47f91b8d |
| test2 | start_points | fixed:100 | rul_bias | patchtst[lookback=128] | -361.406 [-455.647, -278.609] |  |  | 40 | 5 | 67ad156f |
| test2 | start_points | fixed:100 | rul_bias | transformer[lookback=32] | -270.112 [-359.889, -187.614] |  |  | 40 | 5 | 24fcd90b |
| test2 | start_points | fixed:100 | rul_mae | age_only | 324.500 [240.124, 420.676] |  |  | 40 | 5 | 576359ba |
| test2 | start_points | fixed:100 | rul_mae | elasticnet | 243.248 [167.526, 330.559] |  |  | 40 | 5 | e50c3707 |
| test2 | start_points | fixed:100 | rul_mae | itransformer[lookback=32] | 261.365 [190.408, 340.539] |  |  | 40 | 5 | b27d640a |
| test2 | start_points | fixed:100 | rul_mae | lgbm | 279.603 [194.506, 375.610] |  |  | 40 | 5 | baa7bf55 |
| test2 | start_points | fixed:100 | rul_mae | lstm[lookback=128] | 288.312 [224.887, 358.108] |  |  | 40 | 5 | 47f91b8d |
| test2 | start_points | fixed:100 | rul_mae | patchtst[lookback=128] | 361.418 [278.621, 455.648] |  |  | 40 | 5 | 67ad156f |
| test2 | start_points | fixed:100 | rul_mae | transformer[lookback=32] | 284.976 [208.010, 371.405] |  |  | 40 | 5 | 24fcd90b |
| test2 | start_points | frac:0.3 | alpha_lambda_acc | age_only | 0.275 [0.150, 0.425] |  |  | 40 | 5 | 576359ba |
| test2 | start_points | frac:0.3 | alpha_lambda_acc | elasticnet | 0.550 [0.400, 0.700] |  |  | 40 | 5 | e50c3707 |
| test2 | start_points | frac:0.3 | alpha_lambda_acc | itransformer[lookback=32] | 0.360 [0.230, 0.495] |  |  | 40 | 5 | b27d640a |
| test2 | start_points | frac:0.3 | alpha_lambda_acc | lgbm | 0.650 [0.500, 0.800] |  |  | 40 | 5 | baa7bf55 |
| test2 | start_points | frac:0.3 | alpha_lambda_acc | lstm[lookback=128] | 0.450 [0.310, 0.595] |  |  | 40 | 5 | 47f91b8d |
| test2 | start_points | frac:0.3 | alpha_lambda_acc | patchtst[lookback=128] | 0.025 [0.005, 0.055] |  |  | 40 | 5 | 67ad156f |
| test2 | start_points | frac:0.3 | alpha_lambda_acc | transformer[lookback=32] | 0.305 [0.195, 0.420] |  |  | 40 | 5 | 24fcd90b |
| test2 | start_points | frac:0.3 | rul_bias | age_only | -313.000 [-410.929, -223.671] |  |  | 40 | 5 | 576359ba |
| test2 | start_points | frac:0.3 | rul_bias | elasticnet | -135.929 [-202.930, -76.630] |  |  | 40 | 5 | e50c3707 |
| test2 | start_points | frac:0.3 | rul_bias | itransformer[lookback=32] | -191.459 [-253.604, -131.908] |  |  | 40 | 5 | b27d640a |
| test2 | start_points | frac:0.3 | rul_bias | lgbm | -98.204 [-165.201, -39.617] |  |  | 40 | 5 | baa7bf55 |
| test2 | start_points | frac:0.3 | rul_bias | lstm[lookback=128] | -147.567 [-225.053, -63.683] |  |  | 40 | 5 | 47f91b8d |
| test2 | start_points | frac:0.3 | rul_bias | patchtst[lookback=128] | -417.802 [-492.248, -349.582] |  |  | 40 | 5 | 67ad156f |
| test2 | start_points | frac:0.3 | rul_bias | transformer[lookback=32] | -224.279 [-292.263, -160.961] |  |  | 40 | 5 | 24fcd90b |
| test2 | start_points | frac:0.3 | rul_mae | age_only | 324.500 [240.124, 420.676] |  |  | 40 | 5 | 576359ba |
| test2 | start_points | frac:0.3 | rul_mae | elasticnet | 166.302 [114.638, 226.323] |  |  | 40 | 5 | e50c3707 |
| test2 | start_points | frac:0.3 | rul_mae | itransformer[lookback=32] | 214.098 [163.783, 268.688] |  |  | 40 | 5 | b27d640a |
| test2 | start_points | frac:0.3 | rul_mae | lgbm | 141.274 [90.330, 200.431] |  |  | 40 | 5 | baa7bf55 |
| test2 | start_points | frac:0.3 | rul_mae | lstm[lookback=128] | 215.535 [154.730, 284.773] |  |  | 40 | 5 | 47f91b8d |
| test2 | start_points | frac:0.3 | rul_mae | patchtst[lookback=128] | 417.802 [349.582, 492.248] |  |  | 40 | 5 | 67ad156f |
| test2 | start_points | frac:0.3 | rul_mae | transformer[lookback=32] | 238.710 [181.999, 302.379] |  |  | 40 | 5 | 24fcd90b |
| test2 | start_points | frac:0.5 | alpha_lambda_acc | age_only | 0.125 [0.025, 0.225] |  |  | 40 | 5 | 576359ba |
| test2 | start_points | frac:0.5 | alpha_lambda_acc | elasticnet | 0.575 [0.425, 0.725] |  |  | 40 | 5 | e50c3707 |
| test2 | start_points | frac:0.5 | alpha_lambda_acc | itransformer[lookback=32] | 0.365 [0.245, 0.490] |  |  | 40 | 5 | b27d640a |
| test2 | start_points | frac:0.5 | alpha_lambda_acc | lgbm | 0.625 [0.475, 0.775] |  |  | 40 | 5 | baa7bf55 |
| test2 | start_points | frac:0.5 | alpha_lambda_acc | lstm[lookback=128] | 0.420 [0.290, 0.550] |  |  | 40 | 5 | 47f91b8d |
| test2 | start_points | frac:0.5 | alpha_lambda_acc | patchtst[lookback=128] | 0.065 [0.015, 0.130] |  |  | 40 | 5 | 67ad156f |
| test2 | start_points | frac:0.5 | alpha_lambda_acc | transformer[lookback=32] | 0.245 [0.145, 0.355] |  |  | 40 | 5 | 24fcd90b |
| test2 | start_points | frac:0.5 | rul_bias | age_only | -294.775 [-376.656, -217.621] |  |  | 40 | 5 | 576359ba |
| test2 | start_points | frac:0.5 | rul_bias | elasticnet | -67.754 [-109.477, -29.621] |  |  | 40 | 5 | e50c3707 |
| test2 | start_points | frac:0.5 | rul_bias | itransformer[lookback=32] | -133.175 [-181.057, -87.754] |  |  | 40 | 5 | b27d640a |
| test2 | start_points | frac:0.5 | rul_bias | lgbm | 19.179 [-21.132, 56.300] |  |  | 40 | 5 | baa7bf55 |
| test2 | start_points | frac:0.5 | rul_bias | lstm[lookback=128] | -105.438 [-144.082, -67.334] |  |  | 40 | 5 | 47f91b8d |
| test2 | start_points | frac:0.5 | rul_bias | patchtst[lookback=128] | -254.765 [-300.577, -212.131] |  |  | 40 | 5 | 67ad156f |
| test2 | start_points | frac:0.5 | rul_bias | transformer[lookback=32] | -150.827 [-191.776, -112.798] |  |  | 40 | 5 | 24fcd90b |
| test2 | start_points | frac:0.5 | rul_mae | age_only | 306.275 [234.249, 385.529] |  |  | 40 | 5 | 576359ba |
| test2 | start_points | frac:0.5 | rul_mae | elasticnet | 102.442 [72.754, 136.641] |  |  | 40 | 5 | e50c3707 |
| test2 | start_points | frac:0.5 | rul_mae | itransformer[lookback=32] | 156.773 [119.567, 198.453] |  |  | 40 | 5 | b27d640a |
| test2 | start_points | frac:0.5 | rul_mae | lgbm | 92.145 [66.865, 120.217] |  |  | 40 | 5 | baa7bf55 |
| test2 | start_points | frac:0.5 | rul_mae | lstm[lookback=128] | 129.961 [100.848, 161.729] |  |  | 40 | 5 | 47f91b8d |
| test2 | start_points | frac:0.5 | rul_mae | patchtst[lookback=128] | 254.847 [212.268, 300.620] |  |  | 40 | 5 | 67ad156f |
| test2 | start_points | frac:0.5 | rul_mae | transformer[lookback=32] | 160.367 [126.681, 198.120] |  |  | 40 | 5 | 24fcd90b |
| test2 | start_points | frac:0.7 | alpha_lambda_acc | age_only | 0.025 [0.000, 0.075] |  |  | 40 | 5 | 576359ba |
| test2 | start_points | frac:0.7 | alpha_lambda_acc | elasticnet | 0.550 [0.400, 0.700] |  |  | 40 | 5 | e50c3707 |
| test2 | start_points | frac:0.7 | alpha_lambda_acc | itransformer[lookback=32] | 0.655 [0.525, 0.775] |  |  | 40 | 5 | b27d640a |
| test2 | start_points | frac:0.7 | alpha_lambda_acc | lgbm | 0.250 [0.125, 0.375] |  |  | 40 | 5 | baa7bf55 |
| test2 | start_points | frac:0.7 | alpha_lambda_acc | lstm[lookback=128] | 0.480 [0.380, 0.585] |  |  | 40 | 5 | 47f91b8d |
| test2 | start_points | frac:0.7 | alpha_lambda_acc | patchtst[lookback=128] | 0.310 [0.220, 0.410] |  |  | 40 | 5 | 67ad156f |
| test2 | start_points | frac:0.7 | alpha_lambda_acc | transformer[lookback=32] | 0.600 [0.485, 0.710] |  |  | 40 | 5 | 24fcd90b |
| test2 | start_points | frac:0.7 | rul_bias | age_only | -235.550 [-285.353, -185.050] |  |  | 40 | 5 | 576359ba |
| test2 | start_points | frac:0.7 | rul_bias | elasticnet | 44.790 [23.839, 65.649] |  |  | 40 | 5 | e50c3707 |
| test2 | start_points | frac:0.7 | rul_bias | itransformer[lookback=32] | -17.845 [-41.507, 5.760] |  |  | 40 | 5 | b27d640a |
| test2 | start_points | frac:0.7 | rul_bias | lgbm | 91.319 [73.385, 109.103] |  |  | 40 | 5 | baa7bf55 |
| test2 | start_points | frac:0.7 | rul_bias | lstm[lookback=128] | -7.792 [-30.720, 15.743] |  |  | 40 | 5 | 47f91b8d |
| test2 | start_points | frac:0.7 | rul_bias | patchtst[lookback=128] | -81.334 [-109.397, -53.108] |  |  | 40 | 5 | 67ad156f |
| test2 | start_points | frac:0.7 | rul_bias | transformer[lookback=32] | -33.464 [-54.415, -13.177] |  |  | 40 | 5 | 24fcd90b |
| test2 | start_points | frac:0.7 | rul_mae | age_only | 247.050 [203.099, 292.501] |  |  | 40 | 5 | 576359ba |
| test2 | start_points | frac:0.7 | rul_mae | elasticnet | 63.966 [49.034, 79.552] |  |  | 40 | 5 | e50c3707 |
| test2 | start_points | frac:0.7 | rul_mae | itransformer[lookback=32] | 59.671 [44.405, 76.344] |  |  | 40 | 5 | b27d640a |
| test2 | start_points | frac:0.7 | rul_mae | lgbm | 95.230 [79.651, 111.251] |  |  | 40 | 5 | baa7bf55 |
| test2 | start_points | frac:0.7 | rul_mae | lstm[lookback=128] | 68.912 [58.180, 80.558] |  |  | 40 | 5 | 47f91b8d |
| test2 | start_points | frac:0.7 | rul_mae | patchtst[lookback=128] | 106.873 [88.556, 126.980] |  |  | 40 | 5 | 67ad156f |
| test2 | start_points | frac:0.7 | rul_mae | transformer[lookback=32] | 59.066 [45.677, 74.346] |  |  | 40 | 5 | 24fcd90b |
| test2 | start_points | overall | rul_bias | age_only | -289.081 [-370.032, -213.002] |  |  | 40 | 5 | 576359ba |
| test2 | start_points | overall | rul_bias | elasticnet | -97.709 [-151.522, -50.011] |  |  | 40 | 5 | e50c3707 |
| test2 | start_points | overall | rul_bias | itransformer[lookback=32] | -138.562 [-193.554, -87.155] |  |  | 40 | 5 | b27d640a |
| test2 | start_points | overall | rul_bias | lgbm | -65.315 [-117.104, -19.578] |  |  | 40 | 5 | baa7bf55 |
| test2 | start_points | overall | rul_bias | lstm[lookback=128] | -89.886 [-146.121, -31.071] |  |  | 40 | 5 | 47f91b8d |
| test2 | start_points | overall | rul_bias | patchtst[lookback=128] | -278.827 [-332.744, -230.625] |  |  | 40 | 5 | 67ad156f |
| test2 | start_points | overall | rul_bias | transformer[lookback=32] | -169.671 [-224.244, -119.462] |  |  | 40 | 5 | 24fcd90b |
| test2 | start_points | overall | rul_mae | age_only | 300.581 [229.922, 379.256] |  |  | 40 | 5 | 576359ba |
| test2 | start_points | overall | rul_mae | elasticnet | 143.990 [105.595, 189.483] |  |  | 40 | 5 | e50c3707 |
| test2 | start_points | overall | rul_mae | itransformer[lookback=32] | 172.977 [131.696, 218.394] |  |  | 40 | 5 | b27d640a |
| test2 | start_points | overall | rul_mae | lgbm | 152.063 [116.871, 192.907] |  |  | 40 | 5 | baa7bf55 |
| test2 | start_points | overall | rul_mae | lstm[lookback=128] | 175.680 [139.591, 215.968] |  |  | 40 | 5 | 47f91b8d |
| test2 | start_points | overall | rul_mae | patchtst[lookback=128] | 285.235 [236.635, 340.083] |  |  | 40 | 5 | 67ad156f |
| test2 | start_points | overall | rul_mae | transformer[lookback=32] | 185.780 [141.719, 236.248] |  |  | 40 | 5 | 24fcd90b |

</details>

<details><summary>toyota_soh (84 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rmse | age_only | 4.008 [3.665, 4.471] |  |  | 43 | 5 | cd1211f0 |
| test1 | all | overall | rmse | elasticnet | 1.181 [0.963, 1.458] |  |  | 43 | 5 | 1f049d74 |
| test1 | all | overall | rmse | itransformer[lookback=128] | 1.061 [0.814, 1.391] |  |  | 43 | 5 | f6b438b9 |
| test1 | all | overall | rmse | lgbm | 0.947 [0.750, 1.225] |  |  | 43 | 5 | 7345cc3d |
| test1 | all | overall | rmse | lstm[lookback=32] | 1.074 [0.796, 1.434] |  |  | 43 | 5 | 3ad2c3cb |
| test1 | all | overall | rmse | patchtst[lookback=128] | 1.643 [1.458, 1.854] |  |  | 43 | 5 | 271523a9 |
| test1 | all | overall | rmse | transformer[lookback=32] | 0.907 [0.621, 1.266] |  |  | 43 | 5 | e1e42381 |
| test1 | start_points | fixed:100 | rmse | age_only | 0.567 [0.284, 1.052] |  |  | 43 | 5 | cd1211f0 |
| test1 | start_points | fixed:100 | rmse | elasticnet | 0.690 [0.512, 0.913] |  |  | 43 | 5 | 1f049d74 |
| test1 | start_points | fixed:100 | rmse | itransformer[lookback=128] | 0.631 [0.432, 0.939] |  |  | 43 | 5 | f6b438b9 |
| test1 | start_points | fixed:100 | rmse | lgbm | 0.357 [0.208, 0.584] |  |  | 43 | 5 | 7345cc3d |
| test1 | start_points | fixed:100 | rmse | lstm[lookback=32] | 0.509 [0.358, 0.722] |  |  | 43 | 5 | 3ad2c3cb |
| test1 | start_points | fixed:100 | rmse | patchtst[lookback=128] | 0.807 [0.622, 1.021] |  |  | 43 | 5 | 271523a9 |
| test1 | start_points | fixed:100 | rmse | transformer[lookback=32] | 0.343 [0.195, 0.592] |  |  | 43 | 5 | e1e42381 |
| test1 | start_points | frac:0.3 | rmse | age_only | 1.299 [0.894, 1.783] |  |  | 43 | 5 | cd1211f0 |
| test1 | start_points | frac:0.3 | rmse | elasticnet | 0.567 [0.434, 0.714] |  |  | 43 | 5 | 1f049d74 |
| test1 | start_points | frac:0.3 | rmse | itransformer[lookback=128] | 0.543 [0.419, 0.686] |  |  | 43 | 5 | f6b438b9 |
| test1 | start_points | frac:0.3 | rmse | lgbm | 0.250 [0.179, 0.334] |  |  | 43 | 5 | 7345cc3d |
| test1 | start_points | frac:0.3 | rmse | lstm[lookback=32] | 0.460 [0.370, 0.554] |  |  | 43 | 5 | 3ad2c3cb |
| test1 | start_points | frac:0.3 | rmse | patchtst[lookback=128] | 0.759 [0.622, 0.904] |  |  | 43 | 5 | 271523a9 |
| test1 | start_points | frac:0.3 | rmse | transformer[lookback=32] | 0.302 [0.240, 0.373] |  |  | 43 | 5 | e1e42381 |
| test1 | start_points | frac:0.5 | rmse | age_only | 2.498 [1.876, 3.154] |  |  | 43 | 5 | cd1211f0 |
| test1 | start_points | frac:0.5 | rmse | elasticnet | 0.877 [0.592, 1.245] |  |  | 43 | 5 | 1f049d74 |
| test1 | start_points | frac:0.5 | rmse | itransformer[lookback=128] | 0.838 [0.615, 1.106] |  |  | 43 | 5 | f6b438b9 |
| test1 | start_points | frac:0.5 | rmse | lgbm | 0.496 [0.325, 0.705] |  |  | 43 | 5 | 7345cc3d |
| test1 | start_points | frac:0.5 | rmse | lstm[lookback=32] | 1.013 [0.566, 1.622] |  |  | 43 | 5 | 3ad2c3cb |
| test1 | start_points | frac:0.5 | rmse | patchtst[lookback=128] | 0.758 [0.578, 0.966] |  |  | 43 | 5 | 271523a9 |
| test1 | start_points | frac:0.5 | rmse | transformer[lookback=32] | 0.942 [0.488, 1.557] |  |  | 43 | 5 | e1e42381 |
| test1 | start_points | frac:0.7 | rmse | age_only | 2.778 [2.187, 3.412] |  |  | 43 | 5 | cd1211f0 |
| test1 | start_points | frac:0.7 | rmse | elasticnet | 1.098 [0.680, 1.620] |  |  | 43 | 5 | 1f049d74 |
| test1 | start_points | frac:0.7 | rmse | itransformer[lookback=128] | 0.977 [0.655, 1.378] |  |  | 43 | 5 | f6b438b9 |
| test1 | start_points | frac:0.7 | rmse | lgbm | 0.686 [0.480, 0.953] |  |  | 43 | 5 | 7345cc3d |
| test1 | start_points | frac:0.7 | rmse | lstm[lookback=32] | 1.037 [0.582, 1.621] |  |  | 43 | 5 | 3ad2c3cb |
| test1 | start_points | frac:0.7 | rmse | patchtst[lookback=128] | 1.422 [1.136, 1.738] |  |  | 43 | 5 | 271523a9 |
| test1 | start_points | frac:0.7 | rmse | transformer[lookback=32] | 1.052 [0.616, 1.611] |  |  | 43 | 5 | e1e42381 |
| test1 | start_points | overall | rmse | age_only | 2.168 [1.705, 2.664] |  |  | 43 | 5 | cd1211f0 |
| test1 | start_points | overall | rmse | elasticnet | 0.959 [0.712, 1.266] |  |  | 43 | 5 | 1f049d74 |
| test1 | start_points | overall | rmse | itransformer[lookback=128] | 0.857 [0.645, 1.136] |  |  | 43 | 5 | f6b438b9 |
| test1 | start_points | overall | rmse | lgbm | 0.527 [0.378, 0.722] |  |  | 43 | 5 | 7345cc3d |
| test1 | start_points | overall | rmse | lstm[lookback=32] | 0.915 [0.599, 1.329] |  |  | 43 | 5 | 3ad2c3cb |
| test1 | start_points | overall | rmse | patchtst[lookback=128] | 1.124 [0.968, 1.290] |  |  | 43 | 5 | 271523a9 |
| test1 | start_points | overall | rmse | transformer[lookback=32] | 0.808 [0.482, 1.230] |  |  | 43 | 5 | e1e42381 |
| test2 | all | overall | rmse | age_only | 3.673 [3.520, 3.821] |  |  | 40 | 5 | cd1211f0 |
| test2 | all | overall | rmse | elasticnet | 4.155 [4.023, 4.310] |  |  | 40 | 5 | 1f049d74 |
| test2 | all | overall | rmse | itransformer[lookback=128] | 1.554 [1.417, 1.727] |  |  | 40 | 5 | f6b438b9 |
| test2 | all | overall | rmse | lgbm | 2.553 [2.429, 2.684] |  |  | 40 | 5 | 7345cc3d |
| test2 | all | overall | rmse | lstm[lookback=32] | 2.188 [2.072, 2.331] |  |  | 40 | 5 | 3ad2c3cb |
| test2 | all | overall | rmse | patchtst[lookback=128] | 2.676 [2.569, 2.799] |  |  | 40 | 5 | 271523a9 |
| test2 | all | overall | rmse | transformer[lookback=32] | 2.532 [2.435, 2.644] |  |  | 40 | 5 | e1e42381 |
| test2 | start_points | fixed:100 | rmse | age_only | 0.252 [0.146, 0.387] |  |  | 40 | 5 | cd1211f0 |
| test2 | start_points | fixed:100 | rmse | elasticnet | 1.347 [1.152, 1.542] |  |  | 40 | 5 | 1f049d74 |
| test2 | start_points | fixed:100 | rmse | itransformer[lookback=128] | 0.501 [0.428, 0.583] |  |  | 40 | 5 | f6b438b9 |
| test2 | start_points | fixed:100 | rmse | lgbm | 0.539 [0.475, 0.609] |  |  | 40 | 5 | 7345cc3d |
| test2 | start_points | fixed:100 | rmse | lstm[lookback=32] | 0.328 [0.256, 0.403] |  |  | 40 | 5 | 3ad2c3cb |
| test2 | start_points | fixed:100 | rmse | patchtst[lookback=128] | 0.910 [0.734, 1.112] |  |  | 40 | 5 | 271523a9 |
| test2 | start_points | fixed:100 | rmse | transformer[lookback=32] | 0.600 [0.514, 0.688] |  |  | 40 | 5 | e1e42381 |
| test2 | start_points | frac:0.3 | rmse | age_only | 2.216 [1.814, 2.689] |  |  | 40 | 5 | cd1211f0 |
| test2 | start_points | frac:0.3 | rmse | elasticnet | 1.720 [1.507, 1.928] |  |  | 40 | 5 | 1f049d74 |
| test2 | start_points | frac:0.3 | rmse | itransformer[lookback=128] | 0.855 [0.728, 0.995] |  |  | 40 | 5 | f6b438b9 |
| test2 | start_points | frac:0.3 | rmse | lgbm | 0.437 [0.354, 0.524] |  |  | 40 | 5 | 7345cc3d |
| test2 | start_points | frac:0.3 | rmse | lstm[lookback=32] | 0.853 [0.716, 0.989] |  |  | 40 | 5 | 3ad2c3cb |
| test2 | start_points | frac:0.3 | rmse | patchtst[lookback=128] | 0.873 [0.758, 0.998] |  |  | 40 | 5 | 271523a9 |
| test2 | start_points | frac:0.3 | rmse | transformer[lookback=32] | 1.073 [0.939, 1.204] |  |  | 40 | 5 | e1e42381 |
| test2 | start_points | frac:0.5 | rmse | age_only | 4.875 [4.499, 5.210] |  |  | 40 | 5 | cd1211f0 |
| test2 | start_points | frac:0.5 | rmse | elasticnet | 1.857 [1.611, 2.090] |  |  | 40 | 5 | 1f049d74 |
| test2 | start_points | frac:0.5 | rmse | itransformer[lookback=128] | 1.095 [0.883, 1.348] |  |  | 40 | 5 | f6b438b9 |
| test2 | start_points | frac:0.5 | rmse | lgbm | 1.264 [0.973, 1.567] |  |  | 40 | 5 | 7345cc3d |
| test2 | start_points | frac:0.5 | rmse | lstm[lookback=32] | 1.610 [1.439, 1.775] |  |  | 40 | 5 | 3ad2c3cb |
| test2 | start_points | frac:0.5 | rmse | patchtst[lookback=128] | 0.817 [0.629, 1.039] |  |  | 40 | 5 | 271523a9 |
| test2 | start_points | frac:0.5 | rmse | transformer[lookback=32] | 1.661 [1.478, 1.829] |  |  | 40 | 5 | e1e42381 |
| test2 | start_points | frac:0.7 | rmse | age_only | 4.258 [3.958, 4.524] |  |  | 40 | 5 | cd1211f0 |
| test2 | start_points | frac:0.7 | rmse | elasticnet | 1.694 [1.446, 1.954] |  |  | 40 | 5 | 1f049d74 |
| test2 | start_points | frac:0.7 | rmse | itransformer[lookback=128] | 1.639 [1.293, 2.029] |  |  | 40 | 5 | f6b438b9 |
| test2 | start_points | frac:0.7 | rmse | lgbm | 2.198 [1.873, 2.509] |  |  | 40 | 5 | 7345cc3d |
| test2 | start_points | frac:0.7 | rmse | lstm[lookback=32] | 1.825 [1.636, 2.013] |  |  | 40 | 5 | 3ad2c3cb |
| test2 | start_points | frac:0.7 | rmse | patchtst[lookback=128] | 1.583 [1.166, 2.065] |  |  | 40 | 5 | 271523a9 |
| test2 | start_points | frac:0.7 | rmse | transformer[lookback=32] | 2.048 [1.848, 2.236] |  |  | 40 | 5 | e1e42381 |
| test2 | start_points | overall | rmse | age_only | 3.509 [3.286, 3.718] |  |  | 40 | 5 | cd1211f0 |
| test2 | start_points | overall | rmse | elasticnet | 1.709 [1.519, 1.899] |  |  | 40 | 5 | 1f049d74 |
| test2 | start_points | overall | rmse | itransformer[lookback=128] | 1.183 [0.992, 1.404] |  |  | 40 | 5 | f6b438b9 |
| test2 | start_points | overall | rmse | lgbm | 1.369 [1.180, 1.553] |  |  | 40 | 5 | 7345cc3d |
| test2 | start_points | overall | rmse | lstm[lookback=32] | 1.324 [1.194, 1.449] |  |  | 40 | 5 | 3ad2c3cb |
| test2 | start_points | overall | rmse | patchtst[lookback=128] | 1.253 [1.051, 1.493] |  |  | 40 | 5 | 271523a9 |
| test2 | start_points | overall | rmse | transformer[lookback=32] | 1.479 [1.339, 1.610] |  |  | 40 | 5 | e1e42381 |

</details>
