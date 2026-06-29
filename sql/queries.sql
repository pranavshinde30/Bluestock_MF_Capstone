-- =====================================================
-- Query 1 : Top 5 Funds by AUM
-- =====================================================

SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- =====================================================
-- Query 2 : Average NAV Per Month
-- =====================================================

SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav),2) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

-- =====================================================
-- Query 3 : SIP YoY Growth
-- =====================================================

SELECT
    month,
    yoy_growth_pct
FROM monthly_sip_inflows
ORDER BY month;

-- =====================================================
-- Query 4 : Transactions by State
-- =====================================================

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- =====================================================
-- Query 5 : Expense Ratio Below 1%
-- =====================================================

SELECT
    scheme_name,
    fund_house,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- =====================================================
-- Query 6 : Top 10 Funds by 5-Year Return
-- =====================================================

SELECT
    scheme_name,
    fund_house,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- =====================================================
-- Query 7 : Total Investment by Payment Mode
-- =====================================================

SELECT
    payment_mode,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY payment_mode
ORDER BY total_amount DESC;


-- =====================================================
-- Query 8 : Funds by Risk Grade
-- =====================================================

SELECT
    risk_grade,
    COUNT(*) AS total_funds
FROM fact_performance
GROUP BY risk_grade
ORDER BY total_funds DESC;


-- =====================================================
-- Query 9 : Top States by Investment Amount
-- =====================================================

SELECT
    state,
    SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY state
ORDER BY total_investment DESC
LIMIT 10;

-- =====================================================
-- Query 10 : Average Expense Ratio by Fund House
-- =====================================================

SELECT
    fund_house,
    ROUND(AVG(expense_ratio_pct),2) AS average_expense_ratio
FROM fact_performance
GROUP BY fund_house
ORDER BY average_expense_ratio;

