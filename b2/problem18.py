# 항해99_알고리즘_2021-03-15 백준번호: 10773_제로../by 정석진


r = int(input())
stack = []
for _ in range(r):
    x = int(input())
    if x == 0:
        stack.pop(-1)  # 스택의 맨위 가장 최근 값 스택은 LIFO 구조이기 때문에 .pop() 로 해도 가능.
        # print(stack)
    else:
        stack.append(x)
        # print(stack)

print(sum(stack))
