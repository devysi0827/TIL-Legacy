import sys
sys.stdin = open("1.txt","r")


def find_beacho():
    for i in range(m):
        for j in range(n):
            if box[i][j] == 1:
                return [i,j]
    return  [-1,-1]


def dfs(now_i,now_j):
    box[now_i][now_j] = 0
    vector_x = [1,-1,0,0]
    vector_y = [0,0,-1,1]
    for i in range(4):
        now_x = now_i + vector_x[i]
        now_y = now_j + vector_y[i]
        if now_x >= 0 and now_x < m and now_y >=0 and now_y < n and box[now_x][now_y] == 1:
            dfs(now_x,now_y)


repeat = int(input())
for _ in range(repeat):
    n, m, p = list(map(int, input().split()))
    box = [[0]*n for i in range(m)]
    for i in range(p):
        x, y = list(map(int, input().split()))
        box[y][x] = 1

    count = 0
    while 1:
        beacho = find_beacho()
        if beacho[0] == -1:
            break
        else:
            dfs(beacho[0],beacho[1])
            count +=1
    print(count)