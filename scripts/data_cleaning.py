import pandas as pd 
import os

nav_df = pd.read_csv("data/raw/02_nav_history.csv")

print("before cleaning:", nav_df.info())

nav_df["date"] = pd.to_datetime(nav_df["date"])
nav_df = nav_df.sort_values(by = ['amfi_code', 'date'])
nav_df = nav_df.drop_duplicates()
nav_df = nav_df[nav_df["nav"]>0]

os.makedirs("data/processed", exist_ok=True)
nav_df.to_csv("data/processed/02_nav_history_cleaned.csv", index=False)
print("\nafter cleaning:", nav_df.info())

print("NAV history cleaned successfully")

transactions = pd.read_csv("data/raw/08_investor_transactions.csv")
print("\n Transactions before cleaning:", transactions.info())

transactions["transaction_date"]= pd.to_datetime(transactions["transaction_date"])
transactions = transactions. drop_duplicates()
transactions["transaction_type"] = (transactions["transaction_type"].str.strip())
transactions = transactions[transactions["transaction_type"].isin(["SIP", "Lumpsum","Redemption"])]
transactions = transactions[transactions["amount_inr"]>0]
transactions["kyc_status"] = (transactions["kyc_status"].str.strip())
transactions.to_csv("data/processed/08_investor_transactions_cleaned.csv", index=False)

print("\n transactions after cleaning:", transactions.info())
print("transactions cleaned successfully!")
 
performance = pd.read_csv("data/raw/07_scheme_performance.csv")
print("\nperformance before cleaning:", performance.info())
performance = performance.drop_duplicates()
return_columns = ["return_1yr_pct", "return_3yr_pct", "return_5yr_pct"]

for col in return_columns:
    performance[col] = pd.to_numeric(performance[col],errors="coerce")
    performance = performance.dropna(subset = return_columns)
    performance = performance[(performance["expense_ratio_pct"]>= 0.1) & (performance["expense_ratio_pct"]<= 2.5)]
    performance.to_csv("data/processed/07_scheme_performance_cleaned.csv", index=False)

print("\n performance after cleaning:", performance.info())
print("performance cleaned successfully!")  
