# 항해99_알고리즘_2021-03-17, 백준번호: 11054_가장 긴 바이토닉../by 정석진
# 오름차순의 경우와 내림차순의 경우를 합해준 최댓값을 찾아주면됨

r = int(input())
arr = list(map(int, input().split()))
reverse = arr[::-1]  # arr를 역순으로 reverse에 저장

p = [1 for i in range(r)]  # 오름차순의 길이를 담아줄 리스트
m = [1 for i in range(r)]  # 내림차순의 길이를 담아줄 리스트

for i in range(r):
    for j in range(i):
        if arr[i] > arr[j]:
            p[i] = max(p[i], p[j]+1)  # 오름차순
        if reverse[i] > reverse[j]:
            m[i] = max(m[i], m[j]+1)  # 내림차순

res = [0 for i in range(r)]
for i in range(r):
    res[i] = p[i] + m[r-i-1] - 1  # 오름차순과 내림차순길이의 합
    # 내림차순은 p를 기준으로 역순이기 때문에 같은 숫자에 대한 길이를 매칭 시키려면 뒤애서부터 찾아와야함.
    # -1을 해주는 이유는 오름차순, 내림차순의 합을 각각 구하면서 중복이 한번 발생하기 때문
print(max(res))
