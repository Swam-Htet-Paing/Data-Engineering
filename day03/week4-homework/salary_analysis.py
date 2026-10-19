import pandas as pd

df = pd.read_csv('employees.csv')
print(df.head())
print(df.tail())
print(df.shape)

print(df.isnull().sum())
avg_salary = df.groupby('Department')['Salary'].transform('mean')
df['Salary'] = df['Salary'].fillna(avg_salary)
df['Experience'] = df['Experience'].fillna(0)

print(df["Salary"].mean())
print(df["Salary"].max())
print(df["Salary"].min())
print(df.sort_values("Salary", ascending=True).iloc[0])
print(df[df["Salary"] > 1000])
print(df.groupby('Department')['Salary'].mean())

df.to_csv("employees_processed.csv", index=False)
