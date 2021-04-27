import sys
sys.stdin = open("1.txt","r")

def position_queen(idx,col,visited):
    global count
    # 마지막 계단에 도달시 count +=1
    if idx == n-1:
        count +=1

    else:
        # visited를 visited_2로 초기화
        visited_2= []
        for i in range(len(visited)):
            visited_2.append(list(visited[i]))

        # 백트래킹 검사
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
        #모든 백트래킹을 통과한 사람에 한해서 다음열로 진출
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
