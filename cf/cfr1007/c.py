from collections import defaultdict
from itertools import chain


def solve():
    N, _, E = read_ints()
    graph = defaultdict(list)
    for _ in range(N - 1):
        u, v = read_ints()
        graph[u].append(v)
        graph[v].append(u)

    parent = [0] * (N + 1)
    layers = []
    cur_layer = [E]
    while cur_layer:
        layers.append(cur_layer)
        cur_layer = []
        for u in layers[-1]:
            par = parent[u]
            for v in graph[u]:
                if v == par:
                    continue
                parent[v] = u
                cur_layer.append(v)

    layers.reverse()
    write_ints(chain(*layers))


### Python 3.8-3.13 compatible competitive programming template ###
# 21 Feb 2025 Version
from sys import stdin, stdout
from typing import Iterable, Iterator

srdl = stdin.readline
swrt = stdout.write


def read_ints() -> Iterator[int]:
    """Reads a line as space-separated integers"""
    return map(int, srdl().split())


def read_int() -> int:
    """Reads a line as a single integer"""
    return int(srdl())


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


def prompt(msg: str, prefix: str = '? ') -> str:
    """Writes a string as a line and reads a line. Flushes output buffer.
    Prepends a default prefix to output."""
    swrt(prefix)
    swrt(msg)
    swrt('\n')
    stdout.flush()
    return read_str()


# N-Testcases format
if __name__ == '__main__':
    for _ in range(read_int()):
        solve()
