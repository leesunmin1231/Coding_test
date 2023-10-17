import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split(" ")))


d = [-1] * N
stack = []
stack.append(0)
for i in range(1,N):
    while stack and arr[stack[-1]] < arr[i]:
        tmp = stack.pop()
        d[tmp] = arr[i]
    stack.append(i)

print(' '.join(list(map(str, d))))
