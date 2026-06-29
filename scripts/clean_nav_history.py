import pandas as pd

print("=" * 60)
print("CLEANING NAV HISTORY DATASET")
print("=" * 60)

# Load dataset
df = pd.read_csv("data/raw/02_nav_history.csv")

print("\nOriginal Dataset")
print(df.head())

print("\nOriginal Shape:")
print(df.shape)

print("\nOriginal Data Types:")
print(df.dtypes)

# --------------------------------------------------
# Step 1 : Convert Date
# --------------------------------------------------
df["date"] = pd.to_datetime(df["date"])

# --------------------------------------------------
# Step 2 : Sort Data
# --------------------------------------------------
df = df.sort_values(by=["amfi_code", "date"])

# --------------------------------------------------
# Step 3 : Check Missing NAV
# --------------------------------------------------
missing_nav = df["nav"].isna().sum()

print("\nMissing NAV Values:", missing_nav)

if missing_nav > 0:
    df["nav"] = df.groupby("amfi_code")["nav"].ffill()
    print("Missing NAV values forward-filled.")
else:
    print("No missing NAV values found. Forward fill not required.")

# --------------------------------------------------
# Step 4 : Remove Duplicates
# --------------------------------------------------
duplicates = df.duplicated().sum()

print("\nDuplicate Rows:", duplicates)

if duplicates > 0:
    df = df.drop_duplicates()
    print("Duplicate rows removed.")
else:
    print("No duplicate rows found.")

# --------------------------------------------------
# Step 5 : Validate NAV
# --------------------------------------------------
invalid_nav = (df["nav"] <= 0).sum()

print("\nInvalid NAV Values (<=0):", invalid_nav)

if invalid_nav > 0:
    print("Warning: Invalid NAV values detected.")
else:
    print("All NAV values are valid.")

# --------------------------------------------------
# Step 6 : Save Cleaned Dataset
# --------------------------------------------------
output_path = "data/processed/nav_history_cleaned.csv"

df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully.")
print("Location:", output_path)

# --------------------------------------------------
# Final Summary
# --------------------------------------------------
print("\n" + "=" * 60)
print("DATA CLEANING SUMMARY")
print("=" * 60)

print(f"Rows                : {len(df)}")
print(f"Columns             : {len(df.columns)}")
print(f"Missing NAV         : {missing_nav}")
print(f"Duplicate Rows      : {duplicates}")
print(f"Invalid NAV         : {invalid_nav}")

print("\nFinal Data Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())

print("\nNAV History Cleaning Completed Successfully.")
print("=" * 60)