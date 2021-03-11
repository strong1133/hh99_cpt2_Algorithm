# 항해99_알고리즘_2021-03-05, 백준번호: 4673_셀프넘버../by 정석진

# set 방식
numbers = set(range(1, 10000))
remove_set = set()

# 10 -> 10 +1, 10 +0
for num in numbers:
    for n in str(num):  # 숫자를 한자리 씩 분리해서 더해줘야 하기 때문에 str처리 만약 10이면 '1','0'
        num += int(n)   # 이와 같이 처리하는 이유는 자리수마다 더해야 하기 때문
    remove_set.add(num)

# 차집합 연산을 통해 셀프숫자가아닌 값들을 numbers에서 빼줘 self_numbers에 따로 담아준다
self_numbers = numbers - remove_set

for self_number in sorted(self_numbers):
    print(self_number)


# 리스트 방식
numbers = list(range(1, 10_001))
remove_list = []
for num in numbers:
    for n in str(num):
        num += int(n)
    if num <= 10_000:
        remove_list.append(num)
for remove_num in set(remove_list):
    numbers.remove(remove_num)
for self_num in numbers:
    print(self_num)
