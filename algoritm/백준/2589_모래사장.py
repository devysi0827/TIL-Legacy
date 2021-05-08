import sys
sys.stdin = open("1.txt","r")

from _collections import deque

n, m = map(int, input().split())

box = []
for i in range(n):
    temp = list(input())
    change =[]
    for j in range(m):
        if temp[j] == 'W':
            change.append(1)
        else:
            change.append(0)
    box.append(change)
    #w == 1 l ==0

# print(box)

#벡터랑 체크박스
dx = [1,0,0,-1]
dy = [0,-1,1,0]
che_box = [[0]*m for _ in range(n)] # 방문체크 박스
dis_box = [[0]*m for _ in range(n)]



maximum = 0 #최댓값

# !?!! ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ(ノへ￣、)(っ °Д °;)っ{{{(>_<)}}}(;´༎ຶД༎ຶ`)
for i in range(n):
    for j in range(m):
        #땅이면 실행
        if box[i][j] == 0:
            queue = deque()
            # 체크박스랑 거리박스 만들기!
            # box === wlwlwlwlwlwl
            # che_box == 방문체크 하는 것
            che_box = [[0] * m for _ in range(n)]
            # 거리저장하는 박스
            dis_box = [[0] * m for _ in range(n)]
            queue.append([i,j])
            che_box[i][j] = 1


            while queue:
                now = queue.popleft()
                now_x = now[0]
                now_y = now[1]

                for k in range(4):
                    temp_x = now_x + dx[k]
                    temp_y = now_y + dy[k]
                    #인덱스 조건을 만족하면
                    if temp_x >= 0 and temp_y >= 0 and temp_x < n and temp_y < m and che_box[temp_x][temp_y] == 0 and box[temp_x][temp_y] != 1:
                        dis_box[temp_x][temp_y] = dis_box[now_x][now_y] + 1
                        # 만약 이 값이 maximum보다 크면 바꾼다
                        if dis_box[temp_x][temp_y] > maximum:
                            maximum = dis_box[temp_x][temp_y]

                        #방문체크하기
                        che_box[temp_x][temp_y] = 1
                        #그곳 추가하기
                        queue.append([temp_x, temp_y])

print(maximum)
