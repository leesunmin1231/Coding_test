import sys
# Recursion Error 방지- 재귀의 한도 10000까지 풀어주기
sys.setrecursionlimit(100000)

def isCorner(d, nd):
    if d == -1:
        return False
    if abs(nd-d) == 1:
        return True
    if d==0 and nd == 4:
        return True
    if d == 4 and nd == 0:
        return True
    return False

def dfs(node, d, line, corner, board, visit):
    r, c = node
    print(r,c)
    if r == N-1 and c == N-1:
        result = line * 100 + corner * 500
        ans.append(result)
        return
    if visit[r][c]:
        return
    visit[r][c] = True
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        nd = i
        if nr < 0 or nr >= N:
            continue
        if nc < 0 or nc >= N:
            continue
        if board[nr][nc] == 1:
            continue
        if abs(d - nd) == 2:
            continue
        if isCorner(d, nd):
            dfs([nr, nc], nd, line+1, corner + 1, board, visit)
        else:
            dfs([nr, nc], nd, line+1, corner, board, visit)

    
def solution(board):
    global dr, dc, N, ans
    dr = [-1, 0, 1, 0] # 위, 오른쪽, 아래, 왼쪽
    dc = [0, 1, 0, -1]
    N = len(board)
    ans = []
    visit = [[False] * N for _ in range(N)]
    dfs([0,0], -1, 0, 0, board, visit)
    return min(ans)

print(solution([[0,0,0],[0,0,0],[0,0,0]]))