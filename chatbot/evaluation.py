"""Lightweight evaluation harness for the Academate tools."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, List

from chatbot.tools import (
    check_student_results,
    fetch_previous_papers,
    get_academic_calendar,
    get_class_timetable,
    get_faculty_info,
    query_exam_schedule,
)


@dataclass
class EvalCase:
    name: str
    run: Callable[[], str]
    expected_substrings: List[str]

    def execute(self) -> tuple[bool, str]:
        output = self.run()
        passed = all(text.lower() in output.lower() for text in self.expected_substrings)
        return passed, output


def run_evaluations() -> dict:
    cases = [
        EvalCase(
            name="Exam Schedule",
            run=lambda: query_exam_schedule("Computer Science", 3, "2024-25"),
            expected_substrings=["Data Structures", "Hall"],
        ),
        EvalCase(
            name="Timetable",
            run=lambda: get_class_timetable(student_id="CS2024001"),
            expected_substrings=["Department:", "Monday"],
        ),
        EvalCase(
            name="Faculty",
            run=lambda: get_faculty_info(faculty_name="Ramesh"),
            expected_substrings=["Ramesh", "Faculty"],
        ),
        EvalCase(
            name="Academic Calendar",
            run=lambda: get_academic_calendar(days_ahead=30),
            expected_substrings=["events"],
        ),
        EvalCase(
            name="Student Results",
            run=lambda: check_student_results("CS2024001"),
            expected_substrings=["Student", "SGPA"],
        ),
        EvalCase(
            name="Previous Papers",
            run=lambda: fetch_previous_papers("CS301", years=3),
            expected_substrings=["2023", "CS301"],
        ),
    ]

    summary = {}
    for case in cases:
        passed, output = case.execute()
        summary[case.name] = {"passed": passed, "preview": output[:200]}
    return summary


__all__ = ["run_evaluations"]
