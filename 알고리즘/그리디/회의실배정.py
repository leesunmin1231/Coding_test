import sys

input = sys.stdin.readline

N = int(input())
timeTable = []
for _ in range(N):
    timeTable.append(list(map(int, input().split(" "))))
timeTable.sort(key=lambda x: x[0])
timeTable.sort(key=lambda x: x[1])
ans = 0
clock = 0
for time in timeTable:
    if clock <= time[0]:
        clock = time[1]
        ans += 1
print(ans)