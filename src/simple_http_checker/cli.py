import logging
import click
from typing import Collection

from .checker import check_urls

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)-8s %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

"""OUTPUT
[2026-07-09 14:30:15] INFO     app     : Server started
[2026-07-09 14:30:18] ERROR    app     : Database connection failed 

level=logging.INFO → Show INFO, WARNING, ERROR, and CRITICAL messages.
format=... → Controls the layout of each log message.
%(asctime)s → Current date and time.
%(levelname)s → Log level (INFO, ERROR, etc.).
%(name)s → Logger name.
%(message)s → Your message.
datefmt → How the date and time are formatted.

""" 

logger = logging.getLogger(__name__)


@click.command()
@click.argument("urls", nargs=-1)
@click.option(
    "--timeout",
    default=5,
    help="Timeout in seconds for each request.",
)
@click.option(
    "--verbose", "-v", is_flag=True, help="Enable debug logging."
)
def main(urls: Collection[str], timeout: int, verbose: bool):
    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Verbose logging enabled.")

    logger.debug(f"Received urls: {urls}")
    logger.debug(f"Received timeout: {timeout}")
    logger.debug(f"Received verbose: {verbose}")

    if not urls:
        logger.warning("No URLs provided to check.")
        click.echo("Usage: check-urls <URL1> <URL2> ...")
        return

    logger.info(f"Starting check for {len(urls)} URLs.")

    results = check_urls(urls, timeout)

    click.echo("\n--- Results ---")
    for url, status in results.items():
        if "OK" in status:
            fg_color = "green"
        else:
            fg_color = "red"

        click.secho(f"{url:<40} -> {status}", fg=fg_color)


"""EXPLANATION
logging → Prints structured log messages.
click → Builds command-line applications.
basicConfig() → Configures how logs look.
getLogger(__name__) → Creates a logger for the current file.
@click.command() → Makes the function executable from the terminal.
@click.argument() → Defines required command-line arguments.
@click.option() → Defines optional flags such as --timeout and -v. 
""" 