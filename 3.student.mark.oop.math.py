

import math
import numpy as np
import curses 
class Student :
    def __init__(self,student_id,name,dob):
        self.id=student_id
        self.name=name 
        self.dob=dob
        self.marks={}

    def calculate_gpa(self,courses):
        marks=np.array([self.marks[c.id]for c in courses])
        credits= np.array([c.credits for c in courses])
        return np.sum(marks * credits )/np.sum(credits)
class Course:
    def __init__(self,course_id,name,credits):
        self.id=course_id
        self.name=name
        self.credits=credits 

def input_students ():
    students =[]
    n=int(input("Enter number of students: "))
    for i in range(n):
        print(f"\nStudent {i+1}")
        student_id=input("Enter student ID:")
        name=input("Enter name:")
        dob=input("Enter date of birth(dd/mm/yyyy):")
        student =Student(student_id,name,dob)
        students.append(student)
    return students
def input_courses():
    courses=[]
    n=int(input("enter number of  courses:"))
    for i in range(n):
        print(f"\nCourse{i+1}")
        course_id=input("Enter course ID(unique):")
        name =input("Enter name course name:")
        credits=int(input("Enter credits(>0):"))
        courses.append(Course(course_id, name, credits))
    return courses 

def input_mark():
    mark=float(input("Enter mark:"))
    return math.floor(mark*10) /10
def list_students(students):
    for i, student in enumerate(students,start=1):
        print(i,student.id,student.name,student.dob)
def list_courses(courses):
    for i, course in enumerate(courses,start=1):
        print(i,course.id,course.name,"Credits:",course.credits)
def input_marks(students,courses):
    remaining=courses.copy()
    while remaining:
        print("\nCourses stiil needing marks:")
        list_courses(remaining)
        choice =int(input("Select course number:"))
        course=remaining.pop(choice-1)
        for student in students:
            print(f"{course.name}-{student.name}")
            student.marks[course.id]=input_mark()
def show_course_marks(students,courses):
    print("\nView marks for a course:")
    list_courses(courses)
    choice=int(input("Select course number:"))
    course=courses[choice-1]
    for student in students :
        print(student.id,student.name,f"{student.marks[course.id]:.1f}")
def show_gpa(screen,student,courses):
    screen.clear()
    screen.border()
    screen.addstr(1,2,"Student GPA",curses.A_BOLD)
    screen.addstr(3,2,f"ID:{student.id}")
    screen.addstr(4,2,f"Name:{student.name}")
    screen.addstr(5,2,f"GPA:{student.calculate_gpa(courses):.2f}")
    screen.addstr(7,2,"Press any key to continue...")
    screen.refresh()
    screen.getch()
def main():
    students=input_students()
    courses=input_courses()
    input_marks(students,courses)
    print("\nStudent list:")
    list_students(students)
    show_course_marks(students,courses)
    students.sort(key=lambda student:student.calculate_gpa(courses),reverse=True)
    print("\nGPA ranking(descending):")
    for i,student in enumerate(students,start=1):
        print(i,student.id,student.name,
              f"{student.calculate_gpa(courses):.2f}")
    choice=int(input("Select student number to view GPA:"))
    curses.wrapper(show_gpa,students[choice-1],courses)
if __name__=="__main__":
    main()
