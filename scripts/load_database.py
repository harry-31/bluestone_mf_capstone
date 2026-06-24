import pandas as pd 
import sqlite3
import os

os.makedirs('database', exist_ok=True)

conn = sqlite3.connect("database/bluestock_mf.db")
nav = pd.read_csv("data/processed/02_nav_history_cleaned.csv")
transactions = pd.read_csv("data/processed/08_investor_transactions_cleaned.csv")
performance = pd.read_csv("data/processed/07_scheme_performance_cleaned.csv")

dim_fund = performance[["amfi_code", "scheme_name", "fund_house", "category", "plan"]]

nav["date"]= pd.to_datetime(nav["date"])
   
dim_date = pd.DataFrame()
   
dim_date["date"] =( nav["date"].drop_duplicates().reset_index(drop=True))
dim_date["date"] = pd.to_datetime(dim_date["date"])

dim_date["year"] = dim_date["date"].dt.year
dim_date["month"] = dim_date["date"].dt.month 
dim_date["day"] = dim_date["date"].dt.day

dim_fund.to_sql("dim_fund",conn,if_exists="replace",index=False)
dim_date.to_sql("dim_date",conn,if_exists="replace",index=False)

nav.to_sql("fact_nav",conn,if_exists="replace",index=False)
transactions.to_sql("fact_transactions",conn,if_exists="replace",index=False)
performance.to_sql("fact_performance",conn,if_exists="replace",index=False)

conn.close()
print("SQLite databases loaded succesfully")

