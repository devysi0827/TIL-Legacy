

def select_box(idx,box_sum,check_list):
    # 다 뽑아서 정리했다면
    global min_sum
    if idx == n:
        if box_sum < min_sum:
            min_sum = box_sum
    else:
        # print(check_list, end =" ")
        # print(box_sum, end =" ")
        # print(min_sum, end=" ")
        # print(idx)
        for i in range(n):
            if i not in check_list:
                check_list_2 = list(check_list)
                box_sum_2 = int(box_sum)
                check_list_2.append(i)
                box_sum_2 += box[idx][i]
                if box_sum_2 < min_sum:
                    select_box(idx+1, box_sum_2, check_list_2)

T = int(input())
for tc in range(T):
    # 기본 세팅
    n= int(input())
    box = []
    check_list = []
    min_sum = 99999999
    for i in range(n):
        box.append(list(map(int,input().split())))
    select_box(0,0,check_list)
    print("#{} {}".format(tc + 1, min_sum))
