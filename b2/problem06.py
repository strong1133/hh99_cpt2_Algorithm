# 항해99_알고리즘_2021-03-13, 백준번호: 9184_신나는 함수 실행_/by 정석진

max = 21
dp = [[[0] * max for _ in range(max)] for __ in range(max)]
# 입력해야 하는 입력값이 3개이기 때문에 3차원 배열로 생성
# dp에는 각 함수의 계산값들이 담긴다.


def W(a, b, c):  # a,b,c 를 파라미터로 받음
    if a <= 0 or b <= 0 or c <= 0:
        return 1  # 하나라도 0보다 작으면 1로 바뀜 음수 값 대처가능
    if a > 20 or b > 20 or c > 20:
        return W(20, 20, 20)

    # 값이 이미 존재 한다면 그 값으로 리턴
    if dp[a][b][c]:
        return dp[a][b][c]

    # a < b < c 인 경우
    if a < b < c:
        dp[a][b][c] = W(a, b, c-1) + W(a, b-1, c-1) - W(a, b-1, c)
        return dp[a][b][c]
    # a < b < c 그외의 경우
    dp[a][b][c] = W(a-1, b, c) + W(a-1, b-1, c) + \
        W(a-1, b, c-1) - W(a-1, b-1, c-1)
    return dp[a][b][c]


while(1):  # 무한루프 -> 특정조건으로 break
    a, b, c = map(int, input().split())  # 함수에 넣을 세가지 값을 입력받음
    if (a, b, c) == (-1, -1, -1):
        break  # -1 -1 -1 일때 실행종료
    print("w(%d, %d, %d) = %d" % (a, b, c, W(a, b, c)))
    # a,b,c,자리에는 a,b,c  =%d 자리에는  W(a, b, c)의 결과값을 넣어줌 => 이런 행위도 함수 호출
