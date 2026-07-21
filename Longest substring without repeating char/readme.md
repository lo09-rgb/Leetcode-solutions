# Longest Substring Without Repeating Characters

## Problem Statement

Given a string `s`, find the length of the longest substring without repeating characters.

### Example 1

Input:
```
s = "abcabcbb"
```

Output:
```
3
```

Explanation:
The longest substring without repeating characters is `"abc"`.

---

### Example 2

Input:
```
s = "bbbbb"
```

Output:
```
1
```

Explanation:
The longest substring is `"b"`.

---

### Example 3

Input:
```
s = "pwwkew"
```

Output:
```
3
```

Explanation:
The longest substring is `"wke"`.

---

## Approach

This problem can be solved efficiently using the **Sliding Window** technique.

The idea is to maintain a window that always contains **unique characters**.

- Expand the window by moving the `right` pointer.
- If a duplicate character is encountered, shrink the window by moving the `left` pointer until the duplicate is removed.
- After every valid expansion, update the maximum window length.

A **HashSet** is used to quickly determine whether a character already exists inside the current window.

---

## Algorithm

1. Initialize two pointers:
   - `left = 0`
   - `right = 0`
2. Create an empty HashSet to store characters currently in the window.
3. Move the `right` pointer through the string.
4. While the current character already exists in the HashSet:
   - Remove the character at the `left` pointer.
   - Increment `left`.
5. Add the current character to the HashSet.
6. Update the maximum window length.
7. Continue until the end of the string.

---

## Dry Run

For:

```
s = "abcabcbb"
```

| Window | Length | Longest |
|--------|-------:|--------:|
| a | 1 | 1 |
| ab | 2 | 2 |
| abc | 3 | 3 |
| bca | 3 | 3 |
| cab | 3 | 3 |
| abc | 3 | 3 |
| cb | 2 | 3 |
| b | 1 | 3 |

Answer:

```
3
```

---

## Time Complexity

Each character enters the window once and leaves the window once.

```
O(n)
```

---

## Space Complexity

The HashSet stores at most all unique characters in the current window.

```
O(min(n, m))
```

where:

- `n` = length of the string
- `m` = size of the character set (e.g., 128 for ASCII)

---

## Concepts Used

- Sliding Window (Variable Size)
- Two Pointers
- HashSet
