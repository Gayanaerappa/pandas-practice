import pandas as pd

# -----------------------------
# 1. Create Sample Dataset
# -----------------------------
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 22, 35, 28],
    "Salary": [50000, 60000, 45000, 80000, 52000],
    "Department": ["HR", "IT", "IT", "Finance", "HR"]
}

df = pd.DataFrame(data)

print("\n✅ Original DataFrame:\n")
print(df)

# -----------------------------
# 2. Basic Information
# -----------------------------
print("\n✅ DataFrame Info:\n")
print(df.info())

print("\n✅ Statistical Summary:\n")
print(df.describe())

# -----------------------------
# 3. Column Selection
# -----------------------------
print("\n✅ Selecting Salary Column:\n")
print(df["Salary"])

# -----------------------------
# 4. Filtering Data
# -----------------------------
high_salary = df[df["Salary"] > 50000]

print("\n✅ Employees with Salary > 50000:\n")
print(high_salary)

# -----------------------------
# 5. Add New Column
# -----------------------------
df["Bonus"] = df["Salary"] * 0.10

print("\n✅ Added Bonus Column:\n")
print(df)

# -----------------------------
# 6. GroupBy Example
# -----------------------------
dept_avg_salary = df.groupby("Department")["Salary"].mean()

print("\n✅ Average Salary by Department:\n")
print(dept_avg_salary)

# -----------------------------
# 7. Sorting Data
# -----------------------------
sorted_df = df.sort_values(by="Salary", ascending=False)

print("\n✅ Sorted by Salary (Descending):\n")
print(sorted_df)

# -----------------------------
# 8. Handling Missing Values
# -----------------------------
df.loc[2, "Salary"] = None  # Introduce missing value

print("\n✅ DataFrame with Missing Value:\n")
print(df)

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print("\n✅ Missing Salary Filled with Mean:\n")
print(df)
