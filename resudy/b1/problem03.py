h, m = map(int, input().split())

if m > 44:
    m -= 45
elif m < 45 and h >= 1:
    h -= 1
    m += 15
else:
    h = 23
    m += 15
print(h, m)
