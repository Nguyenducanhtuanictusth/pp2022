from math import *


class Student:
    def __init__(self, ID="", Name="", DoB="", GPA=0):
        self.__ID = ID
        self.__Name = Name
        self.__DoB = DoB
        self.__GPA = GPA
    def getId(self):
        return self.__ID
    def getName(self):
        return self.__Name
    def getDob(self):
        return self.__DoB
    def getGPA(self):
        return self.__GPA
    def setGPA(self, GPA):
        self.__GPA = GPA
    def input(self):
        self.__ID = input("Student ID is : ")
        self.__Name = input("Student Name is: ")
        self.__DoB = input("Student DoB : ")

    def __str__(self):
        return "ID: " + self.__ID + " Student: " + self.__Name + " DOB: " + self.__DoB
    def describe(self):
        print(self.__str__())
class Mark:
    def __init__(self, Name, Course, Mark=0, GPA=0):
        self.__Name = Name
        self.__Course = Course
        self.__Mark = Mark
        self.__GPA = GPA

    def input(self):
        print(f"Enter Student's mark for {self.__Name}")
        self.__mark = float(input(f"in {self.__Course}: "))
    def getMark(self):
        return floor(self.__Mark * 10) / 10
    def getCourse(self):
        return self.__course
    def getGPA(self):
        return floor(self.__GPA * 10) / 10

    def setGPA(self, GPA):
        self.__GPA = GPA

    def getName(self):
        return self.__Name
    def __str__(self):
        return "Student " + self.getName() + " Mark: " + str(
            self.getMark()) + " in " + self.getCourse()

    def describe(self):
        print(self.__str__())


class Course:
    def __init__(self, id="", name=""):
        self.__id = id
        self.__name = name
    def getId(self):
        return self.__id
    def getName(self):
        return self.__name
    def input(self):
        self.__id = input("Course Id: ")
        self.__name = input("Course Name: ")
    def __str__(self):
        return "Course: " + self.__name + " with id of " + self.__id + " and credit of " + str(self.__etc)

    def describe(self):
        print(self.__str__())
ClassRoom = []
ListOfCourse = []
Marks = []
NumberStd = int(input("Enter number of Students: "))
for i in range(NumberStd):
    s = Student()
    s.input()
    ClassRoom += [s]
for student in ClassRoom:
    print(student)
NumberOfCourse = int(input("Enter number of Courses: "))
for i in range(NumberOfCourse):
    c = Course()
    c.input()
    ListOfCourse += [c]
for c in ListOfCourse:
    print(c)
def choseCourse():
    Course = input("Enter the course name: ")
    return Course
def inputMark(Course):
    for i in range(NumberOfCourse):
        if Course == ListOfCourse[i].getName():
            for j in range(NumberStd):
                m = Mark(ClassRoom[j].getName(), ListOfCourse[i].getName(), ListOfCourse[i].getCredit())
                m.input()
                Marks.append(m)
def printMark(Course):
    for mark in Marks:
        if mark.getCourse() == Course:
            print([mark.getName(), mark.getMark(), mark.getCredit()])
def chooseStudent():
    stdName = input("Enter a Student's name: ")
    return stdName
def averageMark(Name):
    x = y = 0
    for mark in Marks:
        if mark.getName() == Name:
            x += mark.getMark() * mark.getCredit()
            y += mark.getCredit()

    AverageMark = x / y
    AverageMark_fld = floor(AverageMark * 10) / 10
    print("Average Mark for " + Name + ": " + str(AverageMark_fld))

    for students in ClassRoom:
        if students.getName() == Name:
            students.setGPA(AverageMark_fld)
for course in ListOfCourse:
    inputMark(choseCourse())
for course in ListOfCourse:
    printMark(choseCourse())
