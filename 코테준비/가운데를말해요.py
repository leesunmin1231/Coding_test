import sys
import heapq

input = sys.stdin.readline

N = int(input())
        
left = [] # 최대힙
right = [] # 최소힙

for _ in range(N):
    num = int(input())
    if len(left) == len(right):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)
    if not right:
        print(num)
        continue
    while -left[0] > right[0]:
        leftNum = heapq.heappop(left)
        rightNum = heapq.heappop(right)
        heapq.heappush(right, -leftNum)
        heapq.heappush(left, -rightNum)
    print(-left[0])