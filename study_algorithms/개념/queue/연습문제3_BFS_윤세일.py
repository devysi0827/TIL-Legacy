import sys
sys.stdin = open("input.txt","r")

#  함수
def enque(a):
    global rear
    rear += 1
    queue.append(a)

def deque():
    global front
    front += 1
    return queue.pop(0)

#  본문<-------------------->
n, e = map(int,input().split( ))
box = [[0]*(n+1) for _ in range(n+1)]  # (n+1)*(n+1)행 배열 생성
for i in range(e):
    x, y = map(int,input().split( ))
    box[x][y] = 1
    box[y][x] = 1

#  기초 설정
s = 1
queue = []
rear = -1
front = -1
root = []
visited = [False]*(n+1)  #방문하면 해당위치를 True
enque(s)  #s값, 최초값 삽입

# 풀이
while len(queue) > 0:
    check = deque()  #스택의 맨위를 살핀다
    if visited[check] == True:  #트루면 방문하지 않는다.
        pass
    else:
        s = check
        visited[s] = True  #False면 방문한다
        root.append(s)
        for i in range(n+1):  #행의 모든 원소에 대해
            if visited[i] == False and box[s][i] == 1:  #방문한적이 없고, 그 지점값이 1이라면
                enque(i)  #스택에 추가한다!

print(root)

