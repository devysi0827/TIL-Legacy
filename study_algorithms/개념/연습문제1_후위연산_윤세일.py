token_numbers ={'+':1, '-':1, '*':2, '/':2, '(':0}  #token 식셔너리
senentce =list('(6+5*(2-8)/2)')
stack = []
ans = []

for i in range(len(senentce)):
    # 숫자를 만난다면,
    if ord(senentce[i]) >=48 and ord(senentce[i])<=57:  #숫자판별
        j = i  #임시변수
        num = ''  #전체숫자 담기
        if i > 1:  #인덱스 에러방지
            if ord(senentce[i-1]) >= 48 and ord(senentce[i-1]) <= 57:  #전에가 숫자라면 이미 처리했으니 무시한다.
                continue
        while 1:
            if j >= len(senentce):  #인덱스 에러방지
                if num != '':  #빈 문자 가 아닌 숫자라면 추가한다
                    ans.append(num)
                break
            if ord(senentce[j]) >= 48 and ord(senentce[j])<=57:  #숫자라면 num에 문자형식으로 계속 추가한다.
                num += senentce[j]
                j = j + 1
            else:
                ans.append(num)  #숫자가 아닌 수를 만난다면 그 수를 ans에 추가한다.
                break


    # 여는 괄호를 만나면 무조건 추가한다.
    elif senentce[i] == '(':
        stack.append(senentce[i])

    # 닫는 괄호를 만난다면 여는 괄호를 만날때까지 모두 반환한다.
    elif senentce[i] == ')' :
        while 1:
            if stack[-1] == '(':
                stack.pop()
                break
            else:
                temp = stack.pop()
                ans.append(temp)

    # +,-를 만난다면
    elif senentce[i] == '+' or senentce[i] == '-':
        token_num = 1

        # stack이 비어있다면, 추가하고 끝낸다
        while 1:
            if len(stack) == 0:
                stack.append(senentce[i])
                break

            #토큰 넘버 구하기
            top = stack[-1]
            top_num = token_numbers[top]

            # 연산자 우선순위 비교
            if token_num > top_num:  # 새로 추가되는 연산자 우선순위가 더 높다면 그냥 추가한다.
                break
            else:  # 같거나 작다면 그녀석을 뺀다. 위에 if문을 만족할때까지 반복
                temp = stack.pop()
                ans.append(temp)
        stack.append(senentce[i])  #break가 걸리면 공통적으로 실행

    elif senentce[i] == '*' or senentce[i] == '/':
        token_num = 2

        # stack이 비어있다면, 추가하고 끝난다.
        while 1:
            if len(stack) == 0:
                stack.append(senentce[i])
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

print(ans)
