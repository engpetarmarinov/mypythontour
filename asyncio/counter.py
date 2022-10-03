import time


def counter(name: str):
    for i in range(0, 10):
        print(f"{name}: {i!s}")
        time.sleep(1)


def main():
    for n in range(0, 4):
        counter(f"task{n}")


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"main done in {end-start}s")  # main done in 40.14921569824219s
