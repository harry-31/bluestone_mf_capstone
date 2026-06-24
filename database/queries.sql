SELECT 
scheme _name,
aum_crore
FROM fact_performence
ORDER BY aum_crore DESC
LIMIT 5;

SELECT
amfi_code,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

SELECT 
amfi_code,
return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

SELECT 
transaction_type,
SUM(amount_inr)
FROM fact_transactions
GROUP BY transaction_type;

SELECT
amfi_code,
COUNT(DISTINCT investor_id)
FROM fact_transtions
GROUP BY amfi_code;

SELECT 
AVG(expense_ratio_pct)
FROM fact_performance;

SELECT
amfi_code,
sharpe_ratio
FROM fact_performance 
ORDER BY sharpe_ratio DESC;

SELECT 
risk_grade,
COUNT(*)
FROM fact_performance
GROUP BY risk_grade;

SELECT
strftime('%m',data)AS MONTH,
AVG(nav)
FROM fact_nav
GROUP BY MONTH;

SELECT 
CATEGORY,
COUNT(*)
FROM dim_fund
GROUP BY category;