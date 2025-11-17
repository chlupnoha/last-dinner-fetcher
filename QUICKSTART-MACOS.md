# Quick Start Guide for macOS 🍎

Get the Last Supper Date Fetcher running on your Mac in 5 minutes!

## Prerequisites

### Check Python Installation

```bash
python3 --version
```

- ✅ **Python 3.8+** → You're ready!
- ❌ **Not found** or **< 3.8** → Install Python first

### Install Python on macOS

**Option 1: Using Homebrew (Recommended)**
```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python@3.11
```

**Option 2: Official Installer**
Download from [python.org/downloads/macos](https://www.python.org/downloads/macos/)

---

## One-Command Setup 🚀

```bash
./setup-macos.sh
```

That's it! The script will:
1. ✅ Verify Python 3.8+ is installed
2. ✅ Check for pip
3. ✅ Create virtual environment in `venv/`
4. ✅ Install Python dependencies (Playwright, etc.)
5. ✅ Download Chromium browser

---

## Manual Setup (Alternative)

If you prefer step-by-step control:

### 1. Create Virtual Environment

```bash
python3 -m venv venv
```

### 2. Activate Virtual Environment

```bash
source venv/bin/activate
```

Your prompt should now show `(venv)` prefix.

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Install Playwright Browser

```bash
playwright install chromium
```

---

## Usage Examples

### Activate Environment

**Always** activate before running the fetcher:

```bash
source venv/bin/activate
```

### Example 1: Fetch Dates (JSON)

```bash
python fetcher.py
```

**Output:**
```json
{
  "event": "Cenacolo Vinciano",
  "fetch_timestamp": "2025-11-17T10:30:00",
  "total_dates_found": 15,
  "available_dates": [...]
}
```

### Example 2: Save to File

```bash
python fetcher.py --output last-supper-dates.json
```

View the file:
```bash
cat last-supper-dates.json | python -m json.tool
```

### Example 3: Simple Text Output

```bash
python fetcher.py --format simple
```

### Example 4: Debug Mode (Watch It Work)

```bash
python fetcher.py --no-headless
```

Opens Chrome so you can see the scraping happen live!

### Example 5: All Options Combined

```bash
python fetcher.py \
  --output dates.json \
  --format json \
  --no-headless
```

---

## macOS-Specific Tips

### 1. Add to PATH (zsh)

Add to your `~/.zshrc`:

```bash
# Last Supper Fetcher alias
alias lastsupper='cd /path/to/last-dinner-fetcher && source venv/bin/activate && python fetcher.py'
```

Reload:
```bash
source ~/.zshrc
```

Now you can run from anywhere:
```bash
lastsupper --output ~/Desktop/dates.json
```

### 2. Add to PATH (bash)

Add to your `~/.bash_profile` or `~/.bashrc`:

```bash
# Last Supper Fetcher alias
alias lastsupper='cd /path/to/last-dinner-fetcher && source venv/bin/activate && python fetcher.py'
```

Reload:
```bash
source ~/.bash_profile
```

### 3. Schedule with launchd

Create `~/Library/LaunchAgents/com.lastsupper.fetcher.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.lastsupper.fetcher</string>

    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>-c</string>
        <string>cd /path/to/last-dinner-fetcher && source venv/bin/activate && python fetcher.py --output ~/Documents/last-supper-dates.json</string>
    </array>

    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>9</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>

    <key>StandardOutPath</key>
    <string>/tmp/lastsupper.log</string>

    <key>StandardErrorPath</key>
    <string>/tmp/lastsupper.error.log</string>
</dict>
</plist>
```

Load it:
```bash
launchctl load ~/Library/LaunchAgents/com.lastsupper.fetcher.plist
```

This runs daily at 9 AM and saves results to `~/Documents/last-supper-dates.json`.

### 4. Use with Automator

Create a Quick Action in Automator:
1. Open **Automator**
2. New Document → **Quick Action**
3. Add "Run Shell Script"
4. Paste:
   ```bash
   cd /path/to/last-dinner-fetcher
   source venv/bin/activate
   python fetcher.py --output ~/Desktop/dates.json
   osascript -e 'display notification "Last Supper dates fetched!" with title "Fetcher Complete"'
   ```
5. Save as "Fetch Last Supper Dates"

Now accessible from Services menu or Spotlight!

---

## Common macOS Issues

### "Permission denied: ./setup-macos.sh"

Make it executable:
```bash
chmod +x setup-macos.sh
./setup-macos.sh
```

### "python3: command not found"

Install Python:
```bash
brew install python@3.11
```

Or download from [python.org](https://www.python.org/downloads/macos/)

### "playwright: command not found" after install

Activate the virtual environment first:
```bash
source venv/bin/activate
playwright install chromium
```

### SSL Certificate Errors

Update certificates:
```bash
pip install --upgrade certifi
```

Or install Python certificates:
```bash
/Applications/Python\ 3.11/Install\ Certificates.command
```

### "xcrun: error: invalid active developer path"

Install Xcode Command Line Tools:
```bash
xcode-select --install
```

### Chromium Won't Launch

Check security settings:
1. Go to **System Preferences** → **Security & Privacy**
2. Allow apps from **App Store and identified developers**
3. Or manually allow Chromium when prompted

### M1/M2 Apple Silicon Issues

If you encounter architecture issues:
```bash
# Use Rosetta Python if needed
arch -x86_64 python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

---

## Keyboard Shortcuts

When running with `--no-headless`:
- **⌘Q** - Quit browser
- **⌘R** - Refresh page
- **⌘⌥I** - Open DevTools

---

## Performance Tips for Mac

### 1. Use Headless Mode (Faster)

```bash
python fetcher.py  # Headless by default
```

### 2. Close Other Apps

Free up memory for better performance.

### 3. Check Activity Monitor

If slow, check Activity Monitor (⌘+Space → "Activity Monitor") for:
- High CPU usage
- Low memory
- Other Python processes

---

## Directory Structure

```
last-dinner-fetcher/
├── venv/                    # Virtual environment (created by setup)
├── fetcher.py              # Main script
├── config.py               # Configuration
├── requirements.txt        # Dependencies
├── setup-macos.sh         # This setup script
├── QUICKSTART-MACOS.md    # This guide
└── README.md              # Full documentation
```

---

## Quick Reference

| Command | Action |
|---------|--------|
| `./setup-macos.sh` | Run setup |
| `source venv/bin/activate` | Activate environment |
| `python fetcher.py` | Fetch dates |
| `python fetcher.py -o dates.json` | Save to file |
| `python fetcher.py --format simple` | Text output |
| `python fetcher.py --no-headless` | Debug mode |
| `python fetcher.py --help` | Show all options |
| `deactivate` | Exit virtual environment |
| `rm -rf venv/` | Remove environment |

---

## Terminal Shortcuts

- **⌘K** - Clear terminal
- **⌘T** - New tab
- **Control+C** - Stop running program
- **↑/↓** - Navigate command history

---

## Integration Examples

### Save to iCloud

```bash
python fetcher.py --output ~/Library/Mobile\ Documents/com~apple~CloudDocs/last-supper-dates.json
```

### Open in TextEdit

```bash
python fetcher.py --output dates.json && open -a TextEdit dates.json
```

### Pretty Print to Terminal

```bash
python fetcher.py | python -m json.tool
```

### Copy to Clipboard

```bash
python fetcher.py | pbcopy
```

Then paste anywhere with **⌘V**.

---

## What's Next?

1. **Explore options**: `python fetcher.py --help`
2. **Customize**: Edit `config.py` for your needs
3. **Automate**: Set up launchd or Automator workflow
4. **Share**: Results are in standard JSON format

---

## Getting Help

1. Check debug files:
   - `page_screenshot.png` - Visual snapshot
   - `page_content.html` - Raw HTML

2. Run in debug mode:
   ```bash
   python fetcher.py --no-headless
   ```

3. Check logs:
   ```bash
   python fetcher.py 2>&1 | tee fetcher.log
   ```

---

## Updating

### Update Dependencies

```bash
source venv/bin/activate
pip install -r requirements.txt --upgrade
```

### Update Playwright

```bash
pip install playwright --upgrade
playwright install chromium
```

### Pull Latest Code

```bash
git pull origin main
./setup-macos.sh
```

---

**Enjoy!** 🎨🍷

For more detailed documentation, see `README.md`.
