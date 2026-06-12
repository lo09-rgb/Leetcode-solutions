class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Cycle detected

        self.parent[root_y] = root_x
        return True


def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  # Sort by weight

    dsu = DSU(n)
    mst_weight = 0
    mst_edges = []

    for u, v, weight in edges:
        if dsu.union(u, v):
            mst_weight += weight
            mst_edges.append((u, v, weight))

    return mst_weight, mst_edges


# Example graph
n = 4

edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

weight, mst = kruskal(n, edges)

print("MST Weight:", weight)
print("Edges in MST:")
for edge in mst:
    print(edge)
