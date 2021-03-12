# 항해99_알고리즘_2021-03-12, 백준번호: 4948_베트트랑 공준/by 정석진  -> 에라토네스체 확인
import math


def prime(num):  # 소수를 만드는 함수
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):  # 1은 소수가 아니고 제곱근이 1이라면 모든게 0으로 떨어지 때문에 제곱근 +1
        if num % i == 0:  # 나누어 떨어지는것은 소수가 아니다.
            return False

    return True


# 1은 소수가 아니고 123,456 은 문제에서 정해준 n의 범위인데 n*2 까지니까  123,456 * 2 = 246912
li = list(range(2, 246912))
arr = []
for i in li:
    if prime(i):  # false 반환되는 숫자는 if를 통과못하고 ture만 통과해서 arr에 append된다.
        arr.append(i)  # 문제에서 허용한 범위를 모두 소수로 만들어두고


while(1):  # 무한루프
    ans = 0
    n = int(input())
    if n == 0:
        break  # 문제에서 무한루프를 마쳐줄 값으로 0을 지정
    for i in arr:  # 소수가 전부 담겨 있는 리스트에서 소수를 하나씩 꺼내옴
        if 1 < 2 <= 2:  # 만약 n으로 입력 받은 값 사이에 소수가 있을때마다 ans += 1
            ans += 1  # ex) n=1 => 1< 2 <=2
            # arr=[2,3,4,7,11....]
    print(ans)
