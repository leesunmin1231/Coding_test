import sys

input = sys.stdin.readline

N = int(input())
def dp(N):
    d = [0] * (N+1)
    if (N == 1):
        return 1
    if (N == 2):
        return 2
    d[1] = 1
    d[2] = 2
    for i in range(3, N+1):
        d[i] = d[i-1] + d[i-2]
    return d[N]
print(dp(N)%10007)