from sys import stdin
read = stdin.readline
for _ in range(int(read())):
    N, M = map(int, read().split())
    num_n = 1
    num_m = 1
    num_d = 1
    for i in range(1, N+1):
        num_n *= i
    for j in range(1, M+1):
        num_m *= j
    for x in range(1, M-N+1):
        num_d *= x
    res = (num_m//num_n)//num_d
    print(res)
