# 항해99_알고리즘_2021-03-15 백준번호: 11050_이항계수1../by 정석진

from math import factorial as f

n, k = map(int, input().split())

if k < 0 or k > n:
    print(0)
else:
    print(int(f(n)/(f(k)*f(n-k))))


# 이항 계수 공식
# ( n )    { n! / (k!(n-k)!)  0 <= k <= n }
# |   |  = { 0                   K < 0    }
# ( k )    { 0                   K > n    }
#
