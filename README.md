# 🎓 Student Management System

A full-stack Student Management System built with **Python, OOP, MySQL, and Streamlit**.

The project started as a command-line CRUD application and evolved into a database-backed web application with a layered architecture, persistent storage, student management, and dashboard analytics.

---

## 🚀 Features

### Student Management

* Add students
* View individual student details
* View all students
* Update attendance
* Update assignment status
* Delete students
* Duplicate USN validation
* Input validation

### Database

* MySQL persistent storage
* Parameterized SQL queries
* CRUD operations
* Database abstraction through `DatabaseManager`

### Dashboard & Analytics

* Total number of students
* Average attendance
* Students below attendance threshold
* Pending assignments
* Student overview table

### UI

* Streamlit web interface
* Interactive forms
* Session state for multi-step operations
* Success/error feedback
* Dashboard metrics

---

## 🏗️ Architecture

The project follows a layered architecture:

```text
                    Streamlit UI
                       app.py
                         │
                         ▼
                  StudentManager
               Business Logic Layer
                         │
                         ▼
                 DatabaseManager
                  Database Layer
                         │
                         ▼
                      MySQL
```

### Responsibilities

**`app.py`**

* Handles the Streamlit interface
* Collects user input
* Displays results
* Manages UI state

**`student_manager.py`**

* Contains business logic
* Coordinates operations between the UI and database
* Converts database records into `Student` objects

**`student.py`**

* Defines the `Student` class
* Contains student-related data and calculations

**`database.py`**

* Handles MySQL connection
* Executes SQL queries
* Performs database CRUD operations

---

## 📁 Project Structure

```text
STUDENT-MANAGEMENT-SYSTEM/
│
├── app.py
├── student.py
├── student_manager.py
├── database.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

| Technology             | Purpose                   |
| ---------------------- | ------------------------- |
| Python                 | Core programming language |
| OOP                    | Application structure     |
| MySQL                  | Persistent database       |
| mysql-connector-python | Python ↔ MySQL connection |
| Streamlit              | Web interface             |
| Git                    | Version control           |
| GitHub                 | Source code hosting       |

---

## 🗄️ Database

The application uses a MySQL database named:

```text
student_management
```

The main table is:

```text
student
```

The student records contain information such as:

```text
USN
Name
Attended
Assignment Status
```

---

## 🔄 Project Evolution

This project was developed incrementally rather than being built all at once.

### V1 — CLI CRUD

Implemented:

* Add student
* View student
* View all students
* Update student
* Delete student
* Attendance tracking
* Assignment tracking
* Input validation
* Duplicate USN checking

### V2 — JSON Persistence

Added:

* Saving data to JSON
* Loading data from JSON
* Auto-save
* Auto-load
* Missing/corrupt JSON handling

### V3 — OOP Refactor

Introduced:

* `Student` class
* `StudentManager` class
* Separation of responsibilities

### V4 — MySQL Integration

Added:

* MySQL database
* SQL CRUD operations
* `DatabaseManager`
* Parameterized queries
* Persistent database storage

### V5 — Streamlit Application

Converted the CLI application into a web application.

Added:

* Streamlit UI
* CRUD forms
* Session state
* Interactive feedback
* Database-backed interface

### V6 — Dashboard & Analytics

Added:

* Dashboard metrics
* Student overview
* Attendance analytics
* Assignment analytics

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd STUDENT-MANAGEMENT-SYSTEM
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure MySQL

Create the database:

```sql
CREATE DATABASE student_management;
```

Create the required `student` table according to the fields used by the application.

Update the MySQL connection details in `database.py`:

```python
self.connection = mysql.connector.connect(
    host="localhost",
    user="root",
    port=3307,
    password="YOUR_PASSWORD",
    database="student_management"
)
```

> Do not commit your real database password to GitHub. Use environment variables for production projects.

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🧠 Concepts Learned

This project was used to build practical understanding of:

* Python functions
* Object-oriented programming
* Classes and objects
* Exception handling
* File persistence
* JSON
* SQL
* MySQL
* CRUD operations
* Parameterized queries
* Database abstraction
* Separation of concerns
* Layered architecture
* Streamlit
* Session state
* Git and GitHub
* Basic analytics

---

## 🔮 Future Improvements

Possible improvements for a production version include:

* User authentication and authorization
* Environment variables for secrets
* REST API using FastAPI
* PostgreSQL support
* Automated testing
* Logging
* Better error handling
* Pagination
* Role-based access
* Deployment
* Docker containerization

These are intentionally outside the scope of this version.

---

## 🎯 Project Goal

The primary goal of this project was not simply to create a student CRUD application.

It was to progressively learn how a software system evolves:

```text
CLI
 ↓
Persistence
 ↓
OOP
 ↓
Database
 ↓
Web UI
 ↓
Analytics
```

The project serves as a foundation for moving toward larger **software engineering and AI systems projects**.

---

## 👨‍💻 Author

**Aditya Hegde**

Computer Science Engineering Student
Bangalore Institute of Technology

---

## 📌 Version

**V6 — Dashboard & Analytics**

Status: **Complete ✅**
