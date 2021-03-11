# 항해99_알고리즘_2021-03-08, 백준번호: 1929_소수구하기../by 정석진
import math


def issosu(num):  # 9
    if num == 1:
        return False

    # 시간 복잡도 감소를 위해 제곱근 방식으로 처리 9의 제곱근 3, 10~15의 제곱근도 3, 16의 제곱근 4
    n = int(math.sqrt(num))  # 3

    for v in range(2, n+1):  # 2 ~ 4
        if num % v == 0:  # 9 % 2 = 0
            return False
    return True


a, b = map(int, input().split())
for i in range(a, b):  # 3 ~10
    if issosu(i):  # 3  , 4, 5 ,6
        print(i)  # 3 5

#3, 5, 7,
