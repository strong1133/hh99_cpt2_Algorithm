# 항해99_알고리즘_2021-03-09, 백준번호: 1874 스택수열../by 정석진

from sys import stdin

n = int(stdin.readline())  # 총 수열의 길이
li = []  # 수열을 담아줄 배열

for _ in range(n):  # 수열의 길이만큼 수열에 넣어줄 값을 입력받음
    li.append(int(stdin.readline()))


def numbering():
    cnt, stack, result = 1, [], []  # 각 변수 선언
    for i in li:  # 만약 배열에 [3,4,5]가 있다면 첫번째 i는 3
        # 스택에 1부터 넣어야 함 (문제 지시 사항) 때문에 1부터 늘어나면서 넣어줄 값을 cnt로 선언하고 1로 초기화
        while cnt <= i:  # cnt가 목표값인 i보다 작을땐 스택에 1부터 계속 넣어 줘야 하기때문에 '+'
            stack.append(cnt)
            result.append('+')  # '+'를 이후에 출력을 위해 result배열에 담아줌
            cnt += 1  # cnt값의 증가를 위한 +1 작업
        # cnt값이 목표값을 넘으면 while종료
        if stack.pop() != i:
            return 'No'
            # 스택에서 꺼낼수 있는 맨위 값이 i로 받아올수 있는 값과 비교해서 일치 하는게 없으면 더이상 수행이 불가능해서 No출력
        else:
            result.append('-')
            # else로 온것 부터가 위의 필터들을 다 통과해서 온것이기 때문에  스택의 맨위의 값은 목표값과 같을수 밖에 없다.
            # 해서 stack.pop()과 동시에 스택에서 뺏으니 '-'를 담아준다.
    return '\n'.join(result)
    # 함수로 돌려받는 값을 출력해줄 것이기 때문에 리턴값이 해당 result들을 던저준다. '\n'=> 줄넘김


print(numbering())
