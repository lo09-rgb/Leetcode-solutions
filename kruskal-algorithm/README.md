# Kruskal's Algorithm in Python

## Overview

Kruskal's Algorithm is a greedy algorithm used to find the Minimum Spanning Tree (MST) of a weighted, undirected graph.

A Minimum Spanning Tree is a subset of the graph's edges that:

- Connects all vertices.
- Contains no cycles.
- Has the minimum possible total edge weight.

---

## How the Algorithm Works

1. Sort all edges in ascending order of their weights.
2. Pick the edge with the smallest weight.
3. Check if adding the edge creates a cycle.
4. If no cycle is formed, add the edge to the MST.
5. Repeat until all vertices are connected.

To efficiently detect cycles, Kruskal's Algorithm uses a Disjoint Set Union (DSU), also known as Union-Find.

---

## Example

### Input Graph

```text
(0,1,10)
(0,2,6)
(0,3,5)
(1,3,15)
(2,3,4)
```

### Sorted Edges

```text
(2,3,4)
(0,3,5)
(0,2,6)
(0,1,10)
(1,3,15)
```

### MST Construction

Select (2,3,4)

```text
2 --- 3
```

Select (0,3,5)

```text
0 --- 3 --- 2
```

Skip (0,2,6) because it creates a cycle.

Select (0,1,10)

```text
1 --- 0 --- 3 --- 2
```

### Final MST

```text
(2,3,4)
(0,3,5)
(0,1,10)
```

### Total Weight

```text
19
```

---

## Why Union-Find is Used

Union-Find helps determine whether two vertices already belong to the same connected component.

- Same parent → Adding the edge creates a cycle → Skip it.
- Different parent → Safe to add the edge.

This allows cycle detection in nearly constant time.

---

## Time Complexity

```text
Sorting Edges: O(E log E)

Union-Find Operations: O(E α(V))
```

Overall Complexity:

```text
O(E log E)
```

where:

- E = Number of edges
- V = Number of vertices

---

## Space Complexity

```text
O(V)
```

Used for storing the parent array in the Union-Find data structure.

---

## Concepts Learned

- Graphs
- Minimum Spanning Tree (MST)
- Greedy Algorithms
- Union-Find (Disjoint Set Union)
- Cycle Detection
- Edge Sorting

---

## Key Takeaway

Kruskal's Algorithm builds a Minimum Spanning Tree by repeatedly selecting the smallest available edge that does not form a cycle. By combining edge sorting with Union-Find, it efficiently produces the minimum-cost way to connect all vertices in a graph.
