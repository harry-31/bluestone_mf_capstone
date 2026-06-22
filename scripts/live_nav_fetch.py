from urllib import response

import requests
import pandas as pd 

scheme_code ={
    "SBI Bluechip": 119551,
    "ICICI Bluechip": 120503,
    "Nippon Large Cap": 118632,
    "Axis Bluechip": 119092,
    "Kotak Bluechip": 120841
}

def fetch_nav(scheme_code):

    url=f"https://api.mfapi.in/mf/{scheme_code}"
    response = requests.get(url)
    data = response.json()
    return data

nav_list = []
for fund, code in scheme_code.items():
    data = fetch_nav(code)
    latest = data["data"][0]

    nav_list.append({
        "fund_name": data["meta"]["scheme_name"],
        "date": latest["date"],
        "nav": latest["nav"]
    })

    print(fund,"NAV fetched")

df_nav = pd.DataFrame(nav_list)

df_nav.to_csv("data/raw/five_scheme_nav.csv",index=False)

print("NAV data saved successfully")

