import sys

sys.stdin = open("1.txt","r")

# def dfs_count_dis(i,j,num,stack):
#     now_x = i
#     now_y = j
#
#     for k in range(4):
#         temp_x = now_x + dx[k]
#         temp_y = now_y + dy[k]
#         if temp_x >= 0 and temp_y >= 0 and temp_x < n and temp_y < n and box[temp_x][temp_y] == box[now_x][now_y]+1:
#             stack.append([temp_x,temp_y])
#
#     for m in range(len(stack)):
#         now = stack.pop()
#         stack_new = list(stack)
#         new_num = int(num)
#         new_num +=1
#         dfs_count_dis(now[0],now[1],new_num,stack_new)



T = int(input())

for tc in range(T):
    # 기본 세팅
    n = int(input())
    box = []
    for i in range(n):
        box.append(list(map(int,input().split())))

    max_count = -1
    max_num = -1
    dx = [1,0,0,-1]
    dy = [0,1,-1,0]
    for i in range(n):
        for j in range(n):
            stack = [[i,j]]
            count = 0
            while stack:
                now = stack.pop()
                now_x = now[0]
                now_y = now[1]
                count +=1
                for k in range(4):
                    temp_x = now_x + dx[k]
                    temp_y = now_y + dy[k]
                    if temp_x >= 0 and temp_y >= 0 and temp_x < n and temp_y < n and box[temp_x][temp_y] == box[now_x][
                        now_y] + 1:
                        stack.append([temp_x, temp_y])

            if count > max_count:
                max_count = count
                max_num = box[i][j]
            elif count == max_count:
                if box[i][j] < max_num:
                    max_count = count
                    max_num = box[i][j]

    print('#{} {} {}'.format(tc + 1,max_num, max_count))