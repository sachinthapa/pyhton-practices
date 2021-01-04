import concurrent.futures
import requests
import threading
from codetiming import Timer

thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f'{len(response.content)} -> {url}')


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)


if __name__ == "__main__":
    sites = ["https://www.jython.org",
             "http://olympus.realpython.org/dice",
             ] * 10

    with Timer(text="Downloaded in : {:.2f} secs"):
        download_all_sites(sites)
