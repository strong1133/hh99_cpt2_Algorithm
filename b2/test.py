import sys
n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))
dp = [0]*n  # n개의 0을 가진 list 생성
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
# print(dp)
a2 = a
a2.reverse()
dp2 = [0]*n  # n개의 0을 가진 list 생성
for i in range(n):
    for j in range(i):
        if a2[i] > a2[j] and dp2[i] < dp2[j]:
            dp2[i] = dp2[j]
    dp2[i] += 1
dp2.reverse()
# print(dp2)
final_dp = []
for i in range(n):
    if i == 0:
        final_dp.append(dp2[0])
    elif 0 < i < n-1:
        if dp[i] == dp[i+1]:
            final_dp.append(dp[i]-1+max(dp2[i+1:]))
        else:
            final_dp.append(dp[i]+max(dp2[i+1:]))
    elif i == n-1:
        final_dp.append(dp[i])
# print(final_dp)
print(max(final_dp))
