import sys
sys.stdin = open("sample_input (3).txt","r")
case_num = int(input())  #최초반복횟수
#함수

#본문
for case in range(case_num):
    # 기본 인풋, 박스형성
    n, k =map(int,input().split( ))
    box = []
    for i in range(n):
        temp = list(map(int,input().split( )))
        box.append((temp))
    answer = 0

    for i in range(n):
        count = 0
        for j in range(n):
            if box[i][j]== 1:
                count +=1
            if box[i][j] == 0:
                if count == k:
                    answer +=1
                count = 0
        if count == k:
            answer +=1

    for i in range(n):
        count = 0
        for j in range(n):
            if box[j][i]== 1:
                count +=1
            if box[j][i] == 0:
                if count == k:
                    answer +=1
                count = 0
        if count == k:
            answer +=1
    print("#{} {}".format(case+1,answer))






