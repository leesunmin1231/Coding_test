import sys
from collections import deque

def bfs():
    q = deque();
    q.append(start) # 시작 노드 넣기
    while q: # 큐가 비어있지 않은 동안
        node = q.popleft(); # 앞에서 노드 꺼냄.
        if (node == end): # BFS 종료 조건
            return dist[node]
        for next in (node-1, node+1, node*2): # 탐색할 다음 노드 목록
            if (0 <= next <= MAX) and not dist[next]: 
                # dist 배열 인덱스 범위를 벗어나지 않고, 아직 방문하지 않은 노드일 때,
                q.append(next) # 방문할 노드 큐에 넣기
                dist[next] = dist[node] + 1 # 트리 깊이


MAX = 10**5
dist = [0]*(MAX+1)
start, end = map(int, sys.stdin.readline().split())
print(bfs())