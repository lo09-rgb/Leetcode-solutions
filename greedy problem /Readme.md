# Jump Game - Greedy Algorithm

## Problem Statement

Given an integer array `nums`, you are initially positioned at the first index.

Each element in the array represents your maximum jump length at that position.

Return `True` if you can reach the last index, otherwise return `False`.

### Example

```python
nums = [2, 3, 1, 1, 4]
```

Output:

```python
True
```

Explanation:

* Start at index 0.
* From index 0, you can jump up to 2 positions.
* By making valid jumps, you can eventually reach the last index.

---

## Approach

This solution uses the **Greedy Algorithm**.

Instead of checking every possible path, we keep track of the **farthest index reachable** at every step.

For each position:

1. Check if the current index is reachable.
2. Update the farthest reachable position.
3. If we encounter an index beyond our reach, return `False`.
4. If the traversal completes successfully, return `True`.

---

## Algorithm

1. Initialize a variable `farthest = 0`.
2. Traverse the array.
3. If the current index is greater than `farthest`, return `False`.
4. Update:

```python
farthest = max(farthest, i + nums[i])
```

5. After traversal, return `True`.

---

## Python Implementation

```python
def canJump(nums):
    farthest = 0

    for i in range(len(nums)):
        if i > farthest:
            return False

        farthest = max(farthest, i + nums[i])

    return True


nums = [2, 3, 1, 1, 4]
print(canJump(nums))
```

---

## Dry Run

Input:

```python
nums = [2, 3, 1, 1, 4]
```

| Index | Value | Farthest Reach |
| ----- | ----- | -------------- |
| 0     | 2     | 2              |
| 1     | 3     | 4              |
| 2     | 1     | 4              |
| 3     | 1     | 4              |
| 4     | 4     | 8              |

Since the last index is reachable, the function returns:

```python
True
```

---

## Time Complexity

* Traversal of array: **O(n)**

Overall Time Complexity:

```text
O(n)
```

---

## Space Complexity

Only one extra variable (`farthest`) is used.

```text
O(1)
```

---

## Key Learning

The Greedy approach works because at every position we only care about the **farthest reachable index**. Tracking this information eliminates the need to explore all possible jump combinations, resulting in an efficient O(n) solution.
