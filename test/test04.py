# 항해99_알고리즘_2021-03-19, **시험2_1** 백준번호:1920 _수 찾기 /by 정석진

import sys
input = sys.stdin.readline

r = int(input())
arr = set(map(int, input().split()))

n = int(input())
arr2 = list(map(int, input().split()))

for x in arr2:
    if x in arr:
        print(1)
    else:
        print(0)
