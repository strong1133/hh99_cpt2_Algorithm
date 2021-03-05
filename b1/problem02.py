# 항해99_알고리즘_2021-03-05, 백준번호:2588 _곱셈 /by 정석진

print('첫번째 값을 입력하세요')
ipt1 = int(input())
print('두번째 값을 입력하세요')
ipt2 = int(input())
# map으로 받지 않는 이유는 문제에서 두번 받으라고 요구함.

opt1 = ipt1 * ((ipt2 % 100) % 10)  # 나머지 구하기로 1의자리 숫자 추출
opt2 = ipt1 * ((ipt2 % 100) // 10)  # 나머지와 몫으로 10의 자리 추출
opt3 = ipt1 * (ipt2 // 100)  # 몫으로 100의 자리 추출

result = ipt1 * ipt2  # 최종 결과 값 저장

print(opt1, opt2, opt3, result)
