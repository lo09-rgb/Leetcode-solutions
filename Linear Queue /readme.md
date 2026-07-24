# Queue Implementation Using Linear Array (Python)

## 📌 Problem Statement

Implement a **Queue** data structure using a **linear array**. The queue should support the following operations:

- **Enqueue** – Insert an element at the rear of the queue.
- **Dequeue** – Remove and return the front element of the queue.
- **Front** – Return the front element without removing it.

If the queue is empty and a dequeue or front operation is performed, print `-1`.

---

## 📚 Queue Overview

A **Queue** is a **First In, First Out (FIFO)** data structure.

The first element inserted into the queue is the first one to be removed.

Example:

```
Enqueue 10
Enqueue 20
Enqueue 30

Queue:
10 20 30

Dequeue

Queue:
20 30
```

---

## 🛠 Data Structures Used

- Fixed-size linear array
- Two pointers:
  - `front` – Points to the first element of the queue.
  - `rear` – Points to the last element of the queue.

---

## 🔹 Initialization

```python
queue = [0] * 100000
front = 0
rear = -1
```

Initially,

```
front = 0
rear = -1
```

Since

```
front > rear
```

the queue is considered empty.

---

## 🔹 Operations

### 1. Enqueue

**Algorithm**

1. Increment the `rear` pointer.
2. Insert the element at `queue[rear]`.

```python
rear += 1
queue[rear] = value
```

Example

Before:

```
front = 0
rear = -1

Queue:
[]
```

After inserting `10`:

```
front = 0
rear = 0

Queue:
10
```

---

### 2. Dequeue

**Algorithm**

1. Check if the queue is empty.
2. If empty, print `-1`.
3. Otherwise:
   - Print `queue[front]`
   - Increment `front`.

```python
if front > rear:
    print(-1)
else:
    print(queue[front])
    front += 1
```

Example

Before:

```
10 20 30
^
front
```

After dequeue:

```
20 30
^
front
```

Notice that the value `10` still exists in the array but is ignored because the `front` pointer has moved.

---

### 3. Front (Peek)

Returns the front element without removing it.

```python
if front > rear:
    print(-1)
else:
    print(queue[front])
```

Unlike dequeue, the `front` pointer does **not** move.

---

## 🧠 Working Principle

Each query begins with an instruction number.

| Query | Meaning |
|--------|---------|
| `1 X` | Enqueue `X` |
| `2` | Dequeue |
| `3` | Print Front |

Example:

Input

```
1 50
```

gets converted into

```python
query = [1, 50]
```

Here,

```
query[0] → Command (1 = Enqueue)
query[1] → Value to insert (50)
```

The program first checks the command:

```python
if query[0] == 1:
```

If true, it inserts `query[1]` into the queue.

---

## 💻 Python Implementation

```python
q = int(input())

queue = [0] * 100000
front = 0
rear = -1

for _ in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        rear += 1
        queue[rear] = query[1]

    elif query[0] == 2:
        if front > rear:
            print(-1)
        else:
            print(queue[front])
            front += 1

    elif query[0] == 3:
        if front > rear:
            print(-1)
        else:
            print(queue[front])
```

---

## ⏱ Time Complexity

| Operation | Complexity |
|-----------|------------|
| Enqueue | O(1) |
| Dequeue | O(1) |
| Front | O(1) |

---

## 💾 Space Complexity

```
O(N)
```

where `N = 100000` (maximum queue capacity).

---

## ⚠ Limitations of a Linear Queue

A linear queue does not reuse empty spaces created after dequeue operations.

Example:

```
Index:
0 1 2 3 4

Queue:
10 20 30 40 50
```

After removing all elements:

```
front = 5
rear = 4
```

Although the queue is empty, `rear` has reached the end of the array.

The freed positions at the beginning cannot be reused in a **linear queue**.

This limitation is solved using a **Circular Queue**, where the `front` and `rear` pointers wrap around to the beginning of the array.

---

## Key Takeaways

- Queue follows the **FIFO (First In, First Out)** principle.
- `front` points to the first valid element.
- `rear` points to the last inserted element.
- Enqueue increments `rear`.
- Dequeue increments `front`.
- Elements are **not physically removed** from the array; moving the `front` pointer logically removes them.
- The queue is empty when:

```
front > rear
```
