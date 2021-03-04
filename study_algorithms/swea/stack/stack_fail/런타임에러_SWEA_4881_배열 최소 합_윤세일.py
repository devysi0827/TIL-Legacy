import sys
sys.stdin = open("sample_input.txt","r")

#함수
def perm(idx):  #재귀 순열 생성 함수
    if idx == n:
        list_1.append(list(sel))  #만들어진 순열을 list_1에 저장한다.

    else:
        for i in range(n):
            if check[i] == 0:
                sel[idx] = arr[i]
                check[i] = 1
                perm(idx+1)
                check[i] = 0

#본문<-------------------->
case_num = int(input())  #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    n = int(input())
    box = []
    for i in range(n):
        temp = list(map(int,input().split( )))
        box.append(temp)

    # arr 및 기본 순열 함수 생성
    arr = []
    for i in range(n):
        arr.append(i)
    sel = [0] * n
    check = [0]* n
    list_1 = []
    perm(0)
    print(list_1)

    minimum = 99999
    for i in range(len(list_1)):
        sum_list = 0
        for j in range(n):
            sum_list += box[j][list_1[i][j]]
        if sum_list < minimum:
            minimum = sum_list
    print("#{} {}".format(case + 1, minimum))

