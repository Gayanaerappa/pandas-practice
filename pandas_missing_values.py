import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Salary": [50000, None, 45000, None]
}

df = pd.DataFrame(data)

print("Before Filling Missing Values:\n")
print(df)

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print("\nAfter Filling Missing Values with Mean:\n")
print(df)
