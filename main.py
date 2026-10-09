from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return{
        "message": "hello good morning"
    }

@app.get("/students")
def get_students():
    return {
        "id": 123,
        "name":"barani",
        "course": "python"
    }
