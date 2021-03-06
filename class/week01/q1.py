a = [3, 5, 6, 1, 2, 4]

# print(max(a))


def find_max(array):
    for num in a:
        for compare_num in array:
            if num < compare_num:
                break
        else:
            return num


result = find_max(a)
print(result)
