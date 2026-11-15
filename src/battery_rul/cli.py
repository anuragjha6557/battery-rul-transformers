"""Command-line entry point: ``battery-rul <command>``.

Commands are added phase by phase (see docs/PLAN.md §7). Unimplemented
commands exit with a clear message rather than silently doing nothing.
"""

from __future__ import annotations

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
    _not_yet("Phase 1")


@app.command()
def benchmark(config: str = typer.Option(..., help="Experiment config name")) -> None:
    """Run a benchmark experiment and log to MLflow."""
    _not_yet("Phase 3")


@app.command()
def predict(csv_path: str = typer.Argument(..., help="Cycle-level CSV to score")) -> None:
    """Predict SOH trajectory and RUL distribution for an uploaded cell."""
    _not_yet("Phase 8")


if __name__ == "__main__":  # pragma: no cover
    app()
