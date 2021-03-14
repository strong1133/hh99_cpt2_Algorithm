# 항해99_알고리즘_2021-03-14 백준번호: 11399_ATM../by 정석진


N = int(input())
nums = list(map(int, input().split()))

if N == 1:  # 1
    print(nums[0])
else:
    nums.sort()  # 2

    i_sum = 0
    min_sum = 0

    for i in range(N):
        min_sum += (i_sum + nums[i])  # 3
        i_sum += nums[i]  # 4

    print(min_sum)
