from .models import URLReport
from statistics import mean, median


def calculate_stats(reports: list[URLReport]) -> dict:

    success = sum(1 for r in reports if r.error is None)
    failed = sum(1 for r in reports if r.error is not None)

    times = [r.response_time for r in reports if r.response_time is not None]

    if not times:
        return {
            "total": len(reports),
            "success": success,
            "failed": failed,
            "avg_time": None,
            "median_time": None,
            "min_time": None,
            "max_time": None,
        }

    return {
        "total": len(reports),
        "success": success,
        "failed": failed,
        "avg_time": mean(times),
        "median_time": median(times),
        "min_time": min(times),
        "max_time": max(times),
    }