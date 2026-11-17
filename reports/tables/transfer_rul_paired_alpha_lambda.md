| candidate | reference | dataset | split | metric | cand_mean | ref_mean | delta [95% CI] | k_cells | k_pairs | wilcoxon_p |
|---|---|---|---|---|---|---|---|---|---|---|
| transfer:itransformer+ft_full | transfer:itransformer+scratch | calce | loco | alpha_lambda_acc | 0.75 | 0.55 | +0.200 [+0.000, +0.600] | 1/4 | 4/20 | nan |
| transfer:itransformer+ft_full | transfer:itransformer+scratch | nasa | loco | alpha_lambda_acc | 0.25 | 0.1 | +0.150 [+0.000, +0.450] | 1/4 | 3/20 | nan |
| transfer:itransformer+zero_shot | transfer:itransformer+scratch | calce | loco | alpha_lambda_acc | 0 | 0.55 | -0.550 [-1.000, -0.100] | 0/4 | 0/20 | nan |
| transfer:itransformer+zero_shot | transfer:itransformer+scratch | nasa | loco | alpha_lambda_acc | 0 | 0.1 | -0.100 [-0.300, +0.000] | 0/4 | 0/20 | nan |
