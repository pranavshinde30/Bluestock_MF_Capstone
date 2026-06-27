from pathlib import Path
import pandas as pd

# Project root folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Path to raw data
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"

print("=" * 60)
print("BLUESTOCK MUTUAL FUND DATA INGESTION")
print("=" * 60)

# Find all CSV files
csv_files = sorted(RAW_DATA_PATH.glob("*.csv"))

print(f"\nFound {len(csv_files)} CSV files.\n")

# Loop through each CSV
for file in csv_files:
    print("=" * 60)
    print(f"Reading: {file.name}")

    try:
        df = pd.read_csv(file)

        print(f"\nShape: {df.shape}")

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

    except Exception as e:
        print(f"Error reading {file.name}")
        print(e)

print("\nData ingestion completed successfully.")