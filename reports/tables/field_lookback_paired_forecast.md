| candidate | reference | dataset | split | metric | cand_mean | ref_mean | delta [95% CI] | k_cells | k_pairs | wilcoxon_p |
|---|---|---|---|---|---|---|---|---|---|---|
| field_lookback:itransformer[lookback=128] | field_lookback:itransformer[lookback=32] | calce | loco | rmse_h50 | 4.62 | 3.99 | +0.635 [+0.158, +1.216] | 0/4 | 2/12 | nan |
| field_lookback:itransformer[lookback=128] | field_lookback:itransformer[lookback=32] | toyota | test1 | rmse_h50 | 1.28 | 1.25 | +0.028 [-0.048, +0.135] | 23/43 | 70/129 | 0.392 |
| field_lookback:itransformer[lookback=128] | field_lookback:itransformer[lookback=32] | toyota | test2 | rmse_h50 | 1.45 | 1.89 | -0.433 [-0.565, -0.290] | 35/40 | 101/120 | 2.04e-06 |
| field_lookback:lstm[lookback=128] | field_lookback:lstm[lookback=32] | calce | loco | rmse_h50 | 2.77 | 2.84 | -0.070 [-0.107, -0.033] | 4/4 | 7/12 | nan |
| field_lookback:lstm[lookback=128] | field_lookback:lstm[lookback=32] | toyota | test1 | rmse_h50 | 0.976 | 0.977 | -0.001 [-0.011, +0.008] | 19/43 | 71/129 | 0.237 |
| field_lookback:lstm[lookback=128] | field_lookback:lstm[lookback=32] | toyota | test2 | rmse_h50 | 2.28 | 2.27 | +0.010 [+0.000, +0.019] | 15/40 | 42/120 | 0.0682 |
| field_lookback:transformer[lookback=128] | field_lookback:transformer[lookback=32] | calce | loco | rmse_h50 | 2.98 | 3.36 | -0.384 [-0.884, +0.077] | 2/4 | 9/12 | nan |
| field_lookback:transformer[lookback=128] | field_lookback:transformer[lookback=32] | toyota | test1 | rmse_h50 | 1.14 | 1.03 | +0.101 [+0.029, +0.182] | 19/43 | 56/129 | 0.0708 |
| field_lookback:transformer[lookback=128] | field_lookback:transformer[lookback=32] | toyota | test2 | rmse_h50 | 2.36 | 2.7 | -0.338 [-0.421, -0.255] | 34/40 | 102/120 | 2.07e-08 |
