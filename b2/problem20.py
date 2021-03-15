# 항해99_알고리즘_2021-03-15 백준번호: 18258_큐2../by 정석진
import sys
from collections import deque
input = sys.stdin.readline
# 해당 문제는 스택처럼 구현할경우 기능구현은 가능하지만 시간초과가 뜬다.
# sys.stdin.readline과 from collections import deque를 통해 시간복잡도를 줄여줘야 하는것이 키포인트


def push(x):
    queue.append(x)


def pop():
    if not(queue):
        return -1
    else:
        return(queue.popleft())


def size():
    return len(queue)


def empty():
    return 0 if queue else 1


def front():
    return queue[0] if queue else -1


def back():
    return queue[-1] if queue else -1


queue = deque()
r = int(input())
for _ in range(r):
    input_str = input().rstrip().split()
    order = input_str[0]
    if order == 'push':
        push(input_str[1])
    elif order == 'pop':
        print(pop())
    elif order == 'size':
        print(size())
    elif order == 'empty':
        print(empty())
    elif order == 'front':
        print(front())
    elif order == 'back':
        print(back())
