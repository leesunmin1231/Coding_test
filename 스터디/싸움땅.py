n,m,k = map(int,input().replace("\n", '').strip().split(" "))
board = []
for _ in range(n):
    tmp = list(map(int, input().replace("\n", '').strip().split(" ")))
    board.append([[x] for x in tmp])

players = []
for _ in range(m):
    x, y, d, s = map(int,input().replace("\n", '').strip().split(" "))
    players.append([x-1,y-1,d,s,0, 0])
# 0,1,2,3
# 위,오른쪽,아래 왼쪽
dr = [-1,0,1,0]
dc = [0,1,0,-1]

def checkIsPlayer(players, nr,nc):
    flag=False
    target=None
    for j in range(m):
        check = players[j]
        if nr == check[0] and nc == check[1]:
            flag = True
            target = j
            break
    return [flag, target]

def checkOutOfRange(r,c):
    if r < 0 or r >= n:
        return True
    if c < 0 or c >= n:
        return True
    return False

def moveCurPlayer(r,c,d):
    nr = r + dr[d]
    nc = c + dc[d]
    nd = d
    if checkOutOfRange(nr,nc):
        nd = (d+2) % 4
        nr = r + dr[nd]
        nc = c + dc[nd]
        return [nr,nc,nd]
    return [nr,nc,nd]

def getNewGun(board, gun, nr,nc):
    if len(board[nr][nc]) == 0:
        return gun
    mostStrong = max(board[nr][nc])
    newGun = gun
    # 총 바꿔 들기
    if mostStrong > gun:
        newGun = mostStrong
        board[nr][nc].remove(mostStrong)
        board[nr][nc].append(gun)
    return newGun

def moveLosePlayer(board, player, players):
    r, c, d, s, point, gun = player
    nr = r + dr[d]
    nc = c + dc[d]
    nd = d
    newGun = gun
    if gun != 0:
        board[r][c].append(gun)
        newGun = 0
    for i in range(1,5):
        if not checkOutOfRange(nr,nc) and not checkIsPlayer(players, nr,nc)[0]:
            break
        nd = (d+i) % 4
        nr = r + dr[nd]
        nc = c + dc[nd]
    if checkOutOfRange(nr,nc) or checkIsPlayer(players, nr,nc)[0]:
        return [r,c,d,s,point,newGun]
    if len(board[nr][nc]) != 0:
        newGun = max(board[nr][nc])
        board[nr][nc].remove(newGun)
    return [nr,nc,nd,s,point,newGun]

def curPlayerWin(cur, target):
    curS = cur[0]
    curGun = cur[1]
    targetS = target[0]
    targetGun = target[1]
    if curS+curGun > targetS+ targetGun:
        return [True, (curS+curGun) - (targetS+ targetGun)]
    if curS+curGun < targetS+ targetGun:
        return [False, (targetS + targetGun) - (curS+curGun)]
    if curS+curGun == targetS+ targetGun and curS > targetS:
        return [True, (curS+curGun) - (targetS+ targetGun)]
    if curS+curGun == targetS+ targetGun and curS < targetS:
        return [False, (targetS + targetGun) - (curS+curGun)]

for _ in range(k):
    for i in range(m):
        r,c,d,s,point, gun = players[i]
        newGun = gun
        # 현재 플레이어 이동
        nr, nc, nd = moveCurPlayer(r,c,d)

        # 이동한 방향에 플레이어 없는지 확인
        flag, target = checkIsPlayer(players, nr,nc)
    
        players[i] = [nr, nc, nd, s, point, newGun]

        # 이동 방향에 플레이어 있을 경우
        if flag:
            isCurWin, newPoint = curPlayerWin([s,gun],[players[target][3], players[target][5]])
            # 현재 플레이어가 이긴 경우
            if isCurWin:
                point += newPoint
                # 진 플레이어 이동
                players[target] = moveLosePlayer(board,players[target], players)
                # 이긴 플레이어 총 획득
                newGun = getNewGun(board, gun, nr,nc)
            # 타겟 플레이어가 이긴 경우
            else:
                players[target][4] += newPoint
                 # 진 플레이어 이동
                nr, nc, nd, s, point, newGun = moveLosePlayer(board, players[i] , players)
                # 이긴 플레이어 총 획득
                targetNewGun = getNewGun(board, players[target][5], players[target][0], players[target][1])
                players[target][5] = targetNewGun
            players[i] = [nr, nc, nd, s, point, newGun]
        
        # 이동 방향에 플레이어 없고 총이 있는 경우
        elif not flag and len(board[nr][nc]) != 0:
            newGun = getNewGun(board,gun,nr,nc)
            players[i] = [nr, nc, nd, s, point, newGun]

print(' '.join([str(x[4]) for x in players]))