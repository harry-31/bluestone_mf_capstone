CREATE TABLE dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    plan TEXT,
);

CREATE TABLE dim_date (
    date TEXT PRIMARY KEY,
    year INTEGER,
    month INTEGER,
    day INTEGER,
);

CREATE TABLE fact_nav(
    amfi_code INTEGER,
    date TEXT,
    nav REAL,
    
    FOREIGN KEY (amfi_code)
    REFERENCES dim_fund(amfi_code),

    FOREIGN KEY (date)
    REFERENCES dim_date(date)
);

CREATE TABLE fact_transactions(
    investor_iD TEXT,
    transaction_date TEXT,
    amfi_code INTEGER,
    transaction_type TEXT,
    amount_inr REAL,

    FOREIGN KEY (amfi_code)
    REFERENCES dim_fund(amfi_code),
);

CREATE TABLE fact_performance(
    amfi_code INTEGER,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    alpha REAL,
    beta REAL,
    sharpe_ratio REAL,

    FOREIGN KEY (amfi_code)
    REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_aum(
    amfi_code INTEGER,
    aum_inr REAL,

    FOREIGN KEY (amfi_code)
    REFERENCES dim_fund(amfi_code)
);

