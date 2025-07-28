def solve():
    N, X = read_ints()
    if N == 1:
        write_ints([X])
        return
    if X == 0:
        write_ints([0] * N)
        return
    msb = X.bit_length()
    # least significant continuous set bits
    lsb_cnt = 0
    x = X
    while x & 1:
        lsb_cnt += 1
        x >>= 1
    mex = 1 << lsb_cnt
    mex_len = min(mex, N)
    res = list(range(mex_len))
    res.extend([X] * (N - mex_len))
    if (mex_len - 1).bit_length() < msb:
        res[-1] = X
    write_ints(res)


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
