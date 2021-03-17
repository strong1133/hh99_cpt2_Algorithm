# 항해99_알고리즘_2021-03-16 백준번호: 2798_블랙잭../by 정석진

r, m = map(int, input().split())
cards = list(map(int, input().split()))

res = 0
length = len(cards)  # 카드를 뽑아와서 더하는 행위 자체도 카드의 장수 만큼 반복되어져야 함으로

for i in range(0, length):  # a+b+c 에서 a
    for j in range(i + 1, length):  # a+b+c 에서 b
        for k in range(j + 1, length):  # a+b+c 에서 c
            s = cards[i] + cards[j]+cards[k]  # a+b+c
            if s <= m:  # 합산이 목표한 m보다 작거나 같아야함.
                res = max(res, s)  # 최대한 가꺼운 값을 찾아 줘야 하고
                # 한번 돌때 구해진 s가 res에 쌓이고 다음 반복부터는 더 큰값을 찾아 저장하게 됨

print(res)
