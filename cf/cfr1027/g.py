def solve():
    N, K = read_ints()
    arr = list(read_ints())

    xp = [
        (v & -v).bit_length() - 1
        for v in arr
    ]

    pfc = [0]  # prefix counts (leftward-insertion)
    for i in range(N):
        v, e = arr[i], xp[i]
        res = 1 << e
        if i and arr[i - 1] % v == 0 and (collision := arr[i - 1] // v).bit_count() == 1:
            res -= (1 << xp[i - 1] - collision.bit_length() + 2) - 1  # collapsing a binary sub-tree of height prev_e - collision
        pfc.append(pfc[-1] + res)

    sfc = [0]  # suffix counts (rightward-insertion)
    for i in reversed(range(N)):
        v, e = arr[i], xp[i]
        res = 1 << e
        if i + 1 < N and arr[i + 1] % v == 0 and (collision := arr[i + 1] // v).bit_count() == 1:
            res -= (1 << xp[i + 1] - collision.bit_length() + 2) - 1
        sfc.append(sfc[-1] + res)
    sfc.reverse()
    sfc.pop()

    # code duplication is king.

    ans = max(pfc[-1], sfc[0])
    for i in range(1, N - 1):
        res = pfc[i + 1] + sfc[i] - (1 << xp[i])  # de-dupli-count
        ans = max(ans, res)

    if ans >= K:
        write_str('YES')
    else:
        write_str('NO')


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
