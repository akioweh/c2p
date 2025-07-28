from operator import sub


def solve():
    N, M = read_ints()
    ns = list(read_ints())
    ms = list(read_ints())

    ns.sort()
    ms.sort()
    n_pairs = list(map(sub, ns[:(N - 1) // 2:-1], ns))
    m_pairs = list(map(sub, ms[:(M - 1) // 2:-1], ms))
    n_pairs.append(0)
    m_pairs.append(0)

    max_ops = min(N, M, (N + M) // 3)  # k_max
    n_idx, m_idx = 0, 0  # current index for n_pairs and m_pairs
    ans = []
    this_ans = 0
    for k in range(max_ops):
        if n_idx == N - k:
            n_idx -= 1
            this_ans -= n_pairs[n_idx]
            this_ans += m_pairs[m_idx] + m_pairs[m_idx + 1]
            m_idx += 2
        elif m_idx == M - k:
            m_idx -= 1
            this_ans -= m_pairs[m_idx]
            this_ans += n_pairs[n_idx] + n_pairs[n_idx + 1]
            n_idx += 2
        else:
            cur_n_pts = n_pairs[n_idx] if n_idx * 2 + m_idx + 1 < N else 0
            cur_m_pts = m_pairs[m_idx] if m_idx * 2 + n_idx + 1 < M else 0
            if cur_n_pts > cur_m_pts:
                this_ans += n_pairs[n_idx]
                n_idx += 1
            else:
                this_ans += m_pairs[m_idx]
                m_idx += 1

        ans.append(this_ans)

    write_int(max_ops)
    if max_ops:
        write_ints(ans)


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


# N-Testcases format
if __name__ == '__main__':
    for _ in range(read_int()):
        solve()
