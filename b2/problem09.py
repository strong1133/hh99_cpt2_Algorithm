# 항해99_알고리즘_2021-03-13, 백준번호: 1932_정수삼각형../by 정석진
import sys
read = sys.stdin.readline

h = int(read())

arr = [list(map(int, read().split())) for _ in range(0, h)]

for i in range(1, h):
    for j in range(len(arr[i])):
        if j == 0:
            arr[i][j] += arr[i-1][j]  # arr[i-1][j] ⬆︎ 한칸
        elif j == i:
            arr[i][j] += arr[i-1][j-1]  # arr[i-1][j] ⬆︎ 한칸 ⬅︎ 한칸
        else:
            # 만약 대각선 방향 아래가 양쪽에 있다면 둘중에 최댓값을 찾아 +연산
            arr[i][j] += max(arr[i-1][j], arr[i-1][j-1])
print(max(arr[h-1]))  # 위 로직을 통하면 삼각형의 마지막 줄엔 각 덧셈 값들이 들어있게 된다 최댓값을 찾아주면 정답
