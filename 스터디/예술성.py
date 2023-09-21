import sys
import copy
from collections import deque

input = sys.stdin.readline

n = int(input().replace("\n", "").strip())

board = []
for _ in range(n):
    board.append(list(map(int, input().replace("\n", "").strip().split(" "))))

def bfs(visit, board, groupBoard, group, start):
    q = deque()
    q.append(start)
    blockNum = board[start[0]][start[1]]
    blockCount = 0
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    while q:
        r, c = q.popleft()
        if visit[r][c]:
            continue
        visit[r][c] = True
        groupBoard[r][c] = group
        blockCount+=1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= n:
                continue
            if nc < 0 or nc >= n:
                continue
            if visit[nr][nc]:
                continue
            if board[nr][nc] != blockNum:
                continue
            q.append([nr,nc])
    return [blockCount, blockNum]

def calculate(board):
    visit = [[False] * n for _ in range(n)]
    groupBoard = [[0] * n for _ in range(n)]
    blockCounts = {}
    group = 0
    for r in range(n):
        for c in range(n):
            if visit[r][c]:
                continue
            blockCount, blockNum = bfs(visit, board, groupBoard, group, [r,c])
            blockCounts[group] = [blockCount, blockNum]
            group+=1
    total = 0
    for r in range(n):
        for c in range(n):
            if r < n-1 and groupBoard[r][c] != groupBoard[r+1][c]:
                count, num = blockCounts[groupBoard[r][c]]
                nCount, nNum = blockCounts[groupBoard[r+1][c]]
                total += (count + nCount) * num * nNum
            if c < n-1 and groupBoard[r][c] != groupBoard[r][c+1]:
                count, num = blockCounts[groupBoard[r][c]]
                nCount, nNum = blockCounts[groupBoard[r][c+1]]
                total += (count + nCount) * num * nNum
    return total

def rotateLeft(board):
    newBoard = copy.deepcopy(board)
    for r in range(n):
        c = n // 2
        newBoard[n-1-c][r] = board[r][c]
    for c in range(n):
        r = n // 2
        newBoard[n-1-c][r] = board[r][c]
    return newBoard

def rotateRight(board, rowStart, colStart):
    newBoard = copy.deepcopy(board)
    for r in range(n // 2):
        for c in range(n // 2):
            newBoard[c + rowStart][n // 2-1-r + colStart] = board[r + rowStart][c + colStart]
    return newBoard

ans = 0
total = calculate(board)
ans += total
for _ in range(3):
    board = rotateLeft(board)
    board = rotateRight(board, 0, 0)
    board = rotateRight(board, 0, n // 2+1)
    board = rotateRight(board, n//2+1, 0)
    board = rotateRight(board, n//2+1, n//2+1)
    total = calculate(board)
    ans += total
print(ans)