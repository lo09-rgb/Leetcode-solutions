# Merge Sort in Python

## 📌 Overview

This project implements the **Merge Sort** algorithm in Python using the **Divide and Conquer** approach. Merge Sort recursively divides the array into smaller subarrays, sorts them, and then merges the sorted subarrays to produce the final sorted array.

---

## 🚀 Features

- Efficient sorting algorithm with **O(n log n)** time complexity.
- Uses recursion for dividing the array.
- Merges sorted subarrays into a fully sorted array.
- Suitable for large datasets due to its consistent performance.

---

## 📂 Code Structure

```text
merge_sort(arr)
│
├── Base Case
│   └── If array has 0 or 1 element, return it.
│
├── Divide
│   └── Split the array into left and right halves.
│
├── Conquer
│   └── Recursively sort both halves.
│
└── Combine
    └── Merge the two sorted halves using merge().
```

---

## 🛠️ Algorithm

1. Check if the array contains one or no elements.
2. Find the middle index.
3. Divide the array into two halves.
4. Recursively apply Merge Sort on both halves.
5. Merge the two sorted halves into one sorted array.
6. Return the merged sorted array.

---

## 💻 Example

### Input

```python
arr = [38, 27, 43, 3, 9, 82, 10]
```

### Output

```python
[3, 9, 10, 27, 38, 43, 82]
```

---

## 📊 Time Complexity

| Case | Complexity |
|------|------------|
| Best Case | O(n log n) |
| Average Case | O(n log n) |
| Worst Case | O(n log n) |

---

## 💾 Space Complexity

| Complexity |
|------------|
| O(n) |

Merge Sort requires additional memory during the merging process, making it **not an in-place sorting algorithm**.

---

## ✅ Advantages

- Guaranteed **O(n log n)** time complexity.
- Stable sorting algorithm (preserves the order of equal elements).
- Efficient for sorting large datasets.
- Well-suited for linked lists and external sorting.

---

## ❌ Disadvantages

- Requires extra memory proportional to the input size.
- Recursive implementation adds function call overhead.
- Less space-efficient than in-place algorithms like Heap Sort.

---

## 📖 Concepts Used

- Divide and Conquer
- Recursion
- Array Manipulation
- Two-Pointer Technique (during merging)

---

## ▶️ How to Run

1. Save the program as `merge_sort.py`.
2. Open a terminal in the project directory.
3. Run the program:

```bash
python merge_sort.py
```

---

## 🎯 Learning Outcome

This project demonstrates:

- Recursive problem solving
- Divide and Conquer strategy
- Merging two sorted arrays efficiently
- Time and space complexity analysis
- Building one of the most fundamental comparison-based sorting algorithms

---

## 👨‍💻 Author

**Aayusshman Baral**

Computer Science & Engineering Student | Data Structures & Algorithms Enthusiast
