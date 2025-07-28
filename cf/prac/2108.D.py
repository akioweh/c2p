class Prompter:
    def __init__(self, n: int):
        self._n = n
        self._cnt = 0

    def __getitem__(self, idx: int) -> int:
        if not 0 <= idx < self._n:
            exit(-3)
        if self._cnt == 250:
            exit(-69)
        self._cnt += 1
        return prompt(f'{idx + 1}', reader=read_int)


def solve():
    N, K = read_ints()
    if N == 2 * K:  # half half
        prompt(f'{K} {K}', '! ', lambda: None)
        return

    arr = Prompter(N)
    a_pattern = [arr[i] for i in range(K)]
    b_pattern = [-1] * K
    for i in range(N - K, N):
        b_pattern[i % K] = arr[i]

    for i, (pa, pb) in enumerate(zip(a_pattern, b_pattern)):
        if pa != pb:
            diff_i = i
            break
    else:
        prompt('-1', '! ', lambda: None)
        return

    s_l = 0
    s_r = N // K if N % K > diff_i else N // K - 1
    while s_l < s_r:
        mid = (s_l + s_r) // 2
        if arr[mid * K + diff_i] == a_pattern[diff_i]:
            s_l = mid + 1
        else:
            s_r = mid

    i_r = min(s_l * K + diff_i, N - K)
    i_l = max(i_r - K + 1, K)
    for j in range(i_l, i_r):
        pa, pb = a_pattern[j % K], b_pattern[j % K]
        if pa == pb:
            continue
        if arr[j] == pa:
            i_l = j + 1
        else:
            i_r = j
            break
    if i_l != i_r:
        prompt('-1', '! ', lambda: None)
    else:
        prompt(f'{i_l} {N - i_l}', '! ', lambda: None)


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
