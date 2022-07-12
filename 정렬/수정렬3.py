import sys
n = int(input())
lst = [0 for _ in range(10001)]
for _ in range(n):
    num = int(sys.stdin.readline())
    lst[num] += 1
for i in range(10001):
    if lst[i] != 0:
        for j in range(lst[i]):
            print(i)