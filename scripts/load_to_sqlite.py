import pandas as pd
from sqlalchemy import create_engine

print("=" * 50)
print("CONNECTED SUCCESSFULLY TO SQLITE DATABASE")
print("=" * 50)

# SQLite database connection
engine = create_engine("sqlite:///bluestock_mf.db")

# -----------------------------
# Load Fund Master
# -----------------------------
fund = pd.read_csv("data/raw/01_fund_master.csv")
fund.to_sql("dim_fund", engine, if_exists="replace", index=False)
print("dim_fund loaded")

# -----------------------------
# Load NAV History
# -----------------------------
nav = pd.read_csv("data/processed/nav_history_cleaned.csv")
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
print("fact_nav loaded")

# -----------------------------
# Load Investor Transactions
# -----------------------------
transactions = pd.read_csv(
    "data/processed/investor_transactions_cleaned.csv"
)
transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)
print("fact_transactions loaded")

# -----------------------------
# Load Scheme Performance
# -----------------------------
performance = pd.read_csv(
    "data/processed/scheme_performance_cleaned.csv"
)
performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)
print("fact_performance loaded")

# -----------------------------
# Load AUM
# -----------------------------
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")
aum.to_sql("fact_aum", engine, if_exists="replace", index=False)
print("fact_aum loaded")


# Load Monthly SIP Inflows
sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")
sip.to_sql(
    "monthly_sip_inflows",
    engine,
    if_exists="replace",
    index=False
)
print("monthly_sip_inflows loaded")


# Load Category Inflows
category = pd.read_csv("data/raw/05_category_inflows.csv")
category.to_sql(
    "category_inflows",
    engine,
    if_exists="replace",
    index=False
)
print("category_inflows loaded")


# Load Industry Folio Count
folio = pd.read_csv("data/raw/06_industry_folio_count.csv")
folio.to_sql(
    "industry_folio_count",
    engine,
    if_exists="replace",
    index=False
)
print("industry_folio_count loaded")


# Load Portfolio Holdings
portfolio = pd.read_csv("data/raw/09_portfolio_holdings.csv")
portfolio.to_sql(
    "portfolio_holdings",
    engine,
    if_exists="replace",
    index=False
)
print("portfolio_holdings loaded")


# Load Benchmark Indices
benchmark = pd.read_csv("data/raw/10_benchmark_indices.csv")
benchmark.to_sql(
    "benchmark_indices",
    engine,
    if_exists="replace",
    index=False
)
print("benchmark_indices loaded")

print("\nAll datasets loaded successfully!")