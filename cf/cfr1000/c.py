from collections import defaultdict


def solve():
    N = read_int()
    connections = defaultdict(int)
    adj_list = defaultdict(list)
    for _ in range(N - 1):
        u, v = read_ints()
        connections[u] += 1
        connections[v] += 1
        adj_list[u].append(v)
        adj_list[v].append(u)

    if N <= 2:
        print(0)
        return

    if N == 3:
        print(1)
        return

    # find most connected node
    nodes = list(connections.keys())
    nodes.sort(key=connections.get, reverse=True)

    # if there is a tie, tiebreak by picking most connected node
    # with the least most connected neighbor
    most_connected1 = nodes[0]
    most_connections = connections[most_connected1]
    r = 1
    while r < N and most_connections == connections[nodes[r]]:
        r += 1
    most_connected1 = min(
        nodes[:r],
        key=lambda n: sum(map(connections.get, adj_list[n]))
    )

    # most_connected1 = max(connections, key=connections.get)
    # print(connections)
    ans = connections[most_connected1]
    del connections[most_connected1]
    # update counts for adjacent nodes
    for neighbor in adj_list[most_connected1]:
        connections[neighbor] -= 1
    # second most connected node
    most_connected2 = max(connections, key=connections.get)

    ans += connections[most_connected2] - 1
    print(ans)



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
