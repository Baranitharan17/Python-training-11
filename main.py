from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return{
        "message": "hello good morning"
    }
students=[{
    "id": 1,
    "name": "barani",
    "course" : "python"
}]

@app.get("/students")
def get_students():
    return students 

@app.post("/students")
def create_student(student: dict):
    students.append(student)
    return{
        "message": "Student created",
        "student": student
    }
