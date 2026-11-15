# Data

Raw and processed data are **never committed**. `data/raw/` and `data/processed/` are gitignored and rebuilt by `make data` (`battery-rul download all && battery-rul build-data all`). The download step checks SHA-256 sums recorded in `src/battery_rul/data/download.py`.

## Sources (verified 2026-11-15)

| Dataset | Cells used | URL | Raw format | Citation |
|---|---|---|---|---|
| NASA PCoE Battery Data Set (#5) | B0005, B0006, B0007, B0018 | `https://phm-datasets.s3.amazonaws.com/NASA/5.+Battery+Data+Set.zip` → inner `1. BatteryAgingARC-FY08Q4.zip` | MATLAB v5 `.mat` per cell; `cycle[]` struct of charge / discharge / impedance entries | B. Saha and K. Goebel, "Battery Data Set", NASA Ames Prognostics Data Repository, 2007. |
| CALCE CS2 (LiCoO2, 1.1 Ah prismatic) | CS2_35, CS2_36, CS2_37, CS2_38 | `https://web.calce.umd.edu/batteries/data/CS2_3{5,6,7,8}.zip` (server is slow; allow long timeouts) | zip of Arbin `.xlsx` files, one per test session | CALCE Battery Research Group, University of Maryland. Y. Xing et al., Microelectron. Rel. 53 (2013) 811–820. |
| Toyota / MIT / Stanford fast-charging (Severson 2019) | 124 LFP/graphite A123 18650 cells, 3 batches | `https://data.matr.io/1/api/v1/file/{5c86c0b5fa2ede00015ddf66, 5c86bf13fa2ede00015ddd82, 5c86bd64fa2ede00015ddbb2}/download` | MATLAB v7.3 (HDF5) `.mat`, one per batch | K. A. Severson et al., "Data-driven prediction of battery cycle life before capacity degradation", *Nature Energy* 4, 383–391 (2019). |

Terms: NASA asks that publications acknowledge the repository and the data donors, and the data is used at the user's own risk. CALCE and Toyota/MIT/Stanford ask for the citations above. The MIT/Stanford *modelling* code is under academic licence and is **not** used here; only the publicly documented data-cleaning steps are re-implemented.

## Layout

```
data/
├── raw/
│   ├── nasa/     B0005.mat B0006.mat B0007.mat B0018.mat README.txt (+ original zip)
│   ├── calce/    CS2_35.zip … CS2_38.zip (extracted to CS2_35/ … on build)
│   └── toyota/   2017-05-12_batchdata_updated_struct_errorcorrect.mat, 2017-06-30_…, 2018-04-12_…
└── processed/
    └── <dataset>/ cells.parquet  cycles.parquet  curves.parquet
```

The three processed tables follow the contract in `src/battery_rul/data/schema.py` (units, sign conventions, cycle pairing, no label columns). Labels (EOL, RUL, horizons) are built in `battery_rul.tasks`.

## Known data facts (from inspection; expanded in `reports/data_quality.md`)
- NASA B0005: 616 entries (170 charge, 168 discharge, 278 impedance); 168 capacity-measured cycles; first capacity 1.856 Ah, not the nominal 2.0 Ah. This is why SOH is normalized to each cell's first 5 cycles (ADR-0005).
- NASA cells were cycled with rest periods of varying length, which causes capacity "regeneration" spikes. The `rest_before_s` column records the idle time so models can explain them.
