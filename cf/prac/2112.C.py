from bisect import bisect_left, bisect_right


def solve():
    N = read_int()
    nums = list(read_ints())
    # nums.sort()
    MAX = nums[-1]
    ans = 0
    for ia in range(N - 2):
        a = nums[ia]
        ib = ia + 1
        b = nums[ib]
        l = bisect_right(nums, MAX - (a + b), ib + 1)
        r = bisect_left(nums, a + b, ib + 1)
        if l < r:
            ans += r - l
        for ib in range(ia + 2, N - 1):
            b = nums[ib]
            if l <= ib:
                l = ib + 1
            else:
                while l - 1 > ib and nums[l - 1] + a + b > MAX:
                    l -= 1
            while r < N and nums[r] < a + b:
                r += 1
            if l < r:
                ans += r - l

    write_int(ans)


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


# N-Testcases format
if __name__ == '__main__':
    for _ in range(read_int()):
        solve()
