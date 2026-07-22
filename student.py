total_classes = 26
class Student:

    def __init__(self,usn, name,attended,assignment_status):
        self.usn=usn
        self.name=name
        self.attended=attended
        self.assignment_status=assignment_status
    

    def attendance_calculator(self):
        atd_perc=(self.attended/total_classes)*100 
        return atd_perc

    def display(self):
        print("usn:",self.usn)
        print("name:",self.name)
        print("attended:",self.attended)
        print("assignment_status:",self.assignment_status)
        print("attendance percentage:",self.attendance_calculator())
    
    def to_dict(self):
        return {
            "USN": self.usn,
            "Name": self.name,
            "Attended": self.attended,
            "Assignment Status": self.assignment_status,
            "Attendance %": round(self.attendance_calculator(), 2)
        }
