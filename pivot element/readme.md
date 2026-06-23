# Find Pivot Index

## Problem Statement

Given an array of integers `nums`, calculate the **pivot index** of the array.

The pivot index is the index where the sum of all numbers strictly to the left of the index is equal to the sum of all numbers strictly to the right of the index.

If no such index exists, return `-1`.

### Example

```python
nums = [1, 7, 3, 6, 5, 6]
```

Output:

```python
3
```

Explanation:

* Left sum of index `3` = `1 + 7 + 3 = 11`
* Right sum of index `3` = `5 + 6 = 11`

Since both sums are equal, `3` is the pivot index.

---

## Approach

A straightforward brute-force solution is to iterate through each index and:

1. Calculate the sum of all elements on the left.
2. Calculate the sum of all elements on the right.
3. Compare both sums.
4. Return the current index if they are equal.

If no pivot index is found after checking all indices, return `-1`.

---

## Python Solution

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i + 1:]):
                return i

        return -1
```

---

## Complexity Analysis

### Time Complexity

For every index, two sums are computed:

* `sum(nums[:i])`
* `sum(nums[i+1:])`

Each sum operation takes `O(n)` time.

Since this is done for every index:

```text
O(n²)
```

### Space Complexity

Only a few variables are used:

```text
O(1)
```

(ignoring the temporary slices created by Python)

---

## Key Learning

A common mistake is placing:

```python
else:
    return -1
```

inside the loop.

Doing so causes the function to terminate after checking only the first index.

The correct approach is to return `-1` only after the entire array has been checked and no pivot index is found.

```python
for i in range(len(nums)):
    if condition:
        return i

return -1
```

This ensures every index gets evaluated before concluding that no pivot exists.
