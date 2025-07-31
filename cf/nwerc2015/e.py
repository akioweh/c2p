from bisect import bisect_left


def solve():
    N = read_int()
    eqs = [tuple(read_ints()) for _ in range(N)]
    _res = set()
    __res = []
    for a, b in eqs:
        r = set((a + b, a - b, a * b))
        __res.append(r)
        _res.update(r)
    rhs = list(_res)
    rhs.sort()
    M = len(rhs)
    if M < N:
        write_str('impossible')
        return

    g = [[] for _ in range(N)]
    for i in range(N):
        g[i].extend(bisect_left(rhs, v) for v in __res[i])

    h = [-1] * M

    def match(_u: int) -> bool:
        if seen[_u]:
            return False
        seen[_u] = True
        for _v in g[_u]:
            if (_w := h[_v]) == -1 or match(_w):
                h[_v] = _u
                return True
        return False

    matches = 0
    for u in range(N):
        seen = [False] * N
        matches += match(u)

    if matches != N:
        write_str('impossible')
        return

    rev_h = [-1] * N
    for i, v in enumerate(h):
        if v == -1:
            continue
        rev_h[v] = i

    for i in range(N):
        a, b = eqs[i]
        r = rhs[rev_h[i]]
        if a + b == r:
            sym = '+'
        elif a - b == r:
            sym = '-'
        else:
            sym = '*'
        write_str(f'{a} {sym} {b} = {r}')


### Python 3.10-3.13 compatible competitive programming template ###
# 23 July 2025 Version
from collections.abc import Callable, Iterable, Iterator
from sys import stdin, stdout
from typing import TypeVar

T = TypeVar('T')

srdl = stdin.readline
swrt = stdout.write


def read_ints(int_t: type[int] = int) -> Iterator[int]:
    """Reads a line as space-separated integers"""
    return map(int_t, srdl().split())


def read_int(int_t: type[int] = int) -> int:
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


def prompt(msg: str, prefix: str = '? ', reader: Callable[[], T] = read_str) -> T:  # type: ignore[assignment]
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
