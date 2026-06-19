# Bellman-Ford Algorithm in Python

## Overview

The Bellman-Ford Algorithm is a shortest path algorithm used to find the minimum distance from a source vertex to all other vertices in a weighted graph.

Unlike Dijkstra's Algorithm, Bellman-Ford can handle **negative edge weights** and can also **detect negative weight cycles**.

---

## Problem Statement

Given:

* `V` vertices
* A list of weighted edges
* A source vertex `src`

Find the shortest distance from the source vertex to every other vertex.

---

## Algorithm

### Step 1: Initialize Distances

Set all distances to infinity except the source vertex.

```python
dist = [float('inf')] * V
dist[src] = 0
```

---

### Step 2: Relax All Edges (V - 1) Times

For every edge `(u, v, wt)`:

```python
if dist[u] != float('inf') and dist[u] + wt < dist[v]:
    dist[v] = dist[u] + wt
```

Repeat this process `V - 1` times.

---

### Step 3: Detect Negative Weight Cycles

Perform one additional relaxation pass.

If any distance can still be reduced:

```python
if dist[u] + wt < dist[v]:
    return [-1]
```

A negative weight cycle exists.

---

## Python Implementation

```python
class Solution:
    def bellmanFord(self, V, edges, src):
        dist = [float('inf')] * V
        dist[src] = 0

        for _ in range(V - 1):
            for u, v, wt in edges:
                if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt

        for u, v, wt in edges:
            if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                return [-1]

        return dist
```

---

## Example

### Input

```python
V = 5

edges = [
    [0, 1, -1],
    [0, 2, 4],
    [1, 2, 3],
    [1, 3, 2],
    [1, 4, 2],
    [3, 2, 5],
    [3, 1, 1],
    [4, 3, -3]
]

src = 0
```

### Output

```python
[0, -1, 2, -2, 1]
```

---

## Why V - 1 Relaxations?

A shortest path in a graph with `V` vertices can contain at most `V - 1` edges.

Therefore:

```text
Maximum edges in shortest path = V - 1
```

Performing `V - 1` relaxation rounds guarantees that the shortest distance information reaches every vertex.

---

## Negative Weight Cycle Example

```text
0 → 1 (1)
1 → 2 (-2)
2 → 0 (-2)
```

Cycle Cost:

```text
1 + (-2) + (-2) = -3
```

Since the total weight is negative, the path cost can decrease indefinitely by repeatedly traversing the cycle.

Bellman-Ford detects this condition during the final cycle-check pass.

---

## Time Complexity

| Operation       | Complexity |
| --------------- | ---------- |
| Edge Relaxation | O(V × E)   |
| Cycle Detection | O(E)       |
| Total           | O(V × E)   |

---

## Space Complexity

```text
O(V)
```

Only a distance array is maintained.

---

## Advantages

* Handles negative edge weights.
* Detects negative weight cycles.
* Simple implementation.
* Works on directed and undirected graphs.

---

## Disadvantages

* Slower than Dijkstra's Algorithm.
* Not suitable for very large dense graphs.

---

## Bellman-Ford vs Dijkstra

| Feature                | Bellman-Ford | Dijkstra   |
| ---------------------- | ------------ | ---------- |
| Negative Edges         | ✅ Yes        | ❌ No       |
| Detect Negative Cycles | ✅ Yes        | ❌ No       |
| Time Complexity        | O(V × E)     | O(E log V) |
| Faster                 | ❌            | ✅          |

---

## Key Takeaway

Bellman-Ford is the preferred shortest path algorithm when a graph contains negative edge weights or when negative cycle detection is required. For graphs with only non-negative weights, Dijkstra's Algorithm is generally more efficient.
