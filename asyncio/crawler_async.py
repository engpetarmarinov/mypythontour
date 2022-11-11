import asyncio
import time
from http_client import HttpClient
from urls import urls
from tqdm import tqdm


async def main(client: HttpClient):
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(client.get_url_async(url)))

    for task in tqdm(tasks, desc="running crawler_async", miniters=1):
        await task

    # await asyncio.gather(*tasks, return_exceptions=False)


if __name__ == "__main__":
    start = time.time()

    asyncio.run(main(HttpClient()))

    end = time.time()
    print(f"main done in {end - start}s")  # main done in 1.547325849533081s
