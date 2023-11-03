import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split(" "))

q = deque()
q.append([n,0])
visit = [False] * 100001

while q:
    cur,time = q.popleft()
    if cur == k:
        print(time)
        break
    if cur >= 100001:
        continue
    if cur < 0:
        continue
    if visit[cur]:
        continue
    visit[cur] = True
    q.append([cur-1, time+1])
    q.append([cur+1, time+1])
    q.appendleft([cur*2, time])