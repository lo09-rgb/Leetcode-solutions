# Binary Tree in Python

## Overview

A Binary Tree is a hierarchical data structure in which each node has at most two children:

- Left Child
- Right Child

Binary Trees are widely used in:

- Searching
- Sorting
- Expression Parsing
- File Systems
- Databases

---

## Tree Structure

Example tree used in this program:

        1
       / \
      2   3
     / \
    4   5

---

## Implementation

Each node contains:

- Data
- Reference to left child
- Reference to right child

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```
