import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split(" ")))

d = [0] * N
d[0] = arr[0]
d[1] = max(arr[0], arr[1])

for i in range(2, N):
    d[i] = max(arr[i] + d[i-2], d[i-1])
print(d[N-1])