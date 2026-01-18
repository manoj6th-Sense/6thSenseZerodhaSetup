"""
Simple Authentication Module
"""
import pyotp
import requests
import json
from datetime import datetime, date
from kiteconnect import KiteConnect
from step00_config import Config
from pathlib import Path

class KiteAuth:
    TOKEN_FILE = Config.DATA_DIR / 'access_token.json'
    
    def __init__(self):
        self.kite = KiteConnect(api_key=Config.API_KEY)
        self.access_token = None
        self._load_saved_token()
    
    def _load_saved_token(self):
        try:
            if self.TOKEN_FILE.exists():
                with open(self.TOKEN_FILE, 'r') as f:
                    data = json.load(f)
                if data.get('date') == str(date.today()):
                    self.access_token = data['access_token']
                    self.kite.set_access_token(self.access_token)
                    print("✅ Loaded existing access token from today")
                    return True
        except Exception as e:
            print(f"⚠️ Could not load saved token: {e}")
        return False
    
    def _save_token(self):
        try:
            Config.DATA_DIR.mkdir(exist_ok=True)
            with open(self.TOKEN_FILE, 'w') as f:
                json.dump({
                    'access_token': self.access_token,
                    'date': str(date.today()),
                }, f)
            print("💾 Access token saved to file")
        except Exception as e:
            print(f"❌ Could not save token: {e}")
    
    def login(self, force=False):
        if not force and self.access_token:
            try:
                profile = self.kite.profile()
                print(f"✅ Already logged in as {profile['user_name']}")
                return self.kite
            except Exception:
                print("⚠️ Existing token invalid, performing fresh login")
        
        print(f"🔐 Initiating auto-login for {Config.USER_ID}")
        
        try:
            session = requests.Session()
            login_url = f"https://kite.zerodha.com/connect/login?api_key={Config.API_KEY}&v=3"
            session.get(login_url)
            
            # Step 2: Login
            login_response = session.post(
                "https://kite.zerodha.com/api/login",
                data={"user_id": Config.USER_ID, "password": Config.PASSWORD}
            )
            login_data = login_response.json()
            if login_data.get('status') != 'success':
                raise Exception(f"Login failed: {login_data.get('message')}")
            
            request_id = login_data['data']['request_id']
            
            # Step 3: TOTP
            print("📲 Generating TOTP...")
            totp = pyotp.TOTP(Config.TOTP_SECRET)
            twofa_value = totp.now()
            
            twofa_response = session.post(
                "https://kite.zerodha.com/api/twofa",
                data={
                    "user_id": Config.USER_ID,
                    "request_id": request_id,
                    "twofa_value": twofa_value,
                    "twofa_type": "totp"
                }
            )
            twofa_data = twofa_response.json()
            if twofa_data.get('status') != 'success':
                raise Exception(f"2FA failed: {twofa_data.get('message')}")
            
            # Step 4: Get Request Token
            authorize_url = f"https://kite.zerodha.com/connect/login?api_key={Config.API_KEY}&v=3"
            response = session.get(authorize_url)
            
            # Extract request_token from redirected URL
            from urllib.parse import urlparse, parse_qs
            parsed = urlparse(response.url)
            request_token = parse_qs(parsed.query).get('request_token', [None])[0]
            
            if not request_token:
                 raise Exception("Could not retrieve request_token. Check API Key/Secret.")

            # Step 5: Generate Session
            print(f"🔄 Generating session...")
            session_data = self.kite.generate_session(
                request_token, 
                api_secret=Config.API_SECRET
            )
            
            self.access_token = session_data['access_token']
            self.kite.set_access_token(self.access_token)
            self._save_token()
            
            return self.kite
            
        except Exception as e:
            print(f"❌ Auto-login failed: {e}")
            raise
