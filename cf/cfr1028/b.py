MOD = 998244353


def solve():
    n = read_int()
    p = list(read_ints())
    q = list(read_ints())

    ppfm = []
    cur_max = -1
    for i, v in enumerate(p):
        if v > cur_max:
            ppfm.append(i)
            cur_max = v
        else:
            ppfm.append(ppfm[-1])
    qpfm = []
    cur_max = -1
    for i, v in enumerate(q):
        if v > cur_max:
            qpfm.append(i)
            cur_max = v
        else:
            qpfm.append(qpfm[-1])

    ans = []
    for i in range(n):
        j1 = ppfm[i]
        j2 = i - qpfm[i]

        if j1 == j2:
            j = j1
        else:
            mej1, mej2 = max(p[j1], q[i - j1]), max(p[j2], q[i - j2])
            if mej1 > mej2:
                j = j1
            elif mej2 > mej1:
                j = j2
            else:
                j = max((j1, j2), key=lambda j_: p[j_] + q[i - j_])

        ans.append(
            pow(2, p[j], MOD) + pow(2, q[i - j], MOD) % MOD
        )

    write_ints(ans)


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
