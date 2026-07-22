import streamlit as st
from student_manager import StudentManager
from student import Student
from database import DatabaseManager

db=DatabaseManager()
manager=StudentManager(db)


st.title("🧑‍🎓 student management system")
st.write("welcome to student management system")

st.header("ADD STUDENT")
usn=st.text_input("enter new student usn",key="add_usn")
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
search_usn=st.text_input("enter student usn ",key="search_usn")
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
                round(student.attendance_calculator(),2)
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

st.header("UPDATE STUDENTS ")
update_usn=st.text_input(" enter student usn",key="update_usn")
if st.button("load student"):
    student=manager.show_student(update_usn)
    if student is None:
        st.error("student not found")
    else:
        st.session_state["update_student"]=student
if "update_student" in st.session_state:
        student=st.session_state["update_student"]
        st.success("student loaded succesfully")
        st.write("student name:",student.name)
        updated_attended=st.number_input("attended classes : ",value=student.attended,max_value=26)
        options=["submitted","pending"]
        updated_assignment=st.selectbox("assignment status:",
                     options,
                     index=options.index(student.assignment_status)
                     )
        if st.button("UPDATE STUDENT"):
            x=manager.update_student(student.usn,updated_attended,updated_assignment)
            if x:
                st.success("student updated succesully")
                del st.session_state["update_student"]
            else:
                st.error("something went wrong")

    
st.header("DELETE STUDENT")
delete_usn=st.text_input("enter student usn ",key="delete_usn")
if st.button("load "):
    student=manager.show_student(delete_usn)
    if student is None:
        if "delete_student" in st.session_state:
            del st.session_state["delete_student"]
        st.error(" ❌❌student not found")
        
    else:
        st.session_state["delete_student"]=student
if "delete_student" in st.session_state:
    student=st.session_state["delete_student"]
    st.success("student loaded succesfully")
    st.write("student usn",student.usn)
    st.write("student name",student.name)
    st.write("Attended Classes:", student.attended)
    st.write("Assignment Status:", student.assignment_status)
    if st.button("delete student"):
        x=manager.delete_student(student.usn)
        if x:
            st.success("student deleted from database")
            del st.session_state["delete_student"]
        else:
            st.error("student deletion fsiled")
