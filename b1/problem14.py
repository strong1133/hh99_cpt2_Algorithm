# 항해99_알고리즘_2021-03-09, 백준번호: 2805_나무자르기/by 정석진

from sys import stdin
from collections import Counter

n, m = map(int, stdin.readline().split())
tree = Counter(map(int, stdin.readline().split()))

start, end = 0, max(tree.keys())

ans = 0

while end >= start:
    mid = (start+end)//2
    s = 0
    for i in tree.keys():
        if i > mid:
            s += (i-mid) * tree[i]

    if s < m:
        end -= 1
    elif s == m:
        ans = mid
        break
    else:
        ans = mid
        start += 1

print(ans)
