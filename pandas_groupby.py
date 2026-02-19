import pandas as pd

data = {
    "Department": ["HR", "IT", "IT", "Finance", "HR"],
    "Salary": [50000, 60000, 45000, 80000, 52000]
}

df = pd.DataFrame(data)

grouped = df.groupby("Department")["Salary"].mean()

print("Average Salary by Department:\n")
print(grouped)
