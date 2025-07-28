from collections import defaultdict


def floyd_warshall(graph: dict[int, list[int]]) -> dict[int, dict[int, float]]:
    """Floyd-Warshall Algorithm for (directed) unweighted graphs."""
    dist = defaultdict(lambda: defaultdict(lambda: float('inf')))
    for u in graph:
        dist[u][u] = 0
        for v in graph[u]:
            dist[u][v] = 1

    for k in graph:
        for u in graph:
            for v in graph:
                dist[u][v] = min(dist[u][v], dist[u][k] + dist[k][v])

    return dist
