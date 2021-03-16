# 항해99_알고리즘_2021-03-15 백준번호: 2798_블랙잭../by 정석진

r, m = map(int, input().split())
cards = list(map(int, input().split()))

res = 0
length = len(cards)

for i in range(0, length):
    for j in range(i + 1, length):
        for k in range(j + 1, length):
            s = cards[i] + cards[j]+cards[k]
            if s <= m:
                res = max(res, s)

print(res)
