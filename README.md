# Last Supper Date Fetcher

A Python tool to fetch available booking dates for the Last Supper (Cenacolo Vinciano) in Milan from the VivaTicket booking system.

## Features

- Automated browser-based fetching using Playwright
- Handles JavaScript-heavy booking pages
- Extracts available booking dates
- Outputs results in JSON or simple text format
- Debug mode with screenshots and HTML dumps
- Configurable and extensible

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone this repository or download the files

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Install Playwright browsers:
```bash
playwright install chromium
```

## Usage

### Basic Usage

Run the fetcher with default settings (JSON output to stdout):
```bash
python fetcher.py
```

### Output to File

Save results to a JSON file:
```bash
python fetcher.py --output results.json
```

### Simple Format

Get a simple text list instead of JSON:
```bash
python fetcher.py --format simple
```

### Debug Mode

Run with visible browser for debugging:
```bash
python fetcher.py --no-headless
```

### Combined Options

```bash
python fetcher.py --no-headless --output results.json --format json
```

## Command Line Options

- `--no-headless` - Run browser in visible mode (useful for debugging)
- `--output`, `-o` - Specify output file path (default: stdout)
- `--format` - Choose output format: `json` or `simple` (default: json)

## Output Format

### JSON Format
```json
{
  "event": "Cenacolo Vinciano",
  "event_url": "https://cenacolovinciano.vivaticket.it/en/event/cenacolo-vinciano/151991",
  "fetch_timestamp": "2025-11-17T10:30:00.123456",
  "total_dates_found": 15,
  "available_dates": [
    {
      "selector": "[class*='date']",
      "text": "20",
      "date_attribute": "2025-11-20",
      "classes": "date-available",
      "available": true
    }
  ]
}
```

## Configuration

Edit `config.py` to customize:
- Browser timeout settings
- User agent strings
- Viewport dimensions
- Retry behavior
- Debug options

## Debugging

When run, the script creates debug files:
- `page_screenshot.png` - Screenshot of the booking page
- `page_content.html` - Raw HTML content of the page

These files help troubleshoot issues with date extraction.

## How It Works

1. Launches a Chromium browser using Playwright
2. Navigates to the Last Supper booking page
3. Handles cookie consent popups
4. Waits for dynamic content to load
5. Searches for date picker elements using multiple strategies
6. Extracts date information from DOM elements
7. Returns structured data with available dates

## Troubleshooting

### "playwright not found"
Run: `pip install playwright && playwright install chromium`

### "403 Forbidden" or "Access Denied"
The website may have updated their bot detection. Try:
- Running with `--no-headless` to see what's happening
- Checking if the website structure has changed
- Updating the selectors in the code

### No dates found
- Check `page_screenshot.png` to see what the page looks like
- Review `page_content.html` to find the correct selectors
- The website may require additional interaction (clicking buttons, etc.)

## License

MIT License - Feel free to use and modify as needed.

## Disclaimer

This tool is for educational purposes. Always respect the website's terms of service and robots.txt. Use responsibly and don't overload the server with requests.
