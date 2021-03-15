# 항해99_알고리즘_2021-03-15 백준번호: 1010_다리놓기../by 정석진

def f(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num


r = int(input())
for _ in range(r):
    n, m = map(int, input().split())
    res = f(m) // (f(n) * f(m-n))
    print(res)

# m개의 지역에 n개의 다리를 놓기위한 경의 수는 mCn이다.
# mCn = m! // (n! * (m-n)!)
