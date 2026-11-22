| task | dataset | split | candidate | reference | cand | ref | delta [95% CI] | k_cells | p_holm |
|---|---|---|---|---|---|---|---|---|---|
| soh | calce | loco | itransformer[lookback=32] | age_only | 3.28 | 6.89 | -3.604 [-4.813, -2.388] | 4/4 |  |
| soh | calce | loco | itransformer[lookback=32] | elasticnet | 3.28 | 3.6 | -0.320 [-2.300, +0.912] | 1/4 |  |
| soh | calce | loco | itransformer[lookback=32] | lgbm | 3.28 | 4.15 | -0.863 [-1.867, +0.174] | 3/4 |  |
| soh | calce | loco | itransformer[lookback=32] | lstm[lookback=32] | 3.28 | 2.07 | +1.217 [+0.839, +1.672] | 0/4 |  |
| soh | calce | loco | itransformer[lookback=32] | transformer[lookback=128] | 3.28 | 2.94 | +0.339 [-0.563, +1.245] | 2/4 |  |
| soh | calce | loco | elasticnet | age_only | 3.6 | 6.89 | -3.284 [-4.947, -1.967] | 4/4 |  |
| soh | calce | loco | lgbm | age_only | 4.15 | 6.89 | -2.741 [-4.195, -0.618] | 3/4 |  |
| soh | calce | loco | lstm[lookback=32] | age_only | 2.07 | 6.89 | -4.821 [-6.408, -3.234] | 4/4 |  |
| soh | calce | loco | transformer[lookback=128] | age_only | 2.94 | 6.89 | -3.943 [-5.552, -2.626] | 4/4 |  |
| soh | nasa | loco | itransformer[lookback=64] | age_only | 4.59 | 5.85 | -1.254 [-3.088, +1.066] | 3/4 |  |
| soh | nasa | loco | itransformer[lookback=64] | elasticnet | 4.59 | 5.42 | -0.826 [-3.459, +2.965] | 3/4 |  |
| soh | nasa | loco | itransformer[lookback=64] | lgbm | 4.59 | 3.94 | +0.651 [-0.658, +2.019] | 1/4 |  |
| soh | nasa | loco | itransformer[lookback=64] | lstm[lookback=64] | 4.59 | 4.22 | +0.369 [-0.296, +1.474] | 2/4 |  |
| soh | nasa | loco | itransformer[lookback=64] | transformer[lookback=64] | 4.59 | 7.77 | -3.182 [-5.518, -0.846] | 4/4 |  |
| soh | nasa | loco | elasticnet | age_only | 5.42 | 5.85 | -0.428 [-5.364, +4.073] | 2/4 |  |
| soh | nasa | loco | lgbm | age_only | 3.94 | 5.85 | -1.905 [-3.661, -0.616] | 4/4 |  |
| soh | nasa | loco | lstm[lookback=64] | age_only | 4.22 | 5.85 | -1.623 [-3.016, -0.230] | 3/4 |  |
| soh | nasa | loco | transformer[lookback=64] | age_only | 7.77 | 5.85 | +1.927 [-2.243, +6.097] | 2/4 |  |
| soh | toyota | test1 | itransformer[lookback=128] | age_only | 1.06 | 4.01 | -2.947 [-3.222, -2.695] | 43/43 | 2.05e-12 |
| soh | toyota | test2 | itransformer[lookback=128] | age_only | 1.55 | 3.67 | -2.119 [-2.306, -1.912] | 40/40 | 1.64e-11 |
| soh | toyota | test1 | itransformer[lookback=128] | elasticnet | 1.06 | 1.18 | -0.120 [-0.340, +0.132] | 35/43 | 0.0259 |
| soh | toyota | test2 | itransformer[lookback=128] | elasticnet | 1.55 | 4.16 | -2.601 [-2.723, -2.472] | 40/40 | 1.64e-11 |
| soh | toyota | test1 | itransformer[lookback=128] | lgbm | 1.06 | 0.947 | +0.114 [+0.020, +0.214] | 15/43 | 0.127 |
| soh | toyota | test2 | itransformer[lookback=128] | lgbm | 1.55 | 2.55 | -1.000 [-1.128, -0.867] | 39/40 | 2.55e-11 |
| soh | toyota | test1 | itransformer[lookback=128] | lstm[lookback=32] | 1.06 | 1.07 | -0.014 [-0.290, +0.251] | 20/43 | 0.724 |
| soh | toyota | test2 | itransformer[lookback=128] | lstm[lookback=32] | 1.55 | 2.19 | -0.634 [-0.718, -0.543] | 38/40 | 7.28e-11 |
| soh | toyota | test1 | itransformer[lookback=128] | transformer[lookback=32] | 1.06 | 0.907 | +0.154 [-0.092, +0.371] | 10/43 | 0.0012 |
| soh | toyota | test2 | itransformer[lookback=128] | transformer[lookback=32] | 1.55 | 2.53 | -0.978 [-1.082, -0.867] | 39/40 | 2.55e-11 |
| soh | toyota | test1 | elasticnet | age_only | 1.18 | 4.01 | -2.827 [-3.278, -2.437] | 42/43 | 4.77e-12 |
| soh | toyota | test2 | elasticnet | age_only | 4.16 | 3.67 | +0.482 [+0.249, +0.720] | 11/40 | 0.000798 |
| soh | toyota | test1 | lgbm | age_only | 0.947 | 4.01 | -3.060 [-3.335, -2.819] | 43/43 | 2.05e-12 |
| soh | toyota | test2 | lgbm | age_only | 2.55 | 3.67 | -1.119 [-1.342, -0.894] | 35/40 | 1.63e-09 |
| soh | toyota | test1 | lstm[lookback=32] | age_only | 1.07 | 4.01 | -2.933 [-3.369, -2.508] | 41/43 | 2.16e-11 |
| soh | toyota | test2 | lstm[lookback=32] | age_only | 2.19 | 3.67 | -1.485 [-1.680, -1.281] | 38/40 | 4.55e-11 |
| soh | toyota | test1 | transformer[lookback=32] | age_only | 0.907 | 4.01 | -3.101 [-3.497, -2.698] | 41/43 | 6.82e-12 |
| soh | toyota | test2 | transformer[lookback=32] | age_only | 2.53 | 3.67 | -1.141 [-1.323, -0.952] | 38/40 | 7.64e-11 |
| forecast | calce | loco | itransformer[lookback=32] | age_only | 3.96 | 7.08 | -3.121 [-4.465, -1.777] | 4/4 |  |
| forecast | calce | loco | itransformer[lookback=32] | elasticnet | 3.96 | 2.77 | +1.192 [+0.661, +1.711] | 0/4 |  |
| forecast | calce | loco | itransformer[lookback=32] | lgbm | 3.96 | 4.69 | -0.725 [-2.026, +0.575] | 2/4 |  |
| forecast | calce | loco | itransformer[lookback=32] | lstm[lookback=128] | 3.96 | 2.83 | +1.133 [+0.160, +2.034] | 1/4 |  |
| forecast | calce | loco | itransformer[lookback=32] | transformer[lookback=32] | 3.96 | 3.22 | +0.738 [+0.321, +1.155] | 0/4 |  |
| forecast | calce | loco | elasticnet | age_only | 2.77 | 7.08 | -4.314 [-6.096, -2.531] | 4/4 |  |
| forecast | calce | loco | lgbm | age_only | 4.69 | 7.08 | -2.396 [-3.924, -0.064] | 3/4 |  |
| forecast | calce | loco | lstm[lookback=128] | age_only | 2.83 | 7.08 | -4.254 [-6.440, -2.068] | 4/4 |  |
| forecast | calce | loco | transformer[lookback=32] | age_only | 3.22 | 7.08 | -3.859 [-5.620, -2.099] | 4/4 |  |
| forecast | nasa | loco | itransformer[lookback=64] | age_only | 5.82 | 6.28 | -0.457 [-2.022, +1.405] | 3/4 |  |
| forecast | nasa | loco | itransformer[lookback=64] | elasticnet | 5.82 | 7.74 | -1.918 [-4.810, +0.973] | 2/4 |  |
| forecast | nasa | loco | itransformer[lookback=64] | lgbm | 5.82 | 6.47 | -0.646 [-2.424, +1.276] | 3/4 |  |
| forecast | nasa | loco | itransformer[lookback=64] | lstm[lookback=64] | 5.82 | 5.62 | +0.204 [-0.745, +1.153] | 2/4 |  |
| forecast | nasa | loco | itransformer[lookback=64] | transformer[lookback=64] | 5.82 | 8.47 | -2.644 [-5.176, -0.745] | 4/4 |  |
| forecast | nasa | loco | elasticnet | age_only | 7.74 | 6.28 | +1.462 [-1.931, +5.557] | 2/4 |  |
| forecast | nasa | loco | lgbm | age_only | 6.47 | 6.28 | +0.189 [-1.070, +1.175] | 1/4 |  |
| forecast | nasa | loco | lstm[lookback=64] | age_only | 5.62 | 6.28 | -0.661 [-2.654, +1.792] | 3/4 |  |
| forecast | nasa | loco | transformer[lookback=64] | age_only | 8.47 | 6.28 | +2.188 [-0.092, +4.102] | 1/4 |  |
| forecast | toyota | test1 | itransformer[lookback=32] | age_only | 1.26 | 4.22 | -2.963 [-3.271, -2.677] | 43/43 | 2.05e-12 |
| forecast | toyota | test2 | itransformer[lookback=32] | age_only | 1.9 | 3.77 | -1.871 [-2.010, -1.730] | 40/40 | 1.64e-11 |
| forecast | toyota | test1 | itransformer[lookback=32] | elasticnet | 1.26 | 1.42 | -0.163 [-0.370, +0.027] | 25/43 | 0.0708 |
| forecast | toyota | test2 | itransformer[lookback=32] | elasticnet | 1.9 | 4.22 | -2.320 [-2.545, -2.104] | 40/40 | 1.64e-11 |
| forecast | toyota | test1 | itransformer[lookback=32] | lgbm | 1.26 | 0.927 | +0.328 [+0.207, +0.466] | 8/43 | 2.58e-06 |
| forecast | toyota | test2 | itransformer[lookback=32] | lgbm | 1.9 | 2.45 | -0.543 [-0.732, -0.350] | 33/40 | 6.11e-06 |
| forecast | toyota | test1 | itransformer[lookback=32] | lstm[lookback=128] | 1.26 | 0.999 | +0.256 [+0.121, +0.399] | 11/43 | 0.000437 |
| forecast | toyota | test2 | itransformer[lookback=32] | lstm[lookback=128] | 1.9 | 2.2 | -0.297 [-0.484, -0.107] | 30/40 | 0.00554 |
| forecast | toyota | test1 | itransformer[lookback=32] | transformer[lookback=32] | 1.26 | 1.03 | +0.223 [+0.099, +0.361] | 11/43 | 0.00356 |
| forecast | toyota | test2 | itransformer[lookback=32] | transformer[lookback=32] | 1.9 | 2.74 | -0.837 [-1.079, -0.614] | 35/40 | 5.82e-09 |
| forecast | toyota | test1 | elasticnet | age_only | 1.42 | 4.22 | -2.800 [-3.201, -2.414] | 42/43 | 1.14e-11 |
| forecast | toyota | test2 | elasticnet | age_only | 4.22 | 3.77 | +0.449 [+0.202, +0.701] | 14/40 | 0.00554 |
| forecast | toyota | test1 | lgbm | age_only | 0.927 | 4.22 | -3.292 [-3.603, -3.018] | 43/43 | 2.05e-12 |
| forecast | toyota | test2 | lgbm | age_only | 2.45 | 3.77 | -1.328 [-1.565, -1.091] | 36/40 | 7.64e-10 |
| forecast | toyota | test1 | lstm[lookback=128] | age_only | 0.999 | 4.22 | -3.220 [-3.549, -2.916] | 43/43 | 2.05e-12 |
| forecast | toyota | test2 | lstm[lookback=128] | age_only | 2.2 | 3.77 | -1.574 [-1.787, -1.354] | 39/40 | 2.55e-11 |
| forecast | toyota | test1 | transformer[lookback=32] | age_only | 1.03 | 4.22 | -3.186 [-3.510, -2.901] | 43/43 | 2.05e-12 |
| forecast | toyota | test2 | transformer[lookback=32] | age_only | 2.74 | 3.77 | -1.034 [-1.281, -0.764] | 37/40 | 5.22e-07 |
| rul | calce | loco | itransformer[lookback=32] | age_only | 50.6 | 50.7 | -0.065 [-2.015, +1.885] | 2/4 |  |
| rul | calce | loco | itransformer[lookback=32] | elasticnet | 50.6 | 3.25e+04 | -32495.930 [-97346.317, -19.718] | 4/4 |  |
| rul | calce | loco | itransformer[lookback=32] | lgbm | 50.6 | 65.7 | -15.116 [-26.963, +1.062] | 3/4 |  |
| rul | calce | loco | itransformer[lookback=32] | lstm[lookback=128] | 50.6 | 52.5 | -1.831 [-12.168, +6.531] | 2/4 |  |
| rul | calce | loco | itransformer[lookback=32] | transformer[lookback=32] | 50.6 | 54 | -3.364 [-10.807, +4.787] | 3/4 |  |
| rul | calce | loco | elasticnet | age_only | 3.25e+04 | 50.7 | +32495.865 [+17.703, +97346.923] | 0/4 |  |
| rul | calce | loco | lgbm | age_only | 65.7 | 50.7 | +15.051 [-2.799, +29.009] | 1/4 |  |
| rul | calce | loco | lstm[lookback=128] | age_only | 52.5 | 50.7 | +1.766 [-4.351, +9.875] | 2/4 |  |
| rul | calce | loco | transformer[lookback=32] | age_only | 54 | 50.7 | +3.299 [-6.524, +11.467] | 1/4 |  |
| rul | nasa | loco | itransformer[lookback=64] | age_only | 15.1 | 33.8 | -18.626 [-22.796, -14.288] | 4/4 |  |
| rul | nasa | loco | itransformer[lookback=64] | elasticnet | 15.1 | 535 | -520.133 [-1478.156, -6.225] | 4/4 |  |
| rul | nasa | loco | itransformer[lookback=64] | lgbm | 15.1 | 24.3 | -9.126 [-11.272, -6.979] | 4/4 |  |
| rul | nasa | loco | itransformer[lookback=64] | lstm[lookback=64] | 15.1 | 21.3 | -6.156 [-12.265, -2.484] | 4/4 |  |
| rul | nasa | loco | itransformer[lookback=64] | transformer[lookback=64] | 15.1 | 27.2 | -12.119 [-19.890, -7.158] | 4/4 |  |
| rul | nasa | loco | elasticnet | age_only | 535 | 33.8 | +501.507 [-12.568, +1463.868] | 2/4 |  |
| rul | nasa | loco | lgbm | age_only | 24.3 | 33.8 | -9.500 [-12.347, -4.781] | 4/4 |  |
| rul | nasa | loco | lstm[lookback=64] | age_only | 21.3 | 33.8 | -12.470 [-15.898, -9.289] | 4/4 |  |
| rul | nasa | loco | transformer[lookback=64] | age_only | 27.2 | 33.8 | -6.507 [-10.977, -2.071] | 4/4 |  |
| rul | toyota | test1 | itransformer[lookback=32] | age_only | 55.8 | 236 | -180.299 [-232.909, -134.594] | 40/43 | 3.46e-10 |
| rul | toyota | test2 | itransformer[lookback=32] | age_only | 146 | 259 | -113.574 [-148.866, -80.705] | 34/40 | 8.35e-08 |
| rul | toyota | test1 | itransformer[lookback=32] | elasticnet | 55.8 | 79.7 | -23.965 [-40.104, -10.656] | 33/43 | 0.000305 |
| rul | toyota | test2 | itransformer[lookback=32] | elasticnet | 146 | 125 | +20.956 [+10.119, +31.943] | 12/40 | 0.00419 |
| rul | toyota | test1 | itransformer[lookback=32] | lgbm | 55.8 | 51.2 | +4.588 [-0.644, +9.754] | 16/43 | 0.218 |
| rul | toyota | test2 | itransformer[lookback=32] | lgbm | 146 | 153 | -7.374 [-19.199, +4.776] | 21/40 | 0.423 |
| rul | toyota | test1 | itransformer[lookback=32] | lstm[lookback=128] | 55.8 | 54.4 | +1.343 [-8.970, +11.209] | 15/43 | 0.513 |
| rul | toyota | test2 | itransformer[lookback=32] | lstm[lookback=128] | 146 | 156 | -10.478 [-30.683, +4.614] | 23/40 | 0.423 |
| rul | toyota | test1 | itransformer[lookback=32] | transformer[lookback=32] | 55.8 | 58.7 | -2.923 [-11.818, +5.329] | 17/43 | 0.806 |
| rul | toyota | test2 | itransformer[lookback=32] | transformer[lookback=32] | 146 | 162 | -15.685 [-26.473, -4.280] | 32/40 | 0.00559 |
| rul | toyota | test1 | elasticnet | age_only | 79.7 | 236 | -156.334 [-198.903, -117.206] | 39/43 | 5.9e-10 |
| rul | toyota | test2 | elasticnet | age_only | 125 | 259 | -134.530 [-168.118, -101.463] | 36/40 | 2.43e-08 |
| rul | toyota | test1 | lgbm | age_only | 51.2 | 236 | -184.887 [-236.382, -139.387] | 40/43 | 3.77e-10 |
| rul | toyota | test2 | lgbm | age_only | 153 | 259 | -106.200 [-141.352, -72.413] | 33/40 | 1.59e-06 |
| rul | toyota | test1 | lstm[lookback=128] | age_only | 54.4 | 236 | -181.642 [-239.662, -131.813] | 39/43 | 1.43e-09 |
| rul | toyota | test2 | lstm[lookback=128] | age_only | 156 | 259 | -103.097 [-146.055, -60.205] | 33/40 | 3.75e-05 |
| rul | toyota | test1 | transformer[lookback=32] | age_only | 58.7 | 236 | -177.376 [-229.397, -131.080] | 39/43 | 1.23e-09 |
| rul | toyota | test2 | transformer[lookback=32] | age_only | 162 | 259 | -97.890 [-128.951, -67.354] | 33/40 | 2.09e-06 |
