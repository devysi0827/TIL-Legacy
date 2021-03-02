import sys
sys.stdin = open("sample_input.txt","r")

#함수

#본문<-------------------->
case_num = int(input())  #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    input_list = list(input().split( ))
    pmmd = ['+','-','*','/']
    stack = []
    ans = []
    check = 0
    for i in range(len(input_list)):
        if input_list[i] == '.':
            if len(stack) == 0:
                check = 1
                break
            temp = stack.pop()
            ans.append(temp)

        elif input_list[i] in pmmd:
            if len(stack) < 2:
                check = 1
                break

            else :
                first = stack.pop()
                second = stack.pop()
                if input_list[i] == '+':
                    stack.append(first+second)
                elif input_list[i]  == '-':
                    stack.append(second-first)
                elif input_list[i]  == '*':
                    stack.append(first*second)
                elif input_list[i]  == '/':
                    stack.append(int(second/first))
        else:
            stack.append(int(input_list[i]))



    if check == 0:
        if len(stack) >= 2:
            check = 1
            print("#{} {}".format(case + 1, 'error'))
            continue
        print("#{} ".format(case+1), end ='')
        print(*ans)
    else:
        print("#{} {}".format(case + 1, 'error'))
