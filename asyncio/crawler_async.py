import aiohttp
import asyncio
import time


async def get_url_async(url):
    start = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            end = time.time()
            print(f"get_url_async {url} done in {end - start}s")
            return resp


async def main():
    urls = [
        "https://google.com",
        "https://yahoo.com",
        "https://apple.com",
        "https://microsoft.com",
    ]
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(get_url_async(url)))

    for task in tasks:
        result = await task
        print(result.status)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f"main done in {end-start}s")  # main done in 1.547325849533081s

