MOD = 10 ** 9 + 7


def rev(x: int, p: int) -> int:
    res = 0
    while x:
        x, r = divmod(x, p)
        res = res * p + r
    return res


def solve():
    N, K = read_ints()
    v_sqrt = int(round(N ** (1 / 2), 8))
    v_cbrt = int(round(N ** (1 / 3), 8))

    ans = 0
    # 4+ digit:          p <= cbrt(N)
    for p in range(2, min(K, v_cbrt) + 1):
        ans += rev(N, p)
        ans = ans - MOD if ans >= MOD else ans

    # 3-digit: cbrt(N) < p <= sqrt(N)
    for p in range(v_cbrt + 1, min(K, v_sqrt) + 1):
        n_, n0 = divmod(N, p)
        n2, n1 = divmod(n_, p)
        ans += p * (p * n0 + n1) + n2
        ans = ans - MOD if ans >= MOD else ans

    # 2-digit: sqrt(N) < p <= N
    l, r = min(K, v_sqrt) + 1, min(K, N) + 1
    s_pn = N * (      # N * sum(range(v_sqrt + 1, N + 1))
            (r - l) * (l + r - 1) // 2
    )
    s_n_div_p = 0     # sum(N // p for p in range(l, r))
    s_pp_n_div_p = 0  # sum(N // p * p**2 for p in range(l, r))
    for x in range(N // (r - 1), N // l + 1):
        p_l = N // (x + 1) + 1
        p_r = N // x
        p_r = min(p_r, K) + 1
        s_n_div_p += x * (p_r - p_l)
        s_pp_n_div_p += x * (
                p_r * (p_r - 1) * (2 * p_r - 1)
                - p_l * (p_l - 1) * (2 * p_l - 1)
        ) // 6
    ans += s_pn - s_pp_n_div_p + s_n_div_p
    ans %= MOD

    # 1-digit:       N < p
    ans += (max(K - N, 0) * N) % MOD
    ans = ans - MOD if ans >= MOD else ans

    write_int(ans)


### Python 3.8-3.13 compatible competitive programming template ###
# 21 Feb 2025 Version
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


def prompt(msg: str, prefix: str = '? ') -> str:
    """Writes a string as a line and reads a line. Flushes output buffer.
    Prepends a default prefix to output."""
    swrt(prefix)
    swrt(msg)
    swrt('\n')
    stdout.flush()
    return read_str()


# N-Testcases format
if __name__ == '__main__':
    for _ in range(read_int()):
        solve()
