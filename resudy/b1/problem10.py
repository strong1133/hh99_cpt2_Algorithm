t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    rn = n//h + 1
    f = n % h
    if f == 0:
        rn -= 1
        f = h
    print(f*100 + rn)
