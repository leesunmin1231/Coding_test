import sys

input = sys.stdin.readline

import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split(" ")))

d = [0] * N
stack = []
for i in range(N-1,-1,-1):
    while stack and arr[stack[-1]] < arr[i]:
        tmp = stack.pop()
        d[tmp] = i+1
    stack.append(i)
print(*d)
    