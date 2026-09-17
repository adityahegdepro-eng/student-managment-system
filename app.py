import streamlit as st


from backend.api_client import (
    get_students,
    create_student,
    get_student,
    update_student,
    delete_student,
    get_dashboard
)



st.title("Student Management System")
st.subheader("Dashboard")

dashboard = get_dashboard()

total_students = dashboard["total_students"]
average_attendance = dashboard["average_attendance"]
low_attendance = dashboard["low_attendance"]
pending_assignments = dashboard["pending_assignments"]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Students", total_students)

with col2:
    if average_attendance is not None:
        st.metric("Average Attendance", f"{average_attendance:.1f}")
    else:
        st.metric("Average Attendance", "0")

with col3:
    st.metric("Below 75%", low_attendance)

with col4:
    st.metric("Pending Assignments", pending_assignments)


st.subheader("Student Overview")


students = get_students()

if students:
    st.dataframe(students, use_container_width=True)
else:
    st.info("No students found.")




st.header("ADD STUDENT")

usn = st.text_input(
    "enter new student usn",
    key="add_usn"
)

name = st.text_input("enter name")

attended = st.number_input(
    "enter number of classes attended",
    value=0,
    step=1,
    max_value=26
)

assignment_status = st.selectbox(
    "assignment status",
    ["submitted", "pending"]
)

if st.button("Add student"):

    if not usn or not name:
        st.error("please enter every field")

    else:
        response = create_student(
            usn,
            name,
            attended,
            assignment_status
        )

        if response.status_code == 201:
            st.success("Student added successfully")

        elif response.status_code == 409:
            st.error("Already exists with this USN")

        else:
            st.error("Something went wrong")

st.header("VIEW STUDENT")
search_usn=st.text_input("enter student usn ",key="search_usn")
if st.button("search for student"):
     
    if not search_usn:
        st.error("please enter usn")
    else:
        response = get_student(search_usn)

        if response.status_code == 404:
            st.error("Student not found")

        elif response.status_code == 200:
            student = response.json()

            st.subheader("Student Details")
            st.write("USN:", student["usn"])
            st.write("Name:", student["name"])
            st.write("Attended Classes:", student["attended"])

            st.write(
                "Assignment Status:",
                student["assignment_status"]
            )

        else:
            st.error("Something went wrong")
             

st.header("SHOW ALL STUDENTS")

if st.button("show all students", key="show_all_students"):

    students = get_students()

    if not students:
        st.info("No students found.")
    else:
        st.dataframe(
            students,
            use_container_width=True
        )

st.header("UPDATE STUDENTS")

update_usn = st.text_input(
    "enter student usn",
    key="update_usn"
)

if st.button("load student",key="update_load"):

    if not update_usn:
        st.error("please enter usn")

    else:
        response = get_student(update_usn)

        if response.status_code == 404:
            st.error("student not found")

        elif response.status_code == 200:
            student = response.json()
            st.session_state["update_student"] = student

        else:
            st.error("something went wrong")


if "update_student" in st.session_state:

    student = st.session_state["update_student"]

    st.success("student loaded successfully")

    st.write("Student name:", student["name"])

    updated_attended = st.number_input(
        "attended classes:",
        value=student["attended"],
        max_value=26
    )

    options = ["submitted", "pending"]

    updated_assignment = st.selectbox(
        "assignment status:",
        options,
        index=options.index(student["assignment_status"])
    )

    if st.button("UPDATE STUDENT"):

        response = update_student(
            student["usn"],
            updated_attended,
            updated_assignment
        )

        if response.status_code == 200:
            st.success("student updated successfully")
            del st.session_state["update_student"]

        elif response.status_code == 404:
            st.error("student not found")

        else:
            st.error("something went wrong")

    
st.header("DELETE STUDENT")

delete_usn = st.text_input(
    "enter student usn",
    key="delete_usn"
)

if st.button("load student",key="delete_load"):

    if not delete_usn:
        st.error("please enter usn")

    else:
        response = get_student(delete_usn)

        if response.status_code == 404:
            st.error("student not found")

        elif response.status_code == 200:
            student = response.json()
            st.session_state["delete_student"] = student

        else:
            st.error("something went wrong")


if "delete_student" in st.session_state:

    student = st.session_state["delete_student"]

    st.success("student loaded successfully")

    st.write("Student USN:", student["usn"])
    st.write("Student Name:", student["name"])
    st.write("Attended Classes:", student["attended"])
    st.write("Assignment Status:", student["assignment_status"])

    if st.button("delete student",key="confirm_delete"):

        response = delete_student(student["usn"])

        if response.status_code == 200:
            st.success("student deleted successfully")
            del st.session_state["delete_student"]

        elif response.status_code == 404:
            st.error("student not found")

        else:
            st.error("student deletion failed")
