import sys
sys.stdin = open("input.txt","r")

#함수

#본문<-------------------->
case_num = 10 #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    n, number = input().split( )
    number = list(number)
    stack = []
    for i in range(len(number)):
        stack.append(number[i])
        if len(stack) >=2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()

    str_stack = ''
    for i in stack:
        str_stack+=str(i)

    print("#{} {}".format(case + 1,str_stack))
