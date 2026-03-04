from .requester import request_url
from .saver import save_pretty_html

import argparse
import requests
import logging
import sys



def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("logs/app.log"),
            logging.StreamHandler()
        ]
    )

    parser = argparse.ArgumentParser(description="URL CLI")
    parser.add_argument("url", help="Ваш URL")
    args = parser.parse_args()
    url = args.url

    if not url.startswith(("http://", "https://")):
        logging.error("URL must start with http:// or https://")
        sys.exit(1)

    try:
        logging.info(f"Processing URL: {url}")
        html = request_url(url)
        save_pretty_html(html)
    except requests.RequestException as e:
        logging.error(f"Application failed: {e}")
        sys.exit(1)



if __name__ == "__main__":
    main()