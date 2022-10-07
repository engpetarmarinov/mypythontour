import aiohttp
import asyncio
import time


async def get_url_async(url):
    start_time = time.time()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return resp
    except asyncio.CancelledError:
        print(f"{url} cancelled")
    finally:
        end_time = time.time()
        print(f"get_url_async {url} done in {end_time - start_time}s")


async def main():
    urls = [
        "https://google.com",
        "https://yahoo.com",
        "https://apple.com",
        "https://microsoft.com",
        "https://slavi.bg",
    ]
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(get_url_async(url)))

    await asyncio.gather(*tasks, return_exceptions=False)
    for task in tasks:
        result = await task
        print(result.status)


if __name__ == "__main__":
    start = time.time()
    try:
        asyncio.run(main())
    except Exception as e:
        print(e)
    end = time.time()
    print(f"main done in {end - start}s")  # main done in 1.547325849533081s
