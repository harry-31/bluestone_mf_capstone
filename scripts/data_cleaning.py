import pandas as pd 
import os
#==============NAV HISTORY CLEANING===============
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

#============INVESTOR TRANSACTIONS CLEANING========================
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

#=================SCHEME PERFORMANCE CLEANING================== 
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

#====================AUM CLEANNG====================
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

print("\nAUM before cleaning:",aum.info())

aum["date"] = pd.to_datetime(aum["date"])
aum = aum.drop_duplicates()
aum = aum[(aum["aum_crore"]>0)&(aum["aum_lakh_crore"]>0)]
aum["fund_house"] = aum["fund_house"].str.strip()
aum.to_csv("data/processed/03_aum_by_fund_house_cleaned.csv", index=False)

print("\nAUM after cleaning:",aum.info())

#===========MONTHLY SIP CLEANING=========================
sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

print("\nSIP before cleaning:",sip.info())

sip["month"] = pd.to_datetime(sip["month"])
sip = sip.drop_duplicates()
sip = sip[sip["sip_inflow_crore"]>0]
sip = sip[sip["sip_aum_lakh_crore"]>0]

sip.to_csv("data/processed/04_monthly_sip_inflows_cleaned.csv", index=False)

print("\nSIP after cleaning:",sip.info())
print("SIP dataset cleaned successfully!")

#===============CATEGORY IN FLOWS CLEANING================
category = pd.read_csv("data/raw/05_category_inflows.csv")

print("\ncategory before cleaning:",category.info())

category["month"] = pd.to_datetime(category["month"])
category["category"] = category["category"].str.strip()
category = category.drop_duplicates()
category = category[category["net_inflow_crore"]>=0]
category.to_csv("data/processed/05_category_inflows_cleaned.csv",index=False)

print("\ncategory after cleaning:",category.info())
print("category inflows clean successfully!")

#=================INDUSTRY FOLIO COUNT CLEANING================ 
folio = pd.read_csv("data/raw/06_industry_folio_count.csv")

print("\nfolio before cleaning:",folio.info())

folio["month"] = pd.to_datetime(folio["month"])
folio = folio.drop_duplicates()
folio = folio[folio["total_folios_crore"]>0]
folio.to_csv("data/processed/06_industry_folio_count_cleaned.csv",index=False)

print("\nFolio after cleaning:",folio.info())
print("indusrty folio count cleaned successfully!")

#==================PORTFOLIOS HOLDINGS CLEANING============
holdings = pd.read_csv("data/raw/09_portfolio_holdings.csv")

print("\nProtfolio holdings before cleaning:",holdings.info())

holdings["portfolio_date"] = pd.to_datetime(holdings["portfolio_date"])
holdings = holdings.drop_duplicates()
text_columns = holdings.select_dtypes(include="object").columns

for col in text_columns:
    holdings[col] = holdings[col].str.strip()

holdings = holdings.dropna()
holdings = holdings[(holdings["weight_pct"] > 0) &(holdings["market_value_cr"] > 0) &(holdings["current_price_inr"] > 0)]
holdings.to_csv("data/processed/09_portfolio_holdings_cleaned.csv",index=False)

print("portfolio holdiings after cleaning:",holdings.info())
print("portfolio holdings cleaned succesfully!")

#==================FUND MASTER CLEANING==================
fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("\nFund Master before cleaning:")
print(fund_master.info())

fund_master = fund_master.drop_duplicates()

text_columns = fund_master.select_dtypes(include="object").columns
for col in text_columns:
    fund_master[col] = fund_master[col].str.strip()

fund_master = fund_master.dropna(how="all")

fund_master.to_csv(
    "data/processed/01_fund_master_cleaned.csv",
    index=False
)

print("\nFund Master after cleaning:")
print(fund_master.info())
print("Fund Master cleaned successfully!")