"""This is the best demo to show real async IO
"""

import asyncio


async def main():
    task = asyncio.create_task(submain())
    print("A")
    await asyncio.sleep(1)
    print("B")
    
    value = await task

    print(value)


async def submain():
    print("1")
    await asyncio.sleep(3)
    print("2")
    return "Hello World"


if __name__ == "__main__":
    asyncio.run(main())