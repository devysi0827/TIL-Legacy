import sys
sys.stdin = open("sample_input (8).txt","r")

#함수

#본문<-------------------->
case_num = int(input())  #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    n= int(input())
    box = []
    for i in range(n):
        n, m =list(map(int,input().split( )))
        n = n-n//2
        m = m-m//2
        box.append([n, m])
    print(box)
    room = [0]*201
    for i in range(len(box)):
        start = box[i][0]
        end = box[i][1]
        print(start, end)
        if start <= end:
            for j in range(start,end+1):
                room[j] +=1
        else :
            for j in range(end,start+1):
                room[j] +=1

    print(room)
    maxi = 0
    for i in room:
        if maxi < i:
            maxi = i

    print("#{} {}".format(case + 1, maxi))