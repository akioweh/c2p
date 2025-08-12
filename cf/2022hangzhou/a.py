def gcd(a: int, b: int) -> tuple[int, int, int]:
    s, t = 1, 0
    s1, t1 = 0, 1
    r, r1 = a, b
    while r1:
        q = r // r1
        r, r1 = r1, r - q * r1
        s, s1 = s1, s - q * s1
        t, t1 = t1, t - q * t1
    return r, s, t


def solve():
    N, M = read_ints()
    arr = list(read_ints())

    t = sum(arr) % M
    a = N % M
    b = (N * (N + 1) // 2) % M

    # linear combination gcd ahh problem
    g_, s_, t_ = gcd(a, b)
    g, u, v = gcd(g_, M)
    x_ = u * s_
    y_ = u * t_
    z_ = v

    # smallest res so res == t (mod g)
    c = -t % M
    if not c % g:  # yay!
        res = 0
    else:
        res = t % g
    d = (res - t) % M
    k = d // g
    x = x_ * k % M
    y = y_ * k % M

    write_int(res)
    write_ints((x, y))


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
