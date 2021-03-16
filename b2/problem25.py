# 항해99_알고리즘_2021-03-15 백준번호: 9663_N-Queen../by 정석진
from sys import stdin
input = stdin.readline

r = int(input())  # r*r의 체스판위의 r개의 퀸 갯수


def dfs(arr):
    global ans
    length = len(arr)
    if length == r:
        ans += 1
        return
    candicate = list(range(r))
    for arr[i] in candicate:
        candicate.remove(arr[i])
        distance = length - i
        if arr[i]+distance in candicate:
            candicate.remove(arr[i]+distance)
        if arr[i]-distance in candicate:
            candicate.remove(arr[i]-distance)
    if candicate:
        for i in candicate:
            arr.append(i)
            dfs(arr)
            arr.pop()
    else:
        return


ans = 0
for i in range(r):
    dfs([r])
print(ans)
#
#  깃허브 TIL 정리 글
#  https://github.com/strong1133/TIL/blob/main/Algorithm/%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9%20%EC%8B%AC%ED%99%94(N-Queen)_(21-03-16)%20copy.md
#
#  - n=4일때 경우의 수는 2이다.
#  - 노드의 깊이가 n과 같아질뗴 성공한것으로 간주할수 있다.
#  - 그렇다면 현재 놓여져 있는 퀸을 담을 변수 arr[]을 만들고
#  - 아래 줄 4칸에 해당하는 후보자들을 담아줄 candidate를 만들어준다
#  - candidate에서 값을 하나씩 꺼내와 arr[i] 에 해당하는것이 있는지 비교해주고 있으면 후보에서 제외 해준다.
#  - 해당 방법으로 수직, 대각선 방향에 있는 것들을 후보에서 제거해준다. -> `배제`
#  - 위 과정을 거치고도 candidate안에 있다면 그것은 기존의 퀸과 겹치지 않는 다는 뜻
#  - 새롭게 위치한 퀸에서부터 다음단계로 나아가야하니 현재 놓인 퀸의 값인 arr[]에 append
#  - 새로운 arr[]을 사용해서 재귀해주고
#  - 퀸이 다른 위치에 놓였을 때 경의수를 찾아주기 위해 arr.pop() 수행  -> `백트래킹`
#  - 퀸이 놓일수 있는 위치를 1층 부터 n층 까지 다찾았다면 깊이가 length == n 이된다.
#  - 따라서 length == n 일때 `현재 함수`를 return해주면 된다.
