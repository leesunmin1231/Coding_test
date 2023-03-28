def solution(number, k):
    n = len(number)
    ans = []
    for i in range(n):
        for j in range(len(ans)-1, -1, -1):
            if ans[j] < number[i] and k > 0:
                ans.pop()
                k -= 1
            else:
                break
        if k == 0:
            ans += (list(number)[i:])
            break
        ans.append(number[i])
    if k > 0:
        return "".join(ans[:-1*k])
    return "".join(ans)