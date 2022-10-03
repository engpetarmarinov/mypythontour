import time
import requests


def get_url_async(url):
    start = time.time()
    res = requests.get(url)
    end = time.time()
    print(f"get_url_async {url} done in {end - start}s")
    return res


def main():
    urls = [
        "https://google.com",
        "https://yahoo.com",
        "https://apple.com",
        "https://microsoft.com",
    ]

    for url in urls:
        result = get_url_async(url)
        print(result.status_code)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"main done in {end-start}s")  # main done in 3.665160894393921s

