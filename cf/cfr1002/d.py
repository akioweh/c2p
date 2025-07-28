from itertools import product
from heapq import heappush, heappop


def solve():
    N, s1, s2 = read_ints()

    G1 = [[] for _ in range(N + 1)]
    M1 = read_int()
    G1_edges = set()
    for _ in range(M1):
        u, v = read_ints()
        G1[u].append(v)
        G1[v].append(u)
        G1_edges.add((u, v) if u < v else (v, u))

    G2 = [[] for _ in range(N + 1)]
    M2 = read_int()
    inter_vertices = set()
    for _ in range(M2):
        u, v = read_ints()
        G2[u].append(v)
        G2[v].append(u)
        if G1_edges.__contains__((u, v) if u < v else (v, u)):
            inter_vertices.add(u)
            inter_vertices.add(v)

    if not inter_vertices:
        write_int(-1)
        return

    # smarty pants way to traverse imaginary graph
    # without constructing its entire self in memory
    O = N + 1
    P = O ** 2
    cost = [[1_420_696_969_666] * (N + 1) for _ in range(N + 1)]
    cost[s1][s2] = 0
    heap = [0 * P + s1 * O + s2]  # tuple comparison slow as SHIT
    while heap:
        temp = heappop(heap)
        c, tmp2 = divmod(temp, P)
        u1, u2 = divmod(tmp2, O)
        if u1 == u2 and u1 in inter_vertices:
            write_int(c)
            return
        if c > cost[u1][u2]:
            continue
        for v1, v2 in product(G1[u1], G2[u2]):
            new_c = c + abs(v1 - v2)
            if new_c < cost[v1][v2]:
                cost[v1][v2] = new_c
                heappush(heap, new_c * P + v1 * O + v2)

    min_cost = min(cost[x][x] for x in inter_vertices)
    if min_cost == 1_420_696_969_666:  # odd cycle lengths
        write_int(-1)
    else:
        write_int(min_cost)


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
