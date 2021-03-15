# 항해99_알고리즘_2021-03-15 백준번호: 2108_통계학../by 정석진
from sys import stdin
from collections import Counter

input = stdin.readline

r = int(input())
# 최솟값 출력 부분에서 2번째값을 가져오라는 부분을 대비하기 위해 정렬
arr = sorted([int(input()) for _ in range(r)])


def avg(arr):
    return round(sum(arr)/r)  # 문제에서 요구한 반올림


def mid(arr):
    if r == 1:
        return (arr[0])
    else:
        # n이 홀수 일땐 1,2,3,4,5,6,7,8 | 9 까지니까 가운데값 가능
        return (arr[r//2] if r % 2 != 0 else round((arr[r//2] + arr[r//2+1])/2))
        # 짝수일땐 가운데 두개의 값의 평균


def cnt(arr):
    cnt_list = Counter(arr)
    if r == 1:
        return arr[0]
    c = cnt_list.most_common(2)
    # 최빈값이 두개 이상이면 두번째 값(정렬을 했기 때문) 아니라면 첫번째 값
    return (c[1][0] if c[0][1] == c[1][1] else c[0][0])


def maxmin(arr):
    return(max(arr) - min(arr))


print(avg(arr))
print(mid(arr))
print(cnt(arr))
print(maxmin(arr))
