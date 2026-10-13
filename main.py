
from ai_attendance import interpret_instruction
from attendance_tools import (
    get_student,
    get_all_attendance,
    get_class_average,
    update_attendance
)


def execute_command(command):
    """Validate and execute an AI-generated attendance command."""

    if "error" in command:
        return command

    action = command.get("action")

    if action == "clarify":
        return {
            "message": command.get(
                "question",
                "Please provide more details."
            )
        }

    if action == "get_student":
        roll_no = command.get("roll_no")

        if not isinstance(roll_no, (str, int)) or not str(roll_no).strip():
            return {"error": "A valid roll number is required."}

        return get_student(roll_no)

    if action == "get_all_attendance":
        return get_all_attendance()

    if action == "get_class_average":
        return get_class_average()

    if action == "update_attendance":
        roll_no = command.get("roll_no")
        day = command.get("day")
        status = command.get("status")

        if not isinstance(roll_no, (str, int)) or not str(roll_no).strip():
            return {"error": "A valid roll number is required."}

        if not isinstance(day, str) or not day.strip():
            return {"error": "A valid day is required."}

        if status not in ("Present", "Absent", "Unrecorded"):
            return {"error": "Invalid attendance status."}

        return update_attendance(roll_no, day, status)

    return {"error": "Unsupported action. Please try another instruction."}


def main():
    print("====================================")
    print(" AI ATTENDANCE MANAGEMENT SYSTEM")
    print("====================================")
    print("Examples:")
    print("- What is the attendance of roll number 101?")
    print("- Show all students' attendance.")
    print("- Calculate the class average.")
    print("- Mark roll number 102 present on Day 3.")
    print("- Remove roll number 101's attendance for Day 2.")
    print("\nType 'exit' to close the program.")

    while True:
        user_instruction = input("\nEnter your instruction: ").strip()

        if user_instruction.lower() == "exit":
            print("Program closed.")
            break

        if not user_instruction:
            print("Please enter an instruction.")
            continue

        print("\nAI is interpreting your instruction...")

        command = interpret_instruction(user_instruction)
        result = execute_command(command)

        print("\nResult:")
        print(result)


if __name__ == "__main__":
    main()
