# 항해99_알고리즘_2021-03-12, 백준번호: 1011_Fly me to the Alpha Centauri/by 정석진

import math

r = int(input())
res = []
for _ in range(r):
    x, y = map(int, input().split())  # 거리 구하기
    num = y-x  # 필요거리
    if num <= 3:  # 거리 3까지는 1의 속도로 똑같이 가면된다.
        res.append(num)
    else:
        distance = int(math.sqrt(num))  # 거리에 대한 제곱근을 구해서 저장
        if num == distance**2:  # 거리가 n^2일때
            res.append(2*distance-1)
        elif distance**2 < num <= distance**2 + distance:  # 거리가 n^2 이후 부터 n^2+n이하 일때
            res.append(2*distance)
        else:  # 거리 그 외
            res.append(2*distance+1)

for i in res:
    print(i)
    #
    #
    #  거리  ||   이동   ||  횟수
    # --------------------------
    #  1    ||     1   ||  1    ** n은 제곱근 (제곱근은 int이기때문에 소수점을 버린다. 4=>2  5=>2 ... 8=>2  9=>3 )
    #  2    ||    11   ||  2
    #  3    ||   111   ||  3    ->  n<=3 일때까지는
    #  4    ||   121   ||  3    ->  n^2일때  2*(n제곱근) -1 만큼 이동
    #  5    ||  1211   ||  4    ->  n^2 이후 부터 n^2+n이하는 2n => 2(2) =4
    #  6    ||  1221   ||  4    -> 6 역시 제곱근이 2이므로 => 2(2) = 4
    #  7    || 12211   ||  5    ->  n^2+n 보다 7이 크다 때문에 2*n+1 = 5
    #           .
    #           .
    #  9    ||  12321 ||  5    -> 이때 9는 n^2의 거리이기때문에  2n -1
    #
    # 여기서 팁은 거리가 멀수록 횟수가 증가하는게 아니라
    # 제곱근이 취할수 있는 값 기준으로 구해지는 방식에 따라 횟수 공식이 바뀌는것이다
    # 거리가 n^2 일때 이동횟수는 2n -1
    # 거리가 n^2+n 이하는 이동횟수는 2n
    # 그 이후거리로는 이동횟수는 2*n+1
    # 거리구하는 방식은 3가지 이기 때문에 조건 2개 걸고 나머지 하나는 else처리
    #
    #
    #
