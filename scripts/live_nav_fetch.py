import requests
import pandas as pd

# API URL
url = "https://api.mfapi.in/mf/125497"

# Send request
response = requests.get(url)

print("Status Code:", response.status_code)

# Convert response to JSON
data = response.json()

# Display fund information
print("\nFund Name:", data["meta"]["scheme_name"])
print("Fund House:", data["meta"]["fund_house"])
print("Latest NAV:", data["data"][0])

# Convert NAV history into DataFrame
df = pd.DataFrame(data["data"])

# Save CSV
df.to_csv("data/raw/live_nav_125497.csv", index=False)

print("\nCSV saved successfully!")