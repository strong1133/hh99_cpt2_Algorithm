# 항해99_알고리즘_2021-03-17, 백준번호: 11866_요세푸스문제../by 정석진
# 해당 문제는 사실 기능 구현보다 출력 형식 맞추는게 더어려운 문제
from collections import deque

n, k = map(int, input().split())
dq = deque(i for i in range(1, n+1))
res = []
for i in range(n):
    for i in range(k-1):
        temp = dq.popleft()
        dq.append(temp)  # 사실 rotate()를 써서 회전 시켜줘도 됨
    res.append(dq.popleft())
print("<" + ", ".join(list(map(str, res)))+">")
