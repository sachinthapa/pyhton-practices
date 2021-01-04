import requests
import multiprocessing
from codetiming import Timer

session = None

def set_global_session():
    global session
    if not session:
        session = requests.Session()


def download_site(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f'{name} -> {len(response.content)} -> {url}')


def download_all_sites(sites):
    with multiprocessing.Pool(initializer = set_global_session) as pool:
        pool.map(download_site, sites)


if __name__ == "__main__":
    sites = ["https://www.jython.org",
             "http://olympus.realpython.org/dice",
             ] * 10

    with Timer(text="Downloaded in : {:.2f} secs"):
        download_all_sites(sites)
