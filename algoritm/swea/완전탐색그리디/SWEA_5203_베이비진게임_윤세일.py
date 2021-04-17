import sys, copy
sys.stdin = open("1.txt","r")

T = int(input())

def check_run_triple(list_1):
    for i in range(len(list_1)-2):
        if list_1[i] == list_1[i+1] and list_1[i+1] == list_1[i+2]:
            return 1
        # elif list_1[i] == list_1[i+1]-1 and list_1[i+1] == list_1[i+2]-1:
        #     return 1
        elif list_1[i] == list_1[i+1]-1:
            if list_1[i+1] == list_1[i+2]-1:
                return 1
            elif list_1[i+1] == list_1[i+2]:
                if list_1[i+2] == list_1[i+3]-1 and i+3 < len(list_1):
                    return 1



for tc in range(T):
    # 기본 세팅
    first = []
    second =[]
    order = list(map(int,input().split()))
    ans = 0
    for i in range(12):
        if i%2 == 0:
            first.append(order[i])
            if i >= 5:
                temp_first = sorted(first)
                check = check_run_triple(temp_first)
                if check:
                    ans =1
                    break
        else:
            second.append(order[i])
            if i >= 5:
                temp_second = sorted(second)
                check = check_run_triple(temp_second)
                if check:
                    ans =2
                    break

    print("#{} {}".format(tc + 1, ans))