from heapq import nlargest


def diameter_tree(root) -> int:
    """A more efficent (than double-DFS) diameter
    algorithm for unweighted trees.
    """
    return _diameter_tree(root)[1]


def _diameter_tree(node) -> tuple[int, int]:
    if not node.children:
        return 0, 0
    heights, paths = zip(map(_diameter_tree, node.children))  # type: tuple[int, ...], tuple[int, ...]

    tmp = nlargest(2, heights)
    if len(tmp) == 1:
        h1, h2 = tmp[0], -1
    else:
        h1, h2 = tmp

    longest = max(max(paths), h1 + h2 + 2)

    return h1 + 1, longest


def diameter_fw(graph: dict[int, list[int]]) -> int:
    """Diameter of a graph using Floyd-Warshall algorithm."""
    N = max(graph) + 1
    dist = [
        [N] * N
        for _ in range(N)
    ]
    for u in graph:
        dist[u][u] = 0
        for v in graph[u]:
            dist[u][v] = 1

    for k in graph:
        for u in graph:
            for v in graph:
                dist[u][v] = min(dist[u][v], dist[u][k] + dist[k][v])

    return max((max(
        filter(lambda x: x != N, row),
        default=-1
    ) for row in dist), default=-1)

