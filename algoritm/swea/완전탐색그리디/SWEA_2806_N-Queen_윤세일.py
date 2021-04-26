import sys
sys.stdin = open("1.txt","r")

def position_queen(idx,col,visited):
    global count
    if idx == n-1:
        count +=1
    else:
        visited_2= []
        for i in range(len(visited)):
            visited_2.append(list(visited[i]))
        for i in range(idx+1,n):
            visited_2[i][col] = 1
        for i in range(1,n):
            if idx+i < n and col+i <n:
                visited_2[idx+i][col+i] = 1
            else:
                break
        for i in range(1,n):
            if idx+i < n and col-i >=0:
                visited_2[idx+i][col-i] = 1
            else:
                break

        for i in range(n):
            if visited_2[idx+1][i] == 0:
                position_queen(idx+1, i, visited_2)

T = int(input())
for tc in range(T):
    # 기본 세팅
    n= int(input())
    visited = [[0] * n for _ in range(n)]
    check_list = []
    count = 0
    for i in range(n):
        visited = [[0] * n for _ in range(n)]
        position_queen(0,i,visited)
    print("#{} {}".format(tc + 1, count))
