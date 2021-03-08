import sys
sys.stdin = open("sample_input.txt","r")

#함수
def top(stack):
    top = stack[-1]
    return top

# 기본인풋으로 이루어진 박스 만들기
n, m = map(int,input().split( ))
box = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    x, y = map(int,input().split( ))
    box[x][y] = 1
    box[y][x] = 1

# 출입체크용 visted:
visited = [False] * m

# 최초 기본 설정
start = 1
stack = []
my_root = []
my_root.append(start)


# 최초의 1회 시도
for i in range(m):
    if box[start][i] == 1:
        stack.append(i)

# 이후 반복
while len(stack) > 0:
    check = top(stack)
    if visited[check] == True:
        stack = stack[0:-1]
    else:
        start = top(stack)
        visited[start] = True
        my_root.append(start)


        for j in range(m):
            if box[start][j] == 1:
                if visited[j] == False:
                    stack.append(j)

print(my_root)
