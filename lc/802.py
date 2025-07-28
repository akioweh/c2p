"""
802. Find Eventual Safe States
"""

class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        # answer is set of nodes that never lead to a cycle
        N = len(graph)

        state = [0] * N  # 0: unvisited, 1: visiting, 2: visited

        def safe(u: int) -> bool:
            if state[u] == 1:
                return False
            if state[u] == 2:
                return True

            state[u] = 1
            for v in graph[u]:
                if not safe(v):
                    return False
            state[u] = 2
            return True

        return list(filter(safe, range(N)))
