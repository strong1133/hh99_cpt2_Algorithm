# 항해99_알고리즘_2021-03-08, 백준번호: 11729_하노이탑../by 정석진


def hanoi(n, s, e, o):
    if n == 1:
        print(s, e)
        return
    hanoi(n-1, s, o, e)
    print(s, e)
    hanoi(n-1, o, e, s)


n = int(input())
print((2**n) - 1)

hanoi(n, 1, 3, 2)
