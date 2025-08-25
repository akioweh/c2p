"""
Standard Single-source Shortest Path
"""

from heapq import heappush, heappop


def dijkstra(graph: list[list[tuple[int, float]]], src: int) -> list[float]:
    """O((V + E) log V), no negative weights."""
    N = len(graph)
    dist: list[float] = [float('inf')] * N
    dist[src] = 0
    pq: list[tuple[float, int]] = [(0, src)]
    while pq:
        d, u = heappop(pq)
        if d != dist[u]:
            continue
        for v, w in graph[u]:
            if (nd := d + w) < dist[v]:
                dist[v] = nd
                heappush(pq, (nd, v))
    return dist


def dijkstra_2dmtx(grid: list[list[float]], src: tuple[int, int]) -> list[list[float]]:
    M, N = len(grid), len(grid[0])
    dist = [[float('inf')] * N for _ in range(M)]
    dist[src[0]][src[1]] = 0
    pq: list[tuple[float, tuple[int, int]]] = [(0, src)]
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
    while pq:
        d, (i, j) = heappop(pq)
        if d != dist[i][j]:
            continue
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if not (0 <= ni < M and 0 <= nj < N):
                continue
            w = grid[ni][nj]
            if (nd := d + w) < dist[ni][nj]:
                dist[ni][nj] = nd
                heappush(pq, (nd, (ni, nj)))
    return dist
