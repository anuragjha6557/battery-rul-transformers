# Benchmark tables: field_probe_v2

- Protocol version: 1.1
- Git SHA: 42ed5a55a7
- Seeds: 1  |  unit runs: 3
- Note: n = 4 cells per NASA/CALCE dataset, so the 95 % cluster-bootstrap CI is wide by construction. Toyota rows are over test cells (test1 / test2 separately) with a cell-level bootstrap CI and a Holm-adjusted Wilcoxon p vs the best baseline. All metrics are computed per cell from the logged predictions.

## Headline (kind = overall; RMSE in %SOH, RUL MAE in cycles)

### toyota_soh

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rmse | age_only | 4.008 [3.665, 4.471] |  |  | 43 | 1 | 0c9c52db |
| test1 | all | overall | rmse | elasticnet | 1.147 [0.921, 1.427] |  |  | 43 | 1 | 22fc675d |
| test1 | all | overall | rmse | lgbm | 0.968 [0.754, 1.258] |  |  | 43 | 1 | 4b49625d |
| test1 | start_points | overall | rmse | age_only | 2.168 [1.705, 2.664] |  |  | 43 | 1 | 0c9c52db |
| test1 | start_points | overall | rmse | elasticnet | 0.934 [0.659, 1.282] |  |  | 43 | 1 | 22fc675d |
| test1 | start_points | overall | rmse | lgbm | 0.549 [0.388, 0.764] |  |  | 43 | 1 | 4b49625d |
| test2 | all | overall | rmse | age_only | 3.673 [3.520, 3.821] |  |  | 40 | 1 | 0c9c52db |
| test2 | all | overall | rmse | elasticnet | 5.703 [5.298, 6.117] |  |  | 40 | 1 | 22fc675d |
| test2 | all | overall | rmse | lgbm | 2.451 [2.325, 2.586] |  |  | 40 | 1 | 4b49625d |
| test2 | start_points | overall | rmse | age_only | 3.509 [3.286, 3.718] |  |  | 40 | 1 | 0c9c52db |
| test2 | start_points | overall | rmse | elasticnet | 1.486 [1.309, 1.664] |  |  | 40 | 1 | 22fc675d |
| test2 | start_points | overall | rmse | lgbm | 1.338 [1.161, 1.508] |  |  | 40 | 1 | 4b49625d |

## Mean rank (dataset x task x split x policy x headline metric)

| model | mean rank | conditions | missing |
|---|---|---|---|
| lgbm | 1.00 | 4 | 0 |
| elasticnet | 2.25 | 4 | 0 |
| age_only | 2.75 | 4 | 0 |

## Full tables

<details><summary>toyota_soh (36 rows)</summary>

| split | policy | kind | metric | model | mean [95% CI] | vs best baseline | indep. (B0018) | n_cells | n_seeds | run_group |
|---|---|---|---|---|---|---|---|---|---|---|
| test1 | all | overall | rmse | age_only | 4.008 [3.665, 4.471] |  |  | 43 | 1 | 0c9c52db |
| test1 | all | overall | rmse | elasticnet | 1.147 [0.921, 1.427] |  |  | 43 | 1 | 22fc675d |
| test1 | all | overall | rmse | lgbm | 0.968 [0.754, 1.258] |  |  | 43 | 1 | 4b49625d |
| test1 | start_points | fixed:100 | rmse | age_only | 0.567 [0.284, 1.052] |  |  | 43 | 1 | 0c9c52db |
| test1 | start_points | fixed:100 | rmse | elasticnet | 0.499 [0.318, 0.731] |  |  | 43 | 1 | 22fc675d |
| test1 | start_points | fixed:100 | rmse | lgbm | 0.347 [0.192, 0.594] |  |  | 43 | 1 | 4b49625d |
| test1 | start_points | frac:0.3 | rmse | age_only | 1.299 [0.894, 1.783] |  |  | 43 | 1 | 0c9c52db |
| test1 | start_points | frac:0.3 | rmse | elasticnet | 0.536 [0.422, 0.658] |  |  | 43 | 1 | 22fc675d |
| test1 | start_points | frac:0.3 | rmse | lgbm | 0.268 [0.183, 0.369] |  |  | 43 | 1 | 4b49625d |
| test1 | start_points | frac:0.5 | rmse | age_only | 2.498 [1.876, 3.154] |  |  | 43 | 1 | 0c9c52db |
| test1 | start_points | frac:0.5 | rmse | elasticnet | 1.030 [0.646, 1.539] |  |  | 43 | 1 | 22fc675d |
| test1 | start_points | frac:0.5 | rmse | lgbm | 0.515 [0.353, 0.709] |  |  | 43 | 1 | 4b49625d |
| test1 | start_points | frac:0.7 | rmse | age_only | 2.778 [2.187, 3.412] |  |  | 43 | 1 | 0c9c52db |
| test1 | start_points | frac:0.7 | rmse | elasticnet | 1.051 [0.659, 1.545] |  |  | 43 | 1 | 22fc675d |
| test1 | start_points | frac:0.7 | rmse | lgbm | 0.722 [0.485, 1.033] |  |  | 43 | 1 | 4b49625d |
| test1 | start_points | overall | rmse | age_only | 2.168 [1.705, 2.664] |  |  | 43 | 1 | 0c9c52db |
| test1 | start_points | overall | rmse | elasticnet | 0.934 [0.659, 1.282] |  |  | 43 | 1 | 22fc675d |
| test1 | start_points | overall | rmse | lgbm | 0.549 [0.388, 0.764] |  |  | 43 | 1 | 4b49625d |
| test2 | all | overall | rmse | age_only | 3.673 [3.520, 3.821] |  |  | 40 | 1 | 0c9c52db |
| test2 | all | overall | rmse | elasticnet | 5.703 [5.298, 6.117] |  |  | 40 | 1 | 22fc675d |
| test2 | all | overall | rmse | lgbm | 2.451 [2.325, 2.586] |  |  | 40 | 1 | 4b49625d |
| test2 | start_points | fixed:100 | rmse | age_only | 0.252 [0.146, 0.387] |  |  | 40 | 1 | 0c9c52db |
| test2 | start_points | fixed:100 | rmse | elasticnet | 0.749 [0.599, 0.908] |  |  | 40 | 1 | 22fc675d |
| test2 | start_points | fixed:100 | rmse | lgbm | 0.621 [0.525, 0.724] |  |  | 40 | 1 | 4b49625d |
| test2 | start_points | frac:0.3 | rmse | age_only | 2.216 [1.814, 2.689] |  |  | 40 | 1 | 0c9c52db |
| test2 | start_points | frac:0.3 | rmse | elasticnet | 1.376 [1.180, 1.563] |  |  | 40 | 1 | 22fc675d |
| test2 | start_points | frac:0.3 | rmse | lgbm | 0.407 [0.322, 0.495] |  |  | 40 | 1 | 4b49625d |
| test2 | start_points | frac:0.5 | rmse | age_only | 4.875 [4.499, 5.210] |  |  | 40 | 1 | 0c9c52db |
| test2 | start_points | frac:0.5 | rmse | elasticnet | 1.719 [1.508, 1.923] |  |  | 40 | 1 | 22fc675d |
| test2 | start_points | frac:0.5 | rmse | lgbm | 1.241 [0.971, 1.518] |  |  | 40 | 1 | 4b49625d |
| test2 | start_points | frac:0.7 | rmse | age_only | 4.258 [3.958, 4.524] |  |  | 40 | 1 | 0c9c52db |
| test2 | start_points | frac:0.7 | rmse | elasticnet | 1.715 [1.452, 1.996] |  |  | 40 | 1 | 22fc675d |
| test2 | start_points | frac:0.7 | rmse | lgbm | 2.097 [1.780, 2.401] |  |  | 40 | 1 | 4b49625d |
| test2 | start_points | overall | rmse | age_only | 3.509 [3.286, 3.718] |  |  | 40 | 1 | 0c9c52db |
| test2 | start_points | overall | rmse | elasticnet | 1.486 [1.309, 1.664] |  |  | 40 | 1 | 22fc675d |
| test2 | start_points | overall | rmse | lgbm | 1.338 [1.161, 1.508] |  |  | 40 | 1 | 4b49625d |

</details>
