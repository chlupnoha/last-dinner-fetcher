@echo off
REM Last Supper Date Fetcher - Setup Script for Windows
REM This script sets up the virtual environment and installs dependencies

echo ==========================================
echo Last Supper Date Fetcher - Setup
echo ==========================================
echo.

REM Check Python version
echo [1/5] Checking Python version...
python --version >nul 2>&1
if errorlevel 1 (
    echo X Error: Python is not installed or not in PATH
    echo   Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo + Python %PYTHON_VERSION% detected
echo.

REM Create virtual environment
echo [2/5] Creating virtual environment...
if exist venv (
    echo   Virtual environment already exists, skipping...
) else (
    python -m venv venv
    echo + Virtual environment created
)
echo.

REM Activate virtual environment
echo [3/5] Activating virtual environment...
call venv\Scripts\activate.bat
echo + Virtual environment activated
echo.

REM Install Python dependencies
echo [4/5] Installing Python dependencies...
python -m pip install --upgrade pip >nul 2>&1
pip install -r requirements.txt
echo + Python packages installed
echo.

REM Install Playwright browsers
echo [5/5] Installing Playwright browsers...
echo   This may take a few minutes...
playwright install chromium
echo + Chromium browser installed
echo.

echo ==========================================
echo + Setup complete!
echo ==========================================
echo.
echo To use the fetcher:
echo   1. Activate the virtual environment:
echo      venv\Scripts\activate.bat
echo.
echo   2. Run the fetcher:
echo      python fetcher.py
echo.
echo See QUICKSTART.md for more examples and usage instructions.
echo.
pause
