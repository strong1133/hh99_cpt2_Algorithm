c = int(input())

for i in range(c):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:]) / nums[0]
    for score in nums[1:]:
        if score > avg:
            rate = score/nums[0] * 100
    print('%.3f' % round(rate, 3))
