import requests
import pandas as pd
import time

def fetch_nifty_option_chain():
    url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    session = requests.Session()
    
    try:
        # First request to get cookies
        session.get("https://www.nseindia.com", headers=headers)
        time.sleep(1)  # Small delay to prevent being blocked

        # Fetch option chain data
        response = session.get(url, headers=headers)
        response.raise_for_status()  # Raises an error if request fails

        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None  # Return None if API fails

def process_option_chain(data):
    if not data or 'records' not in data:
        print("Invalid data received")
        return pd.DataFrame()  # Return empty DataFrame

    records = data['records']['data']
    option_data = []

    for record in records:
        strike_price = record.get('strikePrice', 0)
        ce_data = record.get('CE', {})
        pe_data = record.get('PE', {})

        option_data.append({
            "Strike": strike_price,
            "CE_OI": ce_data.get("openInterest", 0),
            "CE_IV": ce_data.get("impliedVolatility", 0),
            "PE_OI": pe_data.get("openInterest", 0),
            "PE_IV": pe_data.get("impliedVolatility", 0)
        })

    df = pd.DataFrame(option_data)
    return df

def main():
    print("Fetching Nifty option chain data...")
    data = fetch_nifty_option_chain()

    if data:
        df = process_option_chain(data)
        df.to_csv("option_chain.csv", index=False)  # Save data to CSV
        print("Option chain data saved to option_chain.csv")

        print("Fetched and Processed Option Chain Data:")
        print(df.head(10))  # Display first 10 rows
    else:
        print("Failed to fetch data. Please try again later.")

if __name__ == "__main__":
    main()
