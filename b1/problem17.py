# 항해99_알고리즘_2021-03-09, 백준번호: 1021_회전하는_큐../by 정석진

r, n = map(int, input().split())  # 큐의 크기 r, 뽑고자 하는 갯수 n
targets = list(map(int, input().split()))  # 뽑아 내고자 하는 목표 숫자

queue = [i for i in range(1, r+1)]  # 큐에는 1부터 r+1까지 의 숫자가 차례 대로 담겨있음
ans = 0  # 변수 초기화

for target in targets:  # 뽑아 내고자 하는 목표 숫자의 배열에서 하나씩 가져와서 로직처리
    plus_index = queue.index(target)  # 먼저 오른쪽회전일지 왼쪽 회전할지를 골라줌
    minus_index = len(queue) - plus_index
    # 1등 부터 100등 사이에서 30등은  1등 부터 따지면 30등이지만 뒤에서부터는 70등이다.
    # 또 1~10 중 8은 앞에서부턴 8번째지만 뒤에서 부턴 3번째다
    # 이걸 이용해서 오른쪽에서 가까우면 오른쪽으로 돌리고 왼쪽에서 가까우면 왼쪽으로 돌린다.

    steps = min(plus_index, minus_index)  # 둘중에 작은것을 steps에 담아둔다.
    if steps == plus_index:  # steps에서 저장된 값이 plus면 plus로 마킹
        s = 'plus'
    else:
        s = 'minus'  # steps에서 저장된 값이 minus면 minus로 마킹

    if s == 'plus':  # 마킹을 검사해서 다음 로직 수행
        for _ in range(steps):  # plus에서 steps이 3이면 이는 곳 3번째에 있다는 의미이기때문에
            temp = queue.pop(0)  # 큐에서 그전 까지 꺼내주면 된다.
            queue.append(temp)
            # 큐애서 꺼내준 값을 temp에 담아 고대로 큐의 뒤쪽에 넣어준다. (왼쪽에서 오른쪽으로 가는 회전)

    else:  # plus가 아니면 minus
        # 큐는 pop가 한쪽에서만 되기때문에 뒤쪽에서 빼오게 되는값에는 타켓값을 포함해서 가져와야한다.
        for _ in range(steps):
            temp = queue.pop(-1)
            queue.insert(0, temp)
            # 그렇게 가져온걸 인서트를 통해 큐의 맨앞쪽에 넣어주면 queue[0] 이  타겟값이 된다. (오른쪽에서 완쪽으로 가는 회전)

    ans += steps  # ans에 작업량을 담아준다.
    queue.pop(0)  # 그렇게 찾은 타켓값이 맨위에 있으면 pop로 제거 해주고 다음 타켓으로 넘어간다.

print(ans)
