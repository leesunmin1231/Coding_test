from collections import deque

def bfs(start, table, visited):
    q = deque()
    q.append(start)
    N = len(table)
    shape = [[0]*N for _ in range(N)]
    maxRow = 0 # 후에 shape담는 box 자르기용
    maxCol = 0
    minRow = N
    minCol = N
    # 원래 모양 shape에 담기, visited 채우기
    while q:
        node = q.popleft()
        if visited[node[0]][node[1]]:
            continue
        visited[node[0]][node[1]] = 1
        shape[node[0]][node[1]] = 1
        if node[0] > maxRow:
            maxRow = node[0]
        if node[1] > maxCol:
            maxCol = node[1]
        if node[0] < minRow:
            minRow = node[0]
        if node[1] < minCol:
            minCol = node[1]
        for next in [[node[0]-1, node[1]], [node[0]+1, node[1]], [node[0], node[1]-1], [node[0], node[1]+1]]:
            if next[0] < 0 or next[0] >= N:
                continue
            if next[1] < 0 or next[1] >= N:
                continue
            if visited[next[0]][next[1]] or not table[next[0]][next[1]]:
                continue
            q.append(next)
    cutShape = [row[minCol:maxCol+1] for row in shape[minRow:maxRow + 1]]        
    shapes = [cutShape]
    # 회전시켜서 담기
    for _ in range(3):
        prev = shapes[-1]
        n = len(prev)
        m = len(prev[0])
        rotate = [[0] * n for _ in range(m)]
        for c in range(m):
            for r in range(n):
                rotate[m-c-1][r] = prev[r][c]
        shapes.append(rotate)
    return shapes

def fill_bfs(start, game_board):
    q = deque()
    q.append(start)
    N = len(game_board)
    shape = [[0]*N for _ in range(N)]
    maxRow = 0 # 후에 shape담는 box 자르기용
    maxCol = 0
    minRow = N
    minCol = N
    while q:
        node = q.popleft()
        if game_board[node[0]][node[1]]:
            continue
        game_board[node[0]][node[1]] = 1
        shape[node[0]][node[1]] = 1
        if node[0] > maxRow:
            maxRow = node[0]
        if node[1] > maxCol:
            maxCol = node[1]
        if node[0] < minRow:
            minRow = node[0]
        if node[1] < minCol:
            minCol = node[1]
        for next in [[node[0]-1, node[1]], [node[0]+1, node[1]], [node[0], node[1]-1], [node[0], node[1]+1]]:
            if next[0] < 0 or next[0] >= N:
                continue
            if next[1] < 0 or next[1] >= N:
                continue
            if game_board[next[0]][next[1]]:
                continue
            q.append(next)
    cutShape = [row[minCol:maxCol+1] for row in shape]
    cutShape = cutShape[minRow: maxRow+1] 
    return cutShape

def checkShape(target, all_shapes):
    toDel = -1
    result = False
    for key, shape_type in all_shapes.items():
        for shape in shape_type:
            flag = True
            if len(shape) != len(target):
                flag = False
            for i,row in enumerate(shape):
                if i >= len(target):
                    flag = False
                    break
                if row != target[i]:
                    flag = False
                    break
            if flag:
                break
        if flag:
            result = True
            toDel = key
            break
    if toDel != -1:
        del all_shapes[toDel]
    return result

def solution(game_board, table):
    N = len(table)
    visited = [[False]*N for _ in range(N)]
    all_shapes = {}
    index = 0
    for r in range(N):
        for c in range(N):
            if table[r][c] and not visited[r][c]:
                shapes = bfs([r,c], table, visited)
                all_shapes[(r,c)] = shapes
                index += 1
    ans = 0
    for r in range(N):
        for c in range(N):
            if not game_board[r][c]:
                shape = fill_bfs([r, c], game_board) # 1로 빈자리 채우면서 형태 가져오기
                if checkShape(shape, all_shapes): # all_shapes안에 shape이 있는지 체크하는 로직
                    for row in shape:
                        for box in row:
                            if box:
                                ans +=1
    return ans