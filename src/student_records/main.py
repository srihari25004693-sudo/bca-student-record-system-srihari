# Student Record System - BCA 2nd Year Mini Project
import sqlite3

con = sqlite3.connect("students.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS students (
    roll_no TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    course TEXT NOT NULL,
    marks INTEGER
)""")
con.commit()


def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    course = input("Enter course: ")
    marks = input("Enter marks: ")
    try:
        cur.execute("INSERT INTO students VALUES (?, ?, ?, ?)",
                    (roll, name, course, marks))
        con.commit()
        print("Student added.")
    except sqlite3.IntegrityError:
        print("Roll number already exists.")


def view_students():
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No records found.")


def search_student():
    roll = input("Enter roll number: ")
    cur.execute("SELECT * FROM students WHERE roll_no=?", (roll,))
    row = cur.fetchone()
    print(row if row else "Student not found.")


def update_student():
    roll = input("Enter roll number: ")
    cur.execute("SELECT * FROM students WHERE roll_no=?", (roll,))
    if cur.fetchone():
        name = input("Enter new name: ")
        course = input("Enter new course: ")
        marks = input("Enter new marks: ")
        cur.execute("UPDATE students SET name=?, course=?, marks=? WHERE roll_no=?",
                    (name, course, marks, roll))
        con.commit()
        print("Record updated.")
    else:
        print("Student not found.")


def delete_student():
    roll = input("Enter roll number: ")
    cur.execute("DELETE FROM students WHERE roll_no=?", (roll,))
    con.commit()
    print("Record deleted." if cur.rowcount else "Student not found.")


while True:
    print("\n--- STUDENT RECORD SYSTEM ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        break
    else:
        print("Invalid choice.")

con.close()
