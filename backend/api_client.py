import requests

BASE_URL = "http://127.0.0.1:8000"


def get_students():
    response = requests.get(f"{BASE_URL}/students")
    response.raise_for_status()
    return response.json()


def create_student(usn, name, attended, assignment_status):
    data = {
        "usn": usn,
        "name": name,
        "attended": attended,
        "assignment_status": assignment_status
    }

    response = requests.post(
        f"{BASE_URL}/students",
        json=data
    )

    return response

def get_student(usn):
    response = requests.get(f"{BASE_URL}/students/{usn}")
    return response

def update_student(usn, attended, assignment_status):
    data = {
        "attended": attended,
        "assignment_status": assignment_status
    }

    response = requests.put(
        f"{BASE_URL}/students/{usn}",
        json=data
    )

    return response

def delete_student(usn):
    response = requests.delete(f"{BASE_URL}/students/{usn}")
    return response

def get_dashboard():
    response = requests.get(f"{BASE_URL}/dashboard")
    response.raise_for_status()
    return response.json()