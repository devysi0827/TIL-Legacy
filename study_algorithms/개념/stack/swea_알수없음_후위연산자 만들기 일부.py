import sys
sys.stdin = open("3.txt","r")

#함수

#본문<-------------------->
case_num = 10  #최초반복횟수
token_numbers ={'+':1, '*':2 ,'(':0}  #token 식셔너리

for case in range(case_num):
    # 기본 인풋 및 설정
    trash = input()
    senentce =list(input())
    senentce.append(')')
    senentce.insert(0,'(')
    stack = []
    ans = []

    #후위 연산자로 변경<----------------------->
    for i in range(len(senentce)):
        # 숫자를 만난다면,
        if ord(senentce[i]) >=48 and ord(senentce[i])<=57:  #숫자판별
            ans.append(senentce[i])  #숫자가 아닌 수를 만난다면 그 수를 ans에 추가한다.

        # +를 만난다면
        elif senentce[i] == '+':
            token_num = 1

            # stack이 비어있다면, 추가하고 끝낸다
            while 1:
                if len(stack) == 0:
                    break

                #토큰 넘버 구하기
                top = stack[-1]
                top_num = token_numbers[top]

                # 연산자 우선순위 비교
                if token_num > top_num:  # 새로 추가되는 연산자보다 우선순위가 더 높다면 그냥 추가한다.
                    break
                else:  # 같거나 작다면 그녀석을 뺀다.
                    temp = stack.pop()
                    ans.append(temp)
            stack.append(senentce[i])


         # *를 만난다면
        elif senentce[i] == '*':
            token_num = 2

            # stack이 비어있다면, 추가하고 끝난다.
            while 1:
                if len(stack) == 0:
                    break

                # 토큰 넘버 구하기
                top = stack[-1]
                top_num = token_numbers[top]

                # 연산자 우선순위 비교
                if token_num > top_num:  # 새로 추가되는 연산자 우선순위가 더 높다면 그냥 추가한다.
                    break
                else:  # 같거나 작다면 그녀석을 뺀다.
                    temp = stack.pop()
                    ans.append(temp)
            stack.append(senentce[i])

        #<남는 문자 처리----------->
        # 여는 괄호를 만나면 무조건 추가한다.
        elif senentce[i] == '(':
            stack.append(senentce[i])

        # 닫는 괄호를 만난다면 여는 괄호를 만날때까지 모두 반환한다.
        elif senentce[i] == ')':
            while 1:
                if stack[-1] == '(':
                    stack.pop()
                    break
                else:
                    temp = stack.pop()
                    ans.append(temp)


    for i in range(len(ans)):
        if ord(ans[i]) >= 48 and ord(ans[i]) <= 57:  # 숫자판별
            stack.append(ans[i])  # 숫자가 아닌 수를 만난다면 그 수를 ans에 추가한다.

        elif ans[i] == '+':
            one = int(stack.pop())
            two = int(stack.pop())
            stack.append(one+two)

        elif ans[i] == '*':
            one = int(stack.pop())
            two = int(stack.pop())
            stack.append(one*two)

    print("#{} {}".format(case+1, stack[0]))
    print(stack)

