import sys

input = sys.stdin.readline

N, S = map(int, input().split(" "))
arr = [0] + list(map(int, input().split(" ")))
dist = [0] * (N+1)

for i in range(1, N+1):
    dist[i] = arr[i] + dist[i-1]

start = 0
end = 1
ans = N+1

while end < N+1:
    if dist[end] - dist[start] < S:
        end += 1
        continue
    if ans > end - start:
        ans = end - start
    start += 1

if ans == N+1:
    print(0)
else:
    print(ans)