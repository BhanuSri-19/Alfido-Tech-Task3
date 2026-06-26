import pandas as pd

# Load the CSV dataset
df = pd.read_csv("sample_data.csv")

# Display first five rows
print("Dataset:")
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Clean missing data
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["Age"] = df["Age"].fillna(df["Age"].mean())

print("\nCleaned Dataset:")
print(df)

# Filter employees with salary greater than 55000
high_salary = df[df["Salary"] > 55000]

print("\nEmployees with Salary > 55000:")
print(high_salary)

# Group by Department and calculate average salary
grouped = df.groupby("Department")["Salary"].mean()

print("\nAverage Salary by Department:")
print(grouped)

# Overall statistics
print("\nSummary Statistics:")
print(df.describe())