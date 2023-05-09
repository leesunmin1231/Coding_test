import sys

def reverse(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
          A[i][j] = 1 - A[i][j]

def check():
  for i in range(N):
    for j in range(M):
      if A[i][j] != B[i][j]:
        return False
  
  return True


input = sys.stdin.readline

N, M = map(int, input().split(" "))
A = []
B=[]
for _ in range(N):
    A.append(list(map(int, list(input())[:-1])))
for _ in range(N):
    B.append(list(map(int, list(input())[:-1])))

ans = 0
for i in range(N-2):
  for j in range(M-2):
    if A[i][j] != B[i][j]:
      reverse(i, j)
      ans += 1

if check():
  print(ans)
else:
  print("-1")
