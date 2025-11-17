"""
Configuration settings for Last Supper Date Fetcher
"""

# Target URL
CENACOLO_URL = "https://cenacolovinciano.vivaticket.it/en/event/cenacolo-vinciano/151991"

# Browser settings
BROWSER_HEADLESS = True
BROWSER_TIMEOUT = 30000  # milliseconds
PAGE_LOAD_WAIT = 2000    # milliseconds

# User agent to avoid bot detection
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# Viewport settings
VIEWPORT_WIDTH = 1920
VIEWPORT_HEIGHT = 1080

# Retry settings
MAX_RETRIES = 3
RETRY_DELAY = 2000  # milliseconds

# Output settings
DEFAULT_OUTPUT_FORMAT = "json"
DEBUG_SCREENSHOT = True
DEBUG_SAVE_HTML = True
