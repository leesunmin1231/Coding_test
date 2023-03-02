def case1(query, total):
    left = 0
    for i in range(total//2):
        left += query[i]
    right = 0
    startPoint = total//2
    if (total % 2 == 1):
        startPoint += 1
    for i in range(startPoint, total):
        right += query[i]
    if abs(left - right) % 2 == 0:
        return 0
    else:
        return 1

def case2(query, total):
    left = 0
    for i in range(total//2):
        left += query[i]
    right = 0
    for i in range(total//2, total):
        right += query[i]
    if abs(left - right) % 2 == 0:
        return 0
    else:
        return 1

def solution(queries):
    ans = []
    for query in queries:
        total = len(query)
        if (total % 2 == 1):
            if query[total//2] % 2 == 0:
                ans.append(case1(query, total))
            else:
                ans.append(case2(query, total))
        else:
            ans.append(case1(query, total))
    return ans

print(solution([[0, 1, 1]]))