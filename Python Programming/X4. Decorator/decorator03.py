# Cache Return Value: decorator that cache the return value of a function so when called with same argument, the cache value return instead of re-executing the function.

import time

def cache(function):
    cache = {}
    def wrapper(*args, **kwargs):
        # if the argument is same just return the cache value.
        # print(type(args))
        print(f"Cache arg: {cache}")
        
        # if the same argument is in cache use it
        if args in cache:
            print(f"Using cache for {args}")
            return cache[args]
        
        # if not found in cache use the function to calculate
        print(f"{args} Not found in cache.")
        result = function(*args, **kwargs)
        cache[args] = result
        return result
    
    # return the wrapper function
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(5)
    return a + b

@cache
def getMax(a, b):
    time.sleep(2)
    return max(a, b)

result1 = long_running_function(2, 3)
print("sum", result1)
print("______________________________")

result2 = long_running_function(2, 3)
print("sum", result2)
print("______________________________")

result3 = long_running_function(3, 4)
print("sum", result3)
print("______________________________")

result4 = long_running_function(3, 4)
print("sum", result4)
print("______________________________")

result5 = long_running_function(2, 3)
print("sum", result5)
print("______________________________")


result6 = getMax(2, 3)
print('max', result6)
print("______________________________")

result7 = getMax(2, 3)
print("max", result7)