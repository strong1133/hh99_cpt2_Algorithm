n, m, v = map(int, input().split())
# 정점이 n개일 때, n*n크기의 이차원 배열을 생성한다.
a = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    # x와y가 연결되어있음을 의미함. 방향은 무의미하므로 반대도 성립
    a[x][y] = a[y][x] = 1


def dfs(start_node, visited_node):
    # 모든 노드를 돌아다니면서 한 노드 다 팔 때 까지
    # stack에 시작노드를 입력하고
    # visited node에 시작노드를 입력하면서 pop
    # visited하지않은 노드 다 방문
    stack = [start_node]
    while stack:
        current_node = stack.pop()
        visited_node = current_node
        for i in range(len(a[start_node])):
            print(a[start_node][i])
            if a[start_node][i] == 1 and i not in visited_node:
                stack.append(i)
    return visited_node


print(dfs(v, []))
