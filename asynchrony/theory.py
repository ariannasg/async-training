import time
from random import randint


# This function is a generator because it contains "yield". The generator will run
# up until the yield point, it stops executing and when we call next() again, then
# it resumes execution again until the next iteration until it's done -> StopIteration exception
def odds(start, stop):
    for odd in range(start, stop + 1, 2):
        yield odd


def randn():
    time.sleep(3)
    return randint(1, 10)


def main():
    odd_values = [odd for odd in odds(3, 15)]
    odds2 = tuple(odds(21, 29))
    print(odd_values, odds2)


if __name__ == '__main__':
    main()

# Console output:
# [3, 5, 7, 9, 11, 13, 15] (21, 23, 25, 27, 29)

# Using interactive Python (ipython):
# (.venv) -> ipython -i asynchrony/theory.py
# In [1]: whos
# Variable   Type        Data/Info
# --------------------------------
# odds       function    <function odds at 0x110e1a158>
# In [2]: odds(3, 15)
# Out[2]: <generator object odds at 0x110e1f5c8>
# In [3]: g =  odds(3, 15)
# In [4]: next(g)
# Out[4]: 3
# In [5]: next(g)
# Out[5]: 5
# In [6]: next(g)
# Out[6]: 7
# In [7]: next(g)
# Out[7]: 9
# In [8]: next(g)
# Out[8]: 11
# In [9]: next(g)
# Out[9]: 13
# In [10]: next(g)
# Out[10]: 15
# In [11]: next(g)
# ---------------------------------------------------------------------------
# StopIteration                             Traceback (most recent call last)
# <ipython-input-11-e734f8aca5ac> in <module>
# ----> 1 next(g)
# StopIteration:
# In [12]: g = odds(7, 21)
# In [13]: list(g)
# Out[13]: [7, 9, 11, 13, 15, 17, 19, 21]

# In [1]: whos
# Variable   Type        Data/Info
# --------------------------------
# asyncio    module      <module 'asyncio' from '/<...>3.6/asyncio/__init__.py'>
# main       function    <function main at 0x103e0d7b8>
# odds       function    <function odds at 0x103e0d158>
# randint    method      <bound method Random.rand<...>bject at 0x7f89b281a418>>
# randn      function    <function randn at 0x103e0d730>
# time       module      <module 'time' (built-in)>
# In [2]: randn()
# Out[2]: 6
# In [3]: %time randn()
# CPU times: user 574 µs, sys: 1.3 ms, total: 1.88 ms
# Wall time: 3 s
# Out[3]: 9
# In [4]: %time [randn() for _ in range(3)]
# CPU times: user 431 µs, sys: 852 µs, total: 1.28 ms
# Wall time: 9.01 s
# Out[4]: [9, 6, 8]
