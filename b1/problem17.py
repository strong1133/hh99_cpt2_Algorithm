# 항해99_알고리즘_2021-03-09, 백준번호: 1021_회전하는_큐../by 정석진

r, n = map(int, input().split())
targets = list(map(int, input().split()))

queue = [i for i in range(1, r+1)]
ans = 0

for target in targets:
    plus_index = queue.index(target)
    minus_index = len(queue) - plus_index

    steps = min(plus_index, minus_index)

    if steps == plus_index:
        s = 'plus'
    else:
        s = 'minus'

    if s == 'plus':
        for _ in range(steps):
            temp = queue.pop(0)
            queue.append(temp)
    else:
        for _ in range(steps):
            temp = queue.pop(-1)
            queue.insert(0, temp)

    ans += steps
    queue.pop(0)

print(ans)
