from app.reporter import save_csv
from app.loader import load_urls
from app.stats import calculate_stats
from app.runner import run_requests
from app.statistics_output import print_statistics


def main():

    urls = load_urls("data/urls.txt")
    reports = run_requests(urls)

    save_csv(reports)

    stats = calculate_stats(reports)
    print_statistics(stats)

if __name__ == "__main__":
    main()