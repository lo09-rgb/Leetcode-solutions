
n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

for i in range(n):
    found = 0
    duplicate = 0

    for j in range(m):
        if a[i] == b[j]:
            found = 1
            break

    for k in range(i):
        if a[i] == a[k]:
            duplicate = 1
            break

    if found == 1 and duplicate == 0:
        print(a[i], end=" ")
