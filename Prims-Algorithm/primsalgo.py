import heapq

def prim(graph, start):
    visited = set()
    min_heap = [(0, start)]
    mst_cost = 0
    mst_edges = []

    while min_heap:
        weight, node = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        mst_cost += weight

        for neighbor, edge_weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor))
                mst_edges.append((node, neighbor, edge_weight))

    return mst_cost


graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 5)],
    'D': [('B', 4), ('C', 5)]
}

start_node = 'A'

cost = prim(graph, start_node)

print("Minimum Spanning Tree Cost:", cost)
