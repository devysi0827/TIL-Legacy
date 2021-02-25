import sys
sys.stdin = open("input (6).txt","r")

#함수
case_num = int(input())
for case in range(case_num):
    n = int(input())
    box = []
    for i in range(n):
        temp = list(map(int,input()))
        box.append(temp)

    middle_num = n//2
    minus = -1
    ans= 0

    for i in range(middle_num,-1,-1):
        minus += 1
        for j in range(minus,n-minus):
            ans += box[i][j]

    minus = 0
    for i in range(middle_num+1,n):
        minus += 1
        for j in range(minus,n-minus):
            ans += box[i][j]

    print("#{} {}".format(case+1,ans))
