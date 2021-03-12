# 항해99_알고리즘_2021-03-12, 백준번호: 1316_그룹단어체커../by 정석진

r = int(input())  # 작업을 몇번 해줄것인지 설정
ans = 0  # 답이 몇개인지 담아줄 변수 초기화
for i in range(r):
    string = input()  # 문자열을 입력받고
    res = True  # 그룹단어인지 확인할 확인자 생성 초기값은 그룹단어라고 생각해주기위해 True
    for j in range(len(string)-1):  # 왼쪽문자에서 오른쪽문자를 비교해줄것인데 인덱스참조를 오버플로 하지 않기위한 조치
        if string[j] != string[j+1]:  # 위에서 범위를 이미 +1해도 인덱스 최댓값을 넘지못하게 해줬기 때문에 별탈없이 +1가능
            newstr = string[j+1:]  # 왼쪽 오른쪽 비교했더니 다르다면 오른쪽에 있는 문자를 싹 긁어서 새로저장
            if newstr.count(string[j]) > 0:
                res = False  # 그룹문자가 아니면 확인자에게 아니라고 말해주는 역활
                break
            # 그렇게 긁어온 문자들중에서 현재 왼쪽(기준이 되었던)문자가 옆에 말고 더 뒤쪽엔 있는지 카운팅
            # ex) asdas -> a에서 볼때 s는 다르니까 sdas를 긁어서 sdas중에 a가 있다면 그룹문자가 아닌것임
    if res:  # True, False를 판단해서 True면 그룹문자이기때문에 갯수에 +1
        ans += 1
print(ans)
