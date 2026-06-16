# Two Pointer Technique (Opposite Direction)

## Overview

The **Two Pointer Technique** is an efficient algorithmic approach used when working with arrays, lists, or strings. In the **opposite direction** variant, one pointer starts from the beginning of the array and another starts from the end. The pointers move toward each other based on specific conditions until a solution is found.

This technique often reduces the time complexity from **O(n²)** to **O(n)** by avoiding unnecessary nested loops.

---

## Template Code

```python
def opposite_direction_template(nums: list[int]) -> None:
    left = 0
    right = len(nums) - 1

    while left < right:
        # Calculate or check current state
        current = calculate_something(nums, left, right)

        if found_answer(current, nums, left, right):
            # Process and possibly return
            return
        elif need_to_increase_value(current, nums, left, right):
            left += 1
        else:
            right -= 1
```

---

## How It Works

### Step 1: Initialize Two Pointers

* `left` starts at index `0`.
* `right` starts at the last index of the array.

```python
left = 0
right = len(nums) - 1
```

---

### Step 2: Process While Pointers Haven't Crossed

The loop continues until `left` and `right` meet.

```python
while left < right:
```

This ensures every relevant pair of elements is examined.

---

### Step 3: Evaluate Current State

A calculation or comparison is performed using the values at both pointers.

```python
current = calculate_something(nums, left, right)
```

Examples:

* Sum of two numbers
* Area between two lines
* Difference between values
* Pair comparison

---

### Step 4: Check for the Desired Result

```python
if found_answer(current, nums, left, right):
    return
```

If the required condition is satisfied, the algorithm returns the answer.

---

### Step 5: Move a Pointer

If the current state is too small:

```python
left += 1
```

Move the left pointer rightward to increase the value.

Otherwise:

```python
right -= 1
```

Move the right pointer leftward to decrease the value.

---

## Time Complexity

| Operation   | Complexity |
| ----------- | ---------- |
| Traversal   | O(n)       |
| Extra Space | O(1)       |

Since each pointer moves at most `n` times, the overall runtime is linear.

---

## Common Problems Using This Pattern

### 1. Two Sum II (Sorted Array)

Find two numbers whose sum equals a target value.

### 2. Container With Most Water

Find two lines that can hold the maximum amount of water.

### 3. Valid Palindrome

Check whether a string reads the same forward and backward.

### 4. Pair Difference Problems

Find pairs with a specific difference.

### 5. Sorted Array Search Problems

Efficiently search for matching pairs without nested loops.

---

## Visualization

```text
Array: [1, 2, 3, 4, 5, 6]

        L           R
        ↓           ↓
       [1, 2, 3, 4, 5, 6]

Move pointers toward each other:

           L     R
           ↓     ↓
       [1, 2, 3, 4, 5, 6]

Eventually:

              LR
              ↓
       [1, 2, 3, 4, 5, 6]
```

---

## Key Idea

Instead of checking every possible pair using nested loops (`O(n²)`), two pointers intelligently eliminate impossible cases by moving inward from both ends. This makes the algorithm highly efficient for sorted arrays and pair-based optimization problems.
