"""Helpers for libais."""

from typing import Any


def MaybeToNumber(instance: Any) -> Any:
  """Convert to an int or float if possible."""
  if isinstance(instance, (float, int)) or instance is None:
    return instance

  try:
    return int(instance)
  except (TypeError, ValueError):
    pass

  try:
    return float(instance)
  except (TypeError, ValueError):
    pass

  return instance
