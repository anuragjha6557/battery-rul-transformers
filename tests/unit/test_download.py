"""Downloader: resume after a silently truncated transfer, checksum enforcement."""

from __future__ import annotations

import hashlib
import io
from pathlib import Path
from typing import Any

import pytest

from battery_rul.data import download as dl

PAYLOAD = bytes(range(256)) * 400  # 102 400 bytes


class _FakeResp(io.BytesIO):
    def __init__(self, body: bytes, status: int, length: int) -> None:
        super().__init__(body)
        self.status = status
        self.headers = {"Content-Length": str(length)}

    def __enter__(self) -> _FakeResp:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()


def _fake_server(drop_after: int | None) -> Any:
    """Serves PAYLOAD honouring Range; the first response is cut short at drop_after bytes."""
    calls = {"n": 0}

    def urlopen(req: Any, timeout: int) -> _FakeResp:
        calls["n"] += 1
        rng = req.headers.get("Range")
        start = int(rng.split("=")[1].rstrip("-")) if rng else 0
        rest = PAYLOAD[start:]
        body = rest[:drop_after] if (drop_after is not None and calls["n"] == 1) else rest
        # Content-Length always advertises the full remainder (like a real dropped connection)
        return _FakeResp(body, 206 if rng else 200, len(rest))

    return urlopen, calls


def _remote(sha: str | None) -> dl.RemoteFile:
    return dl.RemoteFile(url="https://example.invalid/f.bin", filename="f.bin", sha256=sha)


def test_resumes_truncated_transfer(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    urlopen, calls = _fake_server(drop_after=30_000)
    monkeypatch.setattr(dl.urllib.request, "urlopen", urlopen)
    out = dl.fetch(_remote(hashlib.sha256(PAYLOAD).hexdigest()), tmp_path)
    assert out.read_bytes() == PAYLOAD
    assert calls["n"] == 2  # one short transfer + one resumed range request


def test_checksum_mismatch_raises(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    urlopen, _ = _fake_server(drop_after=None)
    monkeypatch.setattr(dl.urllib.request, "urlopen", urlopen)
    with pytest.raises(RuntimeError, match="Checksum mismatch"):
        dl.fetch(_remote("0" * 64), tmp_path)
    assert not (tmp_path / "f.bin").exists()


def test_cached_valid_file_is_not_redownloaded(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    (tmp_path / "f.bin").write_bytes(PAYLOAD)

    def boom(*a: Any, **k: Any) -> None:
        raise AssertionError("network must not be touched")

    monkeypatch.setattr(dl.urllib.request, "urlopen", boom)
    monkeypatch.setattr(dl, "RAW_DIR", tmp_path)
    assert dl.fetch(_remote(hashlib.sha256(PAYLOAD).hexdigest()), tmp_path).exists()
