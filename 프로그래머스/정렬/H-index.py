def solution(citations):
    citations.sort(reverse=True)
    ans = 0
    count = 0
    for c in citations:
        count += 1
        tmp = min(count, c)
        if tmp > ans:
            ans = tmp
    return ans