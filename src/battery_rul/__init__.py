"""battery_rul: leakage-free battery SOH / capacity-forecast / RUL benchmark."""

from importlib.metadata import PackageNotFoundError, version

# macOS: torch and lightgbm each ship their own libomp. If torch is imported first, a later
# multi-threaded LightGBM fit aborts ("OMP: Error #179 pthread_mutex_init failed"). Importing
# lightgbm first is the known-good order, so do it before anything in this package loads torch.
import lightgbm  # noqa: F401

try:
    __version__ = version("battery-rul")
except PackageNotFoundError:  # pragma: no cover - only when running from an uninstalled tree
    __version__ = "0.0.0"

__all__ = ["__version__"]
