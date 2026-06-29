import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

print("=" * 60)
print("VERIFYING SQLITE DATABASE")
print("=" * 60)



tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance",
    "fact_aum",
    "monthly_sip_inflows",
    "category_inflows",
    "industry_folio_count",
    "portfolio_holdings",
    "benchmark_indices"
]


for table in tables:
    count = pd.read_sql(f"SELECT COUNT(*) AS total FROM {table}", engine)
    print(f"{table}:")
    print(count)
    print("-" * 40)