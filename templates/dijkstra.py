from heapq import heappush, heappop


def dijkstra(graph: dict[int, list[tuple[int, float]]], start: int) -> list[float]:
    n = len(graph)
    dist: list[float] = [float('inf')] * n
    dist[start] = 0
    heap: list[tuple[float, int]] = [(0, start)]
    while heap:
        d, u = heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heappush(heap, (dist[v], v))
    return dist


def dijkstra_2dmtx(grid: list[list[float]], start: tuple[int, int]) -> list[list[float]]:
    m, n = len(grid), len(grid[0])
    dist = [
        [float('inf')] * n
        for _ in range(m)
    ]
    dist[start[0]][start[1]] = 0
    heap: list[tuple[float, tuple[int, int]]] = [(0, start)]
    while heap:
        d, (i, j) = heappop(heap)
        if d > dist[i][j]:
            continue
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            k, l = i + di, j + dj
            if not (0 <= k < m and 0 <= l < n):
                continue
            w = grid[k][l]
            if d + w < dist[k][l]:
                dist[k][l] = d + w
                heappush(heap, (dist[k][l], (k, l)))
    return dist
