"""
2493. Divide Nodes Into the Maximum Number of Groups
"""

from collections import defaultdict, deque


class Solution:
    def magnificentSets(self, n: int, edges: list[list[int]]) -> int:
        # any odd-length cycles means -1 (impossible)
        # otherwise answer should be diameter of graph
        # P.S. *sum of diameters of all components, since graph may be disconnected

        graph = defaultdict(list)
        for u, v in edges:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)

        diameter = defaultdict(int)  # diameter of each component
        for k in graph:
            dist = [0] * n  # 0 means not visited
            dist[k] = 1
            q = deque([k])
            component_id = k  # id is the min vertex
            while q:
                u = q.popleft()
                component_id = min(component_id, u)
                for v in graph[u]:
                    if not dist[v]:
                        dist[v] = dist[u] + 1
                        q.append(v)
                    else:  # cycle detected
                        if (dist[u] - dist[v]) % 2 == 0:
                            return -1
            diameter[component_id] = max(max(dist), diameter[component_id])

        return sum(diameter.values()) + n - len(graph)  # add isolated vertices


if __name__ == '__main__':
    temp = Solution()
    print(temp.magnificentSets(
        92,
        [[67,29],[13,29],[77,29],[36,29],[82,29],[54,29],[57,29],[53,29],[68,29],[26,29],[21,29],[46,29],[41,29],[45,29],[56,29],[88,29],[2,29],[7,29],[5,29],[16,29],[37,29],[50,29],[79,29],[91,29],[48,29],[87,29],[25,29],[80,29],[71,29],[9,29],[78,29],[33,29],[4,29],[44,29],[72,29],[65,29],[61,29]]
    ))
