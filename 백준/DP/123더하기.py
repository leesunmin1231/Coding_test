import sys


def dp(n):
    d = [0] * (n + 1)
    if n == 1: 
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    d[1] = 1
    d[2] = 2
    d[3] = 4
    for i in range(4, n + 1):
        d[i] = d[i - 1] + d[i - 2] + d[i - 3]
    return d[n]

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp(n))