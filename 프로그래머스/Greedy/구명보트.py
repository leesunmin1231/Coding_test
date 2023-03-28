from collections import deque

def solution(people, limit):
    q = deque(sorted(people))
    ans = 0
    while q:
        if len(q) == 1:
            q.pop()
            ans += 1
        elif q[0] + q[-1] <= limit:
            q.popleft()
            q.pop()
            ans += 1
        else:
            q.pop()
            ans += 1
    return ans