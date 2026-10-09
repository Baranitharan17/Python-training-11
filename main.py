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

@app.put("/students/{student_id}")
def update_student(student_id: int, student: dict):
    for item in students:
        if item["id"] == student_id:
            item["name"] = student["name"]
            return {"message": "Student updated", "student": item}
    return {"message": "Student not found"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for item in students:
        if item["id"] == student_id:
            students.remove(item)
            return {"message": "Student deleted"}
    return {"message": "Student not found"}
