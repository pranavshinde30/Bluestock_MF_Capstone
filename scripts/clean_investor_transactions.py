import pandas as pd

print("=" * 60)
print("CLEANING INVESTOR TRANSACTIONS DATASET")
print("=" * 60)

# Load dataset
df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("\nFirst 5 Rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nUnique Transaction Types:")
print(df["transaction_type"].unique())

print("\nUnique KYC Status:")
print(df["kyc_status"].unique())

print("\n" + "=" * 60)
print("AMOUNT VALIDATION")
print("=" * 60)

invalid_amount = (df["amount_inr"] <= 0).sum()

print("Invalid Amounts (<=0):", invalid_amount)

if invalid_amount > 0:
    print("Warning: Invalid transaction amounts found.")
else:
    print("All transaction amounts are valid.")

print("\n" + "=" * 60)
print("DATE CONVERSION")
print("=" * 60)

df["transaction_date"] = pd.to_datetime(df["transaction_date"])

print(df["transaction_date"].dtype)

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

print(df.isnull().sum())

print("\n" + "=" * 60)
print("DUPLICATE ROWS")
print("=" * 60)

duplicates = df.duplicated().sum()

print("Duplicate Rows:", duplicates)

if duplicates > 0:
    df = df.drop_duplicates()
    print("Duplicates removed.")
else:
    print("No duplicate rows found.")

output_path = "data/processed/investor_transactions_cleaned.csv"

df.to_csv(output_path, index=False)

print("\nCleaned file saved successfully!")
print(output_path)