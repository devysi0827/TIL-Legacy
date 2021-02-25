import sys
sys.stdin = open("input.txt","r")

#본문<-------------------->
case_num = 10  #최초반복횟수 입력
for case in range(case_num):
    c, e = map(int,input().split( ))
    temp_list = list(map(int,input().split( )))

    x_list =[]
    y_list = []
    for i in range(0,len(temp_list)):
        if i%2:
            y_list.append(temp_list[i])
        else:
            x_list.append(temp_list[i])
    maximum = 0
    v = len(set(x_list))
    box = [[0]*(100) for _ in range(100)]  # (n+1)*(n+1)행 배열 생성
    for i in range(e):
        box[x_list[i]][y_list[i]] = 1  # 그 부분의 좌표를 이어준다

    #기초 설정
    s = 0
    stack = []  #stack
    visited = [False]*(100)  #방문하면 해당위치를 True
    stack.append(s)  #s값, 최초값 삽입
    g = 99

    # 풀이
    while len(stack) > 0:
        check = stack.pop()  #스택의 맨위를 살핀다
        if visited[check] == True:  #트루면 방문하지 않는다.
            pass
        else:
            s = check
            visited[s] = True  #False면 방문한다
            for i in range(100):  #행의 모든 원소에 대해
                if visited[i] == False and box[s][i] == 1:  #방문한적이 없고, 그 지점값이 1이라면
                    stack.append(i)  #스택에 추가한다!

    if visited[g]:
        print("#{} {}".format(case+1, 1)) #모든 식이 종료된 뒤, g값이 True라면 1출력
    else:
        print("#{} {}".format(case + 1, 0))

    # # 기본 인풋을 이용한 박스형성
    # v, e = map(int,input().split( ))  # v: 점 수, e: 간선 수
    # box = [[0]*(v+1) for _ in range(v+1)]  # (n+1)*(n+1)행 배열 생성
    #
    # for i in range(e):
    #     x, y = map(int, input().split())  # x: x좌표, y: y좌표 받음
    #     box[x][y] = 1  #그 부분의 좌표를 이어준다
    # s, g = map(int,input().split( ))  # s: 시작 g: 끝

    # #기본 설정:
    # stack = []  #stack
    # visted = [False]*(v+1)  #방문하면 해당위치를 True
    # stack.append(s)  #s값, 최초값 삽입
    #
    # # 풀이
    # while len(stack) > 0:
    #     check = stack.pop()  #스택의 맨위를 살핀다
    #     if visted[check] == True:  #트루면 방문하지 않는다.
    #         pass
    #     else:
    #         s = check
    #         visted[s] = True  #False면 방문한다
    #         for i in range(v + 1):  #행의 모든 원소에 대해
    #             if visted[i] == False and box[s][i] == 1:  #방문한적이 없고, 그 지점값이 1이라면
    #                 stack.append(i)  #스택에 추가한다!
    #
    # if visted[g]:
    #     print("#{} {}".format(case+1, 1)) #모든 식이 종료된 뒤, g값이 True라면 1출력
    # else:
    #     print("#{} {}".format(case + 1, 0))
