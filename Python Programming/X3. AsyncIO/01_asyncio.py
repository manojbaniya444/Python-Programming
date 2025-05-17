import asyncio

def greet():
    print("Hi iam here and synchronous.")

async def async_func():
    print("Hi from the async func")
    await asyncio.sleep(1)
    print("This is asynchronous program")
    await asyncio.sleep(1)
    print("Statement in asynchronous programming")
    
couroutine_func = async_func()
asyncio.run(couroutine_func)

greet()

# This is asynchronous program
# Hi from the async func
# after 1s
# Statement in asynchronous programming
# after 1s
# Hi iam here and synchronous.