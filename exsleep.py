import time
import urllib.request
import urllib.error

def sleep(timeout, retry=3):
    def the_real_decorator(function):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < retry:
                try:
                    value = function(*args, **kwargs)
                    if value is None:
                        return
                except:
                    print(f'Sleeping for {timeout} seconds')
                    time.sleep(timeout)
                    retries += 1
        return wrapper
    return the_real_decorator

@sleep(10)
def uptime_bot(url):
    try:
        conn = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        # Email admin / log
        print(f'HTTPError: {e.code} for {url}')
        # Re-raise the exception for the decorator
        raise urllib.error.HTTPError
    except urllib.error.URLError as e:
        # Email admin / log
        print(f'URLError: {e.code} for {url}')
        # Re-raise the exception for the decorator
        raise urllib.error.URLError
    else:
        # Website is up
        print(f'{url} is up')

@sleep(4)
def sleep_test():
    raise urllib.error.URLError

if __name__ == "__main__":
    sleep_test()
#    uptime_bot('http://www.google.com/py') 
