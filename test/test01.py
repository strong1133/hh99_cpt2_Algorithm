# 항해99_알고리즘_2021-03-12, **시험1_1** 백준번호:10815 _숫자카드 /by 정석진
a = int(input())
sanguen = list(map(int, input().split()))

r = int(input())
cards = list(map(int, input().split()))
sanguen = set(sanguen)


for i in cards:
    if i not in sanguen:
        print(0, end=' ')
    else:
        print(1, end=' ')
