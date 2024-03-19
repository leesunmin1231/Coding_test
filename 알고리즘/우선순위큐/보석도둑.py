import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split(" "))
gems = []
for _ in range(N):
    M, V = map(int, input().split(" "))
    gems.append([M, V])
weight = []
for _ in range(K):
    weight.append(int(input()))
gems.sort()
weight.sort()
q = []
result = 0
for bag in weight:
    while gems and gems[0][0] <= bag: # 현재 가방에 넣을 수 있는 모든 보석 큐에 넣기
        heapq.heappush(q, -gems[0][1]) # 가격 비싼 순으로 저장
        heapq.heappop(gems) # 가장 가벼운 보석 빼기
    if q:
        result -= heapq.heappop(q)

print(result)