import pandas as pd

# Load dataset
df = pd.read_csv("social_media_data.csv")

# Preview data
print("First 5 rows:")
print(df.head())

# Basic info
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Example Engagement Calculation
# (Modify column names based on your dataset)

df["engagement"] = df["likes"] + df["retweets"] + df["replies"]

print("\nEngagement Stats:")
print(df["engagement"].describe())

# Most engaging posts
top_posts = df.sort_values(by="engagement", ascending=False)

print("\nTop 5 Engaging Posts:")
print(top_posts.head())

# Average metrics
print("\nAverage Metrics:")
print(df[["likes", "retweets", "replies"]].mean())
