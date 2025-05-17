import asyncio

async def fn1():
    print("This is the start in function 1.")
    await asyncio.sleep(1)
    await fn2()
    print("This is after the function 2")
    await asyncio.sleep(1)
    
async def fn2():
    print("This is the start in function 2")
    await asyncio.sleep(1)
    print("This is the statement in function 2")

asyncio.run(fn1())

# This is the start in function 1.
# This is the start in function 2
# This is the statement in function 2
# This is after the function 2