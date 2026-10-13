
from attendance_tools import get_all_attendance, get_student

print("===== ALL STUDENTS =====")
print(get_all_attendance())

print("\n===== STUDENT WITH ROLL NO. 101 =====")
print(get_student("101"))
