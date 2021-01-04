add_one = lambda x : x + 1
full_name = lambda fname, lname : f'Full name: {fname} {lname}'

print("Add 1 to 5: ", add_one(5), end = '\n')
print(full_name('Sachin','Thapa'), end = '\n\n')


#Anonymous Functions
lambda x, y : x + y
#print("Anonymous: ", _(5,6)) #in shell 

print('iife: ',  (lambda x, y: x + y) (2, 3))

high_order_function = lambda x, func: x + func(x)

def addition(x):
    return x;

print('lambda as argument: ', high_order_function(5, lambda x : x*x ))
print('function as argument: ',high_order_function(5,addition), end = '\n\n') 

div_zero = lambda x: x / 0
def div_zero(x): return x / 0
#div_zero(2)

sing_exp = (lambda x :
    (x % 2 and 'even' or 'odd'))
print('singexp: ', sing_exp(5))

def full_name(first: str, last: str) -> str:
    return f'{first.title()} {last.title()}'
print(full_name('Sachin','Thapa'))


lambda first, last: first.title() + " " + last.title() 
# SyntaxError with the equivalent lambda function
# lambda first: str, last: str: first.title() + " " + last.title() -> str
 

#Decorators
#my decorator function
def my_decorator(f):
    def wraps(args):
        print(f"Calling my_decorator from {f.__name__}")
        print('returning function')
        return f(args)
    print('returning wraps .....')
    return wraps

@my_decorator
def decorated_function(x):
    print(f"with arg {x}")

decorated_function(5)

def trace(f):
    def wrap(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)
    return wrap

@trace
def addition(x):
    return x+2

addition(3)
print("With lambda decorator ",trace(lambda x : x+2)(2))
print("With lambda decorator ",trace(lambda first: first.title())('sachin'))

# DOC TEST ---------------------------
addtwo = lambda x: x + 2
addtwo.__doc__ = """Add 2 to a number.
    >>> addtwo(2)
    4 
    >>> addtwo(2.2)
    4.2
    >>> addtwo(3) # Should fail
    6
    """
#if __name__ == '__main__':
#    import doctest
#    doctest.testmod(verbose=True)

# DOC TEST --------------------------

num_list = [1,2,3,4,5,6,7,8,9]

def multiply_items(num_list):
    return map(lambda x: x*2, num_list) 

print([num*2 for num in num_list if num%2 == 0])
print(list(multiply_items(num_list)))



























