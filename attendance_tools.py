
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "students.json"


def load_data():
    """Load student records from the JSON file."""
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_data(data):
    """Save updated student records to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def calculate_attendance(student):
    """Calculate attendance totals and percentage."""
    records = student["attendance"]

    total_days = sum(
        status in ("Present", "Absent")
        for status in records.values()
    )
    present_days = sum(
        status == "Present"
        for status in records.values()
    )

    percentage = (
        round((present_days / total_days) * 100, 2)
        if total_days > 0 else 0
    )

    return {
        "name": student["name"],
        "roll_no": student["roll_no"],
        "total_days": total_days,
        "present_days": present_days,
        "absent_days": total_days - present_days,
        "attendance_percentage": percentage
    }


def get_student(roll_no):
    """Find a student using their roll number."""
    data = load_data()

    for student in data["students"]:
        if str(student["roll_no"]) == str(roll_no):
            return calculate_attendance(student)

    return {"error": f"Student with roll number {roll_no} not found."}


def get_class_average():
    """Calculate the average attendance percentage."""
    data = load_data()

    if not data["students"]:
        return {"class_average_percentage": 0}

    percentages = [
        calculate_attendance(student)["attendance_percentage"]
        for student in data["students"]
    ]

    return {
        "class_average_percentage": round(
            sum(percentages) / len(percentages), 2
        )
    }


def update_attendance(roll_no, day, status):
    """Update a student's attendance for a particular day."""
    if status not in ("Present", "Absent", "Unrecorded"):
        return {"error": "Status must be Present, Absent, or Unrecorded."}

    data = load_data()

    for student in data["students"]:
        if str(student["roll_no"]) == str(roll_no):
            if day not in student["attendance"]:
                return {"error": f"{day} does not exist in the attendance records."}

            if status == "Unrecorded":
                del student["attendance"][day]
            else:
                student["attendance"][day] = status

            save_data(data)

            return {
                "message": f"Attendance updated for {student['name']}.",
                "attendance": calculate_attendance(student)
            }

    return {"error": f"Student with roll number {roll_no} not found."}


def get_all_attendance():
    """Return attendance summaries for all students."""
    data = load_data()

    return {
        "students": [
            calculate_attendance(student)
            for student in data["students"]
        ],
        "class_average": get_class_average()
    }
