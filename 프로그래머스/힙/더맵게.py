import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while scoville:
        if scoville[0] >= K:
            return count
        num1 = heapq.heappop(scoville)
        if scoville:
            num2 = heapq.heappop(scoville)
            heapq.heappush(scoville, num1+(num2*2))
            count += 1
        else:
            return -1
    return count
            
        