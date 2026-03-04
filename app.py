from bs4 import BeautifulSoup

import argparse
import requests
import logging
import sys


def request_url(url: str, timeout: int = 10) -> requests.Response:
    """Принимает URL, делает запрос и возвращает response."""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        logging.info(f"URL: {url}, Status Code: {response.status_code}")
        return response
    except requests.RequestException as e:
        logging.error(f"Error requesting URL: {url}, Error: {e}")
        raise

def save_pretty_html(response: requests.Response, filename="html.txt") -> None:
    """
    Принимает response от requests.get() и сохраняет HTML в файл красиво.
    """
    # Форматируем HTML с отступами
    logging.info("Formatting HTML")
    soup = BeautifulSoup(response.text, "html.parser")
    pretty_html = soup.prettify()
    logging.info("HTML formatted successfully")
    
    # Сохраняем в файл
    with open(filename, "w", encoding="utf-8") as f:
        f.write(pretty_html)

    logging.info(f"HTML saved to {filename}")

def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("app.log"),
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