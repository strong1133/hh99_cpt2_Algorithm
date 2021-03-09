import math
tree_num, need_high = map(int, input().split())
now_high = 0
result = 0
tree_list = list(map(int, input().split()))
tree_list.sort(reverse=True)
for count in range(tree_num):
    if tree_num == 1:
        result = need_high
        break
    now_high = tree_list[count] - tree_list[count+1]
    need_high = need_high - now_high * (count + 1)
    if need_high == 0:
        result = result + now_high
        break
    elif need_high > 0:
        result = result + now_high
    else:
        need_high = need_high + now_high * (count + 1)
        result = result + math.ceil(need_high/(count+1))
        break

if tree_num == 1 and tree_list[0] < result:
    print(0)
else:
    print(tree_list[0] - (result))
