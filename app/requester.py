import requests
import logging


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