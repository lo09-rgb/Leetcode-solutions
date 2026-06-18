# Two Sum - LeetCode

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

You may assume that each input has exactly one solution, and you may not use the same element twice.

### Example

```python
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
```

Explanation:

```
nums[0] + nums[1] = 2 + 7 = 9
```

---

## Approach

This solution uses a Hash Map (Python Dictionary) to store numbers that have already been visited.

For each number:

1. Calculate the complement:

```python
complement = target - num
```

2. Check if the complement already exists in the dictionary.

   * If yes, we have found the pair.
   * Return the stored index and the current index.

3. Otherwise, store the current number and its index in the dictionary.

---

## Dry Run

```python
nums = [2,7,11,15]
target = 9
```

### Iteration 1

```python
num = 2
complement = 7
```

Dictionary:

```python
{2: 0}
```

### Iteration 2

```python
num = 7
complement = 2
```

Since `2` already exists in the dictionary:

```python
return [0, 1]
```

---

## Complexity Analysis

### Time Complexity

```python
O(n)
```

We traverse the array only once.

### Space Complexity

```python
O(n)
```

In the worst case, all elements are stored in the dictionary.

---

## Key Concept

The dictionary provides nearly constant-time lookup:

```python
if complement in seen:
```

This avoids the brute-force nested loop approach (`O(n²)`) and makes the solution efficient for large inputs.

---

## LeetCode Submission

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i
```
