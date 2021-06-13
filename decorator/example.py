import functools
import time
import math
import random


def repeat(_func=None, *, num_times = 2):
    print(f"func {_func}")
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for i in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat

def timer(func):
    def wrapper_timer(*args, **kwargs):
        args_repr = [f"{a!r}" for a in args]
        
        kwargs_repr = [f"{k} = {v!r}" for k, v in kwargs.items()]
        print(f"kwargs_repr {kwargs_repr}")

        signature = ",".join(args_repr + kwargs_repr)
        print(f"calling {func.__name__}({signature})")
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"{func.__name__}({signature}) returned {value} in {run_time:.4f} secs")
        return value
    return wrapper_timer

PLUGINS = dict()

def register(func):
    PLUGINS[func.__name__] = func
    return func

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'calling {self.func.__name__} {self.num_calls} times ')
        return self.func(*args, **kwargs)


def my_singleton(cls):
    def wraper_singleton(*args, **kwargs):
        if not wraper_singleton.instance:
            wraper_singleton.instance = cls(*args, **kwargs)
        return wraper_singleton.instance
    wraper_singleton.instance = None
    return wraper_singleton


def cache_test(_func=None):
    def decorator_cache(func):
        def wrapper_cache(*args, **kwargs):
            cache_key = args + tuple(kwargs.items())
            if cache_key not in wrapper_cache.cache:
                wrapper_cache.cache[cache_key] = func(*args, **kwargs)
            return wrapper_cache.cache[cache_key]
        wrapper_cache.cache = dict()
        return wrapper_cache
    return decorator_cache(_func)


def cache(func):
    """Keep a cache of previous function calls"""
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache()


def add_unit(unit):
    def decorator_unit(func):
        func.unit = unit
        return func
    return decorator_unit

# --------------------------------------------------------------------------------

@add_unit("cm")
def volume(value):
    return value * 2

volume_unit = volume(5)
#print(volume.unit)

@cache_test
@CountCalls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


@my_singleton
class Test:
    pass


@timer
def waste_time(repeat, args1, dummy_kwargs = None):
    wasted_sum = 0
    for i in range(repeat):
        wasted_sum += sum([i**2 for i in range(1000)])
    return wasted_sum


my_dict = {'six': 6, 'nine': 9, 'ten': 10}
#waste_time(10,15, dummy_kwargs = my_dict)

math.factorial = timer(math.factorial)

def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))
# approximate_e(5)


@register
def say_bye(name):
    print(f'Bye {name}')


#@register
@repeat()
#@CountCalls
def say_hello(name):
    print(f'Hello {name}')

say_hello("sachin")

# function_name, function_call = random.choice(list(PLUGINS.items()))
# function_call('sachin')


