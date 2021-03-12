# 항해99_알고리즘_2021-03-12, **시험1_3** 백준번호:2751 _정렬히기2 /by 정석진
import sys

r = int(input())
arr = set()

for i in range(r):
    a = int(sys.stdin.readline())
    arr.add(a)

for i in sorted(arr):
    print(i)
