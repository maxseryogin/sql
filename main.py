import sqlite3

connect = sqlite3.connect("univer.db")
cursor = connect.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               age INTEGER NOT NULL,
               major TEXT NOT NULL
)
    ''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS courses(
               course_id INTEGER PRIMARY KEY AUTOINCREMENT,
               course_name TEXT NOT NULL,
               instructor NOT NULL
)
    ''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS student_courses(
               student_id INTEGER,
               course_id INTEGER,
               FOREIGN KEY(student_id) REFERENCES students(id),
               FOREIGN KEY(course_id) REFERENCES course(id)
)
    ''')