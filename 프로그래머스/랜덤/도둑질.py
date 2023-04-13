# 25분 소요

def solution(money):
    totalHome = len(money)
    # 첫번째 집을 훔치는 경우, (원형 배치라 마지막 집은 훔칠 수 없다.)
    dist = [0] * (totalHome-1)
    dist[0] = money[0]
    dist[1] = max([money[0], money[1]])
    for i in range(2, totalHome-1):
        dist[i] = max([dist[i-1], dist[i-2] + money[i]])
    
    # 첫번째 집을 훔치지 않는 경우, (마지막 집을 훔칠 수도, 안훔칠 수도 있다.)
    dist2 = [0] * totalHome
    dist2[1] = money[1]
    for i in range(2, totalHome):
        dist2[i] = max([dist2[i-1], dist2[i-2] + money[i]])
    return max(dist[-1], dist2[-1])