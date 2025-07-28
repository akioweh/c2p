from operator import itemgetter


def base26_decomp(_v: int) -> tuple[int, int, int, int]:
    tmp, d = divmod(_v, 26)
    tmp, c = divmod(tmp, 26)
    a, b = divmod(tmp, 26)
    return a, b, c, d


def solve():
    N = read_int()

    base26_range = list(map(base26_decomp, range(N)))

    def ask(idx: int) -> Iterator[int]:
        print('? ', end='')
        resp = prompt(''.join(
            chr(v + 97) for v in map(itemgetter(idx), base26_range)
        ))
        return (ord(ch) - 97 for ch in resp)

    A, B, C = 26 ** 3, 26 ** 2, 26
    inverse_ans = [
        A * a + B * b + C * c + d
        for a, b, c, d in zip(*map(ask, range(4)))
    ]
    ans = list(range(N))
    ans.sort(key=inverse_ans.__getitem__)

    print('! ', end='')
    write_ints(v + 1 for v in ans)


### Python 3.8-3.13 compatible competitive programming template ###
# 11 Feb 2025 Version
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


def prompt(msg: str) -> str:
    """Writes a string as a line and reads a line. Flushes buffer."""
    swrt(msg)
    swrt('\n')
    stdout.flush()
    return srdl().strip()


# Single-case format
if __name__ == '__main__':
    solve()
