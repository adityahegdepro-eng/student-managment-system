system={}
total_classes=25
def fill_details():
    usn=input("enter the usn:")
    system[f"{usn}"]={}
    while True:
        system[f"{usn}"]["name"]=input("enter name of the student:")
        att_cls=int(input("enter number of classes student attended(0-25):"))
        system[f"{usn}"]["attended"]=att_cls
        att_perc=(att_cls/total_classes)*100 
        system[f"{usn}"]["attendence %"]=att_perc 
        
        ass_st=int(input("1.assignment pending  /n  2.assignment submitted"))
        if ass_st==1:
            system[f"{usn}"]["assignment_status"]="pending"
        elif ass_st==2:
            system[f"{usn}"]["assignment_status"]="submitted"
        else:
            print("enter valid option") 

        break
print("1.enter student details")
print("2.view student details")
print("3.exit")
while True:
    choice=int(input("enter your choice(must be an integer (1-3)):"))
    if choice==1:
        fill_details()
        
    if choice==2:
        if system!={}:
            usn=input("enter usn of the students:") 
            print("name :",system[f"{usn}"]["name"])
            print("attended classes :",system[f"{usn}"]["attended"])
            print("total classes :",total_classes)
            print("attendence percentage:",system[f"{usn}"]["attendence %"],"%")
            print("assignment status:",system[f"{usn}"]["assignment_status"])

                
                
        else:
            print("🔸please add students first to view🔸")      
    if choice==3:
        break
     

        

