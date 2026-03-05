from concurrent.futures import ThreadPoolExecutor
from .requester import check_url


def run_requests(urls: list[str], workers: int = 10):

    with ThreadPoolExecutor(max_workers=workers) as executor:
        results = executor.map(check_url, urls)

        return list(results)