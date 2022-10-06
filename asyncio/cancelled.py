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
        """
        return_exceptions
        When this parameter is set to True, the function returns a list of both values and exceptions; 
        allowing all tasks to complete before returning. 
        As all tasks have been completed they are removed from the event loop.
        
        If return_exceptions is set to False (the default value) then asyncio.gather returns immediately, 
        throwing the exception into the calling coroutine. 
        Any task which has not been terminated will remain on the event loop.
        """
        results = await asyncio.gather(
            foo(), bar(),
            return_exceptions=False
        )
        print(results)
    except ValueError as e:
        print(f"Value Error raised: {e}")

if __name__ == "__main__":
    asyncio.run(main())
