# Next Greater Element (NGE) using Stack

## 📌 Problem Statement

Given an array of integers, find the **Next Greater Element (NGE)** for every element.

The **Next Greater Element** of an element `x` is the **first greater element to its right** in the array. If no greater element exists, return `-1`.

### Example

**Input:**

```text
Array = [2, 1, 4, 3, 5]
```

**Output:**

```text
2 → 4
1 → 4
4 → 5
3 → 5
5 → -1
```

---

# Brute Force Approach

### Intuition

For every element, scan all the elements on its right until a greater element is found.

### Algorithm

1. Traverse each element from left to right.
2. For every element, check every element on its right.
3. If a greater element is found, print it.
4. Otherwise, print `-1`.

### Complexity

* **Time Complexity:** `O(n²)`
* **Space Complexity:** `O(1)`

### Drawback

This approach repeatedly scans the same elements, making it inefficient for large arrays.

---

# Optimal Approach (Monotonic Stack)

### Intuition

Instead of searching to the right every time, process the array **from right to left**.

Maintain a stack that stores only the elements that can still be the Next Greater Element for future elements.

When processing the current element:

* Remove all elements from the stack that are **smaller than or equal** to the current element.
* If the stack becomes empty, there is no greater element.
* Otherwise, the top of the stack is the answer.
* Push the current element onto the stack.

---

# Why Does It Work?

Suppose the array is:

```text
2 1 4 3 5
```

Processing starts from the right.

### Step 1

Current = `5`

```
Stack: []
Answer = -1

Push 5

Stack:
5
```

---

### Step 2

Current = `3`

```
Top = 5

5 > 3

Answer = 5

Push 3
```

Stack:

```
3
5
```

---

### Step 3

Current = `4`

```
Top = 3

3 <= 4

Pop 3
```

Now

```
Top = 5

5 > 4

Answer = 5
```

Push 4

Stack:

```
4
5
```

---

### Step 4

Current = `1`

```
Top = 4

Answer = 4

Push 1
```

Stack:

```
1
4
5
```

---

### Step 5

Current = `2`

```
Top = 1

1 <= 2

Pop
```

Stack:

```
4
5
```

Now

```
Top = 4

Answer = 4
```

Push 2

Final Stack

```
2
4
5
```

---

# Why Do We Pop Smaller Elements?

Consider the array:

```text
2 4 3
```

While processing from the right:

```
Stack

3
```

Current = `4`

Since

```
3 < 4
```

remove `3`.

Why?

Because any element further left that could use `3` will always encounter `4` first.

```
2 ----> 4 ----> 3
```

Since `4` is both **greater** and **closer**, `3` can never become the Next Greater Element for any future element.

Therefore, it is safe to discard it.

---

# Algorithm

```
Traverse the array from right to left

For every element

    While stack is not empty
          AND stack.top() <= current element
          Pop()

    If stack is empty
          Answer = -1
    Else
          Answer = stack.top()

    Push(current element)
```

---

# Complexity Analysis

### Time Complexity

Every element is:

* Pushed once
* Popped at most once

Therefore,

```
O(n + n)
```

which simplifies to

```
O(n)
```

---

### Space Complexity

The stack may contain all elements in the worst case.

```
O(n)
```

---

# Key Learning Points

* Brute force repeatedly searches the right side, resulting in `O(n²)` time.
* Processing from **right to left** allows us to reuse previously computed information.
* The stack stores only **useful candidate elements**.
* Any element that is **smaller than or equal to** the current element can never be the Next Greater Element again and is removed.
* Each element is pushed and popped at most once, giving an overall time complexity of `O(n)`.

---

# Related Problems

* Next Greater Element II (LeetCode 503)
* Daily Temperatures (LeetCode 739)
* Online Stock Span (LeetCode 901)
* Largest Rectangle in Histogram (LeetCode 84)
* Trapping Rain Water (LeetCode 42)

---

## Author

**Aayushman Baral**

*Learning Data Structures & Algorithms with Python.*
