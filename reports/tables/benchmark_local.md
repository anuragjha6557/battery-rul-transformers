# Benchmark tables: benchmark_local

- Protocol version: 1.1
- Git SHA: 0d7541bbcc
- Seeds: 1  |  unit runs: 72
- Note: n = 4 cells per NASA/CALCE dataset, so the 95 % cluster-bootstrap CI is wide by construction. Toyota rows are over test cells (test1 / test2 separately) with a cell-level bootstrap CI and a Holm-adjusted Wilcoxon p vs the best baseline. All metrics are computed per cell from the logged predictions.

## Headline (kind = overall; RMSE in %SOH, RUL MAE in cycles)

### calce_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | start_points | overall | rmse_h1 | gpr | 0.710 [0.534, 0.913] | 3/4 cells, 3/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 365bb77b |
| loco | start_points | overall | rmse_h1 | param_exp2 | 0.932 [0.622, 1.241] |  |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | overall | rmse_h1 | param_linear | 1.710 [1.387, 1.965] | 0/4 cells, 0/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 8308297a |
| loco | start_points | overall | rmse_h1 | param_power | 1.247 [1.192, 1.323] | 0/4 cells, 0/4 cell-seeds (vs param_exp2) |  | 4 | 1 | ce854d01 |
| loco | start_points | overall | rmse_h10 | gpr | 1.503 [1.015, 2.239] | 1/4 cells, 1/4 cell-seeds (vs param_power) |  | 4 | 1 | 365bb77b |
| loco | start_points | overall | rmse_h10 | param_exp2 | 1.388 [0.935, 2.085] | 3/4 cells, 3/4 cell-seeds (vs param_power) |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | overall | rmse_h10 | param_linear | 1.838 [1.205, 2.688] | 0/4 cells, 0/4 cell-seeds (vs param_power) |  | 4 | 1 | 8308297a |
| loco | start_points | overall | rmse_h10 | param_power | 1.387 [0.789, 2.092] |  |  | 4 | 1 | ce854d01 |
| loco | start_points | overall | rmse_h50 | gpr | 2.677 [2.120, 3.593] | 2/4 cells, 2/4 cell-seeds (vs param_power) |  | 4 | 1 | 365bb77b |
| loco | start_points | overall | rmse_h50 | param_exp2 | 2.765 [1.486, 4.168] | 1/4 cells, 1/4 cell-seeds (vs param_power) |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | overall | rmse_h50 | param_linear | 3.402 [2.758, 4.095] | 0/4 cells, 0/4 cell-seeds (vs param_power) |  | 4 | 1 | 8308297a |
| loco | start_points | overall | rmse_h50 | param_power | 2.385 [1.978, 2.838] |  |  | 4 | 1 | ce854d01 |

### calce_rul

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | start_points | overall | rul_mae | gpr | 713.713 [510.684, 908.066] | 0/4 cells, 0/4 cell-seeds (vs param_linear) |  | 4 | 1 | b01a0314 |
| loco | start_points | overall | rul_mae | param_exp2 | 507.500 [373.150, 634.600] | 0/4 cells, 0/4 cell-seeds (vs param_linear) |  | 4 | 1 | 0902ead5 |
| loco | start_points | overall | rul_mae | param_linear | 118.850 [104.900, 140.550] |  |  | 4 | 1 | ed1477de |
| loco | start_points | overall | rul_mae | param_power | 211.850 [121.550, 355.400] | 1/4 cells, 1/4 cell-seeds (vs param_linear) |  | 4 | 1 | 8b8457c1 |

### nasa_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | start_points | overall | rmse_h1 | gpr | 1.648 [0.953, 2.343] | 1/4 cells, 1/4 cell-seeds (vs param_exp2) | 2.450 | 4 | 1 | be2a6022 |
| loco | start_points | overall | rmse_h1 | param_exp2 | 1.394 [0.903, 1.885] |  | 1.977 | 4 | 1 | a2cb006a |
| loco | start_points | overall | rmse_h1 | param_linear | 2.097 [1.698, 2.495] | 0/4 cells, 0/4 cell-seeds (vs param_exp2) | 2.662 | 4 | 1 | b3f24bbf |
| loco | start_points | overall | rmse_h1 | param_power | 1.589 [1.008, 2.170] | 0/4 cells, 0/4 cell-seeds (vs param_exp2) | 2.360 | 4 | 1 | e5fb89a3 |
| loco | start_points | overall | rmse_h10 | gpr | 2.925 [2.636, 3.176] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 3.065 | 4 | 1 | be2a6022 |
| loco | start_points | overall | rmse_h10 | param_exp2 | 16.590 [3.387, 33.528] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 16.421 | 4 | 1 | a2cb006a |
| loco | start_points | overall | rmse_h10 | param_linear | 2.740 [2.458, 3.021] |  | 2.912 | 4 | 1 | b3f24bbf |
| loco | start_points | overall | rmse_h10 | param_power | 3.012 [2.102, 3.921] | 2/4 cells, 2/4 cell-seeds (vs param_linear) | 3.897 | 4 | 1 | e5fb89a3 |
| loco | start_points | overall | rmse_h50 | gpr | 7.334 [4.437, 10.231] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 4.050 | 4 | 1 | be2a6022 |
| loco | start_points | overall | rmse_h50 | param_exp2 | 35.375 [22.976, 47.774] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 50.091 | 4 | 1 | a2cb006a |
| loco | start_points | overall | rmse_h50 | param_linear | 6.676 [4.286, 9.066] |  | 3.476 | 4 | 1 | b3f24bbf |
| loco | start_points | overall | rmse_h50 | param_power | 14.950 [14.622, 15.236] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 15.190 | 4 | 1 | e5fb89a3 |

### nasa_rul

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | start_points | overall | rul_mae | gpr | 56.458 [12.924, 99.991] | 2/4 cells, 2/4 cell-seeds (vs param_power) | 10.842 | 4 | 1 | b6daa7a6 |
| loco | start_points | overall | rul_mae | param_exp2 | 77.800 [49.550, 115.850] | 0/4 cells, 0/4 cell-seeds (vs param_power) | 134.600 | 4 | 1 | ebb632b7 |
| loco | start_points | overall | rul_mae | param_linear | 54.000 [11.100, 96.900] | 2/4 cells, 2/4 cell-seeds (vs param_power) | 9.400 | 4 | 1 | 86d5a25a |
| loco | start_points | overall | rul_mae | param_power | 45.750 [29.000, 64.350] |  | 23.800 | 4 | 1 | 7a073d4e |

### toyota_forecast

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | start_points | overall | rmse_h1 | gpr | 0.060 [0.036, 0.088] | p=4.47e-06 (vs param_power) |  | 43 | 1 | e2d7a35c |
| test1 | start_points | overall | rmse_h1 | param_exp2 | 0.151 [0.099, 0.219] | p=0.9 (vs param_power) |  | 43 | 1 | 8ccdd557 |
| test1 | start_points | overall | rmse_h1 | param_linear | 0.455 [0.410, 0.497] | p=3.41e-12 (vs param_power) |  | 43 | 1 | e7a9712a |
| test1 | start_points | overall | rmse_h1 | param_power | 0.119 [0.098, 0.141] |  |  | 43 | 1 | 792c2b20 |
| test1 | start_points | overall | rmse_h10 | gpr | 0.153 [0.118, 0.192] | p=0.352 (vs param_power) |  | 43 | 1 | e2d7a35c |
| test1 | start_points | overall | rmse_h10 | param_exp2 | 0.288 [0.155, 0.496] | p=0.562 (vs param_power) |  | 43 | 1 | 8ccdd557 |
| test1 | start_points | overall | rmse_h10 | param_linear | 0.569 [0.506, 0.633] | p=2.05e-12 (vs param_power) |  | 43 | 1 | e7a9712a |
| test1 | start_points | overall | rmse_h10 | param_power | 0.167 [0.137, 0.201] |  |  | 43 | 1 | 792c2b20 |
| test1 | start_points | overall | rmse_h50 | gpr | 0.866 [0.734, 1.026] | p=1.26e-09 (vs param_power) |  | 43 | 1 | e2d7a35c |
| test1 | start_points | overall | rmse_h50 | param_exp2 | 2.115 [0.529, 4.807] | p=0.0899 (vs param_power) |  | 43 | 1 | 8ccdd557 |
| test1 | start_points | overall | rmse_h50 | param_linear | 1.211 [1.049, 1.394] | p=3.41e-12 (vs param_power) |  | 43 | 1 | e7a9712a |
| test1 | start_points | overall | rmse_h50 | param_power | 0.518 [0.463, 0.574] |  |  | 43 | 1 | 792c2b20 |
| test2 | start_points | overall | rmse_h1 | gpr | 0.013 [0.009, 0.019] | p=9.09e-11 (vs param_exp2) |  | 40 | 1 | e2d7a35c |
| test2 | start_points | overall | rmse_h1 | param_exp2 | 0.054 [0.047, 0.062] |  |  | 40 | 1 | 8ccdd557 |
| test2 | start_points | overall | rmse_h1 | param_linear | 0.216 [0.186, 0.245] | p=1.09e-11 (vs param_exp2) |  | 40 | 1 | e7a9712a |
| test2 | start_points | overall | rmse_h1 | param_power | 0.069 [0.059, 0.079] | p=0.0299 (vs param_exp2) |  | 40 | 1 | 792c2b20 |
| test2 | start_points | overall | rmse_h10 | gpr | 0.036 [0.030, 0.043] | p=2.4e-08 (vs param_exp2) |  | 40 | 1 | e2d7a35c |
| test2 | start_points | overall | rmse_h10 | param_exp2 | 0.075 [0.069, 0.082] |  |  | 40 | 1 | 8ccdd557 |
| test2 | start_points | overall | rmse_h10 | param_linear | 0.250 [0.216, 0.285] | p=7.64e-11 (vs param_exp2) |  | 40 | 1 | e7a9712a |
| test2 | start_points | overall | rmse_h10 | param_power | 0.087 [0.074, 0.100] | p=0.118 (vs param_exp2) |  | 40 | 1 | 792c2b20 |
| test2 | start_points | overall | rmse_h50 | gpr | 0.199 [0.169, 0.236] | p=0.0598 (vs param_power) |  | 40 | 1 | e2d7a35c |
| test2 | start_points | overall | rmse_h50 | param_exp2 | 0.254 [0.230, 0.286] | p=0.0747 (vs param_power) |  | 40 | 1 | 8ccdd557 |
| test2 | start_points | overall | rmse_h50 | param_linear | 0.449 [0.387, 0.512] | p=2.73e-11 (vs param_power) |  | 40 | 1 | e7a9712a |
| test2 | start_points | overall | rmse_h50 | param_power | 0.227 [0.199, 0.256] |  |  | 40 | 1 | 792c2b20 |

### toyota_rul

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | start_points | overall | rul_mae | gpr | 3080.028 [2826.128, 3302.523] | p=6.82e-13 (vs param_exp2) |  | 43 | 1 | 80fc29b8 |
| test1 | start_points | overall | rul_mae | param_exp2 | 338.767 [227.033, 471.331] |  |  | 43 | 1 | 794099a2 |
| test1 | start_points | overall | rul_mae | param_linear | 2671.971 [2377.517, 2930.799] | p=6.82e-13 (vs param_exp2) |  | 43 | 1 | 30134392 |
| test1 | start_points | overall | rul_mae | param_power | 663.698 [498.200, 838.117] | p=3.73e-05 (vs param_exp2) |  | 43 | 1 | 9c9b46d7 |
| test2 | start_points | overall | rul_mae | gpr | 3060.624 [2833.148, 3260.136] | p=5.46e-12 (vs param_power) |  | 40 | 1 | 80fc29b8 |
| test2 | start_points | overall | rul_mae | param_exp2 | 888.531 [670.975, 1121.205] | p=0.727 (vs param_power) |  | 40 | 1 | 794099a2 |
| test2 | start_points | overall | rul_mae | param_linear | 2887.188 [2618.159, 3100.594] | p=5.46e-12 (vs param_power) |  | 40 | 1 | 30134392 |
| test2 | start_points | overall | rul_mae | param_power | 884.856 [765.147, 1007.612] |  |  | 40 | 1 | 9c9b46d7 |

## Mean rank (dataset x task x split x policy x headline metric)

| model | mean rank | conditions | missing |
|---|---|---|---|
| param_power | 2.00 | 16 | 0 |
| gpr | 2.19 | 16 | 0 |
| param_exp2 | 2.69 | 16 | 0 |
| param_linear | 3.12 | 16 | 0 |

## Full tables

<details><summary>calce_forecast (120 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | start_points | fixed:200 | rmse_h1 | gpr | 0.482 [0.241, 0.748] | 3/4 cells, 3/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 365bb77b |
| loco | start_points | fixed:200 | rmse_h1 | param_exp2 | 0.492 [0.120, 0.874] |  |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | fixed:200 | rmse_h1 | param_linear | 1.874 [1.354, 2.394] | 0/4 cells, 0/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 8308297a |
| loco | start_points | fixed:200 | rmse_h1 | param_power | 1.229 [0.736, 1.723] | 1/4 cells, 1/4 cell-seeds (vs param_exp2) |  | 4 | 1 | ce854d01 |
| loco | start_points | fixed:200 | rmse_h10 | gpr | 1.598 [0.260, 3.893] | 3/4 cells, 3/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 365bb77b |
| loco | start_points | fixed:200 | rmse_h10 | param_exp2 | 1.673 [0.467, 3.642] |  |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | fixed:200 | rmse_h10 | param_linear | 2.821 [1.472, 5.006] | 0/4 cells, 0/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 8308297a |
| loco | start_points | fixed:200 | rmse_h10 | param_power | 2.027 [0.771, 4.064] | 1/4 cells, 1/4 cell-seeds (vs param_exp2) |  | 4 | 1 | ce854d01 |
| loco | start_points | fixed:200 | rmse_h100 | gpr | 2.705 [0.976, 4.326] | 2/4 cells, 2/4 cell-seeds (vs param_power) |  | 4 | 1 | 365bb77b |
| loco | start_points | fixed:200 | rmse_h100 | param_exp2 | 2.981 [1.060, 5.045] | 2/4 cells, 2/4 cell-seeds (vs param_power) |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | fixed:200 | rmse_h100 | param_linear | 4.591 [3.524, 5.409] | 0/4 cells, 0/4 cell-seeds (vs param_power) |  | 4 | 1 | 8308297a |
| loco | start_points | fixed:200 | rmse_h100 | param_power | 2.055 [1.231, 2.641] |  |  | 4 | 1 | ce854d01 |
| loco | start_points | fixed:200 | rmse_h25 | gpr | 1.604 [0.390, 3.319] | 0/4 cells, 0/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 365bb77b |
| loco | start_points | fixed:200 | rmse_h25 | param_exp2 | 1.142 [0.203, 2.185] |  |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | fixed:200 | rmse_h25 | param_linear | 3.849 [3.089, 4.472] | 0/4 cells, 0/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 8308297a |
| loco | start_points | fixed:200 | rmse_h25 | param_power | 2.796 [2.161, 3.294] | 0/4 cells, 0/4 cell-seeds (vs param_exp2) |  | 4 | 1 | ce854d01 |
| loco | start_points | fixed:200 | rmse_h50 | gpr | 1.584 [0.458, 3.301] | 1/4 cells, 1/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 365bb77b |
| loco | start_points | fixed:200 | rmse_h50 | param_exp2 | 1.433 [0.391, 2.474] |  |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | fixed:200 | rmse_h50 | param_linear | 4.024 [3.481, 4.536] | 0/4 cells, 0/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 8308297a |
| loco | start_points | fixed:200 | rmse_h50 | param_power | 2.508 [2.007, 2.865] | 1/4 cells, 1/4 cell-seeds (vs param_exp2) |  | 4 | 1 | ce854d01 |
| loco | start_points | fixed:400 | rmse_h1 | gpr | 0.462 [0.168, 0.808] | 4/4 cells, 4/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 365bb77b |
| loco | start_points | fixed:400 | rmse_h1 | param_exp2 | 0.993 [0.440, 1.555] |  |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | fixed:400 | rmse_h1 | param_linear | 1.632 [1.211, 2.100] | 1/4 cells, 1/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 8308297a |
| loco | start_points | fixed:400 | rmse_h1 | param_power | 1.268 [0.700, 1.835] | 0/4 cells, 0/4 cell-seeds (vs param_exp2) |  | 4 | 1 | ce854d01 |
| loco | start_points | fixed:400 | rmse_h10 | gpr | 0.911 [0.125, 1.698] | 2/4 cells, 2/4 cell-seeds (vs param_linear) |  | 4 | 1 | 365bb77b |
| loco | start_points | fixed:400 | rmse_h10 | param_exp2 | 1.095 [0.900, 1.269] | 1/4 cells, 1/4 cell-seeds (vs param_linear) |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | fixed:400 | rmse_h10 | param_linear | 0.733 [0.080, 1.979] |  |  | 4 | 1 | 8308297a |
| loco | start_points | fixed:400 | rmse_h10 | param_power | 1.122 [0.807, 1.589] | 1/4 cells, 1/4 cell-seeds (vs param_linear) |  | 4 | 1 | ce854d01 |
| loco | start_points | fixed:400 | rmse_h100 | gpr | 4.285 [2.955, 5.616] | 0/4 cells, 0/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 365bb77b |
| loco | start_points | fixed:400 | rmse_h100 | param_exp2 | 2.050 [0.509, 4.093] |  |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | fixed:400 | rmse_h100 | param_linear | 2.270 [0.877, 3.468] | 2/4 cells, 2/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 8308297a |
| loco | start_points | fixed:400 | rmse_h100 | param_power | 2.129 [0.642, 4.543] | 1/4 cells, 1/4 cell-seeds (vs param_exp2) |  | 4 | 1 | ce854d01 |
| loco | start_points | fixed:400 | rmse_h25 | gpr | 1.423 [0.300, 2.546] | 1/4 cells, 1/4 cell-seeds (vs param_linear) |  | 4 | 1 | 365bb77b |
| loco | start_points | fixed:400 | rmse_h25 | param_exp2 | 1.466 [0.948, 2.102] | 1/4 cells, 1/4 cell-seeds (vs param_linear) |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | fixed:400 | rmse_h25 | param_linear | 1.163 [0.139, 2.997] |  |  | 4 | 1 | 8308297a |
| loco | start_points | fixed:400 | rmse_h25 | param_power | 1.515 [0.841, 2.487] | 1/4 cells, 1/4 cell-seeds (vs param_linear) |  | 4 | 1 | ce854d01 |
| loco | start_points | fixed:400 | rmse_h50 | gpr | 2.352 [1.439, 3.125] | 2/4 cells, 2/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 365bb77b |
| loco | start_points | fixed:400 | rmse_h50 | param_exp2 | 1.451 [0.277, 2.946] |  |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | fixed:400 | rmse_h50 | param_linear | 2.088 [1.216, 2.961] | 1/4 cells, 1/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 8308297a |
| loco | start_points | fixed:400 | rmse_h50 | param_power | 1.654 [0.287, 3.143] | 1/4 cells, 1/4 cell-seeds (vs param_exp2) |  | 4 | 1 | ce854d01 |
| loco | start_points | frac:0.3 | rmse_h1 | gpr | 0.922 [0.611, 1.232] | 1/4 cells, 1/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 365bb77b |
| loco | start_points | frac:0.3 | rmse_h1 | param_exp2 | 0.857 [0.336, 1.159] |  |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | frac:0.3 | rmse_h1 | param_linear | 2.016 [1.550, 2.477] | 0/4 cells, 0/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 8308297a |
| loco | start_points | frac:0.3 | rmse_h1 | param_power | 1.299 [0.846, 1.752] | 2/4 cells, 2/4 cell-seeds (vs param_exp2) |  | 4 | 1 | ce854d01 |
| loco | start_points | frac:0.3 | rmse_h10 | gpr | 0.950 [0.713, 1.187] | 1/4 cells, 1/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 365bb77b |
| loco | start_points | frac:0.3 | rmse_h10 | param_exp2 | 0.742 [0.064, 1.724] |  |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | frac:0.3 | rmse_h10 | param_linear | 2.049 [1.209, 2.888] | 1/4 cells, 1/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 8308297a |
| loco | start_points | frac:0.3 | rmse_h10 | param_power | 1.172 [0.360, 2.042] | 2/4 cells, 2/4 cell-seeds (vs param_exp2) |  | 4 | 1 | ce854d01 |
| loco | start_points | frac:0.3 | rmse_h100 | gpr | 3.101 [0.843, 5.980] | 3/4 cells, 3/4 cell-seeds (vs param_power) |  | 4 | 1 | 365bb77b |
| loco | start_points | frac:0.3 | rmse_h100 | param_exp2 | 11.272 [2.914, 22.308] | 1/4 cells, 1/4 cell-seeds (vs param_power) |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | frac:0.3 | rmse_h100 | param_linear | 6.720 [6.452, 7.110] | 0/4 cells, 0/4 cell-seeds (vs param_power) |  | 4 | 1 | 8308297a |
| loco | start_points | frac:0.3 | rmse_h100 | param_power | 3.597 [3.532, 3.703] |  |  | 4 | 1 | ce854d01 |
| loco | start_points | frac:0.3 | rmse_h25 | gpr | 1.312 [0.351, 2.689] | 3/4 cells, 3/4 cell-seeds (vs param_power) |  | 4 | 1 | 365bb77b |
| loco | start_points | frac:0.3 | rmse_h25 | param_exp2 | 2.095 [0.643, 3.249] | 1/4 cells, 1/4 cell-seeds (vs param_power) |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | frac:0.3 | rmse_h25 | param_linear | 2.880 [2.560, 3.359] | 0/4 cells, 0/4 cell-seeds (vs param_power) |  | 4 | 1 | 8308297a |
| loco | start_points | frac:0.3 | rmse_h25 | param_power | 1.649 [1.336, 2.003] |  |  | 4 | 1 | ce854d01 |
| loco | start_points | frac:0.3 | rmse_h50 | gpr | 3.467 [1.566, 6.254] | 2/4 cells, 2/4 cell-seeds (vs param_power) |  | 4 | 1 | 365bb77b |
| loco | start_points | frac:0.3 | rmse_h50 | param_exp2 | 5.204 [2.491, 8.060] | 2/4 cells, 2/4 cell-seeds (vs param_power) |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | frac:0.3 | rmse_h50 | param_linear | 5.439 [3.886, 7.066] | 0/4 cells, 0/4 cell-seeds (vs param_power) |  | 4 | 1 | 8308297a |
| loco | start_points | frac:0.3 | rmse_h50 | param_power | 3.620 [2.217, 5.069] |  |  | 4 | 1 | ce854d01 |
| loco | start_points | frac:0.5 | rmse_h1 | gpr | 0.816 [0.386, 1.394] | 2/4 cells, 2/4 cell-seeds (vs param_power) |  | 4 | 1 | 365bb77b |
| loco | start_points | frac:0.5 | rmse_h1 | param_exp2 | 0.874 [0.321, 1.428] | 2/4 cells, 2/4 cell-seeds (vs param_power) |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | frac:0.5 | rmse_h1 | param_linear | 1.244 [0.503, 1.986] | 0/4 cells, 0/4 cell-seeds (vs param_power) |  | 4 | 1 | 8308297a |
| loco | start_points | frac:0.5 | rmse_h1 | param_power | 0.776 [0.110, 1.443] |  |  | 4 | 1 | ce854d01 |
| loco | start_points | frac:0.5 | rmse_h10 | gpr | 1.559 [1.018, 2.322] | 0/4 cells, 0/4 cell-seeds (vs param_power) |  | 4 | 1 | 365bb77b |
| loco | start_points | frac:0.5 | rmse_h10 | param_exp2 | 1.353 [0.802, 2.149] | 0/4 cells, 0/4 cell-seeds (vs param_power) |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | frac:0.5 | rmse_h10 | param_linear | 0.697 [0.216, 1.075] | 1/4 cells, 1/4 cell-seeds (vs param_power) |  | 4 | 1 | 8308297a |
| loco | start_points | frac:0.5 | rmse_h10 | param_power | 0.386 [0.171, 0.600] |  |  | 4 | 1 | ce854d01 |
| loco | start_points | frac:0.5 | rmse_h100 | gpr | 3.091 [1.299, 4.619] | 1/4 cells, 1/4 cell-seeds (vs param_power) |  | 4 | 1 | 365bb77b |
| loco | start_points | frac:0.5 | rmse_h100 | param_exp2 | 2.639 [1.529, 3.382] | 1/4 cells, 1/4 cell-seeds (vs param_power) |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | frac:0.5 | rmse_h100 | param_linear | 1.915 [0.840, 2.990] | 1/4 cells, 1/4 cell-seeds (vs param_power) |  | 4 | 1 | 8308297a |
| loco | start_points | frac:0.5 | rmse_h100 | param_power | 0.987 [0.692, 1.229] |  |  | 4 | 1 | ce854d01 |
| loco | start_points | frac:0.5 | rmse_h25 | gpr | 1.731 [0.546, 2.924] | 2/4 cells, 2/4 cell-seeds (vs param_power) |  | 4 | 1 | 365bb77b |
| loco | start_points | frac:0.5 | rmse_h25 | param_exp2 | 1.305 [0.421, 2.482] | 2/4 cells, 2/4 cell-seeds (vs param_power) |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | frac:0.5 | rmse_h25 | param_linear | 1.217 [0.561, 1.826] | 1/4 cells, 1/4 cell-seeds (vs param_power) |  | 4 | 1 | 8308297a |
| loco | start_points | frac:0.5 | rmse_h25 | param_power | 0.826 [0.485, 1.095] |  |  | 4 | 1 | ce854d01 |
| loco | start_points | frac:0.5 | rmse_h50 | gpr | 2.156 [1.035, 2.864] | 1/4 cells, 1/4 cell-seeds (vs param_power) |  | 4 | 1 | 365bb77b |
| loco | start_points | frac:0.5 | rmse_h50 | param_exp2 | 1.429 [0.477, 2.002] | 1/4 cells, 1/4 cell-seeds (vs param_power) |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | frac:0.5 | rmse_h50 | param_linear | 1.727 [1.103, 2.431] | 0/4 cells, 0/4 cell-seeds (vs param_power) |  | 4 | 1 | 8308297a |
| loco | start_points | frac:0.5 | rmse_h50 | param_power | 0.679 [0.120, 1.283] |  |  | 4 | 1 | ce854d01 |
| loco | start_points | frac:0.7 | rmse_h1 | gpr | 0.363 [0.132, 0.593] | 4/4 cells, 4/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 365bb77b |
| loco | start_points | frac:0.7 | rmse_h1 | param_exp2 | 0.938 [0.535, 1.238] |  |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | frac:0.7 | rmse_h1 | param_linear | 1.012 [0.166, 1.878] | 2/4 cells, 2/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 8308297a |
| loco | start_points | frac:0.7 | rmse_h1 | param_power | 0.957 [0.610, 1.456] | 2/4 cells, 2/4 cell-seeds (vs param_exp2) |  | 4 | 1 | ce854d01 |
| loco | start_points | frac:0.7 | rmse_h10 | gpr | 0.988 [0.291, 1.735] | 2/4 cells, 2/4 cell-seeds (vs param_linear) |  | 4 | 1 | 365bb77b |
| loco | start_points | frac:0.7 | rmse_h10 | param_exp2 | 0.952 [0.764, 1.275] | 1/4 cells, 1/4 cell-seeds (vs param_linear) |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | frac:0.7 | rmse_h10 | param_linear | 0.738 [0.283, 1.561] |  |  | 4 | 1 | 8308297a |
| loco | start_points | frac:0.7 | rmse_h10 | param_power | 0.873 [0.547, 1.200] | 1/4 cells, 1/4 cell-seeds (vs param_linear) |  | 4 | 1 | ce854d01 |
| loco | start_points | frac:0.7 | rmse_h100 | gpr | 4.312 [3.690, 4.929] | 0/4 cells, 0/4 cell-seeds (vs param_power) |  | 4 | 1 | 365bb77b |
| loco | start_points | frac:0.7 | rmse_h100 | param_exp2 | 1.742 [0.467, 3.988] | 1/4 cells, 1/4 cell-seeds (vs param_power) |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | frac:0.7 | rmse_h100 | param_linear | 1.970 [1.200, 2.740] | 1/4 cells, 1/4 cell-seeds (vs param_power) |  | 4 | 1 | 8308297a |
| loco | start_points | frac:0.7 | rmse_h100 | param_power | 1.580 [0.422, 3.737] |  |  | 4 | 1 | ce854d01 |
| loco | start_points | frac:0.7 | rmse_h25 | gpr | 1.170 [0.498, 2.139] | 2/4 cells, 2/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 365bb77b |
| loco | start_points | frac:0.7 | rmse_h25 | param_exp2 | 1.022 [0.422, 1.481] |  |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | frac:0.7 | rmse_h25 | param_linear | 1.163 [0.191, 2.248] | 2/4 cells, 2/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 8308297a |
| loco | start_points | frac:0.7 | rmse_h25 | param_power | 1.033 [0.482, 1.627] | 2/4 cells, 2/4 cell-seeds (vs param_exp2) |  | 4 | 1 | ce854d01 |
| loco | start_points | frac:0.7 | rmse_h50 | gpr | 2.066 [1.501, 2.639] | 2/4 cells, 2/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 365bb77b |
| loco | start_points | frac:0.7 | rmse_h50 | param_exp2 | 1.178 [0.428, 1.912] |  |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | frac:0.7 | rmse_h50 | param_linear | 1.528 [0.698, 2.603] | 2/4 cells, 2/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 8308297a |
| loco | start_points | frac:0.7 | rmse_h50 | param_power | 1.188 [0.433, 1.943] | 2/4 cells, 2/4 cell-seeds (vs param_exp2) |  | 4 | 1 | ce854d01 |
| loco | start_points | overall | rmse_h1 | gpr | 0.710 [0.534, 0.913] | 3/4 cells, 3/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 365bb77b |
| loco | start_points | overall | rmse_h1 | param_exp2 | 0.932 [0.622, 1.241] |  |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | overall | rmse_h1 | param_linear | 1.710 [1.387, 1.965] | 0/4 cells, 0/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 8308297a |
| loco | start_points | overall | rmse_h1 | param_power | 1.247 [1.192, 1.323] | 0/4 cells, 0/4 cell-seeds (vs param_exp2) |  | 4 | 1 | ce854d01 |
| loco | start_points | overall | rmse_h10 | gpr | 1.503 [1.015, 2.239] | 1/4 cells, 1/4 cell-seeds (vs param_power) |  | 4 | 1 | 365bb77b |
| loco | start_points | overall | rmse_h10 | param_exp2 | 1.388 [0.935, 2.085] | 3/4 cells, 3/4 cell-seeds (vs param_power) |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | overall | rmse_h10 | param_linear | 1.838 [1.205, 2.688] | 0/4 cells, 0/4 cell-seeds (vs param_power) |  | 4 | 1 | 8308297a |
| loco | start_points | overall | rmse_h10 | param_power | 1.387 [0.789, 2.092] |  |  | 4 | 1 | ce854d01 |
| loco | start_points | overall | rmse_h100 | gpr | 3.807 [2.768, 4.846] | 0/4 cells, 0/4 cell-seeds (vs param_power) |  | 4 | 1 | 365bb77b |
| loco | start_points | overall | rmse_h100 | param_exp2 | 5.659 [1.768, 10.572] | 1/4 cells, 1/4 cell-seeds (vs param_power) |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | overall | rmse_h100 | param_linear | 4.084 [3.821, 4.347] | 0/4 cells, 0/4 cell-seeds (vs param_power) |  | 4 | 1 | 8308297a |
| loco | start_points | overall | rmse_h100 | param_power | 2.497 [2.006, 3.338] |  |  | 4 | 1 | ce854d01 |
| loco | start_points | overall | rmse_h25 | gpr | 1.797 [1.275, 2.543] | 1/4 cells, 1/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 365bb77b |
| loco | start_points | overall | rmse_h25 | param_exp2 | 1.632 [1.035, 2.260] |  |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | overall | rmse_h25 | param_linear | 2.468 [1.960, 3.127] | 0/4 cells, 0/4 cell-seeds (vs param_exp2) |  | 4 | 1 | 8308297a |
| loco | start_points | overall | rmse_h25 | param_power | 1.751 [1.412, 2.209] | 2/4 cells, 2/4 cell-seeds (vs param_exp2) |  | 4 | 1 | ce854d01 |
| loco | start_points | overall | rmse_h50 | gpr | 2.677 [2.120, 3.593] | 2/4 cells, 2/4 cell-seeds (vs param_power) |  | 4 | 1 | 365bb77b |
| loco | start_points | overall | rmse_h50 | param_exp2 | 2.765 [1.486, 4.168] | 1/4 cells, 1/4 cell-seeds (vs param_power) |  | 4 | 1 | 3e6a6f4b |
| loco | start_points | overall | rmse_h50 | param_linear | 3.402 [2.758, 4.095] | 0/4 cells, 0/4 cell-seeds (vs param_power) |  | 4 | 1 | 8308297a |
| loco | start_points | overall | rmse_h50 | param_power | 2.385 [1.978, 2.838] |  |  | 4 | 1 | ce854d01 |

</details>

<details><summary>calce_rul (60 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | start_points | fixed:200 | rul_bias | gpr | 313.655 [-131.967, 759.278] | (vs nan) |  | 4 | 1 | b01a0314 |
| loco | start_points | fixed:200 | rul_bias | param_exp2 | 617.500 [209.500, 867.000] | (vs nan) |  | 4 | 1 | 0902ead5 |
| loco | start_points | fixed:200 | rul_bias | param_linear | -175.000 [-242.250, -79.750] | (vs nan) |  | 4 | 1 | ed1477de |
| loco | start_points | fixed:200 | rul_bias | param_power | 65.750 [-58.000, 252.250] | (vs nan) |  | 4 | 1 | 8b8457c1 |
| loco | start_points | fixed:200 | rul_mae | gpr | 445.622 [131.967, 759.278] | 1/4 cells, 1/4 cell-seeds (vs param_power) |  | 4 | 1 | b01a0314 |
| loco | start_points | fixed:200 | rul_mae | param_exp2 | 617.500 [209.500, 867.000] | 1/4 cells, 1/4 cell-seeds (vs param_power) |  | 4 | 1 | 0902ead5 |
| loco | start_points | fixed:200 | rul_mae | param_linear | 175.000 [79.750, 242.250] | 1/4 cells, 1/4 cell-seeds (vs param_power) |  | 4 | 1 | ed1477de |
| loco | start_points | fixed:200 | rul_mae | param_power | 123.750 [37.000, 275.750] |  |  | 4 | 1 | 8b8457c1 |
| loco | start_points | fixed:400 | rul_bias | gpr | 1032.250 [965.250, 1086.000] | (vs nan) |  | 4 | 1 | b01a0314 |
| loco | start_points | fixed:400 | rul_bias | param_exp2 | 197.000 [133.250, 259.250] | (vs nan) |  | 4 | 1 | 0902ead5 |
| loco | start_points | fixed:400 | rul_bias | param_linear | 35.750 [-34.250, 120.000] | (vs nan) |  | 4 | 1 | ed1477de |
| loco | start_points | fixed:400 | rul_bias | param_power | 269.500 [154.750, 422.750] | (vs nan) |  | 4 | 1 | 8b8457c1 |
| loco | start_points | fixed:400 | rul_mae | gpr | 1032.250 [965.250, 1086.000] | 0/4 cells, 0/4 cell-seeds (vs param_linear) |  | 4 | 1 | b01a0314 |
| loco | start_points | fixed:400 | rul_mae | param_exp2 | 197.000 [133.250, 259.250] | 0/4 cells, 0/4 cell-seeds (vs param_linear) |  | 4 | 1 | 0902ead5 |
| loco | start_points | fixed:400 | rul_mae | param_linear | 63.250 [21.500, 123.250] |  |  | 4 | 1 | ed1477de |
| loco | start_points | fixed:400 | rul_mae | param_power | 269.500 [154.750, 422.750] | 0/4 cells, 0/4 cell-seeds (vs param_linear) |  | 4 | 1 | 8b8457c1 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | gpr | 0.000 [0.000, 0.000] | 0/4 cells, 0/4 cell-seeds (vs param_power) |  | 4 | 1 | b01a0314 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | param_exp2 | 0.000 [0.000, 0.000] | 0/4 cells, 0/4 cell-seeds (vs param_power) |  | 4 | 1 | 0902ead5 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | param_linear | 0.000 [0.000, 0.000] | 0/4 cells, 0/4 cell-seeds (vs param_power) |  | 4 | 1 | ed1477de |
| loco | start_points | frac:0.3 | alpha_lambda_acc | param_power | 0.250 [0.000, 0.750] |  |  | 4 | 1 | 8b8457c1 |
| loco | start_points | frac:0.3 | rul_bias | gpr | 119.706 [-235.107, 592.249] | (vs nan) |  | 4 | 1 | b01a0314 |
| loco | start_points | frac:0.3 | rul_bias | param_exp2 | 546.250 [60.750, 828.000] | (vs nan) |  | 4 | 1 | 0902ead5 |
| loco | start_points | frac:0.3 | rul_bias | param_linear | -234.750 [-278.500, -169.750] | (vs nan) |  | 4 | 1 | ed1477de |
| loco | start_points | frac:0.3 | rul_bias | param_power | -16.000 [-95.500, 123.000] | (vs nan) |  | 4 | 1 | 8b8457c1 |
| loco | start_points | frac:0.3 | rul_mae | gpr | 354.813 [139.082, 690.251] | 0/4 cells, 0/4 cell-seeds (vs param_power) |  | 4 | 1 | b01a0314 |
| loco | start_points | frac:0.3 | rul_mae | param_exp2 | 639.250 [339.750, 828.000] | 0/4 cells, 0/4 cell-seeds (vs param_power) |  | 4 | 1 | 0902ead5 |
| loco | start_points | frac:0.3 | rul_mae | param_linear | 234.750 [169.750, 278.500] | 1/4 cells, 1/4 cell-seeds (vs param_power) |  | 4 | 1 | ed1477de |
| loco | start_points | frac:0.3 | rul_mae | param_power | 112.500 [75.500, 166.500] |  |  | 4 | 1 | 8b8457c1 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | gpr | 0.250 [0.000, 0.750] | 1/4 cells, 1/4 cell-seeds (vs param_linear) |  | 4 | 1 | b01a0314 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | param_exp2 | 0.000 [0.000, 0.000] | 0/4 cells, 0/4 cell-seeds (vs param_linear) |  | 4 | 1 | 0902ead5 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | param_linear | 0.500 [0.000, 1.000] |  |  | 4 | 1 | ed1477de |
| loco | start_points | frac:0.5 | alpha_lambda_acc | param_power | 0.000 [0.000, 0.000] | 0/4 cells, 0/4 cell-seeds (vs param_linear) |  | 4 | 1 | 8b8457c1 |
| loco | start_points | frac:0.5 | rul_bias | gpr | 714.882 [274.147, 945.500] | (vs nan) |  | 4 | 1 | b01a0314 |
| loco | start_points | frac:0.5 | rul_bias | param_exp2 | 862.750 [717.750, 945.500] | (vs nan) |  | 4 | 1 | 0902ead5 |
| loco | start_points | frac:0.5 | rul_bias | param_linear | -31.750 [-90.000, 35.750] | (vs nan) |  | 4 | 1 | ed1477de |
| loco | start_points | frac:0.5 | rul_bias | param_power | 268.250 [147.000, 427.250] | (vs nan) |  | 4 | 1 | 8b8457c1 |
| loco | start_points | frac:0.5 | rul_mae | gpr | 714.882 [274.147, 945.500] | 1/4 cells, 1/4 cell-seeds (vs param_linear) |  | 4 | 1 | b01a0314 |
| loco | start_points | frac:0.5 | rul_mae | param_exp2 | 862.750 [717.750, 945.500] | 0/4 cells, 0/4 cell-seeds (vs param_linear) |  | 4 | 1 | 0902ead5 |
| loco | start_points | frac:0.5 | rul_mae | param_linear | 64.250 [38.750, 95.500] |  |  | 4 | 1 | ed1477de |
| loco | start_points | frac:0.5 | rul_mae | param_power | 268.250 [147.000, 427.250] | 1/4 cells, 1/4 cell-seeds (vs param_linear) |  | 4 | 1 | 8b8457c1 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | gpr | 0.000 [0.000, 0.000] | 0/4 cells, 0/4 cell-seeds (vs param_linear) |  | 4 | 1 | b01a0314 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | param_exp2 | 0.000 [0.000, 0.000] | 0/4 cells, 0/4 cell-seeds (vs param_linear) |  | 4 | 1 | 0902ead5 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | param_linear | 0.500 [0.000, 1.000] |  |  | 4 | 1 | ed1477de |
| loco | start_points | frac:0.7 | alpha_lambda_acc | param_power | 0.000 [0.000, 0.000] | 0/4 cells, 0/4 cell-seeds (vs param_linear) |  | 4 | 1 | 8b8457c1 |
| loco | start_points | frac:0.7 | rul_bias | gpr | 1021.000 [978.750, 1048.250] | (vs nan) |  | 4 | 1 | b01a0314 |
| loco | start_points | frac:0.7 | rul_bias | param_exp2 | 221.000 [107.250, 380.250] | (vs nan) |  | 4 | 1 | 0902ead5 |
| loco | start_points | frac:0.7 | rul_bias | param_linear | 34.500 [-29.750, 124.250] | (vs nan) |  | 4 | 1 | ed1477de |
| loco | start_points | frac:0.7 | rul_bias | param_power | 285.250 [153.000, 484.750] | (vs nan) |  | 4 | 1 | 8b8457c1 |
| loco | start_points | frac:0.7 | rul_mae | gpr | 1021.000 [978.750, 1048.250] | 0/4 cells, 0/4 cell-seeds (vs param_linear) |  | 4 | 1 | b01a0314 |
| loco | start_points | frac:0.7 | rul_mae | param_exp2 | 221.000 [107.250, 380.250] | 0/4 cells, 0/4 cell-seeds (vs param_linear) |  | 4 | 1 | 0902ead5 |
| loco | start_points | frac:0.7 | rul_mae | param_linear | 57.000 [9.000, 127.750] |  |  | 4 | 1 | ed1477de |
| loco | start_points | frac:0.7 | rul_mae | param_power | 285.250 [153.000, 484.750] | 0/4 cells, 0/4 cell-seeds (vs param_linear) |  | 4 | 1 | 8b8457c1 |
| loco | start_points | overall | rul_bias | gpr | 640.299 [424.738, 857.734] | (vs nan) |  | 4 | 1 | b01a0314 |
| loco | start_points | overall | rul_bias | param_exp2 | 488.900 [317.350, 634.600] | (vs nan) |  | 4 | 1 | 0902ead5 |
| loco | start_points | overall | rul_bias | param_linear | -74.250 [-135.600, 6.750] | (vs nan) |  | 4 | 1 | ed1477de |
| loco | start_points | overall | rul_bias | param_power | 174.550 [63.050, 342.000] | (vs nan) |  | 4 | 1 | 8b8457c1 |
| loco | start_points | overall | rul_mae | gpr | 713.713 [510.684, 908.066] | 0/4 cells, 0/4 cell-seeds (vs param_linear) |  | 4 | 1 | b01a0314 |
| loco | start_points | overall | rul_mae | param_exp2 | 507.500 [373.150, 634.600] | 0/4 cells, 0/4 cell-seeds (vs param_linear) |  | 4 | 1 | 0902ead5 |
| loco | start_points | overall | rul_mae | param_linear | 118.850 [104.900, 140.550] |  |  | 4 | 1 | ed1477de |
| loco | start_points | overall | rul_mae | param_power | 211.850 [121.550, 355.400] | 1/4 cells, 1/4 cell-seeds (vs param_linear) |  | 4 | 1 | 8b8457c1 |

</details>

<details><summary>nasa_forecast (120 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | start_points | fixed:30 | rmse_h1 | gpr | 1.941 [0.832, 3.026] | 1/4 cells, 1/4 cell-seeds (vs param_exp2) | 0.347 | 4 | 1 | be2a6022 |
| loco | start_points | fixed:30 | rmse_h1 | param_exp2 | 1.690 [1.072, 2.349] |  | 0.899 | 4 | 1 | a2cb006a |
| loco | start_points | fixed:30 | rmse_h1 | param_linear | 1.954 [0.823, 3.113] | 1/4 cells, 1/4 cell-seeds (vs param_exp2) | 0.322 | 4 | 1 | b3f24bbf |
| loco | start_points | fixed:30 | rmse_h1 | param_power | 1.756 [0.805, 2.641] | 1/4 cells, 1/4 cell-seeds (vs param_exp2) | 0.323 | 4 | 1 | e5fb89a3 |
| loco | start_points | fixed:30 | rmse_h10 | gpr | 2.627 [2.207, 2.907] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 1.982 | 4 | 1 | be2a6022 |
| loco | start_points | fixed:30 | rmse_h10 | param_exp2 | 3.607 [2.457, 4.756] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 5.329 | 4 | 1 | a2cb006a |
| loco | start_points | fixed:30 | rmse_h10 | param_linear | 1.882 [1.647, 2.064] |  | 2.070 | 4 | 1 | b3f24bbf |
| loco | start_points | fixed:30 | rmse_h10 | param_power | 2.383 [1.858, 3.171] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 2.068 | 4 | 1 | e5fb89a3 |
| loco | start_points | fixed:30 | rmse_h100 | gpr | 14.870 [7.306, 22.434] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 11.101 | 4 | 1 | be2a6022 |
| loco | start_points | fixed:30 | rmse_h100 | param_exp2 | 26.376 [17.256, 39.764] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 46.538 | 4 | 1 | a2cb006a |
| loco | start_points | fixed:30 | rmse_h100 | param_linear | 11.608 [4.302, 17.119] |  | 11.553 | 4 | 1 | b3f24bbf |
| loco | start_points | fixed:30 | rmse_h100 | param_power | 16.319 [12.712, 19.926] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 11.523 | 4 | 1 | e5fb89a3 |
| loco | start_points | fixed:30 | rmse_h25 | gpr | 4.192 [2.932, 5.452] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 2.617 | 4 | 1 | be2a6022 |
| loco | start_points | fixed:30 | rmse_h25 | param_exp2 | 12.248 [5.057, 25.844] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 32.743 | 4 | 1 | a2cb006a |
| loco | start_points | fixed:30 | rmse_h25 | param_linear | 2.971 [2.229, 3.645] |  | 2.766 | 4 | 1 | b3f24bbf |
| loco | start_points | fixed:30 | rmse_h25 | param_power | 4.077 [3.209, 4.825] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 2.760 | 4 | 1 | e5fb89a3 |
| loco | start_points | fixed:30 | rmse_h50 | gpr | 8.860 [4.213, 13.506] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 1.464 | 4 | 1 | be2a6022 |
| loco | start_points | fixed:30 | rmse_h50 | param_exp2 | 20.028 [12.502, 34.149] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 41.322 | 4 | 1 | a2cb006a |
| loco | start_points | fixed:30 | rmse_h50 | param_linear | 6.851 [3.186, 10.516] |  | 1.714 | 4 | 1 | b3f24bbf |
| loco | start_points | fixed:30 | rmse_h50 | param_power | 9.142 [4.142, 11.907] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 1.702 | 4 | 1 | e5fb89a3 |
| loco | start_points | fixed:50 | rmse_h1 | gpr | 0.617 [0.399, 1.016] | 3/4 cells, 3/4 cell-seeds (vs param_power) | 1.221 | 4 | 1 | be2a6022 |
| loco | start_points | fixed:50 | rmse_h1 | param_exp2 | 1.140 [0.453, 2.401] | 1/4 cells, 1/4 cell-seeds (vs param_power) | 3.026 | 4 | 1 | a2cb006a |
| loco | start_points | fixed:50 | rmse_h1 | param_linear | 1.273 [0.582, 2.504] | 0/4 cells, 0/4 cell-seeds (vs param_power) | 3.096 | 4 | 1 | b3f24bbf |
| loco | start_points | fixed:50 | rmse_h1 | param_power | 0.945 [0.426, 1.880] |  | 2.332 | 4 | 1 | e5fb89a3 |
| loco | start_points | fixed:50 | rmse_h10 | gpr | 2.403 [1.037, 3.273] | 2/4 cells, 2/4 cell-seeds (vs param_power) | 0.297 | 4 | 1 | be2a6022 |
| loco | start_points | fixed:50 | rmse_h10 | param_exp2 | 9.257 [0.288, 25.414] | 3/4 cells, 3/4 cell-seeds (vs param_power) | 33.783 | 4 | 1 | a2cb006a |
| loco | start_points | fixed:50 | rmse_h10 | param_linear | 2.436 [1.533, 3.167] | 1/4 cells, 1/4 cell-seeds (vs param_power) | 0.996 | 4 | 1 | b3f24bbf |
| loco | start_points | fixed:50 | rmse_h10 | param_power | 1.093 [0.477, 2.222] |  | 0.437 | 4 | 1 | e5fb89a3 |
| loco | start_points | fixed:50 | rmse_h100 | gpr | 10.038 [3.601, 16.135] | 1/3 cells, 1/3 cell-seeds (vs param_linear) |  | 3 | 1 | fa89a962 |
| loco | start_points | fixed:50 | rmse_h100 | param_exp2 | 49.892 [1.196, 76.592] | 1/3 cells, 1/3 cell-seeds (vs param_linear) |  | 3 | 1 | 3bc66e1a |
| loco | start_points | fixed:50 | rmse_h100 | param_linear | 10.121 [4.826, 15.527] |  |  | 3 | 1 | 503ad3f1 |
| loco | start_points | fixed:50 | rmse_h100 | param_power | 27.079 [1.573, 43.256] | 1/3 cells, 1/3 cell-seeds (vs param_linear) |  | 3 | 1 | 7bdd5942 |
| loco | start_points | fixed:50 | rmse_h25 | gpr | 5.154 [2.941, 7.003] | 2/4 cells, 2/4 cell-seeds (vs param_power) | 1.845 | 4 | 1 | be2a6022 |
| loco | start_points | fixed:50 | rmse_h25 | param_exp2 | 11.844 [1.551, 30.048] | 2/4 cells, 2/4 cell-seeds (vs param_power) | 39.395 | 4 | 1 | a2cb006a |
| loco | start_points | fixed:50 | rmse_h25 | param_linear | 4.705 [2.194, 6.811] | 2/4 cells, 2/4 cell-seeds (vs param_power) | 0.889 | 4 | 1 | b3f24bbf |
| loco | start_points | fixed:50 | rmse_h25 | param_power | 2.594 [0.862, 4.327] |  | 3.610 | 4 | 1 | e5fb89a3 |
| loco | start_points | fixed:50 | rmse_h50 | gpr | 5.675 [1.625, 9.725] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 1.776 | 4 | 1 | be2a6022 |
| loco | start_points | fixed:50 | rmse_h50 | param_exp2 | 22.191 [7.179, 38.586] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 45.088 | 4 | 1 | a2cb006a |
| loco | start_points | fixed:50 | rmse_h50 | param_linear | 4.999 [0.551, 9.448] |  | 0.369 | 4 | 1 | b3f24bbf |
| loco | start_points | fixed:50 | rmse_h50 | param_power | 5.401 [3.042, 7.866] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 5.589 | 4 | 1 | e5fb89a3 |
| loco | start_points | frac:0.3 | rmse_h1 | gpr | 0.403 [0.261, 0.511] | 4/4 cells, 4/4 cell-seeds (vs param_power) | 0.405 | 4 | 1 | be2a6022 |
| loco | start_points | frac:0.3 | rmse_h1 | param_exp2 | 0.753 [0.523, 0.920] | 0/4 cells, 0/4 cell-seeds (vs param_power) | 0.821 | 4 | 1 | a2cb006a |
| loco | start_points | frac:0.3 | rmse_h1 | param_linear | 0.595 [0.250, 1.116] | 2/4 cells, 2/4 cell-seeds (vs param_power) | 0.478 | 4 | 1 | b3f24bbf |
| loco | start_points | frac:0.3 | rmse_h1 | param_power | 0.581 [0.369, 0.792] |  | 0.455 | 4 | 1 | e5fb89a3 |
| loco | start_points | frac:0.3 | rmse_h10 | gpr | 2.593 [1.474, 3.711] | 2/4 cells, 2/4 cell-seeds (vs param_linear) | 1.996 | 4 | 1 | be2a6022 |
| loco | start_points | frac:0.3 | rmse_h10 | param_exp2 | 29.218 [5.155, 74.315] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 8.358 | 4 | 1 | a2cb006a |
| loco | start_points | frac:0.3 | rmse_h10 | param_linear | 2.011 [0.632, 3.390] |  | 0.289 | 4 | 1 | b3f24bbf |
| loco | start_points | frac:0.3 | rmse_h10 | param_power | 3.561 [1.847, 5.666] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 3.689 | 4 | 1 | e5fb89a3 |
| loco | start_points | frac:0.3 | rmse_h100 | gpr | 16.854 [13.238, 22.298] | 2/4 cells, 2/4 cell-seeds (vs param_linear) | 15.695 | 4 | 1 | be2a6022 |
| loco | start_points | frac:0.3 | rmse_h100 | param_exp2 | 63.220 [42.657, 76.965] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 75.724 | 4 | 1 | a2cb006a |
| loco | start_points | frac:0.3 | rmse_h100 | param_linear | 19.076 [15.071, 23.081] |  | 15.980 | 4 | 1 | b3f24bbf |
| loco | start_points | frac:0.3 | rmse_h100 | param_power | 61.045 [36.131, 76.965] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 75.724 | 4 | 1 | e5fb89a3 |
| loco | start_points | frac:0.3 | rmse_h25 | gpr | 6.419 [5.245, 8.144] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 9.016 | 4 | 1 | be2a6022 |
| loco | start_points | frac:0.3 | rmse_h25 | param_exp2 | 45.290 [14.626, 75.954] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 60.862 | 4 | 1 | a2cb006a |
| loco | start_points | frac:0.3 | rmse_h25 | param_linear | 6.042 [5.236, 6.848] |  | 7.014 | 4 | 1 | b3f24bbf |
| loco | start_points | frac:0.3 | rmse_h25 | param_power | 9.349 [3.335, 15.363] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 16.825 | 4 | 1 | e5fb89a3 |
| loco | start_points | frac:0.3 | rmse_h50 | gpr | 8.790 [5.161, 12.419] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 6.330 | 4 | 1 | be2a6022 |
| loco | start_points | frac:0.3 | rmse_h50 | param_exp2 | 61.804 [33.665, 83.173] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 81.576 | 4 | 1 | a2cb006a |
| loco | start_points | frac:0.3 | rmse_h50 | param_linear | 9.213 [6.274, 11.602] |  | 4.903 | 4 | 1 | b3f24bbf |
| loco | start_points | frac:0.3 | rmse_h50 | param_power | 21.046 [12.889, 29.203] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 30.898 | 4 | 1 | e5fb89a3 |
| loco | start_points | frac:0.5 | rmse_h1 | gpr | 1.893 [0.299, 3.488] | 1/4 cells, 1/4 cell-seeds (vs param_exp2) | 3.489 | 4 | 1 | be2a6022 |
| loco | start_points | frac:0.5 | rmse_h1 | param_exp2 | 1.438 [0.175, 2.701] |  | 2.685 | 4 | 1 | a2cb006a |
| loco | start_points | frac:0.5 | rmse_h1 | param_linear | 2.450 [1.605, 3.260] | 0/4 cells, 0/4 cell-seeds (vs param_exp2) | 2.858 | 4 | 1 | b3f24bbf |
| loco | start_points | frac:0.5 | rmse_h1 | param_power | 1.633 [0.083, 3.183] | 1/4 cells, 1/4 cell-seeds (vs param_exp2) | 3.335 | 4 | 1 | e5fb89a3 |
| loco | start_points | frac:0.5 | rmse_h10 | gpr | 3.987 [3.087, 5.348] | 1/4 cells, 1/4 cell-seeds (vs param_exp2) | 6.032 | 4 | 1 | be2a6022 |
| loco | start_points | frac:0.5 | rmse_h10 | param_exp2 | 3.138 [1.438, 4.838] |  | 5.493 | 4 | 1 | a2cb006a |
| loco | start_points | frac:0.5 | rmse_h10 | param_linear | 3.848 [2.474, 5.362] | 1/4 cells, 1/4 cell-seeds (vs param_exp2) | 5.917 | 4 | 1 | b3f24bbf |
| loco | start_points | frac:0.5 | rmse_h10 | param_power | 3.175 [1.074, 5.568] | 2/4 cells, 2/4 cell-seeds (vs param_exp2) | 7.014 | 4 | 1 | e5fb89a3 |
| loco | start_points | frac:0.5 | rmse_h100 | gpr | 7.613 [3.512, 14.424] | 1/3 cells, 1/3 cell-seeds (vs param_linear) |  | 3 | 1 | fa89a962 |
| loco | start_points | frac:0.5 | rmse_h100 | param_exp2 | 54.060 [15.071, 74.944] | 0/3 cells, 0/3 cell-seeds (vs param_linear) |  | 3 | 1 | 3bc66e1a |
| loco | start_points | frac:0.5 | rmse_h100 | param_linear | 6.762 [0.640, 14.244] |  |  | 3 | 1 | 503ad3f1 |
| loco | start_points | frac:0.5 | rmse_h100 | param_power | 39.772 [13.901, 74.759] | 0/3 cells, 0/3 cell-seeds (vs param_linear) |  | 3 | 1 | 7bdd5942 |
| loco | start_points | frac:0.5 | rmse_h25 | gpr | 4.598 [3.381, 5.894] | 3/4 cells, 3/4 cell-seeds (vs param_power) | 3.514 | 4 | 1 | be2a6022 |
| loco | start_points | frac:0.5 | rmse_h25 | param_exp2 | 5.100 [1.910, 8.422] | 1/4 cells, 1/4 cell-seeds (vs param_power) | 2.357 | 4 | 1 | a2cb006a |
| loco | start_points | frac:0.5 | rmse_h25 | param_linear | 4.289 [2.625, 5.952] | 2/4 cells, 2/4 cell-seeds (vs param_power) | 3.382 | 4 | 1 | b3f24bbf |
| loco | start_points | frac:0.5 | rmse_h25 | param_power | 4.211 [1.878, 5.634] |  | 5.814 | 4 | 1 | e5fb89a3 |
| loco | start_points | frac:0.5 | rmse_h50 | gpr | 7.075 [5.472, 9.224] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 5.713 | 4 | 1 | be2a6022 |
| loco | start_points | frac:0.5 | rmse_h50 | param_exp2 | 20.961 [6.792, 40.736] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 3.030 | 4 | 1 | a2cb006a |
| loco | start_points | frac:0.5 | rmse_h50 | param_linear | 6.528 [4.896, 9.113] |  | 5.542 | 4 | 1 | b3f24bbf |
| loco | start_points | frac:0.5 | rmse_h50 | param_power | 11.598 [6.022, 17.692] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 10.866 | 4 | 1 | e5fb89a3 |
| loco | start_points | frac:0.7 | rmse_h1 | gpr | 1.320 [0.213, 3.142] | 2/4 cells, 2/4 cell-seeds (vs param_exp2) | 4.008 | 4 | 1 | be2a6022 |
| loco | start_points | frac:0.7 | rmse_h1 | param_exp2 | 0.806 [0.298, 1.200] |  | 1.306 | 4 | 1 | a2cb006a |
| loco | start_points | frac:0.7 | rmse_h1 | param_linear | 2.240 [0.766, 3.714] | 0/4 cells, 0/4 cell-seeds (vs param_exp2) | 4.164 | 4 | 1 | b3f24bbf |
| loco | start_points | frac:0.7 | rmse_h1 | param_power | 1.366 [0.380, 2.598] | 1/4 cells, 1/4 cell-seeds (vs param_exp2) | 3.315 | 4 | 1 | e5fb89a3 |
| loco | start_points | frac:0.7 | rmse_h10 | gpr | 1.348 [0.276, 2.507] | 2/4 cells, 2/4 cell-seeds (vs param_linear) | 1.611 | 4 | 1 | be2a6022 |
| loco | start_points | frac:0.7 | rmse_h10 | param_exp2 | 3.134 [0.308, 6.766] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 8.864 | 4 | 1 | a2cb006a |
| loco | start_points | frac:0.7 | rmse_h10 | param_linear | 1.515 [0.304, 3.159] |  | 1.421 | 4 | 1 | b3f24bbf |
| loco | start_points | frac:0.7 | rmse_h10 | param_power | 2.644 [1.251, 3.794] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 2.939 | 4 | 1 | e5fb89a3 |
| loco | start_points | frac:0.7 | rmse_h100 | gpr | 4.697 | 0/1 cells, 0/1 cell-seeds (vs param_exp2) |  | 1 | 1 | 8a07ba8d |
| loco | start_points | frac:0.7 | rmse_h100 | param_exp2 | 0.787 |  |  | 1 | 1 | 5fcc1a46 |
| loco | start_points | frac:0.7 | rmse_h100 | param_linear | 5.431 | 0/1 cells, 0/1 cell-seeds (vs param_exp2) |  | 1 | 1 | e025e9f3 |
| loco | start_points | frac:0.7 | rmse_h100 | param_power | 13.564 | 0/1 cells, 0/1 cell-seeds (vs param_exp2) |  | 1 | 1 | 87585a5b |
| loco | start_points | frac:0.7 | rmse_h25 | gpr | 3.331 [2.724, 3.939] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 2.765 | 4 | 1 | be2a6022 |
| loco | start_points | frac:0.7 | rmse_h25 | param_exp2 | 9.267 [2.832, 20.047] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 25.302 | 4 | 1 | a2cb006a |
| loco | start_points | frac:0.7 | rmse_h25 | param_linear | 2.674 [0.953, 4.150] |  | 2.497 | 4 | 1 | b3f24bbf |
| loco | start_points | frac:0.7 | rmse_h25 | param_power | 6.276 [3.378, 9.041] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 5.286 | 4 | 1 | e5fb89a3 |
| loco | start_points | frac:0.7 | rmse_h50 | gpr | 3.347 [1.585, 5.109] | 2/4 cells, 2/4 cell-seeds (vs param_linear) | 2.006 | 4 | 1 | be2a6022 |
| loco | start_points | frac:0.7 | rmse_h50 | param_exp2 | 15.957 [3.217, 36.208] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 46.275 | 4 | 1 | a2cb006a |
| loco | start_points | frac:0.7 | rmse_h50 | param_linear | 2.548 [1.575, 4.471] |  | 1.608 | 4 | 1 | b3f24bbf |
| loco | start_points | frac:0.7 | rmse_h50 | param_power | 14.667 [5.917, 23.416] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 6.845 | 4 | 1 | e5fb89a3 |
| loco | start_points | overall | rmse_h1 | gpr | 1.648 [0.953, 2.343] | 1/4 cells, 1/4 cell-seeds (vs param_exp2) | 2.450 | 4 | 1 | be2a6022 |
| loco | start_points | overall | rmse_h1 | param_exp2 | 1.394 [0.903, 1.885] |  | 1.977 | 4 | 1 | a2cb006a |
| loco | start_points | overall | rmse_h1 | param_linear | 2.097 [1.698, 2.495] | 0/4 cells, 0/4 cell-seeds (vs param_exp2) | 2.662 | 4 | 1 | b3f24bbf |
| loco | start_points | overall | rmse_h1 | param_power | 1.589 [1.008, 2.170] | 0/4 cells, 0/4 cell-seeds (vs param_exp2) | 2.360 | 4 | 1 | e5fb89a3 |
| loco | start_points | overall | rmse_h10 | gpr | 2.925 [2.636, 3.176] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 3.065 | 4 | 1 | be2a6022 |
| loco | start_points | overall | rmse_h10 | param_exp2 | 16.590 [3.387, 33.528] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 16.421 | 4 | 1 | a2cb006a |
| loco | start_points | overall | rmse_h10 | param_linear | 2.740 [2.458, 3.021] |  | 2.912 | 4 | 1 | b3f24bbf |
| loco | start_points | overall | rmse_h10 | param_power | 3.012 [2.102, 3.921] | 2/4 cells, 2/4 cell-seeds (vs param_linear) | 3.897 | 4 | 1 | e5fb89a3 |
| loco | start_points | overall | rmse_h100 | gpr | 13.602 [8.329, 18.834] | 2/4 cells, 2/4 cell-seeds (vs param_linear) | 13.593 | 4 | 1 | be2a6022 |
| loco | start_points | overall | rmse_h100 | param_exp2 | 54.046 [39.400, 64.944] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 62.849 | 4 | 1 | a2cb006a |
| loco | start_points | overall | rmse_h100 | param_linear | 13.776 [11.685, 16.309] |  | 13.943 | 4 | 1 | b3f24bbf |
| loco | start_points | overall | rmse_h100 | param_power | 43.410 [30.262, 56.558] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 54.161 | 4 | 1 | e5fb89a3 |
| loco | start_points | overall | rmse_h25 | gpr | 5.016 [4.322, 5.786] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 4.723 | 4 | 1 | be2a6022 |
| loco | start_points | overall | rmse_h25 | param_exp2 | 23.382 [7.524, 39.241] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 37.347 | 4 | 1 | a2cb006a |
| loco | start_points | overall | rmse_h25 | param_linear | 4.563 [3.958, 5.228] |  | 3.881 | 4 | 1 | b3f24bbf |
| loco | start_points | overall | rmse_h25 | param_power | 6.527 [5.082, 7.973] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 8.550 | 4 | 1 | e5fb89a3 |
| loco | start_points | overall | rmse_h50 | gpr | 7.334 [4.437, 10.231] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 4.050 | 4 | 1 | be2a6022 |
| loco | start_points | overall | rmse_h50 | param_exp2 | 35.375 [22.976, 47.774] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 50.091 | 4 | 1 | a2cb006a |
| loco | start_points | overall | rmse_h50 | param_linear | 6.676 [4.286, 9.066] |  | 3.476 | 4 | 1 | b3f24bbf |
| loco | start_points | overall | rmse_h50 | param_power | 14.950 [14.622, 15.236] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 15.190 | 4 | 1 | e5fb89a3 |

</details>

<details><summary>nasa_rul (60 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | start_points | fixed:30 | rul_bias | gpr | 71.672 [7.845, 135.500] | (vs nan) | -7.146 | 4 | 1 | b6daa7a6 |
| loco | start_points | fixed:30 | rul_bias | param_exp2 | 134.500 [91.000, 178.000] | (vs nan) | 192.000 | 4 | 1 | ebb632b7 |
| loco | start_points | fixed:30 | rul_bias | param_linear | 69.250 [3.000, 135.500] | (vs nan) | -8.000 | 4 | 1 | 86d5a25a |
| loco | start_points | fixed:30 | rul_bias | param_power | 81.750 [20.750, 139.000] | (vs nan) | -8.000 | 4 | 1 | 7a073d4e |
| loco | start_points | fixed:30 | rul_mae | gpr | 75.246 [14.991, 135.500] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 7.146 | 4 | 1 | b6daa7a6 |
| loco | start_points | fixed:30 | rul_mae | param_exp2 | 134.500 [91.000, 178.000] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 192.000 | 4 | 1 | ebb632b7 |
| loco | start_points | fixed:30 | rul_mae | param_linear | 73.250 [11.000, 135.500] |  | 8.000 | 4 | 1 | 86d5a25a |
| loco | start_points | fixed:30 | rul_mae | param_power | 85.750 [32.750, 139.000] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 8.000 | 4 | 1 | 7a073d4e |
| loco | start_points | fixed:50 | rul_bias | gpr | 63.129 [8.464, 117.794] | (vs nan) | 6.732 | 4 | 1 | b6daa7a6 |
| loco | start_points | fixed:50 | rul_bias | param_exp2 | 40.000 [-32.000, 153.250] | (vs nan) | 212.000 | 4 | 1 | ebb632b7 |
| loco | start_points | fixed:50 | rul_bias | param_linear | 60.500 [7.500, 113.500] | (vs nan) | 4.000 | 4 | 1 | 86d5a25a |
| loco | start_points | fixed:50 | rul_bias | param_power | -2.000 [-23.500, 19.500] | (vs nan) | 26.000 | 4 | 1 | 7a073d4e |
| loco | start_points | fixed:50 | rul_mae | gpr | 63.129 [8.464, 117.794] | 2/4 cells, 2/4 cell-seeds (vs param_power) | 6.732 | 4 | 1 | b6daa7a6 |
| loco | start_points | fixed:50 | rul_mae | param_exp2 | 72.000 [17.500, 164.750] | 1/4 cells, 1/4 cell-seeds (vs param_power) | 212.000 | 4 | 1 | ebb632b7 |
| loco | start_points | fixed:50 | rul_mae | param_linear | 60.500 [7.500, 113.500] | 2/4 cells, 2/4 cell-seeds (vs param_power) | 4.000 | 4 | 1 | 86d5a25a |
| loco | start_points | fixed:50 | rul_mae | param_power | 21.500 [13.000, 30.000] |  | 26.000 | 4 | 1 | 7a073d4e |
| loco | start_points | frac:0.3 | alpha_lambda_acc | gpr | 0.000 [0.000, 0.000] | 0/4 cells, 0/4 cell-seeds (vs param_exp2) | 0.000 | 4 | 1 | b6daa7a6 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | param_exp2 | 0.000 [0.000, 0.000] |  | 0.000 | 4 | 1 | ebb632b7 |
| loco | start_points | frac:0.3 | alpha_lambda_acc | param_linear | 0.000 [0.000, 0.000] | 0/4 cells, 0/4 cell-seeds (vs param_exp2) | 0.000 | 4 | 1 | 86d5a25a |
| loco | start_points | frac:0.3 | alpha_lambda_acc | param_power | 0.000 [0.000, 0.000] | 0/4 cells, 0/4 cell-seeds (vs param_exp2) | 0.000 | 4 | 1 | 7a073d4e |
| loco | start_points | frac:0.3 | rul_bias | gpr | 62.022 [-16.456, 140.500] | (vs nan) | -20.087 | 4 | 1 | b6daa7a6 |
| loco | start_points | frac:0.3 | rul_bias | param_exp2 | 3.250 [-68.000, 113.750] | (vs nan) | -43.000 | 4 | 1 | ebb632b7 |
| loco | start_points | frac:0.3 | rul_bias | param_linear | 62.500 [-15.500, 140.500] | (vs nan) | -14.000 | 4 | 1 | 86d5a25a |
| loco | start_points | frac:0.3 | rul_bias | param_power | 14.750 [-41.000, 115.750] | (vs nan) | -35.000 | 4 | 1 | 7a073d4e |
| loco | start_points | frac:0.3 | rul_mae | gpr | 78.478 [16.456, 140.500] | 2/4 cells, 2/4 cell-seeds (vs param_power) | 20.087 | 4 | 1 | b6daa7a6 |
| loco | start_points | frac:0.3 | rul_mae | param_exp2 | 79.750 [36.000, 135.250] | 0/4 cells, 0/4 cell-seeds (vs param_power) | 43.000 | 4 | 1 | ebb632b7 |
| loco | start_points | frac:0.3 | rul_mae | param_linear | 78.000 [15.500, 140.500] | 2/4 cells, 2/4 cell-seeds (vs param_power) | 14.000 | 4 | 1 | 86d5a25a |
| loco | start_points | frac:0.3 | rul_mae | param_power | 68.250 [30.500, 133.250] |  | 35.000 | 4 | 1 | 7a073d4e |
| loco | start_points | frac:0.5 | alpha_lambda_acc | gpr | 0.000 [0.000, 0.000] | 0/4 cells, 0/4 cell-seeds (vs param_power) | 0.000 | 4 | 1 | b6daa7a6 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | param_exp2 | 0.000 [0.000, 0.000] | 0/4 cells, 0/4 cell-seeds (vs param_power) | 0.000 | 4 | 1 | ebb632b7 |
| loco | start_points | frac:0.5 | alpha_lambda_acc | param_linear | 0.000 [0.000, 0.000] | 0/4 cells, 0/4 cell-seeds (vs param_power) | 0.000 | 4 | 1 | 86d5a25a |
| loco | start_points | frac:0.5 | alpha_lambda_acc | param_power | 0.250 [0.000, 0.750] |  | 0.000 | 4 | 1 | 7a073d4e |
| loco | start_points | frac:0.5 | rul_bias | gpr | 39.341 [-1.607, 91.698] | (vs nan) | -13.694 | 4 | 1 | b6daa7a6 |
| loco | start_points | frac:0.5 | rul_bias | param_exp2 | 0.500 [-35.250, 51.250] | (vs nan) | -9.000 | 4 | 1 | ebb632b7 |
| loco | start_points | frac:0.5 | rul_bias | param_linear | 39.750 [0.250, 92.000] | (vs nan) | -13.000 | 4 | 1 | 86d5a25a |
| loco | start_points | frac:0.5 | rul_bias | param_power | -0.500 [-31.000, 43.500] | (vs nan) | -18.000 | 4 | 1 | 7a073d4e |
| loco | start_points | frac:0.5 | rul_mae | gpr | 46.188 [17.452, 91.698] | 3/4 cells, 3/4 cell-seeds (vs param_power) | 13.694 | 4 | 1 | b6daa7a6 |
| loco | start_points | frac:0.5 | rul_mae | param_exp2 | 37.000 [14.500, 61.250] | 1/4 cells, 1/4 cell-seeds (vs param_power) | 9.000 | 4 | 1 | ebb632b7 |
| loco | start_points | frac:0.5 | rul_mae | param_linear | 46.250 [13.500, 92.000] | 2/4 cells, 2/4 cell-seeds (vs param_power) | 13.000 | 4 | 1 | 86d5a25a |
| loco | start_points | frac:0.5 | rul_mae | param_power | 32.500 [14.000, 52.500] |  | 18.000 | 4 | 1 | 7a073d4e |
| loco | start_points | frac:0.7 | alpha_lambda_acc | gpr | 0.000 [0.000, 0.000] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 0.000 | 4 | 1 | b6daa7a6 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | param_exp2 | 0.000 [0.000, 0.000] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 0.000 | 4 | 1 | ebb632b7 |
| loco | start_points | frac:0.7 | alpha_lambda_acc | param_linear | 0.250 [0.000, 0.750] |  | 0.000 | 4 | 1 | 86d5a25a |
| loco | start_points | frac:0.7 | alpha_lambda_acc | param_power | 0.000 [0.000, 0.000] | 0/4 cells, 0/4 cell-seeds (vs param_linear) | 0.000 | 4 | 1 | 7a073d4e |
| loco | start_points | frac:0.7 | rul_bias | gpr | 19.247 [7.255, 31.769] | (vs nan) | 6.550 | 4 | 1 | b6daa7a6 |
| loco | start_points | frac:0.7 | rul_bias | param_exp2 | 48.750 [-17.000, 160.500] | (vs nan) | 217.000 | 4 | 1 | ebb632b7 |
| loco | start_points | frac:0.7 | rul_bias | param_linear | 10.000 [-1.000, 23.000] | (vs nan) | 8.000 | 4 | 1 | 86d5a25a |
| loco | start_points | frac:0.7 | rul_bias | param_power | -2.750 [-23.500, 19.250] | (vs nan) | 32.000 | 4 | 1 | 7a073d4e |
| loco | start_points | frac:0.7 | rul_mae | gpr | 19.247 [7.255, 31.769] | 3/4 cells, 3/4 cell-seeds (vs param_linear) | 6.550 | 4 | 1 | b6daa7a6 |
| loco | start_points | frac:0.7 | rul_mae | param_exp2 | 65.750 [10.500, 165.750] | 1/4 cells, 1/4 cell-seeds (vs param_linear) | 217.000 | 4 | 1 | ebb632b7 |
| loco | start_points | frac:0.7 | rul_mae | param_linear | 12.000 [5.000, 23.000] |  | 8.000 | 4 | 1 | 86d5a25a |
| loco | start_points | frac:0.7 | rul_mae | param_power | 20.750 [10.000, 30.000] | 2/4 cells, 2/4 cell-seeds (vs param_linear) | 32.000 | 4 | 1 | 7a073d4e |
| loco | start_points | overall | rul_bias | gpr | 51.082 [2.173, 99.991] | (vs nan) | -5.529 | 4 | 1 | b6daa7a6 |
| loco | start_points | overall | rul_bias | param_exp2 | 45.400 [1.300, 92.600] | (vs nan) | 113.800 | 4 | 1 | ebb632b7 |
| loco | start_points | overall | rul_bias | param_linear | 48.400 [0.700, 96.100] | (vs nan) | -4.600 | 4 | 1 | 86d5a25a |
| loco | start_points | overall | rul_bias | param_power | 18.250 [-4.200, 43.050] | (vs nan) | -0.600 | 4 | 1 | 7a073d4e |
| loco | start_points | overall | rul_mae | gpr | 56.458 [12.924, 99.991] | 2/4 cells, 2/4 cell-seeds (vs param_power) | 10.842 | 4 | 1 | b6daa7a6 |
| loco | start_points | overall | rul_mae | param_exp2 | 77.800 [49.550, 115.850] | 0/4 cells, 0/4 cell-seeds (vs param_power) | 134.600 | 4 | 1 | ebb632b7 |
| loco | start_points | overall | rul_mae | param_linear | 54.000 [11.100, 96.900] | 2/4 cells, 2/4 cell-seeds (vs param_power) | 9.400 | 4 | 1 | 86d5a25a |
| loco | start_points | overall | rul_mae | param_power | 45.750 [29.000, 64.350] |  | 23.800 | 4 | 1 | 7a073d4e |

</details>

<details><summary>toyota_forecast (200 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | start_points | fixed:100 | rmse_h1 | gpr | 0.010 [0.007, 0.014] | p=1.49e-07 (vs param_power) |  | 43 | 1 | e2d7a35c |
| test1 | start_points | fixed:100 | rmse_h1 | param_exp2 | 0.067 [0.058, 0.077] | p=1.96e-09 (vs param_power) |  | 43 | 1 | 8ccdd557 |
| test1 | start_points | fixed:100 | rmse_h1 | param_linear | 0.123 [0.100, 0.155] | p=6.82e-13 (vs param_power) |  | 43 | 1 | e7a9712a |
| test1 | start_points | fixed:100 | rmse_h1 | param_power | 0.028 [0.022, 0.035] |  |  | 43 | 1 | 792c2b20 |
| test1 | start_points | fixed:100 | rmse_h10 | gpr | 0.074 [0.053, 0.097] | p=0.168 (vs param_power) |  | 43 | 1 | e2d7a35c |
| test1 | start_points | fixed:100 | rmse_h10 | param_exp2 | 0.116 [0.104, 0.128] | p=1.96e-09 (vs param_power) |  | 43 | 1 | 8ccdd557 |
| test1 | start_points | fixed:100 | rmse_h10 | param_linear | 0.188 [0.148, 0.246] | p=6.82e-13 (vs param_power) |  | 43 | 1 | e7a9712a |
| test1 | start_points | fixed:100 | rmse_h10 | param_power | 0.048 [0.039, 0.059] |  |  | 43 | 1 | 792c2b20 |
| test1 | start_points | fixed:100 | rmse_h100 | gpr | 0.955 [0.698, 1.289] | p=0.0676 (vs param_power) |  | 42 | 1 | e2d7a35c |
| test1 | start_points | fixed:100 | rmse_h100 | param_exp2 | 1.595 [1.467, 1.729] | p=5.06e-10 (vs param_power) |  | 42 | 1 | 8ccdd557 |
| test1 | start_points | fixed:100 | rmse_h100 | param_linear | 0.857 [0.716, 1.022] | p=0.059 (vs param_power) |  | 42 | 1 | e7a9712a |
| test1 | start_points | fixed:100 | rmse_h100 | param_power | 0.682 [0.522, 0.866] |  |  | 42 | 1 | 792c2b20 |
| test1 | start_points | fixed:100 | rmse_h200 | gpr | 2.245 [1.707, 2.943] | p=1 (vs param_linear) |  | 42 | 1 | e2d7a35c |
| test1 | start_points | fixed:100 | rmse_h200 | param_exp2 | 5.726 [5.197, 6.280] | p=1.36e-12 (vs param_linear) |  | 42 | 1 | 8ccdd557 |
| test1 | start_points | fixed:100 | rmse_h200 | param_linear | 2.023 [1.664, 2.437] |  |  | 42 | 1 | e7a9712a |
| test1 | start_points | fixed:100 | rmse_h200 | param_power | 2.648 [1.927, 3.494] | p=1 (vs param_linear) |  | 42 | 1 | 792c2b20 |
| test1 | start_points | fixed:100 | rmse_h50 | gpr | 0.485 [0.329, 0.687] | p=6.04e-06 (vs param_power) |  | 43 | 1 | e2d7a35c |
| test1 | start_points | fixed:100 | rmse_h50 | param_exp2 | 0.550 [0.507, 0.594] | p=8.86e-09 (vs param_power) |  | 43 | 1 | 8ccdd557 |
| test1 | start_points | fixed:100 | rmse_h50 | param_linear | 0.522 [0.382, 0.740] | p=8.83e-08 (vs param_power) |  | 43 | 1 | e7a9712a |
| test1 | start_points | fixed:100 | rmse_h50 | param_power | 0.241 [0.185, 0.306] |  |  | 43 | 1 | 792c2b20 |
| test1 | start_points | frac:0.3 | rmse_h1 | gpr | 0.022 [0.015, 0.031] | p=6.35e-05 (vs param_power) |  | 43 | 1 | e2d7a35c |
| test1 | start_points | frac:0.3 | rmse_h1 | param_exp2 | 0.091 [0.063, 0.131] | p=6.31e-07 (vs param_power) |  | 43 | 1 | 8ccdd557 |
| test1 | start_points | frac:0.3 | rmse_h1 | param_linear | 0.164 [0.140, 0.189] | p=1.47e-07 (vs param_power) |  | 43 | 1 | e7a9712a |
| test1 | start_points | frac:0.3 | rmse_h1 | param_power | 0.057 [0.037, 0.085] |  |  | 43 | 1 | 792c2b20 |
| test1 | start_points | frac:0.3 | rmse_h10 | gpr | 0.111 [0.075, 0.153] | p=0.052 (vs param_power) |  | 43 | 1 | e2d7a35c |
| test1 | start_points | frac:0.3 | rmse_h10 | param_exp2 | 0.111 [0.084, 0.149] | p=1.5e-05 (vs param_power) |  | 43 | 1 | 8ccdd557 |
| test1 | start_points | frac:0.3 | rmse_h10 | param_linear | 0.218 [0.180, 0.260] | p=8.6e-10 (vs param_power) |  | 43 | 1 | e7a9712a |
| test1 | start_points | frac:0.3 | rmse_h10 | param_power | 0.065 [0.052, 0.079] |  |  | 43 | 1 | 792c2b20 |
| test1 | start_points | frac:0.3 | rmse_h100 | gpr | 1.380 [0.917, 2.011] | p=6.61e-06 (vs param_power) |  | 43 | 1 | e2d7a35c |
| test1 | start_points | frac:0.3 | rmse_h100 | param_exp2 | 0.912 [0.640, 1.313] | p=8.64e-07 (vs param_power) |  | 43 | 1 | 8ccdd557 |
| test1 | start_points | frac:0.3 | rmse_h100 | param_linear | 0.987 [0.697, 1.397] | p=1.33e-05 (vs param_power) |  | 43 | 1 | e7a9712a |
| test1 | start_points | frac:0.3 | rmse_h100 | param_power | 0.504 [0.399, 0.611] |  |  | 43 | 1 | 792c2b20 |
| test1 | start_points | frac:0.3 | rmse_h200 | gpr | 2.754 [2.085, 3.532] | p=4.08e-05 (vs param_power) |  | 42 | 1 | e2d7a35c |
| test1 | start_points | frac:0.3 | rmse_h200 | param_exp2 | 2.284 [1.715, 2.925] | p=0.00404 (vs param_power) |  | 42 | 1 | 8ccdd557 |
| test1 | start_points | frac:0.3 | rmse_h200 | param_linear | 2.097 [1.641, 2.590] | p=0.00578 (vs param_power) |  | 42 | 1 | e7a9712a |
| test1 | start_points | frac:0.3 | rmse_h200 | param_power | 1.551 [1.161, 1.963] |  |  | 42 | 1 | 792c2b20 |
| test1 | start_points | frac:0.3 | rmse_h50 | gpr | 0.573 [0.385, 0.822] | p=1.75e-05 (vs param_power) |  | 43 | 1 | e2d7a35c |
| test1 | start_points | frac:0.3 | rmse_h50 | param_exp2 | 0.391 [0.284, 0.539] | p=3.91e-08 (vs param_power) |  | 43 | 1 | 8ccdd557 |
| test1 | start_points | frac:0.3 | rmse_h50 | param_linear | 0.477 [0.365, 0.626] | p=1.08e-06 (vs param_power) |  | 43 | 1 | e7a9712a |
| test1 | start_points | frac:0.3 | rmse_h50 | param_power | 0.203 [0.161, 0.250] |  |  | 43 | 1 | 792c2b20 |
| test1 | start_points | frac:0.5 | rmse_h1 | gpr | 0.067 [0.031, 0.112] | p=0.000782 (vs param_power) |  | 43 | 1 | e2d7a35c |
| test1 | start_points | frac:0.5 | rmse_h1 | param_exp2 | 0.180 [0.084, 0.313] | p=0.000782 (vs param_power) |  | 43 | 1 | 8ccdd557 |
| test1 | start_points | frac:0.5 | rmse_h1 | param_linear | 0.296 [0.253, 0.343] | p=1.36e-06 (vs param_power) |  | 43 | 1 | e7a9712a |
| test1 | start_points | frac:0.5 | rmse_h1 | param_power | 0.092 [0.059, 0.130] |  |  | 43 | 1 | 792c2b20 |
| test1 | start_points | frac:0.5 | rmse_h10 | gpr | 0.134 [0.091, 0.185] | p=0.184 (vs param_power) |  | 43 | 1 | e2d7a35c |
| test1 | start_points | frac:0.5 | rmse_h10 | param_exp2 | 0.371 [0.114, 0.800] | p=0.00466 (vs param_power) |  | 43 | 1 | 8ccdd557 |
| test1 | start_points | frac:0.5 | rmse_h10 | param_linear | 0.356 [0.302, 0.413] | p=4.87e-06 (vs param_power) |  | 43 | 1 | e7a9712a |
| test1 | start_points | frac:0.5 | rmse_h10 | param_power | 0.119 [0.078, 0.167] |  |  | 43 | 1 | 792c2b20 |
| test1 | start_points | frac:0.5 | rmse_h100 | gpr | 1.210 [0.961, 1.502] | p=2.03e-05 (vs param_power) |  | 42 | 1 | e2d7a35c |
| test1 | start_points | frac:0.5 | rmse_h100 | param_exp2 | 5.101 [0.444, 12.004] | p=0.196 (vs param_power) |  | 42 | 1 | 8ccdd557 |
| test1 | start_points | frac:0.5 | rmse_h100 | param_linear | 1.331 [1.116, 1.557] | p=4.38e-09 (vs param_power) |  | 42 | 1 | e7a9712a |
| test1 | start_points | frac:0.5 | rmse_h100 | param_power | 0.450 [0.318, 0.609] |  |  | 42 | 1 | 792c2b20 |
| test1 | start_points | frac:0.5 | rmse_h200 | gpr | 5.165 [4.275, 6.107] | p=2.73e-12 (vs param_power) |  | 41 | 1 | e2d7a35c |
| test1 | start_points | frac:0.5 | rmse_h200 | param_exp2 | 6.847 [2.266, 13.357] | p=0.175 (vs param_power) |  | 41 | 1 | 8ccdd557 |
| test1 | start_points | frac:0.5 | rmse_h200 | param_linear | 5.193 [4.129, 6.286] | p=9.09e-12 (vs param_power) |  | 41 | 1 | e7a9712a |
| test1 | start_points | frac:0.5 | rmse_h200 | param_power | 2.225 [1.682, 2.844] |  |  | 41 | 1 | 792c2b20 |
| test1 | start_points | frac:0.5 | rmse_h50 | gpr | 0.529 [0.391, 0.688] | p=0.00779 (vs param_power) |  | 43 | 1 | e2d7a35c |
| test1 | start_points | frac:0.5 | rmse_h50 | param_exp2 | 3.459 [0.273, 8.886] | p=0.102 (vs param_power) |  | 43 | 1 | 8ccdd557 |
| test1 | start_points | frac:0.5 | rmse_h50 | param_linear | 0.684 [0.548, 0.852] | p=1.24e-06 (vs param_power) |  | 43 | 1 | e7a9712a |
| test1 | start_points | frac:0.5 | rmse_h50 | param_power | 0.256 [0.178, 0.350] |  |  | 43 | 1 | 792c2b20 |
| test1 | start_points | frac:0.7 | rmse_h1 | gpr | 0.072 [0.040, 0.111] | p=0.00224 (vs param_exp2) |  | 43 | 1 | e2d7a35c |
| test1 | start_points | frac:0.7 | rmse_h1 | param_exp2 | 0.130 [0.089, 0.188] |  |  | 43 | 1 | 8ccdd557 |
| test1 | start_points | frac:0.7 | rmse_h1 | param_linear | 0.813 [0.725, 0.896] | p=5.72e-08 (vs param_exp2) |  | 43 | 1 | e7a9712a |
| test1 | start_points | frac:0.7 | rmse_h1 | param_power | 0.173 [0.140, 0.208] | p=0.00224 (vs param_exp2) |  | 43 | 1 | 792c2b20 |
| test1 | start_points | frac:0.7 | rmse_h10 | gpr | 0.173 [0.118, 0.240] | p=0.242 (vs param_exp2) |  | 43 | 1 | e2d7a35c |
| test1 | start_points | frac:0.7 | rmse_h10 | param_exp2 | 0.220 [0.152, 0.304] |  |  | 43 | 1 | 8ccdd557 |
| test1 | start_points | frac:0.7 | rmse_h10 | param_linear | 1.013 [0.894, 1.133] | p=4.94e-08 (vs param_exp2) |  | 43 | 1 | e7a9712a |
| test1 | start_points | frac:0.7 | rmse_h10 | param_power | 0.264 [0.210, 0.329] | p=0.00531 (vs param_exp2) |  | 43 | 1 | 792c2b20 |
| test1 | start_points | frac:0.7 | rmse_h100 | gpr | 4.220 [3.599, 4.851] | p=2.37e-09 (vs param_exp2) |  | 42 | 1 | e2d7a35c |
| test1 | start_points | frac:0.7 | rmse_h100 | param_exp2 | 2.463 [1.923, 3.024] |  |  | 42 | 1 | 8ccdd557 |
| test1 | start_points | frac:0.7 | rmse_h100 | param_linear | 4.955 [4.253, 5.656] | p=5.63e-08 (vs param_exp2) |  | 42 | 1 | e7a9712a |
| test1 | start_points | frac:0.7 | rmse_h100 | param_power | 2.925 [2.479, 3.377] | p=0.000183 (vs param_exp2) |  | 42 | 1 | 792c2b20 |
| test1 | start_points | frac:0.7 | rmse_h200 | gpr | 8.528 [6.671, 10.390] | p=9.16e-05 (vs param_exp2) |  | 17 | 1 | e2d7a35c |
| test1 | start_points | frac:0.7 | rmse_h200 | param_exp2 | 3.769 [2.526, 5.126] |  |  | 17 | 1 | 8ccdd557 |
| test1 | start_points | frac:0.7 | rmse_h200 | param_linear | 8.080 [6.386, 9.735] | p=9.16e-05 (vs param_exp2) |  | 17 | 1 | e7a9712a |
| test1 | start_points | frac:0.7 | rmse_h200 | param_power | 6.276 [4.842, 7.659] | p=0.000504 (vs param_exp2) |  | 17 | 1 | 792c2b20 |
| test1 | start_points | frac:0.7 | rmse_h50 | gpr | 1.237 [1.048, 1.434] | p=8.96e-06 (vs param_exp2) |  | 43 | 1 | e2d7a35c |
| test1 | start_points | frac:0.7 | rmse_h50 | param_exp2 | 0.724 [0.582, 0.888] |  |  | 43 | 1 | 8ccdd557 |
| test1 | start_points | frac:0.7 | rmse_h50 | param_linear | 2.146 [1.883, 2.406] | p=5.72e-08 (vs param_exp2) |  | 43 | 1 | e7a9712a |
| test1 | start_points | frac:0.7 | rmse_h50 | param_power | 0.880 [0.773, 0.985] | p=0.00112 (vs param_exp2) |  | 43 | 1 | 792c2b20 |
| test1 | start_points | overall | rmse_h1 | gpr | 0.060 [0.036, 0.088] | p=4.47e-06 (vs param_power) |  | 43 | 1 | e2d7a35c |
| test1 | start_points | overall | rmse_h1 | param_exp2 | 0.151 [0.099, 0.219] | p=0.9 (vs param_power) |  | 43 | 1 | 8ccdd557 |
| test1 | start_points | overall | rmse_h1 | param_linear | 0.455 [0.410, 0.497] | p=3.41e-12 (vs param_power) |  | 43 | 1 | e7a9712a |
| test1 | start_points | overall | rmse_h1 | param_power | 0.119 [0.098, 0.141] |  |  | 43 | 1 | 792c2b20 |
| test1 | start_points | overall | rmse_h10 | gpr | 0.153 [0.118, 0.192] | p=0.352 (vs param_power) |  | 43 | 1 | e2d7a35c |
| test1 | start_points | overall | rmse_h10 | param_exp2 | 0.288 [0.155, 0.496] | p=0.562 (vs param_power) |  | 43 | 1 | 8ccdd557 |
| test1 | start_points | overall | rmse_h10 | param_linear | 0.569 [0.506, 0.633] | p=2.05e-12 (vs param_power) |  | 43 | 1 | e7a9712a |
| test1 | start_points | overall | rmse_h10 | param_power | 0.167 [0.137, 0.201] |  |  | 43 | 1 | 792c2b20 |
| test1 | start_points | overall | rmse_h100 | gpr | 2.676 [2.238, 3.220] | p=2.5e-11 (vs param_power) |  | 43 | 1 | e2d7a35c |
| test1 | start_points | overall | rmse_h100 | param_exp2 | 3.948 [1.637, 7.251] | p=0.227 (vs param_power) |  | 43 | 1 | 8ccdd557 |
| test1 | start_points | overall | rmse_h100 | param_linear | 2.787 [2.376, 3.216] | p=2.25e-11 (vs param_power) |  | 43 | 1 | e7a9712a |
| test1 | start_points | overall | rmse_h100 | param_power | 1.594 [1.383, 1.801] |  |  | 43 | 1 | 792c2b20 |
| test1 | start_points | overall | rmse_h200 | gpr | 4.963 [4.349, 5.629] | p=1.19e-08 (vs param_power) |  | 42 | 1 | e2d7a35c |
| test1 | start_points | overall | rmse_h200 | param_exp2 | 6.512 [4.019, 10.028] | p=0.00076 (vs param_power) |  | 42 | 1 | 8ccdd557 |
| test1 | start_points | overall | rmse_h200 | param_linear | 4.692 [4.143, 5.227] | p=1.28e-07 (vs param_power) |  | 42 | 1 | e7a9712a |
| test1 | start_points | overall | rmse_h200 | param_power | 3.219 [2.741, 3.729] |  |  | 42 | 1 | 792c2b20 |
| test1 | start_points | overall | rmse_h50 | gpr | 0.866 [0.734, 1.026] | p=1.26e-09 (vs param_power) |  | 43 | 1 | e2d7a35c |
| test1 | start_points | overall | rmse_h50 | param_exp2 | 2.115 [0.529, 4.807] | p=0.0899 (vs param_power) |  | 43 | 1 | 8ccdd557 |
| test1 | start_points | overall | rmse_h50 | param_linear | 1.211 [1.049, 1.394] | p=3.41e-12 (vs param_power) |  | 43 | 1 | e7a9712a |
| test1 | start_points | overall | rmse_h50 | param_power | 0.518 [0.463, 0.574] |  |  | 43 | 1 | 792c2b20 |
| test2 | start_points | fixed:100 | rmse_h1 | gpr | 0.008 [0.005, 0.011] | p=1.13e-05 (vs param_power) |  | 40 | 1 | e2d7a35c |
| test2 | start_points | fixed:100 | rmse_h1 | param_exp2 | 0.044 [0.040, 0.048] | p=6.91e-11 (vs param_power) |  | 40 | 1 | 8ccdd557 |
| test2 | start_points | fixed:100 | rmse_h1 | param_linear | 0.065 [0.058, 0.071] | p=1.09e-11 (vs param_power) |  | 40 | 1 | e7a9712a |
| test2 | start_points | fixed:100 | rmse_h1 | param_power | 0.018 [0.014, 0.022] |  |  | 40 | 1 | 792c2b20 |
| test2 | start_points | fixed:100 | rmse_h10 | gpr | 0.038 [0.029, 0.049] | p=0.188 (vs param_power) |  | 40 | 1 | e2d7a35c |
| test2 | start_points | fixed:100 | rmse_h10 | param_exp2 | 0.090 [0.080, 0.099] | p=8.64e-09 (vs param_power) |  | 40 | 1 | 8ccdd557 |
| test2 | start_points | fixed:100 | rmse_h10 | param_linear | 0.083 [0.074, 0.093] | p=1.64e-11 (vs param_power) |  | 40 | 1 | e7a9712a |
| test2 | start_points | fixed:100 | rmse_h10 | param_power | 0.028 [0.023, 0.034] |  |  | 40 | 1 | 792c2b20 |
| test2 | start_points | fixed:100 | rmse_h100 | gpr | 0.465 [0.366, 0.601] | p=0.128 (vs param_linear) |  | 40 | 1 | e2d7a35c |
| test2 | start_points | fixed:100 | rmse_h100 | param_exp2 | 1.061 [0.931, 1.180] | p=2.32e-07 (vs param_linear) |  | 40 | 1 | 8ccdd557 |
| test2 | start_points | fixed:100 | rmse_h100 | param_linear | 0.330 [0.291, 0.369] |  |  | 40 | 1 | e7a9712a |
| test2 | start_points | fixed:100 | rmse_h100 | param_power | 0.437 [0.347, 0.532] | p=0.128 (vs param_linear) |  | 40 | 1 | 792c2b20 |
| test2 | start_points | fixed:100 | rmse_h200 | gpr | 1.002 [0.821, 1.255] | p=0.00057 (vs param_linear) |  | 40 | 1 | e2d7a35c |
| test2 | start_points | fixed:100 | rmse_h200 | param_exp2 | 3.561 [3.082, 3.998] | p=2.73e-07 (vs param_linear) |  | 40 | 1 | 8ccdd557 |
| test2 | start_points | fixed:100 | rmse_h200 | param_linear | 0.681 [0.600, 0.761] |  |  | 40 | 1 | e7a9712a |
| test2 | start_points | fixed:100 | rmse_h200 | param_power | 1.853 [1.460, 2.256] | p=1.27e-05 (vs param_linear) |  | 40 | 1 | 792c2b20 |
| test2 | start_points | fixed:100 | rmse_h50 | gpr | 0.185 [0.136, 0.249] | p=0.536 (vs param_power) |  | 40 | 1 | e2d7a35c |
| test2 | start_points | fixed:100 | rmse_h50 | param_exp2 | 0.403 [0.360, 0.443] | p=3e-10 (vs param_power) |  | 40 | 1 | 8ccdd557 |
| test2 | start_points | fixed:100 | rmse_h50 | param_linear | 0.170 [0.148, 0.192] | p=0.485 (vs param_power) |  | 40 | 1 | e7a9712a |
| test2 | start_points | fixed:100 | rmse_h50 | param_power | 0.143 [0.114, 0.173] |  |  | 40 | 1 | 792c2b20 |
| test2 | start_points | frac:0.3 | rmse_h1 | gpr | 0.013 [0.006, 0.023] | p=1.13e-05 (vs param_power) |  | 40 | 1 | e2d7a35c |
| test2 | start_points | frac:0.3 | rmse_h1 | param_exp2 | 0.053 [0.046, 0.059] | p=1.85e-07 (vs param_power) |  | 40 | 1 | 8ccdd557 |
| test2 | start_points | frac:0.3 | rmse_h1 | param_linear | 0.085 [0.076, 0.097] | p=2.73e-11 (vs param_power) |  | 40 | 1 | e7a9712a |
| test2 | start_points | frac:0.3 | rmse_h1 | param_power | 0.028 [0.022, 0.034] |  |  | 40 | 1 | 792c2b20 |
| test2 | start_points | frac:0.3 | rmse_h10 | gpr | 0.030 [0.024, 0.036] | p=0.837 (vs param_power) |  | 40 | 1 | e2d7a35c |
| test2 | start_points | frac:0.3 | rmse_h10 | param_exp2 | 0.062 [0.054, 0.070] | p=1.56e-10 (vs param_power) |  | 40 | 1 | 8ccdd557 |
| test2 | start_points | frac:0.3 | rmse_h10 | param_linear | 0.098 [0.091, 0.105] | p=2.73e-11 (vs param_power) |  | 40 | 1 | e7a9712a |
| test2 | start_points | frac:0.3 | rmse_h10 | param_power | 0.029 [0.023, 0.036] |  |  | 40 | 1 | 792c2b20 |
| test2 | start_points | frac:0.3 | rmse_h100 | gpr | 0.380 [0.305, 0.464] | p=1.01e-08 (vs param_power) |  | 40 | 1 | e2d7a35c |
| test2 | start_points | frac:0.3 | rmse_h100 | param_exp2 | 0.226 [0.195, 0.263] | p=9.22e-10 (vs param_power) |  | 40 | 1 | 8ccdd557 |
| test2 | start_points | frac:0.3 | rmse_h100 | param_linear | 0.259 [0.225, 0.294] | p=3.14e-07 (vs param_power) |  | 40 | 1 | e7a9712a |
| test2 | start_points | frac:0.3 | rmse_h100 | param_power | 0.126 [0.099, 0.155] |  |  | 40 | 1 | 792c2b20 |
| test2 | start_points | frac:0.3 | rmse_h200 | gpr | 0.882 [0.711, 1.090] | p=3.29e-09 (vs param_power) |  | 40 | 1 | e2d7a35c |
| test2 | start_points | frac:0.3 | rmse_h200 | param_exp2 | 0.522 [0.440, 0.617] | p=4.8e-10 (vs param_power) |  | 40 | 1 | 8ccdd557 |
| test2 | start_points | frac:0.3 | rmse_h200 | param_linear | 0.540 [0.471, 0.609] | p=6.78e-09 (vs param_power) |  | 40 | 1 | e7a9712a |
| test2 | start_points | frac:0.3 | rmse_h200 | param_power | 0.264 [0.199, 0.339] |  |  | 40 | 1 | 792c2b20 |
| test2 | start_points | frac:0.3 | rmse_h50 | gpr | 0.178 [0.142, 0.219] | p=6.78e-09 (vs param_power) |  | 40 | 1 | e2d7a35c |
| test2 | start_points | frac:0.3 | rmse_h50 | param_exp2 | 0.121 [0.106, 0.137] | p=1.95e-09 (vs param_power) |  | 40 | 1 | 8ccdd557 |
| test2 | start_points | frac:0.3 | rmse_h50 | param_linear | 0.177 [0.154, 0.208] | p=2.73e-11 (vs param_power) |  | 40 | 1 | e7a9712a |
| test2 | start_points | frac:0.3 | rmse_h50 | param_power | 0.064 [0.051, 0.079] |  |  | 40 | 1 | 792c2b20 |
| test2 | start_points | frac:0.5 | rmse_h1 | gpr | 0.009 [0.005, 0.014] | p=3.72e-06 (vs param_power) |  | 40 | 1 | e2d7a35c |
| test2 | start_points | frac:0.5 | rmse_h1 | param_exp2 | 0.050 [0.037, 0.066] | p=8.25e-05 (vs param_power) |  | 40 | 1 | 8ccdd557 |
| test2 | start_points | frac:0.5 | rmse_h1 | param_linear | 0.148 [0.126, 0.169] | p=2.73e-11 (vs param_power) |  | 40 | 1 | e7a9712a |
| test2 | start_points | frac:0.5 | rmse_h1 | param_power | 0.022 [0.017, 0.028] |  |  | 40 | 1 | 792c2b20 |
| test2 | start_points | frac:0.5 | rmse_h10 | gpr | 0.029 [0.019, 0.043] | p=0.973 (vs param_power) |  | 40 | 1 | e2d7a35c |
| test2 | start_points | frac:0.5 | rmse_h10 | param_exp2 | 0.056 [0.041, 0.074] | p=0.00221 (vs param_power) |  | 40 | 1 | 8ccdd557 |
| test2 | start_points | frac:0.5 | rmse_h10 | param_linear | 0.171 [0.144, 0.197] | p=2.73e-11 (vs param_power) |  | 40 | 1 | e7a9712a |
| test2 | start_points | frac:0.5 | rmse_h10 | param_power | 0.027 [0.020, 0.035] |  |  | 40 | 1 | 792c2b20 |
| test2 | start_points | frac:0.5 | rmse_h100 | gpr | 0.345 [0.269, 0.429] | p=1.17e-08 (vs param_power) |  | 40 | 1 | e2d7a35c |
| test2 | start_points | frac:0.5 | rmse_h100 | param_exp2 | 0.148 [0.103, 0.202] | p=0.39 (vs param_power) |  | 40 | 1 | 8ccdd557 |
| test2 | start_points | frac:0.5 | rmse_h100 | param_linear | 0.455 [0.378, 0.530] | p=1.04e-10 (vs param_power) |  | 40 | 1 | e7a9712a |
| test2 | start_points | frac:0.5 | rmse_h100 | param_power | 0.114 [0.091, 0.139] |  |  | 40 | 1 | 792c2b20 |
| test2 | start_points | frac:0.5 | rmse_h200 | gpr | 1.165 [0.969, 1.372] | p=1.14e-05 (vs param_exp2) |  | 40 | 1 | e2d7a35c |
| test2 | start_points | frac:0.5 | rmse_h200 | param_exp2 | 0.522 [0.385, 0.681] |  |  | 40 | 1 | 8ccdd557 |
| test2 | start_points | frac:0.5 | rmse_h200 | param_linear | 1.145 [0.948, 1.344] | p=0.000126 (vs param_exp2) |  | 40 | 1 | e7a9712a |
| test2 | start_points | frac:0.5 | rmse_h200 | param_power | 0.529 [0.419, 0.649] | p=0.307 (vs param_exp2) |  | 40 | 1 | 792c2b20 |
| test2 | start_points | frac:0.5 | rmse_h50 | gpr | 0.125 [0.086, 0.175] | p=4.46e-06 (vs param_power) |  | 40 | 1 | e2d7a35c |
| test2 | start_points | frac:0.5 | rmse_h50 | param_exp2 | 0.085 [0.059, 0.114] | p=0.0125 (vs param_power) |  | 40 | 1 | 8ccdd557 |
| test2 | start_points | frac:0.5 | rmse_h50 | param_linear | 0.270 [0.229, 0.310] | p=1.09e-11 (vs param_power) |  | 40 | 1 | e7a9712a |
| test2 | start_points | frac:0.5 | rmse_h50 | param_power | 0.044 [0.035, 0.053] |  |  | 40 | 1 | 792c2b20 |
| test2 | start_points | frac:0.7 | rmse_h1 | gpr | 0.010 [0.005, 0.017] | p=5.08e-05 (vs param_exp2) |  | 40 | 1 | e2d7a35c |
| test2 | start_points | frac:0.7 | rmse_h1 | param_exp2 | 0.036 [0.023, 0.053] |  |  | 40 | 1 | 8ccdd557 |
| test2 | start_points | frac:0.7 | rmse_h1 | param_linear | 0.384 [0.325, 0.442] | p=2.95e-07 (vs param_exp2) |  | 40 | 1 | e7a9712a |
| test2 | start_points | frac:0.7 | rmse_h1 | param_power | 0.128 [0.109, 0.148] | p=1.29e-06 (vs param_exp2) |  | 40 | 1 | 792c2b20 |
| test2 | start_points | frac:0.7 | rmse_h10 | gpr | 0.021 [0.016, 0.027] | p=0.0842 (vs param_exp2) |  | 40 | 1 | e2d7a35c |
| test2 | start_points | frac:0.7 | rmse_h10 | param_exp2 | 0.044 [0.029, 0.063] |  |  | 40 | 1 | 8ccdd557 |
| test2 | start_points | frac:0.7 | rmse_h10 | param_linear | 0.443 [0.375, 0.513] | p=2.95e-07 (vs param_exp2) |  | 40 | 1 | e7a9712a |
| test2 | start_points | frac:0.7 | rmse_h10 | param_power | 0.162 [0.136, 0.188] | p=6.98e-07 (vs param_exp2) |  | 40 | 1 | 792c2b20 |
| test2 | start_points | frac:0.7 | rmse_h100 | gpr | 0.827 [0.715, 0.944] | p=1.04e-05 (vs param_exp2) |  | 40 | 1 | e2d7a35c |
| test2 | start_points | frac:0.7 | rmse_h100 | param_exp2 | 0.671 [0.336, 1.251] |  |  | 40 | 1 | 8ccdd557 |
| test2 | start_points | frac:0.7 | rmse_h100 | param_linear | 1.550 [1.321, 1.778] | p=4.38e-06 (vs param_exp2) |  | 40 | 1 | e7a9712a |
| test2 | start_points | frac:0.7 | rmse_h100 | param_power | 0.965 [0.826, 1.104] | p=3.17e-06 (vs param_exp2) |  | 40 | 1 | 792c2b20 |
| test2 | start_points | frac:0.7 | rmse_h200 | gpr | 4.489 [3.855, 5.153] | p=0.0512 (vs param_power) |  | 38 | 1 | e2d7a35c |
| test2 | start_points | frac:0.7 | rmse_h200 | param_exp2 | 4.722 [2.175, 9.400] | p=1.04e-06 (vs param_power) |  | 38 | 1 | 8ccdd557 |
| test2 | start_points | frac:0.7 | rmse_h200 | param_linear | 5.236 [4.444, 6.065] | p=4.37e-11 (vs param_power) |  | 38 | 1 | e7a9712a |
| test2 | start_points | frac:0.7 | rmse_h200 | param_power | 4.201 [3.585, 4.842] |  |  | 38 | 1 | 792c2b20 |
| test2 | start_points | frac:0.7 | rmse_h50 | gpr | 0.209 [0.178, 0.245] | p=0.0013 (vs param_exp2) |  | 40 | 1 | e2d7a35c |
| test2 | start_points | frac:0.7 | rmse_h50 | param_exp2 | 0.156 [0.098, 0.242] |  |  | 40 | 1 | 8ccdd557 |
| test2 | start_points | frac:0.7 | rmse_h50 | param_linear | 0.807 [0.685, 0.930] | p=1.2e-06 (vs param_exp2) |  | 40 | 1 | e7a9712a |
| test2 | start_points | frac:0.7 | rmse_h50 | param_power | 0.400 [0.339, 0.464] | p=2.56e-06 (vs param_exp2) |  | 40 | 1 | 792c2b20 |
| test2 | start_points | overall | rmse_h1 | gpr | 0.013 [0.009, 0.019] | p=9.09e-11 (vs param_exp2) |  | 40 | 1 | e2d7a35c |
| test2 | start_points | overall | rmse_h1 | param_exp2 | 0.054 [0.047, 0.062] |  |  | 40 | 1 | 8ccdd557 |
| test2 | start_points | overall | rmse_h1 | param_linear | 0.216 [0.186, 0.245] | p=1.09e-11 (vs param_exp2) |  | 40 | 1 | e7a9712a |
| test2 | start_points | overall | rmse_h1 | param_power | 0.069 [0.059, 0.079] | p=0.0299 (vs param_exp2) |  | 40 | 1 | 792c2b20 |
| test2 | start_points | overall | rmse_h10 | gpr | 0.036 [0.030, 0.043] | p=2.4e-08 (vs param_exp2) |  | 40 | 1 | e2d7a35c |
| test2 | start_points | overall | rmse_h10 | param_exp2 | 0.075 [0.069, 0.082] |  |  | 40 | 1 | 8ccdd557 |
| test2 | start_points | overall | rmse_h10 | param_linear | 0.250 [0.216, 0.285] | p=7.64e-11 (vs param_exp2) |  | 40 | 1 | e7a9712a |
| test2 | start_points | overall | rmse_h10 | param_power | 0.087 [0.074, 0.100] | p=0.118 (vs param_exp2) |  | 40 | 1 | 792c2b20 |
| test2 | start_points | overall | rmse_h100 | gpr | 0.578 [0.507, 0.659] | p=0.765 (vs param_power) |  | 40 | 1 | e2d7a35c |
| test2 | start_points | overall | rmse_h100 | param_exp2 | 0.752 [0.594, 1.016] | p=0.0464 (vs param_power) |  | 40 | 1 | 8ccdd557 |
| test2 | start_points | overall | rmse_h100 | param_linear | 0.843 [0.725, 0.961] | p=4.9e-07 (vs param_power) |  | 40 | 1 | e7a9712a |
| test2 | start_points | overall | rmse_h100 | param_power | 0.571 [0.509, 0.633] |  |  | 40 | 1 | 792c2b20 |
| test2 | start_points | overall | rmse_h200 | gpr | 2.445 [2.139, 2.755] | p=1 (vs param_power) |  | 40 | 1 | e2d7a35c |
| test2 | start_points | overall | rmse_h200 | param_exp2 | 3.350 [2.154, 5.503] | p=1 (vs param_power) |  | 40 | 1 | 8ccdd557 |
| test2 | start_points | overall | rmse_h200 | param_linear | 2.640 [2.238, 3.044] | p=0.0332 (vs param_power) |  | 40 | 1 | e7a9712a |
| test2 | start_points | overall | rmse_h200 | param_power | 2.378 [2.087, 2.663] |  |  | 40 | 1 | 792c2b20 |
| test2 | start_points | overall | rmse_h50 | gpr | 0.199 [0.169, 0.236] | p=0.0598 (vs param_power) |  | 40 | 1 | e2d7a35c |
| test2 | start_points | overall | rmse_h50 | param_exp2 | 0.254 [0.230, 0.286] | p=0.0747 (vs param_power) |  | 40 | 1 | 8ccdd557 |
| test2 | start_points | overall | rmse_h50 | param_linear | 0.449 [0.387, 0.512] | p=2.73e-11 (vs param_power) |  | 40 | 1 | e7a9712a |
| test2 | start_points | overall | rmse_h50 | param_power | 0.227 [0.199, 0.256] |  |  | 40 | 1 | 792c2b20 |

</details>

<details><summary>toyota_rul (104 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | start_points | fixed:100 | rul_bias | gpr | 3521.288 [3272.804, 3720.466] | (vs nan) |  | 43 | 1 | 80fc29b8 |
| test1 | start_points | fixed:100 | rul_bias | param_exp2 | -288.837 [-408.117, -192.158] | (vs nan) |  | 43 | 1 | 794099a2 |
| test1 | start_points | fixed:100 | rul_bias | param_linear | 3301.791 [2988.712, 3569.199] | (vs nan) |  | 43 | 1 | 30134392 |
| test1 | start_points | fixed:100 | rul_bias | param_power | 1091.767 [591.218, 1625.385] | (vs nan) |  | 43 | 1 | 9c9b46d7 |
| test1 | start_points | fixed:100 | rul_mae | gpr | 3521.288 [3272.804, 3720.466] | p=3.36e-08 (vs param_exp2) |  | 43 | 1 | 80fc29b8 |
| test1 | start_points | fixed:100 | rul_mae | param_exp2 | 288.837 [192.158, 408.117] |  |  | 43 | 1 | 794099a2 |
| test1 | start_points | fixed:100 | rul_mae | param_linear | 3301.791 [2988.712, 3569.199] | p=3.36e-08 (vs param_exp2) |  | 43 | 1 | 30134392 |
| test1 | start_points | fixed:100 | rul_mae | param_power | 1296.186 [836.190, 1785.792] | p=0.0126 (vs param_exp2) |  | 43 | 1 | 9c9b46d7 |
| test1 | start_points | frac:0.3 | alpha_lambda_acc | gpr | 0.000 [0.000, 0.000] | p=1.38e-05 (vs param_exp2) |  | 43 | 1 | 80fc29b8 |
| test1 | start_points | frac:0.3 | alpha_lambda_acc | param_exp2 | 0.488 [0.349, 0.628] |  |  | 43 | 1 | 794099a2 |
| test1 | start_points | frac:0.3 | alpha_lambda_acc | param_linear | 0.000 [0.000, 0.000] | p=1.38e-05 (vs param_exp2) |  | 43 | 1 | 30134392 |
| test1 | start_points | frac:0.3 | alpha_lambda_acc | param_power | 0.465 [0.326, 0.605] | p=0.782 (vs param_exp2) |  | 43 | 1 | 9c9b46d7 |
| test1 | start_points | frac:0.3 | rul_bias | gpr | 3583.993 [3322.252, 3791.762] | (vs nan) |  | 43 | 1 | 80fc29b8 |
| test1 | start_points | frac:0.3 | rul_bias | param_exp2 | 209.256 [35.139, 445.048] | (vs nan) |  | 43 | 1 | 794099a2 |
| test1 | start_points | frac:0.3 | rul_bias | param_linear | 3190.279 [2827.766, 3512.124] | (vs nan) |  | 43 | 1 | 30134392 |
| test1 | start_points | frac:0.3 | rul_bias | param_power | 352.674 [185.254, 569.351] | (vs nan) |  | 43 | 1 | 9c9b46d7 |
| test1 | start_points | frac:0.3 | rul_mae | gpr | 3583.993 [3322.252, 3791.762] | p=7.27e-08 (vs param_exp2) |  | 43 | 1 | 80fc29b8 |
| test1 | start_points | frac:0.3 | rul_mae | param_exp2 | 286.930 [120.883, 516.608] |  |  | 43 | 1 | 794099a2 |
| test1 | start_points | frac:0.3 | rul_mae | param_linear | 3190.279 [2827.766, 3512.124] | p=7.27e-08 (vs param_exp2) |  | 43 | 1 | 30134392 |
| test1 | start_points | frac:0.3 | rul_mae | param_power | 370.721 [207.836, 584.860] | p=0.0278 (vs param_exp2) |  | 43 | 1 | 9c9b46d7 |
| test1 | start_points | frac:0.5 | alpha_lambda_acc | gpr | 0.000 [0.000, 0.000] | p=0.0245 (vs param_exp2) |  | 43 | 1 | 80fc29b8 |
| test1 | start_points | frac:0.5 | alpha_lambda_acc | param_exp2 | 0.163 [0.070, 0.279] |  |  | 43 | 1 | 794099a2 |
| test1 | start_points | frac:0.5 | alpha_lambda_acc | param_linear | 0.000 [0.000, 0.000] | p=0.0245 (vs param_exp2) |  | 43 | 1 | 30134392 |
| test1 | start_points | frac:0.5 | alpha_lambda_acc | param_power | 0.116 [0.023, 0.209] | p=0.527 (vs param_exp2) |  | 43 | 1 | 9c9b46d7 |
| test1 | start_points | frac:0.5 | rul_bias | gpr | 2823.070 [2431.250, 3197.024] | (vs nan) |  | 43 | 1 | 80fc29b8 |
| test1 | start_points | frac:0.5 | rul_bias | param_exp2 | 512.070 [263.320, 810.893] | (vs nan) |  | 43 | 1 | 794099a2 |
| test1 | start_points | frac:0.5 | rul_bias | param_linear | 2624.140 [2245.255, 2976.796] | (vs nan) |  | 43 | 1 | 30134392 |
| test1 | start_points | frac:0.5 | rul_bias | param_power | 605.512 [394.431, 851.583] | (vs nan) |  | 43 | 1 | 9c9b46d7 |
| test1 | start_points | frac:0.5 | rul_mae | gpr | 2823.070 [2431.250, 3197.024] | p=1.31e-07 (vs param_exp2) |  | 43 | 1 | 80fc29b8 |
| test1 | start_points | frac:0.5 | rul_mae | param_exp2 | 540.256 [298.395, 833.891] |  |  | 43 | 1 | 794099a2 |
| test1 | start_points | frac:0.5 | rul_mae | param_linear | 2624.140 [2245.255, 2976.796] | p=1.46e-07 (vs param_exp2) |  | 43 | 1 | 30134392 |
| test1 | start_points | frac:0.5 | rul_mae | param_power | 606.349 [395.138, 852.006] | p=0.0305 (vs param_exp2) |  | 43 | 1 | 9c9b46d7 |
| test1 | start_points | frac:0.7 | alpha_lambda_acc | gpr | 0.000 [0.000, 0.000] | p=0.0081 (vs param_exp2) |  | 43 | 1 | 80fc29b8 |
| test1 | start_points | frac:0.7 | alpha_lambda_acc | param_exp2 | 0.209 [0.093, 0.326] |  |  | 43 | 1 | 794099a2 |
| test1 | start_points | frac:0.7 | alpha_lambda_acc | param_linear | 0.000 [0.000, 0.000] | p=0.0081 (vs param_exp2) |  | 43 | 1 | 30134392 |
| test1 | start_points | frac:0.7 | alpha_lambda_acc | param_power | 0.047 [0.000, 0.116] | p=0.00815 (vs param_exp2) |  | 43 | 1 | 9c9b46d7 |
| test1 | start_points | frac:0.7 | rul_bias | gpr | 2391.763 [1917.110, 2862.244] | (vs nan) |  | 43 | 1 | 80fc29b8 |
| test1 | start_points | frac:0.7 | rul_bias | param_exp2 | 223.140 [109.046, 376.195] | (vs nan) |  | 43 | 1 | 794099a2 |
| test1 | start_points | frac:0.7 | rul_bias | param_linear | 1571.674 [1361.418, 1768.863] | (vs nan) |  | 43 | 1 | 30134392 |
| test1 | start_points | frac:0.7 | rul_bias | param_power | 374.930 [253.115, 559.865] | (vs nan) |  | 43 | 1 | 9c9b46d7 |
| test1 | start_points | frac:0.7 | rul_mae | gpr | 2391.763 [1917.110, 2862.244] | p=6.82e-13 (vs param_exp2) |  | 43 | 1 | 80fc29b8 |
| test1 | start_points | frac:0.7 | rul_mae | param_exp2 | 239.047 [127.512, 390.630] |  |  | 43 | 1 | 794099a2 |
| test1 | start_points | frac:0.7 | rul_mae | param_linear | 1571.674 [1361.418, 1768.863] | p=6.08e-08 (vs param_exp2) |  | 43 | 1 | 30134392 |
| test1 | start_points | frac:0.7 | rul_mae | param_power | 381.535 [263.044, 565.140] | p=3.63e-05 (vs param_exp2) |  | 43 | 1 | 9c9b46d7 |
| test1 | start_points | overall | rul_bias | gpr | 3080.028 [2826.128, 3302.523] | (vs nan) |  | 43 | 1 | 80fc29b8 |
| test1 | start_points | overall | rul_bias | param_exp2 | 163.907 [90.217, 250.963] | (vs nan) |  | 43 | 1 | 794099a2 |
| test1 | start_points | overall | rul_bias | param_linear | 2671.971 [2377.517, 2930.799] | (vs nan) |  | 43 | 1 | 30134392 |
| test1 | start_points | overall | rul_bias | param_power | 606.221 [436.807, 786.942] | (vs nan) |  | 43 | 1 | 9c9b46d7 |
| test1 | start_points | overall | rul_mae | gpr | 3080.028 [2826.128, 3302.523] | p=6.82e-13 (vs param_exp2) |  | 43 | 1 | 80fc29b8 |
| test1 | start_points | overall | rul_mae | param_exp2 | 338.767 [227.033, 471.331] |  |  | 43 | 1 | 794099a2 |
| test1 | start_points | overall | rul_mae | param_linear | 2671.971 [2377.517, 2930.799] | p=6.82e-13 (vs param_exp2) |  | 43 | 1 | 30134392 |
| test1 | start_points | overall | rul_mae | param_power | 663.698 [498.200, 838.117] | p=3.73e-05 (vs param_exp2) |  | 43 | 1 | 9c9b46d7 |
| test2 | start_points | fixed:100 | rul_bias | gpr | 3288.021 [3144.913, 3411.028] | (vs nan) |  | 40 | 1 | 80fc29b8 |
| test2 | start_points | fixed:100 | rul_bias | param_exp2 | -293.725 [-511.053, -13.297] | (vs nan) |  | 40 | 1 | 794099a2 |
| test2 | start_points | fixed:100 | rul_bias | param_linear | 3120.550 [2825.996, 3356.151] | (vs nan) |  | 40 | 1 | 30134392 |
| test2 | start_points | fixed:100 | rul_bias | param_power | -117.100 [-417.477, 259.579] | (vs nan) |  | 40 | 1 | 9c9b46d7 |
| test2 | start_points | fixed:100 | rul_mae | gpr | 3288.021 [3144.913, 3411.028] | p=2.32e-07 (vs param_exp2) |  | 40 | 1 | 80fc29b8 |
| test2 | start_points | fixed:100 | rul_mae | param_exp2 | 639.625 [488.900, 836.706] |  |  | 40 | 1 | 794099a2 |
| test2 | start_points | fixed:100 | rul_mae | param_linear | 3120.550 [2825.996, 3356.151] | p=2.92e-07 (vs param_exp2) |  | 40 | 1 | 30134392 |
| test2 | start_points | fixed:100 | rul_mae | param_power | 692.450 [451.874, 986.099] | p=0.0174 (vs param_exp2) |  | 40 | 1 | 9c9b46d7 |
| test2 | start_points | frac:0.3 | alpha_lambda_acc | gpr | 0.000 [0.000, 0.000] | p=0.472 (vs param_exp2) |  | 40 | 1 | 80fc29b8 |
| test2 | start_points | frac:0.3 | alpha_lambda_acc | param_exp2 | 0.050 [0.000, 0.125] |  |  | 40 | 1 | 794099a2 |
| test2 | start_points | frac:0.3 | alpha_lambda_acc | param_linear | 0.000 [0.000, 0.000] | p=0.472 (vs param_exp2) |  | 40 | 1 | 30134392 |
| test2 | start_points | frac:0.3 | alpha_lambda_acc | param_power | 0.050 [0.000, 0.125] | p=1 (vs param_exp2) |  | 40 | 1 | 9c9b46d7 |
| test2 | start_points | frac:0.3 | rul_bias | gpr | 3276.996 [2998.593, 3496.349] | (vs nan) |  | 40 | 1 | 80fc29b8 |
| test2 | start_points | frac:0.3 | rul_bias | param_exp2 | 1044.575 [646.168, 1462.504] | (vs nan) |  | 40 | 1 | 794099a2 |
| test2 | start_points | frac:0.3 | rul_bias | param_linear | 3312.725 [2999.391, 3556.451] | (vs nan) |  | 40 | 1 | 30134392 |
| test2 | start_points | frac:0.3 | rul_bias | param_power | 764.750 [631.422, 899.702] | (vs nan) |  | 40 | 1 | 9c9b46d7 |
| test2 | start_points | frac:0.3 | rul_mae | gpr | 3276.996 [2998.593, 3496.349] | p=5.46e-12 (vs param_power) |  | 40 | 1 | 80fc29b8 |
| test2 | start_points | frac:0.3 | rul_mae | param_exp2 | 1046.125 [647.596, 1463.301] | p=0.563 (vs param_power) |  | 40 | 1 | 794099a2 |
| test2 | start_points | frac:0.3 | rul_mae | param_linear | 3312.725 [2999.391, 3556.451] | p=5.46e-12 (vs param_power) |  | 40 | 1 | 30134392 |
| test2 | start_points | frac:0.3 | rul_mae | param_power | 764.750 [631.422, 899.702] |  |  | 40 | 1 | 9c9b46d7 |
| test2 | start_points | frac:0.5 | alpha_lambda_acc | gpr | 0.000 [0.000, 0.000] | p=1 (vs param_exp2) |  | 40 | 1 | 80fc29b8 |
| test2 | start_points | frac:0.5 | alpha_lambda_acc | param_exp2 | 0.000 [0.000, 0.000] |  |  | 40 | 1 | 794099a2 |
| test2 | start_points | frac:0.5 | alpha_lambda_acc | param_linear | 0.000 [0.000, 0.000] | p=1 (vs param_exp2) |  | 40 | 1 | 30134392 |
| test2 | start_points | frac:0.5 | alpha_lambda_acc | param_power | 0.000 [0.000, 0.000] | p=1 (vs param_exp2) |  | 40 | 1 | 9c9b46d7 |
| test2 | start_points | frac:0.5 | rul_bias | gpr | 3078.825 [2762.099, 3364.483] | (vs nan) |  | 40 | 1 | 80fc29b8 |
| test2 | start_points | frac:0.5 | rul_bias | param_exp2 | 1484.700 [1088.248, 1891.011] | (vs nan) |  | 40 | 1 | 794099a2 |
| test2 | start_points | frac:0.5 | rul_bias | param_linear | 3058.900 [2753.472, 3316.254] | (vs nan) |  | 40 | 1 | 30134392 |
| test2 | start_points | frac:0.5 | rul_bias | param_power | 1215.225 [1039.347, 1395.791] | (vs nan) |  | 40 | 1 | 9c9b46d7 |
| test2 | start_points | frac:0.5 | rul_mae | gpr | 3078.825 [2762.099, 3364.483] | p=5.46e-12 (vs param_power) |  | 40 | 1 | 80fc29b8 |
| test2 | start_points | frac:0.5 | rul_mae | param_exp2 | 1484.700 [1088.248, 1891.011] | p=0.46 (vs param_power) |  | 40 | 1 | 794099a2 |
| test2 | start_points | frac:0.5 | rul_mae | param_linear | 3058.900 [2753.472, 3316.254] | p=1.82e-11 (vs param_power) |  | 40 | 1 | 30134392 |
| test2 | start_points | frac:0.5 | rul_mae | param_power | 1215.225 [1039.347, 1395.791] |  |  | 40 | 1 | 9c9b46d7 |
| test2 | start_points | frac:0.7 | alpha_lambda_acc | gpr | 0.000 [0.000, 0.000] | p=0.137 (vs param_exp2) |  | 40 | 1 | 80fc29b8 |
| test2 | start_points | frac:0.7 | alpha_lambda_acc | param_exp2 | 0.100 [0.025, 0.200] |  |  | 40 | 1 | 794099a2 |
| test2 | start_points | frac:0.7 | alpha_lambda_acc | param_linear | 0.000 [0.000, 0.000] | p=0.137 (vs param_exp2) |  | 40 | 1 | 30134392 |
| test2 | start_points | frac:0.7 | alpha_lambda_acc | param_power | 0.000 [0.000, 0.000] | p=0.137 (vs param_exp2) |  | 40 | 1 | 9c9b46d7 |
| test2 | start_points | frac:0.7 | rul_bias | gpr | 2598.655 [2216.732, 2983.373] | (vs nan) |  | 40 | 1 | 80fc29b8 |
| test2 | start_points | frac:0.7 | rul_bias | param_exp2 | 370.375 [185.099, 599.801] | (vs nan) |  | 40 | 1 | 794099a2 |
| test2 | start_points | frac:0.7 | rul_bias | param_linear | 2056.575 [1858.924, 2227.456] | (vs nan) |  | 40 | 1 | 30134392 |
| test2 | start_points | frac:0.7 | rul_bias | param_power | 867.000 [750.172, 988.186] | (vs nan) |  | 40 | 1 | 9c9b46d7 |
| test2 | start_points | frac:0.7 | rul_mae | gpr | 2598.655 [2216.732, 2983.373] | p=3.82e-11 (vs param_exp2) |  | 40 | 1 | 80fc29b8 |
| test2 | start_points | frac:0.7 | rul_mae | param_exp2 | 383.675 [199.798, 611.951] |  |  | 40 | 1 | 794099a2 |
| test2 | start_points | frac:0.7 | rul_mae | param_linear | 2056.575 [1858.924, 2227.456] | p=2.71e-07 (vs param_exp2) |  | 40 | 1 | 30134392 |
| test2 | start_points | frac:0.7 | rul_mae | param_power | 867.000 [750.172, 988.186] | p=0.000177 (vs param_exp2) |  | 40 | 1 | 9c9b46d7 |
| test2 | start_points | overall | rul_bias | gpr | 3060.624 [2833.148, 3260.136] | (vs nan) |  | 40 | 1 | 80fc29b8 |
| test2 | start_points | overall | rul_bias | param_exp2 | 651.481 [449.081, 866.176] | (vs nan) |  | 40 | 1 | 794099a2 |
| test2 | start_points | overall | rul_bias | param_linear | 2887.188 [2618.159, 3100.594] | (vs nan) |  | 40 | 1 | 30134392 |
| test2 | start_points | overall | rul_bias | param_power | 682.469 [593.486, 776.676] | (vs nan) |  | 40 | 1 | 9c9b46d7 |
| test2 | start_points | overall | rul_mae | gpr | 3060.624 [2833.148, 3260.136] | p=5.46e-12 (vs param_power) |  | 40 | 1 | 80fc29b8 |
| test2 | start_points | overall | rul_mae | param_exp2 | 888.531 [670.975, 1121.205] | p=0.727 (vs param_power) |  | 40 | 1 | 794099a2 |
| test2 | start_points | overall | rul_mae | param_linear | 2887.188 [2618.159, 3100.594] | p=5.46e-12 (vs param_power) |  | 40 | 1 | 30134392 |
| test2 | start_points | overall | rul_mae | param_power | 884.856 [765.147, 1007.612] |  |  | 40 | 1 | 9c9b46d7 |

</details>
