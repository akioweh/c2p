def solve():
    # maximum distance pairing... but its on a line so greedy should work (happy face)
    N, M = read_ints()
    rooms = list(read_ints())
    floors = [r // 100 for r in rooms]
    idxs = list(range(M))
    idxs.sort(key=floors.__getitem__)
    h = N // 2
    h1 = N - h
    odd = idxs[:h1] + idxs[-h:]
    even = idxs[-h1:] + idxs[:h]

    for i in range(N):
        r_even = rooms[even[i]]
        r_odd = rooms[odd[i]]
        write_ints((r_even, r_odd, r_even, r_odd, r_even, r_odd))


### Python 3.10-3.13 compatible competitive programming template ###
# 29 May 2025 Version
from collections.abc import Callable, Iterable, Iterator
from sys import stdin, stdout
from typing import Type, TypeVar

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
