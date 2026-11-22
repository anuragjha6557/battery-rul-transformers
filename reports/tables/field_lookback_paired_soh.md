| candidate | reference | dataset | split | metric | cand_mean | ref_mean | delta [95% CI] | k_cells | k_pairs | wilcoxon_p |
|---|---|---|---|---|---|---|---|---|---|---|
| field_lookback:itransformer[lookback=128] | field_lookback:itransformer[lookback=32] | calce | loco | rmse | 3.37 | 3.24 | +0.129 [-0.547, +0.749] | 2/4 | 4/12 | nan |
| field_lookback:itransformer[lookback=128] | field_lookback:itransformer[lookback=32] | toyota | test1 | rmse | 1.02 | 1.04 | -0.025 [-0.089, +0.045] | 22/43 | 76/129 | 0.3 |
| field_lookback:itransformer[lookback=128] | field_lookback:itransformer[lookback=32] | toyota | test2 | rmse | 1.54 | 1.6 | -0.062 [-0.152, +0.025] | 20/40 | 71/120 | 0.295 |
| field_lookback:lstm[lookback=128] | field_lookback:lstm[lookback=32] | calce | loco | rmse | 2.05 | 2.09 | -0.045 [-0.134, +0.059] | 3/4 | 7/12 | nan |
| field_lookback:lstm[lookback=128] | field_lookback:lstm[lookback=32] | toyota | test1 | rmse | 1.07 | 1.07 | -0.001 [-0.009, +0.006] | 17/43 | 51/129 | 0.335 |
| field_lookback:lstm[lookback=128] | field_lookback:lstm[lookback=32] | toyota | test2 | rmse | 2.18 | 2.16 | +0.024 [+0.021, +0.027] | 0/40 | 42/120 | 1.82e-12 |
| field_lookback:transformer[lookback=128] | field_lookback:transformer[lookback=32] | calce | loco | rmse | 2.94 | 3.34 | -0.398 [-1.338, +0.257] | 3/4 | 6/12 | nan |
| field_lookback:transformer[lookback=128] | field_lookback:transformer[lookback=32] | toyota | test1 | rmse | 1.01 | 0.885 | +0.129 [+0.027, +0.258] | 11/43 | 42/129 | 0.000837 |
| field_lookback:transformer[lookback=128] | field_lookback:transformer[lookback=32] | toyota | test2 | rmse | 2.7 | 2.66 | +0.034 [-0.045, +0.121] | 24/40 | 64/120 | 0.91 |
