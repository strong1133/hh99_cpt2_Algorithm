# 항해99_알고리즘_2021-03-12, **시험1_2** 백준번호:2164 _카드2 /by 정석진

import collections  # deque

r = int(input())  # 몇장의 카드가 있는지 r=7
cards = collections.deque([i for i in range(1, r+1)])  # 1,2,3,4,5,6,7

while len(cards) != 1:  # 카드가 한장일때는 끝낸다
    cards.popleft()  # 1,3,5
    cards.rotate(-1)  # 2,4

print(cards[0])

#cards = [4]

#
# r=7
# 1,3,5,2,6
# ===========deque============
#
#
#
# ===========deque============
#
#
