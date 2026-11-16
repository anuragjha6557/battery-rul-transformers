"""Command-line entry point: ``battery-rul <command>``.

Commands are added phase by phase (see docs/PLAN.md §7). Unimplemented
commands exit with a clear message rather than silently doing nothing.
"""

from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console

from battery_rul import __version__

app = typer.Typer(
    name="battery-rul",
    help="Leakage-free battery SOH / capacity-forecast / RUL benchmark.",
    no_args_is_help=True,
    add_completion=False,
)
console = Console()


def _not_yet(phase: str) -> None:
    console.print(f"[yellow]Not implemented yet — scheduled for {phase} (docs/PLAN.md §7).[/]")
    raise typer.Exit(code=2)


@app.command()
def version() -> None:
    """Print the package version."""
    console.print(__version__)


@app.command()
def download(dataset: str = typer.Argument("all", help="nasa | calce | toyota | all")) -> None:
    """Download raw datasets into data/raw with checksum verification."""
    from battery_rul.data.download import download as _download

    _download(dataset)


@app.command("build-data")
def build_data(dataset: str = typer.Argument("all", help="nasa | calce | toyota | all")) -> None:
    """Parse raw files into canonical cycles/curves parquet tables."""
    import importlib

    builders = {
        "nasa": "battery_rul.data.nasa",
        "calce": "battery_rul.data.calce",
        "toyota": "battery_rul.data.toyota",
    }
    known = ("nasa", "calce", "toyota")
    if dataset not in (*known, "all"):
        console.print(f"[red]Unknown dataset {dataset!r}.[/]")
        raise typer.Exit(code=1)
    targets = known if dataset == "all" else (dataset,)
    for name in targets:
        if name not in builders:
            if dataset == "all":
                console.print(f"[yellow]{name}: loader not implemented yet, skipped.[/]")
                continue
            _not_yet("Phase 1")
        tables = importlib.import_module(builders[name]).build()
        console.print(
            f"[green]{name}:[/] {len(tables.cells)} cells, {len(tables.cycles)} cycles, "
            f"{len(tables.curves)} curve rows"
        )


@app.command("build-features")
def build_features(
    dataset: str = typer.Argument("all", help="nasa | calce | toyota | all"),
) -> None:
    """Compute cached per-cycle curve features (ICA, dQ(V)) into curve_features.parquet."""
    import time

    from battery_rul.features.curves import build_curve_features

    known = ("nasa", "calce", "toyota")
    if dataset not in (*known, "all"):
        console.print(f"[red]Unknown dataset {dataset!r}.[/]")
        raise typer.Exit(code=1)
    for name in known if dataset == "all" else (dataset,):
        t0 = time.perf_counter()
        f = build_curve_features(name)
        console.print(f"[green]{name}:[/] {len(f)} cycles in {time.perf_counter() - t0:.1f}s")


@app.command()
def benchmark(
    config: str = typer.Option(..., help="Experiment config name (configs/experiment/<name>.yaml)"),
    n_jobs: int = typer.Option(None, help="Parallel worker processes (default: from config)"),
    override: list[str] = typer.Option([], "--override", "-o", help="Hydra override"),  # noqa: B008
) -> None:
    """Run a benchmark experiment and log to MLflow (resumable)."""
    from battery_rul.train.config import load_experiment
    from battery_rul.train.runner import run_experiment

    cfg = load_experiment(config, list(override))
    s = run_experiment(cfg, n_jobs=n_jobs)
    console.print(
        f"[green]{cfg.name}:[/] {s.n_units} units: {s.n_run} run, {s.n_resumed} resumed, "
        f"{s.n_skipped} skipped (no samples), {s.n_unsupported} unsupported model/task pairs. "
        f"parent run {s.parent_run_id}"
    )


@app.command()
def tune(
    model: str = typer.Option(..., help="Model config name (configs/model/<name>.yaml)"),
    task: str = typer.Option(..., help="soh | forecast | rul"),
    n_trials: int = typer.Option(50, help="Trials to add to the study (equal budget: 50)"),
    n_jobs: int = typer.Option(4, help="Parallel worker processes sharing the study"),
    train_stride: int = typer.Option(4, help="Keep every k-th training origin per cell"),
    journal: str = typer.Option(
        None, help="Optuna journal file (default: <project>/optuna/journal.log)"
    ),
) -> None:
    """Tune a model on Toyota train (inner grouped 5-fold CV); resumes an existing study."""
    from battery_rul.train.tune import TuningError, format_result
    from battery_rul.train.tune import tune as _tune

    try:
        res = _tune(
            model,
            task,
            n_trials=n_trials,
            n_jobs=n_jobs,
            train_stride=train_stride,
            journal=Path(journal) if journal else None,
        )
    except TuningError as e:
        console.print(f"[red]{e}[/]")
        raise typer.Exit(code=1) from e
    console.print(format_result(res))


@app.command()
def report(
    experiment: str = typer.Option(..., help="Experiment name"),
    tracking_uri: str = typer.Option(None, help="MLflow tracking URI (default: env/sqlite)"),
) -> None:
    """Write reports/tables/<experiment>.{md,csv} from FINISHED MLflow runs."""
    from battery_rul.eval.report import write_report
    from battery_rul.train.config import default_tracking_uri

    md, csv = write_report(experiment, tracking_uri or default_tracking_uri())
    console.print(f"[green]wrote[/] {md} and {csv}")


@app.command()
def predict(csv_path: str = typer.Argument(..., help="Cycle-level CSV to score")) -> None:
    """Predict SOH trajectory and RUL distribution for an uploaded cell."""
    _not_yet("Phase 8")


if __name__ == "__main__":  # pragma: no cover
    app()
