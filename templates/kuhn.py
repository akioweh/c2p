def kuhn(graph: list[list[int]], M: int, rmatch: list[int] | None = None) -> tuple[int, list[int]]:
    N = len(graph)
    if rmatch is None:
        rmatch = [-1] * M

    def match(_u: int) -> bool:
        if seen[_u]:
            return False
        seen[_u] = True
        for _v in graph[_u]:
            if (_w := rmatch[_v]) == -1 or match(_w):
                rmatch[_v] = _u
                return True
        return False

    cnt = 0
    for u in range(N):
        seen = [False] * N
        cnt += match(u)

    return cnt, rmatch


from collections import deque


def kuhn_bfs(graph: list[list[int]], M: int) -> tuple[int, list[int], list[int]]:
    N = len(graph)
    rmatch = [-1] * M
    lmatch = [-1] * N

    def augment_one() -> bool:
        queue: deque[int] = deque()
        parent = [-1] * N
        visited = [False] * N

        for u in range(N):
            if lmatch[u] == -1:
                queue.append(u)
                visited[u] = True

        while queue:
            u = queue.popleft()
            for v in graph[u]:
                w = rmatch[v]
                if w == -1:
                    # flip the alternating path
                    cur_u, cur_v = u, v
                    while cur_u != -1:
                        next_v = lmatch[cur_u]
                        rmatch[cur_v] = cur_u
                        lmatch[cur_u] = cur_v
                        cur_u = parent[cur_u]
                        cur_v = next_v
                    return True
                elif not visited[w]:
                    visited[w] = True
                    parent[w] = u
                    queue.append(w)

        return False

    cnt = 0
    while augment_one():
        cnt += 1

    return cnt, lmatch, rmatch
