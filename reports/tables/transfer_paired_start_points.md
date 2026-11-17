| candidate | reference | dataset | split | metric | cand_mean | ref_mean | delta [95% CI] | k_cells | k_pairs | wilcoxon_p |
|---|---|---|---|---|---|---|---|---|---|---|
| transfer:itransformer+ft_full | transfer:itransformer+scratch | calce | loco | rmse_h50 | 1.63 | 1.49 | +0.141 [-0.101, +0.346] | 1/4 | 5/20 | nan |
| transfer:itransformer+ft_full | transfer:itransformer+scratch | nasa | loco | rmse_h50 | 4.15 | 5.73 | -1.574 [-3.125, -0.023] | 3/4 | 15/20 | nan |
| transfer:itransformer+zero_shot | transfer:itransformer+scratch | calce | loco | rmse_h50 | 1.88 | 1.49 | +0.391 [-0.068, +0.756] | 1/4 | 5/20 | nan |
| transfer:itransformer+zero_shot | transfer:itransformer+scratch | nasa | loco | rmse_h50 | 8.1 | 5.73 | +2.374 [+0.332, +4.577] | 1/4 | 5/20 | nan |
| transfer:itransformer+ft_head | transfer:itransformer+scratch | calce | loco | rmse_h50 | 1.89 | 1.49 | +0.400 [+0.157, +0.646] | 0/4 | 2/20 | nan |
| transfer:itransformer+ft_head | transfer:itransformer+scratch | nasa | loco | rmse_h50 | 7.66 | 5.73 | +1.929 [+0.180, +3.372] | 1/4 | 5/20 | nan |
| transfer:itransformer+few_shot | transfer:itransformer+ft_full | calce | loco | rmse_h50 | 1.6 | 1.63 | -0.027 [-0.138, +0.047] | 1/4 | 8/20 | nan |
| transfer:itransformer+few_shot | transfer:itransformer+ft_full | nasa | loco | rmse_h50 | 4.05 | 4.15 | -0.102 [-0.114, -0.094] | 4/4 | 19/20 | nan |
| transfer:itransformer+ft_full | transfer:itransformer+scratch | calce | loco | rmse_h10 | 1.1 | 1.04 | +0.059 [+0.011, +0.111] | 1/4 | 6/20 | nan |
| transfer:itransformer+ft_full | transfer:itransformer+scratch | nasa | loco | rmse_h10 | 2.14 | 1.79 | +0.357 [-0.024, +0.764] | 1/4 | 5/20 | nan |
| transfer:itransformer+zero_shot | transfer:itransformer+scratch | calce | loco | rmse_h10 | 1.19 | 1.04 | +0.152 [-0.014, +0.284] | 1/4 | 5/20 | nan |
| transfer:itransformer+zero_shot | transfer:itransformer+scratch | nasa | loco | rmse_h10 | 2.95 | 1.79 | +1.161 [+0.763, +1.545] | 0/4 | 0/20 | nan |
| transfer:itransformer+ft_head | transfer:itransformer+scratch | calce | loco | rmse_h10 | 1.12 | 1.04 | +0.079 [-0.012, +0.154] | 1/4 | 5/20 | nan |
| transfer:itransformer+ft_head | transfer:itransformer+scratch | nasa | loco | rmse_h10 | 2.07 | 1.79 | +0.284 [-0.051, +0.587] | 1/4 | 5/20 | nan |
| transfer:itransformer+few_shot | transfer:itransformer+ft_full | calce | loco | rmse_h10 | 1.09 | 1.1 | -0.012 [-0.022, +0.002] | 3/4 | 15/20 | nan |
| transfer:itransformer+few_shot | transfer:itransformer+ft_full | nasa | loco | rmse_h10 | 2.11 | 2.14 | -0.037 [-0.070, -0.006] | 3/4 | 16/20 | nan |
