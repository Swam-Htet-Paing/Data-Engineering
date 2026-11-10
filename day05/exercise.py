import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Exercise 1
df = pd.read_csv("online_store_orders_dirty.csv", encoding="utf-8")
print(df.head())
print(df.tail(10))
print(df.shape[0])
print(df.shape[1])
print(df.columns)
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Exercise 2
print(df.isnull().sum())
print(df.duplicated())
print(df["Product"].unique())
print(df["City"].unique())
print(df[df["Quantity"] <= "0"])
print(df[df["Unit_Price"] < 0.0])
print(df[df["Status"] == "Completed"])

# Exercise 3
df_clean = df.copy()
df_clean["Product"] = df_clean["Product"].str.strip()
df_clean["City"] = df_clean["City"].str.strip()
df_clean["City"] = df_clean["City"].str.title()

df_clean["Status"] = df_clean["Status"].replace({
  "complete": "Completed"
})

df_clean["Quantity"] = pd.to_numeric(
  df_clean["Quantity"],
  errors="coerce"
)

df_clean.loc[
  df_clean["Quantity"] < 0,
  "Quantity"
] = np.nan

df_clean.loc[
  df_clean["Unit_Price"] < 0,
  "Unit_Price"
] = np.nan

df_clean["Quantity"] = df_clean["Quantity"].fillna(0) # it's safe to assume a product quantity is 0 if we don't know the exact number
df_clean["City"] = df_clean["City"].fillna("Unknown") # we shouldn't assign random City names to a record, that would be false information
df_clean = df_clean.drop_duplicates(
    subset=[
      "Order_ID",	
      "Order_Date",	
      "Product",
      "Category",	
      "Quantity",	
      "Unit_Price",	
      "City",
      "Status"
    ],
    keep="first"
)

# Exercise 4
df_clean["Total_Amount"] = df_clean["Quantity"] * df_clean["Unit_Price"]
completed_revenue = df_clean.loc[df_clean["Status"] == "Completed", "Total_Amount"].sum()
print(f"Total Revenue from Completed Orders: ${completed_revenue:,.2f}")

product_revenue = df_clean.loc[df_clean["Status"] == "Completed"].groupby("Product")["Total_Amount"].sum()
highest_prod = product_revenue.idxmax()
lowest_prod = product_revenue.idxmin()
print(f"Highest Revenue Product: {highest_prod} (${product_revenue[highest_prod]:,.2f})")
print(f"Lowest Revenue Product: {lowest_prod} (${product_revenue[lowest_prod]:,.2f})")

units_sold = df_clean.loc[df_clean["Status"] == "Completed"].groupby("Product")["Quantity"].sum()
print("\nTotal Units Sold per Product:\n", units_sold)

cat_summary = df_clean.loc[df_clean["Status"] == "Completed"].groupby("Category").agg(
    Total_Revenue=("Total_Amount", "sum"),
    Order_Count=("Order_ID", "count")
)
best_category = cat_summary["Total_Revenue"].idxmax()
print("\nCategory Summary:\n", cat_summary)
print(f"Best-Performing Category: {best_category}")

city_revenue = df_clean.loc[df_clean["Status"] == "Completed"].groupby("City")["Total_Amount"].sum()
highest_city = city_revenue.idxmax()
print("\nCity Revenue:\n", city_revenue)
print(f"City with Highest Revenue: {highest_city}")

status_counts = df_clean["Status"].value_counts()
print("\nOrder Status Counts:\n", status_counts)


# Exercise 5
prod_rev = df_clean.loc[df_clean["Status"] == "Completed"].groupby("Product")["Total_Amount"].sum()
plt.figure(figsize=(10, 5))
prod_rev.plot(kind="bar", color="skyblue")
plt.title("Total Revenue by Product (Completed Orders)")
plt.xlabel("Product")
plt.ylabel("Total Revenue ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("revenue_by_product.png")
plt.close()

city_rev = df_clean.loc[df_clean["Status"] == "Completed"].groupby("City")["Total_Amount"].sum()
plt.figure(figsize=(8, 5))
city_rev.plot(kind="bar", color="salmon")
plt.title("Total Revenue by City (Completed Orders)")
plt.xlabel("City")
plt.ylabel("Total Revenue ($)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("revenue_by_city.png")
plt.close()

status_dist = df_clean["Status"].value_counts()
plt.figure(figsize=(6, 6))
status_dist.plot(kind="pie", autopct="%1.1f%%", startangle=90, colors=["#66b3ff","#99ff99","#ffcc99","#ff9999"])
plt.title("Distribution of Order Statuses")
plt.ylabel("")
plt.tight_layout()
plt.savefig("order_status_distribution.png")
plt.close()


# Exercise 6
df_clean.to_csv("online_store_orders_cleaned.csv", index=False, encoding="utf-8")

sales_report = df_clean.loc[df_clean["Status"] == "Completed"].groupby(["Category", "Product"]).agg(
    Total_Units_Sold=("Quantity", "sum"),
    Total_Revenue=("Total_Amount", "sum")
).reset_index()
sales_report.to_csv("online_store_sales_report.csv", index=False, encoding="utf-8")

df_reopened_clean = pd.read_csv("online_store_orders_cleaned.csv")
df_reopened_report = pd.read_csv("online_store_sales_report.csv")

print("\n--- Verification ---")
print("Cleaned Dataset Shape:", df_reopened_clean.shape)
print("Sales Report Shape:", df_reopened_report.shape)