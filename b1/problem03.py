# 항해99_알고리즘_2021-03-05, 백준번호: 2884 _알람 시계 /by 정석진

h, m = map(int, input().split())

if m > 44:
    m = m - 45
elif m <= 44 and h >= 1:
    h = h-1
    m = m+15
else:
    h = 23
    m = m+15
print(h, m)
