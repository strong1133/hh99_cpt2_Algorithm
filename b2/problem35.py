# 항해99_알고리즘_2021-03-17, 백준번호: 1753_최단경로../by 정석진
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())

K = int(input())
dp = [INF]*(V+1)
heap = []
arr = [[] for _ in range(V+1)]
# print(dp)


def djk(start):
    dp[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        tup, now = heapq.heappop(heap)
        if dp[now] < tup:
            continue

        for w, next in arr[now]:
            next_tup = w+tup
            if next_tup < dp[next]:
                dp[next] = next_tup
                heapq.heappush(heap, (next_tup, next))


for _ in range(E):
    u, v, w = map(int, input().split())
    arr[u].append((w, v))

djk(K)
for i in range(1, V+1):
    print("INF" if dp[i] == INF else dp[i])
