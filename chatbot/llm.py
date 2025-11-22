"""LLM helpers for the Academate agent."""

from __future__ import annotations

from google.adk.models.google_llm import Gemini

from chatbot.configs import MODEL_NAME, RETRY_CONFIG


def build_llm() -> Gemini:
    """Return a Gemini client configured for the project."""
    return Gemini(model=MODEL_NAME, retry_options=RETRY_CONFIG)
