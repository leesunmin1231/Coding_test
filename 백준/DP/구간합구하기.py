import sys
input = sys.stdin.readline

n, m= map(int, input().split(" "))

nums = list(map(int, input().split(" ")))

dist = [0] * (n + 1)
for i in range(n):
    dist[i+1] = nums[i] + dist[i]
for _ in range(m):
    start, end = map(int, input().split(" "))
    print(dist[end]-dist[start-1])