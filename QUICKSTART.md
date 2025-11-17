# Quick Start Guide

Get up and running with the Last Supper Date Fetcher in 5 minutes!

## Prerequisites

- **Python 3.8+** installed on your system
  - Check: `python3 --version` (Linux/Mac) or `python --version` (Windows)
  - Download: [python.org](https://www.python.org/downloads/)

## One-Command Setup

### Linux / macOS

```bash
./setup.sh
```

### Windows

```cmd
setup.bat
```

That's it! The setup script will:
1. ✓ Check Python version
2. ✓ Create virtual environment
3. ✓ Install Python dependencies
4. ✓ Install Chromium browser

---

## Manual Setup (Alternative)

If you prefer to set up manually:

### Step 1: Create Virtual Environment

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate.bat
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
playwright install chromium
```

---

## Usage Examples

### 1. Basic Fetch (JSON output)

```bash
# Linux/macOS
source venv/bin/activate  # If not already activated
python fetcher.py

# Windows
venv\Scripts\activate.bat
python fetcher.py
```

**Output:**
```json
{
  "event": "Cenacolo Vinciano",
  "event_url": "https://...",
  "fetch_timestamp": "2025-11-17T...",
  "total_dates_found": 15,
  "available_dates": [...]
}
```

### 2. Save to File

```bash
python fetcher.py --output results.json
```

Creates `results.json` with all available dates.

### 3. Simple Text Format

```bash
python fetcher.py --format simple
```

**Output:**
```
Available dates for Cenacolo Vinciano:
Fetched: 2025-11-17T10:30:00
Total dates found: 15

- {"date": "2025-11-20", "available": true}
- {"date": "2025-11-21", "available": true}
...
```

### 4. Debug Mode (See What's Happening)

```bash
python fetcher.py --no-headless
```

Opens a visible browser window so you can see the scraping process in action.

### 5. Complete Example

```bash
python fetcher.py --output dates.json --format json --no-headless
```

---

## Common Commands

### Activate Virtual Environment

**Every time** you want to use the fetcher, activate the virtual environment first:

```bash
# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate.bat
```

You'll see `(venv)` in your terminal prompt when activated.

### Deactivate Virtual Environment

```bash
deactivate
```

### Update Dependencies

```bash
pip install -r requirements.txt --upgrade
```

---

## Troubleshooting

### "Command not found: python3"

Try `python` instead:
```bash
python --version
python fetcher.py
```

### "Permission denied: ./setup.sh"

Make it executable:
```bash
chmod +x setup.sh
./setup.sh
```

### "playwright: command not found"

Reinstall Playwright:
```bash
pip install playwright
playwright install chromium
```

### "No dates found"

The website structure may have changed. Check debug files:
- `page_screenshot.png` - Visual snapshot of the page
- `page_content.html` - Raw HTML content

Run with `--no-headless` to see what's happening in the browser.

### "403 Forbidden" or Access Denied

The website is blocking automated access. Try:
1. Running with `--no-headless` to use a visible browser
2. Checking if the URL is still correct
3. Adding delays or changing user agent in `config.py`

---

## What's Next?

### Scheduled Fetching

Run the fetcher automatically using cron (Linux/Mac) or Task Scheduler (Windows):

```bash
# Example cron job (runs daily at 9 AM)
0 9 * * * cd /path/to/last-dinner-fetcher && source venv/bin/activate && python fetcher.py --output dates.json
```

### Integration

Import as a Python module:

```python
from fetcher import LastSupperDateFetcher

fetcher = LastSupperDateFetcher(headless=True)
result = fetcher.fetch_dates()
print(f"Found {result['total_dates_found']} dates")
```

### Customization

Edit `config.py` to customize:
- Browser timeout settings
- User agent strings
- Viewport dimensions
- Debug options

---

## Need Help?

1. Check `README.md` for detailed documentation
2. Review debug files: `page_screenshot.png` and `page_content.html`
3. Run with `--no-headless` to see what's happening
4. Check the website manually to see if it's accessible

---

## Quick Reference Card

| Command | Description |
|---------|-------------|
| `./setup.sh` | Initial setup (Linux/Mac) |
| `setup.bat` | Initial setup (Windows) |
| `source venv/bin/activate` | Activate environment (Linux/Mac) |
| `venv\Scripts\activate.bat` | Activate environment (Windows) |
| `python fetcher.py` | Fetch dates (JSON to stdout) |
| `python fetcher.py -o dates.json` | Save to file |
| `python fetcher.py --format simple` | Simple text output |
| `python fetcher.py --no-headless` | Debug with visible browser |
| `python fetcher.py --help` | Show all options |
| `deactivate` | Deactivate virtual environment |

---

**Happy fetching!** 🎨🍷
