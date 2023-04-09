import sys
from collections import deque
input = sys.stdin.readline

board = []
arr = []
for _ in range(5):
    tmp = list(input())[:-1]
    board.append(tmp)
    arr += tmp



# def bfs(start):
#     count = 0
#     q = deque()
#     q.append(start)
#     dist = []# total, s
#     for _ in range(5):
#         dist.append([[0,0] for _ in range(5)])
#     while q:
#         node = q.popleft()
#         if dist[node[0]][node[1]][0] == 6 and dist[node[0]][node[1]][1] >= 3:
#             count+=1
#         elif dist[node[0]][node[1]][0] == 6 and dist[node[0]][node[1]][1] < 3:
#             continue
#         for next in [[node[0]+1,node[1]],[node[0],node[1]+1]]:
#             if next[0] >= 5 or next[1]>=5:
#                 continue
#             if board[next[0]][next[1]] == "S":
#                 dist[next[0]][next[1]][1] = dist[node[0]][node[1]][1] + 1
#             else:
#                 dist[next[0]][next[1]][1] = dist[node[0]][node[1]][1]
#             dist[next[0]][next[1]][0] = dist[node[0]][node[1]][0] + 1
#             q.append(next)
#     for i in range(5):
#         print(dist[i])
#     print("")
#     return count


# count = 0
# for row in range(5):
#     for col in range(5):
#         if board[row][col] == "S":
        
# print(count)