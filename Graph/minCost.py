import heapq
from collections import defaultdict

class Solution:
    def dijkstra(self, n: int) -> int:
        INF  = 10**9
        vis  = [False] * n
        dist = [INF] * n

        pq: List[Tuple[int, int]] = [(0, 0)]
        dist[0] = 0

        while pq:
            du, u = heapq.heappop(pq)
            if vis[u]:
                continue
            vis[u] = True

            for v, w in self.G[u]:
                nd = du + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))

        return -1 if dist[n - 1] == INF else dist[n - 1]

    def minCost(self, n: int, edges: List[List[int]]) -> int:
        self.G = [[] for _ in range(n)]

        for u, v, w in edges:
            self.G[u].append((v, w))
            self.G[v].append((u, 2 * w))

        return self.dijkstra(n)
sol=Solution()
n = 4
edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]
print(sol.minCost(n,edges))