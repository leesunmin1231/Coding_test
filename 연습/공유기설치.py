import sys

input = sys.stdin.readline
N, C = map(int, input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()

start = arr[1] - arr[0] # 공유기 사이 거리 최솟값(첫번째 집엔 무조건 공유기를 설치하니까)
end = arr[-1] - arr[0] # 공유기 사이 거리 최댓값
result = 0
 
while start <= end:
    mid = (start + end) // 2 # 가장 인접한 공유기 사이의 거리
    value = arr[0] # 공유기 초기 설치 위치
    count = 1 # 공유기 설치 개수
    # 현재의 mid(공유기 사이 거리)를 이용한 공유기 설치
    for i in range(1, N): # 앞에서부터 설치
        if arr[i] >= value + mid:
            # 공유기 설치 위치 변경
            value = arr[i]
            # 개수 증가
            count += 1
    # c개 이상의 공유기를 설치할 수 있는 경우, 공유기 사이 거리 증가
    if count >= C: 
        start = mid + 1
        result = end
    # c개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
    else:
        end = mid - 1
print(result)