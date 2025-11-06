class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    def display_details(self):
        print("-" * 30)
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Grade: {self.grade}")
        print("-" * 30)


class School:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_number, grade):
        student = Student(name, roll_number, grade)
        self.students.append(student)
        print("Student added successfully!\n")

    def remove_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                print("Student removed successfully!\n")
                return
        print("Student not found!\n")

    def display_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                student.display_details()
                return
        print("Student not found!\n")

    def display_all_students(self):
        if not self.students:
            print("No students in the system.\n")
        else:
            print("All Students:")
            for student in self.students:
                student.display_details()


def main():
    school = School()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Display Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            roll = input("Enter roll number: ")
            grade = input("Enter grade: ")
            school.add_student(name, roll, grade)

        elif choice == "2":
            roll = input("Enter roll number to remove: ")
            school.remove_student(roll)

        elif choice == "3":
            roll = input("Enter roll number to display: ")
            school.display_student(roll)

        elif choice == "4":
            school.display_all_students()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
