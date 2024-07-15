class Student:
    def __init__(self):
        self.students = []

    def addstudent(self, rollno, name, age, gender):
        student = {"rollno": rollno, "name": name, "age": age, "gender": gender}
        self.students.append(student)

    def displaystudent(self):
        print("Student Records:")
        for student in self.students:
            print(f"Roll No: {student['rollno']}, Name: {student['name']}, Age: {student['age']}, Gender: {student['gender']}")

# Create an instance of the Student class
student_records = Student()

# Add some students
student_records.addstudent(1, "Alice", 18, "Female")
student_records.addstudent(2, "Bob", 19, "Male")
student_records.addstudent(3, "Charlie", 20, "Non-binary")

# Display all student records
student_records.displaystudent()
