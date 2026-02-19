import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Marks": [85, 92, 78, 88]
}

df = pd.DataFrame(data)

sorted_df = df.sort_values(by="Marks", ascending=False)

print("Sorted by Marks (Highest First):\n")
print(sorted_df)
