"""Download raw datasets into ``data/raw/<dataset>/`` with SHA-256 verification.

Idempotent: files that already exist with the expected checksum are skipped.
A checksum of ``None`` means "not pinned yet"; the computed hash is printed so it
can be pinned here. Pinned checksums make silent upstream changes visible.
"""

from __future__ import annotations

import hashlib
import shutil
import urllib.request
import zipfile
from dataclasses import dataclass
from pathlib import Path

from rich.console import Console
from rich.progress import BarColumn, DownloadColumn, Progress, TransferSpeedColumn

from battery_rul.utils import RAW_DIR

console = Console()
_CHUNK = 1 << 20


@dataclass(frozen=True)
class RemoteFile:
    url: str
    filename: str
    sha256: str | None
    timeout_s: int = 600


NASA_FILES: tuple[RemoteFile, ...] = (
    RemoteFile(
        url="https://phm-datasets.s3.amazonaws.com/NASA/5.+Battery+Data+Set.zip",
        filename="nasa_battery_5.zip",
        sha256="82302a7db4fc1b34e0b6676326610438d43b816bdf11a69d1d012a464ef2f92e",
    ),
)
#: Checksums of the four cell files extracted from the inner FY08Q4 zip.
NASA_CELL_SHA256: dict[str, str] = {
    "B0005.mat": "0eae4585baf3f200c09fe24c5ab884f1889679fc75206ca1aa19da704104f0b0",
    "B0006.mat": "fa818ab4db5db8ab21e910b6dd6c3e20d3761bb9672089e1a4de8f96074616c5",
    "B0007.mat": "d022afa086efaf54ab5b63f05220f5be178c8027e2fa8d68589db0e85a441a3b",
    "B0018.mat": "d1e6c923a43ea1c9666b3a90bbb521757a067fd60b4d17dbfaa49c50b179da69",
    "README.txt": "2b0614ccfdde3ca9c0466ad3e0c03903a1dbe98aec22dbe7ea410219cde51f90",
}
_NASA_INNER_ZIP = "5. Battery Data Set/1. BatteryAgingARC-FY08Q4.zip"

CALCE_FILES: tuple[RemoteFile, ...] = tuple(
    RemoteFile(
        url=f"https://web.calce.umd.edu/batteries/data/CS2_{n}.zip",
        filename=f"CS2_{n}.zip",
        sha256=None,  # pinned after first verified download
        timeout_s=1800,  # the CALCE server is slow
    )
    for n in (35, 36, 37, 38)
)

_MATR = "https://data.matr.io/1/api/v1/file/{}/download"
TOYOTA_FILES: tuple[RemoteFile, ...] = (
    RemoteFile(
        _MATR.format("5c86c0b5fa2ede00015ddf66"),
        "2017-05-12_batchdata_updated_struct_errorcorrect.mat",
        None,
        3600,
    ),
    RemoteFile(
        _MATR.format("5c86bf13fa2ede00015ddd82"),
        "2017-06-30_batchdata_updated_struct_errorcorrect.mat",
        None,
        3600,
    ),
    RemoteFile(
        _MATR.format("5c86bd64fa2ede00015ddbb2"),
        "2018-04-12_batchdata_updated_struct_errorcorrect.mat",
        None,
        3600,
    ),
)

REGISTRY: dict[str, tuple[RemoteFile, ...]] = {
    "nasa": NASA_FILES,
    "calce": CALCE_FILES,
    "toyota": TOYOTA_FILES,
}


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(_CHUNK), b""):
            h.update(chunk)
    return h.hexdigest()


def _verify(path: Path, expected: str | None) -> bool:
    actual = sha256_of(path)
    if expected is None:
        console.print(f"[yellow]unpinned[/] {path.name} sha256={actual}")
        return True
    if actual != expected:
        console.print(f"[red]checksum mismatch[/] {path.name}: expected {expected}, got {actual}")
        return False
    return True


def fetch(remote: RemoteFile, dest_dir: Path) -> Path:
    """Download one file (skip if present and valid). Returns the local path."""
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / remote.filename
    if dest.exists() and _verify(dest, remote.sha256):
        console.print(f"[green]ok[/] {dest.relative_to(RAW_DIR.parent)} (cached)")
        return dest

    tmp = dest.with_suffix(dest.suffix + ".part")
    req = urllib.request.Request(remote.url, headers={"User-Agent": "battery-rul/0.1"})
    with (
        urllib.request.urlopen(req, timeout=remote.timeout_s) as resp,
        tmp.open("wb") as out,
        Progress(
            "[progress.description]{task.description}",
            BarColumn(),
            DownloadColumn(),
            TransferSpeedColumn(),
            console=console,
        ) as progress,
    ):
        total = int(resp.headers.get("Content-Length") or 0) or None
        task = progress.add_task(remote.filename, total=total)
        for chunk in iter(lambda: resp.read(_CHUNK), b""):
            out.write(chunk)
            progress.advance(task, len(chunk))
    if not _verify(tmp, remote.sha256):
        tmp.unlink(missing_ok=True)
        raise RuntimeError(f"Checksum mismatch for {remote.url}")
    tmp.replace(dest)
    return dest


def _extract_nasa(outer_zip: Path) -> None:
    dest = outer_zip.parent
    if all((dest / f).exists() for f in NASA_CELL_SHA256):
        return
    with zipfile.ZipFile(outer_zip) as outer, outer.open(_NASA_INNER_ZIP) as inner_f:
        inner_path = dest / "_inner_fy08q4.zip"
        with inner_path.open("wb") as tmp:
            shutil.copyfileobj(inner_f, tmp)
    with zipfile.ZipFile(inner_path) as inner:
        for name in NASA_CELL_SHA256:
            with inner.open(name) as src, (dest / name).open("wb") as dst:
                shutil.copyfileobj(src, dst)
    inner_path.unlink()


def download(dataset: str) -> list[Path]:
    """Download (and for NASA, extract) one dataset. ``dataset='all'`` downloads everything."""
    names = list(REGISTRY) if dataset == "all" else [dataset]
    paths: list[Path] = []
    for name in names:
        if name not in REGISTRY:
            raise ValueError(f"Unknown dataset {name!r}; choose from {[*REGISTRY, 'all']}")
        dest_dir = RAW_DIR / name
        for remote in REGISTRY[name]:
            paths.append(fetch(remote, dest_dir))
        if name == "nasa":
            _extract_nasa(dest_dir / NASA_FILES[0].filename)
            for fname, digest in NASA_CELL_SHA256.items():
                if not _verify(dest_dir / fname, digest):
                    raise RuntimeError(f"NASA extracted file {fname} failed checksum")
    return paths
