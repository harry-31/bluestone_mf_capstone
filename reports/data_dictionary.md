# Mutual Fund Analytics Platform - Data Dictionary

## 1. dim_fund

Stores basic information about mutual fund schemes.

Column Name |  Description 
->amfi_code - Unique code assign to each mutual code
->scheme_name - Complete name of the mutual fund scheme
->fund_house - Company managing the mutual fund
->category - Type of the fund
->plan - Direct or regular plan details

## 2. dim_date

This table helps in performing date based analysis.

Column Name     |    Description
->date - Date on which NAV was recorded
->year - Year extracted from the data 
->month - Month extracted from date
->day - Day extracted from the date 

## 3. fact_nav

These table stores daily NAV fund of mutual funds

Column Name     |     Description
->amfi_code - code use to identify the fund
->date - Date of NAV entry \
->nav - Net asset value of the mutual fund

## 4. fact_transactions

This table stores investor transaction information 

Column Name     |   Description 
->investor_id - Unique id od the investor 
->transaction_date - Date when the transaction happened
->amfi_code - Mutual fund involve in transaction
->transacion_type - Type of transaction (SIP,Lumpsum,Redemption)
->amount_inr - Transaction amount in INR

## 5. fact_performance

This table stores the performance related information od funds.

Column Name   |  Description
->amfi_code - Unique fund code 
-> return_1yr_pct - Fund return in last 1 year 
-> return_3yr_pct - Fund return in last 3 years 
-> return_5yr_pct - Fund return in last 5 years 
-> alpha - Measures fund performance compared to benchmark 
-> beta - Shows fund risk compared to market 
-> sharpe_ratio - Measures return based on risk taken 
-> expense_ratio_pct - Percentage charged for managing the fund 
-> aum_crore - Total assets managed by the fund 

## 6. Data cleaning performed :
->Converted date columns into proper date format.
->Removed duplcate records. 
->Checked and handle missing data.
->Validated NAV values .
->Verified transactions type like SIP,Lumpsun,Redemption.
->Removed invalid transactions amount.
->Checked expense ratio range.
->Stored final cleaned data into SQLite database.

## 7. FINAL OUTPUT 
The cleaned datasetsare stored inside "data/processed" folder and the final SQLite database is available as "bluestock_mf.db".