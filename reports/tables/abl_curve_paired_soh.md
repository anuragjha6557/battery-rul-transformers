| candidate | reference | dataset | split | metric | cand_mean | ref_mean | delta [95% CI] | k_cells | k_pairs | wilcoxon_p |
|---|---|---|---|---|---|---|---|---|---|---|
| abl_curve:lgbm | benchmark:lgbm | calce | loco | rmse | 1.21 | 1.19 | +0.019 [+0.007, +0.031] | 0/4 | 0/20 | nan |
| abl_curve:lgbm | benchmark:lgbm | nasa | loco | rmse | 0.926 | 0.928 | -0.002 [-0.005, +0.001] | 3/4 | 15/20 | nan |
| abl_curve:lgbm | benchmark:lgbm | toyota | test1 | rmse | 0.133 | 0.133 | +0.000 [-0.000, +0.000] | 12/43 | 60/215 | 0.0074 |
| abl_curve:lgbm | benchmark:lgbm | toyota | test2 | rmse | 0.0204 | 0.0236 | -0.003 [-0.004, -0.003] | 40/40 | 200/200 | 1.82e-12 |
| abl_curve:itransformer | benchmark:itransformer | calce | loco | rmse | 1.25 | 1.26 | -0.003 [-0.013, +0.007] | 3/4 | 11/20 | nan |
| abl_curve:itransformer | benchmark:itransformer | nasa | loco | rmse | 0.749 | 0.703 | +0.046 [+0.020, +0.077] | 0/4 | 4/20 | nan |
| abl_curve:itransformer | benchmark:itransformer | toyota | test1 | rmse | 0.111 | 0.111 | +0.000 [-0.000, +0.000] | 23/43 | 122/215 | 0.715 |
| abl_curve:itransformer | benchmark:itransformer | toyota | test2 | rmse | 0.0251 | 0.0234 | +0.002 [+0.001, +0.002] | 1/40 | 81/200 | 5.46e-12 |
