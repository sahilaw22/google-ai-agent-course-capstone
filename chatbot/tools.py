"""CSV-backed helper functions that the Gemini agent can call."""
from __future__ import annotations

from datetime import date, datetime, timedelta
from typing import List, Optional

from chatbot.datasets import load_rows, load_map

DATE_FMT = "%Y-%m-%d"


def _casefold(value: Optional[str]) -> str:
    return (value or "").strip().casefold()


def _parse_date(value: str) -> date:
    return datetime.strptime(value, DATE_FMT).date()


def query_exam_schedule(
    department: str,
    semester: int,
    academic_year: Optional[str] = None,
) -> str:
    """Return a formatted exam schedule for the given group."""
    exams = [
        row
        for row in load_rows("exam_schedule")
        if _casefold(row["department"]) == _casefold(department)
        and int(row["semester"]) == int(semester)
    ]

    if academic_year:
        exams = [row for row in exams if row["academic_year"] == academic_year]
    elif exams:
        academic_year = exams[0]["academic_year"]

    if not exams:
        scope = f"{department}, semester {semester}"
        if academic_year:
            scope += f" in {academic_year}"
        return f"No exam schedule found for {scope}."

    exams.sort(key=lambda row: (_parse_date(row["exam_date"]), row["exam_time"]))
    lines = [
        f" **Exam Schedule – {department} – Semester {semester}**",
        f"Academic Year: {academic_year}",
        "",
    ]

    for exam in exams:
        lines.append(f" {exam['subject_name']} ({exam['subject_code']})")
        lines.append(f" Date: {_parse_date(exam['exam_date']).strftime('%d %B %Y')}")
        lines.append(f" Time: {exam['exam_time']}")
        lines.append(f" Duration: {exam['duration_minutes']} minutes")
        lines.append(f" Room: {exam['room_number']}")
        lines.append(f" Type: {exam['exam_type']}")
        lines.append(f" Total Marks: {exam['total_marks']}")
        lines.append("")

    return "\n".join(lines).strip()


def fetch_previous_papers(
    subject_code: str,
    years: Optional[int] = 3,
    paper_type: Optional[str] = None,
) -> str:
    """List older papers for a subject with links when available."""
    current_year = datetime.now().year
    min_year = current_year - (years or 3)

    papers = [
        row
        for row in load_rows("previous_papers")
        if _casefold(row["subject_code"]) == _casefold(subject_code)
        and int(row["exam_year"]) >= min_year
        and (not paper_type or _casefold(row["paper_type"]) == _casefold(paper_type))
    ]

    if not papers:
        return f"No previous papers found for {subject_code} in the last {years} years."

    papers.sort(key=lambda row: int(row["exam_year"]), reverse=True)
    lines = [f" Previous Papers – {subject_code.upper()}", ""]

    for paper in papers:
        lines.append(f" {paper['exam_year']} – {paper['paper_type']}")
        lines.append(f" Subject: {paper['subject_name']}")
        lines.append(f" Department: {paper['department']} | Semester: {paper['semester']}")
        lines.append(f" Marks: {paper['total_marks']}\n   Link: {paper.get('file_url', 'Not available')}")
        lines.append("")

    return "\n".join(lines).strip()


def get_class_timetable(
    student_id: Optional[str] = None,
    department: Optional[str] = None,
    semester: Optional[int] = None,
    section: Optional[str] = None,
    week_day: Optional[str] = None,
) -> str:
    """Show a weekly timetable or a single day schedule."""
    if student_id:
        students_map = load_map("students", "student_id")
        if student_id not in students_map:
            return f"Student {student_id} not found."
        student = students_map[student_id]
        department = department or student["department"]
        semester = semester or int(student["semester"])
        section = section or student.get("section")

    if not department or semester is None:
        return "Please provide either student_id or (department and semester)."

    slots = [
        row
        for row in load_rows("timetable")
        if _casefold(row["department"]) == _casefold(department)
        and int(row["semester"]) == int(semester)
        and (not section or _casefold(row["section"]) == _casefold(section))
        and (not week_day or _casefold(row["day_of_week"]) == _casefold(week_day))
    ]

    if not slots:
        return f"No timetable found for {department}, semester {semester}."

    day_order = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    slots.sort(key=lambda row: (day_order.index(_casefold(row["day_of_week"])), row["start_time"]))

    header = f"Department: {department} | Semester: {semester}"
    if section:
        header += f" | Section: {section}"

    lines = ["Class Timetable", header, ""]
    current_day = None
    for slot in slots:
        if slot["day_of_week"] != current_day:
            current_day = slot["day_of_week"]
            lines.append(f"**{current_day}**")
        lines.append(
            f"  {slot['start_time']} - {slot['end_time']}: {slot['subject_name']} ({slot['subject_code']})"
        )
        lines.append(
            f"     {slot['faculty_name']} |  {slot['room_number']} | Type: {slot['class_type']}"
        )
        lines.append("")

    return "\n".join(lines).strip()


def get_faculty_info(
    faculty_name: Optional[str] = None,
    department: Optional[str] = None,
    faculty_id: Optional[str] = None,
) -> str:
    """Return basic faculty info using name, department, or ID filters."""
    staff = load_rows("faculty")
    results = [
        row
        for row in staff
        if (
            (faculty_id and _casefold(row["faculty_id"]) == _casefold(faculty_id))
            or (faculty_name and _casefold(faculty_name) in _casefold(row["name"]))
            or (department and _casefold(row["department"]) == _casefold(department))
        )
    ]

    if not results:
        return "No faculty found matching your search criteria."

    lines = ["Faculty Information", ""]
    for fac in results:
        lines.append(f"{fac['name']}")
        lines.append(f" Faculty ID: {fac['faculty_id']}")
        lines.append(f" Department: {fac['department']}")
        lines.append(f" Designation: {fac['designation']}")
        if fac.get("specialization"):
            lines.append(f" Specialization: {fac['specialization']}\n   Email: {fac['email']}")
        if fac.get("phone"):
            lines.append(f" Phone: {fac['phone']}")
        if fac.get("office_location"):
            lines.append(f" Office: {fac['office_location']}")
        if fac.get("office_hours"):
            lines.append(f" Office Hours: {fac['office_hours']}")
        if fac.get("research_interests"):
            lines.append(f" Research Interests: {fac['research_interests']}")
        lines.append("")

    return "\n".join(lines).strip()


def get_academic_calendar(
    event_type: Optional[str] = None,
    days_ahead: int = 30,
    include_past: bool = False,
) -> str:
    """List upcoming events for the next few weeks."""
    today = date.today()
    cutoff = today + timedelta(days=days_ahead)

    events = [
        row
        for row in load_rows("academic_calendar")
        if (
            (include_past or _parse_date(row["event_date"]) >= today)
            and _parse_date(row["event_date"]) <= cutoff
            and (not event_type or _casefold(row["event_type"]) == _casefold(event_type))
        )
    ]

    if not events:
        filter_text = f" of type '{event_type}'" if event_type else ""
        return f"No events{filter_text} found in the next {days_ahead} days."

    events.sort(key=lambda row: _parse_date(row["event_date"]))
    lines = [f" Academic Calendar – Next {days_ahead} Days", ""]

    for event in events:
        event_date = _parse_date(event["event_date"])
        delta = (event_date - today).days
        if delta < 0:
            time_text = f"{abs(delta)} days ago"
        elif delta == 0:
            time_text = "TODAY"
        elif delta == 1:
            time_text = "TOMORROW"
        else:
            time_text = f"in {delta} days"

        lines.append(f" {event['event_name']} ({time_text})")
        if event.get("end_date"):
            lines.append(f" {event['event_date']} - {event['end_date']}")
        else:
            lines.append(f" {event['event_date']}")
        lines.append(f" Type: {event['event_type']}")
        if event.get("description"):
            lines.append(f" {event['description']}")
        if event.get("applicable_to"):
            lines.append(f" Applicable to: {event['applicable_to']}")
        if event.get("is_holiday", "").lower() == "true":
            lines.append("Holiday")
        lines.append("")

    return "\n".join(lines).strip()


def check_student_results(
    student_id: str,
    semester: Optional[int] = None,
    academic_year: Optional[str] = None,
) -> str:
    """Summarize marks and SGPA for a student."""
    students_map = load_map("students", "student_id")
    if student_id not in students_map:
        return f"Student {student_id} not found in the system."

    results = [
        row
        for row in load_rows("student_results")
        if row["student_id"] == student_id
        and (semester is None or int(row["semester"]) == int(semester))
        and (academic_year is None or row["academic_year"] == academic_year)
    ]

    if not results:
        return f"No results found for student {student_id}."

    results.sort(key=lambda row: (int(row["semester"]), row["subject_code"]))
    student = students_map[student_id]
    lines = [
        " **Student Results**",
        f"Student: {student['name']} ({student_id})",
        f"Department: {student['department']}",
        "",
    ]

    current_sem = None
    sem_total = sem_obtained = sem_credits = sem_grade_points = 0.0
    for res in results:
        res_sem = int(res["semester"])
        if current_sem != res_sem:
            if current_sem is not None and sem_total > 0:
                percentage = (sem_obtained / sem_total) * 100
                sgpa = (sem_grade_points / sem_credits) if sem_credits else 0
                lines.append("Semester Summary:")
                lines.append(f"  Total: {sem_obtained:.1f}/{sem_total} ({percentage:.2f}%)")
                lines.append(f"  SGPA: {sgpa:.2f}")
                lines.append("")
            current_sem = res_sem
            sem_total = sem_obtained = sem_credits = sem_grade_points = 0.0
            lines.append(f"Semester {res_sem} – {res['academic_year']}")
        lines.append(f" {res['subject_name']} ({res['subject_code']})")
        lines.append(
            f" Marks: {res['marks_obtained']}/{res['total_marks']} | Grade: {res['grade']} | Status: {res['result_status']}"
        )
        sem_obtained += float(res["marks_obtained"])
        sem_total += float(res["total_marks"])
        if res.get("credits"):
            credit_val = float(res["credits"])
            sem_credits += credit_val
            if res.get("grade_points"):
                sem_grade_points += float(res["grade_points"]) * credit_val

    if sem_total > 0:
        percentage = (sem_obtained / sem_total) * 100
        sgpa = (sem_grade_points / sem_credits) if sem_credits else 0
        lines.append("Semester Summary:")
        lines.append(f" Total: {sem_obtained:.1f}/{sem_total} ({percentage:.2f}%)")
        lines.append(f" SGPA: {sgpa:.2f}")

    return "\n".join(lines).strip()


def get_all_tools() -> List:
    """Return the full list of callable tools."""
    return [
        query_exam_schedule,
        fetch_previous_papers,
        get_class_timetable,
        get_faculty_info,
        get_academic_calendar,
        check_student_results,
    ]


__all__ = [
    "query_exam_schedule",
    "fetch_previous_papers",
    "get_class_timetable",
    "get_faculty_info",
    "get_academic_calendar",
    "check_student_results",
    "get_all_tools",
]
