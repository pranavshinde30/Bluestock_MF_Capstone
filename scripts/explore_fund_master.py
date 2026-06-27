import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 60)
print("FUND MASTER EXPLORATION")
print("=" * 60)

# Dataset Information
print("\nTotal Schemes:", len(df))

# Fund Houses
print("\nUnique Fund Houses:")
print(df["fund_house"].unique())

print("\nNumber of Fund Houses:", df["fund_house"].nunique())

# Categories
print("\nUnique Categories:")
print(df["category"].unique())

print("\nNumber of Categories:", df["category"].nunique())

# Sub Categories
print("\nUnique Sub Categories:")
print(df["sub_category"].unique())

print("\nNumber of Sub Categories:", df["sub_category"].nunique())

# Risk Grades
print("\nRisk Categories:")
print(df["risk_category"].unique())

print("\nNumber of Risk Categories:", df["risk_category"].nunique())

# AMFI Codes
print("\nSample AMFI Codes:")
print(df["amfi_code"].head(10).tolist())