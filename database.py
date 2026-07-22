import mysql.connector

class DatabaseManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            port=3307,
            password="password@root",
            database="student_management"
        )
        
        self.cursor = self.connection.cursor(buffered=True)

    def insert_students(self,student):
        query = """
        INSERT INTO student
        VALUES (%s, %s, %s, %s)
        """
        values = (
        student.usn,
        student.name,
        student.attended,
        student.assignment_status
        )
        self.cursor.execute(query,values)
        self.connection.commit()

    def get_student(self,usn):
        query="SELECT * FROM student WHERE usn=%s"
        self.cursor.execute(query,(usn,))
        student=self.cursor.fetchone()
        return student

    def get_all_students(self):
        self.cursor.execute("SELECT * FROM student")
        rows = self.cursor.fetchall()
        return rows
    
    def update_attendance(self,attended,usn):
        query="UPDATE student SET attended=%s WHERE usn=%s"
        self.cursor.execute(query,(attended,usn))
        self.connection.commit()

    def update_assignment(self,assignment_status,usn):
        query="UPDATE student SET assignment_status=%s WHERE usn=%s"
        self.cursor.execute(query,(assignment_status,usn))
        self.connection.commit()

    def student_exist(self,usn):
        query="SELECT * FROM student WHERE usn=%s"
        self.cursor.execute(query,(usn,))
        student=self.cursor.fetchone()
        return student is not None



    def delete_student(self,usn):
        query="DELETE FROM student WHERE usn=%s"
        self.cursor.execute(query,(usn,))
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()