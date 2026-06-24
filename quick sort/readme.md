# Quick Sort in Python

## Overview

Quick Sort is a highly efficient Divide and Conquer sorting algorithm. It works by selecting a pivot element and partitioning the array into two parts:

- Elements smaller than the pivot
- Elements greater than the pivot

The same process is then applied recursively to the subarrays until the entire array is sorted.

---

## Algorithm Steps

1. Choose a pivot element.
2. Partition the array around the pivot.
3. Place the pivot in its correct sorted position.
4. Recursively sort the left subarray.
5. Recursively sort the right subarray.

---

## Python Implementation

```python
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


arr = [10, 7, 8, 9, 1, 5]

quick_sort(arr, 0, len(arr) - 1)

print("Sorted Array:", arr)
