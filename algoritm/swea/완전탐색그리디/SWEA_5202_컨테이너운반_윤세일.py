import sys
sys.stdin = open("1.txt","r")


T = int(input())

for tc in range(T):
    # 기본 세팅
    trash = input()
    sorpo_list = sorted(list(map(int,input().split())))[::-1]
    truck_list = sorted(list(map(int,input().split())))[::-1]

    i = 0
    index = 0
    weight = 0
    while i<len(sorpo_list) and index < len(truck_list):
        if truck_list[index] >= sorpo_list[i]:
            weight += sorpo_list[i]
            index +=1
            i +=1
        else:
            i +=1

    print('#{} {}'.format(tc + 1,weight))