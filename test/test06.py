# 항해99_알고리즘_2021-03-19, **시험2_3** 백준번호: 1904_01타일 /by 정석진

# n =1 : 1
# n =2 : 00, 11
# n =3 : 1 00, 00 1
# dp[n] = dp[n-2] + dp[n-1]  -> 동적계획법 메모이제이션

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
    dp[i] = (dp[i-1]+dp[i-2]) % 15746
print(dp[n])
