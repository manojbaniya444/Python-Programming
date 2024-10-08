# Timing Function Execution: write a decorator that measures the time a function takes to execute

import time

def timer(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f'{function.__name__} took {end - start} seconds to execute')
        return result
    return wrapper # returning for decorator

def example_function(n):
    time.sleep(n)
    
# using manually
example_function = timer(example_function)
print(example_function.__name__) # we are getting wrapper function
example_function(2) # this 2 goes in args and kwargs at first and then in n.

# using the decorator
@timer
def example_function(n):
    time.sleep(n)
    
example_function(2)