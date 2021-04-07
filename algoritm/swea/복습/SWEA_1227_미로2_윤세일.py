from _collections import deque
import sys
sys.stdin = open("1.txt","r")

def find_x(num):
    for i in range(100):
        for j in range(100):
            if box[i][j] == num:
                xy = [i,j]
                return xy

for tc in range(10):
    input()
    n = 100
    box = []
    for i in range(n):
        temp = list(map(int,input()))
        box.append(temp)

    s = find_x(2)
    e = find_x(3)
    check_box = [[0]*n for _ in range(n)]
    dx = [1,0,0,-1]
    dy = [0,1,-1,0]
    queue = deque()
    queue.append(s)
    check_box[s[0]][s[1]] ==1
    check = 0

    while len(queue) > 0:
        xy = queue.popleft()
        x = xy[0]
        y = xy[1]
        if check == 1:
            break

        for i in range(4):
            temp_x = x + dx[i]
            temp_y = y + dy[i]

            if temp_x >= 0 and temp_x < n and temp_y >= 0 and temp_y < n and box[temp_x][temp_y] != 1 and check_box[temp_x][temp_y] == 0:
                check_box[temp_x][temp_y] =1
                queue.append([temp_x,temp_y])

                if temp_x == e[0] and temp_y == e[1]:
                    check =1
                    break

    print('#{} {}'.format(tc + 1, check))

