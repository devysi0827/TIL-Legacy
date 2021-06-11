import sys
sys.stdin = open("1.txt","r")

# 0. 기본 인풋
computer_num = int(input())
edge_num = int(input())

# 1. 간선 입력받기, 간선 1을 기준으로 작은 수 정렬
graph = [[0]*(computer_num+1) for _ in range(computer_num+1)]
for _ in range(edge_num):
    x, y = map(int, input().split())
    graph[x][y], graph[y][x] = 1, 1

# 2. 바이러스체크 만들기, 1번 감염시키기
computers_virus = [False]*(computer_num+1)
computers_virus[1] = True

# 3. 중복방지 visited 만들기
visited = [False]*(computer_num+1)

# 4. 감염전파
stack = []
stack.append(1)

while stack:
    now_num = stack.pop()
    for i in range(computer_num+1):
        if graph[now_num][i] == 1 and visited[i] == False:
            stack.append(i)
            computers_virus[i] = True
            visited[i] = True

print(computers_virus.count(True)-1)

