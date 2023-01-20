import re
import json
import os

# student class defning student 
class Student:
    def __init__(self, name, grade, dateofbirth, fees):
        self.name = name # name of student
        self.grade = grade # grade of student 
        self.dateofbirth = dateofbirth # date of birth of student 
        self.fees = fees # fees of student
        self.grades = {} # grades for the student used dictinary

# list to storing the student data and 
studentlist = []

def jsondataload():
    try:
        with open("students.json", "r") as f:
            jsonfile = json.load(f)
            for eachstudent in jsonfile:
                student = Student(eachstudent['name'], eachstudent['grade'], 
                                  eachstudent['dateofbirth'], eachstudent['fees'])
                student.grades = eachstudent['grades'] 
                studentlist.append(student)# adding grades to the student
    except Exception as e:# giving exception
        print("Json file not opeing no jsonfile present: ",e)

jsondataload()        

def savejsondata():
    try:
        with open("students.json", "w") as f:
            json.dump([student.__dict__ for student in studentlist], f) # saving student data to json file
    except Exception as e:
        print("Error in saving json file: ",e)

                

def addstudent(name, grade, dateofbirth, fees):
    student = Student(name, grade, dateofbirth, fees)
    studentlist.append(student) # adding student to my list with append function

# removing student from my list
def removestudent(name):
    for i, student in enumerate(studentlist):
        if student.name == name:
            del studentlist[i]
            print("Student removed successfully!")
            return
    print("Student not found.")

# changing student details
def editstudentdetails(name, newname=None, newclass=None, dateofbirth=None, fees=None):
    for student in studentlist:
        if student.name == name:
            if newname:
                student.name = newname
            if newclass:
                student.grade = newclass
            if dateofbirth:
                student.dateofbirth = dateofbirth
            if fees:
                student.fees = fees

# view every student data
def viewstduents():
    if not studentlist:
        print("No students found.")
        return
    for student in studentlist:
        print("Name:", student.name)
        print("Class:", student.grade)
        print("Date of Birth:", student.dateofbirth)
        print("Fees:", student.fees)
        print("-----------------------------") 

# checking name
def validname(name):
    if re.match("^[a-zA-Z\s]*$", name):
        return True
    return False

# checking grade
def validclass(grade):
    if re.match("^[0-9a-zA-Z\s]*$", grade):
        return True
    return False


# checking date of birth
def validdateofbirth(dateofbirth):
    if re.match("^[0-9]{2}/[0-9]{2}/[0-9]{4}$", dateofbirth):
        return True
    return False

# checking fees
def validfees(fees):
    if re.match("^[0-9]*$", fees):
        return True
    return False  

# adding grade for a student
def addgrades(name, subject, grade):
    for student in studentlist:
        if student.name == name:
            student.grades[subject] = grade
            print("grade added in the student profile")
            return
    print("student not found")

# editing grade for a student
def editgrades(name, subject, new_grade):
    for student in studentlist:
        if student.name == name:
            if subject in student.grades:
                student.grades[subject] = new_grade
                print("grade added in the student profile")
                return
            else:
                print(f"Subject {subject} not found for student {name}")
                return
    print("student not found")

# viewing grade for a student
def viewgrades(name):
    for student in studentlist:
        if student.name == name:
            if student.grades:
                for subject, grade in student.grades.items():
                    print(f"{subject}: {grade}")
            else:
                print(f"No grades found for student {name}")
            return
    print("Student not found.")


def menu():# main menu of the program
    while True:
        print("1 add student in database")
        print("2 remove student in databse")
        print("3 edit student details")
        print("4 view every students")
        print("5 grades")
        print("6 exit")
        choice = input("enter your choice: ")

        if choice == "1":
            name = input("enter student name: ")
            if name == "":
                print("You cant left it empty")# checking if user left empty name
                continue
            grade = input("enter class: ")
            if grade == "":
                print("You cant left it empty")# checking if user left empty class
                continue
            dateofbirth = input("enter date of birth in the form of(dd/mm/yyyy): ")
            if dateofbirth == "":
                print("You cant left it empty")# checking if user left dob
                continue
            fees = input("enter fees: ")
            if fees == "":
                print("You cant left it empty")# checking if user left empty fees
                continue
            addstudent(name, grade, dateofbirth, fees)
            print("student added succesfully in the list")


        elif choice == "2":
            name = input("Enter student name: ")
            removestudent(name)

        elif choice == "3":
            name = input("Enter student name: ")
            newname = input("Enter new name of the student ")
            newclass = input("Enter new grade of the student ")
            dateofbirth = input("Enter new date of birth ")
            fees = input("Enter new fees of the student ")
            editstudentdetails(name, newname, newclass, dateofbirth, fees)
        elif choice == "4":
            viewstduents()
        elif choice == "5":
            print("1 add grades of student")
            print("2 edit grades of student")
            print("3 view grades of student")
            gradeselection = input("Enter your choice: ")
            if gradeselection == "1":
                name = input("Enter student name: ")
                subject = input("Enter subject: ")
                grade = input("Enter grade: ")
                addgrades(name, subject, grade)
            elif gradeselection == "2":
                name = input("Enter student name: ")
                subject = input("Enter subject: ")
                new_grade = input("Enter new grade: ")
                editgrades(name, subject, new_grade)
            elif gradeselection == "3":
                name = input("Enter student name: ")
                viewgrades(name)
            else:
                print("wrong input please enter a valid input")
        elif choice == "6":
            savejsondata()
            print("Exiting...")
            break
        else:
            print("wrong input please enter a valid input")

menu()