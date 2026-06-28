# Selection Sort in Python

This project demonstrates the implementation of the **Selection Sort** algorithm using Python.

## 📌 Description

Selection Sort is a simple comparison-based sorting algorithm. It repeatedly finds the smallest element from the unsorted portion of the array and places it at the beginning. This process continues until the entire array is sorted.

Although Selection Sort is easy to understand and implement, it is not efficient for large datasets due to its quadratic time complexity.

---

## 📂 Algorithm

1. Start from the first element.
2. Assume the current element is the minimum.
3. Traverse the remaining unsorted part of the array.
4. Find the actual minimum element.
5. Swap it with the current element.
6. Move to the next position.
7. Repeat until the array is sorted.

---

## 💻 Python Implementation

```python
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


numbers = [64, 25, 12, 22, 11]
print(selection_sort(numbers))
```

---

## ▶️ Sample Output

```
[11, 12, 22, 25, 64]
```

---

## ⏱️ Time Complexity

| Case | Complexity |
|------|------------|
| Best Case | O(n²) |
| Average Case | O(n²) |
| Worst Case | O(n²) |

---

## 💾 Space Complexity

- **O(1)** (In-place sorting)

---

## ✅ Advantages

- Simple and easy to implement.
- Requires no additional memory.
- Performs a minimal number of swaps.
- Suitable for small datasets.

---

## ❌ Disadvantages

- Inefficient for large datasets.
- Time complexity remains O(n²) even if the array is already sorted.
- Not a stable sorting algorithm by default.

---

## 📚 Example

**Input**

```
[64, 25, 12, 22, 11]
```

**Pass 1**

```
[11, 25, 12, 22, 64]
```

**Pass 2**

```
[11, 12, 25, 22, 64]
```

**Pass 3**

```
[11, 12, 22, 25, 64]
```

**Final Output**

```
[11, 12, 22, 25, 64]
```

---

## 🚀 How to Run

1. Clone the repository.

```bash
git clone <repository-url>
```

2. Navigate to the project directory.

```bash
cd <repository-folder>
```

3. Run the Python file.

```bash
python selection_sort.py
```

---

## 📖 Key Concepts

- Comparison-based sorting
- In-place sorting
- Minimum element selection
- Swapping elements
- Nested loops
- Time and space complexity analysis

---

## 👨‍💻 Author

A Python implementation of the Selection Sort algorithm for learning Data Structures and Algorithms (DSA).
