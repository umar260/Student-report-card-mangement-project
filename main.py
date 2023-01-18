import re
import json
import os

class Student:
    def __init__(self, name, classofs, dob, fees):
        self.name = name
        self.class_ = classofs
        self.dob = dob
        self.fees = fees
        self.grades = {}



studentslist = []

def loadfromjson():
    try:
        with open("students.json", "r") as f:
            data = json.load(f)
            for student_data in data:
                student = Student(student_data['name'], student_data['classofs'], 
                                  student_data['dob'], student_data['fees'])
                student.grades = student_data['grades']
                studentslist.append(student)
    except Exception as e:
        print("Getting Error in loading json file: ",e)

loadfromjson()        

def savetojson():
    try:
        with open("students.json", "w") as f:
            json.dump([student.__dict__ for student in studentslist], f)
    except Exception as e:
        print("Getting Error in saving the json file: ",e)

                

def addstudents(name, classofs, dob, fees):
    student = Student(name, classofs, dob, fees)
    studentslist.append(student)


def removestudents(name):
    for i, student in enumerate(studentslist):
        if student.name == name:
            del studentslist[i]
            print("Student is removed successfully!")
            return
    print("Student not found.")

def editstudents(name, newname=None, newclass=None, newdob=None, newfees=None):
    for student in studentslist:
        if student.name == name:
            if newname:
                student.name = newname
            if newclass:
                student.classofs = newclass
            if newdob:
                student.dob = newdob
            if newfees:
                student.fees = newfees
            print("Student details are updated successfully!")
            return
    print("Student not found.")

def viewstudents():
    if not studentslist:
        print("No students found.")
        return
    for student in studentslist:
        print("Name:", student.name)
        print("Class:", student.classofs)
        print("Date of Birth:", student.dob)
        print("Fees:", student.fees)
        print("-------------")    

def isvalidname(name):
    if re.match("^[a-zA-Z\s]*$", name):
        return True
    return False

def isvalidclass(classofs):
    if re.match("^[0-9a-zA-Z\s]*$", classofs):
        return True
    return False

def isvaliddob(dob):
    if re.match("^[0-9]{2}/[0-9]{2}/[0-9]{4}$", dob):
        return True
    return False

def isvalidfees(fees):
    if re.match("^[0-9]*$", fees):
        return True
    return False  

def addgrades(name, subject, grade):
    for student in studentslist:
        if student.name == name:
            student.grades[subject] = grade
            print("Grades are added successfully!")
            return
    print("Could not found the student.")

def editgrades(name, subject, new_grade):
    for student in studentslist:
        if student.name == name:
            if subject in student.grades:
                student.grades[subject] = new_grade
                print("Grades are updated successfully!")
                return
            else:
                print(f"Subject {subject} not found for student {name}")
                return
    print("Could not found the student.")

def viewgrades(name):
    for student in studentslist:
        if student.name == name:
            if student.grades:
                for subject, grade in student.grades.items():
                    print(f"{subject}: {grade}")
            else:
                print(f"No grades found for student {name}")
            return
    print("Could not found the student.")                  


def menu():
    while True:
        print("1. Add a student")
        print("2. Remove a student")
        print("3. Edit student details")
        print("4. View a students")
        print("5. Add/Edit/View grades od the student")
        print("6. To Exit")
        selection = input("Enter your choice: ")

        if selection == "1":
            name = input("Enter the student name: ")
            classofs = input("Enter the class: ")
            dob = input("Enter the date of birth of the student(dd/mm/yyyy): ")
            fees = input("Enter the fees: ")
            addstudents(name, classofs, dob, fees)
            print("Student is added successfully!")

        elif selection == "2":
            name = input("Enter a student name: ")
            removestudents(name)

        elif selection == "3":
            name = input("Enter a student name: ")
            new_name = input("Enter a new name (Please Press Enter to skip): ")
            new_class = input("Enter a new class (Please Press Enter to skip): ")
            new_dob = input("Enter new date of birth of the student (PLease Press Enter to skip): ")
            new_fees = input("Enter the new fees (PLease Press Enter to skip): ")
            editstudents(name, new_name, new_class, new_dob, new_fees)

        elif selection == "4":
            viewstudents()

        elif selection == "5":
            print("1. To Add grades")
            print("2. To Edit grades")
            print("3. To View grades")
            gradechoice = input("Enter your choice: ")

            if gradechoice == "1":
                name = input("Enter the student name: ")
                subject = input("Enter the  subject: ")
                grade = input("Enter the grade: ")
                addgrades(name, subject, grade)

            elif gradechoice == "2":
                name = input("Enter the student name: ")
                subject = input("Enter the subject: ")
                new_grade = input("Enter the new grade: ")
                editgrades(name, subject, new_grade)

            elif gradechoice == "3":
                name = input("Enter a student name: ")
                viewgrades(name)
            else:
                print("Invalid choice. Can u Please try again.")

        elif selection == "6":
            savetojson()
            print("Exiting...")
            break 
        else:
            print("Invalid choice. Can u Please try again.")

menu()