def solution(N, number):
    dist = [0]
    for i in range(1, 9):
        tmp = []
        tmp.append(int(str(N) * i))
        for j in range(1, i):
            numlist1= dist[j]
            numlist2= dist[i-j]
            for num1 in numlist1:
                for num2 in numlist2:
                    if num2 == 0:
                        continue
                    tmp.append(num1 + num2)
                    tmp.append(num1 - num2)
                    tmp.append(num1 / num2)            
                    tmp.append(num1 * num2)
        result = list(set(tmp))
        for ans in result:
            if ans == number:
                return i
        dist.append(result)
    return -1
        