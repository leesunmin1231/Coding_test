import sys
input = sys.stdin.readline

N = input()
d = [(0,0) for _ in range(N)]
arr =[]
for _ in range(N):
    arr.append(map(int, input().split(" ")))
       