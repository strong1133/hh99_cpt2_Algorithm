# 항해99_알고리즘_2021-03-10, 백준번호: 2606_바이러스../by 정석진

from sys import stdin
read = stdin.readline

dic = {}
for i in range(int(read())):
    dic[i+1] = set()

for j in range(int(read())):
    a, b = map(int, read().split())
    dic[a].add(b)
    dic[b].add(a)


# bfs
def bfs(start, dic):
    queue = [start]
    while queue:
        for i in dic[queue.pop()]:
            if i not in visited:
                visited.append(i)
                queue.append(i)


# dfs
def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)


visited = []
# bfs(1, dic)
dfs(1, dic)
print(len(visited)-1)
