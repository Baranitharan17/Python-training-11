""" import pandas as pd
import matplotlib.pyplot as plt
data = {
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

import numpy as np
numbers=np.array([10,20,30,40,50,60,70,80,90,100])
print("The array of numbers :", numbers)

maximum = np.max(numbers)
minimum = np.min(numbers)
average=np.mean(numbers)
total=np.sum(numbers)
