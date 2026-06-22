import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("unique Fund houses:")
print(fund_master["fund_house"].unique())

print("\ncategories:")
print(fund_master["category"].unique())

print("\nsubcategories:")
print(fund_master["sub_category"].unique())

print("\nrisk_categories:")
print(fund_master["risk_category"].unique())