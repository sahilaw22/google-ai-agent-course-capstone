"""Simple session memory utilities for Academate."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, List, Sequence

Message = Dict[str, str]


@dataclass
class SessionMemory:
    """In-memory transcript store keyed by session id."""

    _store: Dict[str, List[Message]] = field(default_factory=lambda: defaultdict(list))

    def append(self, session_id: str, role: str, content: str) -> None:
        self._store[session_id].append({"role": role, "content": content})

    def get_history(self, session_id: str, limit: int | None = None) -> Sequence[Message]:
        history = self._store.get(session_id, [])
        if limit is None or limit >= len(history):
            return list(history)
        return history[-limit:]

    def clear(self, session_id: str) -> None:
        self._store.pop(session_id, None)

    def summarize(self, session_id: str) -> str:
        history = self._store.get(session_id, [])
        if not history:
            return "No prior context."
        summary_lines = [
            f"{msg['role'].title()}: {msg['content']}" for msg in history[-5:]
        ]
        return "\n".join(summary_lines)


SESSION_MEMORY = SessionMemory()

__all__ = ["SESSION_MEMORY", "SessionMemory"]
