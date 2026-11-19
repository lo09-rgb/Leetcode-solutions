
n = int(input())
arr = list(map(int, input().split()))

arr.sort()

ans = float('inf')

for i in range(n - 1):
    ans = min(ans, arr[i + 1] - arr[i])

print(ans)
