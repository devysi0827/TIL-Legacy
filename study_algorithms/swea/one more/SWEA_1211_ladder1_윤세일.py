#입력
import sys
sys.stdin = open("2.txt","r")
case_num = 10  #최초반복횟수

#함수
def find_two(box,n):
    for i in range(100):
        if box[n][i] ==2:
            return i

#본문
for case in range(case_num):
    #인풋
    trash = input()
    box = []
    for i in range(100):
        temp = list(map(int,input().split( )))
        box.append(temp)

    #좌표함수
    dx =[1,-1,0,0]
    dy =[0,0,1,-1]

    #2찾기
    my_x = find_two(box,99)  # print(location) 57
    my_y = 99

    for i in range(99):
        my_x += dx[3]
        my_y += dy[3]
        if my_x == 99:
            while box[my_y][my_x-1] ==1:
                my_x += dx[1]
                if my_x == 0:
                    break
            continue

        if my_x == 0:
            while box[my_y][my_x-1] ==1:
                my_x += dx[1]
                if my_x == 0:
                    break
            continue

        if box[my_y][my_x+1] ==1:
            while box[my_y][my_x+1] ==1:
                my_x += dx[0]
                if my_x == 99:
                    break
        elif box[my_y][my_x-1] ==1:
            while box[my_y][my_x-1] ==1:
                my_x += dx[1]
                if my_x == 0:
                    break

    print("#{} {}".format(case+1,my_x))






