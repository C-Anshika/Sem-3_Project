a=print("Please enter your DESIGNATION: ")
if(a.toLowerCase().equals("student")):
    print("Welcome STUDENT")
elif(a.toLowerCase().equals("teacher")):
    print("Welcome TEACHER")
elif(a.toLowerCase().equals("admin")):
    print("Welcome ADMIN")
else:
    print("Invalid Input")

# Class for Student
class Student:
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Major: {self.major}"


# Class for Course
class Course:
    def __init__(self, course_id, course_name, instructor):
        self.course_id = course_id
        self.course_name = course_name
        self.instructor = instructor

    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.course_name}, Instructor: {self.instructor}"


# Class for Enrollment
class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course

    def __str__(self):
        return f"{self.student.name} is enrolled in {self.course.course_name}"


# Class for hod
class HeadOfDepartment:
    def __init__(self):
        self.students = []
        self.courses = []
        self.enrollments = []

    # Add student to system
    def add_student(self, student_id, name, age, major):
        student = Student(student_id, name, age, major)
        self.students.append(student)
        print(f"Student {name} added successfully.")

    # Add course to system
    def add_course(self, course_id, course_name, instructor):
        course = Course(course_id, course_name, instructor)
        self.courses.append(course)
        print(f"Course {course_name} added successfully.")

    # Enroll student in a course
    def enroll_student(self, student_id, course_id):
        student = next((s for s in self.students if s.student_id == student_id), None)
        course = next((c for c in self.courses if c.course_id == course_id), None)

        if student and course:
            enrollment = Enrollment(student, course)
            self.enrollments.append(enrollment)
            print(f"{student.name} has been enrolled in {course.course_name}")
        else:
            print("Invalid student ID or course ID")

    # View all students
    def view_students(self):
        if self.students:
            for student in self.students:
                print(student)
        else:
            print("No students in the system.")

    # View all courses
    def view_courses(self):
        if self.courses:
            for course in self.courses:
                print(course)
        else:
            print("No courses in the system.")

    # View all enrollments
    def view_enrollments(self):
        if self.enrollments:
            for enrollment in self.enrollments:
                print(enrollment)
        else:
            print("No enrollments yet.")


# Example usage:
Hod= HeadOfDepartment()

# Adding students
Hod.add_student(1, "Alice", 20, "Computer Science")
Hod.add_student(2, "Bob", 21, "Mechanical Engineering")

# Adding courses
Hod.add_course(101, "Data Structures", "Dr. Smith")
Hod.add_course(102, "Thermodynamics", "Dr. Johnson")

# Enrolling students in courses
Hod.enroll_student(1, 101)
Hod.enroll_student(2, 102)

# Viewing students, courses, and enrollments
print("\n--- Students ---")
Hod.view_students()

print("\n--- Courses ---")
Hod.view_courses()

print("\n--- Enrollments ---")
Hod.view_enrollments()
