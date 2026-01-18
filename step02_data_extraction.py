"""
Sample 1: Data Extraction
Fetches historical candle data for a specific instrument and saves it to CSV.
"""
from datetime import datetime, timedelta
import pandas as pd
from step00_auth import KiteAuth
import os

def fetch_data():
    print("🚀 Starting Data Extraction...")
    
    # 1. Login
    auth = KiteAuth()
    kite = auth.login()
    
    # 2. Define Parameters
    instrument_token = 256265  # NIFTY 50 (Example Token)
    from_date = datetime.now() - timedelta(days=5)
    to_date = datetime.now()
    interval = "5minute"
    
    print(f"📥 Fetching data for Token {instrument_token}...")
    print(f"📅 Period: {from_date.date()} to {to_date.date()}")
    
    try:
        # 3. Fetch Historical Data
        data = kite.historical_data(
            instrument_token, 
            from_date, 
            to_date, 
            interval
        )
        
        # 4. Convert to DataFrame
        df = pd.DataFrame(data)
        
        if not df.empty:
            print(f"✅ Fetched {len(df)} records.")
            
            # Save to CSV
            filename = "nifty_5min_data.csv"
            df.to_csv(filename, index=False)
            print(f"💾 Saved to {filename}")
            
            print("\nSample Data:")
            print(df.head())
        else:
            print("⚠️ No data found.")
            
    except Exception as e:
        print(f"❌ Error fetching data: {e}")

if __name__ == "__main__":
    fetch_data()
