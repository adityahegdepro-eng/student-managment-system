from pydantic import BaseModel

class StudentCreate(BaseModel):
    usn: str
    name: str
    attended: int
    assignment_status: str

class StudentUpdate(BaseModel):
    attended: int
    assignment_status: str

class StudentResponse(BaseModel):
    usn: str
    name: str
    attended: int
    assignment_status: str