import sys
sys.stdin = open("sample_input (3).txt","r")

#함수
def find_loca(a):  #문자열 a가 어디 위치하고 있는지 알려준다
    for i in range(n):
        for j in range(n):
            if box[i][j] == a:
                loca =  i, j

    return loca

#본문<-------------------->
case_num = int(input())  #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    n = int(input())  #n*n행렬
    box = []  #인풋박스
    for i in range(n):
        temp = list(input())
        box.append(temp)

    # 노드 부여 및 노드 이어짐 판별
    delta = [[1,0], [0,1], [-1,0], [0,-1]]  #좌표이동
    my_box = []  #좌표박스
    for i in range(n):
        for j in range(n): #모든좌표에 대해서
            x = i
            y = j
            if box[x][y] == '1':  #막힌 곳은 이어져있어도 의미 없으니 패스한다.
                continue
            for k in range(4):  #현재 좌표에 대해서 동서남북 델타이동
                temp_x = x + delta[k][0]
                temp_y = y + delta[k][1]
                if temp_x < 0 or temp_y < 0 or temp_x > n-1 or temp_y > n-1 or box[temp_x][temp_y] == '1':
                    continue  #델타가 범위를 벗어나거나 그 곳이 막힌 벽이라면 무시한다.
                else:
                    node_1 = n*x+ y
                    node_2 = n*temp_x +temp_y
                    if node_1 <= node_2:
                        my_box.append([node_1, node_2])  #고유한 넘버들로 이어준다

    new_box = [[0]*(n**2) for _ in range(n**2)]
    for i in range(len(my_box)):
        new_box[my_box[i][0]][my_box[i][1]] = 1  # 그 부분의 좌표를 이어준다
        new_box[my_box[i][1]][my_box[i][0]] = 1  # 시작위치를 모르니 양방향성으로 설정한다

    # 시작점과 종료점 찾기
    i, j = find_loca('2')
    s = n * i + j
    i, j = find_loca('3')
    g = n * i + j

    # 출입체크용 visted:
    visited = [False] * (n**2)

    # 기초 설정
    stack = []  # stack
    stack.append(s)  # s값, 최초값 삽입

    # dfs 구현
    while len(stack) > 0:
        check = stack.pop()  # 스택의 맨위를 살핀다
        if visited[check] == True:  # 트루면 방문하지 않는다.
            pass
        else:
            s = check
            visited[s] = True  # False면 방문한다
            for i in range(n**2):  # 행의 모든 원소에 대해
                if visited[i] == False and new_box[s][i] == 1:  # 방문한적이 없고, 그 지점값이 1이라면
                    stack.append(i)  # 스택에 추가한다!

    if visited[g]:
        print("#{} {}".format(case+1, 1)) #모든 식이 종료된 뒤, g값이 True라면 1출력
    else:
        print("#{} {}".format(case + 1, 0))