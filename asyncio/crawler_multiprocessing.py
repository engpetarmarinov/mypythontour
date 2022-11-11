from multiprocessing import Pool, cpu_count
import time
from tqdm import tqdm
import requests
from urls import urls


def main():
    with Pool(processes=cpu_count()) as pool:
        jobs = [
            pool.apply_async(func=requests.get, args=(url,))
            for url in urls
        ]
        for job in tqdm(jobs, desc="running crawler_multiprocessing", miniters=1):
            job.get()

        # shutdown the process pool
        pool.close()
        # wait for tasks to complete
        pool.join()


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"main done in {end - start}s")
