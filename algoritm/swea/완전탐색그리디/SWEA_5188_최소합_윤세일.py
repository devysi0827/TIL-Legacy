import sys, copy
sys.stdin = open("1.txt","r")

def dfs_count_dis(i,j,count,visited):
    count += box[i][j]
    global min_sum
    if count >= min_sum:
        return

    if i == n-1 and j == n-1:
        if count < min_sum:
            min_sum = count
        return

    # visited_two = []
    # for temp_i in range(n):
    #     temp = []
    #     for temp_j in range(n):
    #         temp.append(visited[temp_i][temp_j])
    #     visited_two.append(temp)
    visited_two = copy.deepcopy(visited)
    visited_two[i][j] = 1
    stack = []
    now_x = i
    now_y = j
    for k in range(4):
        temp_x = now_x + dx[k]
        temp_y = now_y + dy[k]
        # if temp_x >= 0 and temp_y >= 0 and temp_x < n and temp_y < n and temp_x>=now_x and temp_y>=now_y and visited_two[temp_x][temp_y] == 0:
        if temp_x >= 0 and temp_y >= 0 and temp_x < n and temp_y < n and visited_two[temp_x][temp_y] == 0:
            stack.append([temp_x,temp_y])

    for i in range(len(stack)):
        dfs_count_dis(stack[i][0],stack[i][1],count,visited_two)

T = int(input())

for tc in range(T):
    # 기본 세팅
    n = int(input())
    box = []
    for i in range(n):
        box.append(list(map(int,input().split())))
    visited = [[0]*n for _ in range(n)]
    min_sum = 0
    for i in range(n):
        min_sum += box[0][i]
        min_sum += box[i][n-1]
    min_sum -= box[0][n-1]
    dx = [1,0,0,-1]
    dy = [0,1,-1,0]
    dfs_count_dis(0,0,0,visited)

    print('#{} {}'.format(tc + 1,min_sum))

