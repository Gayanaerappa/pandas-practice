import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Salary": [50000, 60000, 45000]
}

df = pd.DataFrame(data)

# Increase salary by 10%
df["Updated_Salary"] = df["Salary"].apply(lambda x: x * 1.10)

print("Updated Salaries:\n")
print(df)
