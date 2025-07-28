def solve():
    N = read_int()
    mat = [
        list(read_ints())
        for _ in range(N)
    ]

    tot_cost = 0
    for lol in range(2):
        cost = list(read_ints())
        if tot_cost == float('inf'):
            break
        diffs = []
        for i in range(1, N):
            diff = [False, False, False]  # [same, same if prev, same if this]
            for vc, vp in zip(mat[i], mat[i - 1]):
                if vc == vp:
                    diff[0] = True
                elif vc == vp + 1:
                    diff[1] = True
                elif vc + 1 == vp:
                    diff[2] = True
                if all(diff):
                    break
            diffs.append(diff)

        dp = [0, cost[0]]  # [did not go up, went up]
        for i in range(1, N):
            if dp[0] == dp[1] == float('inf'):
                break

            ds = diffs[i - 1]
            if not ds[0]:
                temp_dp = [dp[0], dp[1] + cost[i]]
            else:
                temp_dp = [float('inf'), float('inf')]
            if not ds[1]:
                temp_dp[0] = min(temp_dp[0], dp[1])
            if not ds[2]:
                temp_dp[1] = min(temp_dp[1], dp[0] + cost[i])
            dp = temp_dp

        tot_cost += min(dp)
        if lol == 1:
            break

        # transpose matrix
        mat = list(map(list, zip(*mat)))

    if tot_cost == float('inf'):
        write_int(-1)
        return
    write_int(tot_cost)


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
