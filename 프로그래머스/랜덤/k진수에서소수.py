# 시간: 32분
# 제곱근 범위를 잘못해둬서 또 실수 남,,, 무조건 범위는 정확하게, 넉넉하게 잡자


import math 

def isPrime(num):
    if num == 2:
        return True
    if num == 1:
        return False
    if num % 2 == 0:
        return False
    for i in range(3, math.ceil(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def convert_base(n, k):
    arr = []
    while n != 0:
        r = n % k
        n = n // k
        arr.append(str(r))
    arr.reverse()
    return ''.join(arr)

def solution(n, k):
    converted = convert_base(n, k).split("0")
    count = 0
    for p in converted:
        if p == "":
            continue
        if isPrime(int(p)):
            count += 1
    return count