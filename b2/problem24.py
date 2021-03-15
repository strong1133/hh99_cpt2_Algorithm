# 항해99_알고리즘_2021-03-15 백준번호: 15650_N과 M 2../by 정석진

from itertools import combinations
n, m = map(int, input().split())
a = combinations(range(1, n+1), m)

for i in a:
    print(*i)
