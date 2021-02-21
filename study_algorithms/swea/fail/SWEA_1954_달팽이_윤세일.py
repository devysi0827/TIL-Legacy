import sys
sys.stdin = open("input.txt","r")

#함수



#본문<-------------------->
case_num = int(input())  #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    n = int(input())
    box= [[0]*n for _ in range(n)]
    row = 0
    col = -1
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    check = 0

    for i in range(1,n**2+1):
        temp_row = row + dr[check]
        temp_col = col + dc[check]

        if temp_row >= n or temp_row<0 or temp_col>=n or temp_col<0 or box[temp_row][temp_col] != 0:
            check = (check + 1) % 4

        row = row + dr[check]
        col = col + dc[check]
        box[row][col] = i
    print('#{} '.format(case + 1))
    for i in range(n):
        print(*box[i])










    # print("#{} {}".format(case+1,answer))