"""Logging helpers to keep the agent observable."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

_LOGGER: Optional[logging.Logger] = None


def get_logger() -> logging.Logger:
    global _LOGGER
    if _LOGGER is not None:
        return _LOGGER

    logs_dir = Path.cwd() / "logs"
    logs_dir.mkdir(exist_ok=True)

    logger = logging.getLogger("academate")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.FileHandler(logs_dir / "agent.log", encoding="utf-8")
        handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        )
        logger.addHandler(handler)

    _LOGGER = logger
    return logger


__all__ = ["get_logger"]
