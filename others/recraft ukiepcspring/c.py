from heapq import heapify, heappop


def solve():
    N, K = read_ints()
    eggs = list(read_ints())

    max_heap = [
        (-v, i)
        for i, v in enumerate(eggs)
    ]
    heapify(max_heap)

    ans = [-1] * N
    root = heappop(max_heap)
    r_v = -root[0]
    r_idx = root[1]
    ans[r_idx] = -1
    layer = [(r_v, r_idx)]

    while max_heap:
        new_layer = []
        for par_v, par_idx in layer:
            if not max_heap:
                break
            for _ in range(2):
                if not max_heap:
                    break
                v, idx = heappop(max_heap)
                v *= -1
                if par_v - v < K:
                    write_int(-1)
                    return
                ans[idx] = par_idx
                new_layer.append((v, idx))

        new_layer.sort(reverse=True)
        layer = new_layer

    write_ints(v + 1 for v in ans)


### Python 3.8-3.13 compatible competitive programming template ###
# 4 Mar 2025 Version
from sys import stdin, stdout
from typing import Callable, Iterable, Iterator, Type

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


def prompt(msg: str, prefix: str = '? ', reader: Callable = read_str) -> str:
    """Writes a string as a line and reads a line. Flushes output buffer.
    Prepends a default prefix to output."""
    swrt(prefix)
    swrt(msg)
    swrt('\n')
    stdout.flush()
    return reader()


# Single-case format
if __name__ == '__main__':
    solve()
