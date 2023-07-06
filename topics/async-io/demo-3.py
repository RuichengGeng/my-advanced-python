import asyncio


async def func1():
    await asyncio.sleep(2)
    print(1)


async def func2():
    await asyncio.sleep(1)
    print(2)


async def main():
    await asyncio.gather(func1(), func2())
    print("finished")
    return


if __name__ == "__main__":
    asyncio.run(main())
