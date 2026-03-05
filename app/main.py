from app.processor import check_urls
from app.processor import check_urls
from app.reporter import save_csv
from app.loader import load_urls
from app.stats import calculate_stats


def main():

    urls = load_urls("data/urls.txt")
    reports = check_urls(urls)

    save_csv(reports)

    stats = calculate_stats(reports)
    print("\nStatistics:")
    print(stats)

if __name__ == "__main__":
    main()

