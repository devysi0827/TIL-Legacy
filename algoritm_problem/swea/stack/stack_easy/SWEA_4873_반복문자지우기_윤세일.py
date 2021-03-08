import sys
sys.stdin = open("sample_input.txt","r")

#함수

#본문<-------------------->
case_num = int(input())  #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    sententce = input()
    stack = []

    for i in range(len(sententce)):
        stack.append(sententce[i])
        if len(stack) >=2 and stack[len(stack)-1] ==stack [len(stack)-2]:
            stack.pop()
            stack.pop()


    print("#{} {}".format(case+1,len(stack)))