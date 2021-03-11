# 항해99_알고리즘_2021-03-09, 백준번호: 4949_균형잡힌 세상/by 정석진

import sys
input = sys.stdin.readline

while 1:
    string = input().rstrip()
    stack = []
    flag = 1
    for str in string:
        if str == '(' or str == '[':
            stack.append(str)
        elif str == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = 0
                break
        elif str == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = 0
                break
    if string == '.':
        break

    print("yes" if flag and not(stack) else "no")
