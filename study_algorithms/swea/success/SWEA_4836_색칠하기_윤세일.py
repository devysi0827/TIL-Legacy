#  입력
import sys
sys.stdin = open("sample_input (3).txt","r")
case_num = int(input())  #최초반복횟수


for case in range(case_num):
    # 기본 설정
    num = int(input()) #주어진 박스의 수
    box = []
    for i in range(10):  #0배열 만들기
        box.append([0]*10)

    for i in range(num):
        input_box = list(map(int,input().split( )))  #색칠리스트 받기
        for j in range(input_box[0],input_box[2]+1):
            for k in range(input_box[1],input_box[3]+1):
                if box[j][k] == 0 or box[j][k] == input_box[4]:  #빈칸 또는 같은 색은 칠하기
                    box[j][k] = input_box[4]
                else:  #다른 색은 +
                    box[j][k] += input_box[4]

    # 3인 수 찾기
    ans = 0
    for i in range(10):
        for j in range(10):
            if box[i][j] ==3:
                ans +=1
    print("#{} {}".format(case+1,ans))
