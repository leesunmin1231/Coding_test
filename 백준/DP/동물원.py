import sys

input = sys.stdin.readline

N = int(input())
dist = [0] * N

dist[0] = [1,2]

for i in range(1, N):
    zero = (dist[i-1][1] + dist[i-1][0]) % 9901
    one = (dist[i-1][1] + dist[i-1][0] * 2) % 9901
    dist[i] = [zero, one]
print((dist[N-1][0] + dist[N-1][1]) % 9901)