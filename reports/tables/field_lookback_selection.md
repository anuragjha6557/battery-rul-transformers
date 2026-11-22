| dataset | task | model | lookback | inner-val RMSE (% SOH) | runs | selected |
|---|---|---|---|---|---|---|
| calce | forecast | itransformer | 32 | 4.451 | 12 | **yes** |
| calce | forecast | itransformer | 128 | 5.233 | 12 |  |
| calce | forecast | lstm | 32 | 2.960 | 12 |  |
| calce | forecast | lstm | 128 | 2.890 | 12 | **yes** |
| calce | forecast | transformer | 32 | 3.306 | 12 | **yes** |
| calce | forecast | transformer | 128 | 3.463 | 12 |  |
| calce | soh | itransformer | 32 | 3.057 | 12 | **yes** |
| calce | soh | itransformer | 128 | 3.857 | 12 |  |
| calce | soh | lstm | 32 | 2.142 | 12 | **yes** |
| calce | soh | lstm | 128 | 2.157 | 12 |  |
| calce | soh | transformer | 32 | 3.684 | 12 |  |
| calce | soh | transformer | 128 | 2.840 | 12 | **yes** |
| toyota | forecast | itransformer | 32 | 1.418 | 3 | **yes** |
| toyota | forecast | itransformer | 128 | 1.442 | 3 |  |
| toyota | forecast | lstm | 32 | 1.594 | 3 |  |
| toyota | forecast | lstm | 128 | 1.592 | 3 | **yes** |
| toyota | forecast | patchtst | 32 | 2.357 | 3 |  |
| toyota | forecast | patchtst | 128 | 2.160 | 1 | **yes** |
| toyota | forecast | transformer | 32 | 1.886 | 3 | **yes** |
| toyota | forecast | transformer | 128 | 1.963 | 3 |  |
| toyota | soh | itransformer | 32 | 1.326 | 3 |  |
| toyota | soh | itransformer | 128 | 1.321 | 3 | **yes** |
| toyota | soh | lstm | 32 | 1.152 | 3 | **yes** |
| toyota | soh | lstm | 128 | 1.159 | 3 |  |
| toyota | soh | transformer | 32 | 1.189 | 3 | **yes** |
| toyota | soh | transformer | 128 | 1.378 | 3 |  |
