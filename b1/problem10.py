# 항해99_알고리즘_2021-03-08, 백준번호: 10250_ACM호텔../by 정석진

T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    rn = N//H + 1
    f = N % H
    if f == 0:
        rn -= 1
        f = H

    print(f * 100 + rn)
