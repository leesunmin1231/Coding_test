def solution(m, n, puddles):
    dist = [[0 for j in range(m+1)] for i in range(n+1)]
    for pud in puddles:
        dist[pud[1]][pud[0]] = -1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if dist[i][j] == -1:
                dist[i][j] = 0
                continue
            if i == 1 and j == 1:
                dist[i][j] = 1
                continue
            dist[i][j] = dist[i-1][j] + dist[i][j-1]
    return dist[n][m]

print(solution(4,3,[[2,2]]))