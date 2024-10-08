# Debugging function call: Print the function which print all the argument in the function.

def debug(function):
    def wrapper(*args, **kwargs):
        # check the parameter.
        args_value = ", ".join([str(a) for a in args])
        kwargs_value = ", ".join([f"{key}={value}" for key, value in kwargs.items()])
        print(f"Arguments in {function.__name__}: {args_value} | {kwargs_value}")
        return function(*args, **kwargs)
    return wrapper

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}.")
    print("______________________")
    
@debug
def hello(name):
    print(f"Hello, {name}.")
    print("______________________")
    
@debug
def notify():
    print("Notification.")
    print("______________________")

greet("Alice", greeting="Salut")
hello("Bob")
notify()