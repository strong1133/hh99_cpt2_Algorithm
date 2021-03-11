# 항해99_알고리즘_2021-03-10, 백준번호: 2606_바이러스../by 정석진

from sys import stdin
read = stdin.readline  # input()보다 빠른 stdin.readline 사용의 간소화를 위한 변수처리

dic = {}  # 컴퓨터 번호들을 담아줄 딕셔너리
for i in range(int(read())):  # 총 컴퓨터 대수만큼 반복
    dic[i+1] = set()  # 0번 컴퓨터는 있을수 없으므로 딕셔너리 안에 컴퓨터 번호별 배열을 담아줄때 각 +1

for j in range(int(read())):  # 네트워크에 연결된 쌍의 수 입력 해당 수만큼 반복문 수행
    a, b = map(int, read().split())  # 각각 연결된 컴퓨터 번호를 입력받음
    dic[a].add(b)  # 2,3
    dic[b].add(a)
    print(dic)
    # 만약 1-2 이렇게 연결 되어 있다면 1번 컴퓨터의 연결목록엔 2번이 있고 당연히 2번 컴퓨터 연결 목록에도 1번이 있어여함
    # 즉 연결은 상호연결이므로 서로에게 서로를 add

# 해당 문제는 일종의 트리? 가 구성되기 때문에 bfs와 dfs모두 적용이 가능하다.


# bfs
def bfs(start, dic):
    queue = [start]  # 바이러스 전파 시작 컴퓨터 부터 큐에 담는다.
    while queue:  # 큐가 비어진것은 바이러스 전파할 컴퓨터가 없다는것이니 while종료

        # 큐에서 꺼내온 dic[]에서 인덱스로 활용 ex){1:{2}, 2: {1,3} } 이라면 큐에서 나온값이 1일때 dic에서 연결된 2를 가져올수 있다
        for i in dic[queue.pop()]:  # i=2
            if i not in visited:  # 꺼내온 컴퓨터 넘버가 visited라는 배열안에 없다면 감염이 안된것이기 때문에
                visited.append(i)  # visited에 남김으로써 방문했었다는 표시와 감염을 시킴
                queue.append(i)  # 이후 새롭게 확산된 컴퓨터에서 감염을 뻗어 나가기 위해 큐에 넣어준다


# dfs
def dfs(start, dic):
    for i in dic[start]:  # 감염출발지 컴퓨터 번호를 받아서 dic[]에서 인덱스번호로 활용
        if i not in visited:  # visited에 없으면 감염되지 않은 것이니
            visited.append(i)  # visited에 감염시켰음을 남겨줌
            dfs(i, dic)  # 새롭게 확산을 위해 재귀함수로 새로운 감염출발 컴퓨터 번호를 넣어줌


visited = []  # 함수 호출전 감염여부및 방문여부를 남겨줄 배열 초기화
# bfs(1, dic)
dfs(1, dic)  # 감염출발지 번호와 컴퓨터 번호 및 연결 정보를 담고있는 dic를 파라미터로 넘겨줌
print(len(visited)-1)  # 최초 출발지는 빼야함
