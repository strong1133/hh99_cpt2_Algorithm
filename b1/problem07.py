# 항해99_알고리즘_2021-03-06, 백준번호: 1157_단어공부../by 정석진

words = input().upper()
unique = list(set(words))
cnt_list = []
for i in unique:
    cnt = words.count(i)
    cnt_list.append(cnt)
    print(unique)
    print(cnt_list)

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))
    print(max_index)
    print(unique[max_index])
