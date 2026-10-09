num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))

def avg(a, b, c):
    average=(a +b + c) / 3
    return average

result=avg(num1, num2, num3)
print("The average is :", result)
