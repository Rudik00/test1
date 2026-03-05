def load_urls(filename: str) -> list[str]:

    urls = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            url = line.strip()

            if url:
                urls.append(url)

    return urls