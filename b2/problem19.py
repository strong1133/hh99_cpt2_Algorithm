# 항해99_알고리즘_2021-03-15 백준번호: 9012_괄호../by 정석진


r = int(input())
result = []
for _ in range(r):
    stack = []
    flag = True
    string = input().rstrip()
    for str in string:
        if str == '(':
            stack.append(str)
            # print(stack)
        elif str == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = False  # 균형 여부를 판단 해주는 변수
                break

    # 스택이 비었는지 같이 검새 해주는 이유는 '(((('로만 들어갔을때 flag = True이 기본값이며 균형을 판단할 조건자체가 성립되지 않았어서
    # 스택이 무조건 비었는지 같이 봐줘야 한다.
    if flag and not(stack):

        result.append('YES')
    else:
        result.append('NO')

for i in result:
    print(i)

# 해당 문제는 '4949_균형잡힌 세상' 와 상당히 유사하다.
