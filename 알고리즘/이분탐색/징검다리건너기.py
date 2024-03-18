import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split(" ")))

minK = 1
maxK = (N-1) * (1+ abs(A[N-1] - A[0]))

while minK <= maxK:
    k = (minK+maxK) // 2
    q = [0]
    visit = [False] * N
    while q:
        node = q.pop()
        if visit[node]:
            continue
        visit[node] = True
        if (node == N-1):
            break
        for next in range(node+1, N):
            if visit[next]:
                continue
            if (next - node) * (1+abs(A[next]-A[node])) > k:
                continue
            q.append(next)
    if not visit[N-1]:
        minK = k+1
    else:
        maxK = k-1
print(minK)