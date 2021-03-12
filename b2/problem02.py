# 항해99_알고리즘_2021-03-12, 백준번호: 2839_설탕배달/by 정석진

ans = 0
su = int(input())
while su >= 0:
    if su % 5 == 0:
        ans += (su // 5)
        print(ans)
        break
    su -= 3
    ans += 1
else:
    print(-1)
