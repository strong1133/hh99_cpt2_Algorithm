# 항해99_알고리즘_2021-03-15 백준번호: 2231_분해합../by 정석진

r = int(input())
res = 0
for i in range(1, r+1):
    d = list(map(int, str(i)))
    s = i + sum(d)
    if s == r:
        res = i
        break
print(res)
