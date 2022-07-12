import math
import sys
def is_prime(num):
    if num == 2:
        return True
    if num == 1 or num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)+1), 2):
        if num % i == 0:
            return False
    return True

prime_num = []
for i in range(2, 123456*2+1):
    if is_prime(i):
        prime_num.append(i)
while True:
    num = int(sys.stdin.readline())
    if num == 0:
        break
    count = 0
    for i in prime_num:
        if num < i < num*2 + 1:
            count+=1
    print(count)