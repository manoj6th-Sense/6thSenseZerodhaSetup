"""
Sample 2: Simple Backtest
Runs a basic Moving Average Crossover strategy on historical data.
"""
from datetime import datetime, timedelta
import pandas as pd
from step00_auth import KiteAuth

def run_backtest():
    print("🚀 Starting Backtest (SMA Crossover)...")
    
    # 1. Login & Get Data
    auth = KiteAuth()
    kite = auth.login()
    
    instrument_token = 256265 # NIFTY 50
    from_date = datetime.now() - timedelta(days=30)
    to_date = datetime.now()
    interval = "15minute"
    
    print("📥 Fetching 30 days of data...")
    data = kite.historical_data(instrument_token, from_date, to_date, interval)
    df = pd.DataFrame(data)
    
    if df.empty:
        print("❌ No data to backtest.")
        return

    # 2. Calculate Indicators
    print("🧮 Calculating Indicators (SMA 9 & 21)...")
    df['SMA_9'] = df['close'].rolling(window=9).mean()
    df['SMA_21'] = df['close'].rolling(window=21).mean()
    
    # 3. Generate Signals
    df['Signal'] = 0
    # Buy when SMA 9 crosses above SMA 21
    df.loc[df['SMA_9'] > df['SMA_21'], 'Signal'] = 1 
    # Sell when SMA 9 crosses below SMA 21
    df.loc[df['SMA_9'] < df['SMA_21'], 'Signal'] = -1
    
    # 4. Simulate Trades
    position = 0
    capital = 100000
    pnl = 0
    trades = 0
    
    for i in range(1, len(df)):
        # Buy Signal & No Position
        if df['Signal'].iloc[i] == 1 and position == 0:
            entry_price = df['close'].iloc[i]
            position = 1
            print(f"🟢 BUY at {entry_price} ({df['date'].iloc[i]})")
            trades += 1
            
        # Sell Signal & Long Position
        elif df['Signal'].iloc[i] == -1 and position == 1:
            exit_price = df['close'].iloc[i]
            position = 0
            profit = exit_price - entry_price
            pnl += profit
            print(f"🔴 SELL at {exit_price} | PnL: {profit:.2f}")
    
    print("\n" + "="*30)
    print("📊 BACKTEST RESULTS")
    print("="*30)
    print(f"Total Trades: {trades}")
    print(f"Net PnL:      {pnl:.2f} points")
    print("="*30 + "\n")

if __name__ == "__main__":
    run_backtest()
