import asyncio


async def counter(name: str):
    for i in range(0, 10):
        print(f"{name}: {i!s}")
        await asyncio.sleep(1)


async def main():
    tasks = []
    for n in range(0, 4):
        tasks.append(asyncio.create_task(counter(f"task{n}")))

    for task in tasks:
        await task


if __name__ == "__main__":
    asyncio.run(main())
