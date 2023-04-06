import heapq

def solution(operations):
    answer = []
    for op in operations:
        if op == "D -1" and answer:
            heapq.heappop(answer)
        elif op == "D 1" and answer:
            answer = [-x for x in answer]
            heapq.heapify(answer)
            heapq.heappop(answer)
            answer = [-x for x in answer]
            heapq.heapify(answer)
        elif op.split(" ")[0] == 'I':
            heapq.heappush(answer, int(op.split(" ")[1]))
    if not answer:
        return [0,0]
    return [max(answer), min(answer)]