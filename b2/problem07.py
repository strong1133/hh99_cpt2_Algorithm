# 항해99_알고리즘_2021-03-13, 백준번호: 9461_파도반 수열_/by 정석진

r = int(input())

arr = [1, 1, 1]

for i in range(r):
    x = int(input())
    for j in range(x):
        print(j)
        r = arr[j]+arr[j+1]
        arr.append(r)
        print(arr)
    res = arr[x-1]
    print(arr)
    print(res)
    arr = [1, 1, 1]  # 다음 입력에 대한 수열을 구하기 위해 arr초기화

    # arr에 초기값을 [1,1] 아닌 [1,1,1] 을 준 이유는
    # j=0일때   r = arr[j]+arr[j+1] 해서 구한값 => r = arr[0]+arr[1] => r= 1+1 =2
    # arr.append(r) 을 만나 arr에 맨뒤에 붙여주는데 이때 arr에 초기값이 [1,1] 이거 였다면
    # arr =[1,1,2] 가 되서 다음 반복인  j=1 이 들어오면 1+2=3이 되어버리기 때문에
    # [1,1,1] 을 줌으로써 arr인덱스 위치에 j가 한칸 늦게 증가토록 만들어줬다
    # 입력이 6일경우 j = 0,1,2,3,4,5
    # j= 0
    # [1, 1, 1, 2]
    # j= 1
    # [1, 1, 1, 2, 2]
    # j= 2
    # [1, 1, 1, 2, 2, 3]
    # j= 3
    # [1, 1, 1, 2, 2, 3, 4]
    # j= 4
    # [1, 1, 1, 2, 2, 3, 4, 5]
    # j= 5
    # [1, 1, 1, 2, 2, 3, 4, 5, 7] => j는 한칸늦게 arr에 append를 하기때문에
    #
    # j=5일때 arr[5] + arr[5+1] => 3+4 =7을 붙여준것
