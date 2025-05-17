import asyncio

async def func1():
    print("Function 1 started..")
    await asyncio.sleep(2)
    print("Function 1 Ended")
    return 1


async def func2():
    print("Function 2 started..")
    await asyncio.sleep(3)
    print("Function 2 Ended")
    return 2


async def func3():
    print("Function 3 started..")
    await asyncio.sleep(1)
    print("Function 3 Ended")
    return 3


async def main():
    L = await asyncio.gather(
        func1(),
        func2(),
        func3(),
    )
    for r in L:
        print(f"output: {r}")
    print("Main Ended..")

asyncio.run(main())