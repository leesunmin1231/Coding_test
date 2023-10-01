n, m, h, k = map(int,input().split(" "))
dr = {
    'R': 0,
    'L': 0,
    'U': -1,
    'D': 1
}
dc = {
    'R': 1,
    'L': -1,
    'U': 0,
    'D': 0
}

def check_out_of_range(r,c):
    if r < 0 or r >= n:
        return True
    if c < 0 or c >= n:
        return True
    return False

def move_runners(playerboard, catch, runners):
    cr = catch[0]
    cc = catch[1]
    reverseD = {
        'R': 'L',
        'L' : 'R',
        'D': 'U',
        'U': 'D'
    }
    new_playerBoard = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(len(runners)):
        r, c, d = runners[i]
        # 멀리있는 애들 이동 안함
        if abs(cr-r) + abs(cc-c) > 3:
            new_playerBoard[r][c].append(d)
            continue
        # 가까운 애들 이동
        nr = r + dr[d]
        nc = c + dc[d]
        nd = d
        if check_out_of_range(nr, nc):
            nr = r + dr[reverseD[d]]
            nc = c + dc[reverseD[d]]
            nd = reverseD[d]
        # 이동할 곳에 술래 있으면 이동 안함
        if cr == nr and cc == nc:
            new_playerBoard[r][c].append(d)
            continue
        # 이동할 애들 자리 갱신
        runners[i] = [nr, nc, nd]
        new_playerBoard[nr][nc].append(nd)
    return new_playerBoard

def move_catcher(catch):
    r, c, d, reverseFlag = catch
    nr = r + dr[d]
    nc = c + dc[d]
    nd = d
    nReverse = reverseFlag
    if not reverseFlag:
        if d == "U" and nr - nc == -1:
            nd = 'R'
        if d == "R" and nr + nc == 2 * (n//2):
            nd = "D"
        if d == "D" and nr - nc == 0:
            nd = "L"
        if d == "L" and nr + nc == 2 * (n//2):
            nd = "U"
    # 역방향
    if reverseFlag:
        if d == "D" and nr + nc == 2 * (n//2):
            nd = "R"
        if d == "R" and nr - nc == 0:
            nd = "U"
        if d == "U" and nr + nc == 2 * (n//2):
            nd = "L"
        if d == "L" and nr - nc == -1:
            nd = "D"
    # 끝점
    if nr == 0 and nc == 0:
        nd = "D"
        nReverse = True
    if nr == n//2 and nc == n//2:
        nd = "U"
        nReverse = False
    return [nr, nc, nd, nReverse]

def catch_runnters(playerboard, treeboard, catch):
    count = 0
    r, c, d, rev = catch
    for i in range(3):
        nr = r + dr[d] * i
        nc = c + dc[d] * i
        if check_out_of_range(nr,nc):
            continue
        # 나무가 있는 경우
        if treeboard[nr][nc] == 1:
            continue
        count += len(playerboard[nr][nc])
        playerboard[nr][nc] = []
    return count

def upgradeRunners(playerboard):
    tmp = []
    for r in range(n):
        for c in range(n):
            if len(playerboard[r][c]) != 0:
                for d in playerboard[r][c]:
                    tmp.append([r, c, d])
    return tmp

# 0: 빈공간, 1: 나무
treeboard = [[0] * n for _ in range(n)]
# 1: 도망자 좌우, 2: 도망자 상하
playerboard = [[[] for _ in range(n)] for _ in range(n)]
runners = []
for _ in range(m):
    x, y, d = map(int, input().split(" "))
    # d = 1: 좌우(오른쪽 시작), d = 2: 상하(아래쪽 시작)
    if d == 1:
        playerboard[x-1][y-1] = ['R']
        runners.append([x-1, y-1, 'R'])
    else:
        playerboard[x-1][y-1] = ['D']
        runners.append([x-1, y-1, 'D'])

for _ in range(h):
    x, y = map(int, input().split(" "))
    treeboard[x-1][y-1] = 1

catch = [n//2, n//2, 'U', False]
score = 0

def printBoard(board):
    for row in board:
        print(row)
    print("")


for t in range(1,k+1):
    # 도망자 움직이기
    playerboard = move_runners(playerboard, catch, runners)
    # 술래 움직이기
    catch = move_catcher(catch)
    # 도망자 잡기
    count = catch_runnters(playerboard, treeboard, catch)
    # runners 갱신
    if count != 0:
        runners = upgradeRunners(playerboard)
    # 점수 갱신
    score += t*count

print(score)