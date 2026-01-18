from step00_auth import KiteAuth
from step00_config import Config

def main():
    print("🚀 Starting Simple Auto-Login...")
    try:
        auth = KiteAuth()
        kite = auth.login()
        
        # Verify
        profile = kite.profile()
        margins = kite.margins()
        
        print("\n" + "="*40)
        print("🎉 LOGIN SUCCESSFUL")
        print("="*40)
        print(f"Name:   {profile['user_name']}")
        print(f"ID:     {profile['user_id']}")
        print(f"Email:  {profile['email']}")
        print(f"Cash:   ₹{margins['equity']['available']['cash']:,.2f}")
        print("="*40 + "\n")
        
    except Exception as e:
        print(f"\n❌ FATAL ERROR: {e}")

if __name__ == "__main__":
    main()
