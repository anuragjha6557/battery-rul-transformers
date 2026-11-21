# Benchmark tables: field_screen_field_curve

- Protocol version: 1.1
- Git SHA: f1b71738cc
- Seeds: 3  |  unit runs: 189
- Note: n = 4 cells per NASA/CALCE dataset, so the 95 % cluster-bootstrap CI is wide by construction. Toyota rows are over test cells (test1 / test2 separately) with a cell-level bootstrap CI and a Holm-adjusted Wilcoxon p vs the best baseline. All metrics are computed per cell from the logged predictions.

## Headline (kind = overall; RMSE in %SOH, RUL MAE in cycles)

### calce_soh

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse | age_only | 6.887 [4.966, 8.809] |  |  | 4 | 3 | 21c6e382 |
| loco | all | overall | rmse | elasticnet | 3.603 [2.142, 5.766] |  |  | 4 | 3 | 3ae1400b |
| loco | all | overall | rmse | itransformer | 2.713 [2.212, 3.152] |  |  | 4 | 3 | c36c8628 |
| loco | all | overall | rmse | lgbm | 4.146 [2.276, 5.591] |  |  | 4 | 3 | a77ef1ab |
| loco | all | overall | rmse | lstm | 2.088 [1.545, 2.768] |  |  | 4 | 3 | f42e5c04 |
| loco | all | overall | rmse | patchtst | 7.267 [6.331, 8.711] |  |  | 4 | 3 | 8e3ccaba |
| loco | all | overall | rmse | transformer | 3.073 [2.362, 4.381] |  |  | 4 | 3 | bd101e5c |
| loco | start_points | overall | rmse | age_only | 1.172 [0.494, 1.884] |  |  | 4 | 3 | 21c6e382 |
| loco | start_points | overall | rmse | elasticnet | 2.410 [1.258, 3.637] |  |  | 4 | 3 | 3ae1400b |
| loco | start_points | overall | rmse | itransformer | 2.387 [1.232, 4.051] |  |  | 4 | 3 | c36c8628 |
| loco | start_points | overall | rmse | lgbm | 1.473 [0.671, 2.785] |  |  | 4 | 3 | a77ef1ab |
| loco | start_points | overall | rmse | lstm | 0.891 [0.647, 1.217] |  |  | 4 | 3 | f42e5c04 |
| loco | start_points | overall | rmse | patchtst | 4.678 [3.454, 6.040] |  |  | 4 | 3 | 8e3ccaba |
| loco | start_points | overall | rmse | transformer | 2.028 [1.287, 3.408] |  |  | 4 | 3 | bd101e5c |

### nasa_soh

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse | age_only | 5.846 [3.492, 8.201] |  | 2.929 | 4 | 3 | 02186163 |
| loco | all | overall | rmse | elasticnet | 5.418 [2.669, 8.031] |  | 9.019 | 4 | 3 | 5bcb6177 |
| loco | all | overall | rmse | itransformer | 4.733 [3.412, 6.083] |  | 5.279 | 4 | 3 | c221bf8d |
| loco | all | overall | rmse | lgbm | 3.942 [2.615, 6.502] |  | 2.631 | 4 | 3 | 2a3bb4b2 |
| loco | all | overall | rmse | lstm | 4.408 [3.418, 5.994] |  | 3.281 | 4 | 3 | 5c694671 |
| loco | all | overall | rmse | patchtst | 5.955 [4.069, 7.981] |  | 6.502 | 4 | 3 | ac582d2d |
| loco | all | overall | rmse | transformer | 7.543 [5.555, 9.719] |  | 10.512 | 4 | 3 | 9cfee0d0 |
| loco | start_points | overall | rmse | age_only | 5.033 [4.479, 5.367] |  | 4.212 | 4 | 3 | 02186163 |
| loco | start_points | overall | rmse | elasticnet | 5.621 [2.732, 7.712] |  | 7.034 | 4 | 3 | 5bcb6177 |
| loco | start_points | overall | rmse | itransformer | 4.005 [2.819, 5.313] |  | 6.063 | 4 | 3 | c221bf8d |
| loco | start_points | overall | rmse | lgbm | 3.259 [2.382, 4.136] |  | 1.932 | 4 | 3 | 2a3bb4b2 |
| loco | start_points | overall | rmse | lstm | 3.898 [2.790, 4.848] |  | 2.109 | 4 | 3 | 5c694671 |
| loco | start_points | overall | rmse | patchtst | 5.439 [4.528, 6.602] |  | 7.221 | 4 | 3 | ac582d2d |
| loco | start_points | overall | rmse | transformer | 5.714 [4.986, 6.730] |  | 5.049 | 4 | 3 | 9cfee0d0 |

### toyota_soh

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rmse | age_only | 4.008 [3.665, 4.471] |  |  | 43 | 3 | c47576b8 |
| test1 | all | overall | rmse | elasticnet | 1.177 [0.939, 1.479] |  |  | 43 | 3 | 9804e441 |
| test1 | all | overall | rmse | itransformer | 1.186 [0.959, 1.462] |  |  | 43 | 3 | 0ae36223 |
| test1 | all | overall | rmse | lgbm | 0.923 [0.711, 1.216] |  |  | 43 | 3 | d75ab198 |
| test1 | all | overall | rmse | lstm | 1.061 [0.839, 1.333] |  |  | 43 | 3 | 93a466eb |
| test1 | all | overall | rmse | patchtst | 1.851 [1.630, 2.115] |  |  | 43 | 3 | 9ab9f000 |
| test1 | all | overall | rmse | transformer | 0.914 [0.636, 1.260] |  |  | 43 | 3 | 9daafdbf |
| test1 | start_points | overall | rmse | age_only | 2.168 [1.705, 2.664] |  |  | 43 | 3 | c47576b8 |
| test1 | start_points | overall | rmse | elasticnet | 0.911 [0.660, 1.237] |  |  | 43 | 3 | 9804e441 |
| test1 | start_points | overall | rmse | itransformer | 0.940 [0.732, 1.196] |  |  | 43 | 3 | 0ae36223 |
| test1 | start_points | overall | rmse | lgbm | 0.541 [0.372, 0.763] |  |  | 43 | 3 | d75ab198 |
| test1 | start_points | overall | rmse | lstm | 0.839 [0.600, 1.140] |  |  | 43 | 3 | 93a466eb |
| test1 | start_points | overall | rmse | patchtst | 1.244 [1.072, 1.432] |  |  | 43 | 3 | 9ab9f000 |
| test1 | start_points | overall | rmse | transformer | 0.737 [0.465, 1.082] |  |  | 43 | 3 | 9daafdbf |
| test2 | all | overall | rmse | age_only | 3.673 [3.520, 3.821] |  |  | 40 | 3 | c47576b8 |
| test2 | all | overall | rmse | elasticnet | 11.902 [9.743, 14.328] |  |  | 40 | 3 | 9804e441 |
| test2 | all | overall | rmse | itransformer | 2.267 [2.097, 2.470] |  |  | 40 | 3 | 0ae36223 |
| test2 | all | overall | rmse | lgbm | 2.584 [2.459, 2.716] |  |  | 40 | 3 | d75ab198 |
| test2 | all | overall | rmse | lstm | 2.260 [2.090, 2.460] |  |  | 40 | 3 | 93a466eb |
| test2 | all | overall | rmse | patchtst | 3.235 [3.083, 3.414] |  |  | 40 | 3 | 9ab9f000 |
| test2 | all | overall | rmse | transformer | 2.027 [1.943, 2.115] |  |  | 40 | 3 | 9daafdbf |
| test2 | start_points | overall | rmse | age_only | 3.509 [3.286, 3.718] |  |  | 40 | 3 | c47576b8 |
| test2 | start_points | overall | rmse | elasticnet | 1.600 [1.426, 1.772] |  |  | 40 | 3 | 9804e441 |
| test2 | start_points | overall | rmse | itransformer | 1.292 [0.961, 1.665] |  |  | 40 | 3 | 0ae36223 |
| test2 | start_points | overall | rmse | lgbm | 1.338 [1.149, 1.519] |  |  | 40 | 3 | d75ab198 |
| test2 | start_points | overall | rmse | lstm | 1.241 [1.110, 1.373] |  |  | 40 | 3 | 93a466eb |
| test2 | start_points | overall | rmse | patchtst | 1.288 [1.017, 1.624] |  |  | 40 | 3 | 9ab9f000 |
| test2 | start_points | overall | rmse | transformer | 1.349 [1.204, 1.486] |  |  | 40 | 3 | 9daafdbf |

## Mean rank (dataset x task x split x policy x headline metric)

| model | mean rank | conditions | missing |
|---|---|---|---|
| lstm | 1.88 | 8 | 0 |
| lgbm | 2.62 | 8 | 0 |
| itransformer | 3.62 | 8 | 0 |
| transformer | 3.75 | 8 | 0 |
| elasticnet | 5.12 | 8 | 0 |
| age_only | 5.50 | 8 | 0 |
| patchtst | 5.50 | 8 | 0 |

## Full tables

<details><summary>calce_soh (49 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse | age_only | 6.887 [4.966, 8.809] |  |  | 4 | 3 | 21c6e382 |
| loco | all | overall | rmse | elasticnet | 3.603 [2.142, 5.766] |  |  | 4 | 3 | 3ae1400b |
| loco | all | overall | rmse | itransformer | 2.713 [2.212, 3.152] |  |  | 4 | 3 | c36c8628 |
| loco | all | overall | rmse | lgbm | 4.146 [2.276, 5.591] |  |  | 4 | 3 | a77ef1ab |
| loco | all | overall | rmse | lstm | 2.088 [1.545, 2.768] |  |  | 4 | 3 | f42e5c04 |
| loco | all | overall | rmse | patchtst | 7.267 [6.331, 8.711] |  |  | 4 | 3 | 8e3ccaba |
| loco | all | overall | rmse | transformer | 3.073 [2.362, 4.381] |  |  | 4 | 3 | bd101e5c |
| loco | start_points | fixed:200 | rmse | age_only | 1.381 [0.763, 1.760] |  |  | 4 | 3 | 21c6e382 |
| loco | start_points | fixed:200 | rmse | elasticnet | 2.265 [1.001, 3.529] |  |  | 4 | 3 | 3ae1400b |
| loco | start_points | fixed:200 | rmse | itransformer | 2.745 [1.152, 5.402] |  |  | 4 | 3 | c36c8628 |
| loco | start_points | fixed:200 | rmse | lgbm | 0.511 [0.168, 0.853] |  |  | 4 | 3 | a77ef1ab |
| loco | start_points | fixed:200 | rmse | lstm | 1.120 [0.896, 1.343] |  |  | 4 | 3 | f42e5c04 |
| loco | start_points | fixed:200 | rmse | patchtst | 5.047 [2.531, 8.955] |  |  | 4 | 3 | 8e3ccaba |
| loco | start_points | fixed:200 | rmse | transformer | 1.262 [0.373, 2.151] |  |  | 4 | 3 | bd101e5c |
| loco | start_points | fixed:400 | rmse | age_only | 0.390 [0.127, 0.727] |  |  | 4 | 3 | 21c6e382 |
| loco | start_points | fixed:400 | rmse | elasticnet | 1.587 [0.582, 3.196] |  |  | 4 | 3 | 3ae1400b |
| loco | start_points | fixed:400 | rmse | itransformer | 1.160 [0.673, 1.745] |  |  | 4 | 3 | c36c8628 |
| loco | start_points | fixed:400 | rmse | lgbm | 0.609 [0.406, 0.811] |  |  | 4 | 3 | a77ef1ab |
| loco | start_points | fixed:400 | rmse | lstm | 0.531 [0.261, 0.873] |  |  | 4 | 3 | f42e5c04 |
| loco | start_points | fixed:400 | rmse | patchtst | 2.764 [1.895, 4.153] |  |  | 4 | 3 | 8e3ccaba |
| loco | start_points | fixed:400 | rmse | transformer | 1.337 [0.663, 1.827] |  |  | 4 | 3 | bd101e5c |
| loco | start_points | frac:0.3 | rmse | age_only | 1.300 [0.351, 2.471] |  |  | 4 | 3 | 21c6e382 |
| loco | start_points | frac:0.3 | rmse | elasticnet | 3.100 [1.320, 4.627] |  |  | 4 | 3 | 3ae1400b |
| loco | start_points | frac:0.3 | rmse | itransformer | 2.720 [0.659, 6.026] |  |  | 4 | 3 | c36c8628 |
| loco | start_points | frac:0.3 | rmse | lgbm | 2.689 [0.694, 5.972] |  |  | 4 | 3 | a77ef1ab |
| loco | start_points | frac:0.3 | rmse | lstm | 0.947 [0.546, 1.425] |  |  | 4 | 3 | f42e5c04 |
| loco | start_points | frac:0.3 | rmse | patchtst | 4.626 [2.697, 6.748] |  |  | 4 | 3 | 8e3ccaba |
| loco | start_points | frac:0.3 | rmse | transformer | 2.966 [0.995, 6.765] |  |  | 4 | 3 | bd101e5c |
| loco | start_points | frac:0.5 | rmse | age_only | 1.037 [0.242, 2.422] |  |  | 4 | 3 | 21c6e382 |
| loco | start_points | frac:0.5 | rmse | elasticnet | 2.207 [0.876, 3.577] |  |  | 4 | 3 | 3ae1400b |
| loco | start_points | frac:0.5 | rmse | itransformer | 1.097 [0.585, 1.763] |  |  | 4 | 3 | c36c8628 |
| loco | start_points | frac:0.5 | rmse | lgbm | 0.573 [0.114, 1.114] |  |  | 4 | 3 | a77ef1ab |
| loco | start_points | frac:0.5 | rmse | lstm | 0.741 [0.223, 1.639] |  |  | 4 | 3 | f42e5c04 |
| loco | start_points | frac:0.5 | rmse | patchtst | 4.169 [1.851, 6.487] |  |  | 4 | 3 | 8e3ccaba |
| loco | start_points | frac:0.5 | rmse | transformer | 0.678 [0.271, 1.188] |  |  | 4 | 3 | bd101e5c |
| loco | start_points | frac:0.7 | rmse | age_only | 0.832 [0.212, 1.534] |  |  | 4 | 3 | 21c6e382 |
| loco | start_points | frac:0.7 | rmse | elasticnet | 1.569 [0.448, 3.027] |  |  | 4 | 3 | 3ae1400b |
| loco | start_points | frac:0.7 | rmse | itransformer | 1.900 [0.901, 3.049] |  |  | 4 | 3 | c36c8628 |
| loco | start_points | frac:0.7 | rmse | lgbm | 0.677 [0.388, 0.965] |  |  | 4 | 3 | a77ef1ab |
| loco | start_points | frac:0.7 | rmse | lstm | 0.478 [0.323, 0.597] |  |  | 4 | 3 | f42e5c04 |
| loco | start_points | frac:0.7 | rmse | patchtst | 2.933 [1.565, 4.301] |  |  | 4 | 3 | 8e3ccaba |
| loco | start_points | frac:0.7 | rmse | transformer | 1.530 [1.339, 1.720] |  |  | 4 | 3 | bd101e5c |
| loco | start_points | overall | rmse | age_only | 1.172 [0.494, 1.884] |  |  | 4 | 3 | 21c6e382 |
| loco | start_points | overall | rmse | elasticnet | 2.410 [1.258, 3.637] |  |  | 4 | 3 | 3ae1400b |
| loco | start_points | overall | rmse | itransformer | 2.387 [1.232, 4.051] |  |  | 4 | 3 | c36c8628 |
| loco | start_points | overall | rmse | lgbm | 1.473 [0.671, 2.785] |  |  | 4 | 3 | a77ef1ab |
| loco | start_points | overall | rmse | lstm | 0.891 [0.647, 1.217] |  |  | 4 | 3 | f42e5c04 |
| loco | start_points | overall | rmse | patchtst | 4.678 [3.454, 6.040] |  |  | 4 | 3 | 8e3ccaba |
| loco | start_points | overall | rmse | transformer | 2.028 [1.287, 3.408] |  |  | 4 | 3 | bd101e5c |

</details>

<details><summary>nasa_soh (49 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| loco | all | overall | rmse | age_only | 5.846 [3.492, 8.201] |  | 2.929 | 4 | 3 | 02186163 |
| loco | all | overall | rmse | elasticnet | 5.418 [2.669, 8.031] |  | 9.019 | 4 | 3 | 5bcb6177 |
| loco | all | overall | rmse | itransformer | 4.733 [3.412, 6.083] |  | 5.279 | 4 | 3 | c221bf8d |
| loco | all | overall | rmse | lgbm | 3.942 [2.615, 6.502] |  | 2.631 | 4 | 3 | 2a3bb4b2 |
| loco | all | overall | rmse | lstm | 4.408 [3.418, 5.994] |  | 3.281 | 4 | 3 | 5c694671 |
| loco | all | overall | rmse | patchtst | 5.955 [4.069, 7.981] |  | 6.502 | 4 | 3 | ac582d2d |
| loco | all | overall | rmse | transformer | 7.543 [5.555, 9.719] |  | 10.512 | 4 | 3 | 9cfee0d0 |
| loco | start_points | fixed:30 | rmse | age_only | 4.134 [3.969, 4.299] |  | 4.327 | 4 | 3 | 02186163 |
| loco | start_points | fixed:30 | rmse | elasticnet | 4.290 [2.014, 6.163] |  | 4.175 | 4 | 3 | 5bcb6177 |
| loco | start_points | fixed:30 | rmse | itransformer | 3.342 [1.630, 5.295] |  | 3.159 | 4 | 3 | c221bf8d |
| loco | start_points | fixed:30 | rmse | lgbm | 3.679 [2.715, 4.435] |  | 2.173 | 4 | 3 | 2a3bb4b2 |
| loco | start_points | fixed:30 | rmse | lstm | 3.731 [2.064, 4.844] |  | 1.310 | 4 | 3 | 5c694671 |
| loco | start_points | fixed:30 | rmse | patchtst | 4.943 [2.871, 6.386] |  | 1.968 | 4 | 3 | ac582d2d |
| loco | start_points | fixed:30 | rmse | transformer | 4.936 [3.924, 6.340] |  | 3.705 | 4 | 3 | 9cfee0d0 |
| loco | start_points | fixed:50 | rmse | age_only | 4.566 [3.204, 5.580] |  | 2.579 | 4 | 3 | 02186163 |
| loco | start_points | fixed:50 | rmse | elasticnet | 5.695 [2.527, 8.369] |  | 8.009 | 4 | 3 | 5bcb6177 |
| loco | start_points | fixed:50 | rmse | itransformer | 4.306 [1.615, 8.324] |  | 10.461 | 4 | 3 | c221bf8d |
| loco | start_points | fixed:50 | rmse | lgbm | 2.844 [1.153, 4.798] |  | 0.473 | 4 | 3 | 2a3bb4b2 |
| loco | start_points | fixed:50 | rmse | lstm | 4.098 [3.288, 5.139] |  | 3.127 | 4 | 3 | 5c694671 |
| loco | start_points | fixed:50 | rmse | patchtst | 5.659 [4.167, 8.214] |  | 9.423 | 4 | 3 | ac582d2d |
| loco | start_points | fixed:50 | rmse | transformer | 6.162 [5.503, 7.264] |  | 5.517 | 4 | 3 | 9cfee0d0 |
| loco | start_points | frac:0.3 | rmse | age_only | 5.236 [4.785, 5.687] |  | 4.570 | 4 | 3 | 02186163 |
| loco | start_points | frac:0.3 | rmse | elasticnet | 5.727 [3.229, 7.695] |  | 7.751 | 4 | 3 | 5bcb6177 |
| loco | start_points | frac:0.3 | rmse | itransformer | 3.211 [1.976, 4.887] |  | 2.121 | 4 | 3 | c221bf8d |
| loco | start_points | frac:0.3 | rmse | lgbm | 4.249 [3.416, 5.269] |  | 3.633 | 4 | 3 | 2a3bb4b2 |
| loco | start_points | frac:0.3 | rmse | lstm | 3.730 [1.669, 5.286] |  | 0.650 | 4 | 3 | 5c694671 |
| loco | start_points | frac:0.3 | rmse | patchtst | 2.834 [0.868, 5.322] |  | 0.359 | 4 | 3 | ac582d2d |
| loco | start_points | frac:0.3 | rmse | transformer | 6.236 [4.411, 8.045] |  | 3.389 | 4 | 3 | 9cfee0d0 |
| loco | start_points | frac:0.5 | rmse | age_only | 5.305 [4.473, 5.862] |  | 5.811 | 4 | 3 | 02186163 |
| loco | start_points | frac:0.5 | rmse | elasticnet | 5.837 [2.264, 8.695] |  | 7.077 | 4 | 3 | 5bcb6177 |
| loco | start_points | frac:0.5 | rmse | itransformer | 1.887 [1.369, 2.425] |  | 1.618 | 4 | 3 | c221bf8d |
| loco | start_points | frac:0.5 | rmse | lgbm | 2.123 [1.012, 3.225] |  | 0.423 | 4 | 3 | 2a3bb4b2 |
| loco | start_points | frac:0.5 | rmse | lstm | 3.514 [1.913, 4.854] |  | 0.996 | 4 | 3 | 5c694671 |
| loco | start_points | frac:0.5 | rmse | patchtst | 4.698 [3.300, 5.910] |  | 2.539 | 4 | 3 | ac582d2d |
| loco | start_points | frac:0.5 | rmse | transformer | 4.758 [3.756, 5.928] |  | 3.475 | 4 | 3 | 9cfee0d0 |
| loco | start_points | frac:0.7 | rmse | age_only | 5.452 [3.767, 6.609] |  | 2.946 | 4 | 3 | 02186163 |
| loco | start_points | frac:0.7 | rmse | elasticnet | 6.086 [3.358, 8.285] |  | 7.460 | 4 | 3 | 5bcb6177 |
| loco | start_points | frac:0.7 | rmse | itransformer | 3.492 [1.914, 5.792] |  | 6.976 | 4 | 3 | c221bf8d |
| loco | start_points | frac:0.7 | rmse | lgbm | 2.063 [0.855, 3.760] |  | 0.576 | 4 | 3 | 2a3bb4b2 |
| loco | start_points | frac:0.7 | rmse | lstm | 3.303 [2.477, 4.636] |  | 2.511 | 4 | 3 | 5c694671 |
| loco | start_points | frac:0.7 | rmse | patchtst | 4.460 [0.977, 9.600] |  | 12.318 | 4 | 3 | ac582d2d |
| loco | start_points | frac:0.7 | rmse | transformer | 4.275 [2.757, 6.072] |  | 6.944 | 4 | 3 | 9cfee0d0 |
| loco | start_points | overall | rmse | age_only | 5.033 [4.479, 5.367] |  | 4.212 | 4 | 3 | 02186163 |
| loco | start_points | overall | rmse | elasticnet | 5.621 [2.732, 7.712] |  | 7.034 | 4 | 3 | 5bcb6177 |
| loco | start_points | overall | rmse | itransformer | 4.005 [2.819, 5.313] |  | 6.063 | 4 | 3 | c221bf8d |
| loco | start_points | overall | rmse | lgbm | 3.259 [2.382, 4.136] |  | 1.932 | 4 | 3 | 2a3bb4b2 |
| loco | start_points | overall | rmse | lstm | 3.898 [2.790, 4.848] |  | 2.109 | 4 | 3 | 5c694671 |
| loco | start_points | overall | rmse | patchtst | 5.439 [4.528, 6.602] |  | 7.221 | 4 | 3 | ac582d2d |
| loco | start_points | overall | rmse | transformer | 5.714 [4.986, 6.730] |  | 5.049 | 4 | 3 | 9cfee0d0 |

</details>

<details><summary>toyota_soh (84 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rmse | age_only | 4.008 [3.665, 4.471] |  |  | 43 | 3 | c47576b8 |
| test1 | all | overall | rmse | elasticnet | 1.177 [0.939, 1.479] |  |  | 43 | 3 | 9804e441 |
| test1 | all | overall | rmse | itransformer | 1.186 [0.959, 1.462] |  |  | 43 | 3 | 0ae36223 |
| test1 | all | overall | rmse | lgbm | 0.923 [0.711, 1.216] |  |  | 43 | 3 | d75ab198 |
| test1 | all | overall | rmse | lstm | 1.061 [0.839, 1.333] |  |  | 43 | 3 | 93a466eb |
| test1 | all | overall | rmse | patchtst | 1.851 [1.630, 2.115] |  |  | 43 | 3 | 9ab9f000 |
| test1 | all | overall | rmse | transformer | 0.914 [0.636, 1.260] |  |  | 43 | 3 | 9daafdbf |
| test1 | start_points | fixed:100 | rmse | age_only | 0.567 [0.284, 1.052] |  |  | 43 | 3 | c47576b8 |
| test1 | start_points | fixed:100 | rmse | elasticnet | 0.645 [0.462, 0.869] |  |  | 43 | 3 | 9804e441 |
| test1 | start_points | fixed:100 | rmse | itransformer | 0.478 [0.312, 0.732] |  |  | 43 | 3 | 0ae36223 |
| test1 | start_points | fixed:100 | rmse | lgbm | 0.345 [0.181, 0.607] |  |  | 43 | 3 | d75ab198 |
| test1 | start_points | fixed:100 | rmse | lstm | 0.489 [0.338, 0.708] |  |  | 43 | 3 | 93a466eb |
| test1 | start_points | fixed:100 | rmse | patchtst | 1.007 [0.854, 1.173] |  |  | 43 | 3 | 9ab9f000 |
| test1 | start_points | fixed:100 | rmse | transformer | 0.305 [0.153, 0.575] |  |  | 43 | 3 | 9daafdbf |
| test1 | start_points | frac:0.3 | rmse | age_only | 1.299 [0.894, 1.783] |  |  | 43 | 3 | c47576b8 |
| test1 | start_points | frac:0.3 | rmse | elasticnet | 0.524 [0.411, 0.649] |  |  | 43 | 3 | 9804e441 |
| test1 | start_points | frac:0.3 | rmse | itransformer | 0.632 [0.462, 0.835] |  |  | 43 | 3 | 0ae36223 |
| test1 | start_points | frac:0.3 | rmse | lgbm | 0.244 [0.165, 0.340] |  |  | 43 | 3 | d75ab198 |
| test1 | start_points | frac:0.3 | rmse | lstm | 0.442 [0.353, 0.533] |  |  | 43 | 3 | 93a466eb |
| test1 | start_points | frac:0.3 | rmse | patchtst | 0.671 [0.543, 0.818] |  |  | 43 | 3 | 9ab9f000 |
| test1 | start_points | frac:0.3 | rmse | transformer | 0.281 [0.213, 0.359] |  |  | 43 | 3 | 9daafdbf |
| test1 | start_points | frac:0.5 | rmse | age_only | 2.498 [1.876, 3.154] |  |  | 43 | 3 | c47576b8 |
| test1 | start_points | frac:0.5 | rmse | elasticnet | 0.807 [0.532, 1.167] |  |  | 43 | 3 | 9804e441 |
| test1 | start_points | frac:0.5 | rmse | itransformer | 0.877 [0.606, 1.196] |  |  | 43 | 3 | 0ae36223 |
| test1 | start_points | frac:0.5 | rmse | lgbm | 0.519 [0.338, 0.743] |  |  | 43 | 3 | d75ab198 |
| test1 | start_points | frac:0.5 | rmse | lstm | 0.922 [0.585, 1.362] |  |  | 43 | 3 | 93a466eb |
| test1 | start_points | frac:0.5 | rmse | patchtst | 0.953 [0.711, 1.222] |  |  | 43 | 3 | 9ab9f000 |
| test1 | start_points | frac:0.5 | rmse | transformer | 0.821 [0.513, 1.218] |  |  | 43 | 3 | 9daafdbf |
| test1 | start_points | frac:0.7 | rmse | age_only | 2.778 [2.187, 3.412] |  |  | 43 | 3 | c47576b8 |
| test1 | start_points | frac:0.7 | rmse | elasticnet | 1.092 [0.658, 1.656] |  |  | 43 | 3 | 9804e441 |
| test1 | start_points | frac:0.7 | rmse | itransformer | 1.162 [0.870, 1.501] |  |  | 43 | 3 | 0ae36223 |
| test1 | start_points | frac:0.7 | rmse | lgbm | 0.718 [0.487, 1.019] |  |  | 43 | 3 | d75ab198 |
| test1 | start_points | frac:0.7 | rmse | lstm | 0.942 [0.595, 1.371] |  |  | 43 | 3 | 93a466eb |
| test1 | start_points | frac:0.7 | rmse | patchtst | 1.609 [1.286, 1.949] |  |  | 43 | 3 | 9ab9f000 |
| test1 | start_points | frac:0.7 | rmse | transformer | 1.018 [0.606, 1.541] |  |  | 43 | 3 | 9daafdbf |
| test1 | start_points | overall | rmse | age_only | 2.168 [1.705, 2.664] |  |  | 43 | 3 | c47576b8 |
| test1 | start_points | overall | rmse | elasticnet | 0.911 [0.660, 1.237] |  |  | 43 | 3 | 9804e441 |
| test1 | start_points | overall | rmse | itransformer | 0.940 [0.732, 1.196] |  |  | 43 | 3 | 0ae36223 |
| test1 | start_points | overall | rmse | lgbm | 0.541 [0.372, 0.763] |  |  | 43 | 3 | d75ab198 |
| test1 | start_points | overall | rmse | lstm | 0.839 [0.600, 1.140] |  |  | 43 | 3 | 93a466eb |
| test1 | start_points | overall | rmse | patchtst | 1.244 [1.072, 1.432] |  |  | 43 | 3 | 9ab9f000 |
| test1 | start_points | overall | rmse | transformer | 0.737 [0.465, 1.082] |  |  | 43 | 3 | 9daafdbf |
| test2 | all | overall | rmse | age_only | 3.673 [3.520, 3.821] |  |  | 40 | 3 | c47576b8 |
| test2 | all | overall | rmse | elasticnet | 11.902 [9.743, 14.328] |  |  | 40 | 3 | 9804e441 |
| test2 | all | overall | rmse | itransformer | 2.267 [2.097, 2.470] |  |  | 40 | 3 | 0ae36223 |
| test2 | all | overall | rmse | lgbm | 2.584 [2.459, 2.716] |  |  | 40 | 3 | d75ab198 |
| test2 | all | overall | rmse | lstm | 2.260 [2.090, 2.460] |  |  | 40 | 3 | 93a466eb |
| test2 | all | overall | rmse | patchtst | 3.235 [3.083, 3.414] |  |  | 40 | 3 | 9ab9f000 |
| test2 | all | overall | rmse | transformer | 2.027 [1.943, 2.115] |  |  | 40 | 3 | 9daafdbf |
| test2 | start_points | fixed:100 | rmse | age_only | 0.252 [0.146, 0.387] |  |  | 40 | 3 | c47576b8 |
| test2 | start_points | fixed:100 | rmse | elasticnet | 1.226 [1.063, 1.391] |  |  | 40 | 3 | 9804e441 |
| test2 | start_points | fixed:100 | rmse | itransformer | 0.348 [0.236, 0.495] |  |  | 40 | 3 | 0ae36223 |
| test2 | start_points | fixed:100 | rmse | lgbm | 0.472 [0.397, 0.550] |  |  | 40 | 3 | d75ab198 |
| test2 | start_points | fixed:100 | rmse | lstm | 0.295 [0.228, 0.367] |  |  | 40 | 3 | 93a466eb |
| test2 | start_points | fixed:100 | rmse | patchtst | 0.943 [0.810, 1.093] |  |  | 40 | 3 | 9ab9f000 |
| test2 | start_points | fixed:100 | rmse | transformer | 0.482 [0.404, 0.562] |  |  | 40 | 3 | 9daafdbf |
| test2 | start_points | frac:0.3 | rmse | age_only | 2.216 [1.814, 2.689] |  |  | 40 | 3 | c47576b8 |
| test2 | start_points | frac:0.3 | rmse | elasticnet | 1.520 [1.338, 1.698] |  |  | 40 | 3 | 9804e441 |
| test2 | start_points | frac:0.3 | rmse | itransformer | 0.575 [0.370, 0.831] |  |  | 40 | 3 | 0ae36223 |
| test2 | start_points | frac:0.3 | rmse | lgbm | 0.427 [0.344, 0.510] |  |  | 40 | 3 | d75ab198 |
| test2 | start_points | frac:0.3 | rmse | lstm | 0.722 [0.590, 0.858] |  |  | 40 | 3 | 93a466eb |
| test2 | start_points | frac:0.3 | rmse | patchtst | 0.674 [0.509, 0.876] |  |  | 40 | 3 | 9ab9f000 |
| test2 | start_points | frac:0.3 | rmse | transformer | 0.870 [0.737, 1.000] |  |  | 40 | 3 | 9daafdbf |
| test2 | start_points | frac:0.5 | rmse | age_only | 4.875 [4.499, 5.210] |  |  | 40 | 3 | c47576b8 |
| test2 | start_points | frac:0.5 | rmse | elasticnet | 1.700 [1.484, 1.906] |  |  | 40 | 3 | 9804e441 |
| test2 | start_points | frac:0.5 | rmse | itransformer | 0.925 [0.578, 1.351] |  |  | 40 | 3 | 0ae36223 |
| test2 | start_points | frac:0.5 | rmse | lgbm | 1.278 [0.991, 1.575] |  |  | 40 | 3 | d75ab198 |
| test2 | start_points | frac:0.5 | rmse | lstm | 1.494 [1.334, 1.655] |  |  | 40 | 3 | 93a466eb |
| test2 | start_points | frac:0.5 | rmse | patchtst | 0.992 [0.699, 1.362] |  |  | 40 | 3 | 9ab9f000 |
| test2 | start_points | frac:0.5 | rmse | transformer | 1.442 [1.269, 1.610] |  |  | 40 | 3 | 9daafdbf |
| test2 | start_points | frac:0.7 | rmse | age_only | 4.258 [3.958, 4.524] |  |  | 40 | 3 | c47576b8 |
| test2 | start_points | frac:0.7 | rmse | elasticnet | 1.725 [1.466, 2.002] |  |  | 40 | 3 | 9804e441 |
| test2 | start_points | frac:0.7 | rmse | itransformer | 2.059 [1.489, 2.693] |  |  | 40 | 3 | 0ae36223 |
| test2 | start_points | frac:0.7 | rmse | lgbm | 2.142 [1.822, 2.444] |  |  | 40 | 3 | d75ab198 |
| test2 | start_points | frac:0.7 | rmse | lstm | 1.746 [1.538, 1.967] |  |  | 40 | 3 | 93a466eb |
| test2 | start_points | frac:0.7 | rmse | patchtst | 1.728 [1.223, 2.341] |  |  | 40 | 3 | 9ab9f000 |
| test2 | start_points | frac:0.7 | rmse | transformer | 1.988 [1.773, 2.199] |  |  | 40 | 3 | 9daafdbf |
| test2 | start_points | overall | rmse | age_only | 3.509 [3.286, 3.718] |  |  | 40 | 3 | c47576b8 |
| test2 | start_points | overall | rmse | elasticnet | 1.600 [1.426, 1.772] |  |  | 40 | 3 | 9804e441 |
| test2 | start_points | overall | rmse | itransformer | 1.292 [0.961, 1.665] |  |  | 40 | 3 | 0ae36223 |
| test2 | start_points | overall | rmse | lgbm | 1.338 [1.149, 1.519] |  |  | 40 | 3 | d75ab198 |
| test2 | start_points | overall | rmse | lstm | 1.241 [1.110, 1.373] |  |  | 40 | 3 | 93a466eb |
| test2 | start_points | overall | rmse | patchtst | 1.288 [1.017, 1.624] |  |  | 40 | 3 | 9ab9f000 |
| test2 | start_points | overall | rmse | transformer | 1.349 [1.204, 1.486] |  |  | 40 | 3 | 9daafdbf |

</details>
