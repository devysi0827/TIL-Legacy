import sys
sys.stdin = open("1.txt","r")
from collections import deque

node_num, edge_num, start = list(map(int,input().split()))

# 0-1 graph 생성
graph = [[0] * (node_num+1) for _ in range(node_num+1)]

# 0-2 edges 입력
for i in range(edge_num):
    edge_1, edge_2 = list(map(int,input().split()))
    graph[edge_1][edge_2] = graph[edge_2][edge_1] = 1

# # 1 bfs
# stack = []
# stack.append(start)
# stack_visited = [False] * (node_num+1)
# stack_visited[start] = True
# stack_road = []
# while stack:
#     now_num = stack.pop()
#     stack_road.append(now_num)
#     for i in range(node_num +1):
#         if graph[now_num][i] ==1 and stack_visited[i] == False:
#             stack_visited[i] = True
#             stack.append(i)
#
# #이건 dfs가 아니야!!
# print(stack_road)

#1 dfs
def dfs_recur(num) :
    global stack_road
    stack_road.append(num)
    for i in range(node_num +1):
        if graph[num][i] ==1 and stack_visited[i] == False:
            stack_visited[i] = True
            dfs_recur(i)

stack_visited = [False] * (node_num+1)
stack_visited[start] = True
stack_road = []
dfs_recur(start)
print(*stack_road)

#2 bfs
q = deque()
q.append(start)
q_visited = [False] * (node_num+1)
q_visited[start] = True
q_road = []
while q:
    now_num = q.popleft()
    q_road.append(now_num)
    for i in range(node_num +1):
        if graph[now_num][i] ==1 and q_visited[i] == False:
            q_visited[i] = True
            q.append(i)
print(*q_road)



