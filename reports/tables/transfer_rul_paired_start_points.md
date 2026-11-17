| candidate | reference | dataset | split | metric | cand_mean | ref_mean | delta [95% CI] | k_cells | k_pairs | wilcoxon_p |
|---|---|---|---|---|---|---|---|---|---|---|
| transfer:itransformer+ft_full | transfer:itransformer+scratch | calce | loco | rul_mae | 85.7 | 72.7 | +13.018 [-4.721, +30.758] | 2/4 | 5/20 | nan |
| transfer:itransformer+ft_full | transfer:itransformer+scratch | nasa | loco | rul_mae | 18.8 | 15.8 | +2.950 [-6.346, +12.246] | 2/4 | 10/20 | nan |
| transfer:itransformer+zero_shot | transfer:itransformer+scratch | calce | loco | rul_mae | 349 | 72.7 | +276.685 [+140.534, +355.575] | 0/4 | 0/20 | nan |
| transfer:itransformer+zero_shot | transfer:itransformer+scratch | nasa | loco | rul_mae | 47.3 | 15.8 | +31.498 [+3.942, +59.752] | 1/4 | 5/20 | nan |
