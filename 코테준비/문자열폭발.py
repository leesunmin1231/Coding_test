import sys

input = sys.stdin.readline

total = list(input().strip())
splitTarget = list(input().strip())
stack = []

targetLen = len(splitTarget)
for i in total:
    stack.append(i)
    if stack[len(stack) - targetLen: len(stack)] == splitTarget:
        for _ in range(targetLen):
            stack.pop()

if stack:
    print(*stack, sep='')
else:
    print("FRULA")