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
    # 초반작업 3번 계단까지 수동으로 올라가주는 이유는
    dp.append(max(stairs[0]+stairs[2], stairs[1]+stairs[2]))
    # for문안에서는 n-3번 째 계단 까지 고려해줄것인데.. 3번까지 안올라가있으면 인덱스오류가 난다..
    for i in range(3, r):
        dp.append(max(dp[i-2]+stairs[i], dp[i-3] +
                      stairs[i]+stairs[i-1]))  # 둘중에 최댓값
        # 계단의 중간 부터 시작 하면 3->1->n 의 경우와 2-> n 가 있다.
    return dp.pop()


print(up())
#
#
#                     ___
#                  __|n
#               __|n-1
#            __|n-2
#         __|n-3
#      __|😀
#     😀가 n위로 올라가려면  3->1->n // 2-> n가 가능하다.
#
#
