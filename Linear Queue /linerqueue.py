q = int(input())

queue = [0] * 100000
front = 0
rear = -1

for _ in range(q):
    query = list(map(int, input().split()))

    # Enqueue
    if query[0] == 1:
        rear += 1
        queue[rear] = query[1]

    # Dequeue
    elif query[0] == 2:
        if front > rear:
            print(-1)
        else:
            print(queue[front])
            front += 1

    # Front
    elif query[0] == 3:
        if front > rear:
            print(-1)
        else:
            print(queue[front])
