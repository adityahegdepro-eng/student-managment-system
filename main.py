import json
from student import Student 
from student_manager import StudentManager

manager=StudentManager()

while True:
    print("----------------------")
    print("1.enter student details")
    print("2.view student details")
    print("3.show all students")
    print("4.update student")
    print("5.delete student")
    print("6.exit")
    choice=int(input("enter your choice(must be an integer (1-4)):"))
    if choice==1:
        usn=input("enter usn:")
        name=input("enter name:")
        try:
            attended=int(input("attended classes:"))

        except ValueError:
            print("enter valid attendence")
        try:
            choice=int(input("1.submitted \n2.pending \nenter your choice"))
            if choice==1:
                assignment_status="submitted"
            elif choice==2:
                assignment_status="pending"
            else:
                print("choice must be 1 or 2")

        except ValueError:
            print("enter valid assginment status")

        student=Student(usn,name,attended,assignment_status)
        manager.add_student(student)
       
    elif choice==2:
        
        usn=input("enter usn of the students:") 
        manager.show_student(usn)
    elif choice==3:
    
        manager.show_all_students()
    elif choice==4:
        usn=input("enter usn of the students:") 
        manager.update_student(usn)
        
    elif choice==5:
        usn=input("enter usn of the students:") 
        manager.delete_student(usn)
        
    elif choice==6:
        break
