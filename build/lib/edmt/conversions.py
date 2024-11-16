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
        print("The shortened url is : " + short_url)
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




"""
Create a function that accepts a pdf file and convert to word 
provide an output link
provide a pdf link to the function 
"""
def pdf_word(url=None,dir=None,pdf=None,word=None):

    """
    A function to convert pdf to word using pdf2word
    """

    if url is None:
        logging.error("No URL provided to shorten.")
        return None

    try:
        """
        Add the implementation to perform the conversion
        """


    except Exception as e:
        logging.error(f"An error occurred while shortening the URL: {e}")
        return None

    return pdf_word