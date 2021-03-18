# 2019년 상반기 LINE 인턴 채용 코딩테스트

from collections import deque

c = 10
b = 1


def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))
    visited = [{} for _ in range(200001)]

    while cony_loc < 200000:
        cony_loc += time
        if time in visited[cony_loc]:
            return time

        for i in range(0, len(queue)):
            cur_position, cur_time = queue.popleft()
            new_time = cur_time + 1

            new_position = cur_position - 1
            if new_position >= 0 and new_position <= 200000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = cur_position + 1
            if new_position >= 0 and new_position <= 200000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = cur_position * 2
            if new_position >= 0 and new_position <= 200000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

        time += 1


print(catch_me(c, b))  # 5가 나와야 합니다!
