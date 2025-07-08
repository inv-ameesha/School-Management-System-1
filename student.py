import json
import os
from datetime import datetime
from utils import (
    validate_name,
    validate_age,
    validate_email,
    validate_phone,
    get_course
)

students_file = 'data/students.json'
CURRENT_YEAR = datetime.now().year

def load_students():
    if not os.path.exists(students_file):
        return []
    with open(students_file, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_students(student_list):
    with open(students_file, "w") as file:
        json.dump(student_list, file, indent=4)

def get_regno(student_list):
    l = len(student_list) + 1
    return f"REG-{CURRENT_YEAR}-{l:04d}"

def register_student():
    student_list = load_students()

    print("\nRegister new Student")
    name = input("Enter name : ")
    if not validate_name(name):
        print("Invalid name")
        return

    age = input("Enter age : ")
    if not validate_age(age):
        print("Invalid age")
        return

    email = input("Enter email : ")
    if not validate_email(email):
        print("Invalid email")
        return

    phone = input("Enter phone : ")
    if not validate_phone(phone):
        print("Invalid phone")
        return

    course = get_course()
    if not course:
        print("Invalid course")
        return

    regno = get_regno(student_list)

    new_student = {
        'name': name,
        'reg_no': regno,
        'age': int(age),
        'email': email,
        'phone': phone,
        'course': course
    }

    student_list.append(new_student)
    save_students(student_list)
    print(f"Student registered successfully! Reg No: {regno}")

def get_students():
    student_list = load_students()
    print("\nSTUDENTS LIST")
    if not student_list:
        print("No students yet")
        return

    for s in student_list:
        print(f"{s['reg_no']} | {s['name']} | Age: {s['age']} | Email: {s['email']} | Phone: {s['phone']} | Course: {s['course']}")
