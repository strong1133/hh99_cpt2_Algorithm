# 항해99_알고리즘_2021-03-15 백준번호: 2579_계단오르기../by 정석진

r = int(input())
stairs = []
for _ in range(r):
    stairs.append(int(input()))
dp = []


def up():
    if r == 0:
        return
    dp.append(stairs[0])
    if len(stairs) == 1:
        return dp.pop()
    elif len(stairs) == 2:
        dp.append(max(stairs[0]+stairs[1], stairs[1]))
        return dp.pop()
    dp.append(max(stairs[0]+stairs[1], stairs[1]))
    dp.append(max(stairs[0]+stairs[2], stairs[1]+stairs[2]))
    for i in range(3, r):
        dp.append(max(dp[i-2]+stairs[i], dp[i-3]+stairs[i]+stairs[i-1]))
    return dp.pop()


print(up())
