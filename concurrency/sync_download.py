import requests
from codetiming import Timer


def download_site(url, session):
    with session.get(url) as response:
        print(f'{len(response.content)} -> {url}')


def download_all_sites(sites):
    with requests.session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    sites = ["https://www.jython.org",
             "http://olympus.realpython.org/dice",
             ] * 10

    with Timer(text="Downloaded in : {:.2f} secs"):
        download_all_sites(sites)
