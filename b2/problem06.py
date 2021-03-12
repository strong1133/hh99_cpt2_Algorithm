# 항해99_알고리즘_2021-03-12, 백준번호: 1436_영화감독 숌../by 정석진

n = int(input())

name = 666
cnt = 0
while(1):
    if "666" in str(name):  # 문자열 "666"이 있는지 확인해줌
        cnt += 1
        if cnt == n:
            print(name)
            break
    name += 1

# n = 1 -> cnt = 1 -> if true -> print(666)
# n = 2 -> cnt = 1 -> 667 -> 666이 더이상 name안에 없기 때문에 다음 666등장까지 계속 반복문 수행
# 다음 666은 1666이라
#
#
#
#
