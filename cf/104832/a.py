def solve():
    N, M = read_ints()
    mat = [
        list(read_str())
        for _ in range(N)
    ]

    ans = 0

    def neighbors(_r, _c):
        for _dr, _dc in (
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
        ):
            _nr, _nc = _r + _dr, _c + _dc
            if not (0 <= _nr < N and 0 <= _nc < M):
                continue
            yield _nr, _nc

    all_paths = set()

    def n_ways(_r, _c, idx, path):
        if idx == len(target):
            all_paths.add(tuple(path))
            return 1
        if mat[_r][_c] != target[idx]:
            return 0

        path.append((_r, _c))

        return sum(
            n_ways(nr, nc, idx + 1, path.copy())
            for nr, nc in neighbors(_r, _c)
        )

    target = 'YOKOHAMA'
    for r in range(N):
        for c in range(M):
            ans += n_ways(r, c, 0, [])

    print(len(all_paths))



### Python 3.8-3.13 compatible competitive programming template ###
# 21 Jan 2025 Version
from sys import stdin, stdout
from typing import Iterable, List

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
