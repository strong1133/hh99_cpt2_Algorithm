# 항해99_알고리즘_2021-03-05, 백준번호: 1110_알람 시계 /by 정석진

num = int(input())

if num < 10:
    num *= 10
origin = num
temp = 0
newnum = 0
count = 0

while True:
    temp = (num // 10) + (num % 10)
    newnum = (num % 10)*10 + (temp % 10)
    count += 1
    num = newnum
    if newnum == origin:
        break
print(count)
