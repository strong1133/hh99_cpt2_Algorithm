# 항해99_알고리즘_2021-03-09, 백준번호: 1874 스택수열../by 정석진

from sys import stdin

n = int(stdin.readline())
li = []

for _ in range(n):
    li.append(int(stdin.readline()))


def numbering():
    cnt, stack, result = 1, [], []
    for i in li:
        while cnt <= i:
            stack.append(cnt)
            result.append('+')
            cnt += 1
        if stack.pop() != i:
            return 'No'
        else:
            result.append('-')
    return '\n'.join(result)


print(numbering())
