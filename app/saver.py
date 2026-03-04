from pathlib import Path
from bs4 import BeautifulSoup

import logging


def save_pretty_html(response: requests.Response, filename="html.txt") -> None:
    """
    Сохраняет HTML в папку reports/ в красивом виде.
    """
    logging.info("Formatting HTML")

    soup = BeautifulSoup(response.text, "html.parser")
    pretty_html = soup.prettify()

    logging.info("HTML formatted successfully")

    # Путь к папке reports (рядом с app/)
    base_dir = Path(__file__).resolve().parent.parent
    reports_dir = base_dir / "reports"
    reports_dir.mkdir(exist_ok=True)  # создаст папку если её нет

    file_path = reports_dir / filename

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(pretty_html)

    logging.info(f"HTML saved to {file_path}")