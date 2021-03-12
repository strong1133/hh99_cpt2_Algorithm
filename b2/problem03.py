# 항해99_알고리즘_2021-03-12, 백준번호: 1011_Fly me to the Alpha Centauri/by 정석진

import math

r = int(input())
res = []
for _ in range(r):
    x, y = map(int, input().split())
    num = y-x
    if num <= 3:
        res.append(num)
    else:
        distance = int(math.sqrt(num))
        if num == distance**2:
            res.append(2*distance-1)
        elif distance**2 < num <= distance**2 + distance:
            res.append(2*distance)
        else:
            res.append(2*distance+1)

for i in res:
    print(i)
