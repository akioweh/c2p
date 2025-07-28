from bisect import bisect_left, bisect_right


def find_next(arr, val):
    i = bisect_right(arr, val)
    return arr[i] if i != len(arr) else None


def find_prev(arr, val):
    i = bisect_left(arr, val)
    return arr[i-1] if i else None


def solve():
    R, C = read_ints()
    grid = [read_str() for _ in range(R)]

    N_obs = 0
    __r, __c = None, None  # for use when N_obs == 1
    rows = [list() for _ in range(R)]
    cols = [list() for _ in range(C)]
    for i, r in enumerate(grid):
        for j, c in enumerate(r):
            if c == '.':
                continue
            N_obs += 1
            rows[i].append(j)
            cols[j].append(i)
            __r, __c = i, j

    if N_obs == 0:
        print(0)
        return
    if N_obs == 1:
        print(4)
        print(f'N{__c + 1} E{__r + 1} S{__c + 1} W{__r + 1}')
        return

    dir_map_1 = (1, 0, 3, 2)
    dir_map_2 = (3, 2, 1, 0)

    def simulate(_r, _c, _dir):
        obs_encountered = 0
        while True:
            obs = rows[_r] if _dir % 2 else cols[_c]
            if not obs:
                break

            if _dir == 0:  # down
                next_obs = find_next(obs, _r)
            elif _dir == 1:  # left
                next_obs = find_prev(obs, _c)
            elif _dir == 2:  # up
                next_obs = find_prev(obs, _r)
            else:  # right
                next_obs = find_next(obs, _c)

            if next_obs is None:
                break

            obs_encountered += 1
            if _dir % 2:
                obs_r, obs_c = _r, next_obs
            else:
                obs_r, obs_c = next_obs, _c

            _r, _c = obs_r, obs_c
            if grid[obs_r][obs_c] == '/':
                _dir = dir_map_1[_dir]
            else:
                _dir = dir_map_2[_dir]

        if obs_encountered >= N_obs:
            return _r, _c, _dir
        return None

    dir_map = 'NESW'
    for starting_dir in range(4):
        det = starting_dir % 2
        lim = C if det else R
        starting_pos = [None, None]
        starting_pos[det] = lim if starting_dir == 1 or starting_dir == 2 else -1
        for i in range(R if det else C):
            starting_pos[1 - det] = i
            res = simulate(*starting_pos, starting_dir)
            if res:
                other_dir = (res[2] - 2) % 4
                i2 = res[1 - (other_dir % 2)]
                print(2)
                print(f'{dir_map[starting_dir]}{i + 1} {dir_map[other_dir]}{i2 + 1}')
                return

    print(0)


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
