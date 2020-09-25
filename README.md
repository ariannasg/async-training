[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE.md)

# Async Python Training

## Description
Follow a series of tutorials/courses to understand how Concurrency & Parallelism work in Python.

## Python 3 Concurrency With the AsyncIO Module - Tutorial
https://realpython.com/async-io-python/
https://realpython.com/courses/python-3-concurrency-asyncio-module/

This tutorial covers the basics of Asynchronous IO (AsyncIO).
The code for this tutorial lives in the [asynchrony folder](./asynchrony).

Concurrency encompasses both multiprocessing (ideal for CPU-bound tasks) and threading (suited for IO-bound tasks). Multiprocessing is a form of parallelism, with parallelism being a specific type (subset) of concurrency. The Python standard library has offered longstanding support for both of these through its multiprocessing, threading, and concurrent.futures packages.

AsyncIO is not threading, nor is it multiprocessing - is a single-threaded, single-process; it uses cooperative multitasking.

**Parallelism** consists of performing multiple operations at the same time. Multiprocessing is a means to effect parallelism, and it entails spreading tasks over a computer’s central processing units (CPUs, or cores). Multiprocessing is well-suited for CPU-bound tasks.

**Concurrency** is a slightly broader term than parallelism. It suggests that multiple tasks have the ability to run in an overlapping manner. 

**Threading** is a concurrent execution model whereby multiple threads take turns executing tasks. One process can contain multiple threads.


## License
This project is licensed under the terms of the MIT License.
Please see [LICENSE](LICENSE.md) for details.
