import sys

sys.stdin = open("1.txt","r")

T = int(input())

for tc in range(T):
    # 기본 세팅
    n, m = map(int,input().split())
    box = []
    for i in range(n):
        temp_tas, temp_cal = map(int,input().split())
        box.append([temp_tas,temp_cal])
    max_tas = 0

    for i in range(1 << n):
        tas_sum = 0
        cal_sum = 0
        for j in range(n + 1):
            if i & (1 << j):
                cal_sum += box[j][1]
                tas_sum += box[j][0]
                if cal_sum >= m:
                    break

            if tas_sum > max_tas:
                max_tas = tas_sum


    print("#{} {}".format(tc+ 1, max_tas))
