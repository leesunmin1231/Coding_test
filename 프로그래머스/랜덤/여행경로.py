def dfs(tickets):
    n = len(tickets)
    twithIdx = [[x[0], x[1], i] for i,x in enumerate(tickets)]
    start = sorted([x for x in twithIdx if x[0] == "ICN"], key=lambda x: x[1])[0]
    stack = [start[0], start[1]]
    visited = [False] * n
    visited[start[2]] = True
    ans = []
    while len(ans) + len(stack) != len(tickets) + 1:
        top = stack[-1]
        nextlist = sorted([x for x in twithIdx if x[0] == top and not visited[x[2]]], key=lambda x:x[1])
        if len(nextlist) == 0:
            tmp = stack.pop()
            ans.append(tmp)
            continue
        nextnode = nextlist[0]
        stack.append(nextnode[1])
        visited[nextnode[2]] = True
    while stack:
        ans.append(stack.pop())
    return list(reversed(ans))
    
def solution(tickets):
    return dfs(tickets)

    
print(dfs([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))