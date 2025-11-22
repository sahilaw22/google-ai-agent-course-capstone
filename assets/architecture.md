# Academate Architecture Notes

![Architecture Diagram](graph_image.png)

## Flow At A Glance

```
Student question
       ↓
Academate agent (Gemini 2.5 Flash Lite)
       │
       ├─> Session Memory (remembers conversation context)
       │
       └─> Observability (logs the turn to logs/agent.log)
       ↓
Tool picker
       ↓
┌─────────────┬─────────────┬─────────────┐
│ Exam tool   │ Timetable   │ Faculty     │
│ Papers      │ Calendar    │ Results     │
└─────────────┴─────────────┴─────────────┘
       ↓
CSV datasets (students, exams, timetable, faculty)
       ↓
Clean response back to the user
```

The agent reads the question, checks its memory, logs the request, grabs the needed tool, loads the right CSV rows, and formats a short answer.

An offline **Evaluation Harness** (`chatbot/evaluation.py`) also runs checks against this flow to ensure the tools return predictable answers.

## Tool Reference

1. **Query exam schedule** – needs department, semester, and optional academic year. Sends back dates, rooms, and exam type.
2. **Fetch previous papers** – needs subject code plus optional year count or paper type. Returns file links if present.
3. **Get class timetable** – works with student ID or department + semester (+ section). Lists day-wise slots.
4. **Get faculty info** – filters by name, department, or faculty ID. Shows contact, office hours, and focus areas.
5. **Get academic calendar** – shows events within the next N days, filtered by type if needed.
6. **Check student results** – pulls marks, grades, and SGPA summary for a student, with optional semester filter.

## Dataset Columns (Short Form)

```
students        -> student_id, name, contact, dept, semester, section
exam_schedule   -> subject info, department, semester, exam slot details
timetable       -> department, semester, section, day, time slots
faculty         -> faculty_id, contact, office info, specialization
academic_calendar -> event name, type, date range, description
previous_papers -> subject_code, year, type, file pointers
student_results -> marks, grades, credits per subject
```

## Stack Recap

- Model: Gemini 2.5 Flash Lite
- Framework: Google ADK 1.18.0
- Data: CSV files in `data/`
- Language: Python 3.9+
- Extras: google-genai, python-dotenv

That’s the whole setup. Simple pipeline, shared CSV bundle, six tools.
                       │
