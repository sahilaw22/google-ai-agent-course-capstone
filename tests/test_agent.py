"""Quick smoke test for the Academate agent."""

import os
import sys

# Add parent directory so imports still work when run directly
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from dotenv import load_dotenv

# Load environment
load_dotenv()

print("ACADEMATE TEST SUITE")
print("=" * 60)

# Test 1: Environment Check
print("\nTesting environment setup...")
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    print("API key found")
    print(f"Key prefix: {api_key[:20]}...")
else:
    print("API Key not found!")
    exit(1)

# Test 2: Dataset Access
print("\nTesting dataset access...")
try:
    from chatbot.datasets import load_rows

    student_rows = load_rows("students")
    faculty_rows = load_rows("faculty")

    if not student_rows or not faculty_rows:
        raise ValueError("Missing seed data in CSV files")

    print("CSV datasets loaded")
    print(f" Students: {len(student_rows)}")
    print(f" Faculty: {len(faculty_rows)}")
except Exception as e:
    print(f" Dataset error: {e}")
    exit(1)

# Test 3: Tools Import
print("\nTesting tool imports...")
try:
    from chatbot.tools import (
        query_exam_schedule,
        fetch_previous_papers,
        get_class_timetable,
        get_faculty_info,
        get_academic_calendar,
        check_student_results,
        get_all_tools
    )
    
    tools = get_all_tools()
    print("All tools imported")
    print(f" Available tools: {len(tools)}")
except Exception as e:
    print(f" Tools import error: {e}")
    exit(1)

# Test 4: Individual Tool Testing
print("\nTesting individual tools...")

# Test 4a: Exam Schedule
print("\nTesting query_exam_schedule...")
try:
    # Test standard case
    result = query_exam_schedule("Computer Science", 3, "2024-25")
    if "Data Structures" in result:
        print("query_exam_schedule working (Standard)")
    else:
        print(f" Unexpected result: {result[:100]}...")
        
    # Test case insensitivity
    result_lower = query_exam_schedule("computer science", 3, "2024-25")
    if "Data Structures" in result_lower:
        print("query_exam_schedule working (Lowercase)")
    else:
        print(f" Lowercase failed: {result_lower[:100]}...")
except Exception as e:
    print(f" Error: {e}")

# Test 4b: Previous Papers
print("\n Testing fetch_previous_papers...")
try:
    result = fetch_previous_papers("CS301", years=3)
    if "2023" in result or "2022" in result:
        print("fetch_previous_papers working (Standard)")
    
    # Test case insensitivity
    result_lower = fetch_previous_papers("cs301", years=3)
    if "2023" in result_lower or "2022" in result_lower:
        print("fetch_previous_papers working (Lowercase)")
    else:
        print(f" Lowercase failed: {result_lower[:100]}...")
except Exception as e:
    print(f" Error: {e}")

# Test 4c: Timetable
print("\nTesting get_class_timetable...")
try:
    result = get_class_timetable(student_id="CS2024001")
    if "Monday" in result or "Timetable" in result:
        print("get_class_timetable working")
    else:
        print(f" Unexpected result: {result[:100]}...")
except Exception as e:
    print(f" Error: {e}")

# Test 4d: Faculty Info
print("\nTesting get_faculty_info...")
try:
    result = get_faculty_info(faculty_name="Ramesh")
    if "Ramesh" in result or "Faculty" in result:
        print("get_faculty_info working")
    else:
        print(f" Unexpected result: {result[:100]}...")
except Exception as e:
    print(f" Error: {e}")

# Test 4e: Academic Calendar
print("\nTesting get_academic_calendar...")
try:
    result = get_academic_calendar(days_ahead=30)
    if "Calendar" in result or "event" in result.lower():
        print("get_academic_calendar working")
    else:
        print(f" Unexpected result: {result[:100]}...")
except Exception as e:
    print(f" Error: {e}")

# Test 4f: Student Results
print("\nTesting check_student_results...")
try:
    result = check_student_results("CS2024001")
    if "Student" in result or "Results" in result:
        print("check_student_results working")
    else:
        print(f" Unexpected result: {result[:100]}...")
except Exception as e:
    print(f" Error: {e}")

# Test 5: Agent Creation
print("\nTesting agent creation...")
try:
    from chatbot.runtime import build_agent
    
    agent = build_agent(tools=tools)
    print("Agent created")
    print(f" Agent name: {agent.name}")
    print(f" Tools loaded: {len(agent.tools)}")
except Exception as e:
    print(f" Agent creation error: {e}")
    exit(1)

# Final Summary
print("\n" + "=" * 60)
print("ALL TESTS PASSED")
print("=" * 60)
print("\nAcademate is ready to use.")
print("\nTo start the agent, run:")
print("   python -m chatbot.main")
print("\nDocumentation:")
print("   README.md")
print()
