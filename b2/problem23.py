# 항해99_알고리즘_2021-03-15 백준번호: 2630_색종이../by 정석진
# 분할정복에 대한 이해가 필요하다.
# 해당 문제에 대한 코드 분석은 TIL에 기록했다.
# https://github.com/strong1133/TIL/blob/main/Algorithm/%EB%B6%84%ED%95%A0%EC%8B%AC%ED%99%94(%EC%83%89%EC%A2%85%EC%9D%B4%EB%AC%B8%EC%A0%9C)_(21-03-16).md

from sys import stdin
input = stdin.readline

n = int(input())
colorpaper = [list(map(int, input().split())) for _ in range(n)]
# n*m의 직사각형 배열

white = 0  # 하얀색 갯수를 담아줄 변수
blue = 0  # 파란색 갯수를 담아줄 변수


def cutting(x, y, n):
    global blue, white
    check = colorpaper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != colorpaper[i][j]:  # 하나라도 같은 색이 아닐경우
                cutting(x, y, n//2)  # 1사분면
                cutting(x, y+n//2, n//2)  # 2사분면
                cutting(x+n//2, y, n//2)  # 3사분면
                cutting(x+n//2, y+n//2, n//2)  # 4사분면
                return
    if check == 0:
        white += 1
        return
    else:
        blue += 1
        return


cutting(0, 0, n)
print(white)
print(blue)
