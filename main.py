import re
import json
import os

class Student:
    def __init__(self, name, class_, dob, fees):
        self.name = name
        self.class_ = class_
        self.dob = dob
        self.fees = fees
        self.grades = {}



students_list = []

def load_from_json():
    try:
        with open("students.json", "r") as f:
            data = json.load(f)
            for student_data in data:
                student = Student(student_data['name'], student_data['class_'], 
                                  student_data['dob'], student_data['fees'])
                student.grades = student_data['grades']
                students_list.append(student)
    except Exception as e:
        print("Error in loading json file: ",e)

load_from_json()        

def save_to_json():
    try:
        with open("students.json", "w") as f:
            json.dump([student.__dict__ for student in students_list], f)
    except Exception as e:
        print("Error in saving json file: ",e)

                

def add_student(name, class_, dob, fees):
    student = Student(name, class_, dob, fees)
    students_list.append(student)


def remove_student(name):
    for i, student in enumerate(students_list):
        if student.name == name:
            del students_list[i]
            print("Student removed successfully!")
            return
    print("Student not found.")

def edit_student(name, new_name=None, new_class=None, new_dob=None, new_fees=None):
    for student in students_list:
        if student.name == name:
            if new_name:
                student.name = new_name
            if new_class:
                student.class_ = new_class
            if new_dob:
                student.dob = new_dob
            if new_fees:
                student.fees = new_fees
            print("Student details updated successfully!")
            return
    print("Student not found.")

def view_students():
    if not students_list:
        print("No students found.")
        return
    for student in students_list:
        print("Name:", student.name)
        print("Class:", student.class_)
        print("Date of Birth:", student.dob)
        print("Fees:", student.fees)
        print("-----------------------------")    

def is_valid_name(name):
    if re.match("^[a-zA-Z\s]*$", name):
        return True
    return False

def is_valid_class(class_):
    if re.match("^[0-9a-zA-Z\s]*$", class_):
        return True
    return False

def is_valid_dob(dob):
    if re.match("^[0-9]{2}/[0-9]{2}/[0-9]{4}$", dob):
        return True
    return False

def is_valid_fees(fees):
    if re.match("^[0-9]*$", fees):
        return True
    return False  

def add_grades(name, subject, grade):
    for student in students_list:
        if student.name == name:
            student.grades[subject] = grade
            print("Grades added successfully!")
            return
    print("Student not found.")

def edit_grades(name, subject, new_grade):
    for student in students_list:
        if student.name == name:
            if subject in student.grades:
                student.grades[subject] = new_grade
                print("Grades updated successfully!")
                return
            else:
                print(f"Subject {subject} not found for student {name}")
                return
    print("Student not found.")

def view_grades(name):
    for student in students_list:
        if student.name == name:
            if student.grades:
                for subject, grade in student.grades.items():
                    print(f"{subject}: {grade}")
            else:
                print(f"No grades found for student {name}")
            return
    print("Student not found.")                  




def menu():
    while True:
        print("1. Add student")
        print("2. Remove student")
        print("3. Edit student details")
        print("4. View students")
        print("5. Add/Edit/View grades")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            class_ = input("Enter class: ")
            dob = input("Enter date of birth (dd/mm/yyyy): ")
            fees = input("Enter fees: ")
            add_student(name, class_, dob, fees)
            print("Student added successfully!")

        elif choice == "2":
            name = input("Enter student name: ")
            remove_student(name)

        elif choice == "3":
            name = input("Enter student name: ")
            new_name = input("Enter new name (Press Enter to skip): ")
            new_class = input("Enter new class (Press Enter to skip): ")
            new_dob = input("Enter new date of birth (Press Enter to skip): ")
            new_fees = input("Enter new fees (Press Enter to skip): ")
            edit_student(name, new_name, new_class, new_dob, new_fees)

        elif choice == "4":
            view_students()

        elif choice == "5":
            print("1. Add grades")
            print("2. Edit grades")
            print("3. View grades")
            grade_choice = input("Enter your choice: ")

            if grade_choice == "1":
                name = input("Enter student name: ")
                subject = input("Enter subject: ")
                grade = input("Enter grade: ")
                add_grades(name, subject, grade)

            elif grade_choice == "2":
                name = input("Enter student name: ")
                subject = input("Enter subject: ")
                new_grade = input("Enter new grade: ")
                edit_grades(name, subject, new_grade)

            elif grade_choice == "3":
                name = input("Enter student name: ")
                view_grades(name)
            else:
                print("Invalid choice. Please try again.")
                
        elif choice == "6":
            save_to_json()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

menu()