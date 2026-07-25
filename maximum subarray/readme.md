# Maximum Subarray (Kadane's Algorithm)

## Problem Statement

Given an integer array `nums`, find the **contiguous subarray** (containing at least one number) that has the **largest sum**, and return its sum.

### Example

**Input:**
```python
nums = [-2,1,-3,4,-1,2,1,-5,4]
```

**Output:**
```python
6
```

**Explanation:**

The subarray `[4, -1, 2, 1]` has the largest sum:

```
4 + (-1) + 2 + 1 = 6
```

---

# Approach

This problem is solved using **Kadane's Algorithm**, a greedy algorithm that computes the maximum subarray sum in a single traversal of the array.

At every index, we decide between two choices:

1. **Start a new subarray** from the current element.
2. **Extend the previous subarray** by adding the current element.

The better of these two choices becomes the current running sum.

---

# Algorithm

1. Initialize:
   - `current_sum` = first element
   - `max_sum` = first element

2. Traverse the array from the second element.

3. For every element:
   - Update the running sum:
     ```python
     current_sum = max(nums[i], current_sum + nums[i])
     ```
   - Update the maximum sum found so far:
     ```python
     max_sum = max(max_sum, current_sum)
     ```

4. Return `max_sum`.

---

# Dry Run

For:

```python
nums = [-2,1,-3,4,-1,2,1,-5,4]
```

| Current Element | Current Sum | Maximum Sum |
|----------------:|------------:|------------:|
| -2 | -2 | -2 |
| 1 | 1 | 1 |
| -3 | -2 | 1 |
| 4 | 4 | 4 |
| -1 | 3 | 4 |
| 2 | 5 | 5 |
| 1 | 6 | 6 |
| -5 | 1 | 6 |
| 4 | 5 | 6 |

Final Answer:

```python
6
```

---

# Correctness

If the running sum before the current element is negative, carrying it forward would only decrease the total.

Therefore:

- If extending the current subarray gives a larger sum, continue it.
- Otherwise, start a new subarray from the current element.

By making the optimal local decision at every step, Kadane's Algorithm guarantees the optimal global solution.

---

# Complexity Analysis

- **Time Complexity:** `O(n)`
  - The array is traversed exactly once.

- **Space Complexity:** `O(1)`
  - Only two variables are maintained regardless of input size.

---

# Python Solution

```python
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
```

---

# Key Concepts Used

- Arrays
- Greedy Algorithm
- Kadane's Algorithm
- Dynamic Programming (Space Optimized)

---

# Takeaways

- A negative running sum should never be carried forward.
- At every element, choose between:
  - Starting a new subarray.
  - Extending the existing subarray.
- The algorithm finds the maximum subarray sum in **linear time** with **constant extra space**, making it the optimal solution.
