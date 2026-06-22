# Container With Most Water

## Problem Statement

You are given an integer array `height` of length `n`.

There are `n` vertical lines drawn such that the two endpoints of the `i-th` line are `(i, 0)` and `(i, height[i])`.

Find two lines that, together with the x-axis, form a container that can hold the maximum amount of water.

Return the maximum amount of water a container can store.

**Note:** The container cannot be slanted.

---

## Example

### Input

```python
height = [1,8,6,2,5,4,8,3,7]
```

### Output

```python
49
```

### Explanation

The maximum area is formed between the lines at indices `1` and `8`.

```text
Width  = 8 - 1 = 7
Height = min(8, 7) = 7

Area = 7 × 7 = 49
```

---

# Approach

## Brute Force

A straightforward approach is to check every possible pair of lines.

```python
for i in range(n):
    for j in range(i + 1, n):
        area = (j - i) * min(height[i], height[j])
```

This takes:

* Time Complexity: **O(n²)**
* Space Complexity: **O(1)**

Since every pair is examined, this approach becomes inefficient for large inputs.

---

# Optimized Approach: Two Pointers

## Key Observation

The area of water stored is:

```python
area = width × min(left_height, right_height)
```

Where:

```python
width = right - left
```

To maximize the area:

* We want a large width.
* We want a large minimum height.

---

## Idea

Start with the widest possible container:

```python
left = 0
right = n - 1
```

At each step:

1. Calculate the current area.
2. Update the maximum area found.
3. Move the pointer pointing to the shorter line.

### Why Move the Shorter Line?

Suppose:

```python
height[left] < height[right]
```

The current area is limited by `height[left]`.

Moving the taller line inward only decreases the width while keeping the limiting height unchanged or smaller.

Therefore, moving the taller line can never produce a better result.

The only chance to increase the area is by finding a taller line than the current shorter one.

---

# Algorithm

1. Initialize two pointers:

   * `left = 0`
   * `right = n - 1`

2. Initialize `max_area = 0`.

3. While `left < right`:

   * Compute current width.
   * Compute current area.
   * Update maximum area.
   * Move the pointer at the shorter height inward.

4. Return `max_area`.

---

# Dry Run

Input:

```python
height = [1,8,6,2,5,4,8,3,7]
```

### Iteration 1

```python
left = 0
right = 8

width = 8
area = 8 × min(1,7)
     = 8
```

Move `left`.

---

### Iteration 2

```python
left = 1
right = 8

width = 7
area = 7 × min(8,7)
     = 49
```

Maximum area becomes:

```python
49
```

Move `right`.

---

### Remaining Iterations

The algorithm continues shrinking the window while updating the answer.

No larger area is found.

Final answer:

```python
49
```

---

# Code

```python
class Solution:
    def maxArea(self, height: list[int]) -> int:

        left = 0
        right = len(height) - 1

        max_area = 0

        while left < right:

            width = right - left
            current_area = width * min(height[left], height[right])

            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
```

---

# Complexity Analysis

### Time Complexity

```python
O(n)
```

Each pointer moves at most `n` times.

---

### Space Complexity

```python
O(1)
```

Only a few variables are used regardless of input size.

---

# Key Takeaways

* The area depends on both width and the shorter wall.
* Start with the maximum possible width.
* Always move the pointer at the shorter wall.
* This eliminates unnecessary comparisons and reduces the complexity from **O(n²)** to **O(n)**.
* A classic and highly important **Two Pointer** problem frequently asked in coding interviews.
