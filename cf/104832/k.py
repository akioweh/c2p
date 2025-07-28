MIN = 0
MAX = 100_000
N_PROBES = 0
X_STEP = 100
MARGIN = 95


def ask(x1: int, y1: int, x2: int, y2: int) -> float:
    global N_PROBES
    N_PROBES += 1
    if N_PROBES > 1024:
        raise RuntimeError('mama i pooed my pants')
    if not all(MIN <= x <= MAX for x in (x1, x2)) or not all(MIN <= y <= MAX for y in (y1, y2)):
        raise RuntimeError('dad i gay')
    return float(input(f'query {x1} {y1} {x2} {y2}\n'))


def solve():
    for guess_x in range(MARGIN, MAX - X_STEP + 1, X_STEP):
        v = ask(guess_x, MIN, guess_x, MAX)
        if v != 0:
            ip_x = guess_x
            ip_x2 = guess_x + X_STEP
            v2 = ask(ip_x2, MIN, ip_x2, MAX)
            if v2 > v:
                v = v2
                ip_x = ip_x2
            break
    else:
        raise RuntimeError('allah akbar')

    min_guess_y, max_guess_y = MIN + MARGIN, MAX - MARGIN
    while min_guess_y + 1 < max_guess_y:
        mid = (min_guess_y + max_guess_y) // 2
        if ask(ip_x, min_guess_y, ip_x, mid) > v / 4:  # circle in the lower half
            max_guess_y = mid
        else:  # circle in the upper half
            min_guess_y = mid

    ip_y = (min_guess_y + max_guess_y) // 2

    x1 = ask(MIN, ip_y, ip_x, ip_y)
    x2 = ask(ip_x, ip_y, MAX, ip_y)
    y1 = ask(ip_x, MIN, ip_x, ip_y)
    y2 = ask(ip_x, ip_y, ip_x, MAX)

    center_x = ip_x + (x2 - x1) / 2
    center_y = ip_y + (y2 - y1) / 2

    center_x = round(center_x)
    center_y = round(center_y)

    diameter = ask(MIN, center_y, MAX, center_y)
    radius = round(diameter / 2)
    write_str(f'answer {center_x} {center_y} {radius}')


### Python 3.8-3.13 compatible competitive programming template ###
# 21 Jan 2025 Version
from sys import stdin, stdout
from typing import Iterable, List, NoReturn

srdl = stdin.readline
swrt = stdout.write


def read_ints() -> Iterable[int]:
    """Reads a line as space-separated integers"""
    return map(int, srdl().split())


def read_int() -> int:
    """Reads a line as a single integer"""
    return int(srdl())


def read_str() -> str:
    """Reads a line as-is"""
    return srdl().strip()


def read_strs() -> List[str]:
    """Reads a line as space-separated strings"""
    return srdl().split()


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


# Single-case format
if __name__ == '__main__':
    solve()
