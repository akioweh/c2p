from bisect import bisect


def n_pairs(x: int) -> int:
    return x * (x - 1) // 2


lktbl = list(map(n_pairs, range(0, 501)))


def gen_ans(K: int, i: int, j: int):
    for offset in range(K):
        yield i, j + offset


def solve():
    K = read_int()
    ans: list[tuple[int, int]] = []

    i, j = -(10 ** 9), -(10 ** 9)
    while K:
        n = bisect(lktbl, K) - 1
        ans.extend(gen_ans(n, i, j))
        K -= lktbl[n]
        i += 420
        j += lktbl[n] + 69

    write_int(len(ans))
    for coord in ans:
        write_ints(coord)


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
