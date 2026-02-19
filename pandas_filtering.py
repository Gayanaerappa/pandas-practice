import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 22, 35, 28],
    "Salary": [50000, 60000, 45000, 80000, 52000]
}

df = pd.DataFrame(data)

# Filter employees with salary > 50000
filtered_df = df[df["Salary"] > 50000]

print("Employees with Salary > 50000:\n")
print(filtered_df)
