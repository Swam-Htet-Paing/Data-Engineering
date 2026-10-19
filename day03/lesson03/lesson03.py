import pandas as pd

# print(pd.__version__)
# scores = pd.Series([8.5, 7.0, 9.0, 6.5, 10.0])
# print(scores)
# print(scores[0])
# print(scores[2])

data = {
  "Name" : ["John", "Anna", "Peter", "Mary", "David"],
  "Age" : [20, 21, 20, 22, 21],
  "Score" : [8.5, 7.0, 9.0, 6.5, 7.5]
}

# df = pd.DataFrame(data)
# print(df)
# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
# print(df.info())
# print(df.describe())

df = pd.read_csv("students.csv")

# columns
# print(df["Name"])
# print(df[["Name", "Score"]])

# rows
# print(df.iloc[0])
# print(df.loc[0:3])

# filtering
# high_scores = df[df["Score"] >= 8]
# print(high_scores)

print(df[df["Score"] < 7])
print(df[df["Class"] == "A"])
result = df[(df["Class"] == "A") & (df["Score"] >= 8)]
print(result)

# Basic statistics, grouping
print("Average: ", df["Score"].mean())
print("Maximum: ", df["Score"].max())
print("Minimum: ", df["Score"].min())
print("Total: ", df["Score"].sum())
print("Count: ", df["Score"].count())
print(df.groupby("Class")["Score"].mean())

# Sorting
df_sorted = df.sort_values("Score", ascending=False)
print(df_sorted)

# exporting data
df.to_csv("students_output.csv", index=False)