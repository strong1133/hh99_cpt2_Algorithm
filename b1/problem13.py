# 항해99_알고리즘_2021-03-09, 백준번호: 11651_좌표정렬../by 정석진


num = int(input())
a = []

for i in range(num):
    [x, y] = map(int, input().split())
    res = [y, x]
    a.append(res)

b = sorted(a)
for i in range(num):
    print(b[i][1], b[i][0])
