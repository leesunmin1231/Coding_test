import heapq
from collections import deque

def solution(jobs):
    waiting = []
    jobs.sort(key=lambda x: (x[0], x[1]))
    works = deque(jobs)
    clock = 0
    cpu = None
    ans = 0
    while works or waiting or cpu:
        if works and works[0][0] <= clock:
            job = works.popleft()
            heapq.heappush(waiting, (job[1], job[0])) # 짧게 걸리는 작업 먼저 하기 위해
        if cpu is None and waiting:
            tmp = heapq.heappop(waiting)
            cpu = [tmp[1], clock + tmp[0]]
        if cpu and clock == cpu[1]-1:
            ans += cpu[1] - cpu[0]
            cpu = None
        clock+=1
    return ans//len(jobs)
            