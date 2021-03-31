from _collections import deque
import sys
sys.stdin = open("sample_input.txt","r")

def coloring(m):
    zero_count =0
    for i in range(n):
        for j in range(n):
            if box[i][j] <= m:
                new_box[i][j] = 0
                zero_count += 1
    return  zero_count

def reset_new_box():
    new_box = []
    for i in range(n):
        temp = list(box[i])
        new_box.append(temp)
    return new_box

def find_max_height():
    maximum = -1
    for i in range(n):
        line_max = max(box[i])
        if line_max > maximum:
            maximum = line_max
    return  maximum

def find_min_height():
    low = max_height
    for i in range(n):
        line_low = min(box[i])
        if line_low < low:
            low = line_low
    return  low

#본문
n = int(input())

box = []
for i in range(n):
    temp =list(map(int, input().split()))
    box.append(temp)

max_height = find_max_height()
dx = [1,0,0,-1]
dy = [0,1,-1,0]
count = 0
max_count = 0
queue = [] # queue인듯
min_height = find_min_height() -1

for height in range(min_height, max_height+1):
    new_box = reset_new_box()
    zero_count = coloring(height)
    count = 0
    for i in range(n):
        if zero_count == n**2:
            break
        for j in range(n):
            if new_box[i][j] !=0:
                queue = []
                queue.append([i,j])
                new_box[i][j] = 0
                zero_count += 1
                while len(queue) >0:
                    gijoon = queue.pop(0)
                   ##### # new_box[gijoon[0]][gijoon[1]] = 0 -> 시간초과
                    for k in range(4):
                        x = gijoon[0]
                        y = gijoon[1]
                        temp_x = x + dx[k]
                        temp_y = y + dy[k]
                        if temp_x >=0 and temp_x <n and temp_y >=0 and temp_y <n and new_box[temp_x][temp_y] != 0:
                            queue.append([temp_x,temp_y])
                            new_box[temp_x][temp_y] = 0 #통과
                            zero_count += 1

                count +=1

    if count > max_count:
        max_count = count

print(max_count)





