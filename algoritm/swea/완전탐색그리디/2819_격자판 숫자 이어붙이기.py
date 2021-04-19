import sys
from _collections import deque
sys.stdin = open("1.txt","r")

def dfs_count_dis(i,j,idx,num):
    if idx ==6:
        if num not in total_list:
            total_list.append(num)

    else:
        stack = []
        now_x = i
        now_y = j
        if idx == 0:
            num += str(box[now_x][now_y])

        for k in range(4):
            temp_x = now_x + dx[k]
            temp_y = now_y + dy[k]
            if temp_x >= 0 and temp_y >= 0 and temp_x < n and temp_y < n:
                stack.append([temp_x,temp_y])

        for m in range(len(stack)):
            now = stack.pop()
            new_num = str(num)
            new_num += str(box[now[0]][now[1]])
            dfs_count_dis(now[0],now[1],idx+1,new_num)

T = int(input())

for tc in range(T):
    # 기본 세팅
    n = 4
    box = []
    for i in range(n):
        box.append(list(map(int,input().split())))

    total_list = []
    num = ''
    dx = [1,0,0,-1]
    dy = [0,1,-1,0]
    for i in range(n):
        for j in range(n):
            dfs_count_dis(i,j,0,num)

    print('#{} {}'.format(tc + 1,len(total_list)))
