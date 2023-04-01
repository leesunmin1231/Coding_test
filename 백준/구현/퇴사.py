import sys

input = sys.stdin.readline

info = []
N = int(input())
for _ in range(N):
    tmp = list(map(int, input().split(" ")))
    info.append(tmp)

dist = [0] * (N+1)
for i in range(N):
    for j in range(i + info[i][0], N+1):
        dist[j] = max(dist[j], dist[i] + info[i][1])

print(dist[-1])