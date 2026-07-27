# Spiral Matrix

## Problem Statement

Given an `m x n` matrix, return all elements of the matrix in **spiral order**.

### Example 1

**Input**

```text
matrix = [
 [1,2,3],
 [4,5,6],
 [7,8,9]
]
```

**Output**

```text
[1,2,3,6,9,8,7,4,5]
```

---

### Example 2

**Input**

```text
matrix = [
 [1,2,3,4],
 [5,6,7,8],
 [9,10,11,12]
]
```

**Output**

```text
[1,2,3,4,8,12,11,10,9,5,6,7]
```

---

## Approach

The solution uses **four pointers (boundaries)** to represent the current layer of the matrix:

- `top` → First remaining row
- `bottom` → Last remaining row
- `left` → First remaining column
- `right` → Last remaining column

At every iteration, we traverse the outer layer in four steps:

1. Move **left → right** across the top row.
2. Move **top → bottom** along the right column.
3. Move **right → left** across the bottom row (if it still exists).
4. Move **bottom → top** along the left column (if it still exists).

After completing one layer, the boundaries are updated inward:

- `top += 1`
- `bottom -= 1`
- `left += 1`
- `right -= 1`

This process continues until all elements have been visited.

---

## Algorithm

1. Initialize four boundaries:
   - `top = 0`
   - `bottom = rows - 1`
   - `left = 0`
   - `right = cols - 1`
2. Repeat while `top <= bottom` and `left <= right`:
   - Traverse the top row.
   - Traverse the right column.
   - Traverse the bottom row if it exists.
   - Traverse the left column if it exists.
3. Return the collected elements.

---

## Complexity Analysis

### Time Complexity

**O(m × n)**

Every element in the matrix is visited exactly once.

### Space Complexity

**O(1)** extra space (excluding the output list).

---

## Key Concepts

- Matrix Traversal
- Simulation
- Boundary Pointers
- Two-Dimensional Arrays

---

## Edge Cases Handled

- Empty matrix
- Single row matrix
- Single column matrix
- Square matrices
- Rectangular matrices
- Odd and even dimensions

---

## LeetCode

**Problem:** Spiral Matrix

**Difficulty:** Medium

**Tags:** `Array`, `Matrix`, `Simulation`
