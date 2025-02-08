import requests
import pandas as pd

# NSE Option Chain URL
nse_url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"

# Headers to mimic a real browser request
headers = {"User-Agent": "Mozilla/5.0"}

def fetch_nifty_option_chain():
    session = requests.Session()
    response = session.get(nse_url, headers=headers)
    data = response.json()
    return data["records"]["data"]

# Fetch option chain data
option_chain = fetch_nifty_option_chain()

# Convert to DataFrame
df = pd.json_normalize(option_chain)

# Select relevant columns
df = df[['CE.strikePrice', 'CE.openInterest', 'CE.impliedVolatility', 
         'PE.strikePrice', 'PE.openInterest', 'PE.impliedVolatility']]
df.columns = ['CE_Strike', 'CE_OI', 'CE_IV', 'PE_Strike', 'PE_OI', 'PE_IV']

# Save to CSV for reference
df.to_csv("option_chain.csv", index=False)

print(df.head(10))
