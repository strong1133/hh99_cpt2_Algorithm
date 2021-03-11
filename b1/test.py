def solution(numbers):
    res = 0
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            res = numbers[i]+numbers[j]
            answer.append(res)
    answer = set(answer)
    return answer


nums = list(map(int, input().split()))
print(solution(nums))
