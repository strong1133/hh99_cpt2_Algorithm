# 항해99_알고리즘_2021-03-15 백준번호: 2609_최대공약수와 최소공배수../by 정석진
import math
a, b = map(int, input().split())

print(math.gcd(a, b))
print(math.lcm(a, b))


# 유클리드 호제법으로 구하는 방식
def _gcd(x, y):  # => 유클리드호제법으로 최대 공약수 구하는 공식
    while y:
        x, y = y, x % y
    return x


def _lcm(x, y):  # => 유클리드호제법으로 최소 공배수 구하는 공식
    return x*y // _gcd(x, y)
