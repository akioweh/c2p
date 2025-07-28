from heapq import nlargest, nsmallest
from operator import itemgetter


def solve():
    N = read_int()
    points: list[tuple[int, int]] = []
    for _ in range(N):
        x, y = read_ints()
        points.append((x, y))

    if N <= 2:
        write_int(N)
        return

    min_x, min_x1 = nsmallest(2, points, key=itemgetter(0))
    max_x, max_x1 = nlargest(2, points, key=itemgetter(0))
    min_y, min_y1 = nsmallest(2, points, key=itemgetter(1))
    max_y, max_y1 = nlargest(2, points, key=itemgetter(1))
    lolz = {
        min_x, min_x1,
        max_x, max_x1,
        min_y, min_y1,
        max_y, max_y1,
    }

    def calc_area(ps: set[tuple[int, int]]):
        _min_x = min(ps, key=itemgetter(0))[0]
        _min_y = min(ps, key=itemgetter(1))[1]
        _max_x = max(ps, key=itemgetter(0))[0]
        _max_y = max(ps, key=itemgetter(1))[1]
        _lx, _ly = _max_x - _min_x + 1, _max_y - _min_y + 1
        if _lx * _ly < N:
            if _lx > _ly:
                _lx += 1
            else:
                _ly += 1
        return _lx * _ly

    ans = min(
        calc_area(lolz - {p})
        for p in ((-1, -1), min_x, max_x, min_y, max_y)
    )
    write_int(ans)


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
