from collections import deque
from math import gcd


def solve():
    N = read_int()
    arr = list(read_ints())

    g = arr[0]  # this is the final target value
    for v in arr:
        g = gcd(g, v)

    if g in arr:
        ans = len(arr) - arr.count(g)
        write_int(ans)
        return

    # find fastest way to get g by taking the gcd of elements in arr
    # graph ahh problem
    b = [x // g for x in arr]  # i think this saves speed; target is 1

    dist = {}
    q = deque()
    for v in b:
        if v not in dist:
            dist[v] = 0
            q.append(v)

    go = True
    min_ops = -1
    while q and go:
        u = q.popleft()
        for v in b:
            t = gcd(u, v)
            if t == 1:
                min_ops = dist[u] + 1
                go = False
                break
            if t not in dist:
                dist[t] = dist[u] + 1
                q.append(t)

    if min_ops == -1:  # wtf
        raise RuntimeError
    write_int(min_ops + N - 1)


### Python 3.10-3.13 compatible competitive programming template ###
# 29 May 2025 Version
from collections.abc import Callable, Iterable, Iterator
from sys import stdin, stdout
from typing import Type, TypeVar

T = TypeVar('T')

srdl = stdin.readline
swrt = stdout.write


def read_ints(int_t: Type[int] = int) -> Iterator[int]:
    """Reads a line as space-separated integers"""
    return map(int_t, srdl().split())


def read_int(int_t: Type[int] = int) -> int:
    """Reads a line as a single integer"""
    return int_t(srdl())


def read_str() -> str:
    """Reads a line as-is"""
    return srdl().strip()


def write_ints(arr: Iterable[int]):
    """Writes a list of integers as a space-separated line"""
    swrt(' '.join(map(str, arr)))
    swrt('\n')


def write_int(val: int):
    """Writes a single integer as a line"""
    swrt(str(val))
    swrt('\n')


def write_str(val: str):
    """Writes a single string as a line"""
    swrt(val)
    swrt('\n')


def prompt(msg: str, prefix: str = '? ', reader: Callable[[], T] = read_str) -> T:
    """Writes a string as a line and reads a line. Flushes output buffer.
    Prepends a default prefix to output."""
    swrt(prefix)
    swrt(msg)
    swrt('\n')
    stdout.flush()
    return reader()


# N-Testcases format
if __name__ == '__main__':
    for _ in range(read_int()):
        solve()
