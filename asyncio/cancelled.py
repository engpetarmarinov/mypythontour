import asyncio


async def foo():
    await asyncio.sleep(1)
    raise ValueError("Foo value error.")


async def bar():
    try:
        await asyncio.sleep(2)
        return "Bar finished."
    except asyncio.CancelledError:
        print("Bar Cancelled.")


async def main():
    try:
        results = await asyncio.gather(
            foo(), bar(),
            return_exceptions=False
        )
        print(results)
    except ValueError as e:
        print(f"Value Error raised: {e}")

if __name__ == "__main__":
    asyncio.run(main())
