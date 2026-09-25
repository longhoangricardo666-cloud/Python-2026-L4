USTH Advanced Programming with Python 2026
==================================

* 2410555
* Dinh Hoang Long

def program1():
    def input_students ():
        students =[]
        n=int(input("Enter number of students: "))
        for i in range(n):
            print(f"\nStudent {i+1}")
            student_id=input("Enter student ID:")
            name=input("Enter name:")
            dob=input("Enter date of birth(dd/mm/yyyy):")
            student ={
                "id": student_id,
                "name":name,
                "dob":dob
            }
            students.append(student)
        return students
    students= input_students()
print(students)
