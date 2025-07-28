def solve():
    N, X, K = read_ints()
    moves = read_str()

    cum_delta = 0
    min_cycle_len = 0
    dtz = 0
    for i, move in enumerate(moves):
        cum_delta += -1 if move == 'L' else 1
        if cum_delta == 0 and not min_cycle_len:
            min_cycle_len = i + 1
        if cum_delta == -X and not dtz:
            dtz = i + 1
        if min_cycle_len and dtz:
            break

    if not dtz:
        write_int(0)
        return
    if not min_cycle_len:
        write_int(1)
        return

    write_int(1 + (K - dtz) // min_cycle_len)


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
