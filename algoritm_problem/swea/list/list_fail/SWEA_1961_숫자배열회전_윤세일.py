import sys
sys.stdin = open("input (3).txt","r")

#함수
def get_move(x,y):
    if x <= y:
        small = x
        large = y
    else:
        large = x
        small = y

    if n-small >= large:
        check = small
    else:
        check = n-large-1

    move = n-1-check*2

    return move
def move_box(box_name,x,y):
    vector = [[0,1], [1,0], [0,-1],[-1,0]]

    limit = n-1
    move = get_move(x,y)
    dirertion =0

    num = box[x][y]
    while move >0:
        temp_x = x + vector[dirertion][0]
        temp_y = y + vector[dirertion][1]
        if temp_x > limit or temp_x <0 or temp_y> limit or temp_y<0:
            dirertion = (dirertion+1)%4
            continue
        x = x + vector[dirertion][0]
        y = y + vector[dirertion][1]
        move = move - 1

    box_name[x][y] = num

#본문<-------------------->
case_num = 1  #최초반복횟수
int(input())
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    n = int(input())
    box = []
    for i in range(n):
        temp = list(map(int,input().split( )))
        box.append((temp))

    box_name = [[0]*n for _ in range(n)]

    vector = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    dirertion = 0
    x = 0
    y = 0
    # move_box(box_name, x, y)
    for i in range(1,n**2+1):
        move_box(box_name, x, y)
        if i == n**2:
            break
        while 1:
            temp_x = x + vector[dirertion][0]
            temp_y = y + vector[dirertion][1]
            if temp_x > n-1 or temp_x < 0 or temp_y > n-1 or temp_y < 0 or box_name[temp_x][temp_y] != 0:
                dirertion = (dirertion + 1) % 4
                continue
            x = x + vector[dirertion][0]
            y = y + vector[dirertion][1]
            break
            # move_box(box_name, x, y)



    print(box_name)


