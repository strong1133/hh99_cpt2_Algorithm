# 항해99_알고리즘_2021-03-06, 백준번호: 1157_단어공부../by 정석진

words = input().upper()  # 대소문자 구분을 위해서 통일해줌
unique = list(set(words))  # 중복 배제 - 중복을 빼서 리스트로 만들어준다.
cnt_list = []  # 문자를 세준 갯수를 담아줄 리스트 선언
for i in unique:  # 중복 배제 리스트에서 하나씩 꺼내준다 ex) [a,s,d]
    cnt = words.count(i)  # words에서 꺼내온 i 를 카운팅 해준다.
    cnt_list.append(cnt)  # 세준 개수를 넣어줌
    # 이때 unique= [a,s,d]
    #  cnt_list= [2,n,n] 이런식으로 unique에서 꺼내온 순서대로 카운팅해서 넣어주기때문에
    # unique와 cnt_list의 인덱스값은 동일해진다 ex)unique의 [0]은 a, cnt_list[0] =2 => a의 갯수는 2
    print(unique)
    print(cnt_list)

if cnt_list.count(max(cnt_list)) > 1:  # cnt_list에 저장된 값들중 최대값이 복수개면 ?반환
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))
    print(max_index)
    print(unique[max_index])
    # 위에서 말한것처럼 cnt_list의 최대값이 위치해있는 인덱스값을 unique에 넣으면 해당 문자를 찾을수 있다
