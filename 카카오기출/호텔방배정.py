def solution(k, room_number):
    answer = []
    rooms = {}

    for number in room_number:
        if number not in rooms:
            rooms[number] = number+1
            answer.append(number)
        else:
            target = rooms[number]
            visit = []
            while target in rooms:
                visit.append(target)
                target = rooms[target]
            rooms[target] = target + 1
            for node in visit:
                rooms[node] = target + 1
            answer.append(target)
    
    return answer

print(solution(10, [1,3,4,1,3,1]))