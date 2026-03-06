import argparse

from app.reporter import save_csv
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

    args = parser.parse_args()
    urls = load_urls(args.file)
    reports = run_requests(urls)
    save_csv(reports)
    
    stats = calculate_stats(reports)
    print_statistics(stats)


if __name__ == "__main__":
    main()