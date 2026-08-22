# 🔄 Linked List Cycle II — LeetCode 142

## 📌 Problem

Given the `head` of a linked list, return the node where the cycle begins.

If there is no cycle in the linked list, return `null`.

A cycle exists when a node's `next` pointer points to a previous node in the list, allowing the list to be traversed indefinitely.

> **LeetCode:** 142 — Linked List Cycle II
> **Difficulty:** Medium
> **Topic:** Linked List, Two Pointers

---

## 💡 Approach

This solution uses **Floyd's Tortoise and Hare Algorithm**.

We use two pointers:

* `slow` → moves one node at a time.
* `fast` → moves two nodes at a time.

### Step 1 — Detect the Cycle

If a cycle exists, `slow` and `fast` will eventually meet inside the cycle.

If `fast` reaches `None`, there is no cycle.

### Step 2 — Find the Start of the Cycle

After the two pointers meet:

1. Move `slow` back to `head`.
2. Keep `fast` at the meeting point.
3. Move both pointers one step at a time.
4. The point where they meet again is the **starting node of the cycle**.

---

## 🧠 Why Does This Work?

Suppose:

* Distance from `head` to cycle start = `x`
* Distance from cycle start to meeting point = `y`
* Cycle length = `C`

When the two pointers meet, the difference in their travelled distances is a multiple of the cycle length.

This allows resetting one pointer to `head` and moving both pointers at the same speed. They will meet exactly at the cycle's starting node.

---

## 🧑‍💻 Python Solution

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # Step 1: Detect whether a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        # Step 2: Find the beginning of the cycle
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
```

---

## ⏱️ Complexity

| Complexity | Value  |
| ---------- | ------ |
| Time       | `O(n)` |
| Space      | `O(1)` |

The algorithm traverses the linked list using constant extra space.

---

## 📚 Key Concepts

* Linked Lists
* Floyd's Cycle Detection Algorithm
* Fast and Slow Pointers
* Two-Pointer Technique
* Cycle Detection

---

## 🚀 Takeaway

The important idea is that **detecting a cycle and finding its starting point are two separate steps**.

Floyd's algorithm allows both operations to be performed in:

**`O(n)` time and `O(1)` extra space.**

This makes it much more efficient than storing every visited node in a `set`, which would require `O(n)` additional memory.
