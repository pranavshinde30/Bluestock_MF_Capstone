import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Get unique AMFI codes
fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

print("=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

print("\nTotal AMFI Codes in Fund Master :", len(fund_codes))
print("Total AMFI Codes in NAV History :", len(nav_codes))

# Find missing codes
missing_codes = fund_codes - nav_codes

if len(missing_codes) == 0:
    print("\n✅ Excellent!")
    print("Every AMFI Code in fund_master exists in nav_history.")
else:
    print("\n❌ Missing Codes Found:")
    print(missing_codes)

print("\nValidation Completed.")