from fastapi import FastAPI

app=FastAPI()

students = []

@app.get("/students")
def get_students():
    return students

@app.post("/students")
def create_student(student: dict):
    students.append(student)
    return {"message": "Student created", "student": student}

