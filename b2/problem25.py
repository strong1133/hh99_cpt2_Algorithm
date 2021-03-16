# 항해99_알고리즘_2021-03-15 백준번호: 9663_N-Queen../by 정석진
from sys import stdin
input = stdin.readline

r = int(input())  # r*r의 체스판위의 r개의 퀸 갯수


def dfs(arr):  # 퀸
    global ans
    length = len(arr)  # 현재까지 퀸이 놓여진 위치 //length=2라면 두번째까지 놓였다는 말
    if length == r:
        ans += 1
        return
    # 후보가 될 수 있는 자리를 0를 부터 n-1 까지 만들고 이후에 arr[]과 비교해서 겹치면 후보에서 제거
    candidate = list(range(r))
    for i in range(length):
        if arr[i] in candidate:
            candidate.remove(arr[i])  # 같은 줄에 있으면 제외
        distance = length - i
        if arr[i]+distance in candidate:
            candidate.remove(arr[i]+distance)  # 대각선 제외 ⬋
        if arr[i]-distance in candidate:  # 대각선 제외 ➘
            candidate.remove(arr[i]-distance)
    if candidate:  # 아직 후보가 남아있다는 말은 겹치지 않는 후보가 있다는 말
        for i in candidate:  # 하나씩 꺼내서
            arr.append(i)  # 겹치지 않는 후보에서부터도 새롭게 출발해줘야함 -> 후보지에 퀸을 착수함을 의미
            dfs(arr)  # 새롭게 내려놓은 퀸에서부터 재귀함수 출발
            arr.pop()  # 새롭게 내려놓은 퀸에서 출발한 재귀함수가 종료되면 다음코드인 여기로 옴
            # arr.pop의 의미는 해당 칸에 퀸을 내려놓고 파생되는 경의수는 다봤으니 arr에서 제거하고 for문을 반복해 다른 경의 수도 확인 -> 백트래킹
    else:  # 후보가 비었다면 함수를 종료
        return  # 만약 후보가 비었고 최상위 함수(재귀를 최초에 부른 함수)라면 모든 함수를 마치고 37번 라인으로 간다.


ans = 0
for i in range(r):
    dfs([i])
print(ans)  # dfs() 에서 ans값을 가지고 나오는것이 아닌 dfs에서 ans+=1 로 변경되어 있는 값을 읽어오는 것
# ans가 global로 되어있기에 가능
#
#  깃허브 TIL 정리 글
#  https://github.com/strong1133/TIL/blob/main/Algorithm/%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9%20%EC%8B%AC%ED%99%94(N-Queen)_(21-03-16)%20copy.md
#
#  - n=4일때 경우의 수는 2이다.
#  - 노드의 깊이가 n과 같아질 때 성공한것으로 간주할 수 있다.
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
