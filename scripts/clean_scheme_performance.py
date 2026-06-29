import pandas as pd

print("=" * 60)
print("CLEANING SCHEME PERFORMANCE DATASET")
print("=" * 60)

# Load dataset
df = pd.read_csv("data/raw/07_scheme_performance.csv")

# --------------------------------------------------
# Basic Information
# --------------------------------------------------

print("\nFirst 5 Rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

# --------------------------------------------------
# Convert return columns to numeric
# --------------------------------------------------

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "expense_ratio_pct"
]

for col in return_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# --------------------------------------------------
# Missing Values
# --------------------------------------------------

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

print(df[return_columns].isnull().sum())

# --------------------------------------------------
# Expense Ratio Validation
# --------------------------------------------------

print("\n" + "=" * 60)
print("EXPENSE RATIO VALIDATION")
print("=" * 60)

invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print(f"Invalid Expense Ratios: {len(invalid_expense)}")

if len(invalid_expense) > 0:
    print(invalid_expense[["scheme_name", "expense_ratio_pct"]])
else:
    print("All expense ratios are within range.")

# --------------------------------------------------
# Duplicate Rows
# --------------------------------------------------

print("\n" + "=" * 60)
print("DUPLICATE ROWS")
print("=" * 60)

duplicates = df.duplicated().sum()

print("Duplicate Rows:", duplicates)

# --------------------------------------------------
# Save Cleaned File
# --------------------------------------------------

output_path = "data/processed/scheme_performance_cleaned.csv"

df.to_csv(output_path, index=False)

print("\nCleaned file saved successfully!")
print(output_path)