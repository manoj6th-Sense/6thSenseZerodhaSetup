"""
Simple Configuration
"""
import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env file
env_path = Path(__file__).parent / '.env'
load_dotenv(env_path)

class Config:
    API_KEY = os.getenv('KITE_API_KEY')
    API_SECRET = os.getenv('KITE_API_SECRET')
    USER_ID = os.getenv('ZERODHA_USER_ID')
    PASSWORD = os.getenv('ZERODHA_PASSWORD')
    TOTP_SECRET = os.getenv('ZERODHA_TOTP_SECRET')
    
    # Risk Management
    MAX_LOSS_PER_DAY = float(os.getenv('MAX_LOSS_PER_DAY', 10000))
    MAX_LOSS_PER_TRADE = float(os.getenv('MAX_LOSS_PER_TRADE', 2000))
    MAX_POSITION_SIZE = float(os.getenv('MAX_POSITION_SIZE', 100000))
    RISK_PER_TRADE_PERCENT = float(os.getenv('RISK_PER_TRADE_PERCENT', 2))
    
    BASE_DIR = Path(__file__).parent
    DATA_DIR = BASE_DIR / 'data'
