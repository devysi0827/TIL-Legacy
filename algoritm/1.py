import sys
sys.stdin = open("5.txt","r")

def get_loca(num):
    return_box = []
    for i in range(n):
        for j in range(n):
            if box[i][j] == num:
                return_box.append([i,j])
    return return_box

def cal_move(person,exit):
    x = person[0]
    y = person[1]
    exit_x = exit[0]
    exit_y = exit[1]
    return abs(exit_x-x) + abs(exit_y-y)

repeats = int(input())
for repeat in range(repeats) :
    box = []
    n = int(input())
    for i in range(n):
        temp_box = list(map(int,input().split()))
        box.append(temp_box)
    # 사람들, 출구 위치 정보 받기
    exits = get_loca(2)
    people = get_loca(1)

    # bit화
    bits = []
    total_num = 2 ** len(people)
    max_num = len(bin(total_num-1)[2:])
    for i in range(total_num):
        bit = bin(i)[2:]
        if len(bit) < max_num:
            while len(bit) <max_num:
                bit = '0' +bit
        bits.append(bit)

    min_exit_cnt = 99999999
    for i in range(len(bits)):
        first_exit = [0] * ((2 * n) + len(people) + 10)
        second_exit = [0] * ((2 * n) + len(people) + 10)
        bit = bits[i]
        exit_cnt = 0
        for j in range(len(bit)):
            if bit[j] == '0':
                move = cal_move(people[j],exits[0])
                if first_exit[move+1] == 0:
                    first_exit[move+1] = 1
                    if move+1 > exit_cnt:
                        exit_cnt = move+1
                else:
                    while 1:
                        move += 1
                        if first_exit[move] == 0:
                            first_exit[move] = 1
                            if move > exit_cnt:
                                exit_cnt = move
                            break

            else:
                move = cal_move(people[j],exits[1])
                if second_exit[move+1] == 0:
                    second_exit[move+1]  = 1
                    if move+1 > exit_cnt:
                        exit_cnt = move+1
                else:
                    while 1:
                        move += 1
                        if second_exit[move] == 0:
                            second_exit[move] = 1
                            if move > exit_cnt:
                                exit_cnt = move
                            break

        if exit_cnt < min_exit_cnt:
            min_exit_cnt = exit_cnt
    print('#{} {}'.format(repeat+1,min_exit_cnt))

