total_classes = 26
class Student:

    def __init__(self,usn, name,attended,assignment_status):
        self.usn=usn
        self.name=name
        self.attended=attended
        self.assignment_status=assignment_status
    

    def attendence_calculator(self):
        atd_perc=(self.attended/total_classes)*100 
        return atd_perc

    def display(self):
        print("usn:",self.usn)
        print("name:",self.name)
        print("attended:",self.attended)
        print("assignment_status:",self.assignment_status)
        print("attendence percentage:",self.attendence_calculator())
    
    def update_attendence(self,attended):
        self.attended=attended
        print("attendence updated succesfully")
    
    def update_assignment(self,assignment_status):
        self.assignment_status=assignment_status
    
    def to_dict(self):
        student_dict={}
        student_dict["usn"]=self.usn
        student_dict["name"]=self.name
        student_dict["attended"]=self.attended
        student_dict["assignment_status"]=self.assignment_status
        return student_dict