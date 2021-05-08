#입력
import sys
sys.stdin = open("sample_input (3).txt","r")
case_num = int(input())  #최초반복횟수

#본문
for case in range(case_num):
    n = int(input())
    n_list - list(map(int,input().split( )))
    # 왼쪽 오른쪽 양끝 설정
    a_left = start
    a_right = total_page
    b_left = start
    b_right = total_page
    #반복문 종료 체크용
    check = False

    while check ==False:
        a= (a_left+a_right)//2
        if a < a_page:
            a_left =a
        elif a == a_page:
            answer ='a'
            check = True
        else:
            a_right = a

        b = (b_left + b_right) // 2
        if b < b_page:
            b_left = b
        elif b == b_page:
            answer = 'b'
            if check == True:
                answer = '0'
            check = True
        else:
            b_right = b
    print(answer)