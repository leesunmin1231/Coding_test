import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split(" "))

board = []
for _ in range(N):
    board.append(list(input())[:-1])

def init():
    # R, O, B위치 찾기
    R = []
    O = []
    B = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                R = [i, j]
            if board[i][j] == 'O':
                O = [i, j]
            if board[i][j] == 'B':
                B = [i, j]
    return R, O, B

def move(r, c, dx, dy):
    count = 0
    mover = r
    movec = c
    while board[mover + dy][movec + dx] != '#' and board[mover][movec] != 'O':
        mover += dy
        movec += dx
        count += 1
    return mover, movec, count


def bfs():
    redq = deque()
    blueq = deque()
    R, O, B = init()
    redq.append(R)
    blueq.append(B)
    visited = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]

    dx = [-1, 1, 0,0]
    dy = [0,0, 1, -1]
    visited[R[0]][R[1]][B[0]][B[1]] = 1
    while redq:
        r, c = redq.popleft()
        br, bc = blueq.popleft()
        # 이동 횟수 10회 이상이면 실패
        if visited[r][c][br][bc] > 10:
            return -1
        for i in range(4):
            next_r, next_c, total = move(r,c, dx[i], dy[i])
            bnext_r, bnext_c, btotal = move(br,bc, dx[i], dy[i])
            # 파란공 구멍에 빠지면 실패
            if O == [bnext_r, bnext_c]:
                continue
            # 빨간공 구멍에 빠지면 성공
            if O == [next_r, next_c]:
                return visited[r][c][br][bc]
            # 두 공 위치가 같을때
            if next_r == bnext_r and next_c == bnext_c:
                if total > btotal:
                    next_r -= dy[i]
                    next_c -= dx[i]
                else:
                    bnext_c -= dx[i]
                    bnext_r -= dy[i]
            if visited[next_r][next_c][bnext_r][bnext_c]:
                continue
            # 방문한 곳 갱신
            visited[next_r][next_c][bnext_r][bnext_c] = visited[r][c][br][bc] + 1
            redq.append([next_r, next_c])
            blueq.append([bnext_r, bnext_c])
    return -1
            
print(bfs())