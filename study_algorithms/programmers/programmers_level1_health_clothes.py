# def solution(n, lost, reserve):
#
#     lost_num = len(lost)
#     answer = n - lost_num
#
#     #본인이 잃어버렸다면,
#     overlap = []
#     for i in lost:
#         if i in reserve:
#             overlap.append(i)
#     new_lost = []
#     new_reserve = []
#
#     if overlap:
#         answer += len(overlap)
#         for i in lost:
#             if i not in overlap:
#                 new_lost.append(i)
#         for i in reserve:
#             if i not in overlap:
#                 new_reserve.append(i)
#     else:
#         new_lost =lost
#         new_reserve =reserve
#
#     #타인을 빌려주자
#     minus =[]
#     plus = []
#
#     for i in new_reserve:
#         if i-1 in new_lost:
#             minus.append(i-1)
#         elif i+1 in new_lost:
#             plus.append(i+1)
#
#     for i in minus:
#         if i not in plus:
#             plus.append(i)
#     answer += len(plus)
#
#     return answer


def solution(n, lost, reserve):

    lost_num = len(lost)
    answer = n - lost_num

    #본인이 잃어버렸다면,
    overlap = []
    for i in lost:
        if i in reserve:
            overlap.append(i)
    new_lost = []
    new_reserve = []

    if overlap:
        answer += len(overlap)
        for i in lost:
            if i not in overlap:
                new_lost.append(i)
        for i in reserve:
            if i not in overlap:
                new_reserve.append(i)
    else:
        new_lost =lost
        new_reserve =reserve

    #타인을 빌려주자


    for i in range(len(new_lost)):
        for i in range(len(new_lost)):
            for j in range(len(new_reserve)):
                if new_reserve[j] == new_lost[i] - 1:
                    new_reserve[j] = -1
                    new_lost[i] = -1
                    answer += 1

        for j in range(len(new_reserve)):
            if new_reserve[j] == new_lost[i]+1:
                new_reserve[j] = -1
                new_lost[i] = -1
                answer +=1

    return answer

# 순환 순서에 따른 오류 발생
# https://programmers.co.kr/questions/9706

n= 5
lost=[1,3]
reserve=[2,4]
#5
print(solution(n, lost, reserve))



