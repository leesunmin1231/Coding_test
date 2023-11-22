import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))
T = []
for _ in range(N):
    T.append(int(input()))

minTime = min(T)
maxTime = max(T) * M

while minTime <= maxTime:
    mid = (minTime + maxTime) // 2
    total = 0
    for t in T:
        total += mid//t
    if total >= M:
        maxTime = mid-1
    else:
        minTime = mid+1
print(minTime)