from app.requester import check_url
from app.models import URLReport


def check_urls(urls: list[str]) -> list[URLReport]:

    reports = []

    for url in urls:
        report = check_url(url)
        reports.append(report)

    return reports