nums = set(range(1, 10000))
remove_set = set()

for num in nums:
    for n in str(num):
        num += int(n)
    remove_set.add(num)

self_set = nums - remove_set
for self_num in sorted(self_set):
    print(self_num)
