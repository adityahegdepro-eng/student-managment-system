
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
    
        
    def update_student(self, usn,attended,assignment_status):
        student=self.database.get_student(usn)

        if student is None:
            return None
        
        else:                
            self.database.update_attendance(attended,usn)
            self.database.update_assignment(assignment_status,usn)
            return True


    def delete_student(self, usn):
        student=self.database.get_student(usn)
        if student is None:
            return False 
        self.database.delete_student(usn)
        return True