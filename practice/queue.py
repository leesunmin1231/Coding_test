def solution(bridge_length, weight, truck_weights):
    cur_weight = []
    curr = [] # 트럭의 위치 넣는다 [끝, ... , 1]
    answer = 0
    i = 0
    while i < len(truck_weights):
        if (sum(cur_weight) + truck_weights[i]) <= weight and len(curr) < bridge_length:
            # 현재 다리에 트럭 하나 추가
            for j in range(len(curr)): # 위치 갱신
                curr[j] += 1
            curr.append(1) # 새 트럭 추가
            cur_weight.append(truck_weights[i])
            answer+=1
            i+=1
        elif curr[0] == bridge_length:
            # 다리 끝에 트럭이 왔을 경우.
            curr.pop(0)
            cur_weight.pop(0)
            for j in range(len(curr)): # 위치 갱신
                curr[j] += 1
            answer+=1
            if (sum(cur_weight) + truck_weights[i]) <= weight:
                curr.append(1)
                cur_weight.append(truck_weights[i])
                i+=1
        else:
            answer+=1
            for j in range(len(curr)): # 위치 갱신
                curr[j] += 1
    while curr:
        if curr[0] == bridge_length:
            curr.pop(0)
            cur_weight.pop(0)
        for j in range(len(curr)): # 위치 갱신
            curr[j] += 1
        answer+=1

            
    return answer
print(solution(2,10,[7,4,5,6]))