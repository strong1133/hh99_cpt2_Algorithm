# 항해99_알고리즘_2021-03-12, **시험1_2** 백준번호:2164 _카드2 /by 정석진

import collections

r = int(input())
cards = collections.deque([i for i in range(1, r+1)])  # 1,2,3,4,5,6,7

while len(cards) != 1:
    cards.popleft()
    cards.rotate(-1)

print(cards[0])

#
# r=7
#
# ===========deque============
#
#
#
# ===========deque============
#
#
