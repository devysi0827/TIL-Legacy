def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i < j:
                answer.append(numbers[i] + numbers[j])
    answer = set(answer)
    answer = list(answer)

    for i in range(len(answer)):
        for j in range(i,len(answer)):
            if answer[i] > answer[j]:
                answer[i], answer[j] = answer[j], answer[i]

    return answer
numbers =[2,1,3,4,1]
answer = solution(numbers)
print(answer)