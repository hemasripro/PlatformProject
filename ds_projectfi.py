import re
from collections import defaultdict

class Student:
    def __init__(self, name, age, email, course):
        self.name = name
        self.age = age
        self.email = email
        self.course = course
        self.attendance = []  # List of attendance records
        self.grades = []  # List of grades
        self.assignments_completed = 0  # Track completed assignments

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Email: {self.email}, Course: {self.course}, Attendance: {self.attendance}, Grades: {self.grades}, Completed Assignments: {self.assignments_completed}"

class StudentRegistrationSystem:
    def __init__(self):
        self.students = []

    def register_student(self, name, age, email, course):
        if not self.is_valid_email(email):
            print("Email not valid. Please enter a valid email.")
            return
        if not self.is_valid_age(age):
            print("Age not valid. Please enter a valid age.")
            return
        new_student = Student(name, age, email, course)
        self.students.append(new_student)
        print(f"Student {name} registered successfully.")

    def is_valid_email(self, email):
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(regex, email) is not None

    def is_valid_age(self, age):
        return age.isdigit() and 0 < int(age) < 120

    def view_students(self):
        if not self.students:
            print("No students registered yet.")
            return
        print("\nRegistered Students:")
        for student in self.students:
            print(student)

    def search_student(self, name):
        found_students = [student for student in self.students if name.lower() in student.name.lower()]
        if found_students:
            print("\nSearch Results:")
            for student in found_students:
                print(student)
        else:
            print(f"No student found with the name '{name}'.")

    def delete_student(self, name):
        original_count = len(self.students)
        self.students = [student for student in self.students if student.name.lower() != name.lower()]
        if len(self.students) < original_count:
            print(f"Student {name} deleted successfully.")
        else:
            print(f"No student found with the name '{name}' to delete.")

    def update_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                new_name = input("Enter new name (leave blank to keep current): ")
                new_age = input("Enter new age (leave blank to keep current): ")
                new_email = input("Enter new email (leave blank to keep current): ")
                new_course = input("Enter new course (leave blank to keep current): ")
                
                if new_name:
                    student.name = new_name
                if new_age and self.is_valid_age(new_age):
                    student.age = new_age
                if new_email and self.is_valid_email(new_email):
                    student.email = new_email
                if new_course:
                    student.course = new_course
                
                print(f"Student {name} updated successfully.")
                return
        print(f"No student found with the name '{name}'.")

    def count_students_in_course(self, course):
        enrolled_students = [student for student in self.students if student.course.lower() == course.lower()]
        return len(enrolled_students)

    def record_attendance(self, name, attended):
        for student in self.students:
            if student.name.lower() == name.lower():
                student.attendance.append(attended)
                print(f"Attendance for {name} recorded as {'Present' if attended else 'Absent'}.")
                return
        print(f"No student found with the name '{name}'.")

    def record_grade(self, name, grade):
        for student in self.students:
            if student.name.lower() == name.lower():
                student.grades.append(grade)
                print(f"Grade {grade} recorded for {name}.")
                return
        print(f"No student found with the name '{name}'.")

    def complete_assignment(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                student.assignments_completed += 1
                print(f"Assignment completed for {name}. Total completed: {student.assignments_completed}.")
                return
        print(f"No student found with the name '{name}'.")

def main():
    system = StudentRegistrationSystem()
    while True:
        print("\n--- Student Registration System ---")
        print("1. Register Student")
        print("2. View Registered Students")
        print("3. Search for Student")
        print("4. Delete Student")
        print("5. Update Student Information")
        print("6. Count Students in a Course")
        print("7. Record Attendance")
        print("8. Record Grade")
        print("9. Mark Assignment as Completed")
        print("10. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            email = input("Enter student email: ")
            course = input("Enter the course: ")
            system.register_student(name, age, email, course)
        elif choice == "2":
            system.view_students()
        elif choice == "3":
            name = input("Enter the name of the student to search: ")
            system.search_student(name)
        elif choice == "4":
            name = input("Enter the name of the student to delete: ")
            system.delete_student(name)
        elif choice == "5":
            name = input("Enter the name of the student to update: ")
            system.update_student(name)
        elif choice == "6":
            course = input("Enter the course name to count enrolled students: ")
            count = system.count_students_in_course(course)
            print(f"Number of students enrolled in '{course}': {count}")
        elif choice == "7":
            name = input("Enter the name of the student to record attendance (1 for present, 0 for absent): ")
            attended = input("Enter 1 for present or 0 for absent: ")
            system.record_attendance(name, attended == '1')
        elif choice == "8":
            name = input("Enter the name of the student to record a grade: ")
            grade = input("Enter the grade: ")
            system.record_grade(name, grade)
        elif choice == "9":
            name = input("Enter the name of the student to mark assignment as completed: ")
            system.complete_assignment(name)
        elif choice == "10":
            print("Exiting the system.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
