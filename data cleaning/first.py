import pandas as pd

data = pd.read_csv("employee_data.csv")
print("Original Data:\n", data.head())

avg_age = data["Age"].mean()
avg_salary = data["Salary"].mean()
data["Age"] = data["Age"].apply(lambda x: avg_age if pd.isnull(x) else x)
data["Salary"] = data["Salary"].apply(lambda x: avg_salary if pd.isnull(x) else x)

departments = {"Human Resources": "HR", "H.R.": "HR", "hr": "HR"}
data["Department"] = data["Department"].replace(departments)

data = data.drop_duplicates("ID")

print("\nUpdated Data:\n", data.head())
