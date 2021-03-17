# 항해99_알고리즘_2021-03-17, 백준번호: 1992_쿼드트리../by 정석진
# 해당 문제는 색종이와 거의 같은 문제 이 문제를 잘 풀지 못하겠다면 색종이에 대한 이해를 잡고오는걸 추천
# https://github.com/strong1133/TIL/blob/main/Algorithm/%EB%B6%84%ED%95%A0%EC%8B%AC%ED%99%94(%EC%83%89%EC%A2%85%EC%9D%B4%EB%AC%B8%EC%A0%9C)_(21-03-16).md
# 색종이와 해당 문제의 차이는 -> 주의할점 입력예시를 보면 공백이 없다. 즉 split()로 나누지 못한다는것.
# 리스트에 입력값을 넣고보면 split() 없이 한 결과를 꼭 출력 해보자 의도했던바와 달라야 정상이며
# 형변환의 팔요를 캐치해야한다. -> 나아가 input()과 readline()의 차이를 알게될수도 있다.
n = int(input())
tree = []
for _ in range(n):
    tree.append(list(map(int, str(input()))))
# print(tree)


def cutting(x, y, n):
    global ans
    flag = False
    check = tree[x][y]
    for i in range(x, x+n):
        if flag:
            break
        for j in range(y, y+n):
            if check != tree[i][j]:
                ans += '('
                cutting(x, y, n//2)
                cutting(x, y+n//2, n//2)
                cutting(x+n//2, y, n//2)
                cutting(x+n//2, y+n//2, n//2)
                ans += ')'
                flag = True
                break
    if not flag:
        if tree[x][y] == 1:
            ans += '1'
        else:
            ans += '0'


ans = ''
cutting(0, 0, n)
print(ans)
