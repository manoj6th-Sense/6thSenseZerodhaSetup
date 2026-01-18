# 6th-Sense Simple Setup (Kite Connect)

This folder provides a complete, standalone environment for algorithmic trading using the Zerodha Kite Connect API. It includes scripts for authentication, data extraction, backtesting, paper trading, and live execution.

---

## 🛑 Prerequisites

Before you begin, ensure you have:
1.  **Python 3.8+** installed on your system.
2.  A **Zerodha Trading Account** with **Kite Connect API access** enabled.
    *   You need your `API Key`, `API Secret`, `User ID`, `Password`, and `TOTP Secret`.

---

## ⚙️ Kite Developer Console Setup

To ensure the auto-login script works correctly, please configure your app at [developers.kite.trade](https://developers.kite.trade/) with the following settings (as used in this setup):

*   **App Name**: `6th-Sense` (or your preferred name)
*   **Redirect URL**: `http://127.0.0.1/` (or your personal redirect URL)
    *   *Note: This URL must match exactly what you set in your Kite Developer Console.*
*   **Redirect URL** (Alternative): `http://127.0.0.1/` (If you prefer local handling)
*   **Postback URL**: (Can be left blank)

After creating/updating the app, copy your **API Key** and **API Secret**.

---

## 🛠️ Installation Guide

### 1. One-Click Setup (Recommended)
Double-click on **`setup_env.bat`**.
*   It will automatically create a virtual environment (`venv`).
*   It will install all required libraries (`kiteconnect`, `pandas`, etc.).

**After the setup finishes:**
Open your terminal in this folder and activate the environment:
```bash
venv\Scripts\activate
```

*(Manual Method: Run `pip install -r requirements.txt` if you prefer your own global python)*

### 2. Configure Credentials
**⚠️ CRITICAL STEP**: The scripts need your credentials to connect.

1.  Find the file named `.env.example`.
2.  **Rename** it to `.env` (just `.env`, no `.txt` extension).
3.  Open `.env` in Notepad or VS Code.
4.  Fill in your details carefully:
    ```ini
    KITE_API_KEY=your_actual_api_key
    KITE_API_SECRET=your_actual_api_secret
    ZERODHA_USER_ID=your_six_digit_id
    ZERODHA_PASSWORD=your_password
    ZERODHA_TOTP_SECRET=your_totp_secret_string
    
    # Optional Risk Settings (Leave as is or adjust)
    MAX_LOSS_PER_DAY=10000
    ```
5.  Save the file.

---

## 🏃‍♂️ How to Run (Choose Your Method)

You can run these scripts in three different ways. Choose the one you prefer.

### Method 1: Command Prompt (CMD)
1.  Open CMD and navigate to this folder.
2.  **Activate the environment**:
    ```cmd
    venv\Scripts\activate
    ```
    *(You will see `(venv)` appear at the start of the line)*
3.  **Run any script**:
    ```cmd
    python step01_verify_login.py
    ```

### Method 2: VS Code
1.  Open this folder (`10_Simple_Setup`) in VS Code.
2.  Open any python file (e.g., `step01_verify_login.py`).
3.  **Select Interpreter**: Click the Python version in the bottom right corner -> Select `('venv': venv)`.
4.  Press **Run** (Play Button) in the top right.

### Method 3: Jupyter Notebook
1.  Double-click **`start_jupyter.bat`**.
2.  Browser will open. Click on `step06_notebook_demo.ipynb`.
3.  Run cells using `Shift + Enter`.

Run these scripts in order to test the system functionality.

### Step 1: Verify Connection
Checks if your API credentials are correct and you can login.
```bash
python step01_verify_login.py
```
*   **Success**: You will see "LOGIN SUCCESSFUL" and your account cash balance.
*   **Failure**: Check your `.env` file credentials.

### Step 2: Fetch Historical Data
Downloads historical candle data for NIFTY 50 to confirm data access.
```bash
python step02_data_extraction.py
```
*   **Output**: Creates a file `nifty_5min_data.csv`.

### Step 3: Run a Backtest
Simulates a trading strategy (Moving Average Crossover) on the data you just downloaded.
```bash
python step03_backtest.py
```
*   **Output**: Prints a list of simulated Buy/Sell signals and total PnL.

### Step 4: Paper Trading Simulation
Simulates a live trading session in real-time without placing orders. It watches the live price and prints "Mock Orders".
```bash
python step04_paper_trade.py
```
*   **Output**: Live price updates in your terminal.

### Step 5: Live Trade Execution (⚠️ WARNING)
**This script places a REAL order.**
It is hardcoded to place a LIMIT BUY order for 1 Qty of SBIN at a price far below the current market price (for safety), so it likely won't execute immediately, but it IS a real order.
```bash
python step05_simple_stock_trade.py
```

---

## 📓 Using Jupyter Notebooks
If you prefer interactive data analysis:
1.  Double-click **`start_jupyter.bat`**.
2.  It will automatically activate the environment and open **`step06_notebook_demo.ipynb`** in your browser.
3.  Run the cells to login, fetch data, and plot charts interactively.
    *   **Note**: The correct way to login in a notebook is:
        ```python
        from step00_auth import KiteAuth
        auth = KiteAuth()
        kite = auth.login() # Returns the kite object
        ```

---

## 🔒 Security Note to One Sharing This Folder
If you are sending this folder to someone else:
1.  **DELETE your `.env` file first!** It contains your password and secrets.
2.  The recipient will use `.env.example` to create their own configuration.
