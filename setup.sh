#!/bin/bash
# Last Supper Date Fetcher - Setup Script
# This script sets up the virtual environment and installs dependencies

set -e  # Exit on error

echo "=========================================="
echo "Last Supper Date Fetcher - Setup"
echo "=========================================="
echo ""

# Check Python version
echo "[1/5] Checking Python version..."
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
REQUIRED_VERSION="3.8"

if python3 -c "import sys; exit(0 if sys.version_info >= (3,8) else 1)"; then
    echo "✓ Python $PYTHON_VERSION detected"
else
    echo "✗ Error: Python 3.8 or higher is required"
    echo "  You have Python $PYTHON_VERSION"
    exit 1
fi
echo ""

# Create virtual environment
echo "[2/5] Creating virtual environment..."
if [ -d "venv" ]; then
    echo "  Virtual environment already exists, skipping..."
else
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi
echo ""

# Activate virtual environment
echo "[3/5] Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"
echo ""

# Install Python dependencies
echo "[4/5] Installing Python dependencies..."
pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt
echo "✓ Python packages installed"
echo ""

# Install Playwright browsers
echo "[5/5] Installing Playwright browsers..."
echo "  This may take a few minutes..."
playwright install chromium
echo "✓ Chromium browser installed"
echo ""

echo "=========================================="
echo "✓ Setup complete!"
echo "=========================================="
echo ""
echo "To use the fetcher:"
echo "  1. Activate the virtual environment:"
echo "     source venv/bin/activate"
echo ""
echo "  2. Run the fetcher:"
echo "     python fetcher.py"
echo ""
echo "See QUICKSTART.md for more examples and usage instructions."
echo ""
