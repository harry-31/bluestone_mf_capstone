from matplotlib.pylab import rint
import pandas as pd 

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

nav_history = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = fund_master["amfi_code"]

nav_codes = nav_history["amfi_code"]

missing_codes = []
for code in fund_codes:
    if code not in list(nav_codes):
        missing_codes.append(code)

print("total fund master codes:" + str(len(fund_codes)))
print("total nav history codes:" + str(len(nav_codes.unique())))

print("missingcodes:")
if len(missing_codes) == 0:
    print("All AMFI codes are present")
 
else:
    print(missing_codes)