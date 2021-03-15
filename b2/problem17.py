# 항해99_알고리즘_2021-03-15 백준번호: 10828_스택../by 정석진
import sys
input = sys.stdin.readline


def push(x):
    stack.append(x)


def pop():
    if not(stack):
        return -1
    else:
        return(stack.pop())


def size():
    return len(stack)


def empty():
    return 0 if stack else 1


def top():
    return stack[-1] if stack else -1


r = int(input())  # 명령어 횟수
stack = []  # 스택 초기화

for _ in range(r):
    input_str = input().split()  # 명령을 입력받고 지문에서 보면 명령과 값은 띄어쓰기로 구분

    # 띄어쓰기로 구분했기 때문에 ex) push 1 은  [push, 1]로 인식된다. 0번째 값이 명령어
    order = input_str[0]

    if order == 'push':
        push(input_str[1])
    elif order == 'pop':
        print(pop())
    elif order == 'size':
        print(size())
    elif order == 'empty':
        print(empty())
    elif order == 'top':
        print(top())

# 해당 문제는 스택구현과 명령어를 input할때 split()을 통한 공백구분과 [0] 번째 값에대한 이해가 선행되어야 한다.
# 하지만 이문제의 키 포인트는 시간단축 -> 단순 input()을 쓰면 시간초과가 나오기때문에 sys.stdin.readline을 써야한다.
