from collections import deque

n, m = map(int, input().replace("\n", "").strip().split(" "))
board = []
for _ in range(n):
    board.append(list(map(int, input().replace("\n", "").strip().split(" "))))
destList = []
for _ in range(m):
    r,c = map(int, input().replace("\n", "").strip().split(" "))
    destList.append([r-1, c-1])

def findPath(board, player, dest):
    q = deque()
    q.append([player[0], player[1], []])
    visit = [[False] * n for _ in range(n)]
    dr = [-1,0,0,1]
    dc = [0,-1,1,0]
    while q:
        r, c, path = q.popleft()
        if r == dest[0] and c == dest[1]:
            return path[0]
        if visit[r][c]:
            continue
        visit[r][c] = True
        for i in range(4):
            nr = r + dr[i]
            nc = c +dc[i]
            if nr < 0 or nr >=n:
                continue
            if nc < 0 or nc >= n:
                continue
            if board[nr][nc] == 2:
                continue
            if visit[nr][nc]:
                continue
            tmp = path + [[nr,nc]]
            q.append([nr,nc,tmp])


def movePlayer(board, players, destList):
    for i, player in enumerate(players):
        r,c,index = player
        dest = destList[index]
        nr, nc = findPath(board, player, dest)
        players[i] = [nr, nc, index]
    return players

def checkReceive(players, destList):
    receive = []
    newPlayers = []
    for player in players:
        r,c, index = player
        dest = destList[index]
        if r == dest[0] and c == dest[1]:
            receive.append([r,c])
        else:
            newPlayers.append([r,c,index])
    return [receive, newPlayers]

def getDistance(one, two):
    return abs(one[0]-two[0]) + abs(one[1]-two[1])

def findStart(board, dest):
    q = deque()
    q.append([dest[0], dest[1], 0])
    result = []
    dis = 0
    dr = [-1,0,0,1]
    dc = [0,-1,1,0]
    visit = [[False]*n for _ in range(n)]
    while q:
        r, c, distance = q.popleft()
        if board[r][c] == 1:
            if len(result) == 0:
                result.append([r,c, distance])
                dis = distance
                continue
            if distance < dis:
                result = [[r,c, distance]]
            if dis == distance:
                result.append([r,c,distance])
        if visit[r][c]:
            continue
        visit[r][c] = True
        for i in range(4):
            nr = r + dr[i]
            nc = c +dc[i]
            if nr < 0 or nr >=n:
                continue
            if nc < 0 or nc >= n:
                continue
            if board[nr][nc] == 2:
                continue
            if visit[nr][nc]:
                continue
            q.append([nr,nc, distance+1])
    result.sort(key = lambda x: (x[0], x[1]))
    return result[0]

def blocking(board, receive):
    for target in receive:
        r, c = target
        board[r][c] = 2

players = [] # [r, c, playerIndex]
# 0: 빈공간, 1: 베이스캠프, 2: blocking
time = 0
checker = 0
while True:
    if checker == len(destList):
        break
    # 사람들 이동
    players = movePlayer(board, players, destList)
    # 편의점에 도착한 사람들 체크
    receive, players = checkReceive(players, destList)
    checker += len(receive)
    # 이번에 시작한 베이스캠프, 사람이 도착한 편의점 지나갈 수 없도록 blocking
    blocking(board, receive)
    # 이번에 출발하느 베이스캠프 위치 찾기
    if time < m:
        start = findStart(board, destList[time])
        players.append([start[0], start[1], time])
        board[start[0]][start[1]] = 2
    time+=1
print(time)