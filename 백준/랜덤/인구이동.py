import sys
from collections import deque

input = sys.stdin.readline

N,L,R = map(int, input().split(" "))
board = []
for _ in range(N):
    board.append(list(map(int, input().split(" "))))

def bfs(visited, board,newBoard, start):
    q = deque()
    q.append(start)
    total = 0
    count = 0
    dist = []
    while q:
        node = q.popleft()
        if visited[node[0]][node[1]]:
            continue
        count +=1
        total += board[node[0]][node[1]]
        
        visited[node[0]][node[1]] = True
        dist.append(node)
        for next in [[node[0]-1, node[1]],[node[0]+1, node[1]],[node[0], node[1]-1],[node[0], node[1]+1]]:
            if next[0] >= N or next[0] < 0:
                continue
            if next[1] >= N or next[1] < 0:
                continue
            if visited[next[0]][next[1]]:
                continue
            if L <= abs(board[next[0]][next[1]] - board[node[0]][node[1]]) <= R:
                q.append(next)
    if count == 1:
        newBoard[start[0]][start[1]] = board[start[0]][start[1]]
        return 0
    for node in dist:
        newBoard[node[0]][node[1]] = total//count
    return total//count

ans = 0
while True:
    visited = [[False] * N for _ in range(N)]
    newBoard = [[0] * N for _ in range(N)]
    flag = False
    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                continue
            newNum = bfs(visited,board,newBoard, [r, c]) # visited에 이동된 인구수를 채운다
            if newNum != 0:
                flag = True
    board = newBoard
    if not flag:
        break
    # print(newBoard)
    ans += 1
print(ans)

            