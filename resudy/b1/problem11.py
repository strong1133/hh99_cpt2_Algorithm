import math


def makesosu(num):
    if num == 1:
        return False
    n = int(math.sqrt(num))
    for i in range(2, n+1):
        if num % i == 0:
            return False
    return True


a, b = map(int, input().split())
for v in range(a, b+1):
    if makesosu(v):
        print(v)
