import sys

input = sys.stdin.readline

T = int(input())
ans = []
for _ in range(T):
    n = int(input())
    board1 = list(map(int, input().split(" ")))
    board2 = list(map(int, input().split(" ")))
    d1 = [0] * n
    d2 = [0] * n
    d1[0] = board1[0]
    d2[0] = board2[0]
    for i in range(1, n):
        d1[i] = max(d1[i-1], d2[i-1] + board1[i])
        d2[i] = max(d2[i-1], d1[i-1] + board2[i])
    ans.append(max(d1[n-1], d2[n-1]))
for num in ans:
    print(num)