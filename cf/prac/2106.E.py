def solve():
    N, Q = read_ints()
    perm = [0]
    perm.extend(read_ints())  # a permutation of 1..N
    ridx = [0] * (N + 1)
    for i in range(1, N + 1):
        ridx[perm[i]] = i

    for _ in range(Q):
        L, R, K = read_ints()
        target = ridx[K]
        if not L <= target <= R:
            write_int(-1)
            continue

        indices = []
        dirs = []
        l, r = L, R
        while l <= r:
            m = (l + r) // 2
            if m == target:
                break
            indices.append(m)
            if m < target:
                l = m + 1
                dirs.append(-1)  # v < K
            else:
                r = m - 1
                dirs.append(1)  # v > K

        if l > r or not dirs.count(-1) < K <= N - dirs.count(1):
            write_int(-1)
            continue

        pos, neg = 0, 0
        for i, d in zip(indices, dirs):
            v = perm[i]
            if d == -1 and v > K:
                pos += 1
            elif d == 1 and v < K:
                neg += 1

        write_int(max(pos, neg) * 2)


### Python 3.8-3.13 compatible competitive programming template ###
# 11 Mar 2025 Version
from sys import stdin, stdout
from typing import Callable, Iterable, Iterator, Type, TypeVar

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
