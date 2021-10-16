import sys
sys.stdin = open("1.txt","r")


def mapping_sum(i,j) :
    stack = [[i,j]]
    box[i][j] = 0
    vector = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
    while stack:
        center = stack.pop()
        for k in range(len(vector)):
            now_x = center[0] + vector[k][0]
            now_y = center[1] + vector[k][1]
            if now_x >= 0 and now_x < m and now_y >=0 and now_y< n and box[now_x][now_y]==1:
                box[now_x][now_y] = 0
                stack.append([now_x,now_y])



while 1 :
    n,m = list(map(int,input().split()))
    if n == 0 and m==0:
        break
    box= []
    count = 0
    for i in range(m):
        temp_arr = list(map(int, input().split()))
        box.append(temp_arr)

    for i in range(m):
        for j in range(n):
            if box[i][j] ==1:
                mapping_sum(i,j)
                count +=1
    print(count)