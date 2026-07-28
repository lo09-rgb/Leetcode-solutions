# Rotate Image (LeetCode 48)

## Problem Statement

You are given an `n x n` 2D matrix representing an image.

Rotate the image by **90 degrees clockwise**.

The rotation must be performed **in-place**, meaning you cannot allocate another 2D matrix.

### Example 1

**Input**

```text
[
 [1,2,3],
 [4,5,6],
 [7,8,9]
]
```

**Output**

```text
[
 [7,4,1],
 [8,5,2],
 [9,6,3]
]
```

---

### Example 2

**Input**

```text
[
 [5,1,9,11],
 [2,4,8,10],
 [13,3,6,7],
 [15,14,12,16]
]
```

**Output**

```text
[
 [15,13,2,5],
 [14,3,4,1],
 [12,6,8,9],
 [16,7,10,11]
]
```

---

## Approach

A direct rotation usually requires creating another matrix, but the problem requires an **in-place** solution.

We can achieve this in two steps:

### Step 1: Transpose the Matrix

Swap every element above the main diagonal with its corresponding element below the diagonal.

```
1 2 3
4 5 6
7 8 9
```

becomes

```
1 4 7
2 5 8
3 6 9
```

---

### Step 2: Reverse Every Row

Reverse each row of the transposed matrix.

```
1 4 7
2 5 8
3 6 9
```

becomes

```
7 4 1
8 5 2
9 6 3
```

This is exactly the matrix rotated **90° clockwise**.

---

## Algorithm

1. Find the size `n` of the matrix.
2. Transpose the matrix:
   - For every `i`
   - Swap `matrix[i][j]` with `matrix[j][i]` where `j > i`.
3. Reverse every row.
4. The matrix is now rotated in-place.

---

## Dry Run

### Input

```text
[
 [1,2,3],
 [4,5,6],
 [7,8,9]
]
```

### After Transpose

```text
[
 [1,4,7],
 [2,5,8],
 [3,6,9]
]
```

### After Reversing Rows

```text
[
 [7,4,1],
 [8,5,2],
 [9,6,3]
]
```

---

## Complexity Analysis

### Time Complexity

- Transpose: **O(n²)**
- Reverse each row: **O(n²)**

Overall:

```text
O(n²)
```

---

### Space Complexity

No extra matrix is used.

```text
O(1)
```

---

## Why This Works

A **transpose** swaps rows with columns.

Reversing each row afterward rearranges the columns into their rotated positions, producing a **90° clockwise rotation** while satisfying the **in-place** constraint.

---

## Python Solution

```python
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse every row
        for row in matrix:
            row.reverse()
```

---

## Key Takeaways

- Rotate the matrix **without using extra space**.
- Transpose converts rows into columns.
- Reversing each row completes the clockwise rotation.
- This is the standard optimal solution expected in LeetCode interviews.
