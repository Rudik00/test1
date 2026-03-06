import argparse

from app.reporter import save_csv
from app.reporter import save_json
from app.loader import load_urls
from app.stats import calculate_stats
from app.runner import run_requests
from app.statistics_output import print_statistics


def main():
    parser = argparse.ArgumentParser(description="URL checker")
    parser.add_argument(
        "file",
        help="Path to file with URLs"
    )
    parser.add_argument("--workers", type=int, default=10)
    parser.add_argument("--output", default="report.csv")


    args = parser.parse_args()
    urls = load_urls(args.file)
    reports = run_requests(urls, workers=args.workers)

    save_csv(reports, args.output)
    save_json(reports)
    
    stats = calculate_stats(reports)
    print_statistics(stats)


if __name__ == "__main__":
    main()