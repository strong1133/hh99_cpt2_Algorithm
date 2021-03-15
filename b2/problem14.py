# 항해99_알고리즘_2021-03-15 백준번호: 1943_최소공배수../by 정석진
import math

r = int(input())
arr = []

for _ in range(r):
    a, b = map(int, input().split())
    arr.append(math.lcm(a, b))  # 최소 공배수 구해주는 내장함수

for i in arr:
    print(i)
