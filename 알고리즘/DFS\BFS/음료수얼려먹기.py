import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))
board = []
for _ in range(N):
    board.append(list(map(int, list(input())[:-1])))

def dfs(start):
    board[start[0]][start[1]] = 1
    if start[0]+1 < N and not board[start[0]+1][start[1]]:
        dfs([start[0]+1,start[1]])
    if start[1]+1 < N and not board[start[0]][start[1]+1]:
        dfs([start[0],start[1]+1])
    
ans = 0
for r in range(N):
    for c in range(M):
        if not board[r][c]:
            dfs([r,c])
            ans += 1
print(ans)