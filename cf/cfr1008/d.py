from operator import itemgetter


def solve():
    N = read_int()
    gates = []
    for _ in range(N):
        type_a, a, type_b, b = srdl().split()
        a, b = int(a), int(b)
        gates.append((
            (a, type_a == 'x'),  # True == multiplication; False == addition
            (b, type_b == 'x')
        ))

    max_l = max_r = max_s = (1, 1)
    max_l2_r3 = max_l3_r2 = (1, 1)
    for (a, type_a), (b, type_b) in gates:
        news = []
        for l, r in (max_l, max_r, max_s, max_l2_r3, max_l3_r2):
            new = 0
            if type_a:
                new += l * (a - 1)
            else:
                new += a
            if type_b:
                new += r * (b - 1)
            else:
                new += b
            news.append((l, r + new))
            news.append((l + new, r))
        max_l = max(news, key=itemgetter(0))
        max_r = max(news, key=itemgetter(1))
        max_s = max(news, key=sum)
        max_l2_r3 = max(news, key=lambda x: (x[0] * 2 + x[1] * 3))
        max_l3_r2 = max(news, key=lambda x: (x[0] * 3 + x[1] * 2))

    ans = max(map(sum, (max_l, max_r, max_s, max_l2_r3, max_l3_r2)))
    write_int(ans)


### Python 3.8-3.13 compatible competitive programming template ###
# 4 Mar 2025 Version
from sys import stdin, stdout
from typing import Callable, Iterable, Iterator, Type

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


def prompt(msg: str, prefix: str = '? ', reader: Callable = read_str) -> str:
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
