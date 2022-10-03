import asyncio
import time


async def counter_async(name: str):
    for i in range(0, 10):
        print(f"{name}: {i!s}")
        await asyncio.sleep(1)


async def main():
    tasks = []
    for n in range(0, 4):
        tasks.append(asyncio.create_task(counter_async(f"task{n}")))

    for task in tasks:
        await task


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f"main done in {end-start}s")  # main done in 10.012492895126343s

