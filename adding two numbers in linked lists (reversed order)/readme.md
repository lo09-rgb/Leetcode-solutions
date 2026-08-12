# Add Two Numbers — LeetCode #2

## Problem

You are given two non-empty linked lists representing two non-negative integers.

The digits are stored in **reverse order**, and each node contains a single digit.

Add the two numbers and return the sum as a linked list.

### Example

```text
l1 = 2 → 4 → 3
l2 = 5 → 6 → 4
```

These represent:

```text
342 + 465 = 807
```

So the result is:

```text
7 → 0 → 8
```

## Approach

Since the digits are already stored in reverse order, the first node represents the **ones digit**.

We can add both linked lists from left to right while keeping track of the carry.

For every pair of digits:

```text
sum = digit1 + digit2 + carry
```

Then:

```text
digit = sum % 10
carry = sum // 10
```

The calculated digit is added to the result linked list.

If one list ends before the other, its value is treated as `0`.

We continue processing while either list still has nodes **or a carry remains**.

## Example: 999 + 1

```text
l1 = 9 → 9 → 9
l2 = 1
```

Processing:

```text
9 + 1     = 10 → digit = 0, carry = 1
9 + 0 + 1 = 10 → digit = 0, carry = 1
9 + 0 + 1 = 10 → digit = 0, carry = 1
0 + 0 + 1 = 1  → digit = 1, carry = 0
```

Result:

```text
0 → 0 → 0 → 1
```

This represents `1000`.

## Complexity

Let `n` be the length of the first linked list and `m` be the length of the second linked list.

* **Time Complexity:** `O(max(n, m))`
* **Space Complexity:** `O(max(n, m))` for the result linked list.

## Key Takeaway

The numbers are already stored in reverse order, so there is no need to reverse the linked lists.

The main logic is:

```text
Read digits
    ↓
Add digits + carry
    ↓
Store sum % 10
    ↓
Update carry using sum // 10
    ↓
Move to the next nodes
    ↓
Continue until both lists and carry are finished
```

This is essentially **normal arithmetic addition implemented using linked lists**.
