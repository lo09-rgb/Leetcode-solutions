# Trapping Rain Water

## Problem Statement

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much rainwater can be trapped after raining.

### Example

**Input:**

```python
height = [4,2,0,3,2,5]
```

**Output:**

```text
9
```

---

## Approach

This solution uses **Dynamic Programming** by precomputing two auxiliary arrays:

* **leftMax[]**: Stores the tallest bar to the left (including the current bar).
* **rightMax[]**: Stores the tallest bar to the right (including the current bar).

For every index:

* The maximum water level is determined by the **shorter** of the tallest walls on both sides.
* Water trapped at each position is calculated as:

```text
Water = min(leftMax[i], rightMax[i]) - height[i]
```

The total trapped water is the sum of water stored at every index.

---

## Algorithm

1. Create a `leftMax` array by traversing from left to right.
2. Create a `rightMax` array by traversing from right to left.
3. For every index:

   * Find the minimum of `leftMax[i]` and `rightMax[i]`.
   * Subtract the current height.
   * Add the result to the total trapped water.
4. Return the total.

---

## Complexity Analysis

### Time Complexity

* Building `leftMax` array: **O(n)**
* Building `rightMax` array: **O(n)**
* Calculating trapped water: **O(n)**

**Overall:** `O(n)`

### Space Complexity

* `leftMax` array: **O(n)**
* `rightMax` array: **O(n)**

**Overall:** `O(n)`

---

## Python Implementation

```python
class Solution:
    def trap(self, height):
        n = len(height)

        if n == 0:
            return 0

        leftMax = [0] * n
        rightMax = [0] * n

        leftMax[0] = height[0]

        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax[n - 1] = height[n - 1]

        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        water = 0

        for i in range(n):
            water += min(leftMax[i], rightMax[i]) - height[i]

        return water
```

---

## Key Insight

Water can only be trapped if there is a boundary on both the left and the right.

For every position:

* Find the tallest wall on the left.
* Find the tallest wall on the right.
* The **shorter wall** determines the maximum water level.
* The difference between that water level and the current bar height gives the amount of water trapped at that position.

---

## Example Walkthrough

For:

```text
Height = [4,2,0,3,2,5]
```

| Index | Height | Left Max | Right Max | Water Trapped |
| ----: | -----: | -------: | --------: | ------------: |
|     0 |      4 |        4 |         5 |             0 |
|     1 |      2 |        4 |         5 |             2 |
|     2 |      0 |        4 |         5 |             4 |
|     3 |      3 |        4 |         5 |             1 |
|     4 |      2 |        4 |         5 |             2 |
|     5 |      5 |        5 |         5 |             0 |

**Total Water Trapped = 9**

---

## Learning Outcome

This problem introduces an important Dynamic Programming technique of **precomputing information** to avoid repeated calculations.

Instead of searching for the tallest wall to the left and right for every index (which would take **O(n²)** time), the solution stores these values in advance, reducing the overall complexity to **O(n)**.

The same intuition also leads to the optimal **Two-Pointer** solution, which further reduces the space complexity to **O(1)**.
