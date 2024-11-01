

# shorten url
# def shorten(url=None):
#     import pyshorteners as ps
#     type_tiny = ps.Shortener()
#     short_url = type_tiny.tinyurl.short(url)
#     print("The shortened url is : " + short_url)


import logging
from typing import Optional
import pyshorteners

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def shorten(url: Optional[str] = None) -> Optional[str]:
    """
    Shortens a given URL using the TinyURL service.

    Args:
        url (Optional[str]): The URL to be shortened. If None, the function will not proceed.

    Returns:
        Optional[str]: The shortened URL, or None if the input URL is invalid.
    """
    if url is None:
        logging.error("No URL provided to shorten.")
        return None

    try:
        type_tiny = pyshorteners.Shortener()
        short_url = type_tiny.tinyurl.short(url)
        logging.info(f"The shortened URL is: {short_url}")
        return short_url
    except Exception as e:
        logging.error(f"An error occurred while shortening the URL: {e}")
        return None

def main():
    # Example usage
    url_to_shorten = "https://www.example.com/some/long/url"
    shortened_url = shorten(url_to_shorten)
    if shortened_url:
        logging.info(f"Shortened URL: {shortened_url}")

if __name__ == "__main__":
    main()
