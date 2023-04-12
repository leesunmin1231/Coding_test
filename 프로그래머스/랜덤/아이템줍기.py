from collections import deque

def getValidateWay(node):
    tmp = []
    y, x = node
    if 2 <= y - 1 < 102 and 2 <= x < 102:
        tmp.append([y-1, x])
    if 2 <= y + 1 < 102 and 2 <= x < 102:
        tmp.append([y+1, x])
    if 2 <= y < 102 and 2 <= x - 1 < 102:
        tmp.append([y, x-1])
    if 2 <= y < 102 and 2 <= x + 1 < 102:
        tmp.append([y, x+1])
    return tmp

def bfs(board, start, end):
    q = deque()
    q.append(start)
    dist = [[0] * 102 for _ in range(102)]
    while q:
        node = q.popleft()
        if node == end:
            return dist[node[0]][node[1]]//2
        for next in [x for x in getValidateWay(node) if board[x[0]][x[1]] == 1]:
            if dist[next[0]][next[1]]:
                continue
            dist[next[0]][next[1]] = dist[node[0]][node[1]] + 1
            q.append(next)
        

def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0] * 102 for _ in range(102)]
    # 빈 곳: 0, 테두리: 1, 박스 안: 2
    for rec in rectangle:
        minx, miny, maxx, maxy = [x*2 for x in rec]
        # 테두리 채우기
        for x in range(minx, maxx+1):
            if board[miny][x] == 0: board[miny][x] = 1 
            if board[maxy][x] == 0: board[maxy][x] = 1 
        for y in range(miny, maxy+1):
            if board[y][minx] == 0: board[y][minx] = 1 
            if board[y][maxx] == 0: board[y][maxx] = 1 
        # 박스 내부 채우기
        for y in range(miny+1, maxy):
            for x in range(minx+1, maxx):
                board[y][x] = 2
    return bfs(board, [characterY*2,characterX*2], [itemY*2, itemX*2])