"""Import the package first so its libomp-ordering guard (lightgbm before torch) runs before any
test module imports torch (see ``battery_rul/__init__.py``)."""

import battery_rul  # noqa: F401
