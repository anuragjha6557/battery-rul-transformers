| candidate | reference | dataset | split | metric | cand_mean | ref_mean | delta [95% CI] | k_cells | k_pairs | wilcoxon_p |
|---|---|---|---|---|---|---|---|---|---|---|
| abl_curve:lgbm | benchmark:lgbm | calce | loco | rmse_h50 | 2.86 | 2.84 | +0.019 [+0.001, +0.036] | 1/4 | 5/20 | nan |
| abl_curve:lgbm | benchmark:lgbm | nasa | loco | rmse_h50 | 3.33 | 3.24 | +0.094 [-0.080, +0.287] | 2/4 | 10/20 | nan |
| abl_curve:lgbm | benchmark:lgbm | toyota | test1 | rmse_h50 | 0.419 | 0.451 | -0.033 [-0.046, -0.019] | 34/43 | 170/215 | 1e-05 |
| abl_curve:lgbm | benchmark:lgbm | toyota | test2 | rmse_h50 | 0.281 | 0.302 | -0.021 [-0.031, -0.012] | 30/40 | 150/200 | 9.45e-05 |
| abl_curve:itransformer | benchmark:itransformer | calce | loco | rmse_h50 | 3.08 | 3.13 | -0.053 [-0.133, +0.011] | 2/4 | 15/20 | nan |
| abl_curve:itransformer | benchmark:itransformer | nasa | loco | rmse_h50 | 5.41 | 5.38 | +0.033 [-0.039, +0.075] | 1/4 | 10/20 | nan |
| abl_curve:itransformer | benchmark:itransformer | toyota | test1 | rmse_h50 | 0.389 | 0.402 | -0.013 [-0.020, -0.006] | 29/43 | 141/215 | 0.00162 |
| abl_curve:itransformer | benchmark:itransformer | toyota | test2 | rmse_h50 | 0.226 | 0.2 | +0.026 [+0.018, +0.035] | 4/40 | 38/200 | 3.48e-08 |
