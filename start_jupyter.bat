@echo off
echo ===================================================
echo   Starting Jupyter Notebook...
echo ===================================================

REM Check if venv exists
if not exist "venv\Scripts\activate.bat" (
    echo [ERROR] Virtual environment not found!
    echo Please run 'setup_env.bat' first.
    pause
    exit /b
)

REM Activate venv and start jupyter
call venv\Scripts\activate.bat
jupyter notebook step06_notebook_demo.ipynb
pause
