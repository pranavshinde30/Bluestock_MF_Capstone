# Mutual Fund Analytics - Data Dictionary

## Project
Bluestock Capstone Project I

---

# Table: dim_fund

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Unique AMFI Scheme Code |
| fund_house | TEXT | Mutual Fund Company |
| scheme_name | TEXT | Name of the Scheme |
| category | TEXT | Fund Category |
| sub_category | TEXT | Sub Category |
| plan | TEXT | Direct / Regular Plan |
| launch_date | DATE | Scheme Launch Date |
| benchmark | TEXT | Benchmark Index |
| expense_ratio_pct | REAL | Expense Ratio (%) |
| exit_load_pct | REAL | Exit Load (%) |
| min_sip_amount | INTEGER | Minimum SIP Amount |
| min_lumpsum_amount | INTEGER | Minimum Lumpsum Amount |
| fund_manager | TEXT | Fund Manager Name |
| risk_category | TEXT | Risk Category |
| sebi_category_code | TEXT | SEBI Category Code |

Source:
01_fund_master.csv

---

# Table: fact_nav

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | AMFI Scheme Code |
| date | DATE | NAV Date |
| nav | REAL | Net Asset Value |

Source:
02_nav_history.csv

---

# Table: fact_transactions

| Column | Data Type | Description |
|---------|-----------|-------------|
| investor_id | TEXT | Investor ID |
| transaction_date | DATE | Transaction Date |
| amfi_code | INTEGER | Scheme Code |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | INTEGER | Transaction Amount |
| state | TEXT | Investor State |
| city | TEXT | Investor City |
| city_tier | TEXT | Tier Classification |
| age_group | TEXT | Investor Age Group |
| gender | TEXT | Gender |
| annual_income_lakh | REAL | Annual Income (Lakhs) |
| payment_mode | TEXT | Payment Mode |
| kyc_status | TEXT | KYC Verification Status |

Source:
08_investor_transactions.csv

---

# Table: fact_performance

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Scheme Code |
| scheme_name | TEXT | Scheme Name |
| fund_house | TEXT | Fund House |
| category | TEXT | Category |
| return_1yr_pct | REAL | 1-Year Return (%) |
| return_3yr_pct | REAL | 3-Year Return (%) |
| return_5yr_pct | REAL | 5-Year Return (%) |
| benchmark_3yr_pct | REAL | Benchmark Return |
| alpha | REAL | Alpha |
| beta | REAL | Beta |
| sharpe_ratio | REAL | Sharpe Ratio |
| sortino_ratio | REAL | Sortino Ratio |
| std_dev_ann_pct | REAL | Standard Deviation |
| max_drawdown_pct | REAL | Maximum Drawdown |
| aum_crore | INTEGER | Assets Under Management |
| expense_ratio_pct | REAL | Expense Ratio |
| morningstar_rating | INTEGER | Morningstar Rating |
| risk_grade | TEXT | Risk Grade |

Source:
07_scheme_performance.csv

---

# Table: fact_aum

| Column | Data Type | Description |
|---------|-----------|-------------|
| date | DATE | Reporting Date |
| fund_house | TEXT | Fund House |
| aum_lakh_crore | REAL | AUM (Lakh Crore) |
| aum_crore | REAL | AUM (Crore) |
| num_schemes | INTEGER | Number of Schemes |

Source:
03_aum_by_fund_house.csv

---

# Additional Tables

- monthly_sip_inflows → 04_monthly_sip_inflows.csv
- category_inflows → 05_category_inflows.csv
- industry_folio_count → 06_industry_folio_count.csv
- portfolio_holdings → 09_portfolio_holdings.csv
- benchmark_indices → 10_benchmark_indices.csv