import requests
import time
from app.models import URLReport


def check_url(url: str, timeout: int = 10) -> URLReport:
    try:
        start = time.perf_counter()

        response = requests.get(url, timeout=timeout)

        end = time.perf_counter()
        response_time = end - start

        size_bytes = len(response.content)

        return URLReport(
            url=url,
            status_code=response.status_code,
            response_time=response_time,
            size_bytes=size_bytes,
            error=None
        )

    except requests.RequestException as e:

        return URLReport(
            url=url,
            status_code=None,
            response_time=None,
            size_bytes=None,
            error=str(e)
        )