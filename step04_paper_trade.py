"""
Sample 3: Paper Trading
Simulates a live trading session, checking LTP and printing "Mock Orders".
"""
import time
import random
from step00_auth import KiteAuth

def run_paper_trade():
    print("🚀 Starting Paper Trading Simulation...")
    print("This script simulates a strategy without placing real orders.\n")
    
    # 1. Login
    auth = KiteAuth()
    kite = auth.login()
    
    # Symbols to track (Instrument Tokens)
    # Using specific tokens effectively
    tokens = [256265] # NIFTY 50
    
    print(f"👀 Monitoring Instrument: {tokens[0]}")
    print("Conditions: Buy if price > 20000 (Example condition)")
    
    try:
        # Simulate a loop (e.g., 5 iterations)
        for i in range(5):
            print(f"\n--- Tick {i+1} ---")
            
            # Fetch Quote
            quote = kite.quote(f"NSE:NIFTY 50")
            ltp = quote["NSE:NIFTY 50"]["last_price"]
            
            print(f"📈 LTP: {ltp}")
            
            # Simple Logic
            # Randomized threshold for meaningful output in demo
            threshold = ltp - 10 # Force a trigger
            
            if ltp > threshold:
                print(f"⚡ SIGNAL: Buy Signal detected (LTP {ltp} > {threshold})")
                print(f"📝 PAPER ORDER: BUY 50 Qty @ Market (Mock)")
            else:
                print("💤 No signal.")
                
            time.sleep(2) # Wait 2 seconds
            
        print("\n✅ Paper Trade Session Complete.")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    run_paper_trade()
