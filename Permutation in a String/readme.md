# 🔍 Permutation in String (LeetCode 567)

## 📝 Problem Statement

Given two strings `s1` and `s2`, determine whether `s2` contains a permutation of `s1`.

A permutation of a string is any rearrangement of its characters. Return `True` if any substring of `s2` is a permutation of `s1`; otherwise, return `False`.

---

## 💡 Approach

Since every valid permutation must have the **same length** as `s1`, we use a **fixed-size sliding window** of length `len(s1)` over `s2`.

Two frequency arrays of size **26** are maintained:

* `freq1` stores the frequency of characters in `s1`.
* `freq2` stores the frequency of characters in the current window of `s2`.

### Algorithm

1. If `s1` is longer than `s2`, return `False`.
2. Build the frequency arrays for:

   * `s1`
   * The first window of `s2`
3. Compare the two frequency arrays.

   * If they are equal, a permutation exists.
4. Slide the window one character at a time:

   * Add the new character entering the window.
   * Remove the character leaving the window.
5. After every slide, compare the frequency arrays.
6. If a match is found, return `True`.
7. If no matching window exists, return `False`.

---

## 🧠 Why This Works

A permutation contains **exactly the same characters with the same frequencies**, regardless of their order.

Instead of sorting every substring (which is inefficient), we compare the character frequencies of each window with the frequency of `s1`.

Since the window size never changes, each slide requires updating only **two characters**, making the solution highly efficient.

---

## ⏱️ Time Complexity

* Building the initial frequency arrays: **O(m)**
* Sliding the window across `s2`: **O(n - m)**
* Comparing two frequency arrays of size 26 takes **O(26) = O(1)**.

**Overall Time Complexity:** **O(n)**

Where:

* `m = len(s1)`
* `n = len(s2)`

---

## 📦 Space Complexity

Two frequency arrays of size 26 are used.

**Overall Space Complexity:** **O(1)**

---

## ✅ Python Solution

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        # Build frequency arrays
        for i in range(len(s1)):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1

        # Check the first window
        if freq1 == freq2:
            return True

        left = 0

        # Slide the window
        for right in range(len(s1), len(s2)):
            freq2[ord(s2[right]) - ord('a')] += 1
            freq2[ord(s2[left]) - ord('a')] -= 1
            left += 1

            if freq1 == freq2:
                return True

        return False
```
