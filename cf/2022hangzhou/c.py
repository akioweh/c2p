NINF = -10000000


def solve():
    N, K = read_ints()
    W = []
    V = []
    for _ in range(N):
        r = list(read_ints())
        W.append(r[0])
        V.append(r)

    prev_r = [NINF] * (K + 1)
    prev_r[0] = 0
    prev_r[W[0]] = V[0][-1]
    L = [prev_r]
    for i in range(1, N):
        cur_r = prev_r.copy()
        for w in range(wi := W[i], K + 1):
            if wi <= w:
                cur_r[w] = max(prev_r[w], prev_r[w - wi] + V[i][-1])
        L.append(cur_r)
        prev_r = cur_r

    prev_r = [NINF] * (K + 1)
    prev_r[0] = 0
    prev_r[W[-1]] = V[-1][-1]
    R = [prev_r]
    for i in range(N - 2, -1, -1):
        cur_r = prev_r.copy()
        for w in range(wi := W[i], K + 1):
            if wi <= w:
                cur_r[w] = max(prev_r[w], prev_r[w - wi] + V[i][-1])
        R.append(cur_r)
        prev_r = cur_r
    R.reverse()

    ans = L[-1][K]

    zeros = [0] * (K + 1)
    for i in range(N):
        left = L[i - 1] if i > 0 else zeros
        right = R[i + 1] if i < N - 1 else zeros
        for w in range(1, W[i]):
            sum_ = K - w  # required sum
            if sum_ < 0:
                continue
            pfs = max((left[j] + right[sum_ - j] for j in range(sum_ + 1)), default=0)
            if pfs < 0:
                continue
            ans = max(ans, V[i][w] + pfs)

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


# Single-case format
if __name__ == '__main__':
    solve()
