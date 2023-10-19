import sys

input = sys.stdin.readline

sen = list(input().strip())

def solution():
    stack = []
    layer = 1 # 이중, 삼중 괄호는 이 변수로 관리
    total = 0

    for i in range(len(sen)):
        if sen[i] == "(":
            stack.append(sen[i])
            layer *= 2
        elif sen[i] == "[":
            stack.append(sen[i])
            layer *= 3
        elif sen[i] == "]":
            if not stack:
                return 0
            if stack.pop() != "[":
                return 0
            # 가장 안쪽 괄호일 경우 중첩 계산 값 더해주기
            if sen[i-1] == "[":
                total += layer
            layer //= 3
        elif sen[i] == ")":
            if not stack:
                return 0
            if stack.pop() != "(":
                return 0
            # 가장 안쪽 괄호일 경우 중첩 계산 값 더해주기
            if sen[i-1] == "(":
                total += layer
            layer //= 2
    if stack:
        return 0
    return total

print(solution())