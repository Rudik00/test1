from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from .requester import check_url


def run_requests(urls: list[str], workers: int = 10):

    with ThreadPoolExecutor(max_workers=workers) as executor:
        results = list(
            tqdm(
                executor.map(check_url, urls),
                total=len(urls),
                desc="Checking URLs",
                colour="green",
                ncols=80
            )
        )

    return results