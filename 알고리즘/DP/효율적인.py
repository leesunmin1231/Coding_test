import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()

dist = [10001] * (M+1)

dist[0] = 0
for i in range(N):
    for j in range(arr[i], M+1):
        if dist[j - arr[i]] != 10001:
            dist[j] = min(dist[j], dist[j- arr[i]]+1)
if dist[M] == 10001:
    print(-1)
else:
    print(dist[M])