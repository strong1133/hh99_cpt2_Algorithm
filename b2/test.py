import sys
num = int(sys.stdin.readline())
num_list = list(x for x in range(1, num + 1))
stack = []
# print(num_list)
answer = []
error = False
for _ in range(num):
    target = int(sys.stdin.readline())
    # target 이 num_list 에 없다면 "NO"
    if error:
        continue
    # stack 이 비어있을 땐 무조건 append!
    if len(stack) == 0:
        for i in range(target):
            stack.append(num_list[0])
            num_list.pop(0)
            answer.append("+")
        continue
    # stack 의 맨 위가 target 과 같거나 클 때
    if stack[-1] >= target:
        while stack[-1] >= target:
            stack.pop()
            answer.append("-")
            if len(stack) == 0:
                break
        continue
    # stack 의 맨 위가 target 보다 작을 때
    if stack[-1] < target:
        # 이때 target 이 num_list 에 없다면!?
        if target not in num_list:
            error = True
            continue
        while stack[-1] != target:
            stack.append(num_list.pop(0))
            answer.append("+")
        # stack 의 마지막과 target 이 같아졌으면,
        # target 에 해당하는 stack 을 pop 시켜준다.
        stack.pop()
        answer.append("-")
if error != True:
    print(*answer, sep='\n')
else:
    print("NO")
