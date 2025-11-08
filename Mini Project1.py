import sqlite3

# Connect to database
conn = sqlite3.connect("grading_system.db")
c = conn.cursor()

#----  Create tables  ----

c.execute("""
CREATE TABLE IF NOT EXISTS STUDENT (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
);
""")

c.execute("""
CREATE TABLE IF NOT EXISTS COURSE (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL
);
""")

c.execute("""
CREATE TABLE IF NOT EXISTS GRADE (
    grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    course_id INTEGER,
    grade TEXT,
    FOREIGN KEY (student_id) REFERENCES STUDENT(student_id),
    FOREIGN KEY (course_id) REFERENCES COURSE(course_id)
);
""")
conn.commit()

#----  CREATE FUNCTIONS  ----

def add_student(name, age):
    c.execute("INSERT INTO STUDENT (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    print(" Student added successfully!")

def add_course(course_name):
    c.execute("INSERT INTO COURSE (course_name) VALUES (?)", (course_name,))
    conn.commit()
    print(" Course added successfully!")

def add_grade(student_id, course_id, grade):
    c.execute("INSERT INTO GRADE (student_id, course_id, grade) VALUES (?, ?, ?)",
              (student_id, course_id, grade))
    conn.commit()
    print(" Grade added successfully!")

#----  READ FUNCTIONS  ----

def view_students():
    print("\n Students:")
    for row in c.execute("SELECT * FROM STUDENT"):
        print(row)

def view_courses():
    print("\n Courses:")
    for row in c.execute("SELECT * FROM COURSE"):
        print(row)

def view_grades():
    print("\n Grades:")
    for row in c.execute("""
        SELECT STUDENT.student_id, STUDENT.name, COURSE.course_name, GRADE.grade
        FROM GRADE
        JOIN STUDENT ON GRADE.student_id = STUDENT.student_id
        JOIN COURSE ON GRADE.course_id = COURSE.course_id;
    """):
        print(row)

#----  UPDATE FUNCTIONS  ----

def update_student(student_id, new_name, new_age):
    c.execute("UPDATE STUDENT SET name = ?, age = ? WHERE student_id = ?",
              (new_name, new_age, student_id))
    conn.commit()
    print(" Student updated successfully!")

def update_course(course_id, new_name):
    c.execute("UPDATE COURSE SET course_name = ? WHERE course_id = ?",
              (new_name, course_id))
    conn.commit()
    print(" Course updated successfully!")

def update_grade(grade_id, new_grade):
    c.execute("UPDATE GRADE SET grade = ? WHERE grade_id = ?",
              (new_grade, grade_id))
    conn.commit()
    print(" Grade updated successfully!")

#----  DELETE FUNCTIONS ----

def delete_student(student_id):
    c.execute("DELETE FROM STUDENT WHERE student_id = ?", (student_id,))
    conn.commit()
    print(" Student deleted!")

def delete_course(course_id):
    c.execute("DELETE FROM COURSE WHERE course_id = ?", (course_id,))
    conn.commit()
    print(" Course deleted!")

def delete_grade(grade_id):
    c.execute("DELETE FROM GRADE WHERE grade_id = ?", (grade_id,))
    conn.commit()
    print(" Grade deleted!")

#----  MENU SYSTEM  ----

while True:
    print("\n STUDENT GRADING SYSTEM")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Add Course")
    print("6. View Courses")
    print("7. Update Course")
    print("8. Delete Course")
    print("9. Add Grade")
    print("10. View Grades")
    print("11. Update Grade")
    print("12. Delete Grade")
    print("13. Exit")

    choice = input("Enter choice: ")

    try:
        if choice == "1":
            name = input("Enter student name: ")
            age = int(input("Enter age: "))
            add_student(name, age)

        elif choice == "2":
            view_students()

        elif choice == "3":
            student_id = int(input("Enter student ID to update: "))
            new_name = input("Enter new name: ")
            new_age = int(input("Enter new age: "))
            update_student(student_id, new_name, new_age)

        elif choice == "4":
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)

        elif choice == "5":
            course_name = input("Enter course name: ")
            add_course(course_name)

        elif choice == "6":
            view_courses()

        elif choice == "7":
            course_id = int(input("Enter course ID to update: "))
            new_name = input("Enter new course name: ")
            update_course(course_id, new_name)

        elif choice == "8":
            course_id = int(input("Enter course ID to delete: "))
            delete_course(course_id)

        elif choice == "9":
            student_id = int(input("Enter student ID: "))
            course_id = int(input("Enter course ID: "))
            grade = input("Enter grade (A/B/C...): ").upper()
            add_grade(student_id, course_id, grade)

        elif choice == "10":
            view_grades()

        elif choice == "11":
            grade_id = int(input("Enter grade ID to update: "))
            new_grade = input("Enter new grade: ").upper()
            update_grade(grade_id, new_grade)

        elif choice == "12":
            grade_id = int(input("Enter grade ID to delete: "))
            delete_grade(grade_id)

        elif choice == "13":
            print(" Exiting..")
            break

        else:
            print(" Invalid choice. Try again.")

    except Exception as e:
        print(" Error:", e)

conn.close()