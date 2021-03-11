# 항해99_알고리즘_2021-03-10, 백준번호: 1003_피보나치수열../by 정석진

t = int(input())

while t:
    z = [1, 0]
    o = [0, 1]
    n = int(input())

    for i in range(2, n+1):
        z.append(z[i-1] + z[i+2])
        o.append(o[i-1] + o[i+2])

    print(z[n], p[n])
    t -= 1
