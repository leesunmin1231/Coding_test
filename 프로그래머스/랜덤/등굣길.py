# 1시간 실화냐

def solution(m, n, puddles):
    dist = [[0] * m for _ in range(n)]
    for pud in puddles:
        c, r = pud
        dist[r-1][c-1] = -1
    for r in range(n):
        for c in range(m):
            if r==0 and c ==0 :
                dist[0][0] = 1
                continue
            if dist[r][c] == -1: continue
            prev = 0
            if r > 0 and dist[r-1][c] != -1:
                prev += dist[r-1][c]
            if c > 0 and dist[r][c-1] != -1:
                prev += dist[r][c-1]
            dist[r][c] = prev
    return dist[n-1][m-1]%1000000007