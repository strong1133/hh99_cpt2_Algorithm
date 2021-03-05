# 항해99_알고리즘_2021-03-05, 백준번호: 1110_더하기사이클 /by 정석진

num = int(input())

if num < 10:
    num *= 10

origin = num  # num은 newnum을 저장해서 반복문을 수행해야함 때문에 원래 값을 기억해줄 변수 선언
count = 0  # 로직이 몇번 돌았는지 카운팅 해 줄 변수 초기화
newnum = 0  # 변화된 값을 만들어주고 num에게 전달해줄 중간역활 변수 선언

while True:
    # 만약 26 이라면 2와 6을 분리 해서 2 + 6 을 해야함.
    temp = (num // 10) + (num % 10)

    # 원래 숫자의 일의 자리 숫자와 더해서 나온 더하기 값의 일의 자리 숫자를 합쳐 줘야함.
    newnum = ((num % 10)*10) + (temp % 10)

    # 그렇게 만들어진 새로운 숫자를 다시 쪼개서 temp에 주는 로직을 처리하기 위해 num에 넣어줌
    num = newnum
    count += 1  # 반복문이 한번 돌았으니 카운팅 +1
    if newnum == origin:  # 수행 결과가 원래 값이랑 일치한지 검사
        break  # 일치 하면 while을 부수고 탈출
print(count)
