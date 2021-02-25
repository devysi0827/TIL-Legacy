import sys
sys.stdin = open("sample_input.txt","r")

#함수

#본문<-------------------->
case_num = int(input())  #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    galho = ['{','}','(',')']
    stack = []
    check = 0
    sentence = list(input())

    for i in range(len(sentence)):
        for j in range(len(galho)):
            if sentence[i] == galho[j]:
                if len(stack) == 0 and j%2 ==1:
                    check = 1
                stack.append(j)

                if len(stack)>=2 and  stack[-1] -1 == stack[-2] and stack[-2]%2 == 0 :
                    stack.pop()
                    stack.pop()

    if check == 1:
        print("#{} {}".format(case+1,0))
        continue

    if len(stack) == 0:
        print("#{} {}".format(case + 1, 1))
    else:
        print("#{} {}".format(case + 1, 0))




    # print("#{} {}".format(case+1,ans))