from _collections import deque
import sys
sys.stdin = open("sample_input.txt","r")

def there_is_zero():
    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                return -1
    return None

m, n = map(int,input().split( ))

box = []
for i in range(n):
    box.append(list(map(int, input().split())))

q = deque()
change_count = 0

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append([i,j])
            change_count += 1
            #0의 개수도 미리 세논다면, -> 토마토가 익을때마다 0의 개수를 줄인다!!! 안익은 = 0 break

dx = [1,0,0,-1]
dy = [0,1,-1,0]
day = -1
count = 0


while len(q) >0:
    bottom = q.popleft()
    count +=1
    for i in range(4):
        x= bottom[0]
        y= bottom[1]
        temp_x = x + dx[i]
        temp_y = y + dy[i]
        if temp_x >= 0 and temp_x < n and temp_y>=0 and temp_y< m and box[temp_x][temp_y] == 0:
            box[temp_x][temp_y] = 1
            q.append([temp_x,temp_y])
            box[x][y] = 1

    if count == change_count: #size day1->큐의 길이 day2->큐의 길이 포문을 돈다
        count = 0
        day +=1
        change_count = len(q)

check =  there_is_zero()
if check == -1:
    day = -1

# print(box)
print(day)