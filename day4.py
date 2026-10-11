import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


""" data = {
    "name": ["Mani", "Ravi", "Kumar", "Arun", "Priya"],
    "python": [85, 78, 92, 67, 88],
    "sql": [80, 75, 90, 70, 85],
    "math": [90, 82, 88, 65, 91]
}
df = pd.DataFrame(data)
df["average"] = (
    df["python"] + df["sql"] + df["math"]
) / 3
print(df)
print("Python Average:", df["python"].mean())
top_student = df.loc[df["average"].idxmax()]
print("Top Student:")
print(top_student)
plt.bar(df["name"], df["average"])
plt.title("Student Average Marks")
plt.xlabel("Student")
plt.ylabel("Average")
plt.show() """

""" numbers=np.array([10,20,30,40,50,60,70,80,90,100])
print("The array of numbers :", numbers) """

""" numbers=np.array([10,20,30,40,50,60,70,80,90,100])
maximum = np.max(numbers)
minimum = np.min(numbers)
average=np.mean(numbers)
total=np.sum(numbers)

print("Maximum :", maximum)
print("Minimum :", minimum)
print("Average :", average)
print("Total :", total)
 """

#create a 3x3 array

""" numbers=np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

print("The 3x3 array is :" , numbers)

#accessing one element

print("Accessing one element :", numbers[2,1]) """

# create a pandas data frame

""" data={
    "Students": ["Arun", "Varun", "Tharun", "Harshan", "Pranitha"],
    "Marks" : [35,50,70,85,95]
    }
df = pd.DataFrame(data) """
""" print(df) """

#print the first three rows uing head
""" print(df.head(3)) """

#print only the name and mark columns
""" print(df[["Students", "Marks"]]) """
#add a passed column based on marks

""" df["Passed"] = df["Marks"] >=40
print(df) """

#create a bar showing using student marks

""" plt.bar(df["Students"], df["Marks"])
plt.title("Students Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.show()
 """

""" BigBillionDays=["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"]
sales=[100,150,120,200,250]
plt.plot(BigBillionDays, sales, marker="o")
plt.title("Overall sales over 5 days")
plt.xlabel("BigBillionDays")
plt.ylabel("sales")
plt.show()
 """
Marks=[85,90,35,92,28,75,65,80,55,48]
plt.hist(Marks, bins=5, edgecolor="black")
plt.title("Distribution of student marks")
plt.xlabel("Marks")
plt.ylabel("Number of students")
plt.show()

