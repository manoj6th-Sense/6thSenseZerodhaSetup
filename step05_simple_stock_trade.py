"""
Sample 4: Simple Stock Trade (LIVE)
⚠️ W A R N I N G : THIS SCRIPT PLACES REAL ORDERS
"""
from step00_auth import KiteAuth
from kiteconnect import KiteConnect

def place_simple_trade():
    print("!" * 50)
    print("⚠️  WARNING: REAL TRADE EXECUTION")
    print("This script will attempt to place a REAL order.")
    print("!" * 50)
    
    confirm = input("\nType 'YES' to proceed with a Limit Buy Order for SBIN: ")
    if confirm != 'YES':
        print("❌ Aborted.")
        return

    try:
        # 1. Login
        auth = KiteAuth()
        kite = auth.login()
        
        # 2. Define Order Details
        symbol = "SBIN"
        exchange = "NSE"
        quantity = 1
        price = 400  # LIMIT Price (Way below CMP for safety in test)
        
        print(f"\n🚀 Placing Order: BUY {quantity} {symbol} @ ₹{price}")
        
        # 3. Place Order
        order_id = kite.place_order(
            tradingsymbol=symbol,
            exchange=exchange,
            transaction_type=kite.TRANSACTION_TYPE_BUY,
            quantity=quantity,
            variety=kite.VARIETY_REGULAR,
            order_type=kite.ORDER_TYPE_LIMIT,
            product=kite.PRODUCT_CNC, # Long term (Delivery)
            price=price,
            validity=kite.VALIDITY_DAY
        )
        
        print(f"✅ Order Placed Successfully! ID: {order_id}")
        
    except Exception as e:
        print(f"❌ Order Failed: {e}")

if __name__ == "__main__":
    place_simple_trade()
