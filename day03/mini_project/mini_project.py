import pandas as pd

df = pd.read_csv("students.csv")

print(df.head())
print(df.isnull())
print(df["Score"].mean())
print(df.sort_values("Score", ascending=False).iloc[0])
print(df[df["Score"] >= 5.0])
print(df.groupby("Class")["Score"].mean())

df.to_csv("students_processed.csv", index=False)

