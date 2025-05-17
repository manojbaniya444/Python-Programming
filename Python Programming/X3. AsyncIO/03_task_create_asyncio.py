import asyncio

async def fn():
    task = asyncio.create_task(fn2())
    print("This is the start statement in fn1")

    await asyncio.sleep(1)
    print("This is the statement in fn1")

async def fn2():
    print("This is the start in function 2")
    await asyncio.sleep(1)
    print("This is the statement in function 2")

asyncio.run(fn())

# This is the start statement in fn1
# This is the start in function 2
# This is the statement in fn1
# This is the statement in function 2