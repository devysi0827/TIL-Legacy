import sys
sys.stdin = open("1.txt","r")

#함수
def get_cnt(a, b):
    cnt = 0
    for i in range(8):
        if i% 2 == 0:
            check = box[a][b]  #맨위를 기준으로 한다 # black -1
        else:
            check = box[a][b] * -1 #w white
        for j in range(8):
            if box[a+i][b+j] != check :  #기준과 다르면 cnt +=1 -1 check -1
                cnt +=1
            check *= -1  #색이 바뀌므로 -1을 곱한다. 1(white) -1(black) 1

    # cnt 34(검은거)  30(하얀색)
    if cnt >= 64 - cnt:
        return 64-cnt
    else:
        return cnt  # 둘중 작은 값 리턴


#본문<-------------------->
# 인풋처리
n, m = map(int, input().split( ))
box = []
for i in range(n):
    box.append(list(input()))

# [bwbwwwbwbw] [bwbwbwbw] .....

# 숫자로 바꾸기
for i in range(n):
    for j in range(m):
        if box[i][j] == 'W':
            box[i][j] =1
        else:
            box[i][j] = -1

[-11 -1 1-1-11111] [1-1-1-1-111111]

minimum = 8*8  #최대 칠하는 개수는 8*8

for i in range (0, n-7):
    for j in range(0, m-7):
        change = get_cnt(i, j)  #칠하는 개수를 구하는 함수
        if minimum > change:
            minimum = change

print(minimum)

# print("#{} {}".format(case+1,answer))