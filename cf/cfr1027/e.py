from collections import deque


def solve():
    N = read_int()
    w = list(read_ints())
    graph = [
        []
        for _ in range(N)
    ]
    for _ in range(N - 1):
        _u, _v = read_ints()
        _u -= 1
        _v -= 1
        graph[_u].append(_v)
        graph[_v].append(_u)

    min_s = [maxsize] * N
    max_s = [0] * N
    min_s[0] = max_s[0] = w[0]
    # bfs dp
    q = deque([(0, 0)])
    while q:
        u, prev = q.popleft()
        minw = min_s[u]
        maxw = max_s[u]
        for v in graph[u]:
            if v == prev:
                continue
            max_s[v] = max(w[v] - minw, w[v])
            min_s[v] = min(w[v] - maxw, w[v])
            q.append((v, u))

    write_ints(max_s)


### Python 3.8-3.13 compatible competitive programming template ###
# 11 Mar 2025 Version
from sys import maxsize, stdin, stdout
from typing import Callable, Iterable, Iterator, Type, TypeVar

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
