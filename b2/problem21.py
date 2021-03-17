# 항해99_알고리즘_2021-03-15 백준번호: 1260_DFS와 BFS../by 정석진

r, link, s = map(int, input().split())

dic = [[] for i in range(r+1)]


for i in range(link):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

for i in range(r):
    dic[i].sort()  # 문제 조건에서 작은 번호를 먼저 방문하라는 말이 있어서 정렬을 해줘야힘


# bfs
def bfs(start, dic):
    queue = [start]
    visited = [start]
    while queue:
        for i in dic[queue.pop(0)]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
    return visited


# dfs
def dfs(start, dic):
    visited.append(start)
    for i in dic[start]:
        if i not in visited:
            dfs(i, dic)
    return visited


visited = []
print(*dfs(s, dic))
print(*bfs(s, dic))  # 프린트 한줄로 하기
