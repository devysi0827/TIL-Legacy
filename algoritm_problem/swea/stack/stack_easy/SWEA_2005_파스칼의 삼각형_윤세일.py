import sys
sys.stdin = open("sample_input.txt","r")

#함수

#본문<-------------------->
case_num = int(input())  #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    n = int(input())
    box = [[1],[1,1]]
    for i in range(2,n):
        temp = [1]
        for j in range(0,i-1):
            tem = box[i-1][j] +box[i-1][j+1]
            temp.append(tem)
        temp.append(1)
        box.append(temp)
    print('#{}'.format(case+1))
    for i in range(n):
        print(*box[i])





    # print("#{} {}".format(case+1,ans))







    # print("#{} {}".format(case+1,answer))
