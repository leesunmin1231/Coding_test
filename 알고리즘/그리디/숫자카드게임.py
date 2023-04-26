import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))
arr = []
for _ in range(N):
    arr.append(min(list(map(int, input().split(" ")))))
print(max(arr))
