import sys
input = sys.stdin.readline

def dp(costs, N):
    for i in range(1,N):
        costs[i][0] = min(costs[i-1][1], costs[i-1][2]) + costs[i][0]
        costs[i][1] = min(costs[i-1][0], costs[i-1][2]) + costs[i][1]
        costs[i][2] = min(costs[i-1][1], costs[i-1][0]) + costs[i][2]
    return min(costs[N-1])

N = int(input())
costs = []
for _ in range(N):
    row = list(map(int, input().split(" ")))
    costs.append(row)
print(dp(costs, N))