from itertools import permutations

def transferToArr(expression):
    arr = []
    i = 0
    while i < len(expression):
        if expression[i] in "*-+":
            arr.append(expression[i])
            i+=1
            continue
        start = i
        while i < len(expression) and expression[i] not in "*-+":
            i += 1
        arr.append(int(expression[start:i]))
    return arr

def transferToBackword(arr, rateDic):
    exp = []
    stack = []
    for target in arr:
        if target not in ["-", "*", "+"]:
            exp.append(target)
            continue
        if not stack:
            stack.append(target)
            continue
        if rateDic[stack[-1]] < rateDic[target]:
            stack.append(target)
            continue
        while stack and rateDic[stack[-1]] >= rateDic[target]:
            exp.append(stack.pop())
        stack.append(target)
    while stack:
        exp.append(stack.pop())
    return exp

def solution(expression):
    rates = list(permutations(["*", "-", "+"], 3))
    expArr = transferToArr(expression)
    ans = 0
    
    for rate in rates:
        rateDic = {}
        for idx, r in enumerate(rate):
            rateDic[r] = idx
        # 후위표기법으로 변환
        backwordNotaion = transferToBackword(expArr, rateDic)
        # 계산
        stack = []
        for token in backwordNotaion:
            if token in ["-", "*", "+"]:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "+":
                    stack.append(num1+num2)
                elif token == "*":
                    stack.append(num1*num2)
                elif token == "-":
                    stack.append(num1-num2)
            else:
                stack.append(token)
        result = stack.pop()
        if abs(result) > ans:
            ans = abs(result)
    return ans
print(solution("100-200*300-500+20"))