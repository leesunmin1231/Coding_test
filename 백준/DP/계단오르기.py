import sys

def dp(stairs):
    N = len(stairs)
    d = [0] * N
    d[1] = stairs[1]
    if N == 2:
        return d[1]
    d[2] = d[1] + stairs[2]
    if N == 3:
        return d[2]
    d[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])
    if N == 4:
        return d[3]

    for i in range(4, N):
        d[i] = max(d[i - 3] + stairs[i -1] + stairs[i], d[i - 2] + stairs[i])
    return d[N-1]

input = sys.stdin.readline

T = int(input())
stairs = [0]
for _ in range(T):
    n = int(input())
    stairs.append(n)
print(dp(stairs))