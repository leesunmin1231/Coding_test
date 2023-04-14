from collections import deque

def bfs(board, start):
    q = deque()
    q.append(start)
    n = len(board)
    dist = [0] * n
    dist[start] = 1
    count = 0
    while q:
        node = q.popleft()
        count += 1
        for next in [index for index, x in enumerate(board[node]) if x]:
            if dist[next]:
                continue
            dist[next] = dist[node] + 1
            q.append(next)
    return count

def solution(n, wires):
    board = [[0] * (n+1) for _ in range(n+1)]
    for wire in wires:
        board[wire[0]][wire[1]] = 1
        board[wire[1]][wire[0]] = 1
    ans = n
    for wire in wires:
        board[wire[0]][wire[1]] = 0
        board[wire[1]][wire[0]] = 0
        tree1 = bfs(board, wire[0])
        tree2 = bfs(board, wire[1])
        if abs(tree1-tree2) < ans:
            ans = abs(tree1-tree2)
        board[wire[0]][wire[1]] = 1
        board[wire[1]][wire[0]] = 1
    return ans