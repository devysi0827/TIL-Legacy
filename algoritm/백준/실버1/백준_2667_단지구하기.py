import sys
sys.stdin = open("1.txt","r")

#함수
def sum_second_list(box):   #이차원 배열의 모든 값의 합을 계산합니다.
    total_sum = 0
    for i in range(n):
        total_sum += sum(box[i])
    return  total_sum

#본문<-------------------->
# 기본 인풋
n = int(input())
box = [] #이차우너배열
for i in range(n):
    box.append(list(map(int,input())))

# 기본 설정
sum_box = sum_second_list(box)  #break문
check_box = [[0]*n for _ in range(n)]  #visited
stack = []  #stack
delta = [[1,0], [-1,0], [0,1], [0,-1]]  #delta
danjis = []  #단지들


#풀이
for i in range(n):
    sum_check_box =sum_second_list(check_box)  #chck_box의 총합을 구합니다
    if sum_box == sum_check_box:  #같다면 더 할 필요없이 정지합니다
        break

    for j in range(n):
        if box[i][j] == 1 and check_box[i][j] == 0:  #1이면서 방문하지 않았다면,
            check_box[i][j] = 1  #방문표시를 하고
            stack.append(i*n+j)  #스택에 추가합니다
            cnt = 1  #최초 단지이므로 1을 값으로 합니다.

            while len(stack) >0:  #스택이 있는한 반복합니다.
                number = stack.pop()  #stack에 있는 값을 꺼냅니다
                now_i = int(number//n)  #몫은 i좌표
                now_j = int(number%n)  #나머지는 j좌표가 됩니다
                for k in range(4):  #달팽이 4방향 검사
                    di = now_i+ delta[k][0]
                    dj = now_j +delta[k][1]
                    if di >=0 and di < n and dj<n and dj>=0 and box[di][dj] == 1 and check_box[di][dj] == 0 :  #조건 미충족시 탈락
                        stack.append(di*n+dj)  #맞다면 추가를 하고
                        check_box[di][dj] = 1  #방문체크
                        cnt += 1  #단지 수 +1

            danjis.append(cnt) #끝나면 단지에 추가합니다

danjis.sort()  #정렬합니다

#<-------------------출력------------------->
print(len(danjis))
for i in range(len(danjis)):
    print(danjis[i])





