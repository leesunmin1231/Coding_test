from collections import deque
import copy

n, m, k = map(int, input().split(" "))
board = []
for _ in range(n):
    board.append(list(map(int, input().split(" "))))

def checkRowCol(r, c, prevR, prevC, isAttack):
    if isAttack:
        if r+c > prevR+prevC:
            return True
        if r+c == prevR + prevC and c > prevC:
            return True
        return False
    else:
        if r+c < prevR+prevC:
            return True
        if r+c == prevR + prevC and c < prevC:
            return True
        return False

# 공격할 사람, 공격 받을 사람 선정하기
def getAttackTarget(attackTimeBoard):
    attacker = [0,0]
    target = [0, 0]
    for r in range(n):
        for c in range(m):
            # 포탑 부서진 경우 제외
            if board[r][c] == 0:
                continue
            # 공격자 찾기
            if attacker[0] == 0 and attacker[1] == 0 and board[0][0] == 0:
                attacker = [r,c]
            # 공격력이 더 낮을 경우
            if board[r][c] < board[attacker[0]][attacker[1]]:
                attacker = [r,c]
            # 공격력 같을 경우 가장 최근에 공격한 포탑
            elif board[r][c] == board[attacker[0]][attacker[1]] and attackTimeBoard[r][c] > attackTimeBoard[attacker[0]][attacker[1]]:
                attacker = [r,c]
            # 행 열 비교
            elif board[r][c] == board[attacker[0]][attacker[1]] and attackTimeBoard[r][c] == attackTimeBoard[attacker[0]][attacker[1]] and checkRowCol(r,c, attacker[0], attacker[1], True):
                attacker = [r,c]
            
            # 공격 대상 찾기
            # 공격력이 더 높을 경우
            if board[r][c] > board[target[0]][target[1]]:
                target = [r,c]
            # 공격력 같을 경우 공격한지 오래된 포탑
            elif board[r][c] == board[target[0]][target[1]] and attackTimeBoard[r][c] < attackTimeBoard[target[0]][target[1]]:
                target = [r,c]
            # 행 열 비교
            elif board[r][c] == board[target[0]][target[1]] and attackTimeBoard[r][c] == attackTimeBoard[target[0]][target[1]] and checkRowCol(r,c, target[0], target[1],False):
                target = [r,c]
    return [attacker, target]

def checkCanLaserAttack(attack, target):
    # attack에서 target으로 이동 가능한지
    q = deque()
    q.append([attack, []])
    visit = [[False] * m for _ in range(n)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    while q:
        node, path = q.popleft()
        r,c = node
        if visit[r][c]:
            continue
        if r == target[0] and c == target[1]:
            return [True, path]
        visit[r][c] = True
        for i in range(4):
            nr = (r + dr[i]) % n
            nc = (c + dc[i]) % m
            if visit[nr][nc]:
                continue
            if board[nr][nc] == 0:
                continue
            tmp = copy.deepcopy(path)
            tmp.append([nr,nc])
            q.append([[nr,nc], tmp])
    return [False, []]


def laserAttack(attack, target, path, attackScale):
    for node in path:
        r, c = node
        if r == target[0] and c == target[1]:
            board[r][c] -= attackScale
        else:
            board[r][c] -= attackScale // 2
        if board[r][c] < 0:
            board[r][c] = 0


def bombAttack(attack, target, attackScale):
    dr = [-1, -1, -1, 1, 1, 1, 0, 0]
    dc = [0, 1, -1, 0, 1, -1, 1, -1]
    for i in range(8):
        r = (target[0] + dr[i]) % n
        c = (target[1] + dc[i]) % m
        if attack[0] == r and attack[1] == c:
            continue
        board[r][c] -= attackScale // 2
        if board[r][c] < 0:
            board[r][c] = 0
    board[target[0]][target[1]] -= attackScale
    if board[target[0]][target[1]] < 0:
        board[target[0]][target[1]] = 0

def printBoard(board):
    for row in board:
        print(row)
    print("")

def solution():
    attackTimeBoard = [[0] * m for _ in range(n)]
    for time in range(1, k+1):
        # 공격할 사람, 공격 받을 사람 선정하기
        attack, target = getAttackTarget(attackTimeBoard)
        # attackTimeBoard 갱신
        attackTimeBoard[attack[0]][attack[1]] = time

        # 기존 보드 저장
        prevBoard = copy.deepcopy(board)

        # 공격
        # 레이저 공격 가능한지 체크
        isLaserAttack, path = checkCanLaserAttack(attack, target)
   
        # 공격자 공격력 변경
        attackScale = board[attack[0]][attack[1]] + n + m
        board[attack[0]][attack[1]] = attackScale
        # 레이저 공격
        if isLaserAttack:
            laserAttack(attack, target, path, attackScale)
        # 포탄 공격
        if not isLaserAttack:
            bombAttack(attack, target, attackScale)

        # 포탑 정비
        for r in range(n):
            for c in range(m):
                # 공격자 제외
                if r == attack[0] and c == attack[1]:
                    continue
                # 부서진 포탑 제외
                if board[r][c] == 0:
                    continue
                # 공격을 안받아서 공격력이 이전과 같다면
                if prevBoard[r][c] == board[r][c]:
                    board[r][c] += 1

        # 포탑 1개남았는지 체크
        count = 0
        for r in range(n):
            for c in range(m):
                if board[r][c] > 0:
                    count+=1
        if count == 1:
            break

    # 가장 강한 포탑 공격력 가져오기
    ans = 0
    for r in range(n):
        for c in range(m):
            if board[r][c] > ans:
                ans = board[r][c]
    return ans

print(solution())