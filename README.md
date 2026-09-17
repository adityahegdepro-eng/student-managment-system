# Student Management System

A full-stack Student Management System built progressively to learn **Python, OOP, SQL, Streamlit, REST APIs, FastAPI, API clients, and backend architecture**.

The project evolved from a simple CLI application into a client-server application where **Streamlit communicates with a FastAPI REST API**, which handles business logic and database operations through MySQL.

---

## 🚀 Project Evolution

The project was developed incrementally:

| Version | Focus                                         |
| ------- | --------------------------------------------- |
| V1      | CLI CRUD                                      |
| V2      | JSON Persistence                              |
| V3      | Object-Oriented Programming                   |
| V4      | MySQL Database Integration                    |
| V5      | Streamlit UI                                  |
| V6      | Dashboard & Analytics                         |
| V7      | FastAPI REST API + Client-Server Architecture |

The purpose of the project was not simply to build a student CRUD application, but to progressively learn how real software systems are structured.

---

# 🏗️ Current Architecture

```text
                    ┌──────────────────────┐
                    │      Streamlit       │
                    │     Frontend / UI    │
                    └──────────┬───────────┘
                               │
                         HTTP + JSON
                               │
                               ▼
                    ┌──────────────────────┐
                    │       FastAPI        │
                    │       REST API       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   StudentManager     │
                    │   Business Logic     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  DatabaseManager     │
                    │      SQL Layer       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │        MySQL         │
                    │      Database        │
                    └──────────────────────┘
```

### Responsibility of each layer

**Streamlit**

* Provides the user interface
* Sends HTTP requests to the API
* Displays API responses

**FastAPI**

* Exposes REST endpoints
* Validates request data
* Handles HTTP status codes
* Provides automatic Swagger/OpenAPI documentation

**StudentManager**

* Contains student-related business logic
* Coordinates operations between the API and database layer

**DatabaseManager**

* Handles MySQL operations
* Executes SQL queries
* Manages database interaction

**MySQL**

* Stores persistent student data

---

# ✨ Features

## Student Management

* Add student
* View individual student
* View all students
* Update student
* Delete student
* Duplicate USN detection
* Input validation
* Assignment status tracking
* Attendance tracking

## Dashboard

* Total students
* Average attendance
* Students below attendance threshold
* Pending assignments

## REST API

The application exposes CRUD functionality through FastAPI:

```text
GET     /students
GET     /students/{usn}
POST    /students
PUT     /students/{usn}
DELETE  /students/{usn}
GET     /dashboard
```

---

# 🔌 API Examples

## Get all students

```http
GET /students
```

Example response:

```json
[
    {
        "usn": "1bi25cs002",
        "name": "av",
        "attended": 25,
        "assignment_status": "pending"
    }
]
```

---

## Get a student

```http
GET /students/{usn}
```

Example:

```http
GET /students/1bi25cs002
```

---

## Create a student

```http
POST /students
```

Request:

```json
{
    "usn": "1bi25cs010",
    "name": "Rahul",
    "attended": 22,
    "assignment_status": "submitted"
}
```

Successful response:

```text
201 Created
```

---

## Update a student

```http
PUT /students/{usn}
```

Request:

```json
{
    "attended": 24,
    "assignment_status": "submitted"
}
```

Successful response:

```text
200 OK
```

---

## Delete a student

```http
DELETE /students/{usn}
```

Successful response:

```json
{
    "message": "student deleted successfully"
}
```

---

# 📊 Dashboard API

```http
GET /dashboard
```

Example:

```json
{
    "total_students": 3,
    "average_attendance": 15.7,
    "low_attendance": 1,
    "pending_assignments": 1
}
```

---

# 🧪 API Testing

The API was tested using:

### Swagger / OpenAPI

FastAPI automatically provides interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

### Postman

Postman was used to independently test:

* GET
* POST
* PUT
* DELETE
* HTTP status codes
* JSON request/response data

This allowed the backend to be tested independently of the Streamlit frontend.

---

# 🛡️ HTTP Status Codes

The API uses appropriate HTTP responses:

| Status | Meaning                      |
| ------ | ---------------------------- |
| `200`  | Successful request           |
| `201`  | Student successfully created |
| `404`  | Student not found            |
| `409`  | Duplicate USN                |
| `422`  | Request validation failed    |
| `500`  | Server/database error        |

---

# 📦 Pydantic Models

FastAPI uses Pydantic models to define the API data contract.

### StudentCreate

```python
class StudentCreate(BaseModel):
    usn: str
    name: str
    attended: int
    assignment_status: str
```

### StudentUpdate

```python
class StudentUpdate(BaseModel):
    attended: int
    assignment_status: str
```

### StudentResponse

```python
class StudentResponse(BaseModel):
    usn: str
    name: str
    attended: int
    assignment_status: str
```

This provides request validation and predictable API responses.

---

# 🔐 Environment Configuration

Database credentials are stored using environment variables rather than being hardcoded into the source code.

Example `.env`:

```env
DB_HOST=localhost
DB_PORT=3307
DB_USER=root
DB_PASSWORD=YOUR_PASSWORD
DB_NAME=student_management
```

`.env` is excluded from Git using `.gitignore`.

---

# 📁 Project Structure

```text
STUDENT MANAGEMENT SYSTEM/
│
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── api_client.py
│   └── schemas.py
│
├── app.py
├── student.py
├── student_manager.py
├── database.py
│
├── .env
├── .gitignore
└── requirements.txt
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone <repository-url>
cd STUDENT-MANAGEMENT-SYSTEM
```

## 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure MySQL

Create the database:

```sql
CREATE DATABASE student_management;
```

Create the required `student` table according to the application's database schema.

Then configure `.env` with your MySQL credentials.

---

# ▶️ Running the Application

The application requires **two processes**.

## Terminal 1 — FastAPI

```bash
uvicorn backend.main:app --reload
```

API:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

## Terminal 2 — Streamlit

```bash
streamlit run app.py
```

Streamlit will provide the local application URL.

---

# 🧠 Concepts Learned

This project was intentionally built incrementally.

### Python

* Functions
* Classes
* Exception handling
* File handling
* JSON
* Modules and imports

### Object-Oriented Programming

* Classes
* Objects
* Encapsulation
* Separation of responsibilities

### SQL / MySQL

* CRUD operations
* Parameterized queries
* Database connections
* Persistent storage
* Aggregation queries

### Streamlit

* UI components
* Session state
* Metrics
* Tables
* User interaction

### Backend Development

* FastAPI
* REST APIs
* HTTP methods
* Path parameters
* JSON request/response
* Pydantic
* HTTP status codes
* Error handling
* Swagger/OpenAPI
* Postman
* API clients
* Client-server architecture

### Software Architecture

The project demonstrates separation between:

```text
Presentation
     ↓
API
     ↓
Business Logic
     ↓
Data Access
     ↓
Database
```

---

# 🔄 Version History

## V1 — CLI CRUD

Built the initial command-line student management system.

Implemented:

* Add
* View
* Update
* Delete
* Attendance
* Assignment status
* Validation
* Duplicate USN checking

## V2 — JSON Persistence

Added:

* Save to JSON
* Load from JSON
* Auto-save
* Auto-load
* Missing/corrupt JSON handling

## V3 — OOP Refactor

Introduced:

```text
Student
StudentManager
```

Responsibilities were separated from the main application logic.

## V4 — MySQL

Replaced JSON persistence with MySQL.

Introduced:

```text
DatabaseManager
```

for database operations.

## V5 — Streamlit

Added a graphical web interface with:

* CRUD operations
* Student overview
* Interactive inputs
* Session state

## V6 — Dashboard & Analytics

Added:

* Total student count
* Average attendance
* Low attendance count
* Pending assignment count

## V7 — FastAPI & REST

Converted the application into a client-server architecture.

Added:

* FastAPI
* REST endpoints
* Pydantic models
* Response models
* HTTP status codes
* Error handling
* Swagger/OpenAPI
* Postman testing
* `requests` API client
* `.env` configuration

Final architecture:

```text
Streamlit
    ↓
HTTP
    ↓
FastAPI
    ↓
StudentManager
    ↓
DatabaseManager
    ↓
MySQL
```

---

# 🎯 Purpose of the Project

This project is a **software engineering learning project**.

The goal was to understand how an application evolves from:

```text
Simple Python Program
        ↓
OOP Application
        ↓
Database Application
        ↓
Web UI
        ↓
REST API
        ↓
Client-Server Application
```

Rather than continuously adding features to the same application, V7 represents the point where the project is considered complete.

Future projects will focus on more advanced areas such as **AI systems, backend engineering, LLMs, RAG, deployment, and scalable software architecture**.

---

# 👨‍💻 Author

**Aditya Hegde**

Computer Science Engineering Student

Built as part of a long-term journey toward **Software Engineering + AI Systems Engineering**.
