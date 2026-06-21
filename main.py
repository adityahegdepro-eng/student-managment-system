system={}
total_classes=25
def fill_details():
    usn=input("enter the usn:")
    if usn in system:
        print("usn already exist")
        return
    else:
        system[usn]={}
    
    system[usn]["name"]=input("enter name of the student:")
    try:
        att_cls=int(input("enter number of classes student attended(0-25):"))
        system[usn]["attended"]=att_cls
    except :
        print("enter valid input")
    
    else:    
        ass_st=int(input("1.assignment pending  /n  2.assignment submitted"))
        if ass_st==1:
            system[usn]["assignment_status"]="pending"
        elif ass_st==2:
            system[usn]["assignment_status"]="submitted"
        else:
            print("enter valid option") 

        

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
        fill_details()
        
    elif choice==2:
        usn=input("enter usn of the students:") 
        if usn in system: 
                print("name :",system[usn]["name"])
                print("attended classes :",system[usn]["attended"])
                print("total classes :",total_classes)
                print("attendance percentage:",(system[usn]["attended"]/total_classes)*100,"%")
                print("assignment status:",system[usn]["assignment_status"])
                
                
                
        else:
                print("🔸enter valid usn🔸")      
    elif choice==3:
        if system!={}:
            print("all students:")
            for usn in system:
                print(usn,"=",system[usn]["name"])
        else:
            print("🔸please add students first to view🔸")
    elif choice==4:
        usn=input("enter usn of student whose data to be changed")
        if usn in system:
            print("1.update attendence")
            print("2.update assignment status")
            choice=int(input("enter choice(1 or 2)"))
            if choice==1:
                system[usn]["attended"]=int(input("new attendence"))
                att_perc=(system[usn]["attended"]/total_classes)*100 
                system[usn]["attendance %"]=att_perc 
                print("attendence update success")
            elif choice==2:
                ass_st=int(input("1.assignment pending  /n  2.assignment submitted"))
                if ass_st==1:
                    system[usn]["assignment_status"]="pending"
                elif ass_st==2:
                    system[usn]["assignment_status"]="submitted"
                else:
                    print("enter valid option") 
        else:
            print("enter existing usn")
       
    elif choice==5:
        usn=input("enter usn of student to be deleted")
        if usn in system:
            del system[usn]
            print("Student deleted successfully")
        else:
            print("enter existing usn")
    elif choice==6:
        break