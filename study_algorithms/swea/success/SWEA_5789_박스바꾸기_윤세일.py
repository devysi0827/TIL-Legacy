import sys
sys.stdin = open("sample_input (1).txt","r")

#함수
def make_it(box,left,right,n):

    for i in range(left-1,right):
        box[i] = n

    return box

#본문<-------------------->
case_num = int(input())  #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    n, num = map(int,input().split( ))
    box = [0]*n
    for i in range(num):
        left, right = map(int,input().split( ))
        box = make_it(box, left, right, i+1)

    print("#{} ".format(case+1),end='')
    print(*box)