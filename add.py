def add():
    print(a+b)
a=10
b=20
add()    

name=input("Enter your name :")
def greet(name):
    print("Hello", name, "welcome !")

greet(name)

a=int(input("Enter a num1:"))
b=int(input("Enter a num2:"))
def findlargest():
    if(a>b):
        print("A is Largest")
    elif(b>a):
            print("B is Largest")

findlargest()            

num=int(input("Enter a num :"))
def oddoreven():
    if(num%2==0):
        print("Even")
    else:
        print("Odd")

oddoreven()

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))

def avg(a, b, c):
    average=(a +b + c) / 3
    return average

result=avg(num1, num2, num3)
print("The average is :", result)

student=["Rahul", "Arun", "Aravind", "Ramya", "Priya"]
for i in student:
    print(i)

student=["Rahul", "Arun", "Aravind", "Ramya", "Priya"]
student.append("Kishore")
print(student)

student=["Rahul", "Arun", "Aravind", "Ramya", "Priya"]
student.remove("Aravind")
print(student)

numbers=[10,25,7,45,32]
largest=numbers[0]
for num in numbers:
    if num>largest:
        largest=num
print("Largest number is :" , largest)

numb=[10,21,34,43,58]
count=0
for i in numb:
    if(i%2==0):
        count=count+1
print("Number of even numbers :", count)

student={
    "name": "Rahul",
    "age": 22,
    "mark": 75

}

print("Name:", student["name"])
print("Age:", student["age"])
print("Mark:", student["mark"])


student={
    "name": "Rahul",
    "age": 22,
    "mark": 75

}
student["city"] ="Madurai"
print(student)

student={
    "name": "Rahul",
    "age": 22,
    "mark": 75

}
student["mark"] =90
print(student)

class car:
    def __init__(self, brand, name, year):
        self.brand= brand
        self.name= name
        self.year= year

car1=car("Suzuki", "Baleno", 2026)
car2=car("Hyundai", "Venue", 2026)

print("Car1: ")
print("Brand :", car1.brand)
print("Name :", car1.name)
print("Year :", car1.year)

print("Car2: ")
print("Brand :", car2.brand)
print("Name :", car2.name)
print("Year :", car2.year)

class employee:
    def __init__(self, name, salary):
        self.name= name
        self.salary=salary

    def display(self):
        print("Name :", self.name) 
        print("Salary :", self.salary)

emp=employee("Arjun", 50000)
emp.display()
        