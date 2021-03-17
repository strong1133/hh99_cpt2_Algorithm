# 항해99_알고리즘_2021-03-17, 백준번호: 2667_단지번호 정하기../by 정석진
# 동적계획법 넘무 어렵다..

r = int(input())


# dfs방식
def dfs(arr, cnt, x, y):
    arr[x][y] = 0  # 재귀로 인해 함수진행

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]  # 상하좌우 탐색용

    for i in range(4):  # 이동할 방향이 상하좌우 라서 4번 반복
        nx = x+dx[i]
        ny = y+dy[i]  # 상하좌우 이동하기 위해서 각 좌표에 dx,dy를 더해줌

        if nx >= 0 and nx < r and ny >= 0 and ny < r:  # nx, ny가 n*n의 배열범위를 벗어나지 않도록 조치
            if arr[nx][ny] == 1:  # 마찬가지로 찾은 부분에 1이 있으면
                cnt = dfs(arr, cnt+1, nx, ny)  # 다시 재귀를 해서 그 주위로 탐색
    return cnt


arr = [list(map(int, list(input()))) for _ in range(r)]  # n*n 배열안에 값들을 넣어줌
ans = []  # 답을 담아줄 리스트

for i in range(r):
    for j in range(r):
        if arr[i][j] == 1:  # 처음에 좌표를 순회하다가 1을
            ans.append(dfs(arr, 1, i, j))  #

print(len(ans))
for i in sorted(ans):  # 출력조건에 오름차순이 있음
    print(i)
