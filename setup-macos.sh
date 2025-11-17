#!/bin/bash
# Last Supper Date Fetcher - macOS Setup Script
# Optimized setup script for macOS users

set -e  # Exit on error

echo "=========================================="
echo "Last Supper Date Fetcher - macOS Setup"
echo "=========================================="
echo ""

# Check if running on macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo "⚠️  Warning: This script is optimized for macOS"
    echo "   Detected OS: $OSTYPE"
    echo "   Continuing anyway..."
    echo ""
fi

# Check if Homebrew is installed (optional but recommended)
echo "[0/6] Checking for Homebrew..."
if command -v brew &> /dev/null; then
    echo "✓ Homebrew detected at $(which brew)"
else
    echo "ℹ️  Homebrew not found (optional)"
    echo "   Consider installing: https://brew.sh"
fi
echo ""

# Check Python version
echo "[1/6] Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    echo "✓ Python $PYTHON_VERSION detected at $(which python3)"

    # Verify minimum version
    if python3 -c "import sys; exit(0 if sys.version_info >= (3,8) else 1)"; then
        echo "✓ Python version is compatible (3.8+)"
    else
        echo "✗ Error: Python 3.8 or higher is required"
        echo "  You have Python $PYTHON_VERSION"
        echo ""
        echo "To upgrade Python on macOS:"
        echo "  brew install python@3.11"
        exit 1
    fi
else
    echo "✗ Error: Python 3 is not installed"
    echo ""
    echo "To install Python on macOS:"
    echo "  brew install python@3.11"
    echo "  or download from: https://www.python.org/downloads/macos/"
    exit 1
fi
echo ""

# Check for pip
echo "[2/6] Checking pip installation..."
if python3 -m pip --version &> /dev/null; then
    PIP_VERSION=$(python3 -m pip --version | awk '{print $2}')
    echo "✓ pip $PIP_VERSION detected"
else
    echo "✗ Error: pip is not installed"
    echo "  Installing pip..."
    python3 -m ensurepip --upgrade
fi
echo ""

# Create virtual environment
echo "[3/6] Creating virtual environment..."
if [ -d "venv" ]; then
    echo "  Virtual environment already exists"
    read -p "  Delete and recreate? (y/N): " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "  Removing old virtual environment..."
        rm -rf venv
        python3 -m venv venv
        echo "✓ Virtual environment recreated"
    else
        echo "  Keeping existing virtual environment"
    fi
else
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi
echo ""

# Activate virtual environment
echo "[4/6] Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"
echo "  Using Python: $(which python)"
echo ""

# Upgrade pip in virtual environment
echo "[5/6] Installing Python dependencies..."
echo "  Upgrading pip..."
pip install --upgrade pip --quiet
echo "  Installing requirements..."
pip install -r requirements.txt
echo "✓ Python packages installed"
echo ""

# Install Playwright browsers
echo "[6/6] Installing Playwright browsers..."
echo "  This may take a few minutes on first run..."
echo "  Installing Chromium..."
playwright install chromium

# Check if installation succeeded
if [ $? -eq 0 ]; then
    echo "✓ Chromium browser installed"
else
    echo "⚠️  Warning: Chromium installation may have had issues"
    echo "  Try running manually: playwright install chromium"
fi
echo ""

echo "=========================================="
echo "✓ macOS Setup Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo ""
echo "  1. Activate the virtual environment:"
echo "     source venv/bin/activate"
echo ""
echo "  2. Run the fetcher:"
echo "     python fetcher.py"
echo ""
echo "  3. Or save results to a file:"
echo "     python fetcher.py --output results.json"
echo ""
echo "  4. Debug mode (see browser in action):"
echo "     python fetcher.py --no-headless"
echo ""
echo "📚 See QUICKSTART-MACOS.md for detailed macOS usage guide"
echo ""
echo "Tip: Add 'source venv/bin/activate' to your shell profile"
echo "     to activate automatically in this directory."
echo ""
