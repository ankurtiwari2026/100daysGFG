
from typing import List
import heapq

class Solution:
    def findCity(self, n: int, m: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = [[] for _ in range(n)]
        for it in edges:
            adj[it[0]].append((it[1], it[2]))
            adj[it[1]].append((it[0], it[2]))

        city_no = -1
        min_city_count = float('inf')

        for i in range(n):
            dist = [float('inf')] * n
            pq = [(0, i)]
            dist[i] = 0

            while pq:
                distance, node = heapq.heappop(pq)
                for adj_node, adj_weight in adj[node]:
                    if distance + adj_weight < dist[adj_node]:
                        dist[adj_node] = distance + adj_weight
                        heapq.heappush(pq, (dist[adj_node], adj_node))

            count = sum(1 for j in range(n) if dist[j] <= distanceThreshold)
            if count <= min_city_count:
                min_city_count = count
                city_no = i

        return city_no