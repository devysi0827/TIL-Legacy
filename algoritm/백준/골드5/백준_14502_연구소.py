import sys
sys.stdin = open("1.txt","r")
from collections import deque
from itertools import permutations
import copy

# 0. 기본 인풋
n,m = list(map(int,input().split()))
box = []
for i in range(n):
    box.append(list(map(int,input().split())))

# 1. 바이러스 위치 찾기
virus_loca = []
def find_virus():
    for i in range(n):
        for j in range(m):
            if box[i][j] == 2:
                virus_loca.append([i,j])
find_virus()

# 2. bfs 함수 짜기
vector = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(xy):
    q = deque()
    q.append(xy)
    while q:
        temp = q.popleft()
        x = temp[0]
        y = temp[1]
        for repeat in range(4):
            now_x = x + vector[repeat][0]
            now_y = y + vector[repeat][1]

            if now_x >= 0 and now_x < n and now_y >=0 and now_y < m and temp_box[now_x][now_y] == 0:
                temp_box[now_x][now_y] = 2
                q.append([now_x,now_y])

# for i in range(len(virus_loca)):
#     bfs(virus_loca[i])


# 3. 안전지역 세기
def find_safearea(my_box):
    safearea = 0
    for i in range(n):
        for j in range(m):
            if my_box[i][j] == 0:
                safearea +=1
    return safearea


# 4. 함수본문 벽세우기
wall_area = []
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            wall_area.append([i,j])
wall_comb = list(permutations(wall_area,3))
# print(wall_comb)
# print(len(wall_comb))
safe_areas = []

for i in range (len(wall_comb)):
    temp_box = copy.deepcopy(box)
    temp_wall = wall_comb[i]
    temp_box[temp_wall[0][0]][temp_wall[0][1]] = 1
    temp_box[temp_wall[1][0]][temp_wall[1][1]] = 1
    temp_box[temp_wall[2][0]][temp_wall[2][1]] = 1
    for k in range(len(virus_loca)):
        bfs(virus_loca[k])
    this_safearea = find_safearea(temp_box)
    safe_areas.append(this_safearea)
# print(safe_areas)
print(max(safe_areas))



