from bisect import bisect_left, bisect_right


def solve():
    N, K = read_ints()
    pos = [-1]
    pos.extend(v - 1 for v in read_ints())
    offset = [-1]
    offset.extend(read_ints())

    # t=0 equivalent positions
    t0pos_r = [(pos[i] - offset[i]) % K for i in range(N + 1)]
    t0pos_l = [(offset[i] + pos[i]) % K for i in range(N + 1)]

    # sorted by t0pos, so we can bin search to find all could-collide lights
    # and since sort is stable, can bin search again to find first-to-collide
    # or maybe this can just be in one swoop if we do custom comp key
    t0pos_r_idx = list(range(1, N + 1))
    t0pos_l_idx = list(range(1, N + 1))
    t0pos_r_idx.sort(key=t0pos_r.__getitem__)
    t0pos_l_idx.sort(key=t0pos_l.__getitem__)

    def find_next(_pos: int, _offset: int, dir_: bool = True) -> int | None:
        _t0pos = (_pos - _offset) % K if dir_ else (_offset + _pos) % K
        if dir_:
            l = bisect_left(t0pos_r_idx, _t0pos, key=t0pos_r.__getitem__)
            r = bisect_right(t0pos_r_idx, _t0pos, key=t0pos_r.__getitem__)
            if not l < r:
                return None
            res = bisect_right(t0pos_r_idx, _pos, l, r, key=pos.__getitem__)
            if res == r:
                return None
            return -t0pos_r_idx[res]
        else:
            l = bisect_left(t0pos_l_idx, _t0pos, key=t0pos_l.__getitem__)
            r = bisect_right(t0pos_l_idx, _t0pos, key=t0pos_l.__getitem__)
            if not l < r:
                return None
            res = bisect_left(t0pos_l_idx, _pos, l, r, key=pos.__getitem__) - 1
            if res < l:
                return None
            return t0pos_l_idx[res]

    # "next light" linked list ahh.
    next_light: list[int | None] = [None] * (2 * N + 1)
    for light in range(1, N + 1):
        _u_pos = pos[light]
        _u_off = offset[light]
        next_light[light] = find_next(_u_pos, _u_off, True)
        next_light[-light] = find_next(_u_pos, _u_off, False)

    has_out: list[bool] = [False] * (2 * N + 1)
    ends: list[int] = []
    prev_light: list[int | None] = [None] * (2 * N + 1)
    for light in range(1, N + 1):
        for light in (light, -light):
            if (_v := next_light[light]) is not None:
                prev_light[_v] = light
            else:
                has_out[light] = True
                ends.append(light)

    for cur in ends:
        while cur := prev_light[cur]:
            has_out[cur] = True

    _ = read_int()
    for start in read_ints():
        start -= 1
        nxt = find_next(start - 1, -1, True)
        write_str('YES' if nxt is None or has_out[nxt] else 'NO')


### Python 3.10-3.13 compatible competitive programming template ###
# 29 May 2025 Version
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
