from student import Student
from grading import calculate_grade

def main():
    students = [
        Student(101, "Ali", 88),
        Student(102, "Sara", 95),
        Student(103, "Ahmed", 72),
        Student(104, "Fatima", 65),
        Student(105, "Hassan", 58),
        Student(106, "Ayesha", 81),
        Student(107, "Bilal", 91),
        Student(108, "Zain", 77)
    ]

    print("=" * 55)
    print("          Student Result Management System")
    print("=" * 55)
    print(f"{'ID':<6}{'Name':<12}{'Marks':<10}{'Grade'}")
    print("-" * 55)

    for student in students:
        grade = calculate_grade(student.marks)
        print(f"{student.student_id:<6}{student.name:<12}{student.marks:<10}{grade}")

    print("=" * 55)

if __name__ == "__main__":
    main()