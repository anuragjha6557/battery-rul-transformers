# Severson 2019 reproduction (Toyota / MIT-Stanford, cycles 1-100 features)

Target: log10(cycle life) (provider label); ElasticNetCV (4-fold), official train split.
Cells dropped for missing features/label: 0.
Temperature feature uses per-cycle `discharge_temp_max_c` (only one available).

| model | split | n cells | RMSE (cycles) | mean % error |
|---|---|---|---|---|
| variance | train | 41 | 104 | 14.2 |
| variance | test1 | 43 | 137 | 14.8 |
| variance | test2 | 40 | 196 | 11.4 |
| discharge | train | 41 | 65 | 8.8 |
| discharge | test1 | 43 | 107 | 12.7 |
| discharge | test2 | 40 | 174 | 11.7 |
| full | train | 41 | 70 | 7.6 |
| full | test1 | 43 | 77 | 10.2 |
| full | test2 | 40 | 292 | 26.8 |

Published mean % error (train / primary test / secondary test), recalled from Severson
et al. 2019 Table 1 -- **published values to verify** against the paper before citing:

| model | published (unverified) |
|---|---|
| variance | ~14 / ~15 / ~11 |
| discharge | ~10 / ~13 / ~11 |
| full | ~5.6 / ~7.5 / ~10.7 (abstract: 9.1 % test error) |
