# LeetCode 155 — Min Stack

## 📌 Problem Statement

Design a stack that supports the following operations in **constant time O(1)**:

* `push(val)` — Push an element onto the stack.
* `pop()` — Remove the top element.
* `top()` — Retrieve the top element.
* `getMin()` — Retrieve the minimum element currently in the stack.

## 💡 Approach: Two Stacks

The solution uses two separate stacks:

1. **Main Stack (`stack`)** — Stores all the elements.
2. **Minimum Stack (`minStack`)** — Stores the minimum element at every level of the main stack.

Whenever a new value is pushed, the minimum stack stores the smaller of the new value and the previous minimum.

When an element is popped, both stacks remove their top elements. This ensures that the minimum value is always available at the top of the minimum stack.

## 🧠 Python Implementation

```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
```

## 📝 Example

**Input:**

```text
push(-2)
push(0)
push(-3)
getMin()
pop()
top()
getMin()
```

**Output:**

```text
-3
0
-2
```

## ⏱️ Complexity Analysis

| Operation  | Time Complexity |
| ---------- | --------------- |
| `push()`   | O(1)            |
| `pop()`    | O(1)            |
| `top()`    | O(1)            |
| `getMin()` | O(1)            |

**Space Complexity:** O(n), where `n` is the number of elements in the stack.

## 🎯 Key Takeaway

The two-stack approach allows the minimum element to be retrieved without traversing the entire stack. By maintaining the current minimum at every level, all required operations achieve **O(1) time complexity**.

## 🏷️ Topics

* Stack
* Design
* Data Structures
* Python
* LeetCode
* Time and Space Complexity

---

**Problem:** LeetCode 155 — Min Stack
**Difficulty:** Medium
**Language:** Python 3
