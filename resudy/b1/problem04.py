num = int(input())

if num < 10:
    num * 10

origin = num
temp = 0
newnum = 0
count = 0

while True:
    temp = (num//10) + (num % 10)
    newnum = ((num % 10)*10) + (temp % 10)
    num = newnum
    count += 1
    if newnum == origin:
        break
print(count)
