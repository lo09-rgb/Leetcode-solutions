# 3Sum - LeetCode

## Problem Statement

Given an integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` such that:

* `i != j`
* `i != k`
* `j != k`
* `nums[i] + nums[j] + nums[k] == 0`

The solution set must not contain duplicate triplets.

---

## Example

### Input

```python
nums = [-1, 0, 1, 2, -1, -4]
```

### Output

```python
[[-1, -1, 2], [-1, 0, 1]]
```

---

## Approach

### 1. Sort the Array

Sorting helps us efficiently use the two-pointer technique and avoid duplicate triplets.

```python
nums.sort()
```

Sorted Array:

```python
[-4, -1, -1, 0, 1, 2]
```

---

### 2. Fix One Number

Treat each element as the first element of a potential triplet.

For example:

```python
nums[i] = -1
```

We need:

```python
-1 + x + y = 0
```

which becomes:

```python
x + y = 1
```

---

### 3. Use Two Pointers

Place:

```python
left = i + 1
right = len(nums) - 1
```

Check:

```python
nums[left] + nums[right]
```

* If the sum is too small, move `left` right.
* If the sum is too large, move `right` left.
* If the sum matches the target, store the triplet.

---

### 4. Skip Duplicates

To avoid repeated triplets:

* Skip duplicate fixed elements.
* Skip duplicate left pointer values.
* Skip duplicate right pointer values.

---

## Time Complexity

Sorting:

```python
O(n log n)
```

Two-pointer traversal:

```python
O(n²)
```

Overall:

```python
O(n²)
```

---

## Space Complexity

Ignoring the output list:

```python
O(1)
```

---

## Key Insight

The 3Sum problem can be reduced to:

```text
Fix one number
+
Solve Two Sum on the remaining sorted array
```

This reduces the brute-force complexity from `O(n³)` to `O(n²)`.
