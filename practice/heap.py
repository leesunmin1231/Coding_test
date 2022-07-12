import heapq

def solution(scoville, K):
    lst = []
    for i in scoville:
        heapq.heappush(lst, i)
    
    answer = 0
    while lst[0] < K:
        if (len(lst) == 1):
            return -1
        print(lst)
        first = heapq.heappop(lst)
        second = heapq.heappop(lst)
        heapq.heappush(lst, first + (second*2))
        answer+=1
    return answer
scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville,K))