import sys
sys.stdin = open("2.txt","r")

#함수

#본문<-------------------->
case_num = int(input())  #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    n = int(input())
    input_list = list(input().split( ))
    list_1 = []
    list_2 = []

    for i in range(n):
        if i<=(n-1)//2:
            list_1.append(input_list[i])
        else:
            list_2.append(input_list[i])

    ans =[]
    for i in range(n):
        if i%2 ==0:
            ans.append(list_1[i//2])
        else:
            ans.append(list_2[i//2])
    print("#{} ".format(case + 1), end ='')
    print(*ans)