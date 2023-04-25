import sys
from itertools import combinations
from collections import deque

input= sys.stdin.readline

N, M = map(int, input().split(" "))
board = []
for _ in range(N):
    board.append(list(map(int, input().split(" "))))
boardTmp = []
for row in board:
    tmp = []
    for k in row:
        tmp.append(k)
    boardTmp.append(tmp)

def bfs(board, visited, start, toFill):
    q = deque()
    q.append(start)
    nodeCount = 0
    print("start", start)
    while q:
        node = q.popleft()
        board[node[0]][node[1]] = toFill
        visited[node[0]][node[1]] = True
        nodeCount += 1
        for next in [[node[0]+1, node[1]],[node[0]-1, node[1]],[node[0], node[1]+1],[node[0], node[1]-1]]:
            if next[0] < 0 or next[0] >= N:
                continue
            if next[1] < 0 or next[1] >= M:
                continue
            if board[next[0]][next[1]] == 1:
                continue
            if visited[next[0]][next[1]]:
                continue
            if toFill == 0 and board[next[0]][next[1]] == 2:
                continue
            q.append(next)
    if toFill == 0:
        print(nodeCount, toFill)
        for row in visited:
            print(row)
        print("")
    return nodeCount

wallPos = []
for i in range(N):
    for j in range(M):
        wallPos.append((i,j))
threeWalls = combinations(wallPos, 3)
ans = 0
for threeWall in threeWalls:
    # board 초기화
    board = []
    for row in boardTmp:
        tmp = []
        for k in row:
            tmp.append(k)
        board.append(tmp)
    # 벽세우기
    for wall in threeWall:
        board[wall[0]][wall[1]] = 1
    # 바이러스 퍼뜨리기
    visited = [[False] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if visited[r][c]:
                continue
            if board[r][c] == 2:
                bfs(board,visited, [r,c], 2)
    # 안전영역 크기 구하기
    sizevisited = [[False] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if sizevisited[r][c]:
                continue
            if board[r][c] == 0 and not sizevisited[r][c]:
                print("아니씨발 ", [r,c],  sizevisited[r][c])
                result = bfs(board, sizevisited, [r,c], 0)
                if result > ans:
                    ans = result
print(ans)

