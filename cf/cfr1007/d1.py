from functools import reduce
from operator import xor


class ThisFuckingSequence:
    # adjusted rules for 0-indexing:
    # a[m] = XOR(a[:ceil(m/2)]) = XOR(a[:(m + 1) // 2])

    def __init__(self, initial: list[int]):
        n = len(initial)
        if n % 2 == 0:
            initial.append(reduce(xor, initial[:(n + 1) // 2]))
            n += 1
        self.n = n
        self.initial = initial
        self.xor_n = reduce(xor, initial)

    def __getitem__(self, idx: int) -> int:
        if idx < self.n:
            return self.initial[idx]
        pfx_idx = (idx + 1) // 2
        if pfx_idx < self.n:
            return reduce(xor, self.initial[:pfx_idx])
        if pfx_idx % 2:
            return self.xor_n
        else:
            return self.xor_n ^ self[pfx_idx - 1]


def solve():
    N, l, _ = read_ints()
    X = l - 1
    a = ThisFuckingSequence(list(read_ints()))
    write_int(a[X])


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
