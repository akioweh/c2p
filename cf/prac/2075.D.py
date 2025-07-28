from bisect import bisect_left
from itertools import accumulate

A_PFS = list(accumulate(range(64)))


def calc_two(a: int, b: int) -> int:
    i = bisect_left(A_PFS, a + b)
    ans = (1 << i) - 1 << 1
    if A_PFS[i] != a + b:
        ans ^= 1 << A_PFS[i] - (a + b)
    # edge cases
    if a in (1, 2) and not ans & a << 1:
        if a == 1 and ans.bit_count() > 1:  # edgier case
            ans += 1 << ans.bit_length() - 1
            ans -= 1 << 1
        else:
            return maxsize
    return ans


def solve():
    X, Y = read_ints()
    if X > Y:
        X, Y = Y, X
    lx, ly = X.bit_length(), Y.bit_length()
    lcp = lx - (X ^ Y >> ly - lx).bit_length()

    anss = []
    for _lcp in range(lcp, max(lcp - 3, -1), -1):
        a = lx - _lcp
        b = ly - _lcp
        anss.append(calc_two(a, b))
        if _lcp <= 0:
            anss.append(calc_two(a + 1, b))

    write_int(min(anss))


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
