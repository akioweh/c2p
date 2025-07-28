from itertools import chain, filterfalse


def solve() -> bool:
    N = read_int()
    graph: list[list[int]] = [[]]
    for _ in range(N):
        it = read_ints()
        next(it)  # burn first
        graph.append(list(it))

    in_degree: list[int] = [0] * (N + 1)
    for v in chain(*graph):
        in_degree[v] += 1
    in_degree[0] = N

    u = next(filterfalse(in_degree.__getitem__, range(1, N + 1)))
    for _ in range(N - 1):
        if not u:
            return False
        next_u = None
        for v in graph[u]:
            in_degree[v] -= 1
            if not in_degree[v]:
                if next_u:
                    return False
                next_u = v
        u = next_u

    return True


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
    write_int(int(solve()))
