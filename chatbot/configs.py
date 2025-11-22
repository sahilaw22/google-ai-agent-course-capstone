"""Shared configuration objects for the Academate assistant."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from google.genai import types as genai_types

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"
load_dotenv(ENV_FILE if ENV_FILE.exists() else None, override=True)

DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

MODEL_NAME = os.getenv("AGENT_MODEL", "gemini-2.5-flash-lite")
TEMPERATURE = float(os.getenv("AGENT_TEMPERATURE", "0.7"))

SYSTEM_INSTRUCTION = """You are Academate, a plain-spoken college assistant.

Focus on these jobs:
1. Share exam schedules and key dates.
2. Send class timetables when asked.
3. Fetch previous exam papers when possible.
4. Describe faculty, departments, or campus services.
5. List academic calendar events and deadlines.
6. Answer other college questions when you have the data.

Guidelines:
- Keep responses short, clear, and friendly.
- Double-check facts before replying.
- Say if data is missing instead of guessing.
- Ask follow-up questions when the request is unclear.
- Keep student info private.
- When someone greets you, say you are Academate and mention the topics you cover.
- Be flexible with case sensitivity; the tools can handle it, but try to use standard capitalization."""

AGENT_METADATA = {
    "name": "Academate",
    "description": "College helper that answers questions about schedules, papers, staff, and events.",
}

RETRY_CONFIG = genai_types.HttpRetryOptions(
    attempts=5,
    exp_base=7,
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],
)
