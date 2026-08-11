# Swap Nodes in Pairs

## Problem

Given a linked list, swap every two adjacent nodes and return its head.

The values inside the nodes **must not be modified**. Only the links between the nodes can be changed.

### Example

```text
Input:
1 → 2 → 3 → 4

Output:
2 → 1 → 4 → 3
```

For an odd number of nodes:

```text
Input:
1 → 2 → 3 → 4 → 5

Output:
2 → 1 → 4 → 3 → 5
```

The last node remains unchanged because it does not have a pair.

---

## Approach

We process the linked list **two nodes at a time**.

For a pair:

```text
previous → first → second → next
```

we want:

```text
previous → second → first → next
```

The important part is to change the `next` references rather than swapping the values.

### Steps

1. Create a dummy node before the head.
2. Keep a `prev` reference pointing to the node before the current pair.
3. Check whether two nodes are available:

   ```text
   prev.next
   prev.next.next
   ```
4. Store references to the two nodes:

   ```text
   first = prev.next
   second = first.next
   ```
5. Save the rest of the list:

   ```text
   temp = second.next
   ```
6. Reverse the pair:

   ```text
   second.next = first
   first.next = temp
   ```
7. Connect the previous part of the list to the new first node:

   ```text
   prev.next = second
   ```
8. Move `prev` forward and repeat.

---

## Pointer Visualization

Initially:

```text
dummy → 1 → 2 → 3 → 4 → 5
         ↑    ↑
       first second
```

Save the remaining list:

```text
temp → 3
```

Then change the references:

```text
2 → 1 → 3 → 4 → 5
```

Move to the next pair:

```text
2 → 1 → 3 → 4 → 5
         ↑    ↑
       first second
```

Swap again:

```text
2 → 1 → 4 → 3 → 5
```

The `5` is left untouched because there is no second node available.

---

## Why Use a Dummy Node?

Without a dummy node, swapping the first pair requires special handling because the head itself changes.

For example:

```text
1 → 2 → 3 → 4
```

After swapping:

```text
2 → 1 → 3 → 4
↑
new head
```

The dummy node gives us a node before the head:

```text
dummy → 1 → 2 → 3 → 4
```

This allows every pair to be handled using the same pointer logic.

At the end:

```python
return dummy.next
```

because `dummy` is not part of the actual linked list.

---

## Complexity

### Time Complexity

```text
O(n)
```

Every node is visited once.

### Space Complexity

```text
O(1)
```

Only a constant number of references are used. No additional list or recursion is required.

---

## Key Takeaway

The main idea is **not to swap the values**.

Instead, we rewire the `next` references:

```text
A → B → C
```

becomes:

```text
B → A → C
```

The important rule when manipulating linked lists is:

> **Before changing a reference, make sure you haven't lost access to the rest of the list.**

That is why we save:

```python
temp = second.next
```

before rewiring the pair.
