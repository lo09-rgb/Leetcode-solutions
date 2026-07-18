# Prefix Expression Evaluation using Stack (Python)

## 📌 Problem Statement

Write a program to evaluate a **Prefix Expression (Polish Notation)** using the **Stack** data structure.

In a prefix expression, every operator appears **before** its operands.

Example:

```
+9*26
```

represents

```
9 + (2 × 6)
```

whose result is **21**.

---

## 📖 Approach

The expression is scanned **from right to left**.

### Algorithm

1. Create an empty stack.
2. Traverse the expression from right to left.
3. If the current character is a digit:
   - Convert it into an integer.
   - Push it onto the stack.
4. If the current character is an operator:
   - Pop the first value → **operand1**
   - Pop the second value → **operand2**
   - Perform the operation:
     - `+`
     - `-`
     - `*`
     - `/` (integer division)
   - Push the result back onto the stack.
5. After the traversal, the remaining element in the stack is the final answer.

---

## ⏱ Time Complexity

- **O(n)**

Each character is processed exactly once.

---

## 💾 Space Complexity

- **O(n)**

In the worst case, all operands are stored in the stack.

---

## ✅ Sample Input

```
+9*26
```

### Output

```
21
```

---

## Another Example

### Input

```
*+23+45
```

### Output

```
45
```

---

## Concepts Used

- Stack Data Structure
- Prefix Expression Evaluation
- String Traversal
- Integer Arithmetic
