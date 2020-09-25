#!/usr/bin/env python3
import asyncio
import time


# The syntax `async def` introduces either a native coroutine or
# an asynchronous generator.
# The keyword `await` passes function control back to the event loop (it
# suspends the execution of the surrounding coroutine.)
async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == "__main__":
    s = time.perf_counter()

    # asyncio.run(main()) -> this is Python 3.7
    # the equivalent in lower versions is loop.run_until_complete
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(main())

    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

    loop.close()


async def f():
    pass


async def g():
    # Pause here and come back to g() when f() is ready
    r = await f()
    return r

# it’s required that f() be an object that is awaitable.
# async def ff(x):
#     y = await z(x)  # OK - `await` and `return` allowed in coroutines
#     return y
#
# async def gg(x):
#     yield x  # OK - this is an async generator
#
# async def m(x):
#     yield from gen(x)  # No - SyntaxError
#
# def m(x):
#     y = await
#     z(x)  # Still no - SyntaxError (no `async def` here)
#     return y


# One
# One
# One
# Two
# Two
# Two
# count_async.py executed in 1.00 seconds.
