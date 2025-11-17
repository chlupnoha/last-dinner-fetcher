#!/usr/bin/env python3
"""
Last Supper (Cenacolo Vinciano) Date Fetcher
Fetches available booking dates from the VivaTicket website
"""

import json
import logging
import sys
from datetime import datetime
from typing import Dict, List, Optional
from playwright.sync_api import sync_playwright, Page, TimeoutError as PlaywrightTimeout


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class LastSupperDateFetcher:
    """Fetches available dates for Last Supper bookings"""

    URL = "https://cenacolovinciano.vivaticket.it/en/event/cenacolo-vinciano/151991"

    def __init__(self, headless: bool = True):
        """
        Initialize the fetcher

        Args:
            headless: Run browser in headless mode (default: True)
        """
        self.headless = headless
        self.available_dates = []

    def fetch_dates(self) -> Dict:
        """
        Main method to fetch available dates

        Returns:
            Dictionary containing event info and available dates
        """
        logger.info("Starting date fetch process...")

        with sync_playwright() as p:
            # Launch browser
            browser = p.chromium.launch(headless=self.headless)

            try:
                # Create context with realistic settings to avoid detection
                context = browser.new_context(
                    viewport={'width': 1920, 'height': 1080},
                    user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
                )

                page = context.new_page()

                # Navigate to the page
                logger.info(f"Navigating to {self.URL}")
                page.goto(self.URL, wait_until='networkidle', timeout=30000)

                # Handle cookie consent if present
                self._handle_cookie_consent(page)

                # Wait for the page to load completely
                page.wait_for_timeout(2000)

                # Extract available dates
                dates = self._extract_dates(page)

                # Prepare result
                result = {
                    "event": "Cenacolo Vinciano",
                    "event_url": self.URL,
                    "fetch_timestamp": datetime.now().isoformat(),
                    "total_dates_found": len(dates),
                    "available_dates": dates
                }

                logger.info(f"Successfully fetched {len(dates)} date(s)")
                return result

            except Exception as e:
                logger.error(f"Error during fetch: {str(e)}")
                raise
            finally:
                browser.close()

    def _handle_cookie_consent(self, page: Page):
        """Handle cookie consent popup if it appears"""
        try:
            # Common selectors for cookie consent buttons
            selectors = [
                'button:has-text("Accept")',
                'button:has-text("Accetta")',
                'button:has-text("Agree")',
                '[id*="cookie"] button',
                '[class*="cookie"] button'
            ]

            for selector in selectors:
                try:
                    if page.locator(selector).count() > 0:
                        logger.info("Accepting cookie consent...")
                        page.locator(selector).first.click(timeout=2000)
                        page.wait_for_timeout(1000)
                        break
                except:
                    continue

        except Exception as e:
            logger.debug(f"No cookie consent found or error handling it: {e}")

    def _extract_dates(self, page: Page) -> List[Dict]:
        """
        Extract available dates from the page

        Args:
            page: Playwright page object

        Returns:
            List of dictionaries with date information
        """
        dates = []

        try:
            # Take a screenshot for debugging
            logger.info("Taking screenshot for debugging...")
            page.screenshot(path="page_screenshot.png")

            # Wait for calendar or date selector to load
            # Try multiple possible selectors
            possible_selectors = [
                '[class*="calendar"]',
                '[class*="date"]',
                '[class*="day"]',
                'button[data-date]',
                '.available-date',
                '[role="gridcell"]',
                '.fc-day',  # FullCalendar
                '[class*="DatePicker"]',
            ]

            # Try to find any date-related elements
            page.wait_for_timeout(3000)  # Give page time to load

            # Get page content for inspection
            content = page.content()

            # Look for date patterns in the page
            logger.info("Searching for date elements on the page...")

            # Try to find calendar widget
            for selector in possible_selectors:
                elements = page.locator(selector)
                count = elements.count()
                if count > 0:
                    logger.info(f"Found {count} elements matching '{selector}'")

                    # Try to extract dates from these elements
                    for i in range(min(count, 100)):  # Limit to first 100
                        try:
                            element = elements.nth(i)
                            text = element.text_content() or ""

                            # Check if element has data attributes
                            date_attr = None
                            for attr in ['data-date', 'data-value', 'aria-label', 'title']:
                                try:
                                    date_attr = element.get_attribute(attr)
                                    if date_attr:
                                        break
                                except:
                                    continue

                            # Check if element is clickable/available
                            is_available = True
                            classes = element.get_attribute('class') or ""
                            if any(x in classes.lower() for x in ['disabled', 'unavailable', 'sold-out']):
                                is_available = False

                            if text.strip() or date_attr:
                                dates.append({
                                    "selector": selector,
                                    "text": text.strip(),
                                    "date_attribute": date_attr,
                                    "classes": classes,
                                    "available": is_available
                                })
                        except Exception as e:
                            logger.debug(f"Error extracting element {i}: {e}")
                            continue

            # If we found dates, process them
            if dates:
                logger.info(f"Extracted {len(dates)} potential date elements")
            else:
                logger.warning("No date elements found. Page might use different structure or require interaction.")

                # Try to find and click on any "Book" or "Select Date" buttons
                book_selectors = [
                    'button:has-text("Book")',
                    'button:has-text("Prenota")',
                    'button:has-text("Select")',
                    'a:has-text("Book")',
                ]

                for selector in book_selectors:
                    try:
                        if page.locator(selector).count() > 0:
                            logger.info(f"Found booking button: {selector}")
                            page.locator(selector).first.click(timeout=5000)
                            page.wait_for_timeout(2000)
                            # Retry date extraction
                            return self._extract_dates(page)
                    except:
                        continue

            return dates

        except Exception as e:
            logger.error(f"Error extracting dates: {str(e)}")
            # Save page content for debugging
            with open('page_content.html', 'w', encoding='utf-8') as f:
                f.write(page.content())
            logger.info("Saved page content to page_content.html for debugging")
            raise


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description='Fetch available dates for Last Supper (Cenacolo Vinciano) bookings'
    )
    parser.add_argument(
        '--no-headless',
        action='store_true',
        help='Run browser in visible mode (for debugging)'
    )
    parser.add_argument(
        '--output',
        '-o',
        help='Output file path (default: stdout)',
        default=None
    )
    parser.add_argument(
        '--format',
        choices=['json', 'simple'],
        default='json',
        help='Output format (default: json)'
    )

    args = parser.parse_args()

    try:
        fetcher = LastSupperDateFetcher(headless=not args.no_headless)
        result = fetcher.fetch_dates()

        # Format output
        if args.format == 'json':
            output = json.dumps(result, indent=2, ensure_ascii=False)
        else:
            # Simple format - just list dates
            output = f"Available dates for {result['event']}:\n"
            output += f"Fetched: {result['fetch_timestamp']}\n"
            output += f"Total dates found: {result['total_dates_found']}\n\n"
            for date_info in result['available_dates']:
                output += f"- {date_info}\n"

        # Write output
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(output)
            logger.info(f"Results written to {args.output}")
        else:
            print(output)

        return 0

    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        return 1


if __name__ == '__main__':
    sys.exit(main())
