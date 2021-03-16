n = int(input())
for i in range(n):
    m = list(input())
    sum = 0  # 여는 괄호는 +1 닫는 괄호는 -1 = 0이면 yes, 그 외 no
    for i in m:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum != 0:
        print('NO')
    else:
        print('YES')
