import sys
sys.stdin = open("input.txt","r")

#함수
def coloring(start_x,end_x,start_y,end_y):
    for i in range(start_x,end_x+1):
        for j in range(start_y,end_y+1):
            check_box[i][j] =1
    return
#본문<-------------------->
case_num = int(input())  #최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    n = int(input())
    box = []
    check_box = [[0]*n for _ in range (n)]
    for _ in range(n):
        box.append(list(map(int,input().split( ))))
    ans = []

    for i in range(n):
        for j in range(n):
            temp_i = i
            temp_j = j
            if box[temp_i][temp_j] and check_box[temp_i][temp_j] == 0:
                while box[temp_i][temp_j]:
                    temp_j += 1
                    if temp_j == n:
                        break
            else:
                continue

            temp_j -=1
            if box[temp_i][temp_j] and check_box[temp_i][temp_j] == 0:
                while box[temp_i][temp_j]:
                    temp_i += 1
                    if temp_i == n:
                        break
            temp_i -=1

            coloring(i,temp_i,j,temp_j)
            ans.append([temp_i-i+1,temp_j-j+1])
            ans.sort()

    for i in range(len(ans)):
        small = ans[i][0] * ans[i][1]
        for j in range(i+1,len(ans)):
            new =  ans[j][0] * ans[j][1]
            if small > new:
                ans[i],ans[j] = ans[j],ans[i]
                small = new
            elif small == new:
                if ans[j][0] < ans[i][0]:
                    ans[i], ans[j] = ans[j], ans[i]
                    small = new

    answer = []
    for i in ans:
        for j in i:
            answer.append(j)


    print("#{} {} ".format(case+1,len(ans)), end='')
    print(*answer)







    # print("#{} {}".format(case+1,answer))
