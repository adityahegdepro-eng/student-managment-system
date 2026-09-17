from fastapi import FastAPI, HTTPException


from database import DatabaseManager
from student_manager import StudentManager
from backend.schemas import StudentCreate,StudentUpdate,StudentResponse
from student import Student
app = FastAPI()

db = DatabaseManager()
student_manager = StudentManager(db)


@app.get("/")
def home():
    return {"message": "Student Management API is running"}


@app.get("/students", response_model=list[StudentResponse])

def get_students():
    students = student_manager.show_all_students()

    return students

@app.get("/students/{usn}", response_model=StudentResponse)
def get_student(usn):
    student = student_manager.show_student(usn)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "usn": student.usn,
        "name": student.name,
        "attended": student.attended,
        "assignment_status": student.assignment_status
    }


@app.post(
    "/students",
    response_model=StudentResponse,
    status_code=201
)
def create_student(student: StudentCreate):
    student_obj = Student(
        student.usn,
        student.name,
        student.attended,
        student.assignment_status
    )

    created = student_manager.add_student(student_obj)

    if not created:
        raise HTTPException(
            status_code=409,
            detail="Student with this USN already exists"
        )

    return student_obj

@app.put("/students/{usn}", response_model=StudentResponse)
def update_student(usn: str, student: StudentUpdate):

    updated = student_manager.update_student(
        usn,
        student.attended,
        student.assignment_status
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="student not found"
        )

    updated_student = student_manager.show_student(usn)

    return {
        "usn": updated_student.usn,
        "name": updated_student.name,
        "attended": updated_student.attended,
        "assignment_status": updated_student.assignment_status
    }

@app.delete("/students/{usn}")
def delete_student(usn:str):
    deleted=student_manager.delete_student(usn)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="student not found"
        )
    return {
        "message":"student deleted succesfully"
    }

@app.get("/dashboard")
def get_dashboard():

    return {
        "total_students": student_manager.total_students(),
        "average_attendance": student_manager.average_attendance(),
        "low_attendance": student_manager.low_attendance_count(),
        "pending_assignments": student_manager.pending_assignments()
    }