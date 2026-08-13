# Reverse Nodes in k-Group

An in-place, iterative solution to **LeetCode 25: Reverse Nodes in k-Group** — reverse every contiguous group of `k` nodes in a singly linked list. If the number of remaining nodes is not a multiple of `k`, the leftover nodes at the end are left as-is.

## Problem Statement

Given the head of a linked list and an integer `k`, reverse the nodes in groups of `k` and return the modified list.

- `k` is a positive integer and is less than or equal to the length of the list.
- If the number of nodes is not a multiple of `k`, the final partial group is left untouched.
- Node **values** may not be changed — only their pointers (`next`) may be modified.

**Example**

```
Input:  head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Input:  head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
```

## Approach

The algorithm reverses the list one group at a time, iteratively, using constant extra space (no recursion stack, no auxiliary list/array).

### Key idea

Maintain a pointer `group_prev` that always points to the node **just before** the group currently being reversed. For each group:

1. **Locate the group boundary** — walk `k` steps ahead from `group_prev` to find the `kth` node of the current group. If fewer than `k` nodes remain, stop and return the list unchanged from this point (partial groups are not reversed).
2. **Remember what comes after** — save `group_next`, the node right after the group, so the group's tail can be reconnected once reversed.
3. **Reverse the group in place** — standard iterative linked-list reversal, but instead of starting `prev` at `None`, start it at `group_next`. This makes the last node of the reversed group automatically point to the node following the group — no separate reconnection step needed for the tail.
4. **Splice the reversed group back in** — `group_prev.next` is pointed at `kth` (the new head of the reversed group, since reversal flips the order).
5. **Advance** — `group_prev` moves to `old_group_start` (the node that was the group's head before reversal, now its tail), ready to process the next group.

A **dummy node** is placed before `head` so the very first group can be reversed the same way as every other group, without special-casing the head of the list.

### Why reversal starts `prev` at `group_next`

This is the trick that avoids a separate "stitch the tail to the rest of the list" step. When the inner `while curr != group_next` loop finishes, the last node processed (originally the group's head) already has its `next` pointer correctly set to `group_next`, because that's what `prev` was initialized to.

### Step-by-step trace

For `head = [1,2,3,4,5]`, `k = 2`:

| Step | group_prev | Group found | Action | List so far |
|---|---|---|---|---|
| 1 | dummy | [1,2] | reverse → 2→1 | dummy→2→1→3→4→5 |
| 2 | node 1 | [3,4] | reverse → 4→3 | dummy→2→1→4→3→5 |
| 3 | node 3 | only [5] left (< k) | stop, return as-is | dummy→2→1→4→3→5 |

Final result: `[2,1,4,3,5]`

## Complexity

| Metric | Complexity | Notes |
|---|---|---|
| Time | `O(n)` | Each node is visited a constant number of times (once to find the group boundary, once to reverse). |
| Space | `O(1)` | Only a fixed number of pointers are used; no recursion, no extra data structures. |

`n` = number of nodes in the list.

## Code

```python
class Solution:
    def reverseKGroup(self, head, k):
        # Dummy node makes reconnecting groups easier
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # 1. Find the kth node
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                # Fewer than k nodes remain
                if kth is None:
                    return dummy.next

            # 2. Save the node after this group
            group_next = kth.next

            # 3. Reverse the k nodes
            prev = group_next
            curr = group_prev.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # 4. Connect previous group to reversed group
            old_group_start = group_prev.next
            group_prev.next = kth

            # 5. Move group_prev to the end of the reversed group
            group_prev = old_group_start
```

### Dependency

This solution assumes a standard singly linked list node definition, typically provided by the judge:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

## Edge Cases Handled

- **`k = 1`** — every "group" is a single node; the reversal loop runs once per node and changes nothing, so the list is returned unchanged.
- **Leftover nodes fewer than `k`** — detected by the `kth is None` check inside the boundary-finding loop; those nodes are left in their original order.
- **Empty list (`head = None`)** — the boundary-finding loop immediately finds `kth is None` and returns `dummy.next`, which is `None`.
- **`k` equal to the length of the list** — the entire list is reversed as one group.

## Usage

```python
# Build a list 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

result = Solution().reverseKGroup(head, 2)

# Walk and print the result: 2 -> 1 -> 4 -> 3 -> 5
node = result
while node:
    print(node.val, end=" -> " if node.next else "\n")
    node = node.next
```
