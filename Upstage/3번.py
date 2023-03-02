def solution(N, trees):
    answer = 0
    check = [0 ,N-1]
    for x in range(N):
        isTree = [pos for pos in trees if pos[0] == x and pos[1] <= check[1]]
        print(isTree)
        if len(isTree) == 0:
            continue
        answer += 1
        check = isTree[0]
    return answer

trees = [[4, 3], [3, 2], [2, 2], [1, 4]]
print(solution(5, trees))

    