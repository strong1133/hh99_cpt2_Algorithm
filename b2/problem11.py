# 항해99_알고리즘_2021-03-14 백준번호: 11399_ATM../by 정석진

N = int(input())
nums = list(map(int, input().split()))

if N == 1:
    print(nums[0])
else:
    # 사람이 2명 이상인 경우, 돈을 인출하는 데 가장 적은 시간이 드는 순서로 정렬한다. 그래야 누적되는 시간이 줄어든다.
    nums.sort()

    i_sum = 0
    min_sum = 0

    for i in range(N):
        min_sum += (i_sum + nums[i])
        # i_sum에는 이전 사람들이 돈을 인출하는 데 걸렸던 시간을 포함한다.
        # nums[i]는 현재 사람이 돈을 인출하는 데 걸리는 시간이다.
        # 이 둘을 더하면 한 사람이 돈을 인출하는 데 걸리는 전체 시간을 구할 수 있다. 그리고 이를 min_sum에 더한다.

        i_sum += + nums[i]
        # i_sum에 현재 사람이 인출하는 데 걸리는 시간을 더해, 다음 사람 순서의 #3에 반영할 수 있도록 한다.

    print(min_sum)
