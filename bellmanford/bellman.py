class Solution:
    def bellmanFord(self, V, edges, src):
        # Step 1: Initialize distances
        dist = [float('inf')] * V
        dist[src] = 0

        # Step 2: Relax all edges V-1 times
        for _ in range(V - 1):
            for u, v, wt in edges:
                if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt

        # Step 3: Check for negative weight cycles
        for u, v, wt in edges:
            if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                return [-1]  # Negative cycle detected

        return dist
