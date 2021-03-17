# 항해99_알고리즘_2021-03-15 백준번호: 1002_터렛../by 정석진

import math
n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)  # 두 원사이의 거리를 구하는 공식
    if dist == 0 and r1 == r2:  # 동심원이거나 일치해서 무한인 경우
        print(-1)
    elif r1+r2 == dist or abs(r1-r2) == dist:  # 외접, 내접
        print(1)
    elif abs(r1-r2) < dist < r1+r2:  # 두점에서 만날경우
        print(2)
    else:
        print(0)

# 해당 문제는 원의 방정식을 알면 쉽게 풀린다.
# 두 원의 중심 사이의 거리 => math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
# 경우의 수는 내접, 외접 할 경우 = 1
# 두점에서 만날경우 = 2
# 동심원이거나 완벽하게 일치 할경우 = 무한이기 때문에 -1
