# O(n)
def solution(n, lost, reserve):
    d = [1] * (n+2)
    for i in reserve:
        d[i] += 1
    for i in lost:
        d[i] -= 1
    for i in range(1, n+1):
        if d[i] == 2 and d[i-1] == 0:
            d[i-1] = 1
            d[i] = 1
            continue
        if d[i] == 2 and d[i+1] == 0:
            d[i+1] = 1
            d[i] = 1
    ans = 0
    for i in range(1, n+1):
        if d[i]:
            ans += 1
    return ans

# O(klogk) k: min(lost길이, reserve 길이)
def solution2(n, lost, reserve):
    s = set(lost) & set(reserve)
    l = set(lost) - s
    r = set(reserve) - s
    for x in sorted(r):
        if x - 1 in l:
            l.remove(x - 1)
        elif x + 1 in l:
            l.remove(x + 1)
    return n - len(l)