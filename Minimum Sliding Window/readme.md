# Minimum Window Substring

## Problem Statement

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring** of `s` such that every character in `t` (including duplicates) is included in the window.

If there is no such substring, return an empty string `""`.

> The test cases are generated such that the answer is unique.

---

## Example

### Input

```text
s = "ADOBECODEBANC"
t = "ABC"
```

### Output

```text
"BANC"
```

### Explanation

The smallest substring of `s` containing all characters `A`, `B`, and `C` is:

```text
BANC
```

---

## Approach

This problem is efficiently solved using the **Sliding Window** technique.

### Algorithm

1. Store the frequency of every character in `t`.
2. Expand the window by moving the right pointer.
3. Track character frequencies inside the current window.
4. Once all required characters are present:
   - Try shrinking the window from the left.
   - Update the minimum window whenever a smaller valid window is found.
5. Continue until the right pointer reaches the end of `s`.

---

## Why Sliding Window?

A brute-force solution checks every possible substring, resulting in **O(n²)** time complexity.

Using a sliding window allows each character to be visited at most twice (once while expanding and once while shrinking), reducing the complexity to **O(m + n)**.

---

## Complexity Analysis

| Complexity | Value |
|------------|-------|
| Time | **O(m + n)** |
| Space | **O(k)** |

Where:

- `m` = length of `s`
- `n` = length of `t`
- `k` = number of distinct characters stored in the hash maps

---

## Python Solution

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        required = len(need)
        formed = 0

        window = {}

        left = 0
        ans_len = float("inf")
        ans_start = 0

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                formed += 1

            while formed == required:

                if right - left + 1 < ans_len:
                    ans_len = right - left + 1
                    ans_start = left

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        if ans_len == float("inf"):
            return ""

        return s[ans_start:ans_start + ans_len]
```

---

## Dry Run

### Input

```text
s = "ADOBECODEBANC"
t = "ABC"
```

### Step 1

Required frequency:

```text
A → 1
B → 1
C → 1
```

### Step 2

Expand the window:

```text
A
AD
ADO
ADOB
ADOBE
ADOBEC ✅
```

Current window:

```text
ADOBEC
```

Try shrinking:

```text
Remove A ❌
Window becomes invalid.
```

Continue expanding:

```text
ODEBANC ✅
```

Shrink again:

```text
BANC ✅
```

No smaller valid window exists.

### Final Answer

```text
BANC
```

---

## Key Concepts

- Sliding Window
- Hash Map (Frequency Counter)
- Two Pointers
- Greedy Window Shrinking

---

## Tags

- Sliding Window
- HashMap
- Two Pointers
- String
- LeetCode Hard
