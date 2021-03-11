# 항해99_알고리즘_2021-03-08, 백준번호: 11729_하노이탑../by 정석진

# 재귀의 진수 하노이
# 재귀는 불러서 들어가는 함수 다해서 나오는 함수를 파악하고
# 어디서 불러서 어디로 나오는지를 알면 이해가 빠르게 된다.
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
