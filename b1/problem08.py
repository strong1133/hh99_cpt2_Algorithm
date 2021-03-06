# 항해99_알고리즘_2021-03-06, 백준번호: 2941_크로아티아 알파벳../by 정석진

a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
b = input()
for i in a:
    b = b.replace(i, 'a')
print(len(b))
