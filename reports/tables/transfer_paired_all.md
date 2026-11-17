| candidate | reference | dataset | split | metric | cand_mean | ref_mean | delta [95% CI] | k_cells | k_pairs | wilcoxon_p |
|---|---|---|---|---|---|---|---|---|---|---|
| transfer:itransformer+ft_full | transfer:itransformer+scratch | calce | loco | rmse_h50 | 3.47 | 3.18 | +0.285 [+0.088, +0.465] | 1/4 | 4/20 | nan |
| transfer:itransformer+ft_full | transfer:itransformer+scratch | nasa | loco | rmse_h50 | 3.88 | 5.41 | -1.532 [-1.630, -1.412] | 4/4 | 20/20 | nan |
| transfer:itransformer+zero_shot | transfer:itransformer+scratch | calce | loco | rmse_h50 | 5.14 | 3.18 | +1.963 [+1.686, +2.239] | 0/4 | 0/20 | nan |
| transfer:itransformer+zero_shot | transfer:itransformer+scratch | nasa | loco | rmse_h50 | 8.99 | 5.41 | +3.575 [+2.082, +5.068] | 0/4 | 0/20 | nan |
| transfer:itransformer+ft_head | transfer:itransformer+scratch | calce | loco | rmse_h50 | 4.27 | 3.18 | +1.090 [+0.977, +1.223] | 0/4 | 0/20 | nan |
| transfer:itransformer+ft_head | transfer:itransformer+scratch | nasa | loco | rmse_h50 | 7.16 | 5.41 | +1.745 [+0.593, +2.897] | 0/4 | 0/20 | nan |
| transfer:itransformer+ft_full | transfer:itransformer+scratch | calce | loco | rmse_h10 | 2.37 | 2.31 | +0.062 [+0.037, +0.080] | 0/4 | 0/20 | nan |
| transfer:itransformer+ft_full | transfer:itransformer+scratch | nasa | loco | rmse_h10 | 1.82 | 1.72 | +0.107 [+0.062, +0.152] | 0/4 | 0/20 | nan |
| transfer:itransformer+zero_shot | transfer:itransformer+scratch | calce | loco | rmse_h10 | 2.64 | 2.31 | +0.324 [+0.261, +0.386] | 0/4 | 0/20 | nan |
| transfer:itransformer+zero_shot | transfer:itransformer+scratch | nasa | loco | rmse_h10 | 2.53 | 1.72 | +0.812 [+0.545, +1.185] | 0/4 | 0/20 | nan |
| transfer:itransformer+ft_head | transfer:itransformer+scratch | calce | loco | rmse_h10 | 2.47 | 2.31 | +0.156 [+0.113, +0.198] | 0/4 | 0/20 | nan |
| transfer:itransformer+ft_head | transfer:itransformer+scratch | nasa | loco | rmse_h10 | 1.81 | 1.72 | +0.098 [+0.043, +0.158] | 0/4 | 0/20 | nan |
