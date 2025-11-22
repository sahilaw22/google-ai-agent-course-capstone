"""Lightweight CSV data access helpers for Academate."""

from __future__ import annotations

import csv
from functools import lru_cache
from pathlib import Path
from typing import Dict, List

from chatbot.configs import DATA_DIR

DATASETS: Dict[str, str] = {
    "students": "students.csv",
    "exam_schedule": "exam_schedule.csv",
    "timetable": "timetable.csv",
    "faculty": "faculty.csv",
    "academic_calendar": "academic_calendar.csv",
    "previous_papers": "previous_papers.csv",
    "student_results": "student_results.csv",
}


def dataset_path(name: str) -> Path:
    """Return the on-disk path for a dataset name."""
    if name not in DATASETS:
        raise KeyError(f"Unknown dataset '{name}'")
    return DATA_DIR / DATASETS[name]


@lru_cache(maxsize=None)
def load_rows(name: str) -> List[Dict[str, str]]:
    """Load a dataset as a list of dictionaries (cached)."""
    path = dataset_path(name)
    if not path.exists():
        raise FileNotFoundError(f"Dataset missing: {path}")

    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            {key: (value.strip() if isinstance(value, str) else value) for key, value in row.items()}
            for row in reader
        ]


@lru_cache(maxsize=None)
def load_map(name: str, key_field: str) -> Dict[str, Dict[str, str]]:
    """Load a dataset indexed by a specific field (cached)."""
    rows = load_rows(name)
    return {row[key_field]: row for row in rows if key_field in row}


def clear_cache() -> None:
    """Reset cached datasets; handy for tests."""
    load_rows.cache_clear()
    load_map.cache_clear()


__all__ = ["load_rows", "load_map", "clear_cache", "DATASETS", "dataset_path"]
