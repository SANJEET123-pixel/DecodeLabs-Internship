import pandas as pd
df = pd.read_csv("DecodeLabs_Project1_raw_dataset.csv")
print(df.head())
print("\nDataset Shape: ",df.shape)
print("\nDataset Names: ",df.columns)
print("\nDataset Datatypes: ",df.dtypes)
print("\nDataset Information: ",df.info())
print("\nRows containing missing values: ")
print(df[df.isnull().any(axis=1)])
print("\nDataset Null Values: ",df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())
df["City"] = df["City"].fillna("Unknown")
df["Email"] = df["Email"].fillna("Unknown")

print("\nMissing values after cleaning: ")
print(df.isnull().sum())

print("\nDuplicate Customer IDs: ")
print(df["Customer_ID"].duplicated().sum())

print("Duplicate ID records: ")
print(df[df["Customer_ID"].duplicated(keep = False)].sort_values("Customer_ID"))
df = df.drop_duplicates(subset ="Customer_ID",keep ="first")

print("\nDuplicate Records After Cleaning: ")
print(df["Customer_ID"].duplicated().sum())

print("\nPurchase Date values:")
print(df["Purchase_Date"].head(20))

df["Purchase_Date"] = pd.to_datetime(
    df["Purchase_Date"],
    errors = "coerce",
    format = "mixed",
    dayfirst = True
)

print("\nInvalid Dates : ")
print(df[df["Purchase_Date"].isna()])

df = df.dropna(subset = ["Purchase_Date"])
print("Invalid Dates After Cleaning: ")
print(df["Purchase_Date"].isna().sum())

df["Purchase_Date"] = df["Purchase_Date"].dt.strftime("%Y-%m-%d")
print("\nCleaned dates:")
print(df["Purchase_Date"].head(10))

print("\nCity values before cleaning:")
print(df["City"].unique())

print("\nProduct values before cleaning:")
print(df["Product"].unique())

df["City"] = df["City"].str.strip().str.title()
df["Product"] = df["Product"].str.strip().str.title()

print("\nCity values after cleaning:")
print(df["City"].unique())

print("\nProduct values after cleaning:")
print(df["Product"].unique())

print("\nData types:")
print(df.dtypes)
print("\nQuantity values:")
print(df["Quantity"].unique())
print("\nPurchase Amount values:")
print(df["Purchase_Amount"].unique())

df["Purchase_Amount"] = (
    df["Purchase_Amount"]
    .astype(str)
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
)

df["Purchase_Amount"] = pd.to_numeric(
    df["Purchase_Amount"],
    errors="coerce"
)

print("\nPurchase Amount data type:")
print(df["Purchase_Amount"].dtype)

print("\nPurchase Amount values:")
print(df["Purchase_Amount"].head(10))



print("\n===FINAL DATA VALIDATION ===")

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate Customer IDs:")
print(df["Customer_ID"].duplicated().sum())

print("\nInvalid dates:")
print(df["Purchase_Date"].isna().sum())

print("\nFinal data types:")
print(df.dtypes)

print("\nFinal dataset shape:")
print(df.shape)


df.to_csv("cleaned_dataset.csv", index=False)

print("\nCleaned dataset saved successfully!")