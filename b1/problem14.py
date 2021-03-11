# 항해99_알고리즘_2021-03-09, 백준번호: 2805_나무자르기/by 정석진

# 2분 탐색은  시작값과 끝값을 2로 나눈 몫을 기준으로 크냐 작냐를 판단해 다음 이분 검색의 기준값들을 정해주는 검색 방식

from sys import stdin
from collections import Counter

n, m = map(int, stdin.readline().split())  # 나무의 총갯수 n과 최종 필요한 나무길이 m 입력
tree = Counter(map(int, stdin.readline().split()))
# 나무를 입력을 받는데 Counter를 통해서 세줌 (중복값이 있을 경우 7M 짜리 몇개 이런식으로)
# tree = 20 15 10 17
# Counter({20: 1, 15: 1, 10: 1, 17: 1}) 이런식으로

start, end = 0, max(tree.keys())
# 시작은 0부터 끝은 최댓값인데 카운터를 썻기때문에 최대 키값을 거져와야함 20 이 최대값
ans = 0

# 스타트가 엔드를 넘으면 이분검색이 성립되지 않으니 반복종료
while end >= start:
    mid = (start+end)//2  # 이분검색을 위한 중간값 계산
    s = 0  # 모은 나무길의 합계를 담아줄 변수
    for i in tree.keys():  # 키값을 가져옴 ex) for i in 20 => i=20
        if i > mid:  # ex) 현재 mid=10 , i가 더 크니
            s += (i-mid) * tree[i]
            # s에 값을 저장 // s = s + (20-10) *1 -> 여기서 tree[i]가 20이 아닌이유는 키값이 20이고 20:1 이기 때문이다.
            # s = 10 mid는 톱날의 높이이고 s는 자르고 모은 나무의 높이 이므로 s == m (목표값) 이 되어야함
            # counter를 사용한 이유는 시간 복잡도를 줄이기 위함 마지막에 '* tree[i]' 를 해줌으로써 중복되는 길이 나무가 있을시 이미 곱해서 구했기때문에
            # 반복문 한사이클을 아낄수 있게 된다.

    if s < m:  # s가 더 작으면 더 낮은 높이로 잘라 남는 부분을 많이 남겨야 하기때문에 end를 줄여준다.
        end -= 1
    elif s == m:  # 목표값이기때문에 끝내준다.
        ans = mid
        break
    else:  # 그외의 상황에서는
        ans = mid  # ans에 mid를 넣어놓고
        start += 1  # 시작을 늘려준다.

print(ans)
