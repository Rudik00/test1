from app.processor import check_urls
from app.processor import check_urls
from app.reporter import save_csv
from app.loader import load_urls


def main():

    urls = load_urls("data/urls.txt")
    reports = check_urls(urls)

    save_csv(reports)

    for r in reports:
        print(r)

if __name__ == "__main__":
    main()

