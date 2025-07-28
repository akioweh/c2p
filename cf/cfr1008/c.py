"""
I cannot read.
I did not see that all elements of b are <= 10^9.
I thought the 10**18 bound was both for b AND a.
Since b's bound is low enough,

WE COULD JUST WILLY NILLY SUM UP B TO GET X
and it will be within bounds.
AEFIJAWEOIAWI;EJFAWEBFALIWUFHALWIEUALWEUFHALWE J
"""

from itertools import chain


def solve():
    N = read_int()
    nums = list(read_ints())
    nums.sort()
    x = nums.pop()  # largest
    pos, neg = nums[:N - 1], nums[N - 1:]
    z = sum(pos, start=0) - sum(neg)
    # x = z + c
    pos.append(x - z)
    print(x, end=' ')
    write_ints(chain(*zip(pos, neg)))


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


# N-Testcases format
if __name__ == '__main__':
    for _ in range(read_int()):
        solve()
