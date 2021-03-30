import sys
sys.stdin = open("input (6).txt","r")
#함수
def my_sort(list_1):
    for i in range(len(list_1)):
        for j in range(i+1,len(list_1)):
            if list_1[i] > list_1[j]:
                list_1[i], list_1[j] = list_1[j], list_1[i]
    return list_1

case_num = int(input())
for case in range(case_num):
    box = []
    n=9
    for i in range(n):
        box.append(list(map(int,input().split( ))))
    check_box = []
    for i in range(1,n+1):
        check_box.append(i)
    ans = 1

    for i in range(n):  #행검사
        row_box= []
        for j in range(n):
            row_box.append(box[i][j])
        row_box = my_sort(row_box)
        if row_box != check_box:
            ans = 0
            break

    if ans == 0:
        print("#{} {}".format(case + 1, ans))

        continue

    for i in range(n):  #열검사
        col_box= []
        for j in range(n):
            col_box.append(box[j][i])
        col_box = my_sort(col_box)
        if col_box != check_box:
            ans = 0
            break

    if ans == 0:
        print("#{} {}".format(case + 1, ans))

        continue

    small_n = 3
    for large_x in range(0,n,3):
        if ans ==0:
            break
        for large_y in range(0,n,3):
            nemo = []
            x = large_x
            y= large_y
            for x in range(small_n):
                for y in range(small_n):
                    nemo.append(box[x][y])
            nemo = my_sort(nemo)
            if nemo != check_box:
                ans =0
                break


    print("#{} {}".format(case+1,ans))


