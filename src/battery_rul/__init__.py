"""battery_rul: leakage-free battery SOH / capacity-forecast / RUL benchmark."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("battery-rul")
except PackageNotFoundError:  # pragma: no cover - only when running from an uninstalled tree
    __version__ = "0.0.0"

__all__ = ["__version__"]
