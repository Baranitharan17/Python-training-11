""" try:
    a=int(input("A :"))
    b=int(input("B :"))
    result=a/b
except ZeroDivisionError:
    print("cannot be divisible by zero")
except ValueError:
    print("invalid input")
finally:
    print("calculation done")

f=open("fruits.txt")
content=f.read()
print(content)

f=open("fruits.txt", "w") 
f.write("banana" + "\n")
f.close()

f=open("fruits.txt", "r+") 
print(f.read())

f=open("fruits.txt", "a")
f.write("mango"+ "\n")
f.write("kiwi"+ "\n")
f.write("pomegranate"+ "\n")
f.close()

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
    } """

