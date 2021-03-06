a = 'hello my name is sparta'
a = a.replace(" ", "")
print(a)
unique = list(set(a))
cnt_list = []
for x in unique:
    cnt = a.count(x)
    cnt_list.append(cnt)

max_index = cnt_list.index(max(cnt_list))

print(unique[max_index])
