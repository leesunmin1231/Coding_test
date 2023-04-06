import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while scoville:
        num1 = heapq.heappop(scoville)
        if num1 >= K:
            return count
        elif len(scoville) == 0:
            return -1
        else:
            num2 = heapq.heappop(scoville)
            heapq.heappush(scoville, num1+(num2*2))
            count += 1
    return count
            
        