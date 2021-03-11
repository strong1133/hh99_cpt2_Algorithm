# 항해99_알고리즘_2021-03-10, 백준번호: 7576_토마토../by 정석진
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]  # x,y를 상하좌우로 한칸씩 움직이게 하기위한 사전작업
#     ↑  ↓  →   ←

w, h = map(int, input().split())  # 넓이와 높이를 입력받음
maps = [list(map(int, input().split()))
        for _ in range(h)]  # 높이만큼의 반복문을 돌면서 []를 반복적으로 입력받음

q = deque()  # deque사용을 위해 q변수 선언

# 전체에서 이미 익은 과일(1) 을 찾아서 deque에 넣어주는 역활
for i in range(h):  # 높이만큼
    for j in range(w):  # 높이만큼 넓이 만큼
        if maps[i][j] == 1:
            q.append([i, j])


# 하루가 지날때마다 익은 토마토 전파를 위한 함수
def bfs():
    global q
    while q:  # deque가 빌때까지
        x, y = q.popleft()  # 왼쪽에서부터 꺼내온다 입력예제 첫번째 값을 넣었다면 (3,5)가 나와서 x=3, y=5

        for i in range(4):  # 우리가 움직여줄 방향은 상하좌우 4방향

            # 입력하고 나서의 x값을 저장할 nx를 선언하고 값 저장 ex) 3 + dx[0] => 3 + (-1) = 2
            nx = x + dx[i]
            # y값을 저장할 ny를 선언하고 값 저장 ex) 5 + dy[0] => 5 + 0 = 5
            ny = y + dy[i]

            # 구해진 이동 좌표가 최소, 최대 높이, 넓이를 이탈했는지 확인 및 익지 않은 토마토가 들어있는지 확인
            if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] == 0:
                # deque말고 토마토상자(maps)에서 토마토를 바꿔준다  ex) maps[2][5] = maps[3][5] +1
                # 이때 maps[3][5]는 이미 숫자 1이 있기때문에 +1 해줘서 maps[2][5] 에는 2가 저장됨 => 이말은 하루가 지났음을 나타내준다.
                maps[nx][ny] = maps[x][y] + 1
                # 그렇게해서 이동한 좌표에도 토마토가 익었을 테니까 다음 전파를 위해서 deque에 저장해줌
                q.append([nx, ny])


# 모든 로직이 끝나고 나서 안익은 토마토가 있는지 다 익었다면 몇일이나 걸렸는지 확인해주는 함수
def go():
    ans = 0  # 변수 초기화
    for i in range(h):  # 높이만큼
        for j in range(w):  # 높이만큼 넓이만큼
            a = maps[i][j]  # 0,0 부터 높이, 넓이만큼 값을 찾아서 a에 넣어줌
            if a == 0:  # 이때 로직이 끝났음에도 0이 들어있다면 전부 익지 않은것이기때문에 -1 출력후 함수 종료
                print(-1)
                return
            ans = max(ans, a)  # 그게 아니라면 다익었다는 것이니까 ans, a에서 최대값을 해준다.
    print(ans - 1)
    # 위 토마토 전파 함수에서 전파된 토마토들을 다 1로 만들어준게 아닌 경과 날짜 표현을 위해 +1 씩 하면서 저장을 해줬기 때문에
    # 8일차 맨마지막에 전파된 토마토 자리에는 1이아닌 9가 들어있을것이고 9가 들어있는 이유는 최초 0이 아닌 1 부터 시작 했기 때문


bfs()
go()
