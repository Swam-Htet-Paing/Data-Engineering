import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("student_data_dirty.csv", encoding="utf-8")
# print(df.head(3))
# print(df.tail())
# print(df.shape)
# print("Number of rows: ", df.shape[0])
# print("Number of columns: ", df.shape[1])

# print(df.columns)
# print(df.info())
# print(df.describe())

# print(df[["Name", "Score", "Class"]])
# print(df[df["Score"] >= "8"])

# print(df.isnull())
# print(df.isnull().sum())
# print(df.isnull().sum().sum())

# print(df.duplicated())

# print(df["Gender"].unique())
# print(df["City"].unique())
# print(df["Score"].max())
# print(df["Age"].min())
# print(df["Attendance"].max())

df_clean = df.copy()

df_clean["Name"] = df_clean["Name"].str.strip()
df_clean["City"] = df_clean["City"].str.strip()

df_clean["Gender"] = df_clean["Gender"].replace({
  "M": "Male",
  "F": "Female"
})

print(df_clean["Gender"])

df_clean["Score"] = pd.to_numeric(
  df_clean["Score"],
  errors="coerce"
)

df_clean.loc[
  (df_clean["Age"] < 16) |
  (df_clean["Age"] > 100),
  "Age"
] = np.nan
print(df_clean["Age"])

df_clean.loc[
  (df_clean["Score"] < 0) |
  (df_clean["Score"] > 10),
  "Score"
] = np.nan
print(df_clean["Score"])

df_clean.loc[
  (df_clean["Attendance"] < 0) |
  (df_clean["Attendance"] > 100),
  "Attendance"
] = np.nan
print(df_clean["Attendance"])

print(df_clean.isnull().sum())
df_clean["Age"] = df_clean["Age"].fillna(
  df_clean["Age"].median()
)

df_clean["Score"] = df_clean["Score"].fillna(
  df_clean["Score"].median()
)

df_clean["Attendance"] = df_clean["Attendance"].fillna(
  df_clean["Attendance"].median()
)

df_clean["City"] = df_clean["City"].fillna("Unknown")

email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

df_clean["Email"] = df_clean["Email"].astype("string")

valid_email = df_clean["Email"].str.match(
    email_pattern,
    na=False
)
df_clean.loc[~valid_email, "Email"] = pd.NA

df_clean = df_clean.drop_duplicates(
    subset=[
        "Name",
        "Age",
        "Class",
        "Score",
        "Attendance",
        "Email",
        "City"
    ],
    keep="first"
)

df_clean = df_clean.reset_index(drop=True)
print(df_clean)

average_score = df_clean["Score"].mean()
highest_score = df_clean["Score"].max()
lowest_score = df_clean["Score"].min()

print(f"avg score: {average_score}")
print(f"highest score: {highest_score}")
print(f"lowest score: {lowest_score}")

sorted_students = df_clean.sort_values(
  by="Score",
  ascending=False
)
print(sorted_students)

class_average = df_clean.groupby("Class")["Score"].mean()

class_average.plot(
    kind="bar",
    title="Average Score by Class",
    xlabel="Class",
    ylabel="Average Score"
)

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

df_clean.to_csv(
    "student_data_cleaned.csv",
    index=False,
    encoding="utf-8"
)