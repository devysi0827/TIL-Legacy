import sys
sys.stdin = open("input.txt","r")

#함수

#본문<-------------------->
case_num = 10 #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    n = int(input())
    galhos = input()
    stack = []

    ans = 1

    for i in range(len(galhos)):
        j = len(stack)
        if galhos[i] == '(' or galhos[i] =='[' or galhos[i] =='{' or galhos[i] =='<':
            stack.append(galhos[i])
        elif galhos[i] == ')':
            while 1:
                j -= 1
                if stack[j] == '(':
                    stack.pop(j)
                    break
                if j == 0:
                    ans = 0
                    break
        elif galhos[i] == ']':
            while 1:
                j -= 1
                if stack[j] == '[':
                    stack.pop(j)
                    break
                if j == 0:
                    ans = 0
                    break
        elif galhos[i] == '}':
            while 1:
                j -= 1
                if stack[j] == '{':
                    stack.pop(j)
                    break
                if j == 0:
                    ans = 0
                    break
        elif galhos[i] == '>':
            while 1:
                j -= 1
                if stack[j] == '<':
                    stack.pop(j)
                    break
                if j == 0:
                    ans = 0
                    break

    print("#{} {}".format(case+1, ans))


    # print("#{} {}".format(case+1,answer))