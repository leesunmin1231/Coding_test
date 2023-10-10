n, m, k = map(int,input().split(" "))

def getNumNotMinus(num):
    if num < 0:
        return 0
    return num

def getRotateStartPoint(playerPos, exitPos, distance):
    er, ec = exitPos
    tmp = [max(playerPos[0],er), max(playerPos[1], ec)]
    start = [getNumNotMinus(tmp[0] - distance), getNumNotMinus(tmp[1] - distance)]
    return start

def getDistance(one, two):
    return abs(one[0] - two[0]) + abs(one[1] - two[1])

def movePlayer(board, player, exit):
    dr = [-1, 1, 0,0]
    dc = [0,0,1,-1]
    nextPos = []
    distance = getDistance(exit, player)
    for i in range(4):
        nr = player[0] + dr[i]
        nc = player[1] + dc[i]
        if nr < 0 or nr >= n:
            continue
        if nc < 0 or nc >= n:
            continue
        if board[nr][nc] != 0:
            continue
        if getDistance(exit, [nr,nc]) < distance:
            nextPos.append([nr,nc])
    if len(nextPos) == 0:
        return [player, 0]
    return [nextPos[0], 1]

def getRotateRange(board, exit, players):
    er, ec = exit
    # 출구에서 r차이와 c차이가 제일 작은 참가자 찾기
    target = players[0]
    targetDistance = max(abs(er-target[0]), abs(ec-target[1]))
    start = getRotateStartPoint(target, exit, targetDistance)
    for player in players:
        maxDistance = max(abs(er-player[0]), abs(ec-player[1]))
        # 더 작은 정사각형 일 경우
        if maxDistance < targetDistance:
            target = player
            targetDistance = maxDistance
            start = getRotateStartPoint(target, exit, targetDistance)
        # 정사각형 크기 같은 경우
        if maxDistance == targetDistance:
            curStart = getRotateStartPoint(player, exit, maxDistance)
            if curStart[0] < start[0]:
                target = player
                targetDistance = maxDistance
                start = curStart
            elif curStart[0] == start[0] and curStart[1] < start[1]:
                target = player
                targetDistance = maxDistance
                start = curStart
    return [start, [start[0] + targetDistance, start[1] + targetDistance]]

def rotateBoard(board, start, end):
    sr, sc = start
    er, ec = end
    tmp = [row[sc:ec+1] for row in board[sr:er+1]]
    rotateTmp = [[0] * len(tmp) for _ in range(len(tmp))]
    for r in range(len(tmp)):
        for c in range(len(tmp)):
            rotateTmp[c][len(tmp)-1-r] = tmp[r][c]
    for r in range(len(tmp)):
        for c in range(len(tmp)):
            board[sr+r][sc+c] = getNumNotMinus(rotateTmp[r][c]-1)
    return len(tmp)

def rotatePlayerAndExit(start, end, exit, players, rotateN):
    sr, sc = start
    er, ec = end
    # 범위내 있는 참가자 회전
    for index, player in enumerate(players):
        if sr <= player[0] <= er and sc <= player[1] <= ec:
            r, c = [player[0] - start[0], player[1] - start[1]]
            players[index] = [c + start[0], rotateN-1-r+start[1]]
    exitr, exitc = [exit[0]-start[0], exit[1]-start[1]]
    exit = [exitc+start[0], rotateN-1-exitr+start[1]]
    return exit

board = []
for _ in range(n):
    board.append(list(map(int, input().split(" "))))

players = []
for _ in range(m):
    r, c = map(int, input().split(" "))
    players.append([r-1,c-1])
er, ec = map(int, input().split(" "))
exit = [er-1, ec-1]


totalDistance = 0
for time in range(k):
    # 참가자 이동
    for index in range(len(players)):
        newPos, distance = movePlayer(board, players[index], exit)
        players[index] = newPos
        totalDistance += distance
    # 출구에 도달한 참가자 삭제
    tmp = []
    for player in players:
        if player[0] == exit[0] and player[1] == exit[1]:
            continue
        tmp.append(player)
    players = tmp
    # 참가자가 모두 탈출한 경우 게임 종료
    if len(players) == 0:
        break
    # 회전
    # 회전할 정사각형 범위 찾기
    start, end = getRotateRange(board, exit, players)
    # 회전하기, 벽 내구도 1깎기
    rotateN = rotateBoard(board, start, end)
    # 회전 범위 내에 있는 참가자와 출구 회전
    exit = rotatePlayerAndExit(start, end, exit, players, rotateN)

print(totalDistance)
print(exit[0]+1, exit[1]+1)