import sys
sys.stdin = open("sample_input.txt","r")

#함수
def dfs(w):
    visited[w] = True #방문하였으므로 True

    for i in range(v+1):  # 행의 모든 원소에 대해
        if visited[i] == False and box[w][i] == 1:  # 방문한적이 없고, 그 지점값이 1이라면 재귀함수를 실행한다.
            dfs(i)

#본문<-------------------->
case_num = int(input())  #최초반복횟수 입력
for case in range(case_num):

    # 기본 인풋을 이용한 박스형성
    v, e = map(int,input().split( ))  # v: 점 수, e: 간선 수
    box = [[0]*(v+1) for _ in range(v+1)]  # (n+1)*(n+1)행 배열 생성

    for i in range(e):
        x, y = map(int, input().split())  # x: x좌표, y: y좌표 받음
        box[x][y] = 1  #이어진 부분의 좌표를 1로,
    s, g = map(int,input().split( ))  # s: 시작 g: 끝

    # 풀이:
    visited = [False] * (v+1)  # 방문하면 해당위치를 True로 바꿀 함수 생성
    dfs(s)

    if visited[g]:
        print("#{} {}".format(case+1, 1))  #모든 식이 종료된 뒤, g값이 True라면 1출력
    else:
        print("#{} {}".format(case + 1, 0))  #아니라면 0 출력

