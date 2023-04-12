def solution(N, stages):
    ans = []
    for stage in range(1, N+1):
        notClear = [x for x in stages if x == stage]
        total = [x for x in stages if x >= stage]
        if len(total) == 0:
            ans.append([stage, 0])
        else:
            ans.append([stage, len(notClear)/len(total)])
    return [x[0] for x in sorted(ans,reverse=True, key=lambda x: x[1])]