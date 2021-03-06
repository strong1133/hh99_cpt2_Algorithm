words = input().upper()
unique = list(set(words))
print(unique)
cnt_List = []
for x in unique:
    cnt = words.count(x)
    cnt_List.append(cnt)
    print(cnt_List)

if cnt_List.count(max(cnt_List)) > 1:
    print('?')
else:
    max_index = cnt_List.index(max(cnt_List))
    print(unique[max_index])
