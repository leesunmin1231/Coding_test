import sys
import heapq

input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
heapq.heapify(arr)
ans = 0
while len(arr) > 1:
    tmp = heapq.heappop(arr) + heapq.heappop(arr)
    ans += tmp
    heapq.heappush(arr, tmp)

print(ans)