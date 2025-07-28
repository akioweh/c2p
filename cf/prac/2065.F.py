"""
for x to be the majority in a seq of len n,
count(X) > n // 2
-> there is more than 1 x for every other _ (non-x value)
-> at least one pair of x's are adjacent to each other
-> this pair, or length 2 seq of [x, x], is in fact a seq where x IS the majority.
Therefore, it suffices to check for any value v wehther two nodes both valued v are adjacent.


^^^ im fucking ritardando that's only valid where n is even.
to make it also work for where n is odd, we need to check for [x, _, x] patterns too.
"""

from collections import defaultdict
from random import getrandbits


class hish(int):
    salt = getrandbits(64)
    def __hash__(self):
        return super().__hash__() ^ hish.salt


def solve():
    N = read_int()
    value = [0]
    value.extend(map(hish, read_ints()))
    neighbor_values = defaultdict(set)
    valid = [0] * (N + 1)
    for _ in range(N - 1):
        u, v = read_ints()
        val_u = value[u]
        val_v = value[v]
        if val_u == val_v:  # first case i thought of
            valid[val_u] = 1
            continue
        # patch to make it work for odd seq lengths
        if val_u in neighbor_values[v]:
            valid[val_u] = 1
        else:
            neighbor_values[v].add(val_u)
        if val_v in neighbor_values[u]:
            valid[val_v] = 1
        else:
            neighbor_values[u].add(val_v)

    it = iter(valid)
    next(it)
    write_str(''.join(map(str, it)))


### Python 3.8-3.13 compatible competitive programming template ###
# 11 Feb 2025 Version
from sys import stdin, stdout
from typing import Iterable

srdl = stdin.readline
swrt = stdout.write


def read_ints() -> Iterable[int]:
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


def prompt(msg: str) -> str:
    """Writes a string as a line and reads a line. Flushes buffer."""
    swrt(msg)
    swrt('\n')
    stdout.flush()
    return srdl().strip()


# N-Testcases format
if __name__ == '__main__':
    for _ in range(read_int()):
        solve()
