import sys
sys.stdin = open("1.txt","r")

def select_box(idx,box_sum,check_list):
    # 다 뽑아서 정리했다면
    global max_sum
    if idx == n:
        if box_sum > max_sum:
            max_sum = box_sum
    else:
        # print(check_list, end =" ")
        # print(box_sum, end =" ")
        # print(min_sum, end=" ")
        # print(idx)
        for i in range(n):
            if i not in check_list:
                check_list_2 = list(check_list)
                box_sum_2 = float(box_sum)
                check_list_2.append(i)
                box_sum_2 *= box[idx][i]/100
                if box_sum_2 > max_sum:
                    select_box(idx+1, box_sum_2, check_list_2)

T = int(input())
for tc in range(T):
    # 기본 세팅
    n= int(input())
    box = []
    check_list = []
    max_sum = 0
    for i in range(n):
        box.append(list(map(int,input().split())))
    select_box(0,1,check_list)
    max_sum = max_sum*100
    print("#{} {:6f}".format(tc + 1, max_sum))
