from app.processor import check_urls
from app.processor import check_urls
from app.reporter import save_csv

def main():

    urls = [
        "https://google.com",
        "https://github.com",
        "https://stackoverflow.com",
        "https://bad-site-123123.com"
    ]

    reports = check_urls(urls)

    save_csv(reports)

    for r in reports:
        print(r)

if __name__ == "__main__":
    main()

