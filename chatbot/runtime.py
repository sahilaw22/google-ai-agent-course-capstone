"""Runtime wiring for the Academate assistant."""

from __future__ import annotations

import asyncio
from typing import Iterable, Optional, Tuple

from google.adk.agents import LlmAgent
from google.adk.runners import InMemoryRunner

from chatbot.configs import AGENT_METADATA, MODEL_NAME, SYSTEM_INSTRUCTION, TEMPERATURE
from chatbot.llm import build_llm
from chatbot.tools import get_all_tools
from chatbot.memory import SESSION_MEMORY
from chatbot.observability import get_logger


def build_agent(tools: Optional[Iterable] = None) -> LlmAgent:
    """Return a configured Academate agent."""
    return LlmAgent(
        name=AGENT_METADATA["name"],
        model=build_llm(),
        description=AGENT_METADATA["description"],
        instruction=SYSTEM_INSTRUCTION,
        tools=list(tools or []),
    )


def build_agent_bundle(tools: Optional[Iterable] = None) -> Tuple[LlmAgent, InMemoryRunner]:
    """Return both the agent and an in-memory runner."""
    selected_tools = list(tools or get_all_tools())
    agent = build_agent(selected_tools)
    runner = InMemoryRunner(agent=agent)
    return agent, runner


def build_runner(tools: Optional[Iterable] = None) -> InMemoryRunner:
    """Bind the agent to an in-memory runner for quick experiments."""
    _, runner = build_agent_bundle(tools)
    return runner


def get_agent() -> LlmAgent:
    """Return the agent with all tools configured for ADK Web."""
    return build_agent(get_all_tools())


def run_cli() -> None:
    """Start a conversational loop similar to the capstone demo."""
    logger = get_logger()
    print("=" * 60)
    print("🎓 ACADEMATE - College Helper")
    print("=" * 60)
    print("\nHere to help with college info.")
    print("Type 'exit' or 'quit' when you are done.\n")

    tools = get_all_tools()
    agent, runner = build_agent_bundle(tools=tools)
    print(f" Agent loaded with {len(tools)} tools")
    print(f" Model: {MODEL_NAME}")
    print(f"  Temperature: {TEMPERATURE}")

    session_id = "cli-session"

    async def _chat_loop():
        while True:
            try:
                user_input = input("\nYou: ").strip()

                if not user_input:
                    continue

                if user_input.lower() in {"exit", "quit", "bye"}:
                    print("\n Bye!\n")
                    break

                print("\n Academate: ", end="", flush=True)
                SESSION_MEMORY.append(session_id, "user", user_input)
                logger.info("User input", extra={"session": session_id, "text": user_input})
                await runner.run_debug(user_input)
                SESSION_MEMORY.append(session_id, "assistant", "Response streamed via run_debug")
            except KeyboardInterrupt:
                raise
            except Exception as exc:  
                print(f"\n Error: {exc}")
                print("Please try again.\n")
                logger.exception("CLI loop error", extra={"session": session_id})

    try:
        asyncio.run(_chat_loop())
    except KeyboardInterrupt:
        print("\n Bye!\n")


__all__ = ["build_agent", "build_agent_bundle", "build_runner", "run_cli"]

