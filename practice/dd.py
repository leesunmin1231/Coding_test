def solution(numbers, target):
    answer = 0
    result = 0
    index = 0
    stack = []
    inx_lst =[]
    while True:
        if len(stack) != 0:
            data = stack.pop()
            result = data[1]
            index = data[0]
        for i in range(index, len(numbers)):
            if i in inx_lst:
                result -= numbers[i]
                inx_lst.remove(i)
            else:
                stack.append([i,result])
                inx_lst.append(i)
                result += numbers[i]
        if result == target:
            answer+=1
        if len(stack) == 0:
            break
    return answer

numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers,target))