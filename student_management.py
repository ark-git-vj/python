class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, grade):
        if student_id not in self.students:
            student = Student(student_id, name, age, grade)
            self.students[student_id] = student
            print(f"\nStudent {name} added successfully!")
        else:
            print("\nStudent ID already exists!")

    def view_student(self, student_id):
        student = self.students.get(student_id)
        if student:
            print(f"\nStudent Details:")
            print(f"ID: {student.student_id}")
            print(f"Name: {student.name}")
            print(f"Age: {student.age}")
            print(f"Grade: {student.grade}")
        else:
            print("\nStudent not found!")

    def view_all_students(self):
        if self.students:
            print("\nAll Students:")
            for student in self.students.values():
                print(f"\nID: {student.student_id}")
                print(f"Name: {student.name}")
                print(f"Age: {student.age}")
                print(f"Grade: {student.grade}")
        else:
            print("\nNo students in the system!")

    def update_student(self, student_id, name, age, grade):
        if student_id in self.students:
            student = self.students[student_id]
            student.name = name
            student.age = age
            student.grade = grade
            print("\nStudent information updated successfully!")
        else:
            print("\nStudent not found!")

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("\nStudent deleted successfully!")
        else:
            print("\nStudent not found!")

def main():
    sms = StudentManagementSystem()
    
    while True:
        print("\n=== Student Management System ===")
        print("1. Add Student")
        print("2. View Student")
        print("3. View All Students")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            grade = input("Enter student grade: ")
            sms.add_student(student_id, name, age, grade)
            
        elif choice == '2':
            student_id = input("Enter student ID: ")
            sms.view_student(student_id)
            
        elif choice == '3':
            sms.view_all_students()
            
        elif choice == '4':
            student_id = input("Enter student ID: ")
            name = input("Enter new name: ")
            age = input("Enter new age: ")
            grade = input("Enter new grade: ")
            sms.update_student(student_id, name, age, grade)
            
        elif choice == '5':
            student_id = input("Enter student ID: ")
            sms.delete_student(student_id)
            
        elif choice == '6':
            print("\nThank you for using Student Management System!")
            break
            
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()
