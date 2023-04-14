from collections import deque

def bfs(start, end, n,m, k):
    q = deque()
    q.append(start)
    board = [[0] * m for _ in range(n)]
    ans = []
    path = {}
    while q:
        node = q.popleft()
        if node == end and board[node[0]][node[1]] == k:
            ans.append(''.join(path[(node[0],node[1])])) 
        for next in [[node[0] - 1, node[1], 'u'], [node[0] + 1, node[1], 'd'], [node[0], node[1] - 1, 'l'], [node[0], node[1] + 1, 'r']]:
            if next[0] >= n or next[0] < 0:
                continue
            if next[1] >= m or next[1] < 0:
                continue
            if board[next[0]][next[1]]:
                continue
            board[next[0]][next[1]] = board[node[0]][node[1]] + 1
            if (next[0],next[1]) in path.keys():
                path[(next[0],next[1])].append(next[2])
            else:
                path[(next[0],next[1])] = [next[2]]
            q.append(next)
    return ans

def solution(n, m, x, y, r, c, k):
    minMove = abs(r-x) + abs(c-y)
    if minMove > k or abs(k - minMove)%2 == 1:
        return "impossible"
    ans = bfs([x,y], [r,c], n, m, k)
    ans.sort()
    return ans[0]


print(solution(3,4,2,3,3,1,5))