| candidate | reference | dataset | split | metric | cand_mean | ref_mean | delta [95% CI] | k_cells | k_pairs | wilcoxon_p |
|---|---|---|---|---|---|---|---|---|---|---|
| transfer:itransformer+ft_full | transfer:itransformer+scratch | calce | loco | rul_mae | 95.8 | 67.4 | +28.382 [+6.117, +56.098] | 1/4 | 3/20 | nan |
| transfer:itransformer+ft_full | transfer:itransformer+scratch | nasa | loco | rul_mae | 16.9 | 16.8 | +0.058 [-6.977, +7.093] | 2/4 | 10/20 | nan |
| transfer:itransformer+zero_shot | transfer:itransformer+scratch | calce | loco | rul_mae | 250 | 67.4 | +182.836 [+117.246, +226.732] | 0/4 | 0/20 | nan |
| transfer:itransformer+zero_shot | transfer:itransformer+scratch | nasa | loco | rul_mae | 40 | 16.8 | +23.228 [+9.286, +37.032] | 0/4 | 0/20 | nan |
