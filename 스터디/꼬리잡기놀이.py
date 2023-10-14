from collections import deque

n, m, k = map(int, input().replace("\n", "").strip().split(" "))
board = []
for _ in range(n):
    board.append(list(map(int,input().replace("\n", "").strip().split(" "))))
# 0: 빈간, 1: 머리사람, 2: 사람, 3: 꼬리사람, 4: 이동선

dr = [0,-1,0,1]
dc = [1,0,-1,0]


def searchTeam(team, start, board):
    q = deque()
    q.append(start)
    team["middle"] = []
    visit = [[False] * n for _ in range(n)]
    while q:
        r, c = q.popleft()
        if board[r][c] == 3:
            team["tail"] = [r,c]
        if visit[r][c]:
            continue
        visit[r][c] = True
        if board[r][c] == 2:
            team["middle"].append([r,c])
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= n:
                continue
            if nc < 0 or nc >= n:
                continue
            if visit[nr][nc]:
                continue
            if board[nr][nc] != 2 and board[nr][nc] != 3:
                continue
            q.append([nr,nc])
    q = deque()
    q.append(start)
    team["middle"] = []
    visit = [[False] * n for _ in range(n)]
    while q:
        r, c = q.popleft()
        if visit[r][c]:
            continue
        visit[r][c] = True
        if board[r][c] == 2:
            team["middle"].append([r,c])
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= n:
                continue
            if nc < 0 or nc >= n:
                continue
            if visit[nr][nc]:
                continue
            if board[nr][nc] != 2:
                continue
            q.append([nr,nc])
    return team

def findNumPosition(board, num, cur):
    r,c = cur
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= n:
            continue
        if nc < 0 or nc >= n:
            continue
        if board[nr][nc] == num:
            return [nr,nc]


def moveTail(tail, board):
    newPos = findNumPosition(board, 2, tail)
    return newPos

def movePerson(person, board):
    newPos = findNumPosition(board, 4, person)
    if not newPos:
        newPos = findNumPosition(board, 3, person)
    board[newPos[0]][newPos[1]] = board[person[0]][person[1]]
    board[person[0]][person[1]] = 4
    return newPos

def findTargets(board, start, d):
    r,c = start
    i = 0
    while i < n:
        nr = r + (dr[d] * i)
        nc = c + (dc[d] * i)
        if board[nr][nc] != 4 and board[nr][nc] != 0:
            return [nr,nc]
        i+=1

def findHead(target, board):
    q = deque()
    q.append([target[0], target[1], 1])
    visit = [[False] * n for _ in range(n)]
    result = 0
    if board[target[0]][target[1]] == 1:
        return [target, 1]
    while q:
        r,c, distance = q.popleft()
        if visit[r][c]:
            continue
        visit[r][c] = True
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= n:
                continue
            if nc < 0 or nc >= n:
                continue
            if visit[nr][nc]:
                continue
            if board[nr][nc] == 1:
                head = [nr,nc]
                result = distance
            if board[nr][nc] != 2:
                continue
            q.append([nr,nc,distance+1])
    return [head, result+1]

def changeDirection(teamHead, teams, board):
    for team in teams:
        if team["head"][0] == teamHead[0] and team["head"][1] == teamHead[1]:
            tmp = team["tail"]
            team["tail"] = team["head"]
            team["head"] = tmp
            board[team["head"][0]][team["head"][1]] = 1
            board[team["tail"][0]][team["tail"][1]] = 3
            team["middle"].reverse()

teams = [] # {head: [r,c], middle: [[r,c], [r,c]...], tail: [r,c]}
for r in range(n):
    for c in range(n):
        if board[r][c] == 1:
            team = {"head": [r,c]}
            team = searchTeam(team, [r,c], board)
            teams.append(team)

ans = 0

for turn in range(k):
    # 모든 팀 머리 사람 따라서 한칸 이동
    for team in teams:
        head = team["head"]
        middle = team["middle"]
        tail = team["tail"]
        # 꼬리 사람 먼저 이동
        newTail = moveTail(tail, board)
        team["tail"] = newTail
        # 나머지 사람 이동
        team["head"] = movePerson(head, board)
        newMiddle = []
        for person in middle:
            newMiddle.append(movePerson(person, board))
        team["middle"] = newMiddle
        board[newTail[0]][newTail[1]] = 3
        if team["head"][0] == tail[0] and team["head"][1] == tail[1]:
            board[tail[0]][tail[1]] = 1
        else:
            board[tail[0]][tail[1]] = 4  
    # 공 던지기
    d = (turn // n) % 4
    line = turn % n
    startPoints = [[line, 0], [n-1, line], [n-1-line, n-1], [0, n-1-line]]

    # 던진 공 받은 팀 점수 획득, 방향 변환
    target = findTargets(board, startPoints[d], d)
    if target:
        teamHead, distance = findHead(target, board)
        # 점수 획득
        ans += distance*distance
        changeDirection(teamHead, teams, board)

print(ans)