# Valid Parentheses

## 📌 Problem

Given a string `s` containing only the characters:

```text
( ) { } [ ]
```

determine whether the string is valid.

A string is valid when:

1. Every opening bracket is closed by the same type of bracket.
2. Brackets are closed in the correct order.
3. Every closing bracket has a corresponding opening bracket.

---

## 💡 Approach

This problem can be solved efficiently using a **Stack**.

A stack follows the **LIFO (Last In, First Out)** principle.

### Algorithm

1. Create an empty stack.
2. Store the corresponding opening bracket for every closing bracket.
3. Traverse the string character by character.
4. If the character is an opening bracket, push it onto the stack.
5. If it is a closing bracket:

   * Check whether the stack is empty.
   * Check whether the top of the stack matches the corresponding opening bracket.
   * If either condition fails, return `False`.
   * Otherwise, remove the opening bracket using `pop()`.
6. After processing the entire string, return `True` only if the stack is empty.

---

## 🧠 Example

### Input

```text
s = "({[]})"
```

### Stack Operations

```text
(    → [(]
{    → [(, {]
[    → [(, {, []
]    → [(, {]
}    → [(]
)    → []
```

The stack is empty at the end.

### Output

```text
True
```

---

## ❌ Invalid Example

```text
s = "([)]"
```

When `)` is encountered, the top of the stack is `[`.

But `)` must match `(`.

Therefore:

```text
False
```

---

## 💻 Python Solution

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if not stack or stack[-1] != pairs[char]:
                    return False

                stack.pop()

        return len(stack) == 0
```

---

## ⏱️ Complexity Analysis

| Complexity      | Explanation                            |
| --------------- | -------------------------------------- |
| **Time: O(n)**  | Each character is processed once       |
| **Space: O(n)** | Stack can contain up to `n` characters |

---

## 🔑 Key Concept

> **Use a stack because brackets must be closed in the reverse order in which they were opened.**

For example:

```text
Opening:  (  {  [
Closing:  ]  }  )
          ↑  ↑  ↑
        LIFO order
```

### Data Structure Used

**Stack — LIFO (Last In, First Out)**

---

## 🏷️ Topics

* Stack
* String
* Hash Map
* LIFO
* Bracket Matching
* Data Structures
* Python
