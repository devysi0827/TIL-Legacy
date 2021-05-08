import sys
sys.stdin = open("sample_input(1).txt","r")

#함수
def check_not_same():  #현재 위치에서, 모든 방향에 대해서, 0이 아니면서, 나와 다른  수를 찾는다 x= -1< x <n, y= -1< y<n
    # vector = [[0,1], [0,-1], [1,0],[0,1],[1,1],[-1,-1],[1,-1],[-1,1]]
    check_list = []
    for i in range(len(vector)):
        temp_x = x + vector[i][0]
        temp_y = y + vector[i][1]

        if temp_x<n and temp_x>-1 and temp_y<n and temp_y>-1 and box[temp_x][temp_y] != 0 and box[temp_x][temp_y] != box[x][y]:
            check_list.append(vector[i])
    return check_list

def check_direction():
    check_list = check_not_same()
    check_list_2 = []
    breaks = box[x][y]  #현재값 저장, 나의 현재위치를 만나면 정지하자
    for i in range(len(check_list)):
        temp_x = x  #좌표초기화
        temp_y = y
        while 1:
            temp_x = temp_x + check_list[i][0]
            temp_y = temp_y + check_list[i][1]
            if temp_x<0 or temp_x>n-1 or temp_y<0 or temp_y>n-1:  #범위를 벗어난다면 그 방향은 반대쪽에 친구가 없다.
                break

            if box[temp_x][temp_y] == breaks:
                check_list_2.append(check_list[i])  #합격
                break
            elif box[temp_x][temp_y] == 0:  #만날 친구가 없네, 불합격
                break

    return check_list_2

def coloring():
    check_list_2 = check_direction()
    breaks = box[x][y]
    for i in range(len(check_list_2)):
        temp_x = x
        temp_y = y
        while 1:
            temp_x = temp_x + check_list_2[i][0]
            temp_y = temp_y + check_list_2[i][1]
            if box[temp_x][temp_y] == breaks:
                break
            else:
                box[temp_x][temp_y] = box[x][y]


#본문<-------------------->
case_num = int(input())  #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    n, m = map(int, input().split( ))
    box = [[0]*n for _ in range(n)]
    vector = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
    x = n//2
    y = n//2
    box[x][y]= 2
    box[x-1][y-1] = 2
    box[x-1][y] = 1
    box[x][y-1] = 1

    for i in range(m):
        x, y, p = map(int,input().split( ))
        x= x-1
        y= y-1
        box[x][y] = p
        coloring()

    count_1 = 0
    for i in range(n):
        for j in range(n):
            if box[i][j] == 1:
                count_1 +=1

    count_2 = 0
    for i in range(n):
        for j in range(n):
            if box[i][j] == 2:
                count_2 += 1

    print("#{} {} {}".format(case+1,count_1, count_2))