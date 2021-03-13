# 항해99_알고리즘_2021-03-13, 백준번호: 1149_RGB거리_/by 정석진

r = int(input())
arr = []
for i in range(r):
    arr.append(list(map(int, input().split())))

for i in range(1, len(arr)):
    # r 선택 -> r선택후 파랑초록 둘중 작은값을 구해서 더해준다.
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
    # g 선택 -> 이전 값들 중에서 최솟값 (빨강 ,파랑)
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]
    # b 선택 -> 이전 값들 중에서 최솟값 (빨강, 초록)
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2]

# for문을 통해 저장된 값들중 최솟값
print(min(arr[r-1][0], arr[r-1][1], arr[r-1][2]))


# print(a//(r*2)+10)
