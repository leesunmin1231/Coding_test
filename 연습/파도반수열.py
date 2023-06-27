import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    dist = [0,1,1,1,2,2]
    N = int(input())
    for i in range(6, N+1):
        dist.append(dist[i-1] + dist[i-5])
    print(dist[N])