from app.models import URLReport


def calculate_stats(reports: list[URLReport]) -> dict:

    total = len(reports)

    success = 0
    failed = 0

    response_times = []

    for r in reports:

        if r.error is None:
            success += 1

            if r.response_time is not None:
                response_times.append(r.response_time)

        else:
            failed += 1

    success_rate = success / total if total > 0 else 0

    avg_response = (
        sum(response_times) / len(response_times)
        if response_times
        else 0
    )

    return {
        "total": total,
        "success": success,
        "failed": failed,
        "success_rate": success_rate,
        "avg_response_time": avg_response
    }