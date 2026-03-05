import csv
from app.models import URLReport


def save_csv(reports: list[URLReport], filename: str = "reports/report.csv") -> None:

    with open(filename, "w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow([
            "url",
            "status_code",
            "response_time",
            "size_bytes",
            "error"
        ])

        for r in reports:
            writer.writerow([
                r.url,
                r.status_code,
                r.response_time,
                r.size_bytes,
                r.error
            ])