def solution(price, money, count):
    total = 0
    for i in range(count):
        total += price*(i+1)
    if total > money:
        return total - money
    return 0