import csv
import json


from dataclasses import asdict
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


def save_json(reports, filename="reports/report.json"):

    data = [asdict(r) for r in reports]

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)