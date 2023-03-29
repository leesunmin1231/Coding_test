def solution(n, costs):
    costs.sort(key=lambda x : x[2])
    ans = 0
    visit = set([costs[0][0]])
    while len(visit) < n:
        for cost in costs:
            if cost[0] in visit and cost[1] in visit:
                continue;
            if cost[0] in visit or cost[1] in visit:
                ans += cost[2]
                visit.update([cost[0], cost[1]])
                break
    return ans