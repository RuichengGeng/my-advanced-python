import asyncio


async def foo(message):
    print(f"foo: {message}")
    await asyncio.sleep(3)


async def main():
    await asyncio.gather(
        foo("A"),
        foo("B"),
        foo("C"),
    )

if __name__ == '__main__':
    asyncio.run(main())