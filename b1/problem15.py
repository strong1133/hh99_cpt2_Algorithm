# 항해99_알고리즘_2021-03-09, 백준번호: 4949_균형잡힌 세상/by 정석진

import sys
input = sys.stdin.readline

while 1:  # 참일때 반복
    string = input().rstrip()  # 입력받는 값의 오른쪽 공백을 없애준다.
    stack = []  # 스택을 만들어주고
    flag = 1  # yes, no를 판별해줄 변수 선언
    for str in string:  # 입력받은 문자열에서 문자들을 str이라는 이름으로 하나씩 받아서 반복문
        if str == '(' or str == '[':  # 받아온 값이 열린 괄호들이면 스택에 다 넣어준다.
            stack.append(str)
        elif str == ')':  # 받아온 값에서 닫힘 괄호를 만났다면
            # 직전에 넣은 괄호가(직전이니 스택의 맨위)동일종류의 열린괄호인지 확인
            if stack and stack[-1] == '(':
                stack.pop()  # 맞으면 둘은 짝이 맞으니 열린괄호를 스택에서 제거 -> 닫힌괄호는 등장후 비교만 해줬지 스택에 들어간적이 없음
            else:
                flag = 0  # 아니라면 짝이 맞지 않으니 flag를 0으로 만들어준다.
                break
        elif str == ']':  # 위와 마찬가지
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = 0
                break
    if string == '.':  # '.'를 만나면 break를 통해 반복문 종료
        break

    print("yes" if flag and not(stack) else "no")
    # 1이면 참 0이면 거짓.. 만약 flag가 참이고 =1 and not(stack)_ 스택이 비어 있으면 'yes'출력
    # 둘중에 하나라도 거짓이면 no -> 조건을 두개 걸어준 이유는 마지막에 짝이 안맞아 스택이 비어버렸어도 no가 나와야 하기때문
