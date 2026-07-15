import logging # Import Python's built-in logging module for logging and application messages.
import requests # import the requests library for making HTTP requests to websites and APIss.
from typing import Collection

logging.getLogger(__name__)



def check_urls(urls: Collection[str], timeout: int = 5) -> dict[str, str]:
    """
# def check_urls(...) = a custom function I create; I must write the logic inside it to perform the actual work.
# it will check the url* and returns a timeout status like below "UP"/"DOWN".
# "https://google.com": "UP",    
# "https://github.com": "UP"

    Checks a list of URLs and returns their status.

    Args:
        urls: A list of URL strings to check.
        timeout: Maximum time in seconds to wait for each request. Defaults to 5.

    Returns:
        A dictionary mapping each URL to its status string.
    """
    logging.info(
        f"Starting check for {len(urls)} URLs with a timeout of {timeout}"
    )
    results: dict[str, str] = {}

    for url in urls:
        status = "UNKNOWN"

        try:
            logging.debug(f"Checking URL: {url}")
            response = requests.get(url, timeout=timeout)

            if response.ok:
                status = f"{response.status_code} OK"
            else:
                status = (
                    f"{response.status_code} {response.reason}"
                )
        except requests.exceptions.Timeout:
            status = "TIMEOUT"
            logging.warning(f"Request to {url} timed out.")
        except requests.exceptions.ConnectionError:
            status = "CONNECTION_ERROR"
            logging.warning(f"Connection error for {url}.")
        except requests.exceptions.RequestException as e:
            status = f"REQUEST_ERROR: {type(e).__name__}"
            logging.error(
                f"An unexpected request error occured for {url}: {e}",
                exc_info=True,
            )

        results[url] = status
        logging.debug(f"Checked: {url:<40} -> {status}")

    logging.info("URL check finished.")
    return results