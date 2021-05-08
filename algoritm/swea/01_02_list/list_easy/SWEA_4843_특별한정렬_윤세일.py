#입력
import sys
sys.stdin = open("sample_input (3).txt","r")
case_num = int(input())  #최초반복횟수

#본문
for case in range(case_num):
    n = int(input())
    n_list = list(map(int,input().split( )))

    for i in range(n):
        for j in range(n):
            if i != j and n_list[j]>=n_list[i]:
                n_list[j], n_list[i] = n_list[i], n_list[j]

    if n%2 == 0:
        middle =int(n//2)
        answer = []
        for i in range(middle):
            answer.append(n_list[-i-1])
            answer.append(n_list[i])

    if n%2 == 1:
        middle = int(n // 2)
        answer = []
        for i in range(middle):
            answer.append(n_list[-i-1])
            answer.append(n_list[i])
        answer.append(n_list[middle+1])

    if n >10:
        answer = answer[0:10]

    print("#{} ".format(case+1), end="")
    print(*answer)