import asyncio
import time


async def foo():
    try:
        await asyncio.sleep(1)
        raise ValueError("Foo value error")
        return "Foo finished"
    except asyncio.CancelledError:
        print("Foo Cancelled.")


async def bar():
    try:
        await asyncio.sleep(2)
        return "Bar finished"
    except asyncio.CancelledError:
        print("Bar Cancelled.")


async def main():
    foo_task = asyncio.create_task(foo(), name="Exception task")
    bar_task = asyncio.create_task(bar(), name="Waiting task")
    await asyncio.gather(
        foo_task, bar_task,
        return_exceptions=False
    )
    foo_result = await foo_task
    bar_result = await bar_task
    print(f"foo_result {foo_result}")
    print(f"bar_result {bar_result}")


if __name__ == "__main__":
    start = time.time()
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Exception caught: {e}")
    else:
        end = time.time()
        print(f"execution took {end-start}s")
