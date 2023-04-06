from collections import deque

def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    goal = (sum1 + sum2) // 2
    q1 = deque(queue1)
    q2 = deque(queue2)
    count = 0
    limit = len(queue1) * 4
    if (sum1 + sum2) % 2 == 1:
        return -1
    while q1 and q2:
        if (sum1 > sum2):
            num = q1.popleft()
            q2.append(num)
            sum1 -= num
            sum2 += num
            count += 1
        elif (sum1 < sum2):
            num = q2.popleft()
            q1.append(num)
            sum2 -= num
            sum1 += num
            count += 1
        else:
            return count
        if count > limit:
            return -1
    return -1