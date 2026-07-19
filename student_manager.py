
from student import Student
class StudentManager:
    def __init__(self,database):
        self.database=database
        
    
    def add_student(self,student):
        if self.database.student_exist(student.usn):
            print("usn exists")
            return 
        
        self.database.insert_students(student)
        return True

    def show_student(self,usn):
        student=self.database.get_student(usn)
        
        if student :
            stu_obj=Student(student[0],student[1],student[2],student[3])
            return stu_obj
        else:
            return None
            

        
    def show_all_students(self):
        students = self.database.get_all_students()
        print(students)
        students_list = []
        for student in students:
            stu_obj = Student(student[0], student[1], student[2], student[3])
            students_list.append(stu_obj)
            print(students_list)
        return students_list
    
        
    def update_student(self, usn):
        student=self.database.get_student(usn)

        if student is None:
            print("student not found")
            return 
        
        print("1.update attendence")
        print("2.update assignment status")
        choice=int(input("enter choice(1 or 2)"))
        if choice==1:
            attended=int(input("enter new attendnece"))                
            self.database.update_attendence(attended,usn)
            print("updated succesfully")
        elif choice==2:
            try:
                print("enter updated assignment stauts")
                choice=int(input("1.submitted \n2.pending \nenter your choice"))
                if choice==1:
                    assignment_status="submitted"
                elif choice==2:
                    assignment_status="pending"
                else:
                    print("choice must be 1 or 2")

            except ValueError:
                print("enter valid assginment status")

            self.database.update_assignment(assignment_status,usn)
            print("updated succesfully")


    def delete_student(self, usn):
        student=self.database.get_student(usn)

        if student is None:
            print("student not found")
            return   
        
        self.database.delete_student(usn)
        print("student deleted succesfully")