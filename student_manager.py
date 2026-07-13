import json
from student import Student
class StudentManager:
    def __init__(self):
        self.students={}
        self.load_data()
    
    def add_student(self,student):
        if student.usn in self.students:
            print("usn exists")
        else:
            self.students[student.usn] = student
            self.save_data()
            print("student added succesfully")
    def show_student(self,usn):
        if usn in self.students:
            self.students[usn].display()
        else:
            print("student not found")
    def show_all_students(self):
        if self.students:
            for student in self.students.values():
                student.display()
        else:
            print("no students found")
    def update_student(self, usn):
        if usn in self.students:
            student=self.students[usn]
            print("1.update attendence")
            print("2.update assignment status")
            choice=int(input("enter choice(1 or 2)"))
            if choice==1:
                attended=int(input("enter new attendnece"))
                student.update_attendence(attended)
                self.save_data()
            elif choice==2:
                assignment_status=input("'submitted' or 'pending'  /n")
                student.update_assignment(assignment_status)
                self.save_data()
        else:
            print("student not found")

    def delete_student(self, usn):
        if usn in self.students:
            del self.students[usn]
            self.save_data()
            print("deleted succesfully")
        else:
            print("student not found")  

    def save_data(self):
        student_dict={}
        for student in self.students.values():
            student_dict[student.usn]=student.to_dict()
        with open("student.json","w") as file:
            json.dump(student_dict,file,indent=4)
        

    def load_data(self):
        try:
            with open("student.json","r") as file:
                student_dict=json.load(file)
                for usn,student_data in student_dict.items():
                    student=Student(
                        student_data["usn"],
                        student_data["name"],
                        student_data["attended"],
                        student_data["assignment_status"]
                    )
                    self.students[usn]=student
            

        except FileNotFoundError:
            print("student.json not found \n starting with empty database")
            return {}
        except ValueError:
            print("student.json is invalid\n starting with empty database")
            return {}
        