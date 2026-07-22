from student import Student
from grading import calculate_grade

def main():
    student1 = Student(101, "Ali", 88)
    student2 = Student(102, "Sara", 95)
    student3 = Student(103, "Ahmed", 72)

    students = [student1, student2, student3]

    print("===== Student Result Management System =====\n")

    for student in students:
        student.display()
        grade = calculate_grade(student.marks)
        print(f"Grade: {grade}")
        print("-" * 30)

if __name__ == "__main__":
    main()