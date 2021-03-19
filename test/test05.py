# 항해99_알고리즘_2021-03-19, **시험2_2** 백준번호:15649 _N과 M 1 /by 정석진

from itertools import permutations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = permutations(range(1, n+1), m)
for i in a:
    print(*i)
