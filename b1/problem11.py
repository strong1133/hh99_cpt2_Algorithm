# 항해99_알고리즘_2021-03-08, 백준번호: 1929_소수구하기../by 정석진
import math


def issosu(num):
    if num == 1:
        return False
    n = int(math.sqrt(num))
    for v in range(2, n+1):
        if num % v == 0:
            return False
    return True


a, b = map(int, input().split())
for i in range(a, b+1):
    if issosu(i):
        print(i)
