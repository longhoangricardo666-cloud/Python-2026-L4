import math
from domains.student import Student
from domains.course import Course
from output import list_courses 
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
        with open("students.txt", "w",encoding="utf-8") as f:
            for student in students:
                print(student.id,student.name,student.dob,file=f)
    return students
def input_courses():
    courses=[]
    n=int(input("enter number of  courses:"))
    for i in range(n):
        print(f"\nCourse{i+1}")
        course_id=input("Enter course ID(unique):")
        name =input("Enter course name:")
        credits=int(input("Enter credits(>0):"))
        courses.append(Course(course_id, name, credits))
    with open("courses.txt", "w",encoding="utf-8")as f:
        for course in courses:
            print(course.id,course.name,course.credits,file=f)
    return courses 

def input_mark():
    mark=float(input("Enter mark:"))
    return math.floor(mark*10) /10
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
    with open("marks.txt", "w",encoding="utf-8")as f:
        for student in students:
            for course in courses:
                print(course.name,student.name,student.marks[course.id],file=f)
 