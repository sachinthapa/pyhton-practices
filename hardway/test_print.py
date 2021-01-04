from functools import partial
import sys

redirect = lambda function, stream: partial(function, file=stream)
prefix = lambda function, prefix: partial(function, prefix)
error = prefix(redirect(print, sys.stderr), '[ERROR]')
error('Something went wrong')

def download(url, loog=print):
    loog(f'downloading {url}')

def custom_print(*args):
    print('download.............')

download("my url", lambda msg : print ('[INFO]',msg))

