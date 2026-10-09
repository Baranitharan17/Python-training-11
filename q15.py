class employee:
    def __init__(self, name, salary):
        self.name= name
        self.salary=salary

    def display(self):
        print("Name :", self.name) 
        print("Salary :", self.salary)

emp=employee("Arjun", 50000)
emp.display()