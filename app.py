import streamlit as st
from student_manager import StudentManager
from student import Student
from database import DatabaseManager

db=DatabaseManager()
manager=StudentManager(db)


st.title("🧑‍🎓 student management system")
st.write("welcome to student management system")

st.header("ADD STUDENT")
usn=st.text_input("enter new student usn")
name=st.text_input("enter name")
attended=st.number_input("enter number of classes attended",value=0,step=1,max_value=26)
assignment_status=st.selectbox("assignment status",["submitted","pending"])
 
if st.button("Add student"):
        
    if not usn or not name :
        st.error("please enter every feild")
    else: 
            student=Student(usn,name,attended,assignment_status)
            x=manager.add_student(student)
            if x:
                st.success("student added succesfully")
            else:
                st.error("already exists with this usn")


st.header("VIEW STUDENT")
search_usn=st.text_input("search student usn ")
if st.button("search for student"):
     
    if not search_usn:
        st.error("please enter usn")
    else:
        student=manager.show_student(search_usn)
        
        if student is None:
            st.error("student not found ")
        else:
            st.subheader("student details")
            st.write("usn:",student.usn)
            st.write("name:",student.name)
            st.write("attended classes ",student.attended)
            st.metric(
                "Attendance %",
                round(student.attendence_calculator(),2)
                )
            st.write("assignment status",student.assignment_status)
             

st.header("show all students")
if st.button("show al students"):
    students=manager.show_all_students()
   
    if not students:
        st.info("No students found.")
    else:
        rows = [student.to_dict() for student in students]
        st.dataframe(rows)
