import logging
from bs4 import BeautifulSoup


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