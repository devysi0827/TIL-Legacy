import sys
sys.stdin = open("sample_input.txt","r")

#함수
def all_plus(list_1,n):
    list_2=[]
    for i in list_1:
        list_2.append(i+n)

    return list_2

#본문<-------------------->
case_num = int(input())  #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 이차원 배열 형성
    iron = list(input())

    # 레이저를 구분한 쇠막대기 만들기
    new_list =[0]  #인데스에러 방지용 더미데이터
    for i in  range(len(iron)-1):
        if iron[i] =='(' and iron[i+1] == ')':
            new_list.append('r')
        elif iron[i] ==')' and iron[i+1] == '(':
            pass
        else:
            new_list.append(iron[i])
    new_list.remove(0) # 인덱스 더미데이터 제거 ['r', '(', '(', '(', 'r', 'r', ')', '(', 'r', ')', 'r', ')', ')', '(', 'r', ')']

    answer = 0
    r_count = 0
    now =[]
    for i in range(len(new_list)):
        if new_list[i] == '(':
            now.append(i)
        elif new_list[i] ==')':
            r = i-now[-1]-1
            answer += r+1
            del now[-1]
            now = all_plus(now, 2)

    print('#{} {}'.format(case + 1, answer))


        # if new_list[i] == ')': #닫는 괄호가 나오면 레이저의 개수를 세자
        #     j = -1
        #     r_count = 1 #안잘리면 1
        #     while 1:
        #         if stack[j] =='(':  #여는 괄호가 나올때까지 실행한다
        #             break
        #         else:
        #             r_count +=1  #그외 다른 것이라면 추가한다
        #             j -= 1
        #     answer += r_count   #정답에 짤린 개수를 더한다
        #     del stack[j]  #만난 괄호를 삭제한다.
        #
        # else:
        #     stack.append(new_list[i])  #그외에는 스택에 더한다






