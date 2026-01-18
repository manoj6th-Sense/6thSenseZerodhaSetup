@echo off
echo ===================================================
echo   6th-Sense Simple Setup - Automated Installer
echo ===================================================

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in your PATH.
    echo Please install Python 3.8+ from python.org and try again.
    pause
    exit /b
)

echo [1/3] Creating Virtual Environment (venv)...
python -m venv venv

echo [2/3] Activating Virtual Environment...
call venv\Scripts\activate.bat

echo [3/3] Installing Dependencies...
pip install -r requirements.txt

echo.
echo ===================================================
echo   SETUP COMPLETE!
echo ===================================================
echo.
echo To run the scripts, you must activate the environment first.
echo Run this command in your terminal:
echo.
echo    venv\Scripts\activate
echo.
pause
