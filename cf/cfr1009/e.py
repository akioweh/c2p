from random import randint, seed


def ask(i: int, j: int, k: int) -> int:
    assert i != j and j != k and i != k
    tmp = prompt(f'{i} {j} {k}', reader=read_int)
    assert tmp != -1
    return tmp


def answer(i: int, j: int, k: int):
    write_str(f'! {i} {j} {k}')
    stdout.flush()


def solve():
    N = read_int()
    assert N != -1

    seed()
    vertices = [1, 2, 3]
    for _ in range(75):
        if not (resp := ask(*vertices)):
            answer(*vertices)
            return
        vertices[randint(0, 2)] = resp

    # pray-ium
    answer(*vertices)


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
        stdout.flush()
